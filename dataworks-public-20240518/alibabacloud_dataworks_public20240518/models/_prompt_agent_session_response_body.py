# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class PromptAgentSessionResponseBody(DaraModel):
    def __init__(
        self,
        error: Any = None,
        id: str = None,
        jsonrpc: str = None,
        meta: main_models.PromptAgentSessionResponseBodyMeta = None,
        method: str = None,
        params: Any = None,
        request_id: str = None,
        result: Any = None,
        timestamp: int = None,
    ):
        # The error message in the SSE frame. The returned content complies with the open-source Agent Client Protocol (ACP) specification. For more information, see https://agentclientprotocol.com/protocol/prompt-turn.
        self.error = error
        # The ID passed by the requester. The value is returned as is.
        self.id = id
        # The JSON-RPC version. Set the value to 2.0.
        self.jsonrpc = jsonrpc
        # Carried only by verified native events. The client saves the EventCursor after fully applying the event, and uses EventId and EventEpoch to resume the subscription to GetAgentSessionEvents after a disconnection. Common subscription errors do not contain proof of the native execution terminal state.
        self.meta = meta
        # The method of the SSE. The returned content complies with the open-source Agent Client Protocol (ACP) specification. For more information, see https://agentclientprotocol.com/protocol/prompt-turn.
        self.method = method
        # The params of the SSE. The returned content complies with the open-source Agent Client Protocol (ACP) specification. For more information, see https://agentclientprotocol.com/protocol/prompt-turn.
        self.params = params
        # Id of the request
        self.request_id = request_id
        # The result set of the SSE frame. The returned content complies with the open-source Agent Client Protocol (ACP) specification. For more information, see https://agentclientprotocol.com/protocol/prompt-turn.
        self.result = result
        # The timestamp.
        self.timestamp = timestamp

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error

        if self.id is not None:
            result['Id'] = self.id

        if self.jsonrpc is not None:
            result['Jsonrpc'] = self.jsonrpc

        if self.meta is not None:
            result['Meta'] = self.meta.to_map()

        if self.method is not None:
            result['Method'] = self.method

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Meta') is not None:
            temp_model = main_models.PromptAgentSessionResponseBodyMeta()
            self.meta = temp_model.from_map(m.get('Meta'))

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class PromptAgentSessionResponseBodyMeta(DaraModel):
    def __init__(
        self,
        event_cursor: main_models.PromptAgentSessionResponseBodyMetaEventCursor = None,
    ):
        # The resumption cursor of the current native event. Carried only by verified native events. The client saves the cursor after fully processing the event, and uses the EventId and EventEpoch in it to resume the subscription to GetAgentSessionEvents after a disconnection without resending the prompt.
        self.event_cursor = event_cursor

    def validate(self):
        if self.event_cursor:
            self.event_cursor.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_cursor is not None:
            result['EventCursor'] = self.event_cursor.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCursor') is not None:
            temp_model = main_models.PromptAgentSessionResponseBodyMetaEventCursor()
            self.event_cursor = temp_model.from_map(m.get('EventCursor'))

        return self

class PromptAgentSessionResponseBodyMetaEventCursor(DaraModel):
    def __init__(
        self,
        event_epoch: str = None,
        event_id: str = None,
        event_type: str = None,
        prompt_id: str = None,
        session_id: str = None,
    ):
        # The event stream generation identifier returned when the current prompt is accepted. It is paired with EventId during resumption. Pass this value as is to the EventEpoch query parameter of GetAgentSessionEvents to verify the same event stream.
        self.event_epoch = event_epoch
        # The integer ID of the current native event, returned as a decimal string. The client saves it after fully processing the event, and passes this value as the Last-Event-Id HTTP header of GetAgentSessionEvents during resumption to continue receiving subsequent events.
        self.event_id = event_id
        # The type of the current native event, obtained from the type field of the native event. The examples do not constitute a fixed enumeration.
        self.event_type = event_type
        # The execution identifier returned when the current prompt is accepted. It is used to associate the current execution with its events.
        self.prompt_id = prompt_id
        # The identifier of the current DataAgent session. It is used to associate the event with its session.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_epoch is not None:
            result['EventEpoch'] = self.event_epoch

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.prompt_id is not None:
            result['PromptId'] = self.prompt_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventEpoch') is not None:
            self.event_epoch = m.get('EventEpoch')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('PromptId') is not None:
            self.prompt_id = m.get('PromptId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

