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
        lens_tags: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The type of the disk. Valid values:
        # - cloud
        # - cloud_efficiency
        # - cloud_ssd
        # - cloud_essd
        # - cloud_auto
        # - cloud_essd_entry
        self.disk_category = disk_category
        # Regular matching fuzzy query to filter cloud disk IDs.
        self.disk_id_pattern = disk_id_pattern
        # The list of disks.
        self.disk_ids = disk_ids
        # Event tags of the disk, which are used to filter the disks on which the events associated with the specified tags occurred in the previous 24 hours. Valid values:
        # 
        # *   NoSnapshot: specifies the event that is triggered because no snapshot is created for the disk to protect data on the disk.
        # *   BurstIOTriggered: specifies the event that is triggered when a burst I/O operation is performed on the disk.
        # *   CostOptimizationNeeded: specifies the event that is triggered when cost optimization is required.
        # *   DiskSpecNotMatchedWithInstance: specifies the event that is triggered if the disk specifications do not match the instance to which the disk is attached.
        # *   DiskIONo4kAligned: specifies the event that is triggered if the physical and logical sectors involved in a read or write operation are not 4K aligned.
        # *   DiskIOHang: specifies the event that is triggered when an I/O hang occurs on the disk.
        # *   InstanceIOPSExceedInstanceMaxLimit: specifies the event that is triggered when the number of IOPS on the instance reaches the upper limit.
        # *   InstanceBPSExceedInstanceMaxLimit: specifies the event that is triggered when the number of BPS on the instance reaches the upper limit.
        # *   DiskIOPSExceedInstanceMaxLimit: specifies the event that is triggered when the number of IOPS on the disk reaches the upper limit of the instance.
        # *   DiskBPSExceedInstanceMaxLimit: specifies the event that is triggered when the number of BPS on the disk reaches the upper limit of the instance.
        # *   DiskIOPSExceedDiskMaxLimit: specifies the event that is triggered when the number of IOPS on the disk reaches the upper limit of the disk.
        # *   DiskBPSExceedDiskMaxLimit: specifies the event that is triggered when the number of BPS on the disk reaches the upper limit of the disk.
        self.lens_tags = lens_tags
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The token used to start the next query to retrieve more results.
        # 
        # >The pagination token that is used in the next request to retrieve a new page of results. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The region ID.
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

        if m.get('LensTags') is not None:
            self.lens_tags = m.get('LensTags')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

