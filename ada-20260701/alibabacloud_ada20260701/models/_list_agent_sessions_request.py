# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ada20260701 import models as main_models
from darabonba.model import DaraModel

class ListAgentSessionsRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        params: main_models.ListAgentSessionsRequestParams = None,
    ):
        # The correlation identifier for this call. It is echoed in the response and does not provide idempotency guarantees.
        self.id = id
        # The JSON-RPC protocol version. Set this parameter to `2.0`.
        self.jsonrpc = jsonrpc
        # The business parameter object. The public fields are only AgentName, MaxResults, and NextToken.
        # 
        # This parameter is required.
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
    ):
        # Optional. Filters sessions by agent name. The maximum length is 64 characters.
        self.agent_name = agent_name
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 50. Keep the page size and filter conditions consistent for subsequent pages.
        self.max_results = max_results
        # The NextToken returned from the previous page. Do not pass this parameter on the first page. In the first phase, the default uses a native opaque cursor. Keep the same filter conditions and pass the token back as is.
        self.next_token = next_token

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

