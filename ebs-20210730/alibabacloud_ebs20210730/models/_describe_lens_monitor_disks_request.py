# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeLensMonitorDisksRequest(DaraModel):
    def __init__(
        self,
        disk_category: str = None,
        disk_id_pattern: str = None,
        disk_ids: List[str] = None,
        ecs_instance_id: str = None,
        lens_tags: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The cloud disk type. Valid values:
        # 
        # - cloud: basic cloud disk.
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: Enterprise SSD (ESSD).
        # - cloud_auto: ESSD AutoPL cloud disk.
        # - cloud_essd_entry: ESSD Entry disk.
        self.disk_category = disk_category
        # The regular expression pattern used for fuzzy match filtering of cloud disk IDs.
        self.disk_id_pattern = disk_id_pattern
        # The list of cloud disk IDs.
        self.disk_ids = disk_ids
        # The ECS instance ID.
        self.ecs_instance_id = ecs_instance_id
        # The list of cloud disk event tags, used to filter cloud disks that have experienced these event types within the last 24 hours. Valid values:
        # - NoSnapshot: data protection
        # - BurstIOTriggered: burst I/O
        # - CostOptimizationNeeded: cost optimization
        # - DiskSpecNotMatchedWithInstance: instance and cloud disk specifications do not match
        # - DiskIONo4kAligned: non-4K aligned read/write
        # - DiskIOHang: I/O hang occurred on the cloud disk
        # - InstanceIOPSExceedInstanceMaxLimit: instance IOPS reached the upper limit
        # - InstanceBPSExceedInstanceMaxLimit: instance BPS reached the upper limit
        # - DiskIOPSExceedInstanceMaxLimit: cloud disk IOPS reached the instance upper limit
        # - DiskBPSExceedInstanceMaxLimit: cloud disk BPS reached the instance upper limit
        # - DiskIOPSExceedDiskMaxLimit: cloud disk IOPS reached the disk upper limit
        # - DiskBPSExceedDiskMaxLimit: cloud disk BPS reached the disk upper limit
        self.lens_tags = lens_tags
        # The maximum number of entries per page for a paged query. Maximum value: 100.
        # Default value:
        # 
        # - The default value is 10.
        # 
        # - If the specified value is greater than 100, the default value of 100 is used.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        # The region ID. You can call DescribeRegions to query the list of regions supported by EBS Lens.
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
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_id_pattern is not None:
            result['DiskIdPattern'] = self.disk_id_pattern

        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids

        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.lens_tags is not None:
            result['LensTags'] = self.lens_tags

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskIdPattern') is not None:
            self.disk_id_pattern = m.get('DiskIdPattern')

        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')

        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('LensTags') is not None:
            self.lens_tags = m.get('LensTags')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

