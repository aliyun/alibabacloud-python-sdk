# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListGatewayFeaturesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListGatewayFeaturesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The response message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListGatewayFeaturesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGatewayFeaturesResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListGatewayFeaturesResponseBodyDataItems] = None,
    ):
        # The list of parameter configurations.
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListGatewayFeaturesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        return self

class ListGatewayFeaturesResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        definition: main_models.ListGatewayFeaturesResponseBodyDataItemsDefinition = None,
        value: str = None,
    ):
        # The parameter definition.
        self.definition = definition
        # The parameter value.
        self.value = value

    def validate(self):
        if self.definition:
            self.definition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.definition is not None:
            result['definition'] = self.definition.to_map()

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('definition') is not None:
            temp_model = main_models.ListGatewayFeaturesResponseBodyDataItemsDefinition()
            self.definition = temp_model.from_map(m.get('definition'))

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ListGatewayFeaturesResponseBodyDataItemsDefinition(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        display_name: str = None,
        group: str = None,
        input_type: str = None,
        max_length: int = None,
        max_value: str = None,
        min_length: int = None,
        min_value: str = None,
        name: str = None,
        read_only: bool = None,
        regex: str = None,
        value_options: List[main_models.ListGatewayFeaturesResponseBodyDataItemsDefinitionValueOptions] = None,
        value_type: str = None,
        value_unit: str = None,
    ):
        # The default value of the parameter.
        self.default_value = default_value
        # The parameter description.
        self.description = description
        # The display name of the parameter.
        self.display_name = display_name
        # The parameter group to which the parameter belongs. Valid values:
        # 
        # *   Telemetry: an observability parameter
        # *   Engine: an engine parameter
        self.group = group
        # The input type of the parameter. Valid values:
        # 
        # *   Trigger
        # *   Input
        # *   SingleSelect
        # *   MultiSelect
        self.input_type = input_type
        # The maximum length of the value. This parameter is valid when the value type is string.
        self.max_length = max_length
        # The maximum value of the parameter. This parameter is valid when the value type is int32, int64, or float.
        self.max_value = max_value
        # The minimum length of the value. This parameter is valid when the value type is string.
        self.min_length = min_length
        # The minimum value of the parameter. This parameter is valid when the value type is int32, int64, or float.
        self.min_value = min_value
        # The parameter name.
        self.name = name
        # Indicates whether the parameter is read-only.
        self.read_only = read_only
        # The regular expression that the parameter value must fulfill. This parameter is valid when the value type is string.
        self.regex = regex
        # The list of options supported by the parameter value.
        self.value_options = value_options
        # The value type of the parameter. Valid values:
        # 
        # *   bool: boolean
        # *   string
        # *   int32: integer
        # *   int64: long integer
        # *   json
        # *   array: JSON array
        # *   float: floating point
        self.value_type = value_type
        # The value unit.
        self.value_unit = value_unit

    def validate(self):
        if self.value_options:
            for v1 in self.value_options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['defaultValue'] = self.default_value

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.group is not None:
            result['group'] = self.group

        if self.input_type is not None:
            result['inputType'] = self.input_type

        if self.max_length is not None:
            result['maxLength'] = self.max_length

        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_length is not None:
            result['minLength'] = self.min_length

        if self.min_value is not None:
            result['minValue'] = self.min_value

        if self.name is not None:
            result['name'] = self.name

        if self.read_only is not None:
            result['readOnly'] = self.read_only

        if self.regex is not None:
            result['regex'] = self.regex

        result['valueOptions'] = []
        if self.value_options is not None:
            for k1 in self.value_options:
                result['valueOptions'].append(k1.to_map() if k1 else None)

        if self.value_type is not None:
            result['valueType'] = self.value_type

        if self.value_unit is not None:
            result['valueUnit'] = self.value_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('inputType') is not None:
            self.input_type = m.get('inputType')

        if m.get('maxLength') is not None:
            self.max_length = m.get('maxLength')

        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minLength') is not None:
            self.min_length = m.get('minLength')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')

        if m.get('regex') is not None:
            self.regex = m.get('regex')

        self.value_options = []
        if m.get('valueOptions') is not None:
            for k1 in m.get('valueOptions'):
                temp_model = main_models.ListGatewayFeaturesResponseBodyDataItemsDefinitionValueOptions()
                self.value_options.append(temp_model.from_map(k1))

        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')

        if m.get('valueUnit') is not None:
            self.value_unit = m.get('valueUnit')

        return self

class ListGatewayFeaturesResponseBodyDataItemsDefinitionValueOptions(DaraModel):
    def __init__(
        self,
        key: str = None,
        label: str = None,
    ):
        # The key to pass the parameter.
        self.key = key
        # The display value.
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.label is not None:
            result['label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('label') is not None:
            self.label = m.get('label')

        return self

