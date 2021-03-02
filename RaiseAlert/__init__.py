from dataclasses import dataclass
import logging
import sys
import azure.functions as func
# from packaging import version
from typing import Generator, List
import uuid
from datetime import datetime

logger = logging.getLogger()


@dataclass
class EventPayload:
    """ This is the event structure we get from ASA via the Functions HTTP binding """
    CorrelationId: str = ''
    Timestamp: str = ''
    NumberOfCauses: int = 0
    Subject: str = ''
    EventType: str = ''


def main(req: func.HttpRequest, outputEvent: func.Out[List[func.EventGridOutputEvent]]) -> func.HttpResponse:
    # if sys.version.parse(sys.version) < sys.version.parse("3.7.4"):
    #     logger.error('function app is not at version 3.7.4')

    logger.info(f'python version: {sys.version}')

    try:
        content = req.get_json()
        if not content:
            raise Exception("No request content")
    except:
        return create_response("No request content, no events will be created")

    try:
        rv = get_events(content)
        outputEvent.set(list(rv))
        logger.info("event grid output event set...")

    except Exception as e:
        logger.exception(f"Unable to publish event to the event grid. {e}")
        return create_response("Error publishing event", status_code=500)

    logger.info("Message submitted to EventGrid...")
    return create_response("Message submitted successfully. eee")


def create_response(msg: str, status_code: int = 200):
    return func.HttpResponse(msg, status_code=status_code)


def get_events(requestJson: List[EventPayload]) -> Generator[func.EventGridOutputEvent, None, None]:
    """ Given a Stream Analytics event, create an iterable of EventGrid messages"""

    if requestJson:
        for event in requestJson:
            if event:
                yield asa_event_to_eventgrid_message(EventPayload(**event))


def asa_event_to_eventgrid_message(asa_event: EventPayload) -> func.EventGridOutputEvent:
    logging.info("event grid output", extra={"correlationId": asa_event.CorrelationId})
    return func.EventGridOutputEvent(
        id=str(uuid.uuid4()),
        subject=asa_event.get("Subject"),
        data={"data": asa_event},
        event_type=asa_event.get("EventType", "Unknown"),
        event_time=datetime.now(),
        data_version="2.0"
    )
