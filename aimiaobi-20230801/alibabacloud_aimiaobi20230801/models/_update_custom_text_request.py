# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCustomTextRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        commodity_code: str = None,
        content: str = None,
        id: int = None,
        title: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.commodity_code = commodity_code
        self.content = content
        # This parameter is required.
        self.id = id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.content is not None:
            result['Content'] = self.content

        if self.id is not None:
            result['Id'] = self.id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

