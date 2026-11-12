# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDatabaseInstanceMetricDataRequest(DaraModel):
    def __init__(
        self,
        database_instance_id: str = None,
        end_time: str = None,
        metric_name: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The ID of the lightweight database instance.
        # 
        # This parameter is required.
        self.database_instance_id = database_instance_id
        # The end of the time range to query. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mmZ` format. The time must be in UTC.
        # 
        # > The time in the console is displayed in UTC+8.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The name of the metric. Valid values:
        # 
        # - `MySQL_MemCpuUsage`: The CPU utilization and memory usage of the instance, as a percentage of the total resources of the operating system.
        # 
        # - `MySQL_DetailedSpaceUsage`: The total, data, log, temporary, and system disk space usage of the instance.
        # 
        # - `MySQL_Sessions`: The number of active and total connections.
        # 
        # - `MySQL_IOPS`: The IOPS of the instance.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The region ID of the lightweight database instance. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to get the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start of the time range to query. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mmZ` format. The time must be in UTC.
        # 
        # > The time in the console is displayed in UTC+8.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

