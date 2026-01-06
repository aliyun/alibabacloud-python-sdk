# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApsMigrationWorkloadsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        oss_location: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        workload_name: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query.
        self.end_time = end_time
        # The Object Storage Service (OSS) URL.
        self.oss_location = oss_location
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The start of the time range to query.
        self.start_time = start_time
        # The name of the workload.
        self.workload_name = workload_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.oss_location is not None:
            result['OssLocation'] = self.oss_location

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OssLocation') is not None:
            self.oss_location = m.get('OssLocation')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')

        return self

