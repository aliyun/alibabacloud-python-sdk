# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSnapshotsRequest(DaraModel):
    def __init__(
        self,
        creator: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_scenario: str = None,
        end_time: str = None,
        max_results: int = None,
        next_token: str = None,
        os_type: str = None,
        region_id: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        source_disk_type: str = None,
        start_time: str = None,
    ):
        # The creator.
        self.creator = creator
        # The ID of the cloud desktop.
        self.desktop_id = desktop_id
        # The name of the cloud desktop.
        self.desktop_name = desktop_name
        self.desktop_scenario = desktop_scenario
        # The end time of the snapshot creation. The time is displayed in UTC and follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-mm-ddthh:mm:ssz` format.
        self.end_time = end_time
        # The number of entries to return per page in a paging query.
        self.max_results = max_results
        # The query token. Set the value to the NextToken parameter value returned by the previous API call.
        self.next_token = next_token
        # The operating system type.
        self.os_type = os_type
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the snapshot.
        self.snapshot_id = snapshot_id
        # The display name of the snapshot. The name must be 2 to 127 characters in length. It must start with a letter or a Chinese character, and can contain digits, underscores (_), and hyphens (-). To prevent name conflicts with automatic snapshots, the name cannot start with `auto`.
        self.snapshot_name = snapshot_name
        # The snapshot type.
        self.snapshot_type = snapshot_type
        # The type of the disk for which you want to create a snapshot.
        # 
        # > The values are not case-sensitive.
        self.source_disk_type = source_disk_type
        # The start time of the snapshot creation. The time is displayed in UTC and follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-mm-ddthh:mm:ssz` format.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_scenario is not None:
            result['DesktopScenario'] = self.desktop_scenario

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type

        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopScenario') is not None:
            self.desktop_scenario = m.get('DesktopScenario')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')

        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

