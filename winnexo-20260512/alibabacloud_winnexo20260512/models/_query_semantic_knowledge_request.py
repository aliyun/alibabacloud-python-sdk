# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySemanticKnowledgeRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        graph_name: str = None,
        query: str = None,
        tenant_id: str = None,
    ):
        # The digital human name. Call listAuthorizedAgents first to retrieve the list of USE permissions.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # The knowledge graph name. Call listGraphs first to retrieve available graphs.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # The natural language query question.
        # 
        # This parameter is required.
        self.query = query
        # The tenant ID. This is a common parameter. In winnexo-cli, pass it explicitly with --tenant-id.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['agentName'] = self.agent_name

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.query is not None:
            result['query'] = self.query

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

