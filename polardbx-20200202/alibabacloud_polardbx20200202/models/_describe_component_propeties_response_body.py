# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeComponentPropetiesResponseBody(DaraModel):
    def __init__(
        self,
        properties: List[main_models.DescribeComponentPropetiesResponseBodyProperties] = None,
        request_id: str = None,
    ):
        self.properties = properties
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.properties:
            for v1 in self.properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['Properties'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.properties = []
        if m.get('Properties') is not None:
            for k1 in m.get('Properties'):
                temp_model = main_models.DescribeComponentPropetiesResponseBodyProperties()
                self.properties.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeComponentPropetiesResponseBodyProperties(DaraModel):
    def __init__(
        self,
        name: str = None,
        order_index: str = None,
        property_code: str = None,
        value: str = None,
    ):
        self.name = name
        self.order_index = order_index
        self.property_code = property_code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.order_index is not None:
            result['OrderIndex'] = self.order_index

        if self.property_code is not None:
            result['PropertyCode'] = self.property_code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')

        if m.get('PropertyCode') is not None:
            self.property_code = m.get('PropertyCode')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

