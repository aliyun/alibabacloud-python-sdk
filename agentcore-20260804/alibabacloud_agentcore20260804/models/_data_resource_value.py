# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DataResourceValue(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        content: str = None,
        metadata: Dict[str, Any] = None,
    ):
        # The name.
        self.name = name
        # The type.
        self.type = type
        # The content.
        self.content = content
        # The metadata.
        self.metadata = metadata

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.content is not None:
            result['content'] = self.content

        if self.metadata is not None:
            result['metadata'] = self.metadata

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        return self

