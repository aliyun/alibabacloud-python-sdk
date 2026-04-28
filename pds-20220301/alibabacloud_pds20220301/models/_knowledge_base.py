# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class KnowledgeBase(DaraModel):
    def __init__(
        self,
        cover_uri: str = None,
        created_at: int = None,
        description: str = None,
        file_filter: str = None,
        knowledge_base_id: str = None,
        link_rule_list: List[main_models.LinkRule] = None,
        name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        owner_type: str = None,
        updated_at: int = None,
    ):
        self.cover_uri = cover_uri
        self.created_at = created_at
        self.description = description
        self.file_filter = file_filter
        self.knowledge_base_id = knowledge_base_id
        self.link_rule_list = link_rule_list
        self.name = name
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.updated_at = updated_at

    def validate(self):
        if self.link_rule_list:
            for v1 in self.link_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_uri is not None:
            result['cover_uri'] = self.cover_uri

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.file_filter is not None:
            result['file_filter'] = self.file_filter

        if self.knowledge_base_id is not None:
            result['knowledge_base_id'] = self.knowledge_base_id

        result['link_rule_list'] = []
        if self.link_rule_list is not None:
            for k1 in self.link_rule_list:
                result['link_rule_list'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.owner_id is not None:
            result['owner_id'] = self.owner_id

        if self.owner_name is not None:
            result['owner_name'] = self.owner_name

        if self.owner_type is not None:
            result['owner_type'] = self.owner_type

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cover_uri') is not None:
            self.cover_uri = m.get('cover_uri')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('file_filter') is not None:
            self.file_filter = m.get('file_filter')

        if m.get('knowledge_base_id') is not None:
            self.knowledge_base_id = m.get('knowledge_base_id')

        self.link_rule_list = []
        if m.get('link_rule_list') is not None:
            for k1 in m.get('link_rule_list'):
                temp_model = main_models.LinkRule()
                self.link_rule_list.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner_id') is not None:
            self.owner_id = m.get('owner_id')

        if m.get('owner_name') is not None:
            self.owner_name = m.get('owner_name')

        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

