# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class CreateDedicatedBlockStorageClusterRequest(DaraModel):
    def __init__(
        self,
        azone: str = None,
        capacity: int = None,
        dbsc_id: str = None,
        dbsc_name: str = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateDedicatedBlockStorageClusterRequestTag] = None,
        type: str = None,
    ):
        # The ID of the zone in which to create the dedicated block storage cluster. You can call the [DescribeZones](https://help.aliyun.com/document_detail/25610.html) operation to query the most recent zone list.
        # 
        # This parameter is required.
        self.azone = azone
        # The capacity of the dedicated block storage cluster. Valid values: 61440 to 2334720. Unit: GiB. 2,334,720 GiB is equal to 2,280 TiB. The capacity increases in a minimum increment of 12,288 GiB.
        # 
        # >  If the capacity of a dedicated block storage cluster is less than 576 TiB, the maximum throughput per TiB cannot exceed 52 MB/s. If the capacity of a dedicated block storage cluster is greater than 576 TiB, the maximum throughput per TiB cannot exceed 26 MB/s.
        # 
        # This parameter is required.
        self.capacity = capacity
        # This parameter is deprecated.
        self.dbsc_id = dbsc_id
        # The name of the dedicated block storage cluster.
        # 
        # This parameter is required.
        self.dbsc_name = dbsc_name
        # The subscription duration of the dedicated block storage cluster. Valid values: 6, 7, 8, 9, 10, 11, 12, 24, and 36.
        self.period = period
        # The unit of the subscription duration specified by `Period`. Set the value to Month.
        self.period_unit = period_unit
        # The ID of the region in which to create the dedicated block storage cluster. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which to assign the dedicated block storage cluster.
        self.resource_group_id = resource_group_id
        # The tags to add to the dedicated block storage cluster. You can specify up to 20 tags.
        self.tag = tag
        # The type of the dedicated block storage cluster. Valid values:
        # 
        # *   Standard: basic dedicated block storage cluster. Enterprise SSDs (ESSDs) at performance level 0 (PL0 ESSDs) can be created in basic dedicated block storage clusters.
        # *   Premium: performance dedicated block storage cluster. ESSDs at performance level 1 (PL1 ESSDs) can be created in performance dedicated block storage clusters.
        # 
        # Default value: Premium.
        # 
        # For more information about ESSDs, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        # 
        # This parameter is required.
        self.type = type

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
        if self.azone is not None:
            result['Azone'] = self.azone

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.dbsc_id is not None:
            result['DbscId'] = self.dbsc_id

        if self.dbsc_name is not None:
            result['DbscName'] = self.dbsc_name

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Azone') is not None:
            self.azone = m.get('Azone')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('DbscId') is not None:
            self.dbsc_id = m.get('DbscId')

        if m.get('DbscName') is not None:
            self.dbsc_name = m.get('DbscName')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDedicatedBlockStorageClusterRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateDedicatedBlockStorageClusterRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the dedicated block storage cluster.
        # 
        # This parameter is required.
        self.key = key
        # The value of tag N to add to the dedicated block storage cluster.
        # 
        # This parameter is required.
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

