# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMonitorNotifyObjectsRequest(DaraModel):
    def __init__(
        self,
        enterprise_id: int = None,
        name: str = None,
        type: int = None,
        webhook_type: str = None,
    ):
        self.enterprise_id = enterprise_id
        self.name = name
        self.type = type
        self.webhook_type = webhook_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.webhook_type is not None:
            result['webhookType'] = self.webhook_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('webhookType') is not None:
            self.webhook_type = m.get('webhookType')

        return self

