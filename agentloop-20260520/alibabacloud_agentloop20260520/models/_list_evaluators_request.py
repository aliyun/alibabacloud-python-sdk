# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEvaluatorsRequest(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        source: str = None,
        type: str = None,
    ):
        # The AgentSpace name.
        # 
        # This parameter is required.
        self.agent_space = agent_space
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.max_results = max_results
        # The fuzzy match condition for the evaluator name.
        self.name = name
        # The pagination token for the next page.
        self.next_token = next_token
        # The evaluator source filter.
        self.source = source
        # The evaluator type filter.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.name is not None:
            result['name'] = self.name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.source is not None:
            result['source'] = self.source

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

