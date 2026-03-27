# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetAddonSchemaResponseBody(DaraModel):
    def __init__(
        self,
        fields: List[main_models.GetAddonSchemaResponseBodyFields] = None,
        request_id: str = None,
        type: str = None,
    ):
        self.fields = fields
        self.request_id = request_id
        self.type = type

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['fields'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('fields') is not None:
            for k1 in m.get('fields'):
                temp_model = main_models.GetAddonSchemaResponseBodyFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetAddonSchemaResponseBodyFields(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.GetAddonSchemaResponseBodyFieldsConditions] = None,
        default_value: Any = None,
        description: str = None,
        disabled: bool = None,
        element: str = None,
        field_path: str = None,
        label: str = None,
        name: str = None,
        placeholder: str = None,
        props: main_models.GetAddonSchemaResponseBodyFieldsProps = None,
        type: str = None,
        validation: main_models.GetAddonSchemaResponseBodyFieldsValidation = None,
    ):
        self.conditions = conditions
        self.default_value = default_value
        self.description = description
        self.disabled = disabled
        self.element = element
        self.field_path = field_path
        self.label = label
        self.name = name
        self.placeholder = placeholder
        self.props = props
        self.type = type
        self.validation = validation

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.props:
            self.props.validate()
        if self.validation:
            self.validation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        if self.default_value is not None:
            result['defaultValue'] = self.default_value

        if self.description is not None:
            result['description'] = self.description

        if self.disabled is not None:
            result['disabled'] = self.disabled

        if self.element is not None:
            result['element'] = self.element

        if self.field_path is not None:
            result['fieldPath'] = self.field_path

        if self.label is not None:
            result['label'] = self.label

        if self.name is not None:
            result['name'] = self.name

        if self.placeholder is not None:
            result['placeholder'] = self.placeholder

        if self.props is not None:
            result['props'] = self.props.to_map()

        if self.type is not None:
            result['type'] = self.type

        if self.validation is not None:
            result['validation'] = self.validation.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.GetAddonSchemaResponseBodyFieldsConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')

        if m.get('element') is not None:
            self.element = m.get('element')

        if m.get('fieldPath') is not None:
            self.field_path = m.get('fieldPath')

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')

        if m.get('props') is not None:
            temp_model = main_models.GetAddonSchemaResponseBodyFieldsProps()
            self.props = temp_model.from_map(m.get('props'))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('validation') is not None:
            temp_model = main_models.GetAddonSchemaResponseBodyFieldsValidation()
            self.validation = temp_model.from_map(m.get('validation'))

        return self

class GetAddonSchemaResponseBodyFieldsValidation(DaraModel):
    def __init__(
        self,
        max: int = None,
        max_length: int = None,
        message: str = None,
        min: int = None,
        min_length: int = None,
        regular: str = None,
        required: bool = None,
    ):
        self.max = max
        self.max_length = max_length
        self.message = message
        self.min = min
        self.min_length = min_length
        self.regular = regular
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max is not None:
            result['max'] = self.max

        if self.max_length is not None:
            result['maxLength'] = self.max_length

        if self.message is not None:
            result['message'] = self.message

        if self.min is not None:
            result['min'] = self.min

        if self.min_length is not None:
            result['minLength'] = self.min_length

        if self.regular is not None:
            result['regular'] = self.regular

        if self.required is not None:
            result['required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('max') is not None:
            self.max = m.get('max')

        if m.get('maxLength') is not None:
            self.max_length = m.get('maxLength')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('min') is not None:
            self.min = m.get('min')

        if m.get('minLength') is not None:
            self.min_length = m.get('minLength')

        if m.get('regular') is not None:
            self.regular = m.get('regular')

        if m.get('required') is not None:
            self.required = m.get('required')

        return self

class GetAddonSchemaResponseBodyFieldsProps(DaraModel):
    def __init__(
        self,
        data_source: List[main_models.GetAddonSchemaResponseBodyFieldsPropsDataSource] = None,
        related: List[str] = None,
        select_mode: str = None,
    ):
        # AK
        self.data_source = data_source
        self.related = related
        self.select_mode = select_mode

    def validate(self):
        if self.data_source:
            for v1 in self.data_source:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dataSource'] = []
        if self.data_source is not None:
            for k1 in self.data_source:
                result['dataSource'].append(k1.to_map() if k1 else None)

        if self.related is not None:
            result['related'] = self.related

        if self.select_mode is not None:
            result['selectMode'] = self.select_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_source = []
        if m.get('dataSource') is not None:
            for k1 in m.get('dataSource'):
                temp_model = main_models.GetAddonSchemaResponseBodyFieldsPropsDataSource()
                self.data_source.append(temp_model.from_map(k1))

        if m.get('related') is not None:
            self.related = m.get('related')

        if m.get('selectMode') is not None:
            self.select_mode = m.get('selectMode')

        return self

class GetAddonSchemaResponseBodyFieldsPropsDataSource(DaraModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['label'] = self.label

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class GetAddonSchemaResponseBodyFieldsConditions(DaraModel):
    def __init__(
        self,
        action: str = None,
        field: str = None,
        op: str = None,
        value: Any = None,
    ):
        self.action = action
        self.field = field
        self.op = op
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.field is not None:
            result['field'] = self.field

        if self.op is not None:
            result['op'] = self.op

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('field') is not None:
            self.field = m.get('field')

        if m.get('op') is not None:
            self.op = m.get('op')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

