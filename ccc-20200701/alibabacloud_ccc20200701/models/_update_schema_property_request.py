# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class UpdateSchemaPropertyRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        property: main_models.UpdateSchemaPropertyRequestProperty = None,
        request_id: str = None,
        schema_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.property = property
        self.request_id = request_id
        # schema id
        # 
        # This parameter is required.
        self.schema_id = schema_id

    def validate(self):
        if self.property:
            self.property.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.property is not None:
            result['Property'] = self.property.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Property') is not None:
            temp_model = main_models.UpdateSchemaPropertyRequestProperty()
            self.property = temp_model.from_map(m.get('Property'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateSchemaPropertyRequestProperty(DaraModel):
    def __init__(
        self,
        array: bool = None,
        attributes: str = None,
        data_type: str = None,
        description: str = None,
        disabled: bool = None,
        display_name: str = None,
        display_order: int = None,
        editor_type: str = None,
        max_length: int = None,
        maximum: float = None,
        min_length: int = None,
        minimum: float = None,
        name: str = None,
        pattern: str = None,
        pattern_error_message: str = None,
        read_only: bool = None,
        required: bool = None,
    ):
        self.array = array
        self.attributes = attributes
        # This parameter is required.
        self.data_type = data_type
        self.description = description
        self.disabled = disabled
        self.display_name = display_name
        self.display_order = display_order
        self.editor_type = editor_type
        self.max_length = max_length
        self.maximum = maximum
        self.min_length = min_length
        self.minimum = minimum
        # This parameter is required.
        self.name = name
        self.pattern = pattern
        self.pattern_error_message = pattern_error_message
        self.read_only = read_only
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array is not None:
            result['Array'] = self.array

        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.description is not None:
            result['Description'] = self.description

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.display_order is not None:
            result['DisplayOrder'] = self.display_order

        if self.editor_type is not None:
            result['EditorType'] = self.editor_type

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.maximum is not None:
            result['Maximum'] = self.maximum

        if self.min_length is not None:
            result['MinLength'] = self.min_length

        if self.minimum is not None:
            result['Minimum'] = self.minimum

        if self.name is not None:
            result['Name'] = self.name

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.pattern_error_message is not None:
            result['PatternErrorMessage'] = self.pattern_error_message

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.required is not None:
            result['Required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Array') is not None:
            self.array = m.get('Array')

        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('DisplayOrder') is not None:
            self.display_order = m.get('DisplayOrder')

        if m.get('EditorType') is not None:
            self.editor_type = m.get('EditorType')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')

        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')

        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('PatternErrorMessage') is not None:
            self.pattern_error_message = m.get('PatternErrorMessage')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        return self

