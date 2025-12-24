# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAutoSnapshotPolicyRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        auto_snapshot_policy_id: str = None,
        region_id: str = None,
    ):
        # RAM用户的虚拟账号ID。
        self.owner_id = owner_id
        # 资源主账号的账号名称。
        self.resource_owner_account = resource_owner_account
        # 资源主账号的ID，亦即UID。
        self.resource_owner_id = resource_owner_id
        # The ID of the automatic snapshot policy. You can call the [DescribeAutoSnapshotPolicyEx](https://help.aliyun.com/document_detail/25530.html) operation to query the IDs of available automatic snapshot policies.
        # 
        # This parameter is required.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The ID of the region to which the automatic snapshot policy belongs. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.auto_snapshot_policy_id is not None:
            result['autoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('autoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('autoSnapshotPolicyId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

