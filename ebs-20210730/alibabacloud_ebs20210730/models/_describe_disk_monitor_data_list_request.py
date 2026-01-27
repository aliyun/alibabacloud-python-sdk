# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiskMonitorDataListRequest(DaraModel):
    def __init__(
        self,
        disk_ids: str = None,
        end_time: str = None,
        max_results: str = None,
        next_token: str = None,
        region_id: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The IDs of the disks. The value is a JSON array that contains multiple disk IDs. Separate the IDs with commas (,).
        self.disk_ids = disk_ids
        # The end of the time range during which you want to query the near real-time monitoring data of the disks. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The number of entries per page. If you specify this parameter, both `MaxResults` and `NextToken` are used for a paged query.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in this request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/354276.html) operation to query the list of regions that support CloudLens for EBS.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range during which you want to query the near real-time monitoring data of the disks. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type of the monitoring data. Set the value to pro.
        # 
        # pro: burst performance data, such as burst I/O operations.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

