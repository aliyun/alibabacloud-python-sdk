# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class ListVirtualResourceResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        virtual_resources: List[main_models.ListVirtualResourceResponseBodyVirtualResources] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The virtual resource groups.
        self.virtual_resources = virtual_resources

    def validate(self):
        if self.virtual_resources:
            for v1 in self.virtual_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VirtualResources'] = []
        if self.virtual_resources is not None:
            for k1 in self.virtual_resources:
                result['VirtualResources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.virtual_resources = []
        if m.get('VirtualResources') is not None:
            for k1 in m.get('VirtualResources'):
                temp_model = main_models.ListVirtualResourceResponseBodyVirtualResources()
                self.virtual_resources.append(temp_model.from_map(k1))

        return self

class ListVirtualResourceResponseBodyVirtualResources(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        service_count: int = None,
        update_time: str = None,
        virtual_resource_id: str = None,
        virtual_resource_name: str = None,
    ):
        # The time when the virtual resource group was created.
        self.create_time = create_time
        # The number of deployed services.
        self.service_count = service_count
        # The time when the virtual resource group was last updated.
        self.update_time = update_time
        # The ID of the virtual resource group.
        self.virtual_resource_id = virtual_resource_id
        # The name of the virtual resource group.
        self.virtual_resource_name = virtual_resource_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.service_count is not None:
            result['ServiceCount'] = self.service_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.virtual_resource_id is not None:
            result['VirtualResourceId'] = self.virtual_resource_id

        if self.virtual_resource_name is not None:
            result['VirtualResourceName'] = self.virtual_resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VirtualResourceId') is not None:
            self.virtual_resource_id = m.get('VirtualResourceId')

        if m.get('VirtualResourceName') is not None:
            self.virtual_resource_name = m.get('VirtualResourceName')

        return self

