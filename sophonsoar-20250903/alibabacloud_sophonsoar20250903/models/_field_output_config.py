# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FieldOutputConfig(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        field_description: str = None,
        field_example: str = None,
        field_name: str = None,
        field_type: str = None,
    ):
        self.default_value = default_value
        self.field_description = field_description
        self.field_example = field_example
        self.field_name = field_name
        self.field_type = field_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.field_description is not None:
            result['FieldDescription'] = self.field_description

        if self.field_example is not None:
            result['FieldExample'] = self.field_example

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_type is not None:
            result['FieldType'] = self.field_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('FieldDescription') is not None:
            self.field_description = m.get('FieldDescription')

        if m.get('FieldExample') is not None:
            self.field_example = m.get('FieldExample')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')

        return self

