# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWebhookContactRequest(DaraModel):
    def __init__(
        self,
        webhook_id: int = None,
    ):
        # The ID of the webhook alert contact.
        # 
        # This parameter is required.
        self.webhook_id = webhook_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')

        return self

