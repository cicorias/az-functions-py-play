import logging
import datetime

import azure.functions as func


def main(req: func.HttpRequest, outputEvent: func.Out[func.EventGridOutputEvent], outputEvent2: func.Out[func.QueueMessage]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        outputEvent.set(
            func.EventGridOutputEvent(
                id="test-id",
                data={"tag1": "value1", "tag2": "value2"},
                subject="test-subject",
                event_type="test-event-1",
                event_time=datetime.datetime.utcnow(),
                data_version="1.0"))

        outputEvent2.set(func.QueueMessage(id="abc", body="the body of message", pop_receipt="none"))

        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.",
                                 status_code=202)
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
