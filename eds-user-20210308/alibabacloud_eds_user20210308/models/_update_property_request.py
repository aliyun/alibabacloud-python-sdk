# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class UpdatePropertyRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        property_id: int = None,
        property_key: str = None,
        property_values: List[main_models.UpdatePropertyRequestPropertyValues] = None,
    ):
        self.business_channel = business_channel
        # The ID of the property that you want to modify. You can call the [ListProperty](https://help.aliyun.com/document_detail/410890.html) operation to query the property ID.
        # 
        # This parameter is required.
        self.property_id = property_id
        # The new property name.
        # 
        # This parameter is required.
        self.property_key = property_key
        # The values of property.
        self.property_values = property_values

    def validate(self):
        if self.property_values:
            for v1 in self.property_values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.property_id is not None:
            result['PropertyId'] = self.property_id

        if self.property_key is not None:
            result['PropertyKey'] = self.property_key

        result['PropertyValues'] = []
        if self.property_values is not None:
            for k1 in self.property_values:
                result['PropertyValues'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')

        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')

        self.property_values = []
        if m.get('PropertyValues') is not None:
            for k1 in m.get('PropertyValues'):
                temp_model = main_models.UpdatePropertyRequestPropertyValues()
                self.property_values.append(temp_model.from_map(k1))

        return self

class UpdatePropertyRequestPropertyValues(DaraModel):
    def __init__(
        self,
        property_value: str = None,
        property_value_id: int = None,
    ):
        # The new property value.
        self.property_value = property_value
        # The ID of property value that you want to modify. You can call the [ListProperty](https://help.aliyun.com/document_detail/410890.html) operation to query the property value ID.
        self.property_value_id = property_value_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value

        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')

        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')

        return self

