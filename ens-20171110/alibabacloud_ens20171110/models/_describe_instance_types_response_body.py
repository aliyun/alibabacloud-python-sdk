# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceTypesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        instance_types: main_models.DescribeInstanceTypesResponseBodyInstanceTypes = None,
        request_id: str = None,
    ):
        # The status code. If the request is successful, 0 is returned. If the request fails, a non-zero error code is returned.
        self.code = code
        # Details about the instance types.
        self.instance_types = instance_types
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_types:
            self.instance_types.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('InstanceTypes') is not None:
            temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypes()
            self.instance_types = temp_model.from_map(m.get('InstanceTypes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceTypesResponseBodyInstanceTypes(DaraModel):
    def __init__(
        self,
        instance_type: List[main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceType] = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type:
            for v1 in self.instance_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceType'] = []
        if self.instance_type is not None:
            for k1 in self.instance_type:
                result['InstanceType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type = []
        if m.get('InstanceType') is not None:
            for k1 in m.get('InstanceType'):
                temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceType()
                self.instance_type.append(temp_model.from_map(k1))

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceType(DaraModel):
    def __init__(
        self,
        cpu_core_count: int = None,
        instance_type_id: str = None,
        instance_type_name: str = None,
        memory_size: int = None,
    ):
        # The number of vCPUs.
        self.cpu_core_count = cpu_core_count
        # This parameter is unavailable.
        self.instance_type_id = instance_type_id
        # The name of the instance type.
        self.instance_type_name = instance_type_name
        # The memory size. Unit: MB.
        self.memory_size = memory_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count

        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id

        if self.instance_type_name is not None:
            result['InstanceTypeName'] = self.instance_type_name

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')

        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')

        if m.get('InstanceTypeName') is not None:
            self.instance_type_name = m.get('InstanceTypeName')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        return self

