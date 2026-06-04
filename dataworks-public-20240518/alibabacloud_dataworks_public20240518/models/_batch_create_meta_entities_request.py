# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class BatchCreateMetaEntitiesRequest(DaraModel):
    def __init__(
        self,
        entities: List[main_models.BatchCreateMetaEntitiesRequestEntities] = None,
    ):
        # This parameter is required.
        self.entities = entities

    def validate(self):
        if self.entities:
            for v1 in self.entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Entities'] = []
        if self.entities is not None:
            for k1 in self.entities:
                result['Entities'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entities = []
        if m.get('Entities') is not None:
            for k1 in m.get('Entities'):
                temp_model = main_models.BatchCreateMetaEntitiesRequestEntities()
                self.entities.append(temp_model.from_map(k1))

        return self

class BatchCreateMetaEntitiesRequestEntities(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        comment: str = None,
        custom_attributes: Dict[str, List[str]] = None,
        entity_type: str = None,
        name: str = None,
    ):
        self.attributes = attributes
        self.comment = comment
        self.custom_attributes = custom_attributes
        # This parameter is required.
        self.entity_type = entity_type
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.custom_attributes is not None:
            result['CustomAttributes'] = self.custom_attributes

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CustomAttributes') is not None:
            self.custom_attributes = m.get('CustomAttributes')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

