# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDiskReplicaPairRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        description: str = None,
        enable_rtc: bool = None,
        pair_name: str = None,
        rpo: int = None,
        region_id: str = None,
        replica_pair_id: str = None,
    ):
        # The bandwidth value. Unit: Kbit/s.
        # 
        # >  This parameter is not publicly available.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the replication pair.
        self.description = description
        # Whether to enable replication time control.
        self.enable_rtc = enable_rtc
        # The name of the replication pair.
        self.pair_name = pair_name
        # The recovery point objective (RPO) of the replication pair-consistent group. Unit: seconds. Valid value: 900.
        self.rpo = rpo
        # The region ID of the primary or secondary disk in the replication pair. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/354276.html) operation to query the most recent list of regions in which async replication is supported.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the replication pair.
        # 
        # This parameter is required.
        self.replica_pair_id = replica_pair_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_rtc is not None:
            result['EnableRtc'] = self.enable_rtc

        if self.pair_name is not None:
            result['PairName'] = self.pair_name

        if self.rpo is not None:
            result['RPO'] = self.rpo

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableRtc') is not None:
            self.enable_rtc = m.get('EnableRtc')

        if m.get('PairName') is not None:
            self.pair_name = m.get('PairName')

        if m.get('RPO') is not None:
            self.rpo = m.get('RPO')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')

        return self

