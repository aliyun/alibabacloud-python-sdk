# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KnowledgeBaseInfo(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        industry: str = None,
        knowledge_base_type: str = None,
        name: str = None,
    ):
        self.description = description
        self.id = id
        self.industry = industry
        self.knowledge_base_type = knowledge_base_type
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.industry is not None:
            result['industry'] = self.industry

        if self.knowledge_base_type is not None:
            result['knowledgeBaseType'] = self.knowledge_base_type

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('knowledgeBaseType') is not None:
            self.knowledge_base_type = m.get('knowledgeBaseType')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

