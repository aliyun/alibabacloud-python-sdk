# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListRecognitionEntitiesResponseBody(DaraModel):
    def __init__(
        self,
        entities: main_models.ListRecognitionEntitiesResponseBodyEntities = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The entities.
        self.entities = entities
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # **Request ID**
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.entities:
            self.entities.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entities is not None:
            result['Entities'] = self.entities.to_map()

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
        if m.get('Entities') is not None:
            temp_model = main_models.ListRecognitionEntitiesResponseBodyEntities()
            self.entities = temp_model.from_map(m.get('Entities'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRecognitionEntitiesResponseBodyEntities(DaraModel):
    def __init__(
        self,
        entity: List[main_models.ListRecognitionEntitiesResponseBodyEntitiesEntity] = None,
    ):
        self.entity = entity

    def validate(self):
        if self.entity:
            for v1 in self.entity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Entity'] = []
        if self.entity is not None:
            for k1 in self.entity:
                result['Entity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entity = []
        if m.get('Entity') is not None:
            for k1 in m.get('Entity'):
                temp_model = main_models.ListRecognitionEntitiesResponseBodyEntitiesEntity()
                self.entity.append(temp_model.from_map(k1))

        return self

class ListRecognitionEntitiesResponseBodyEntitiesEntity(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_info: str = None,
        entity_name: str = None,
    ):
        # The ID of the entity.
        self.entity_id = entity_id
        # The additional information of the entity, in JSON format.
        self.entity_info = entity_info
        # The name of the entity.
        self.entity_name = entity_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_info is not None:
            result['EntityInfo'] = self.entity_info

        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityInfo') is not None:
            self.entity_info = m.get('EntityInfo')

        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        return self

