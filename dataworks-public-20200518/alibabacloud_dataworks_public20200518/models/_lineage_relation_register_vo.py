# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class LineageRelationRegisterVO(DaraModel):
    def __init__(
        self,
        create_timestamp: int = None,
        dest_entity: main_models.LineageEntityVO = None,
        relationship: main_models.RelationshipVO = None,
        src_entity: main_models.LineageEntityVO = None,
    ):
        # The time of lineage relation generation
        self.create_timestamp = create_timestamp
        # The destination entity in lineage relation
        self.dest_entity = dest_entity
        # The relationship between entities
        self.relationship = relationship
        # The source entity in lineage relation
        self.src_entity = src_entity

    def validate(self):
        if self.dest_entity:
            self.dest_entity.validate()
        if self.relationship:
            self.relationship.validate()
        if self.src_entity:
            self.src_entity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.dest_entity is not None:
            result['DestEntity'] = self.dest_entity.to_map()

        if self.relationship is not None:
            result['Relationship'] = self.relationship.to_map()

        if self.src_entity is not None:
            result['SrcEntity'] = self.src_entity.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('DestEntity') is not None:
            temp_model = main_models.LineageEntityVO()
            self.dest_entity = temp_model.from_map(m.get('DestEntity'))

        if m.get('Relationship') is not None:
            temp_model = main_models.RelationshipVO()
            self.relationship = temp_model.from_map(m.get('Relationship'))

        if m.get('SrcEntity') is not None:
            temp_model = main_models.LineageEntityVO()
            self.src_entity = temp_model.from_map(m.get('SrcEntity'))

        return self

