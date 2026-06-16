# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class SearchMem0MemoriesRequest(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        body: Dict[str, Any] = None,
        context_store_id: str = None,
        enable_graph: bool = None,
        org_id: str = None,
        project_id: str = None,
    ):
        self.agent_space = agent_space
        self.body = body
        self.context_store_id = context_store_id
        self.enable_graph = enable_graph
        self.org_id = org_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.body is not None:
            result['body'] = self.body

        if self.context_store_id is not None:
            result['context_store_id'] = self.context_store_id

        if self.enable_graph is not None:
            result['enable_graph'] = self.enable_graph

        if self.org_id is not None:
            result['org_id'] = self.org_id

        if self.project_id is not None:
            result['project_id'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('context_store_id') is not None:
            self.context_store_id = m.get('context_store_id')

        if m.get('enable_graph') is not None:
            self.enable_graph = m.get('enable_graph')

        if m.get('org_id') is not None:
            self.org_id = m.get('org_id')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        return self

