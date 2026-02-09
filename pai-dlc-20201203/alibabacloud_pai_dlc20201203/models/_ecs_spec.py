# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class EcsSpec(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        cpu: int = None,
        default_gpudriver: str = None,
        gpu: int = None,
        gpu_memory: int = None,
        gpu_type: str = None,
        instance_type: str = None,
        is_available: bool = None,
        memory: int = None,
        non_protect_spot_discount: float = None,
        payment_types: List[str] = None,
        resource_type: str = None,
        spot_stock_status: str = None,
        supported_gpudrivers: List[str] = None,
    ):
        # The accelerator type. Valid values:
        # 
        # *   CPU
        # *   GPU
        self.accelerator_type = accelerator_type
        # The number of CPU cores.
        self.cpu = cpu
        # The default GPU driver version.
        self.default_gpudriver = default_gpudriver
        # The number of GPUs.
        self.gpu = gpu
        # The GPU memory size.
        self.gpu_memory = gpu_memory
        # The GPU type.
        self.gpu_type = gpu_type
        # The instance type.
        self.instance_type = instance_type
        # Indicates whether the instance type is available. Valid values:
        # 
        # *   true
        # *   false
        self.is_available = is_available
        # The memory size. Unit: MiB or GiB.
        self.memory = memory
        # The discount on the current price of the preemptible instance.
        self.non_protect_spot_discount = non_protect_spot_discount
        # The billing methods.
        self.payment_types = payment_types
        # The resource type. Valid values:
        # 
        # *   ECS
        # *   Lingjun
        self.resource_type = resource_type
        # The inventory status of preemptible instance.
        self.spot_stock_status = spot_stock_status
        # The GPU driver versions.
        self.supported_gpudrivers = supported_gpudrivers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.default_gpudriver is not None:
            result['DefaultGPUDriver'] = self.default_gpudriver

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory

        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_available is not None:
            result['IsAvailable'] = self.is_available

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.non_protect_spot_discount is not None:
            result['NonProtectSpotDiscount'] = self.non_protect_spot_discount

        if self.payment_types is not None:
            result['PaymentTypes'] = self.payment_types

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.spot_stock_status is not None:
            result['SpotStockStatus'] = self.spot_stock_status

        if self.supported_gpudrivers is not None:
            result['SupportedGPUDrivers'] = self.supported_gpudrivers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DefaultGPUDriver') is not None:
            self.default_gpudriver = m.get('DefaultGPUDriver')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')

        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NonProtectSpotDiscount') is not None:
            self.non_protect_spot_discount = m.get('NonProtectSpotDiscount')

        if m.get('PaymentTypes') is not None:
            self.payment_types = m.get('PaymentTypes')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SpotStockStatus') is not None:
            self.spot_stock_status = m.get('SpotStockStatus')

        if m.get('SupportedGPUDrivers') is not None:
            self.supported_gpudrivers = m.get('SupportedGPUDrivers')

        return self

