# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDesktopTypesResponseBody(DaraModel):
    def __init__(
        self,
        desktop_types: List[main_models.DescribeDesktopTypesResponseBodyDesktopTypes] = None,
        request_id: str = None,
    ):
        # The specifications.
        self.desktop_types = desktop_types
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.desktop_types:
            for v1 in self.desktop_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DesktopTypes'] = []
        if self.desktop_types is not None:
            for k1 in self.desktop_types:
                result['DesktopTypes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktop_types = []
        if m.get('DesktopTypes') is not None:
            for k1 in m.get('DesktopTypes'):
                temp_model = main_models.DescribeDesktopTypesResponseBodyDesktopTypes()
                self.desktop_types.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDesktopTypesResponseBodyDesktopTypes(DaraModel):
    def __init__(
        self,
        cpu_count: str = None,
        data_disk_size: str = None,
        description: str = None,
        desktop_type_id: str = None,
        desktop_type_status: str = None,
        gpu_count: float = None,
        gpu_memory: int = None,
        gpu_spec: str = None,
        instance_type_family: str = None,
        max_session_count: int = None,
        memory_size: str = None,
        scopes: List[str] = None,
        stock_state: str = None,
        system_disk_size: str = None,
    ):
        # The number of vCPUs.
        self.cpu_count = cpu_count
        # The size of the data disk. Unit: GiB.
        self.data_disk_size = data_disk_size
        self.description = description
        # The ID of the cloud desktop type.
        self.desktop_type_id = desktop_type_id
        # The status of the cloud desktop type. If SUFFICIENT is returned, the number of cloud desktops of the type is sufficient.
        self.desktop_type_status = desktop_type_status
        # The number of GPUs.
        self.gpu_count = gpu_count
        # The GPU memory size. For GPU-accelerated cloud computers, this return value is significant. Unit: MB.
        self.gpu_memory = gpu_memory
        # The GPU memory.
        self.gpu_spec = gpu_spec
        # The family of the cloud desktop type.
        self.instance_type_family = instance_type_family
        # The number of sessions supported by the specification.
        self.max_session_count = max_session_count
        # The memory size. Unit: MiB.
        self.memory_size = memory_size
        # The sales modes of the specifications.
        self.scopes = scopes
        # The inventory status of the specification.
        # 
        # Valid values:
        # 
        # *   Insufficient
        # *   Sufficient
        self.stock_state = stock_state
        # The size of the system disk. Unit: GiB.
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.description is not None:
            result['Description'] = self.description

        if self.desktop_type_id is not None:
            result['DesktopTypeId'] = self.desktop_type_id

        if self.desktop_type_status is not None:
            result['DesktopTypeStatus'] = self.desktop_type_status

        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count

        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory

        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.max_session_count is not None:
            result['MaxSessionCount'] = self.max_session_count

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.scopes is not None:
            result['Scopes'] = self.scopes

        if self.stock_state is not None:
            result['StockState'] = self.stock_state

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesktopTypeId') is not None:
            self.desktop_type_id = m.get('DesktopTypeId')

        if m.get('DesktopTypeStatus') is not None:
            self.desktop_type_status = m.get('DesktopTypeStatus')

        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')

        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')

        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('MaxSessionCount') is not None:
            self.max_session_count = m.get('MaxSessionCount')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('Scopes') is not None:
            self.scopes = m.get('Scopes')

        if m.get('StockState') is not None:
            self.stock_state = m.get('StockState')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

