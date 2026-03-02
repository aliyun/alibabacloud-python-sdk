# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Property(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        defines_format: bool = None,
        description: str = None,
        key: str = None,
        required: bool = None,
        sensitive: bool = None,
    ):
        # The default value of the parameter.
        self.default_value = default_value
        # Indicates whether the format is defined.
        self.defines_format = defines_format
        # The description of the parameter.
        self.description = description
        # The name of the parameter key.
        self.key = key
        # Indicates whether the parameter is required.
        self.required = required
        # Indiactes whether the data is sensitive.
        self.sensitive = sensitive

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['defaultValue'] = self.default_value

        if self.defines_format is not None:
            result['definesFormat'] = self.defines_format

        if self.description is not None:
            result['description'] = self.description

        if self.key is not None:
            result['key'] = self.key

        if self.required is not None:
            result['required'] = self.required

        if self.sensitive is not None:
            result['sensitive'] = self.sensitive

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')

        if m.get('definesFormat') is not None:
            self.defines_format = m.get('definesFormat')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('sensitive') is not None:
            self.sensitive = m.get('sensitive')

        return self

