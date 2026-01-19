# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataSchemaPropertiesValue(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        description: str = None,
        name: str = None,
        data_type: str = None,
        pattern: str = None,
        pattern_error_message: str = None,
        min_length: int = None,
        max_length: int = None,
        minimum: float = None,
        maximum: float = None,
        required: bool = None,
        system: bool = None,
        disabled: bool = None,
        array: bool = None,
        read_only: bool = None,
        editor_type: str = None,
        attributes: str = None,
        display_order: int = None,
        created_time: int = None,
        updated_time: int = None,
        created_by: str = None,
    ):
        self.display_name = display_name
        self.description = description
        self.name = name
        self.data_type = data_type
        self.pattern = pattern
        self.pattern_error_message = pattern_error_message
        self.min_length = min_length
        self.max_length = max_length
        self.minimum = minimum
        self.maximum = maximum
        self.required = required
        self.system = system
        self.disabled = disabled
        self.array = array
        self.read_only = read_only
        self.editor_type = editor_type
        self.attributes = attributes
        self.display_order = display_order
        self.created_time = created_time
        self.updated_time = updated_time
        self.created_by = created_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.pattern_error_message is not None:
            result['PatternErrorMessage'] = self.pattern_error_message

        if self.min_length is not None:
            result['MinLength'] = self.min_length

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.minimum is not None:
            result['Minimum'] = self.minimum

        if self.maximum is not None:
            result['Maximum'] = self.maximum

        if self.required is not None:
            result['Required'] = self.required

        if self.system is not None:
            result['System'] = self.system

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.array is not None:
            result['Array'] = self.array

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.editor_type is not None:
            result['EditorType'] = self.editor_type

        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.display_order is not None:
            result['DisplayOrder'] = self.display_order

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('PatternErrorMessage') is not None:
            self.pattern_error_message = m.get('PatternErrorMessage')

        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')

        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('System') is not None:
            self.system = m.get('System')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('Array') is not None:
            self.array = m.get('Array')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('EditorType') is not None:
            self.editor_type = m.get('EditorType')

        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('DisplayOrder') is not None:
            self.display_order = m.get('DisplayOrder')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        return self

