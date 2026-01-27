# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class CreateDiskReplicaPairRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        charge_type: str = None,
        client_token: str = None,
        description: str = None,
        destination_disk_id: str = None,
        destination_region_id: str = None,
        destination_zone_id: str = None,
        disk_id: str = None,
        enable_rtc: bool = None,
        pair_name: str = None,
        period: int = None,
        period_unit: str = None,
        rpo: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_zone_id: str = None,
        tag: List[main_models.CreateDiskReplicaPairRequestTag] = None,
    ):
        # The bandwidth to use to asynchronously replicate data from the primary disk to the secondary disk. Unit: Kbit/s. Valid values:
        # 
        # *   10240
        # *   20480
        # *   51200
        # *   102400
        # 
        # Default value: 10240. When you set the ChargeType parameter to POSTPAY, the Bandwidth parameter is automatically set to 0 and cannot be modified. The value 0 indicates that bandwidth is dynamically allocated based on the volume of data that is asynchronously replicated from the primary disk to the secondary disk.
        self.bandwidth = bandwidth
        # The billing method of the replication pair. Valid values:
        # 
        # *   PREPAY: subscription
        # *   POSTPAY: pay-as-you-go
        # 
        # Default value: POSTPAY.
        self.charge_type = charge_type
        # The client token to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the replication pair. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The ID of the secondary disk.
        # 
        # This parameter is required.
        self.destination_disk_id = destination_disk_id
        # The region ID of the secondary disk. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/354276.html) operation to query the most recent list of regions in which async replication is supported.
        # 
        # This parameter is required.
        self.destination_region_id = destination_region_id
        # The zone ID of the secondary disk.
        # 
        # This parameter is required.
        self.destination_zone_id = destination_zone_id
        # The ID of the primary disk.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # Whether to enable replication time control. By default, this parameter is disabled.
        self.enable_rtc = enable_rtc
        # The name of the replication pair. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. The name can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        self.pair_name = pair_name
        # The subscription duration of the replication pair. When `ChargeType` is set to PREPAY, this parameter must be specified. Valid values: 1, 2, 3, 6, 12, 24, 36, and 60. The subscription duration unit is specified by `PeriodUnit`.
        self.period = period
        # The unit of the subscription duration of the replication pair. Set the value to Month. Valid value: Month
        self.period_unit = period_unit
        # The recovery point objective (RPO) of the replication pair. Unit: seconds. Valid value: 900.
        self.rpo = rpo
        # The ID of the region in which to create the replication pair.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the replication pair belongs.
        self.resource_group_id = resource_group_id
        # The zone ID of the primary disk.
        # 
        # This parameter is required.
        self.source_zone_id = source_zone_id
        # The tags to add to the replication pair-consistent group. You can specify up to 20 tags.
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

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_disk_id is not None:
            result['DestinationDiskId'] = self.destination_disk_id

        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id

        if self.destination_zone_id is not None:
            result['DestinationZoneId'] = self.destination_zone_id

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.enable_rtc is not None:
            result['EnableRtc'] = self.enable_rtc

        if self.pair_name is not None:
            result['PairName'] = self.pair_name

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

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

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationDiskId') is not None:
            self.destination_disk_id = m.get('DestinationDiskId')

        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')

        if m.get('DestinationZoneId') is not None:
            self.destination_zone_id = m.get('DestinationZoneId')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('EnableRtc') is not None:
            self.enable_rtc = m.get('EnableRtc')

        if m.get('PairName') is not None:
            self.pair_name = m.get('PairName')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

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
                temp_model = main_models.CreateDiskReplicaPairRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateDiskReplicaPairRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

