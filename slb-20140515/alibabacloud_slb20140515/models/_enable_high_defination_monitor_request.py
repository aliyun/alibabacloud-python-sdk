# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableHighDefinationMonitorRequest(DaraModel):
    def __init__(
        self,
        log_project: str = None,
        log_store: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: str = None,
    ):
        # The name of the project of Log Service. The name must be 4 to 63 characters in length, and can contain digits and lowercase letters. It must start and end with a digit or a letter.
        # 
        # This parameter is required.
        self.log_project = log_project
        # The name of the Logstore of Log Service. The name must be 2 to 64 characters in length and can contain digits, lowercase letters, hyphens (-) and underscores (_). It must start and end with a digit or a letter.
        # 
        # This parameter is required.
        self.log_store = log_store
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the Classic Load Balancer (CLB) instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/27584.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags of the logs. The tags must be key-value pairs that are contained in a JSON dictionary.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

