# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWebhookContactsRequest(DaraModel):
    def __init__(
        self,
        contact_ids: str = None,
        page: int = None,
        size: int = None,
        webhook_name: str = None,
    ):
        # The ID of the alert contact.
        self.contact_ids = contact_ids
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page = page
        # The number of alert contacts displayed on each page.
        # 
        # This parameter is required.
        self.size = size
        # The name of the webhook alert contact.
        self.webhook_name = webhook_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids

        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')

        return self

