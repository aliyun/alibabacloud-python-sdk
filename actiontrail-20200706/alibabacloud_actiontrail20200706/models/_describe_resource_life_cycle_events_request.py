# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResourceLifeCycleEventsRequest(DaraModel):
    def __init__(
        self,
        resource_type: str = None,
        service_name: str = None,
    ):
        # The resource type.
        self.resource_type = resource_type
        # The name of the Alibaba Cloud service.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

