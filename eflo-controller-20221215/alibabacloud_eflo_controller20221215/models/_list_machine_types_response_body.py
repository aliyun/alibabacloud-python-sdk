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
        # The instance types.
        self.machine_types = machine_types
        # The token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
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
        disk_info: str = None,
        gpu_info: str = None,
        memory_info: str = None,
        name: str = None,
        network_info: str = None,
        node_count: str = None,
        total_cpu_core: int = None,
        type: str = None,
    ):
        # The number of bonds.
        self.bond_num = bond_num
        # The CPU information.
        self.cpu_info = cpu_info
        # The disk information.
        self.disk_info = disk_info
        # The GPU information.
        self.gpu_info = gpu_info
        # The storage information.
        self.memory_info = memory_info
        # The name of the instance type.
        self.name = name
        # The network information.
        self.network_info = network_info
        # The number of nodes.
        self.node_count = node_count
        # The number of vCPUs.
        self.total_cpu_core = total_cpu_core
        # The access type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bond_num is not None:
            result['BondNum'] = self.bond_num

        if self.cpu_info is not None:
            result['CpuInfo'] = self.cpu_info

        if self.disk_info is not None:
            result['DiskInfo'] = self.disk_info

        if self.gpu_info is not None:
            result['GpuInfo'] = self.gpu_info

        if self.memory_info is not None:
            result['MemoryInfo'] = self.memory_info

        if self.name is not None:
            result['Name'] = self.name

        if self.network_info is not None:
            result['NetworkInfo'] = self.network_info

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

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

        if m.get('DiskInfo') is not None:
            self.disk_info = m.get('DiskInfo')

        if m.get('GpuInfo') is not None:
            self.gpu_info = m.get('GpuInfo')

        if m.get('MemoryInfo') is not None:
            self.memory_info = m.get('MemoryInfo')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkInfo') is not None:
            self.network_info = m.get('NetworkInfo')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('TotalCpuCore') is not None:
            self.total_cpu_core = m.get('TotalCpuCore')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

