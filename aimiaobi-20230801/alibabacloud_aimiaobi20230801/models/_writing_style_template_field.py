# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class WritingStyleTemplateField(DaraModel):
    def __init__(
        self,
        build_in: bool = None,
        cascading_fields: List[main_models.WritingStyleTemplateField] = None,
        enums: List[main_models.WritingStyleTemplateFieldEnums] = None,
        initial_value: str = None,
        key: str = None,
        max: float = None,
        max_item: int = None,
        max_item_length: int = None,
        max_length: int = None,
        min: float = None,
        min_item_length: int = None,
        min_length: int = None,
        name: str = None,
        required: bool = None,
        style: main_models.WritingStyleTemplateFieldStyle = None,
    ):
        self.build_in = build_in
        self.cascading_fields = cascading_fields
        self.enums = enums
        self.initial_value = initial_value
        self.key = key
        self.max = max
        self.max_item = max_item
        self.max_item_length = max_item_length
        self.max_length = max_length
        self.min = min
        self.min_item_length = min_item_length
        self.min_length = min_length
        self.name = name
        self.required = required
        self.style = style

    def validate(self):
        if self.cascading_fields:
            for v1 in self.cascading_fields:
                 if v1:
                    v1.validate()
        if self.enums:
            for v1 in self.enums:
                 if v1:
                    v1.validate()
        if self.style:
            self.style.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_in is not None:
            result['BuildIn'] = self.build_in

        result['CascadingFields'] = []
        if self.cascading_fields is not None:
            for k1 in self.cascading_fields:
                result['CascadingFields'].append(k1.to_map() if k1 else None)

        result['Enums'] = []
        if self.enums is not None:
            for k1 in self.enums:
                result['Enums'].append(k1.to_map() if k1 else None)

        if self.initial_value is not None:
            result['InitialValue'] = self.initial_value

        if self.key is not None:
            result['Key'] = self.key

        if self.max is not None:
            result['Max'] = self.max

        if self.max_item is not None:
            result['MaxItem'] = self.max_item

        if self.max_item_length is not None:
            result['MaxItemLength'] = self.max_item_length

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.min is not None:
            result['Min'] = self.min

        if self.min_item_length is not None:
            result['MinItemLength'] = self.min_item_length

        if self.min_length is not None:
            result['MinLength'] = self.min_length

        if self.name is not None:
            result['Name'] = self.name

        if self.required is not None:
            result['Required'] = self.required

        if self.style is not None:
            result['Style'] = self.style.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildIn') is not None:
            self.build_in = m.get('BuildIn')

        self.cascading_fields = []
        if m.get('CascadingFields') is not None:
            for k1 in m.get('CascadingFields'):
                temp_model = main_models.WritingStyleTemplateField()
                self.cascading_fields.append(temp_model.from_map(k1))

        self.enums = []
        if m.get('Enums') is not None:
            for k1 in m.get('Enums'):
                temp_model = main_models.WritingStyleTemplateFieldEnums()
                self.enums.append(temp_model.from_map(k1))

        if m.get('InitialValue') is not None:
            self.initial_value = m.get('InitialValue')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('MaxItem') is not None:
            self.max_item = m.get('MaxItem')

        if m.get('MaxItemLength') is not None:
            self.max_item_length = m.get('MaxItemLength')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('MinItemLength') is not None:
            self.min_item_length = m.get('MinItemLength')

        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Style') is not None:
            temp_model = main_models.WritingStyleTemplateFieldStyle()
            self.style = temp_model.from_map(m.get('Style'))

        return self

class WritingStyleTemplateFieldStyle(DaraModel):
    def __init__(
        self,
        description: str = None,
        format: str = None,
        placeholder: str = None,
        show_time: bool = None,
        suffix: str = None,
        type: str = None,
    ):
        self.description = description
        self.format = format
        self.placeholder = placeholder
        self.show_time = show_time
        self.suffix = suffix
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.format is not None:
            result['Format'] = self.format

        if self.placeholder is not None:
            result['Placeholder'] = self.placeholder

        if self.show_time is not None:
            result['ShowTime'] = self.show_time

        if self.suffix is not None:
            result['Suffix'] = self.suffix

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Placeholder') is not None:
            self.placeholder = m.get('Placeholder')

        if m.get('ShowTime') is not None:
            self.show_time = m.get('ShowTime')

        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class WritingStyleTemplateFieldEnums(DaraModel):
    def __init__(
        self,
        cascading_fields: List[str] = None,
        key: str = None,
        name: str = None,
    ):
        self.cascading_fields = cascading_fields
        self.key = key
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cascading_fields is not None:
            result['CascadingFields'] = self.cascading_fields

        if self.key is not None:
            result['Key'] = self.key

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CascadingFields') is not None:
            self.cascading_fields = m.get('CascadingFields')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

