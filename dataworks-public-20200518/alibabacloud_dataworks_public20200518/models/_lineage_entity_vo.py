# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class LineageEntityVO(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        detail_url: str = None,
        entity_type: str = None,
        name: str = None,
        owner: str = None,
        parent_name: str = None,
        qualified_name: str = None,
    ):
        self.attributes = attributes
        # Detail url of entity
        self.detail_url = detail_url
        self.entity_type = entity_type
        # Name of entity
        self.name = name
        self.owner = owner
        # Parent name of entity
        self.parent_name = parent_name
        # Unique identifier of entity
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

        if self.detail_url is not None:
            result['DetailUrl'] = self.detail_url

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parent_name is not None:
            result['ParentName'] = self.parent_name

        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('DetailUrl') is not None:
            self.detail_url = m.get('DetailUrl')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ParentName') is not None:
            self.parent_name = m.get('ParentName')

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        return self

