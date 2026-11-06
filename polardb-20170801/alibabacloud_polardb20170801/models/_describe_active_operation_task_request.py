# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeActiveOperationTaskRequest(DaraModel):
    def __init__(
        self,
        is_history: int = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        product_id: str = None,
        region: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        task_type: str = None,
    ):
        # Specifies whether to return historical tasks. Valid values:
        # * **0**: Returns current tasks.
        # * **1**: Returns historical tasks.
        # 
        # Default value: **0**.
        self.is_history = is_history
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be greater than 0 and cannot exceed the maximum value of the Integer data type. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30**, **50**, and **100**.
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The commodity ID.
        self.product_id = product_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the regions and zones supported by PolarDB.
        # 
        # > * You can enter **all** to view all pending tasks under your account.
        # * When `Region` is set to **all**, `TaskType` must also be set to **all**.
        # 
        # This parameter is required.
        self.region = region
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The task type. You can call the [DescribeActiveOperationTaskType](ID not yet generated) operation to query the task types of pending tasks.
        # 
        # > * You can also enter **all** to view all pending tasks under your account.
        # * When `TaskType` is set to **all**, `Region` must also be set to **all**.
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

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region is not None:
            result['Region'] = self.region

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

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

