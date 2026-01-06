# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPfsMetricTrendsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        metric: str = None,
        node_id: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The end time must be later than the start time. You can view the data of up to seven days in the previous 30 days.
        self.end_time = end_time
        # The instance ID.
        self.instance_id = instance_id
        # The metric whose trend you want to query. Valid values:
        # 
        # *   **count**: the number of executions.
        # *   **avgRt**: the average execution duration.
        # *   **rtRate**: the execution duration percentage.
        # *   **rowsExamined**: the total number of scanned rows.
        self.metric = metric
        # The node ID.
        # 
        # >  This parameter is required if the database instance is an ApsaraDB RDS for MySQL Cluster Edition instance or a PolarDB for MySQL clusters.
        self.node_id = node_id
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

