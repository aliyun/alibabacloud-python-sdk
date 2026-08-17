# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListMachineTypesResponseBody(DaraModel):
    def __init__(
        self,
        machine_types: List[main_models.ListMachineTypesResponseBodyMachineTypes] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # Details of the machine types.
        self.machine_types = machine_types
        # The token to request the next page of results. Include this token in your next request to retrieve the next page.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.machine_types:
            for v1 in self.machine_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MachineTypes'] = []
        if self.machine_types is not None:
            for k1 in self.machine_types:
                result['MachineTypes'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.machine_types = []
        if m.get('MachineTypes') is not None:
            for k1 in m.get('MachineTypes'):
                temp_model = main_models.ListMachineTypesResponseBodyMachineTypes()
                self.machine_types.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMachineTypesResponseBodyMachineTypes(DaraModel):
    def __init__(
        self,
        bond_num: int = None,
        cpu_info: str = None,
        cpu_info_detail: main_models.ListMachineTypesResponseBodyMachineTypesCpuInfoDetail = None,
        disk_info: str = None,
        disk_info_detail: main_models.ListMachineTypesResponseBodyMachineTypesDiskInfoDetail = None,
        frontend_network_detail: main_models.ListMachineTypesResponseBodyMachineTypesFrontendNetworkDetail = None,
        gpu_info: str = None,
        gpu_info_detail: main_models.ListMachineTypesResponseBodyMachineTypesGpuInfoDetail = None,
        memory_info: str = None,
        memory_info_detail: main_models.ListMachineTypesResponseBodyMachineTypesMemoryInfoDetail = None,
        name: str = None,
        network_info: str = None,
        node_count: str = None,
        rdma_info_detail: main_models.ListMachineTypesResponseBodyMachineTypesRdmaInfoDetail = None,
        total_cpu_core: int = None,
        type: str = None,
    ):
        # The number of bonds.
        self.bond_num = bond_num
        # CPU information.
        self.cpu_info = cpu_info
        self.cpu_info_detail = cpu_info_detail
        # Disk information.
        self.disk_info = disk_info
        self.disk_info_detail = disk_info_detail
        self.frontend_network_detail = frontend_network_detail
        # GPU information.
        self.gpu_info = gpu_info
        self.gpu_info_detail = gpu_info_detail
        # Memory information.
        self.memory_info = memory_info
        self.memory_info_detail = memory_info_detail
        # The name of the machine type.
        self.name = name
        # Network information.
        self.network_info = network_info
        # The number of nodes.
        self.node_count = node_count
        self.rdma_info_detail = rdma_info_detail
        # The number of CPU cores.
        self.total_cpu_core = total_cpu_core
        # The type of the machine type.
        self.type = type

    def validate(self):
        if self.cpu_info_detail:
            self.cpu_info_detail.validate()
        if self.disk_info_detail:
            self.disk_info_detail.validate()
        if self.frontend_network_detail:
            self.frontend_network_detail.validate()
        if self.gpu_info_detail:
            self.gpu_info_detail.validate()
        if self.memory_info_detail:
            self.memory_info_detail.validate()
        if self.rdma_info_detail:
            self.rdma_info_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bond_num is not None:
            result['BondNum'] = self.bond_num

        if self.cpu_info is not None:
            result['CpuInfo'] = self.cpu_info

        if self.cpu_info_detail is not None:
            result['CpuInfoDetail'] = self.cpu_info_detail.to_map()

        if self.disk_info is not None:
            result['DiskInfo'] = self.disk_info

        if self.disk_info_detail is not None:
            result['DiskInfoDetail'] = self.disk_info_detail.to_map()

        if self.frontend_network_detail is not None:
            result['FrontendNetworkDetail'] = self.frontend_network_detail.to_map()

        if self.gpu_info is not None:
            result['GpuInfo'] = self.gpu_info

        if self.gpu_info_detail is not None:
            result['GpuInfoDetail'] = self.gpu_info_detail.to_map()

        if self.memory_info is not None:
            result['MemoryInfo'] = self.memory_info

        if self.memory_info_detail is not None:
            result['MemoryInfoDetail'] = self.memory_info_detail.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.network_info is not None:
            result['NetworkInfo'] = self.network_info

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.rdma_info_detail is not None:
            result['RdmaInfoDetail'] = self.rdma_info_detail.to_map()

        if self.total_cpu_core is not None:
            result['TotalCpuCore'] = self.total_cpu_core

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondNum') is not None:
            self.bond_num = m.get('BondNum')

        if m.get('CpuInfo') is not None:
            self.cpu_info = m.get('CpuInfo')

        if m.get('CpuInfoDetail') is not None:
            temp_model = main_models.ListMachineTypesResponseBodyMachineTypesCpuInfoDetail()
            self.cpu_info_detail = temp_model.from_map(m.get('CpuInfoDetail'))

        if m.get('DiskInfo') is not None:
            self.disk_info = m.get('DiskInfo')

        if m.get('DiskInfoDetail') is not None:
            temp_model = main_models.ListMachineTypesResponseBodyMachineTypesDiskInfoDetail()
            self.disk_info_detail = temp_model.from_map(m.get('DiskInfoDetail'))

        if m.get('FrontendNetworkDetail') is not None:
            temp_model = main_models.ListMachineTypesResponseBodyMachineTypesFrontendNetworkDetail()
            self.frontend_network_detail = temp_model.from_map(m.get('FrontendNetworkDetail'))

        if m.get('GpuInfo') is not None:
            self.gpu_info = m.get('GpuInfo')

        if m.get('GpuInfoDetail') is not None:
            temp_model = main_models.ListMachineTypesResponseBodyMachineTypesGpuInfoDetail()
            self.gpu_info_detail = temp_model.from_map(m.get('GpuInfoDetail'))

        if m.get('MemoryInfo') is not None:
            self.memory_info = m.get('MemoryInfo')

        if m.get('MemoryInfoDetail') is not None:
            temp_model = main_models.ListMachineTypesResponseBodyMachineTypesMemoryInfoDetail()
            self.memory_info_detail = temp_model.from_map(m.get('MemoryInfoDetail'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkInfo') is not None:
            self.network_info = m.get('NetworkInfo')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('RdmaInfoDetail') is not None:
            temp_model = main_models.ListMachineTypesResponseBodyMachineTypesRdmaInfoDetail()
            self.rdma_info_detail = temp_model.from_map(m.get('RdmaInfoDetail'))

        if m.get('TotalCpuCore') is not None:
            self.total_cpu_core = m.get('TotalCpuCore')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListMachineTypesResponseBodyMachineTypesRdmaInfoDetail(DaraModel):
    def __init__(
        self,
        backend_rdma_nic_bw_in_gbps: int = None,
        backend_rdma_nic_count: int = None,
    ):
        self.backend_rdma_nic_bw_in_gbps = backend_rdma_nic_bw_in_gbps
        self.backend_rdma_nic_count = backend_rdma_nic_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_rdma_nic_bw_in_gbps is not None:
            result['BackendRdmaNicBwInGbps'] = self.backend_rdma_nic_bw_in_gbps

        if self.backend_rdma_nic_count is not None:
            result['BackendRdmaNicCount'] = self.backend_rdma_nic_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendRdmaNicBwInGbps') is not None:
            self.backend_rdma_nic_bw_in_gbps = m.get('BackendRdmaNicBwInGbps')

        if m.get('BackendRdmaNicCount') is not None:
            self.backend_rdma_nic_count = m.get('BackendRdmaNicCount')

        return self

class ListMachineTypesResponseBodyMachineTypesMemoryInfoDetail(DaraModel):
    def __init__(
        self,
        memory_size_in_gb: int = None,
    ):
        self.memory_size_in_gb = memory_size_in_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.memory_size_in_gb is not None:
            result['MemorySizeInGB'] = self.memory_size_in_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemorySizeInGB') is not None:
            self.memory_size_in_gb = m.get('MemorySizeInGB')

        return self

class ListMachineTypesResponseBodyMachineTypesGpuInfoDetail(DaraModel):
    def __init__(
        self,
        gpu_count: int = None,
        gpu_memory_in_gb: int = None,
        gpu_name: str = None,
        gpu_vendor: str = None,
        total_gpu_memory_in_gb: int = None,
    ):
        self.gpu_count = gpu_count
        self.gpu_memory_in_gb = gpu_memory_in_gb
        self.gpu_name = gpu_name
        self.gpu_vendor = gpu_vendor
        self.total_gpu_memory_in_gb = total_gpu_memory_in_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count

        if self.gpu_memory_in_gb is not None:
            result['GpuMemoryInGB'] = self.gpu_memory_in_gb

        if self.gpu_name is not None:
            result['GpuName'] = self.gpu_name

        if self.gpu_vendor is not None:
            result['GpuVendor'] = self.gpu_vendor

        if self.total_gpu_memory_in_gb is not None:
            result['TotalGpuMemoryInGB'] = self.total_gpu_memory_in_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')

        if m.get('GpuMemoryInGB') is not None:
            self.gpu_memory_in_gb = m.get('GpuMemoryInGB')

        if m.get('GpuName') is not None:
            self.gpu_name = m.get('GpuName')

        if m.get('GpuVendor') is not None:
            self.gpu_vendor = m.get('GpuVendor')

        if m.get('TotalGpuMemoryInGB') is not None:
            self.total_gpu_memory_in_gb = m.get('TotalGpuMemoryInGB')

        return self

class ListMachineTypesResponseBodyMachineTypesFrontendNetworkDetail(DaraModel):
    def __init__(
        self,
        frontend_network_type: str = None,
        jumbo_frame_supported: bool = None,
    ):
        self.frontend_network_type = frontend_network_type
        self.jumbo_frame_supported = jumbo_frame_supported

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frontend_network_type is not None:
            result['FrontendNetworkType'] = self.frontend_network_type

        if self.jumbo_frame_supported is not None:
            result['JumboFrameSupported'] = self.jumbo_frame_supported

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontendNetworkType') is not None:
            self.frontend_network_type = m.get('FrontendNetworkType')

        if m.get('JumboFrameSupported') is not None:
            self.jumbo_frame_supported = m.get('JumboFrameSupported')

        return self

class ListMachineTypesResponseBodyMachineTypesDiskInfoDetail(DaraModel):
    def __init__(
        self,
        local_disk_count: int = None,
        local_disk_size_in_tb: float = None,
        local_disk_type: str = None,
    ):
        self.local_disk_count = local_disk_count
        self.local_disk_size_in_tb = local_disk_size_in_tb
        self.local_disk_type = local_disk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_disk_count is not None:
            result['LocalDiskCount'] = self.local_disk_count

        if self.local_disk_size_in_tb is not None:
            result['LocalDiskSizeInTB'] = self.local_disk_size_in_tb

        if self.local_disk_type is not None:
            result['LocalDiskType'] = self.local_disk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalDiskCount') is not None:
            self.local_disk_count = m.get('LocalDiskCount')

        if m.get('LocalDiskSizeInTB') is not None:
            self.local_disk_size_in_tb = m.get('LocalDiskSizeInTB')

        if m.get('LocalDiskType') is not None:
            self.local_disk_type = m.get('LocalDiskType')

        return self

class ListMachineTypesResponseBodyMachineTypesCpuInfoDetail(DaraModel):
    def __init__(
        self,
        cpu_arch: str = None,
        cpu_sockets: int = None,
        vcpu_cores: int = None,
    ):
        self.cpu_arch = cpu_arch
        self.cpu_sockets = cpu_sockets
        self.vcpu_cores = vcpu_cores

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_arch is not None:
            result['CpuArch'] = self.cpu_arch

        if self.cpu_sockets is not None:
            result['CpuSockets'] = self.cpu_sockets

        if self.vcpu_cores is not None:
            result['VCpuCores'] = self.vcpu_cores

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuArch') is not None:
            self.cpu_arch = m.get('CpuArch')

        if m.get('CpuSockets') is not None:
            self.cpu_sockets = m.get('CpuSockets')

        if m.get('VCpuCores') is not None:
            self.vcpu_cores = m.get('VCpuCores')

        return self

