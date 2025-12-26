# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class QuotaNodeViewMetric(DaraModel):
    def __init__(
        self,
        cpuusage_rate: str = None,
        created_time: str = None,
        disk_read_rate: str = None,
        disk_write_rate: str = None,
        gputype: str = None,
        memory_usage_rate: str = None,
        network_input_rate: str = None,
        network_output_rate: str = None,
        node_id: str = None,
        node_status: str = None,
        node_type: str = None,
        quota_id: str = None,
        request_cpu: int = None,
        request_gpu: int = None,
        request_memory: int = None,
        task_id_map: Dict[str, Any] = None,
        total_cpu: int = None,
        total_gpu: int = None,
        total_memory: int = None,
        total_tasks: int = None,
        user_ids: List[str] = None,
        user_number: str = None,
    ):
        self.cpuusage_rate = cpuusage_rate
        self.created_time = created_time
        self.disk_read_rate = disk_read_rate
        self.disk_write_rate = disk_write_rate
        self.gputype = gputype
        self.memory_usage_rate = memory_usage_rate
        self.network_input_rate = network_input_rate
        self.network_output_rate = network_output_rate
        self.node_id = node_id
        self.node_status = node_status
        self.node_type = node_type
        self.quota_id = quota_id
        self.request_cpu = request_cpu
        self.request_gpu = request_gpu
        self.request_memory = request_memory
        self.task_id_map = task_id_map
        self.total_cpu = total_cpu
        self.total_gpu = total_gpu
        self.total_memory = total_memory
        self.total_tasks = total_tasks
        self.user_ids = user_ids
        self.user_number = user_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpuusage_rate is not None:
            result['CPUUsageRate'] = self.cpuusage_rate

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.disk_read_rate is not None:
            result['DiskReadRate'] = self.disk_read_rate

        if self.disk_write_rate is not None:
            result['DiskWriteRate'] = self.disk_write_rate

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.memory_usage_rate is not None:
            result['MemoryUsageRate'] = self.memory_usage_rate

        if self.network_input_rate is not None:
            result['NetworkInputRate'] = self.network_input_rate

        if self.network_output_rate is not None:
            result['NetworkOutputRate'] = self.network_output_rate

        if self.node_id is not None:
            result['NodeID'] = self.node_id

        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu

        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu

        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory

        if self.task_id_map is not None:
            result['TaskIdMap'] = self.task_id_map

        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu

        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu

        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory

        if self.total_tasks is not None:
            result['TotalTasks'] = self.total_tasks

        if self.user_ids is not None:
            result['UserIDs'] = self.user_ids

        if self.user_number is not None:
            result['UserNumber'] = self.user_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPUUsageRate') is not None:
            self.cpuusage_rate = m.get('CPUUsageRate')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DiskReadRate') is not None:
            self.disk_read_rate = m.get('DiskReadRate')

        if m.get('DiskWriteRate') is not None:
            self.disk_write_rate = m.get('DiskWriteRate')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('MemoryUsageRate') is not None:
            self.memory_usage_rate = m.get('MemoryUsageRate')

        if m.get('NetworkInputRate') is not None:
            self.network_input_rate = m.get('NetworkInputRate')

        if m.get('NetworkOutputRate') is not None:
            self.network_output_rate = m.get('NetworkOutputRate')

        if m.get('NodeID') is not None:
            self.node_id = m.get('NodeID')

        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')

        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')

        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')

        if m.get('TaskIdMap') is not None:
            self.task_id_map = m.get('TaskIdMap')

        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')

        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')

        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')

        if m.get('TotalTasks') is not None:
            self.total_tasks = m.get('TotalTasks')

        if m.get('UserIDs') is not None:
            self.user_ids = m.get('UserIDs')

        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')

        return self

