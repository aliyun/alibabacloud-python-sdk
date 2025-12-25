# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIntervenesRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        intervene_type: int = None,
        page_index: int = None,
        page_size: int = None,
        query: str = None,
        rule_id: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.intervene_type = intervene_type
        self.page_index = page_index
        self.page_size = page_size
        self.query = query
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.intervene_type is not None:
            result['InterveneType'] = self.intervene_type

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InterveneType') is not None:
            self.intervene_type = m.get('InterveneType')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

