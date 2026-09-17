# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ReplyAgentSessionRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        params: main_models.ReplyAgentSessionRequestParams = None,
    ):
        # The JSON-RPC correlation ID for this reply request. The response returns this value as-is. This is different from PermissionRequestId.
        # 
        # This parameter is required.
        self.id = id
        # The JSON-RPC protocol version. Fixed value: 2.0.
        self.jsonrpc = jsonrpc
        # The user interaction reply parameters.
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
            temp_model = main_models.ReplyAgentSessionRequestParams()
            self.params = temp_model.from_map(m.get('Params'))

        return self

class ReplyAgentSessionRequestParams(DaraModel):
    def __init__(
        self,
        answers: Dict[str, str] = None,
        outcome: main_models.ReplyAgentSessionRequestParamsOutcome = None,
        permission_request_id: str = None,
        session_id: str = None,
    ):
        # The answers to ask_user_question. The key is a zero-based question index string, and the value is the answer text. Specify each answer for multiple questions. Omit this parameter for regular tool authorization or cancellation.
        self.answers = answers
        # The outcome of the user interaction.
        # 
        # This parameter is required.
        self.outcome = outcome
        # The ID of the current permission_request. Obtain this value from _qwen/notify.params.data.requestId in the original SSE. This is not a ToolCallId, HTTP RequestId, or the JSON-RPC Id of this request. The value cannot be . or ..
        # 
        # This parameter is required.
        self.permission_request_id = permission_request_id
        # The LSP session ID. Use the SessionId returned by the create session operation, not the daemon internal session ID.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        if self.outcome:
            self.outcome.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answers is not None:
            result['Answers'] = self.answers

        if self.outcome is not None:
            result['Outcome'] = self.outcome.to_map()

        if self.permission_request_id is not None:
            result['PermissionRequestId'] = self.permission_request_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')

        if m.get('Outcome') is not None:
            temp_model = main_models.ReplyAgentSessionRequestParamsOutcome()
            self.outcome = temp_model.from_map(m.get('Outcome'))

        if m.get('PermissionRequestId') is not None:
            self.permission_request_id = m.get('PermissionRequestId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

class ReplyAgentSessionRequestParamsOutcome(DaraModel):
    def __init__(
        self,
        option_id: str = None,
        outcome: str = None,
    ):
        # Required and cannot be empty when Outcome is set to selected. Set this parameter to the optionId of an actual option in the event options. To submit an answer, select the option with kind=allow_once. Omit this parameter when Outcome is set to cancelled.
        self.option_id = option_id
        # The outcome type. Valid values:
        # - selected: An option is selected.
        # - cancelled: The user explicitly cancels the interaction.
        # 
        # This parameter is required.
        self.outcome = outcome

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.option_id is not None:
            result['OptionId'] = self.option_id

        if self.outcome is not None:
            result['Outcome'] = self.outcome

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionId') is not None:
            self.option_id = m.get('OptionId')

        if m.get('Outcome') is not None:
            self.outcome = m.get('Outcome')

        return self

