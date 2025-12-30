# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class StartAIAgentOutboundCallRequest(DaraModel):
    def __init__(
        self,
        aiagent_id: str = None,
        called_number: str = None,
        caller_number: str = None,
        config: main_models.AIAgentOutboundCallConfig = None,
        ims_aiagent_free_ob_call: str = None,
        session_id: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.aiagent_id = aiagent_id
        # This parameter is required.
        self.called_number = called_number
        # This parameter is required.
        self.caller_number = caller_number
        self.config = config
        self.ims_aiagent_free_ob_call = ims_aiagent_free_ob_call
        self.session_id = session_id
        self.user_data = user_data

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aiagent_id is not None:
            result['AIAgentId'] = self.aiagent_id

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.ims_aiagent_free_ob_call is not None:
            result['ImsAIAgentFreeObCall'] = self.ims_aiagent_free_ob_call

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIAgentId') is not None:
            self.aiagent_id = m.get('AIAgentId')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')

        if m.get('Config') is not None:
            temp_model = main_models.AIAgentOutboundCallConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('ImsAIAgentFreeObCall') is not None:
            self.ims_aiagent_free_ob_call = m.get('ImsAIAgentFreeObCall')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

