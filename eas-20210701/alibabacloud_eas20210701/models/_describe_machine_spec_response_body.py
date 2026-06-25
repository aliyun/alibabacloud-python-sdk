# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DescribeMachineSpecResponseBody(DaraModel):
    def __init__(
        self,
        instance_metas: List[main_models.DescribeMachineSpecResponseBodyInstanceMetas] = None,
        request_id: str = None,
        types: List[main_models.DescribeMachineSpecResponseBodyTypes] = None,
    ):
        # A list of available instance types for deployment.
        self.instance_metas = instance_metas
        # The request ID.
        self.request_id = request_id
        # The supported combinations of CPU and memory values for deployment.
        self.types = types

    def validate(self):
        if self.instance_metas:
            for v1 in self.instance_metas:
                 if v1:
                    v1.validate()
        if self.types:
            for v1 in self.types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceMetas'] = []
        if self.instance_metas is not None:
            for k1 in self.instance_metas:
                result['InstanceMetas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Types'] = []
        if self.types is not None:
            for k1 in self.types:
                result['Types'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_metas = []
        if m.get('InstanceMetas') is not None:
            for k1 in m.get('InstanceMetas'):
                temp_model = main_models.DescribeMachineSpecResponseBodyInstanceMetas()
                self.instance_metas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.types = []
        if m.get('Types') is not None:
            for k1 in m.get('Types'):
                temp_model = main_models.DescribeMachineSpecResponseBodyTypes()
                self.types.append(temp_model.from_map(k1))

        return self

class DescribeMachineSpecResponseBodyTypes(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory: List[int] = None,
    ):
        # The valid values for the number of CPU cores.
        self.cpu = cpu
        # The valid memory values for the specified number of CPU cores.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

class DescribeMachineSpecResponseBodyInstanceMetas(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        gpu: str = None,
        gpuamount: int = None,
        gpumemory: float = None,
        instance_type: str = None,
        is_available: bool = None,
        memory: float = None,
        non_protect_spot_discount: float = None,
        spot_discount: float = None,
        stock_status: str = None,
        vendor: str = None,
    ):
        # The number of CPU cores of the instance type.
        self.cpu = cpu
        # The GPU model of the instance type. This field is not returned for non-GPU instance types.
        self.gpu = gpu
        # The number of GPUs in the instance type.
        self.gpuamount = gpuamount
        # The GPU memory size of the instance type, in GB.
        self.gpumemory = gpumemory
        # The instance type name.
        self.instance_type = instance_type
        # Indicates whether the instance type is currently available.
        self.is_available = is_available
        # The memory size of the instance type, in GB.
        self.memory = memory
        # The minimum discount currently offered for a spot instance in no-protection mode. A value of 0.1 indicates a 90% discount. If this field is not returned, the instance type does not support spot instances.
        self.non_protect_spot_discount = non_protect_spot_discount
        # The current lowest discount for a spot instance with a 1-hour protection period. A value of 0.1 indicates a 90% discount. If this field is not returned, the instance type does not support spot instances.
        self.spot_discount = spot_discount
        # The inventory status of the instance type.
        self.stock_status = stock_status
        # The source of the instance type.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.gpuamount is not None:
            result['GPUAmount'] = self.gpuamount

        if self.gpumemory is not None:
            result['GPUMemory'] = self.gpumemory

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_available is not None:
            result['IsAvailable'] = self.is_available

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.non_protect_spot_discount is not None:
            result['NonProtectSpotDiscount'] = self.non_protect_spot_discount

        if self.spot_discount is not None:
            result['SpotDiscount'] = self.spot_discount

        if self.stock_status is not None:
            result['StockStatus'] = self.stock_status

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUAmount') is not None:
            self.gpuamount = m.get('GPUAmount')

        if m.get('GPUMemory') is not None:
            self.gpumemory = m.get('GPUMemory')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NonProtectSpotDiscount') is not None:
            self.non_protect_spot_discount = m.get('NonProtectSpotDiscount')

        if m.get('SpotDiscount') is not None:
            self.spot_discount = m.get('SpotDiscount')

        if m.get('StockStatus') is not None:
            self.stock_status = m.get('StockStatus')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

