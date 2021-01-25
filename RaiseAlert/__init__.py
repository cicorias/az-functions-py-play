import logging
import datetime
import json
from typing import Dict, Iterator, List, Union
import uuid

import azure.functions as func


def main(req: func.HttpRequest, outputEvent,
         outputEvent2: func.Out[func.QueueMessage]) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    try:
        content = req.get_json()

        outputEvent.set(get_events(content))
        # outputEvent2.set(get_events(content))

        if not content:
            raise Exception("No request content")

        return func.HttpResponse("Hello, This HTTP triggered function executed successfully.",
                                 status_code=202)
    except ValueError:
        pass
    except:
        return create_response("No request content, no events will be created")


def get_events(requestJson: List[Dict]) -> Union[Iterator[func.EventGridOutputEvent], Iterator[func.QueueMessage]]:

    try:
        jsonBody = json.loads(requestJson)
    except:
        jsonBody = requestJson
    finally:
        if not jsonBody:
            jsonBody = list()

    logging.info(f"jsonBody: {jsonBody}")
    if jsonBody:
        for event in jsonBody:
            if event: # is this needed?
                logging.info(f"event {event}")
                yield func.EventGridOutputEvent(
                    id=str(uuid.uuid4()),
                    subject=event.get("Subject", "Unknown"),
                    data=event,
                    event_type=event.get("EventType", "Unknown"),
                    event_time=datetime.datetime.now(),
                    data_version=2.0,
                )


def create_response(msg, status_code=200, **kwargs):
    return func.HttpResponse(msg, status_code=status_code, **kwargs)
