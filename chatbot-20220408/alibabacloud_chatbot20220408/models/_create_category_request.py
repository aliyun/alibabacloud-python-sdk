# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCategoryRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        biz_code: str = None,
        knowledge_type: int = None,
        name: str = None,
        parent_category_id: int = None,
    ):
        # The key of the business space. If this parameter is not specified, the default business space is used. You can obtain the key from the Business Management page of your main account.
        self.agent_key = agent_key
        # The business code.
        self.biz_code = biz_code
        # The knowledge type. Valid values are 1 for an FAQ category and 3 for a document category. The default value is 1.
        self.knowledge_type = knowledge_type
        # The category name.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the parent category. Defaults to -1, which indicates the root category.
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

        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')

        return self

