# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartReplicaGroupDrillRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        group_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the replication pair-consistent group ID. You can call the [DescribeDiskReplicaGroups](https://help.aliyun.com/document_detail/426614.html) operation the most recent list of async replication pair-consistent groups, including group IDs.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the region where the secondary site in the replication pair-consistent group is located. You can call the [DescribeDiskReplicaGroups](https://help.aliyun.com/document_detail/426614.html) operation to query the region where the secondary site in the replication pair-consistent group is located.
        # 
        # >  You must enable the disaster recovery drill feature in the region in which the secondary site resides.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

