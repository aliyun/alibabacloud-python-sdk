# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class LineageRelationRegisterBulkVO(DaraModel):
    def __init__(
        self,
        create_timestamp: int = None,
        dest_entities: List[main_models.LineageEntityVO] = None,
        relationship: main_models.RelationshipVO = None,
        src_entities: List[main_models.LineageEntityVO] = None,
    ):
        self.create_timestamp = create_timestamp
        self.dest_entities = dest_entities
        self.relationship = relationship
        self.src_entities = src_entities

    def validate(self):
        if self.dest_entities:
            for v1 in self.dest_entities:
                 if v1:
                    v1.validate()
        if self.relationship:
            self.relationship.validate()
        if self.src_entities:
            for v1 in self.src_entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        result['DestEntities'] = []
        if self.dest_entities is not None:
            for k1 in self.dest_entities:
                result['DestEntities'].append(k1.to_map() if k1 else None)

        if self.relationship is not None:
            result['Relationship'] = self.relationship.to_map()

        result['SrcEntities'] = []
        if self.src_entities is not None:
            for k1 in self.src_entities:
                result['SrcEntities'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        self.dest_entities = []
        if m.get('DestEntities') is not None:
            for k1 in m.get('DestEntities'):
                temp_model = main_models.LineageEntityVO()
                self.dest_entities.append(temp_model.from_map(k1))

        if m.get('Relationship') is not None:
            temp_model = main_models.RelationshipVO()
            self.relationship = temp_model.from_map(m.get('Relationship'))

        self.src_entities = []
        if m.get('SrcEntities') is not None:
            for k1 in m.get('SrcEntities'):
                temp_model = main_models.LineageEntityVO()
                self.src_entities.append(temp_model.from_map(k1))

        return self

