# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeActiveOperationTasksRequest(DaraModel):
    def __init__(
        self,
        allow_cancel: int = None,
        allow_change: int = None,
        change_level: str = None,
        db_type: str = None,
        ins_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        product_id: str = None,
        region: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: int = None,
        task_type: str = None,
    ):
        # Specifies whether the task can be canceled. Valid values:
        # 
        # - **-1** (default): returns all tasks.
        # 
        # - **0**: returns only tasks that cannot be canceled.
        # 
        # - **1**: returns only tasks that can be canceled.
        self.allow_cancel = allow_cancel
        # Specifies whether the time can be changed. Valid values:
        # 
        # - **-1** (default): returns all tasks.
        # 
        # - **0**: returns only tasks whose time cannot be changed.
        # 
        # - **1**: returns only tasks whose time can be changed.
        self.allow_change = allow_change
        # The level of the task. Valid values:
        # 
        # - **all** (default): returns all tasks.
        # 
        # - **S0**: returns tasks for exception fixing.
        # 
        # - **S1**: returns tasks for system O\\&M.
        self.change_level = change_level
        # The database type. Default value: **all**.
        self.db_type = db_type
        # The name of the instance. This parameter is optional. You can specify only one instance name.
        self.ins_name = ins_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be greater than **0**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30**, **50**, and **100**. Default value: **30**.
        self.page_size = page_size
        # The product name. For MongoDB instances, set this parameter to **MongoDB**.
        self.product_id = product_id
        # The ID of the region where the pending event is located. Call the DescribeRegions operation to obtain the region ID.
        # 
        # > A value of **all** indicates all region IDs.
        self.region = region
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task status. This parameter filters the returned tasks.
        # 
        # - **-1**: all tasks.
        # 
        # - **3**: pending tasks.
        # 
        # - **4**: running tasks.
        # 
        # - **5**: successfully completed tasks.
        # 
        # - **6**: failed tasks.
        # 
        # - **7**: canceled tasks.
        self.status = status
        # The task type. Valid values:
        # 
        # - **rds_apsaradb_ha**: primary-secondary node switchover.
        # 
        # - **rds_apsaradb_transfer**: instance migration.
        # 
        # - **rds_apsaradb_upgrade**: minor version upgrade.
        # 
        # - **rds_apsaradb_maxscale**: proxy minor version upgrade.
        # 
        # - **all**: all task types.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_cancel is not None:
            result['AllowCancel'] = self.allow_cancel

        if self.allow_change is not None:
            result['AllowChange'] = self.allow_change

        if self.change_level is not None:
            result['ChangeLevel'] = self.change_level

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.ins_name is not None:
            result['InsName'] = self.ins_name

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCancel') is not None:
            self.allow_cancel = m.get('AllowCancel')

        if m.get('AllowChange') is not None:
            self.allow_change = m.get('AllowChange')

        if m.get('ChangeLevel') is not None:
            self.change_level = m.get('ChangeLevel')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

