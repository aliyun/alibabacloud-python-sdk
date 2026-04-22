# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListAgentSessionsRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        params: main_models.ListAgentSessionsRequestParams = None,
    ):
        self.id = id
        self.jsonrpc = jsonrpc
        self.params = params

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.jsonrpc is not None:
            result['Jsonrpc'] = self.jsonrpc

        if self.params is not None:
            result['Params'] = self.params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Params') is not None:
            temp_model = main_models.ListAgentSessionsRequestParams()
            self.params = temp_model.from_map(m.get('Params'))

        return self

class ListAgentSessionsRequestParams(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        max_results: int = None,
        next_token: str = None,
        session_id: str = None,
        session_source_list: List[str] = None,
        session_title: str = None,
        tag_list: List[str] = None,
    ):
        self.agent_name = agent_name
        self.max_results = max_results
        self.next_token = next_token
        self.session_id = session_id
        self.session_source_list = session_source_list
        self.session_title = session_title
        self.tag_list = tag_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.session_source_list is not None:
            result['SessionSourceList'] = self.session_source_list

        if self.session_title is not None:
            result['SessionTitle'] = self.session_title

        if self.tag_list is not None:
            result['TagList'] = self.tag_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SessionSourceList') is not None:
            self.session_source_list = m.get('SessionSourceList')

        if m.get('SessionTitle') is not None:
            self.session_title = m.get('SessionTitle')

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        return self

