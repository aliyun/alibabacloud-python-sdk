# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class ListPolarClawBindingsResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        bindings: List[main_models.ListPolarClawBindingsResponseBodyBindings] = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.application_id = application_id
        self.bindings = bindings
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.bindings:
            for v1 in self.bindings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        result['Bindings'] = []
        if self.bindings is not None:
            for k1 in self.bindings:
                result['Bindings'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        self.bindings = []
        if m.get('Bindings') is not None:
            for k1 in m.get('Bindings'):
                temp_model = main_models.ListPolarClawBindingsResponseBodyBindings()
                self.bindings.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPolarClawBindingsResponseBodyBindings(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        channel: str = None,
        channel_account_id: str = None,
    ):
        # Agent ID
        self.agent_id = agent_id
        # Channel ID
        self.channel = channel
        # Account ID
        self.channel_account_id = channel_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.channel_account_id is not None:
            result['ChannelAccountId'] = self.channel_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('ChannelAccountId') is not None:
            self.channel_account_id = m.get('ChannelAccountId')

        return self

