# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetricDefinition(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        regex: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.regex = regex

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.regex is not None:
            result['Regex'] = self.regex

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Regex') is not None:
            self.regex = m.get('Regex')

        return self

