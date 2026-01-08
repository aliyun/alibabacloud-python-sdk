# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class ListEcsSpecsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        ecs_specs: List[main_models.ListEcsSpecsResponseBodyEcsSpecs] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The specifications of the ECS instances returned on this page.
        self.ecs_specs = ecs_specs
        # The HTTP status code. Valid values:
        # 
        # *   400
        # *   404
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of ECS instances.
        self.total_count = total_count

    def validate(self):
        if self.ecs_specs:
            for v1 in self.ecs_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['EcsSpecs'] = []
        if self.ecs_specs is not None:
            for k1 in self.ecs_specs:
                result['EcsSpecs'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.ecs_specs = []
        if m.get('EcsSpecs') is not None:
            for k1 in m.get('EcsSpecs'):
                temp_model = main_models.ListEcsSpecsResponseBodyEcsSpecs()
                self.ecs_specs.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEcsSpecsResponseBodyEcsSpecs(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        cpu: int = None,
        currency: str = None,
        gpu: int = None,
        gpumemory_size: float = None,
        gputype: str = None,
        instance_bandwidth_rx: int = None,
        instance_type: str = None,
        is_available: bool = None,
        labels: List[main_models.ListEcsSpecsResponseBodyEcsSpecsLabels] = None,
        memory: float = None,
        price: float = None,
        spot_stock_status: str = None,
        system_disk_capacity: int = None,
    ):
        # The accelerator type.
        self.accelerator_type = accelerator_type
        # The number of vCPUs.
        self.cpu = cpu
        # The currency unit.
        self.currency = currency
        # The number of GPUs.
        self.gpu = gpu
        self.gpumemory_size = gpumemory_size
        # The GPU type. Valid values:
        # 
        # *   V100
        # *   A100
        # *   A10
        # *   T4
        # *   P100
        self.gputype = gputype
        # The inbound bandwidth of the instance.
        self.instance_bandwidth_rx = instance_bandwidth_rx
        # The instance type.
        self.instance_type = instance_type
        # Indicates whether the resource was available.
        self.is_available = is_available
        # The labels of the ECS specification.
        self.labels = labels
        # The memory size. Unit: GB.
        self.memory = memory
        # The price.
        self.price = price
        self.spot_stock_status = spot_stock_status
        # The size of the system disk. Unit: GB.
        self.system_disk_capacity = system_disk_capacity

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.gpumemory_size is not None:
            result['GPUMemorySize'] = self.gpumemory_size

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.instance_bandwidth_rx is not None:
            result['InstanceBandwidthRx'] = self.instance_bandwidth_rx

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_available is not None:
            result['IsAvailable'] = self.is_available

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.price is not None:
            result['Price'] = self.price

        if self.spot_stock_status is not None:
            result['SpotStockStatus'] = self.spot_stock_status

        if self.system_disk_capacity is not None:
            result['SystemDiskCapacity'] = self.system_disk_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUMemorySize') is not None:
            self.gpumemory_size = m.get('GPUMemorySize')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('InstanceBandwidthRx') is not None:
            self.instance_bandwidth_rx = m.get('InstanceBandwidthRx')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ListEcsSpecsResponseBodyEcsSpecsLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('SpotStockStatus') is not None:
            self.spot_stock_status = m.get('SpotStockStatus')

        if m.get('SystemDiskCapacity') is not None:
            self.system_disk_capacity = m.get('SystemDiskCapacity')

        return self

class ListEcsSpecsResponseBodyEcsSpecsLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The label key added to the ECS specification.
        self.key = key
        # The label value added to the ECS specification.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

