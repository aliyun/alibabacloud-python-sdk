# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCategoryRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_type: int = None,
        parent_category_id: int = None,
    ):
        # The key of the business space. If not specified, the default business space is accessed. Obtain the key value from the business management page of the Alibaba Cloud account.
        self.agent_key = agent_key
        # The knowledge type. Valid values:
        # 
        # - 1: FAQ category.
        # - 3: Document category.
        # 
        # Default value: 1.
        self.knowledge_type = knowledge_type
        # The ID of the parent category.
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type

        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')

        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')

        return self

