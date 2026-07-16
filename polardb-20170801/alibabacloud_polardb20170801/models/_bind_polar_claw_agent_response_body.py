# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class BindPolarClawAgentResponseBody(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        binding: main_models.BindPolarClawAgentResponseBodyBinding = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
        total_bindings: int = None,
    ):
        # The agent ID.
        self.agent_id = agent_id
        # The application ID.
        self.application_id = application_id
        # Details of the newly created binding.
        self.binding = binding
        # The HTTP status code.
        self.code = code
        # A message that indicates the request result.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The total number of global bindings after the operation.
        self.total_bindings = total_bindings

    def validate(self):
        if self.binding:
            self.binding.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.binding is not None:
            result['Binding'] = self.binding.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_bindings is not None:
            result['TotalBindings'] = self.total_bindings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Binding') is not None:
            temp_model = main_models.BindPolarClawAgentResponseBodyBinding()
            self.binding = temp_model.from_map(m.get('Binding'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalBindings') is not None:
            self.total_bindings = m.get('TotalBindings')

        return self

class BindPolarClawAgentResponseBodyBinding(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        agent_id: str = None,
        channel: str = None,
    ):
        # The account ID.
        self.account_id = account_id
        # The agent ID.
        self.agent_id = agent_id
        # The channel ID.
        self.channel = channel

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.channel is not None:
            result['Channel'] = self.channel

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        return self

