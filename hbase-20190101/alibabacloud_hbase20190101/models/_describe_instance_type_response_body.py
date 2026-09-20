# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceTypeResponseBody(DaraModel):
    def __init__(
        self,
        instance_type_spec_list: main_models.DescribeInstanceTypeResponseBodyInstanceTypeSpecList = None,
        request_id: str = None,
    ):
        self.instance_type_spec_list = instance_type_spec_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_type_spec_list:
            self.instance_type_spec_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type_spec_list is not None:
            result['InstanceTypeSpecList'] = self.instance_type_spec_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypeSpecList') is not None:
            temp_model = main_models.DescribeInstanceTypeResponseBodyInstanceTypeSpecList()
            self.instance_type_spec_list = temp_model.from_map(m.get('InstanceTypeSpecList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceTypeResponseBodyInstanceTypeSpecList(DaraModel):
    def __init__(
        self,
        instance_type_spec: List[main_models.DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec] = None,
    ):
        self.instance_type_spec = instance_type_spec

    def validate(self):
        if self.instance_type_spec:
            for v1 in self.instance_type_spec:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceTypeSpec'] = []
        if self.instance_type_spec is not None:
            for k1 in self.instance_type_spec:
                result['InstanceTypeSpec'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type_spec = []
        if m.get('InstanceTypeSpec') is not None:
            for k1 in m.get('InstanceTypeSpec'):
                temp_model = main_models.DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec()
                self.instance_type_spec.append(temp_model.from_map(k1))

        return self

class DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec(DaraModel):
    def __init__(
        self,
        cpu_size: int = None,
        instance_type: str = None,
        mem_size: int = None,
    ):
        self.cpu_size = cpu_size
        self.instance_type = instance_type
        self.mem_size = mem_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_size is not None:
            result['CpuSize'] = self.cpu_size

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.mem_size is not None:
            result['MemSize'] = self.mem_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuSize') is not None:
            self.cpu_size = m.get('CpuSize')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MemSize') is not None:
            self.mem_size = m.get('MemSize')

        return self

