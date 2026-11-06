# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_ada20260701 import models as main_models
from darabonba.model import DaraModel

class ListAgentSessionsResponseBody(DaraModel):
    def __init__(
        self,
        json_rpc_response: main_models.ListAgentSessionsResponseBodyJsonRpcResponse = None,
        request_id: str = None,
    ):
        # The JSON-RPC response object. The business result is located in Result.
        self.json_rpc_response = json_rpc_response
        # The server-side request ID used to troubleshoot this call.
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
        # The Id from the request, echoed as is.
        self.id = id
        # The fixed value `2.0`.
        self.jsonrpc = jsonrpc
        # The paginated result.
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
        max_results: int = None,
        next_token: str = None,
        session_list: Any = None,
    ):
        # The effective page size for the current page.
        self.max_results = max_results
        # The credential to continue querying the next page. Pass it as is to Params.NextToken. Pagination ends when the token is not returned or is empty.
        self.next_token = next_token
        # The array of session summaries for the current page. If no matching records are found, an empty array [] is returned. The type is any. The fields of array elements retain the original backend names. For the structure, see the supplementary description of response parameters.
        self.session_list = session_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.session_list is not None:
            result['SessionList'] = self.session_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SessionList') is not None:
            self.session_list = m.get('SessionList')

        return self

