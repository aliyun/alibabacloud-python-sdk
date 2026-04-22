# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetAgentSessionTokenUsageResponseBody(DaraModel):
    def __init__(
        self,
        json_rpc_response: main_models.GetAgentSessionTokenUsageResponseBodyJsonRpcResponse = None,
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
            temp_model = main_models.GetAgentSessionTokenUsageResponseBodyJsonRpcResponse()
            self.json_rpc_response = temp_model.from_map(m.get('JsonRpcResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAgentSessionTokenUsageResponseBodyJsonRpcResponse(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        result: main_models.GetAgentSessionTokenUsageResponseBodyJsonRpcResponseResult = None,
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
            temp_model = main_models.GetAgentSessionTokenUsageResponseBodyJsonRpcResponseResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetAgentSessionTokenUsageResponseBodyJsonRpcResponseResult(DaraModel):
    def __init__(
        self,
        cached_tokens: int = None,
        completion_tokens: int = None,
        prompt_tokens: int = None,
        thoughts_tokens: int = None,
        total_tokens: int = None,
    ):
        self.cached_tokens = cached_tokens
        self.completion_tokens = completion_tokens
        self.prompt_tokens = prompt_tokens
        self.thoughts_tokens = thoughts_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cached_tokens is not None:
            result['CachedTokens'] = self.cached_tokens

        if self.completion_tokens is not None:
            result['CompletionTokens'] = self.completion_tokens

        if self.prompt_tokens is not None:
            result['PromptTokens'] = self.prompt_tokens

        if self.thoughts_tokens is not None:
            result['ThoughtsTokens'] = self.thoughts_tokens

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CachedTokens') is not None:
            self.cached_tokens = m.get('CachedTokens')

        if m.get('CompletionTokens') is not None:
            self.completion_tokens = m.get('CompletionTokens')

        if m.get('PromptTokens') is not None:
            self.prompt_tokens = m.get('PromptTokens')

        if m.get('ThoughtsTokens') is not None:
            self.thoughts_tokens = m.get('ThoughtsTokens')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

