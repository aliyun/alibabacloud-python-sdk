# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartDiskReplicaGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        one_shot: bool = None,
        region_id: str = None,
        replica_group_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Specifies whether to immediately synchronize data once. Valid values:
        # 
        # *   true: immediately synchronizes data once.
        # *   false: synchronizes data based on the RPO of the replication pair-consistent group.
        # 
        # Default value: false.
        self.one_shot = one_shot
        # The ID of the replication pair-consistent group.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the replication pair-consistent group. You can call the [DescribeDiskReplicaGroups](https://help.aliyun.com/document_detail/426614.html) operation to query the IDs of replication pair-consistent groups.
        # 
        # This parameter is required.
        self.replica_group_id = replica_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.one_shot is not None:
            result['OneShot'] = self.one_shot

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OneShot') is not None:
            self.one_shot = m.get('OneShot')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')

        return self

