# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAlertWebhookResponseBody(DaraModel):
    def __init__(
        self,
        alert_webhook_id: str = None,
        request_id: str = None,
    ):
        self.alert_webhook_id = alert_webhook_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_webhook_id is not None:
            result['alertWebhookId'] = self.alert_webhook_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertWebhookId') is not None:
            self.alert_webhook_id = m.get('alertWebhookId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

