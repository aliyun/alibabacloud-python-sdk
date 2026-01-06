# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LineageRelation(DaraModel):
    def __init__(
        self,
        dest_entity_qualified_name: str = None,
        relationship_guid: str = None,
        src_entity_qualified_name: str = None,
    ):
        self.dest_entity_qualified_name = dest_entity_qualified_name
        self.relationship_guid = relationship_guid
        self.src_entity_qualified_name = src_entity_qualified_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_entity_qualified_name is not None:
            result['DestEntityQualifiedName'] = self.dest_entity_qualified_name

        if self.relationship_guid is not None:
            result['RelationshipGuid'] = self.relationship_guid

        if self.src_entity_qualified_name is not None:
            result['SrcEntityQualifiedName'] = self.src_entity_qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestEntityQualifiedName') is not None:
            self.dest_entity_qualified_name = m.get('DestEntityQualifiedName')

        if m.get('RelationshipGuid') is not None:
            self.relationship_guid = m.get('RelationshipGuid')

        if m.get('SrcEntityQualifiedName') is not None:
            self.src_entity_qualified_name = m.get('SrcEntityQualifiedName')

        return self

