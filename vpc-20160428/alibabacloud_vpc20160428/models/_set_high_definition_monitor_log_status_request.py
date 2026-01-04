# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetHighDefinitionMonitorLogStatusRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        log_project: str = None,
        log_store: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        # The ID of the instance for which you want to configure fine-grained monitoring.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The instance type. Set the value to **EIP**.
        self.instance_type = instance_type
        # The name of the Simple Log Service (SLS) project.
        # 
        # This parameter is required.
        self.log_project = log_project
        # The name of the Logstore.
        # 
        # This parameter is required.
        self.log_store = log_store
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The status of fine-grained monitoring. Valid values:
        # 
        # *   **ON**
        # *   **OFF**
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.log_project is not None:
            result['LogProject'] = self.log_project

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

