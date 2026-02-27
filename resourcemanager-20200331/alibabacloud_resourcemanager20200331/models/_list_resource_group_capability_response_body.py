# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupCapabilityResponseBody(DaraModel):
    def __init__(
        self,
        capabilities: List[main_models.ListResourceGroupCapabilityResponseBodyCapabilities] = None,
        request_id: str = None,
    ):
        # Indicates whether a specific resource type or cloud service supports resource group events.
        self.capabilities = capabilities
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.capabilities:
            for v1 in self.capabilities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Capabilities'] = []
        if self.capabilities is not None:
            for k1 in self.capabilities:
                result['Capabilities'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.capabilities = []
        if m.get('Capabilities') is not None:
            for k1 in m.get('Capabilities'):
                temp_model = main_models.ListResourceGroupCapabilityResponseBodyCapabilities()
                self.capabilities.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListResourceGroupCapabilityResponseBodyCapabilities(DaraModel):
    def __init__(
        self,
        resource_center_resource_type: str = None,
        resource_type: str = None,
        service: str = None,
        support_resource_group_event: bool = None,
    ):
        self.resource_center_resource_type = resource_center_resource_type
        # The resource type.
        # 
        # You can obtain the resource type from the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.resource_type = resource_type
        # The service code.
        # 
        # You can obtain the code from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.service = service
        # Indicates whether a specific resource type or cloud service supports resource group events.
        self.support_resource_group_event = support_resource_group_event

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_center_resource_type is not None:
            result['ResourceCenterResourceType'] = self.resource_center_resource_type

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service is not None:
            result['Service'] = self.service

        if self.support_resource_group_event is not None:
            result['SupportResourceGroupEvent'] = self.support_resource_group_event

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCenterResourceType') is not None:
            self.resource_center_resource_type = m.get('ResourceCenterResourceType')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('SupportResourceGroupEvent') is not None:
            self.support_resource_group_event = m.get('SupportResourceGroupEvent')

        return self

