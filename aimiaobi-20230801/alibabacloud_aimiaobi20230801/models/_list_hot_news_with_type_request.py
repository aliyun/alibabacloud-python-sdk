# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListHotNewsWithTypeRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        current: int = None,
        news_type: str = None,
        news_types: List[str] = None,
        size: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.current = current
        self.news_type = news_type
        self.news_types = news_types
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.current is not None:
            result['Current'] = self.current

        if self.news_type is not None:
            result['NewsType'] = self.news_type

        if self.news_types is not None:
            result['NewsTypes'] = self.news_types

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('NewsType') is not None:
            self.news_type = m.get('NewsType')

        if m.get('NewsTypes') is not None:
            self.news_types = m.get('NewsTypes')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

