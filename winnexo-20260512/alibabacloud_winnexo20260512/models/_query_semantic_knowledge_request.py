# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySemanticKnowledgeRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        app_token: str = None,
        graph_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        query: str = None,
        tenant_id: str = None,
    ):
        # The digital human name. Call listAuthorizedAgents first to retrieve the list of USE permissions.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The knowledge graph name. Call listGraphs first to retrieve available graphs.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
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

        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.query is not None:
            result['query'] = self.query

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')

        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

