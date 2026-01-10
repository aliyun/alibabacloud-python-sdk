# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateToolData(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        source_type: str = None,
        tool_type: str = None,
        updated_at: str = None,
    ):
        self.id = id
        self.name = name
        self.source_type = source_type
        self.tool_type = tool_type
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.tool_type is not None:
            result['toolType'] = self.tool_type

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('toolType') is not None:
            self.tool_type = m.get('toolType')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

