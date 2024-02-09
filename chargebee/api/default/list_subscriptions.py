from http import HTTPStatus
from typing import Any, Dict, Iterator, Optional, Union

import dlt
from dlt.sources.helpers import requests

from ...security.basic_auth import BasicAuth
from ...types import UNSET, Response, Unset
from ...utils import extract_nested_data


def _get_kwargs(
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, str] = UNSET,
    chargebee_request_origin_device: Union[Unset, str] = UNSET,
    chargebee_request_origin_user: Union[Unset, str] = UNSET,
    chargebee_request_origin_user_encoded: Union[Unset, str] = UNSET,
    chargebee_request_origin_ip: Union[Unset, str] = UNSET,
    base_url: str = dlt.config.value,
    credentials: BasicAuth = dlt.secrets.value,
) -> Dict[str, Any]:
    url = "{}/subscriptions".format(base_url)

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "params": params,
    }


def _build_response(response: requests.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=response.json(),
    )


@dlt.resource(table_name="subscriptions")
def list_subscriptions(
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, str] = UNSET,
    chargebee_request_origin_device: Union[Unset, str] = UNSET,
    chargebee_request_origin_user: Union[Unset, str] = UNSET,
    chargebee_request_origin_user_encoded: Union[Unset, str] = UNSET,
    chargebee_request_origin_ip: Union[Unset, str] = UNSET,
    base_url: str = dlt.config.value,
    credentials: BasicAuth = dlt.secrets.value,
    data_json_path: Optional[str] = "list",
) -> Iterator[Any]:
    r"""List subscriptions

     Returns a list of subscriptions meeting **all** the conditions specified in the filter parameters
    below.

    Args:
        limit (Union[Unset, None, int]):  Default: 10.
        offset (Union[Unset, None, str]):
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
        Iterator of 'ListSubscriptionsResponse200ListItem' items
    """

    kwargs = _get_kwargs(
        base_url=base_url,
        credentials=credentials,
        limit=limit,
        offset=offset,
        chargebee_request_origin_device=chargebee_request_origin_device,
        chargebee_request_origin_user=chargebee_request_origin_user,
        chargebee_request_origin_user_encoded=chargebee_request_origin_user_encoded,
        chargebee_request_origin_ip=chargebee_request_origin_ip,
    )
    response = _build_response(requests.request(**kwargs))
    yield extract_nested_data(response.parsed, data_json_path)
