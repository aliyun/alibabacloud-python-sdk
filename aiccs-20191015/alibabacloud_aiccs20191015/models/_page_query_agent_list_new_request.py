# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PageQueryAgentListNewRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        is_available: bool = None,
        page_index: int = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The agent ID.
        self.agent_id = agent_id
        # The agent name.
        self.agent_name = agent_name
        # Indicates whether the agent is available for outbound calls. The value is `true` if the agent\\"s current deployment branch has a published version.
        self.is_available = is_available
        # The page index. This parameter is deprecated. Use `PageNo` instead.
        self.page_index = page_index
        # The page number.
        self.page_no = page_no
        # The page size.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.is_available is not None:
            result['IsAvailable'] = self.is_available

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

