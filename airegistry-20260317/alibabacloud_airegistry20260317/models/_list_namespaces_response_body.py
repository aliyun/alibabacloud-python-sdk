# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airegistry20260317 import models as main_models
from darabonba.model import DaraModel

class ListNamespacesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListNamespacesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListNamespacesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListNamespacesResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListNamespacesResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListNamespacesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNamespacesResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        name: str = None,
        namespace_id: str = None,
        prompt_count: int = None,
        skill_count: int = None,
        source: str = None,
        source_index: int = None,
        tags: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.name = name
        self.namespace_id = namespace_id
        self.prompt_count = prompt_count
        self.skill_count = skill_count
        self.source = source
        self.source_index = source_index
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.prompt_count is not None:
            result['PromptCount'] = self.prompt_count

        if self.skill_count is not None:
            result['SkillCount'] = self.skill_count

        if self.source is not None:
            result['Source'] = self.source

        if self.source_index is not None:
            result['SourceIndex'] = self.source_index

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PromptCount') is not None:
            self.prompt_count = m.get('PromptCount')

        if m.get('SkillCount') is not None:
            self.skill_count = m.get('SkillCount')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceIndex') is not None:
            self.source_index = m.get('SourceIndex')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

