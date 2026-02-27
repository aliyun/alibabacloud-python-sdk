# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class DeleteResourceGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: main_models.DeleteResourceGroupResponseBodyResourceGroup = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the resource group.
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroup') is not None:
            temp_model = main_models.DeleteResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m.get('ResourceGroup'))

        return self

class DeleteResourceGroupResponseBodyResourceGroup(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        region_statuses: main_models.DeleteResourceGroupResponseBodyResourceGroupRegionStatuses = None,
        status: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource group belongs.
        self.account_id = account_id
        # The time when the resource group was created. The time is displayed in UTC.
        self.create_date = create_date
        # The display name of the resource group.
        self.display_name = display_name
        # The ID of the resource group.
        self.id = id
        # The unique identifier of the resource group.
        self.name = name
        self.region_statuses = region_statuses
        # The status of the resource group. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        # *   PendingDelete: The resource group is waiting to be deleted.
        self.status = status

    def validate(self):
        if self.region_statuses:
            self.region_statuses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionStatuses') is not None:
            temp_model = main_models.DeleteResourceGroupResponseBodyResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m.get('RegionStatuses'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DeleteResourceGroupResponseBodyResourceGroupRegionStatuses(DaraModel):
    def __init__(
        self,
        region_status: List[main_models.DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus] = None,
    ):
        self.region_status = region_status

    def validate(self):
        if self.region_status:
            for v1 in self.region_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k1 in self.region_status:
                result['RegionStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k1 in m.get('RegionStatus'):
                temp_model = main_models.DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k1))

        return self

class DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        status: str = None,
    ):
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

