# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudGtmSummaryResponseBody(DaraModel):
    def __init__(
        self,
        instance_total_count: int = None,
        monitor_task_total_count: int = None,
        monitor_task_total_quota: int = None,
        request_id: str = None,
    ):
        # The total number of instances within the current account.
        self.instance_total_count = instance_total_count
        # The total number of configured health check tasks.
        self.monitor_task_total_count = monitor_task_total_count
        # The quota on the number of health check tasks.
        self.monitor_task_total_quota = monitor_task_total_quota
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_total_count is not None:
            result['InstanceTotalCount'] = self.instance_total_count

        if self.monitor_task_total_count is not None:
            result['MonitorTaskTotalCount'] = self.monitor_task_total_count

        if self.monitor_task_total_quota is not None:
            result['MonitorTaskTotalQuota'] = self.monitor_task_total_quota

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTotalCount') is not None:
            self.instance_total_count = m.get('InstanceTotalCount')

        if m.get('MonitorTaskTotalCount') is not None:
            self.monitor_task_total_count = m.get('MonitorTaskTotalCount')

        if m.get('MonitorTaskTotalQuota') is not None:
            self.monitor_task_total_quota = m.get('MonitorTaskTotalQuota')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

