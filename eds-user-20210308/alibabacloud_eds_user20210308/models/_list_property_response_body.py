# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class ListPropertyResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        properties: List[main_models.ListPropertyResponseBodyProperties] = None,
        request_id: str = None,
    ):
        # The token that is used for the next query. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The information about the properties.
        self.properties = properties
        # The ID of the request.
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['Properties'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.properties = []
        if m.get('Properties') is not None:
            for k1 in m.get('Properties'):
                temp_model = main_models.ListPropertyResponseBodyProperties()
                self.properties.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPropertyResponseBodyProperties(DaraModel):
    def __init__(
        self,
        property_id: int = None,
        property_key: str = None,
        property_values: List[main_models.ListPropertyResponseBodyPropertiesPropertyValues] = None,
    ):
        # The ID of the property.
        self.property_id = property_id
        # The name of the property.
        self.property_key = property_key
        # Details about the property values.
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
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')

        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')

        self.property_values = []
        if m.get('PropertyValues') is not None:
            for k1 in m.get('PropertyValues'):
                temp_model = main_models.ListPropertyResponseBodyPropertiesPropertyValues()
                self.property_values.append(temp_model.from_map(k1))

        return self

class ListPropertyResponseBodyPropertiesPropertyValues(DaraModel):
    def __init__(
        self,
        property_value: str = None,
        property_value_id: int = None,
    ):
        # The value of the property.
        self.property_value = property_value
        # The ID of the property value.
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

