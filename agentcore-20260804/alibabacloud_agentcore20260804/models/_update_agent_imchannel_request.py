# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateAgentIMChannelRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateAgentIMChannelRequestBody = None,
        client_token: str = None,
    ):
        # The request body.
        self.body = body
        # The reserved idempotency token. The backend does not provide persistent idempotency guarantees in this phase.
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateAgentIMChannelRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateAgentIMChannelRequestBody(DaraModel):
    def __init__(
        self,
        channel_config: main_models.UpdateAgentIMChannelRequestBodyChannelConfig = None,
        enabled: bool = None,
        service_endpoint_id: str = None,
    ):
        # The channel behavior configuration. When provided, the entire configuration is replaced. An empty object restores default values.
        self.channel_config = channel_config
        # Specifies whether to enable the IM channel. Default value: true (when created).
        self.enabled = enabled
        # The ID of the bound ServiceEndpoint. The endpoint must belong to the specified agent and its current version, be in the ready state, and have a public endpoint address.
        self.service_endpoint_id = service_endpoint_id

    def validate(self):
        if self.channel_config:
            self.channel_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_config is not None:
            result['channelConfig'] = self.channel_config.to_map()

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.service_endpoint_id is not None:
            result['serviceEndpointId'] = self.service_endpoint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelConfig') is not None:
            temp_model = main_models.UpdateAgentIMChannelRequestBodyChannelConfig()
            self.channel_config = temp_model.from_map(m.get('channelConfig'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('serviceEndpointId') is not None:
            self.service_endpoint_id = m.get('serviceEndpointId')

        return self

class UpdateAgentIMChannelRequestBodyChannelConfig(DaraModel):
    def __init__(
        self,
        show_thinking: bool = None,
        show_tool_calls: bool = None,
    ):
        # Specifies whether to display the thinking process in IM messages. Default value: false.
        self.show_thinking = show_thinking
        # Specifies whether to display the tool calling process in IM messages. Default value: false.
        self.show_tool_calls = show_tool_calls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.show_thinking is not None:
            result['showThinking'] = self.show_thinking

        if self.show_tool_calls is not None:
            result['showToolCalls'] = self.show_tool_calls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('showThinking') is not None:
            self.show_thinking = m.get('showThinking')

        if m.get('showToolCalls') is not None:
            self.show_tool_calls = m.get('showToolCalls')

        return self

