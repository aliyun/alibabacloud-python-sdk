# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReprotectDiskReplicaPairRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        replica_pair_id: str = None,
        reverse_replicate: bool = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The region ID of the secondary disk in the replication pair. You can call the [DescribeDiskReplicaPairs](https://help.aliyun.com/document_detail/354206.html) operation to query region IDs of secondary disks in replication pairs.
        # 
        # >  The reverse replication feature must be enabled from the region where the secondary disk is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the replication pair.
        # 
        # This parameter is required.
        self.replica_pair_id = replica_pair_id
        # Specifies whether to enable the reverse replication sub-feature. Valid values: true and false. Default value: true.
        self.reverse_replicate = reverse_replicate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id

        if self.reverse_replicate is not None:
            result['ReverseReplicate'] = self.reverse_replicate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')

        if m.get('ReverseReplicate') is not None:
            self.reverse_replicate = m.get('ReverseReplicate')

        return self

