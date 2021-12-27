def webhook_event_callback(event):
    """ Dispatches the event to celery for processing. """
    import tasks
    # Ansychronous hand-off to celery so that we can continue immediately
    tasks.process_webhook_event(event.pk)
