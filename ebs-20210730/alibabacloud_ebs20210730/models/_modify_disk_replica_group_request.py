# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDiskReplicaGroupRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        description: str = None,
        enable_rtc: bool = None,
        group_name: str = None,
        rpo: int = None,
        region_id: str = None,
        replica_group_id: str = None,
    ):
        # The bandwidth. Unit: Kbps.
        # 
        # > This parameter is not available.
        self.bandwidth = bandwidth
        # A client token to ensure the idempotence of the request. Generate a unique value for this parameter from your client. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the replication pair-consistent group. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable replication time control (RTC). Valid values:
        # 
        # - false: RTC is disabled.
        # 
        # - true: RTC is enabled.
        # 
        # > If this parameter is set to true, RTC is enabled for the replication pair-consistent group. RTC is also enabled for all asynchronous replication pairs that are added to the group.
        self.enable_rtc = enable_rtc
        # The name of the replication pair-consistent group. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. The name can contain digits, colons (:), underscores (_), and hyphens (-).
        self.group_name = group_name
        # The recovery point objective (RPO) of the replication pair-consistent group. Unit: seconds. A value of 900 is supported.
        self.rpo = rpo
        # The region ID of the replication pair-consistent group.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the replication pair-consistent group. Call [DescribeDiskReplicaGroups](https://help.aliyun.com/document_detail/426614.html) to query the IDs of replication pair-consistent groups.
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
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_rtc is not None:
            result['EnableRtc'] = self.enable_rtc

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.rpo is not None:
            result['RPO'] = self.rpo

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id

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

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('RPO') is not None:
            self.rpo = m.get('RPO')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')

        return self

