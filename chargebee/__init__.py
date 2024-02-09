from typing import List

import dlt
from dlt.extract.source import DltResource

from .api import list_customers, list_events, list_invoices, list_orders, list_subscriptions, list_transactions
from .security.basic_auth import BasicAuth

__source_name__ = "chargebee_source"


@dlt.source(name="chargebee", max_table_nesting=2)
def chargebee_source(
    credentials: BasicAuth = dlt.config.value,
    base_url: str = dlt.config.value,
    limit: int = 10,
) -> List[DltResource]:
    # Root list endpoints
    resources = {}
    resources["subscriptions"] = list_subscriptions(credentials=credentials, base_url=base_url, limit=limit)
    resources["customers"] = list_customers(credentials=credentials, base_url=base_url, limit=limit)
    resources["invoices"] = list_invoices(credentials=credentials, base_url=base_url, limit=limit)
    resources["orders"] = list_orders(credentials=credentials, base_url=base_url, limit=limit)
    resources["transactions"] = list_transactions(credentials=credentials, base_url=base_url, limit=limit)
    resources["events"] = list_events(credentials=credentials, base_url=base_url, limit=limit)

    return list(resources.values())
