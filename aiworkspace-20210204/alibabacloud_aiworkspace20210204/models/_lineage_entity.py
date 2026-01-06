# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class LineageEntity(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        entity_type: str = None,
        name: str = None,
        qualified_name: str = None,
    ):
        self.attributes = attributes
        self.entity_type = entity_type
        self.name = name
        self.qualified_name = qualified_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.name is not None:
            result['Name'] = self.name

        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        return self

