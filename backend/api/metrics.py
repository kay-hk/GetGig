from prometheus_client import Counter, Gauge
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Ticket, Festival

# Basic counters
user_signup_counter = Counter(
    'getgig_user_signups_total',
    'Total number of user signups'
)

ticket_purchase_counter = Counter(
    'getgig_ticket_purchases_total',
    'Total number of ticket purchases',
    ['ticket_type']
)

# Gauges for current state
active_users_gauge = Gauge(
    'getgig_active_users',
    'Number of active users'
)

@receiver(post_save, sender=User)
def track_user_signup(sender, instance, created, **kwargs):
    if created:
        user_signup_counter.inc()
        active_users_gauge.inc()

@receiver(post_save, sender=Ticket)
def track_ticket_purchase(sender, instance, created, **kwargs):
    if created:
        ticket_purchase_counter.labels(
            ticket_type=instance.ticket_type_id.ticket_type_name
        ).inc(instance.ticket_quantity)