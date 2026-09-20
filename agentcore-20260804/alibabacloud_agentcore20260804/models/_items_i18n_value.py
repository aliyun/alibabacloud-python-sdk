# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ItemsI18nValue(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        readme: str = None,
    ):
        # The MCP service description in the corresponding language.
        self.description = description
        # The MCP marketplace template name in the corresponding language.
        self.name = name
        # The MCP marketplace template usage instructions in the corresponding language.
        self.readme = readme

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.readme is not None:
            result['readme'] = self.readme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('readme') is not None:
            self.readme = m.get('readme')

        return self

