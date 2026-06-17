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
        dbcluster_id: str = None,
        dbtype: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        status: int = None,
        task_type: str = None,
    ):
        # Specifies whether to allow cancellation. Valid values:
        # 
        # - **-1** (default): all.
        # 
        # - **0**: returns only tasks that do not allow cancellation.
        # 
        # - **1**: returns only tasks that allow cancellation.
        self.allow_cancel = allow_cancel
        # Specifies whether to allow time modification. Valid values:
        # 
        # - **-1** (default): all.
        # 
        # - **0**: returns only tasks that do not allow time modification.
        # 
        # - **1**: returns only tasks that allow time modification.
        self.allow_change = allow_change
        # The task level. Valid values:
        # 
        # - **all** (default): all.
        # 
        # - **S0**: returns tasks at the abnormal repair level.
        # 
        # - **S1**: returns tasks at the system maintenance level.
        self.change_level = change_level
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query detailed information about all clusters under your account, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The database engine type. Valid values:
        # 
        # - **MySQL**
        # 
        # - **PostgreSQL**
        # 
        # - **Oracle**
        self.dbtype = dbtype
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be greater than 0 and cannot exceed the maximum value of the Integer data type. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # - **30** (default)
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # The region ID of the pending event.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The task status. Valid values:
        # 
        # - -1: all tasks.
        # 
        # - 3: pending tasks.
        # 
        # - 4: tasks in progress.
        # 
        # - 5: successfully completed tasks.
        # 
        # - 6: failed tasks.
        # 
        # - 7: canceled tasks.
        self.status = status
        # The type of the pending event task. Valid values:
        # 
        # - **DatabaseSoftwareUpgrading**: database software upgrade
        # 
        # - **DatabaseHardwareMaintenance**: hardware maintenance and upgrade
        # 
        # - **DatabaseStorageUpgrading**: database storage upgrade
        # 
        # - **DatabaseProxyUpgrading**: proxy minor version upgrade
        # 
        # - **all**: returns all types of pending events
        # 
        # > When `Region` is set to **all**, `TaskType` must also be set to **all**.
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

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

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

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

