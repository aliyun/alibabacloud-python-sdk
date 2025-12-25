# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HttpApiParameter(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        example_value: str = None,
        name: str = None,
        required: bool = None,
        type: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.example_value = example_value
        # This parameter is required.
        self.name = name
        self.required = required
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['defaultValue'] = self.default_value

        if self.description is not None:
            result['description'] = self.description

        if self.example_value is not None:
            result['exampleValue'] = self.example_value

        if self.name is not None:
            result['name'] = self.name

        if self.required is not None:
            result['required'] = self.required

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('exampleValue') is not None:
            self.example_value = m.get('exampleValue')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

