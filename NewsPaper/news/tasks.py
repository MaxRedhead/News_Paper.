import datetime
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import *
from NewsPaper import settings
from .signals import send_mail

today = datetime.datetime.now()
last_week = today - datetime.timedelta(days=7)
last_posts = Post.objects.filter(dateCreation__gte=last_week)
categories = set(last_posts.values_list('category', flat=True))
subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers', flat=True))


@shared_task
def weekly_sending(preview, pk, title, subscribers):
    html_content = render_to_string(
        'daily_post.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news{pk}',
        }
    )

    message = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,

    )

    message.attach_alternative(html_content, 'text/html')
    message.send()


@shared_task
def sending_about(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_mail.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news{pk}',
        }
    )

    message = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,

    )

    message.attach_alternative(html_content, 'text/html')
    message.send()


@shared_task
@receiver(m2m_changed, sender=PostCategory)
def malling(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers = category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_mail(instance.preview(), instance.pk, instance.title, subscribers)





