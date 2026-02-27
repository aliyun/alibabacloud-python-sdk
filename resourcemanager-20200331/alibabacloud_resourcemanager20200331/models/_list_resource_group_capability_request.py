# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceGroupCapabilityRequest(DaraModel):
    def __init__(
        self,
        resource_type: str = None,
        service: str = None,
        support_resource_group_event: bool = None,
    ):
        # The resource type.
        # 
        # You can obtain the resource type from the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.resource_type = resource_type
        # The ID of the Alibaba Cloud service.
        # 
        # You can obtain the service code from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.service = service
        # Specifies whether a specific resource type or cloud service supports resource group events.
        self.support_resource_group_event = support_resource_group_event

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service is not None:
            result['Service'] = self.service

        if self.support_resource_group_event is not None:
            result['SupportResourceGroupEvent'] = self.support_resource_group_event

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('SupportResourceGroupEvent') is not None:
            self.support_resource_group_event = m.get('SupportResourceGroupEvent')

        return self

