# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class HyperParameterDefinition(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
        range: main_models.HyperParameterRange = None,
        required: bool = None,
        type: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.display_name = display_name
        # This parameter is required.
        self.name = name
        self.range = range
        self.required = required
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.range:
            self.range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        if self.range is not None:
            result['Range'] = self.range.to_map()

        if self.required is not None:
            result['Required'] = self.required

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Range') is not None:
            temp_model = main_models.HyperParameterRange()
            self.range = temp_model.from_map(m.get('Range'))

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

