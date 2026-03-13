# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QuotaUserViewMetric(DaraModel):
    def __init__(
        self,
        cpunode_number: int = None,
        cpuusage_rate: str = None,
        cpu_job_names: List[str] = None,
        cpu_node_names: List[str] = None,
        disk_read_rate: str = None,
        disk_write_rate: str = None,
        gpunode_number: int = None,
        gpuusage_rate: str = None,
        gpu_job_names: List[str] = None,
        gpu_node_names: List[str] = None,
        job_type: str = None,
        memory_usage_rate: str = None,
        network_input_rate: str = None,
        network_output_rate: str = None,
        node_names: List[str] = None,
        request_cpu: int = None,
        request_gpu: int = None,
        request_memory: int = None,
        total_cpu: int = None,
        total_gpu: int = None,
        total_memory: int = None,
        user_id: str = None,
    ):
        self.cpunode_number = cpunode_number
        self.cpuusage_rate = cpuusage_rate
        self.cpu_job_names = cpu_job_names
        self.cpu_node_names = cpu_node_names
        self.disk_read_rate = disk_read_rate
        self.disk_write_rate = disk_write_rate
        self.gpunode_number = gpunode_number
        self.gpuusage_rate = gpuusage_rate
        self.gpu_job_names = gpu_job_names
        self.gpu_node_names = gpu_node_names
        self.job_type = job_type
        self.memory_usage_rate = memory_usage_rate
        self.network_input_rate = network_input_rate
        self.network_output_rate = network_output_rate
        self.node_names = node_names
        self.request_cpu = request_cpu
        self.request_gpu = request_gpu
        self.request_memory = request_memory
        self.total_cpu = total_cpu
        self.total_gpu = total_gpu
        self.total_memory = total_memory
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpunode_number is not None:
            result['CPUNodeNumber'] = self.cpunode_number

        if self.cpuusage_rate is not None:
            result['CPUUsageRate'] = self.cpuusage_rate

        if self.cpu_job_names is not None:
            result['CpuJobNames'] = self.cpu_job_names

        if self.cpu_node_names is not None:
            result['CpuNodeNames'] = self.cpu_node_names

        if self.disk_read_rate is not None:
            result['DiskReadRate'] = self.disk_read_rate

        if self.disk_write_rate is not None:
            result['DiskWriteRate'] = self.disk_write_rate

        if self.gpunode_number is not None:
            result['GPUNodeNumber'] = self.gpunode_number

        if self.gpuusage_rate is not None:
            result['GPUUsageRate'] = self.gpuusage_rate

        if self.gpu_job_names is not None:
            result['GpuJobNames'] = self.gpu_job_names

        if self.gpu_node_names is not None:
            result['GpuNodeNames'] = self.gpu_node_names

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.memory_usage_rate is not None:
            result['MemoryUsageRate'] = self.memory_usage_rate

        if self.network_input_rate is not None:
            result['NetworkInputRate'] = self.network_input_rate

        if self.network_output_rate is not None:
            result['NetworkOutputRate'] = self.network_output_rate

        if self.node_names is not None:
            result['NodeNames'] = self.node_names

        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu

        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu

        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory

        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu

        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu

        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPUNodeNumber') is not None:
            self.cpunode_number = m.get('CPUNodeNumber')

        if m.get('CPUUsageRate') is not None:
            self.cpuusage_rate = m.get('CPUUsageRate')

        if m.get('CpuJobNames') is not None:
            self.cpu_job_names = m.get('CpuJobNames')

        if m.get('CpuNodeNames') is not None:
            self.cpu_node_names = m.get('CpuNodeNames')

        if m.get('DiskReadRate') is not None:
            self.disk_read_rate = m.get('DiskReadRate')

        if m.get('DiskWriteRate') is not None:
            self.disk_write_rate = m.get('DiskWriteRate')

        if m.get('GPUNodeNumber') is not None:
            self.gpunode_number = m.get('GPUNodeNumber')

        if m.get('GPUUsageRate') is not None:
            self.gpuusage_rate = m.get('GPUUsageRate')

        if m.get('GpuJobNames') is not None:
            self.gpu_job_names = m.get('GpuJobNames')

        if m.get('GpuNodeNames') is not None:
            self.gpu_node_names = m.get('GpuNodeNames')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MemoryUsageRate') is not None:
            self.memory_usage_rate = m.get('MemoryUsageRate')

        if m.get('NetworkInputRate') is not None:
            self.network_input_rate = m.get('NetworkInputRate')

        if m.get('NetworkOutputRate') is not None:
            self.network_output_rate = m.get('NetworkOutputRate')

        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')

        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')

        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')

        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')

        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')

        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')

        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

