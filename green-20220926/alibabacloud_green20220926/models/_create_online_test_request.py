# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOnlineTestRequest(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        url: str = None,
    ):
        # Data ID
        self.data_id = data_id
        # Resource Type
        self.resource_type = resource_type
        # Service Code
        self.service_code = service_code
        # Detection URL
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

