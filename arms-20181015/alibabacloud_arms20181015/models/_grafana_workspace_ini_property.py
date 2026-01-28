# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceIniProperty(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        example: str = None,
        key: str = None,
        secret: bool = None,
        value: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.example = example
        self.key = key
        self.secret = secret
        self.value = value

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

        if self.example is not None:
            result['example'] = self.example

        if self.key is not None:
            result['key'] = self.key

        if self.secret is not None:
            result['secret'] = self.secret

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('example') is not None:
            self.example = m.get('example')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('secret') is not None:
            self.secret = m.get('secret')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

