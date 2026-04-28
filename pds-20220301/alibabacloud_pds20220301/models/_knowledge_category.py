# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class KnowledgeCategory(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        keywords: List[str] = None,
        knowledge_base_id: str = None,
        knowledge_base_name: str = None,
        knowledge_category_id: str = None,
        name: str = None,
        owner: str = None,
        owner_type: str = None,
        parent_knowledge_category_id: str = None,
        status: str = None,
        updated_at: int = None,
    ):
        self.created_at = created_at
        self.description = description
        self.keywords = keywords
        self.knowledge_base_id = knowledge_base_id
        self.knowledge_base_name = knowledge_base_name
        self.knowledge_category_id = knowledge_category_id
        self.name = name
        self.owner = owner
        self.owner_type = owner_type
        self.parent_knowledge_category_id = parent_knowledge_category_id
        self.status = status
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.keywords is not None:
            result['keywords'] = self.keywords

        if self.knowledge_base_id is not None:
            result['knowledge_base_id'] = self.knowledge_base_id

        if self.knowledge_base_name is not None:
            result['knowledge_base_name'] = self.knowledge_base_name

        if self.knowledge_category_id is not None:
            result['knowledge_category_id'] = self.knowledge_category_id

        if self.name is not None:
            result['name'] = self.name

        if self.owner is not None:
            result['owner'] = self.owner

        if self.owner_type is not None:
            result['owner_type'] = self.owner_type

        if self.parent_knowledge_category_id is not None:
            result['parent_knowledge_category_id'] = self.parent_knowledge_category_id

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('keywords') is not None:
            self.keywords = m.get('keywords')

        if m.get('knowledge_base_id') is not None:
            self.knowledge_base_id = m.get('knowledge_base_id')

        if m.get('knowledge_base_name') is not None:
            self.knowledge_base_name = m.get('knowledge_base_name')

        if m.get('knowledge_category_id') is not None:
            self.knowledge_category_id = m.get('knowledge_category_id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')

        if m.get('parent_knowledge_category_id') is not None:
            self.parent_knowledge_category_id = m.get('parent_knowledge_category_id')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

