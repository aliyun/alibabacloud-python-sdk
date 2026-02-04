# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterUsedUtilizationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        cpu_total: float = None,
        dedicated_cluster_id: str = None,
        disk_total: float = None,
        disk_used: float = None,
        du_total: int = None,
        du_used: int = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        memory_total: float = None,
        memory_used: float = None,
        memory_used_percentage: float = None,
        request_id: str = None,
        success: bool = None,
        task_running: int = None,
    ):
        # The error code returned by the backend service. The number is incremented.
        self.code = code
        # The CPU utilization of the cluster. Unit: percentage.
        self.cpu_total = cpu_total
        # The ID of the cluster.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The total disk size of the cluster. Unit: GB.
        self.disk_total = disk_total
        # The disk usage of the cluster. Unit: GB.
        self.disk_used = disk_used
        # The total number of DTS units (DUs).
        self.du_total = du_total
        # The usage of DUs.
        self.du_used = du_used
        # The dynamic part in the error message. This parameter is used to replace %s in the ErrMessage parameter.
        self.dynamic_message = dynamic_message
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The total amount of memory. A value of 0 is temporarily returned.
        self.memory_total = memory_total
        # The memory usage. A value of 0 is temporarily returned.
        self.memory_used = memory_used
        # The memory usage.
        self.memory_used_percentage = memory_used_percentage
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The number of tasks that are in progress.
        self.task_running = task_running

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.cpu_total is not None:
            result['CpuTotal'] = self.cpu_total

        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.disk_total is not None:
            result['DiskTotal'] = self.disk_total

        if self.disk_used is not None:
            result['DiskUsed'] = self.disk_used

        if self.du_total is not None:
            result['DuTotal'] = self.du_total

        if self.du_used is not None:
            result['DuUsed'] = self.du_used

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.memory_total is not None:
            result['MemoryTotal'] = self.memory_total

        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used

        if self.memory_used_percentage is not None:
            result['MemoryUsedPercentage'] = self.memory_used_percentage

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_running is not None:
            result['TaskRunning'] = self.task_running

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CpuTotal') is not None:
            self.cpu_total = m.get('CpuTotal')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('DiskTotal') is not None:
            self.disk_total = m.get('DiskTotal')

        if m.get('DiskUsed') is not None:
            self.disk_used = m.get('DiskUsed')

        if m.get('DuTotal') is not None:
            self.du_total = m.get('DuTotal')

        if m.get('DuUsed') is not None:
            self.du_used = m.get('DuUsed')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MemoryTotal') is not None:
            self.memory_total = m.get('MemoryTotal')

        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')

        if m.get('MemoryUsedPercentage') is not None:
            self.memory_used_percentage = m.get('MemoryUsedPercentage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskRunning') is not None:
            self.task_running = m.get('TaskRunning')

        return self

