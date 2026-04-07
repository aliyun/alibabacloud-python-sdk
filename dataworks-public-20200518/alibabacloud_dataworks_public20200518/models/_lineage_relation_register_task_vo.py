# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class LineageRelationRegisterTaskVO(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        create_timestamp: int = None,
        input_entities: List[main_models.LineageEntityVO] = None,
        name: str = None,
        output_entities: List[main_models.LineageEntityVO] = None,
        qualified_name: str = None,
    ):
        self.attributes = attributes
        self.create_timestamp = create_timestamp
        self.input_entities = input_entities
        self.name = name
        self.output_entities = output_entities
        self.qualified_name = qualified_name

    def validate(self):
        if self.input_entities:
            for v1 in self.input_entities:
                 if v1:
                    v1.validate()
        if self.output_entities:
            for v1 in self.output_entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        result['InputEntities'] = []
        if self.input_entities is not None:
            for k1 in self.input_entities:
                result['InputEntities'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        result['OutputEntities'] = []
        if self.output_entities is not None:
            for k1 in self.output_entities:
                result['OutputEntities'].append(k1.to_map() if k1 else None)

        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        self.input_entities = []
        if m.get('InputEntities') is not None:
            for k1 in m.get('InputEntities'):
                temp_model = main_models.LineageEntityVO()
                self.input_entities.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.output_entities = []
        if m.get('OutputEntities') is not None:
            for k1 in m.get('OutputEntities'):
                temp_model = main_models.LineageEntityVO()
                self.output_entities.append(temp_model.from_map(k1))

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        return self

