# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlertWebhooksShrinkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        webhook_ids_shrink: str = None,
        workspace: str = None,
    ):
        # The name of the webhook.
        self.name = name
        # The page number. Default value: 1.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The unique ID of the webhook.
        self.webhook_ids_shrink = webhook_ids_shrink
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.webhook_ids_shrink is not None:
            result['webhookIds'] = self.webhook_ids_shrink

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('webhookIds') is not None:
            self.webhook_ids_shrink = m.get('webhookIds')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

