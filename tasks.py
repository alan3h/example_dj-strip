from djstripe.models import WebhookEventTrigger
from stripe.error import StripeError
from django import db
db.connections.close_all()


def process_webhook_event(pk):
    """ Processes events from Stripe asynchronously. """
    print(f"Processing Stripe event: {pk}")
    try:
        # get the event
        obj = WebhookEventTrigger.objects.get(pk=pk)
        # process the event.
        # internally, this creates a Stripe WebhookEvent Object and invokes the respective Webhooks
        
        event = obj.process()
        print(event.type, '<== what event this, and save the type event')
    except StripeError as exc:
        print(f"Failed to process Stripe event: {pk}. Retrying in 60 seconds.")
        #raise self.retry(exc=exc, countdown=60)  # retry after 60 seconds
    except WebhookEventTrigger.DoesNotExist as exc:
        # This can happen in case the celery task got executed before the actual model got saved to the DB
        #raise self.retry(exc=exc, countdown=10)  # retry after 10 seconds
        print(f"Failed to process Stripe event: {pk}. Retrying in 60 seconds.")

    return event.type or "Stripe Event Processed"