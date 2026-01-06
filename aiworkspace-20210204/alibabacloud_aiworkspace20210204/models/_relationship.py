# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class Relationship(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        data_channel: str = None,
        relationship_guid: str = None,
        relationship_type: str = None,
    ):
        self.attributes = attributes
        self.data_channel = data_channel
        self.relationship_guid = relationship_guid
        self.relationship_type = relationship_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.data_channel is not None:
            result['DataChannel'] = self.data_channel

        if self.relationship_guid is not None:
            result['RelationshipGuid'] = self.relationship_guid

        if self.relationship_type is not None:
            result['RelationshipType'] = self.relationship_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('DataChannel') is not None:
            self.data_channel = m.get('DataChannel')

        if m.get('RelationshipGuid') is not None:
            self.relationship_guid = m.get('RelationshipGuid')

        if m.get('RelationshipType') is not None:
            self.relationship_type = m.get('RelationshipType')

        return self

