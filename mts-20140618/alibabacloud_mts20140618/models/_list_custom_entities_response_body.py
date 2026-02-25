# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class ListCustomEntitiesResponseBody(DaraModel):
    def __init__(
        self,
        custom_entities: main_models.ListCustomEntitiesResponseBodyCustomEntities = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.custom_entities = custom_entities
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.custom_entities:
            self.custom_entities.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_entities is not None:
            result['CustomEntities'] = self.custom_entities.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomEntities') is not None:
            temp_model = main_models.ListCustomEntitiesResponseBodyCustomEntities()
            self.custom_entities = temp_model.from_map(m.get('CustomEntities'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomEntitiesResponseBodyCustomEntities(DaraModel):
    def __init__(
        self,
        custom_entity: List[main_models.ListCustomEntitiesResponseBodyCustomEntitiesCustomEntity] = None,
    ):
        self.custom_entity = custom_entity

    def validate(self):
        if self.custom_entity:
            for v1 in self.custom_entity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomEntity'] = []
        if self.custom_entity is not None:
            for k1 in self.custom_entity:
                result['CustomEntity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_entity = []
        if m.get('CustomEntity') is not None:
            for k1 in m.get('CustomEntity'):
                temp_model = main_models.ListCustomEntitiesResponseBodyCustomEntitiesCustomEntity()
                self.custom_entity.append(temp_model.from_map(k1))

        return self

class ListCustomEntitiesResponseBodyCustomEntitiesCustomEntity(DaraModel):
    def __init__(
        self,
        custom_entity_id: str = None,
        custom_entity_info: str = None,
        custom_entity_name: str = None,
    ):
        self.custom_entity_id = custom_entity_id
        self.custom_entity_info = custom_entity_info
        self.custom_entity_name = custom_entity_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_entity_id is not None:
            result['CustomEntityId'] = self.custom_entity_id

        if self.custom_entity_info is not None:
            result['CustomEntityInfo'] = self.custom_entity_info

        if self.custom_entity_name is not None:
            result['CustomEntityName'] = self.custom_entity_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomEntityId') is not None:
            self.custom_entity_id = m.get('CustomEntityId')

        if m.get('CustomEntityInfo') is not None:
            self.custom_entity_info = m.get('CustomEntityInfo')

        if m.get('CustomEntityName') is not None:
            self.custom_entity_name = m.get('CustomEntityName')

        return self

