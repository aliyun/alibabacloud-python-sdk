# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCategoryRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        biz_code: str = None,
        category_id: int = None,
        name: str = None,
    ):
        # The key for the business space. If this parameter is omitted, the default business space is used. You can obtain the key on the **Business Management** page of your primary account.
        self.agent_key = agent_key
        # The business code.
        self.biz_code = biz_code
        # The category ID.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The category name.
        # 
        # This parameter is required.
        self.name = name

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

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

