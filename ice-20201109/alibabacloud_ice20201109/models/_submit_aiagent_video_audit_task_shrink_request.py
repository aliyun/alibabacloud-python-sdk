# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAIAgentVideoAuditTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        aiagent_id: str = None,
        audit_interval: int = None,
        callback_config_shrink: str = None,
        capture_policies_shrink: str = None,
        input_shrink: str = None,
        user_data: str = None,
    ):
        # The ID of the AI agent.
        # 
        # This parameter is required.
        self.aiagent_id = aiagent_id
        # The interval, in milliseconds, at which to submit captured frames to the AI agent. Valid values: 0 to 5000. Default value: 3000. If it is set to 0, all captured frames are sent to the model in a single batch request. Otherwise, frames are sent sequentially with the specified interval between each request.
        self.audit_interval = audit_interval
        # Callback configurations.
        self.callback_config_shrink = callback_config_shrink
        # An array of frame-capturing policies. Each policy defines a set of frames to be analyzed and will generate a separate result from the model.
        # 
        # This parameter is required.
        self.capture_policies_shrink = capture_policies_shrink
        # The details of the input file.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aiagent_id is not None:
            result['AIAgentId'] = self.aiagent_id

        if self.audit_interval is not None:
            result['AuditInterval'] = self.audit_interval

        if self.callback_config_shrink is not None:
            result['CallbackConfig'] = self.callback_config_shrink

        if self.capture_policies_shrink is not None:
            result['CapturePolicies'] = self.capture_policies_shrink

        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIAgentId') is not None:
            self.aiagent_id = m.get('AIAgentId')

        if m.get('AuditInterval') is not None:
            self.audit_interval = m.get('AuditInterval')

        if m.get('CallbackConfig') is not None:
            self.callback_config_shrink = m.get('CallbackConfig')

        if m.get('CapturePolicies') is not None:
            self.capture_policies_shrink = m.get('CapturePolicies')

        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

