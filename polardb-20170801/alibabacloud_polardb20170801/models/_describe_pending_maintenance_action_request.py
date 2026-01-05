# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePendingMaintenanceActionRequest(DaraModel):
    def __init__(
        self,
        is_history: int = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        task_type: str = None,
    ):
        # Specifies whether to return the historical tasks. Valid values:
        # 
        # *   **0**: returns the current task.
        # *   **1**: returns the historical tasks.
        # 
        # Default value: **0**.
        self.is_history = is_history
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Specify the parameter to a positive integer that does not exceed the maximum value of the INTEGER data type. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30**, **50**, and **100**.
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The region ID of the pending event. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the regions and zones that are supported by PolarDB.
        # >- You can set this parameter to **all** to view all pending events within your account.
        # >- If you set `Region` to **all**, you must set `TaskType` to **all**.
        # 
        # This parameter is required.
        self.region = region
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The task type of pending events. Valid values:
        # 
        # *   **DatabaseSoftwareUpgrading**: database software upgrades
        # *   **DatabaseHardwareMaintenance**: hardware maintenance and upgrades
        # *   **DatabaseStorageUpgrading**: database storage upgrades
        # *   **DatabaseProxyUpgrading**: minor version upgrades of the proxy
        # *   **all**: queries the details of the pending events of all preceding types.
        # 
        # > If the `Region` parameter is set to **all**, the `TaskType` parameter must be set to **all**.
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_history is not None:
            result['IsHistory'] = self.is_history

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsHistory') is not None:
            self.is_history = m.get('IsHistory')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

