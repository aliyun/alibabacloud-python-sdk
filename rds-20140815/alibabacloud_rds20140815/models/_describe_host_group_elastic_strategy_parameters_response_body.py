# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHostGroupElasticStrategyParametersResponseBody(DaraModel):
    def __init__(
        self,
        cpu_shar: int = None,
        cpu_zoom: int = None,
        iops_zoom: int = None,
        max_conn_zoom: int = None,
        memory_zoom: int = None,
        request_id: str = None,
    ):
        # The CPU utilization of the instance. Unit: percentage.
        self.cpu_shar = cpu_shar
        # The number of CPU cores used by the instance. Unit: cores.
        self.cpu_zoom = cpu_zoom
        # The number of I/O requests.
        self.iops_zoom = iops_zoom
        # The maximum number of concurrent connections supported by the instance type.
        self.max_conn_zoom = max_conn_zoom
        # The total memory size of the instance in the dedicated cluster. Unit: MB.
        self.memory_zoom = memory_zoom
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_shar is not None:
            result['CpuShar'] = self.cpu_shar

        if self.cpu_zoom is not None:
            result['CpuZoom'] = self.cpu_zoom

        if self.iops_zoom is not None:
            result['IopsZoom'] = self.iops_zoom

        if self.max_conn_zoom is not None:
            result['MaxConnZoom'] = self.max_conn_zoom

        if self.memory_zoom is not None:
            result['MemoryZoom'] = self.memory_zoom

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuShar') is not None:
            self.cpu_shar = m.get('CpuShar')

        if m.get('CpuZoom') is not None:
            self.cpu_zoom = m.get('CpuZoom')

        if m.get('IopsZoom') is not None:
            self.iops_zoom = m.get('IopsZoom')

        if m.get('MaxConnZoom') is not None:
            self.max_conn_zoom = m.get('MaxConnZoom')

        if m.get('MemoryZoom') is not None:
            self.memory_zoom = m.get('MemoryZoom')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

