# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDatabaseInstanceMetricDataResponseBody(DaraModel):
    def __init__(
        self,
        data_format: str = None,
        metric_data: str = None,
        metric_name: str = None,
        request_id: str = None,
        unit: str = None,
    ):
        # The format of the metric data. Valid values:
        # 
        # - `cpuusage&memusage`
        # 
        # - `active_session&total_session`
        # 
        # - `ins_size&data_size&log_size&tmp_size&other_size`
        # 
        # - `io`
        self.data_format = data_format
        # The metric data details.
        self.metric_data = metric_data
        # The name of the metric. Valid values:
        # 
        # - `MySQL_MemCpuUsage`: The CPU utilization and memory usage of the instance, as a percentage of the total resources of the operating system.
        # 
        # - `MySQL_DetailedSpaceUsage`: The total, data, log, temporary, and system disk space usage of the instance.
        # 
        # - `MySQL_Sessions`: The number of active and total connections.
        # 
        # - `MySQL_IOPS`: The IOPS of the instance.
        self.metric_name = metric_name
        # The request ID.
        self.request_id = request_id
        # The unit of the metric data.
        # 
        # - %
        # 
        # - int
        # 
        # - MB
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_format is not None:
            result['DataFormat'] = self.data_format

        if self.metric_data is not None:
            result['MetricData'] = self.metric_data

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')

        if m.get('MetricData') is not None:
            self.metric_data = m.get('MetricData')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

