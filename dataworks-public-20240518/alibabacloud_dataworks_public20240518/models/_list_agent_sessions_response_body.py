# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListAgentSessionsResponseBody(DaraModel):
    def __init__(
        self,
        json_rpc_response: main_models.ListAgentSessionsResponseBodyJsonRpcResponse = None,
        request_id: str = None,
    ):
        self.json_rpc_response = json_rpc_response
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.json_rpc_response:
            self.json_rpc_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.json_rpc_response is not None:
            result['JsonRpcResponse'] = self.json_rpc_response.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonRpcResponse') is not None:
            temp_model = main_models.ListAgentSessionsResponseBodyJsonRpcResponse()
            self.json_rpc_response = temp_model.from_map(m.get('JsonRpcResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAgentSessionsResponseBodyJsonRpcResponse(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        result: main_models.ListAgentSessionsResponseBodyJsonRpcResponseResult = None,
    ):
        self.id = id
        self.jsonrpc = jsonrpc
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.jsonrpc is not None:
            result['Jsonrpc'] = self.jsonrpc

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Result') is not None:
            temp_model = main_models.ListAgentSessionsResponseBodyJsonRpcResponseResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListAgentSessionsResponseBodyJsonRpcResponseResult(DaraModel):
    def __init__(
        self,
        agent_sessions: List[main_models.ListAgentSessionsResponseBodyJsonRpcResponseResultAgentSessions] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.agent_sessions = agent_sessions
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.agent_sessions:
            for v1 in self.agent_sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AgentSessions'] = []
        if self.agent_sessions is not None:
            for k1 in self.agent_sessions:
                result['AgentSessions'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_sessions = []
        if m.get('AgentSessions') is not None:
            for k1 in m.get('AgentSessions'):
                temp_model = main_models.ListAgentSessionsResponseBodyJsonRpcResponseResultAgentSessions()
                self.agent_sessions.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAgentSessionsResponseBodyJsonRpcResponseResultAgentSessions(DaraModel):
    def __init__(
        self,
        meta: main_models.ListAgentSessionsResponseBodyJsonRpcResponseResultAgentSessionsMeta = None,
        session_created_at: int = None,
        session_description: str = None,
        session_id: str = None,
        session_title: str = None,
        session_updated_at: int = None,
    ):
        self.meta = meta
        self.session_created_at = session_created_at
        self.session_description = session_description
        self.session_id = session_id
        self.session_title = session_title
        self.session_updated_at = session_updated_at

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()

        if self.session_created_at is not None:
            result['SessionCreatedAt'] = self.session_created_at

        if self.session_description is not None:
            result['SessionDescription'] = self.session_description

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.session_title is not None:
            result['SessionTitle'] = self.session_title

        if self.session_updated_at is not None:
            result['SessionUpdatedAt'] = self.session_updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Meta') is not None:
            temp_model = main_models.ListAgentSessionsResponseBodyJsonRpcResponseResultAgentSessionsMeta()
            self.meta = temp_model.from_map(m.get('Meta'))

        if m.get('SessionCreatedAt') is not None:
            self.session_created_at = m.get('SessionCreatedAt')

        if m.get('SessionDescription') is not None:
            self.session_description = m.get('SessionDescription')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SessionTitle') is not None:
            self.session_title = m.get('SessionTitle')

        if m.get('SessionUpdatedAt') is not None:
            self.session_updated_at = m.get('SessionUpdatedAt')

        return self

class ListAgentSessionsResponseBodyJsonRpcResponseResultAgentSessionsMeta(DaraModel):
    def __init__(
        self,
        session_source: str = None,
        session_status: str = None,
        session_tag_list: List[main_models.ListAgentSessionsResponseBodyJsonRpcResponseResultAgentSessionsMetaSessionTagList] = None,
    ):
        self.session_source = session_source
        self.session_status = session_status
        self.session_tag_list = session_tag_list

    def validate(self):
        if self.session_tag_list:
            for v1 in self.session_tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_source is not None:
            result['SessionSource'] = self.session_source

        if self.session_status is not None:
            result['SessionStatus'] = self.session_status

        result['SessionTagList'] = []
        if self.session_tag_list is not None:
            for k1 in self.session_tag_list:
                result['SessionTagList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionSource') is not None:
            self.session_source = m.get('SessionSource')

        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')

        self.session_tag_list = []
        if m.get('SessionTagList') is not None:
            for k1 in m.get('SessionTagList'):
                temp_model = main_models.ListAgentSessionsResponseBodyJsonRpcResponseResultAgentSessionsMetaSessionTagList()
                self.session_tag_list.append(temp_model.from_map(k1))

        return self

class ListAgentSessionsResponseBodyJsonRpcResponseResultAgentSessionsMetaSessionTagList(DaraModel):
    def __init__(
        self,
        session_tag_code: str = None,
    ):
        self.session_tag_code = session_tag_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_tag_code is not None:
            result['SessionTagCode'] = self.session_tag_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionTagCode') is not None:
            self.session_tag_code = m.get('SessionTagCode')

        return self

