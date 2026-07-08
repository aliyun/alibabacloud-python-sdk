# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHotNewsWithTypeShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        current: int = None,
        news_type: str = None,
        news_types_shrink: str = None,
        size: int = None,
    ):
        # The unique identifier of the business space: [AgentKey](https://help.aliyun.com/document_detail/3027170.html).
        # 
        # This parameter is required.
        self.agent_key = agent_key
        # The current page number.
        self.current = current
        # The news category. Valid values:
        # - society: social current affairs.
        # - person: people news.
        # - government: government affairs.
        self.news_type = news_type
        # The list of news categories for multi-selection. Valid values:
        # - society: social current affairs.
        # - person: people news.
        # - government: government affairs.
        self.news_types_shrink = news_types_shrink
        # The number of records per page.
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

        if self.news_types_shrink is not None:
            result['NewsTypes'] = self.news_types_shrink

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
            self.news_types_shrink = m.get('NewsTypes')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

