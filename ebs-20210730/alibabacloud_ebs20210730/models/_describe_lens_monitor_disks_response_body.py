# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeLensMonitorDisksResponseBody(DaraModel):
    def __init__(
        self,
        disk_infos: List[main_models.DescribeLensMonitorDisksResponseBodyDiskInfos] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the disks.
        self.disk_infos = disk_infos
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.disk_infos:
            for v1 in self.disk_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DiskInfos'] = []
        if self.disk_infos is not None:
            for k1 in self.disk_infos:
                result['DiskInfos'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk_infos = []
        if m.get('DiskInfos') is not None:
            for k1 in m.get('DiskInfos'):
                temp_model = main_models.DescribeLensMonitorDisksResponseBodyDiskInfos()
                self.disk_infos.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLensMonitorDisksResponseBodyDiskInfos(DaraModel):
    def __init__(
        self,
        bps: int = None,
        bursting_enabled: bool = None,
        disk_category: str = None,
        disk_id: str = None,
        disk_name: str = None,
        disk_status: str = None,
        disk_type: str = None,
        iops: int = None,
        lens_tags: List[str] = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        region_id: str = None,
        sharing_enabled: str = None,
        size: int = None,
        tags: List[main_models.DescribeLensMonitorDisksResponseBodyDiskInfosTags] = None,
        zone_id: str = None,
    ):
        # The BPS.
        self.bps = bps
        # Indicates whether the performance burst feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is available only if you set `DiskCategory` to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The type of the disk. Valid values:
        # - cloud
        # - cloud_efficiency
        # - cloud_ssd
        # - cloud_essd
        # - cloud_auto
        # - cloud_essd_entry
        self.disk_category = disk_category
        # The ID of the disk.
        self.disk_id = disk_id
        # The name of the disk.
        self.disk_name = disk_name
        # The disk status. Valid values:
        # 
        # - Available
        # - Deleted
        self.disk_status = disk_status
        # The disk type. Valid values:
        # *   system: system disk
        # *   data: data disk
        self.disk_type = disk_type
        # The IOPS.
        self.iops = iops
        # Event tags of the disk.
        self.lens_tags = lens_tags
        # The new performance level of the ESSD. Valid values:
        # 
        # *   PL0: An ESSD can deliver up to 10,000 random read/write IOPS.
        # *   PL1: An ESSD can deliver up to 50,000 random read/write IOPS.
        # *   PL2: An ESSD can deliver up to 100,000 random read/write IOPS.
        # *   PL3: An ESSD delivers up to 1,000,000 random read/write IOPS.
        self.performance_level = performance_level
        # The provisioned read/write IOPS of the ESSD AutoPL disk to use as the system disk. Valid values: 0 to min{50,000, 1,000 × Capacity - Baseline IOPS}.
        # 
        # Baseline performance = min{1,800 + 50 × Capacity, 50,000}
        # 
        # This parameter is available only if you set `DiskCategory` to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops
        # The region ID of the disk.
        self.region_id = region_id
        self.sharing_enabled = sharing_enabled
        # The size of the disk. Unit: GiB.
        self.size = size
        # Tags of the disk.
        self.tags = tags
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps is not None:
            result['Bps'] = self.bps

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.disk_status is not None:
            result['DiskStatus'] = self.disk_status

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.iops is not None:
            result['Iops'] = self.iops

        if self.lens_tags is not None:
            result['LensTags'] = self.lens_tags

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sharing_enabled is not None:
            result['SharingEnabled'] = self.sharing_enabled

        if self.size is not None:
            result['Size'] = self.size

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('DiskStatus') is not None:
            self.disk_status = m.get('DiskStatus')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Iops') is not None:
            self.iops = m.get('Iops')

        if m.get('LensTags') is not None:
            self.lens_tags = m.get('LensTags')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SharingEnabled') is not None:
            self.sharing_enabled = m.get('SharingEnabled')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeLensMonitorDisksResponseBodyDiskInfosTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeLensMonitorDisksResponseBodyDiskInfosTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

