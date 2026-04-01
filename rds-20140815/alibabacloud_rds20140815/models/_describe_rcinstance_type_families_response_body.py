# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCInstanceTypeFamiliesResponseBody(DaraModel):
    def __init__(
        self,
        instance_type_families: main_models.DescribeRCInstanceTypeFamiliesResponseBodyInstanceTypeFamilies = None,
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
            temp_model = main_models.DescribeRCInstanceTypeFamiliesResponseBodyInstanceTypeFamilies()
            self.instance_type_families = temp_model.from_map(m.get('InstanceTypeFamilies'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRCInstanceTypeFamiliesResponseBodyInstanceTypeFamilies(DaraModel):
    def __init__(
        self,
        instance_type_family: List[main_models.DescribeRCInstanceTypeFamiliesResponseBodyInstanceTypeFamiliesInstanceTypeFamily] = None,
    ):
        # The instance family.
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
                temp_model = main_models.DescribeRCInstanceTypeFamiliesResponseBodyInstanceTypeFamiliesInstanceTypeFamily()
                self.instance_type_family.append(temp_model.from_map(k1))

        return self

class DescribeRCInstanceTypeFamiliesResponseBodyInstanceTypeFamiliesInstanceTypeFamily(DaraModel):
    def __init__(
        self,
        instance_type_family_desc: str = None,
        instance_type_family_id: str = None,
    ):
        # The description of the instance family.
        self.instance_type_family_desc = instance_type_family_desc
        # The ID of the instance family.
        self.instance_type_family_id = instance_type_family_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type_family_desc is not None:
            result['InstanceTypeFamilyDesc'] = self.instance_type_family_desc

        if self.instance_type_family_id is not None:
            result['InstanceTypeFamilyId'] = self.instance_type_family_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypeFamilyDesc') is not None:
            self.instance_type_family_desc = m.get('InstanceTypeFamilyDesc')

        if m.get('InstanceTypeFamilyId') is not None:
            self.instance_type_family_id = m.get('InstanceTypeFamilyId')

        return self

