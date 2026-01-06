# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceGroupSpecResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        specs: List[main_models.DescribeResourceGroupSpecResponseBodySpecs] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried specifications.
        self.specs = specs

    def validate(self):
        if self.specs:
            for v1 in self.specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Specs'] = []
        if self.specs is not None:
            for k1 in self.specs:
                result['Specs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.specs = []
        if m.get('Specs') is not None:
            for k1 in m.get('Specs'):
                temp_model = main_models.DescribeResourceGroupSpecResponseBodySpecs()
                self.specs.append(temp_model.from_map(k1))

        return self

class DescribeResourceGroupSpecResponseBodySpecs(DaraModel):
    def __init__(
        self,
        allocate_units: List[str] = None,
        max_quantity: int = None,
        name: str = None,
        type: str = None,
    ):
        # The allocation units supported by this specification.
        self.allocate_units = allocate_units
        # The maximum number of resource groups that can be used with this specification.
        self.max_quantity = max_quantity
        # The name of the specification.
        self.name = name
        # The resource type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocate_units is not None:
            result['AllocateUnits'] = self.allocate_units

        if self.max_quantity is not None:
            result['MaxQuantity'] = self.max_quantity

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocateUnits') is not None:
            self.allocate_units = m.get('AllocateUnits')

        if m.get('MaxQuantity') is not None:
            self.max_quantity = m.get('MaxQuantity')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

