# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class ListDSEntityValueResponseBody(DaraModel):
    def __init__(
        self,
        entity_values: List[main_models.ListDSEntityValueResponseBodyEntityValues] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.entity_values = entity_values
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.entity_values:
            for v1 in self.entity_values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EntityValues'] = []
        if self.entity_values is not None:
            for k1 in self.entity_values:
                result['EntityValues'].append(k1.to_map() if k1 else None)

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
        self.entity_values = []
        if m.get('EntityValues') is not None:
            for k1 in m.get('EntityValues'):
                temp_model = main_models.ListDSEntityValueResponseBodyEntityValues()
                self.entity_values.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDSEntityValueResponseBodyEntityValues(DaraModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        entity_id: int = None,
        entity_value_id: int = None,
        modify_time: str = None,
        synonyms: List[str] = None,
    ):
        self.content = content
        self.create_time = create_time
        self.entity_id = entity_id
        self.entity_value_id = entity_value_id
        self.modify_time = modify_time
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')

        return self

