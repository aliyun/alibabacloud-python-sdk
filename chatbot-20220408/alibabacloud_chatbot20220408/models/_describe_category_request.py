# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCategoryRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
    ):
        # The key of the business space. If this parameter is not specified, the default business space is accessed. You can obtain the key value from the business management page of the Alibaba Cloud account.
        self.agent_key = agent_key
        # The category ID.
        # 
        # This parameter is required.
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        return self

