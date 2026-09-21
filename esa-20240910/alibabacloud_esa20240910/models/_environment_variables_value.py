# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnvironmentVariablesValue(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The environment variable type.
        # 
        # Valid values:
        # - `plain_text`: plain text
        # - `secret_text`: encrypted text
        self.type = type
        # The environment variable value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

