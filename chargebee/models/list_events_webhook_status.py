from enum import Enum


class ListEventsWebhookStatus(str, Enum):
    FAILED = "failed"
    NOT_APPLICABLE = "not_applicable"
    NOT_CONFIGURED = "not_configured"
    RE_SCHEDULED = "re_scheduled"
    SCHEDULED = "scheduled"
    SKIPPED = "skipped"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
