# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class CreateDiskReplicaGroupRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        description: str = None,
        destination_region_id: str = None,
        destination_zone_id: str = None,
        enable_rtc: bool = None,
        group_name: str = None,
        rpo: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_zone_id: str = None,
        tag: List[main_models.CreateDiskReplicaGroupRequestTag] = None,
    ):
        # The bandwidth value. Unit: Mbit/s.
        # 
        # >  This parameter is not publicly available.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the replication pair-consistent group. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The region ID of the secondary site.
        # 
        # This parameter is required.
        self.destination_region_id = destination_region_id
        # The zone ID of the secondary site.
        # 
        # This parameter is required.
        self.destination_zone_id = destination_zone_id
        # Whether to enable replication time control. By default, this parameter is disabled.
        self.enable_rtc = enable_rtc
        # The name of the replication pair-consistent group. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.group_name = group_name
        # The RPO of the replication pair-consistent group. Unit: seconds. Valid value: 900.
        self.rpo = rpo
        # The ID of the region in which to create the replication pair-consistent group. The primary site is deployed in the specified region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the replication pair-consistent group belongs.
        self.resource_group_id = resource_group_id
        # The zone ID of the primary site.
        # 
        # This parameter is required.
        self.source_zone_id = source_zone_id
        # The tags. Up to 20 tags are supported.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

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

        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id

        if self.destination_zone_id is not None:
            result['DestinationZoneId'] = self.destination_zone_id

        if self.enable_rtc is not None:
            result['EnableRtc'] = self.enable_rtc

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.rpo is not None:
            result['RPO'] = self.rpo

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_zone_id is not None:
            result['SourceZoneId'] = self.source_zone_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')

        if m.get('DestinationZoneId') is not None:
            self.destination_zone_id = m.get('DestinationZoneId')

        if m.get('EnableRtc') is not None:
            self.enable_rtc = m.get('EnableRtc')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('RPO') is not None:
            self.rpo = m.get('RPO')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceZoneId') is not None:
            self.source_zone_id = m.get('SourceZoneId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDiskReplicaGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateDiskReplicaGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N of the replication pair-consistent group.
        self.key = key
        # The value of tag N of the replication pair-consistent group.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

