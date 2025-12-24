# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceTypeFamiliesResponseBody(DaraModel):
    def __init__(
        self,
        instance_type_families: main_models.DescribeInstanceTypeFamiliesResponseBodyInstanceTypeFamilies = None,
        request_id: str = None,
    ):
        # The instance families.
        self.instance_type_families = instance_type_families
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_type_families:
            self.instance_type_families.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type_families is not None:
            result['InstanceTypeFamilies'] = self.instance_type_families.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypeFamilies') is not None:
            temp_model = main_models.DescribeInstanceTypeFamiliesResponseBodyInstanceTypeFamilies()
            self.instance_type_families = temp_model.from_map(m.get('InstanceTypeFamilies'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceTypeFamiliesResponseBodyInstanceTypeFamilies(DaraModel):
    def __init__(
        self,
        instance_type_family: List[main_models.DescribeInstanceTypeFamiliesResponseBodyInstanceTypeFamiliesInstanceTypeFamily] = None,
    ):
        self.instance_type_family = instance_type_family

    def validate(self):
        if self.instance_type_family:
            for v1 in self.instance_type_family:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceTypeFamily'] = []
        if self.instance_type_family is not None:
            for k1 in self.instance_type_family:
                result['InstanceTypeFamily'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type_family = []
        if m.get('InstanceTypeFamily') is not None:
            for k1 in m.get('InstanceTypeFamily'):
                temp_model = main_models.DescribeInstanceTypeFamiliesResponseBodyInstanceTypeFamiliesInstanceTypeFamily()
                self.instance_type_family.append(temp_model.from_map(k1))

        return self

class DescribeInstanceTypeFamiliesResponseBodyInstanceTypeFamiliesInstanceTypeFamily(DaraModel):
    def __init__(
        self,
        generation: str = None,
        instance_type_family_id: str = None,
    ):
        # The series of the instance family.
        self.generation = generation
        # The ID of the instance family.
        self.instance_type_family_id = instance_type_family_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generation is not None:
            result['Generation'] = self.generation

        if self.instance_type_family_id is not None:
            result['InstanceTypeFamilyId'] = self.instance_type_family_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Generation') is not None:
            self.generation = m.get('Generation')

        if m.get('InstanceTypeFamilyId') is not None:
            self.instance_type_family_id = m.get('InstanceTypeFamilyId')

        return self

