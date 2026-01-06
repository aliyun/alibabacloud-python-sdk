# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DescribeUdmSnapshotsRequest(DaraModel):
    def __init__(
        self,
        disk_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        job_id: str = None,
        snapshot_ids: Dict[str, Any] = None,
        source_type: str = None,
        start_time: int = None,
        udm_region_id: str = None,
    ):
        # The ID of the disk.
        self.disk_id = disk_id
        # The end of the time range to query. The value must be a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The ID of the backup job.
        self.job_id = job_id
        # The list of backup snapshots.
        self.snapshot_ids = snapshot_ids
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        # *   **UDM_ECS_DISK**: disk backup subtask of ECS instance backup
        # *   **UDM_DISK**: disk backup
        # 
        # This parameter is required.
        self.source_type = source_type
        # The beginning of the time range to query. The value must be a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the region where the ECS instance resides.
        # 
        # This parameter is required.
        self.udm_region_id = udm_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')

        return self

