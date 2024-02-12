from typing import Any, Dict, Iterator, Optional, Union

import dlt

from ...models.list_events_event_type import ListEventsEventType
from ...models.list_events_webhook_status import ListEventsWebhookStatus
from ...security.basic_auth import BasicAuth
from ...types import UNSET, Unset
from ...utils import get_pages


def _get_kwargs(
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, str] = UNSET,
    start_time: Union[Unset, None, int] = UNSET,
    end_time: Union[Unset, None, int] = UNSET,
    webhook_status: Union[Unset, None, ListEventsWebhookStatus] = UNSET,
    event_type: Union[Unset, None, ListEventsEventType] = UNSET,
    chargebee_request_origin_device: Union[Unset, str] = UNSET,
    chargebee_request_origin_user: Union[Unset, str] = UNSET,
    chargebee_request_origin_user_encoded: Union[Unset, str] = UNSET,
    chargebee_request_origin_ip: Union[Unset, str] = UNSET,
    base_url: str = dlt.config.value,
    credentials: BasicAuth = dlt.secrets.value,
) -> Dict[str, Any]:
    url = "{}/events".format(base_url)

    base_params: Dict[str, Any] = dict(cookies={}, headers={}, params={})
    base_params.update(credentials.to_http_params())
    headers = base_params["headers"]

    cookies = base_params["cookies"]

    params = base_params["params"]

    if not isinstance(chargebee_request_origin_device, Unset):
        headers["chargebee-request-origin-device"] = chargebee_request_origin_device

    if not isinstance(chargebee_request_origin_user, Unset):
        headers["chargebee-request-origin-user"] = chargebee_request_origin_user

    if not isinstance(chargebee_request_origin_user_encoded, Unset):
        headers["chargebee-request-origin-user-encoded"] = chargebee_request_origin_user_encoded

    if not isinstance(chargebee_request_origin_ip, Unset):
        headers["chargebee-request-origin-ip"] = chargebee_request_origin_ip

    params["limit"] = limit

    params["offset"] = offset

    params["start_time"] = start_time

    params["end_time"] = end_time

    json_webhook_status: Union[Unset, None, str] = UNSET
    if not isinstance(webhook_status, Unset):
        json_webhook_status = webhook_status.value if webhook_status else None

    params["webhook_status"] = json_webhook_status

    json_event_type: Union[Unset, None, str] = UNSET
    if not isinstance(event_type, Unset):
        json_event_type = event_type.value if event_type else None

    params["event_type"] = json_event_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "params": params,
    }


@dlt.resource(table_name="events")
def list_events(
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, str] = UNSET,
    start_time: Union[Unset, None, int] = UNSET,
    end_time: Union[Unset, None, int] = UNSET,
    webhook_status: Union[Unset, None, ListEventsWebhookStatus] = UNSET,
    event_type: Union[Unset, None, ListEventsEventType] = UNSET,
    chargebee_request_origin_device: Union[Unset, str] = UNSET,
    chargebee_request_origin_user: Union[Unset, str] = UNSET,
    chargebee_request_origin_user_encoded: Union[Unset, str] = UNSET,
    chargebee_request_origin_ip: Union[Unset, str] = UNSET,
    base_url: str = dlt.config.value,
    credentials: BasicAuth = dlt.secrets.value,
    data_json_path: Optional[str] = "list",
) -> Iterator[Any]:
    r"""List events

     Retrieves list of events.


    Args:
        limit (Union[Unset, None, int]):  Default: 10.
        offset (Union[Unset, None, str]):
        start_time (Union[Unset, None, int]):
        end_time (Union[Unset, None, int]):
        webhook_status (Union[Unset, None, ListEventsWebhookStatus]):
        event_type (Union[Unset, None, ListEventsEventType]):
        chargebee_request_origin_device (Union[Unset, str]): The device from which the customer
            has made the request
             Example: Android.
        chargebee_request_origin_user (Union[Unset, str]): The email address of your
            customer/user. Use this when the email address has only ASCII characters.
             Example: user@example.com.
        chargebee_request_origin_user_encoded (Union[Unset, str]): The Base64-encoded email
            address of your customer/user. Use this if the email address has UTF-8 characters. When
            this header is provided, the header \`chargebee-request-origin-user\` is ignored.
             Example: dXNlci7QutCy0ZbRgtC+0YfQutCwQGV4YW1wbGUuY29t.
        chargebee_request_origin_ip (Union[Unset, str]): The IP address of the customer where the
            request originated
             Example: 192.168.1.2.


    Returns:
        Iterator of 'ListEventsResponse200ListItem' items
    """

    kwargs = _get_kwargs(
        base_url=base_url,
        credentials=credentials,
        limit=limit,
        offset=offset,
        start_time=start_time,
        end_time=end_time,
        webhook_status=webhook_status,
        event_type=event_type,
        chargebee_request_origin_device=chargebee_request_origin_device,
        chargebee_request_origin_user=chargebee_request_origin_user,
        chargebee_request_origin_user_encoded=chargebee_request_origin_user_encoded,
        chargebee_request_origin_ip=chargebee_request_origin_ip,
    )
    yield from get_pages(kwargs, data_json_path)
