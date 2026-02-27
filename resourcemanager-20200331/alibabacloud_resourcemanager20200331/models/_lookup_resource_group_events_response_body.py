# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class LookupResourceGroupEventsResponseBody(DaraModel):
    def __init__(
        self,
        events: List[main_models.LookupResourceGroupEventsResponseBodyEvents] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The queried events.
        self.events = events
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.LookupResourceGroupEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class LookupResourceGroupEventsResponseBodyEvents(DaraModel):
    def __init__(
        self,
        change_type: str = None,
        event_time: str = None,
        region_id: str = None,
        resource_group_display_name: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service: str = None,
        source_resource_group_info: main_models.LookupResourceGroupEventsResponseBodyEventsSourceResourceGroupInfo = None,
        target_resource_group_info: main_models.LookupResourceGroupEventsResponseBodyEventsTargetResourceGroupInfo = None,
    ):
        # The type of the resource change event.
        self.change_type = change_type
        # The time when the event was triggered.
        self.event_time = event_time
        # The region ID.
        self.region_id = region_id
        # The resource group name.
        self.resource_group_display_name = resource_group_display_name
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        # 
        # You can obtain the resource type from the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.resource_type = resource_type
        # The service code.
        # 
        # You can obtain the code from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.service = service
        # The source resource group.
        self.source_resource_group_info = source_resource_group_info
        # The destination resource group.
        self.target_resource_group_info = target_resource_group_info

    def validate(self):
        if self.source_resource_group_info:
            self.source_resource_group_info.validate()
        if self.target_resource_group_info:
            self.target_resource_group_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_display_name is not None:
            result['ResourceGroupDisplayName'] = self.resource_group_display_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service is not None:
            result['Service'] = self.service

        if self.source_resource_group_info is not None:
            result['SourceResourceGroupInfo'] = self.source_resource_group_info.to_map()

        if self.target_resource_group_info is not None:
            result['TargetResourceGroupInfo'] = self.target_resource_group_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupDisplayName') is not None:
            self.resource_group_display_name = m.get('ResourceGroupDisplayName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('SourceResourceGroupInfo') is not None:
            temp_model = main_models.LookupResourceGroupEventsResponseBodyEventsSourceResourceGroupInfo()
            self.source_resource_group_info = temp_model.from_map(m.get('SourceResourceGroupInfo'))

        if m.get('TargetResourceGroupInfo') is not None:
            temp_model = main_models.LookupResourceGroupEventsResponseBodyEventsTargetResourceGroupInfo()
            self.target_resource_group_info = temp_model.from_map(m.get('TargetResourceGroupInfo'))

        return self

class LookupResourceGroupEventsResponseBodyEventsTargetResourceGroupInfo(DaraModel):
    def __init__(
        self,
        resource_group_display_name: str = None,
        resource_group_id: str = None,
    ):
        # The resource group name.
        self.resource_group_display_name = resource_group_display_name
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_display_name is not None:
            result['ResourceGroupDisplayName'] = self.resource_group_display_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupDisplayName') is not None:
            self.resource_group_display_name = m.get('ResourceGroupDisplayName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class LookupResourceGroupEventsResponseBodyEventsSourceResourceGroupInfo(DaraModel):
    def __init__(
        self,
        resource_group_display_name: str = None,
        resource_group_id: str = None,
    ):
        # The resource group name.
        self.resource_group_display_name = resource_group_display_name
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_display_name is not None:
            result['ResourceGroupDisplayName'] = self.resource_group_display_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupDisplayName') is not None:
            self.resource_group_display_name = m.get('ResourceGroupDisplayName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

