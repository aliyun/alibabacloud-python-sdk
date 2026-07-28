# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class ChatAiAgentResponseBody(DaraModel):
    def __init__(
        self,
        completed: bool = None,
        display_name: str = None,
        error_message: str = None,
        error_type: str = None,
        event: str = None,
        input: Any = None,
        items: List[main_models.ChatAiAgentResponseBodyItems] = None,
        message: str = None,
        session_id: str = None,
        success: str = None,
        text: str = None,
        tool_call_id: str = None,
        tool_name: str = None,
        usage: main_models.ChatAiAgentResponseBodyUsage = None,
    ):
        # Indicates whether this text segment is complete (the last segment of the message it belongs to).
        self.completed = completed
        # The localized display name of the tool.
        self.display_name = display_name
        # The error message when the tool call fails (only when success is false).
        self.error_message = error_message
        # The error type when the tool call fails (only when success is false).
        self.error_type = error_type
        # The event type.
        self.event = event
        # The tool input key-value pairs. The structure varies depending on the toolName.
        self.input = input
        # The list of items pending approval.
        self.items = items
        # The error message (for error events).
        self.message = message
        # The session ID for this conversation.
        self.session_id = session_id
        # Indicates whether the tool calling invoke is successful.
        self.success = success
        # The text output from the assistant.
        self.text = text
        # The tool calling ID, used to pair the invoke call and result.
        self.tool_call_id = tool_call_id
        # The tool function name.
        self.tool_name = tool_name
        # The token usage.
        self.usage = usage

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed is not None:
            result['completed'] = self.completed

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.error_type is not None:
            result['errorType'] = self.error_type

        if self.event is not None:
            result['event'] = self.event

        if self.input is not None:
            result['input'] = self.input

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.success is not None:
            result['success'] = self.success

        if self.text is not None:
            result['text'] = self.text

        if self.tool_call_id is not None:
            result['toolCallId'] = self.tool_call_id

        if self.tool_name is not None:
            result['toolName'] = self.tool_name

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completed') is not None:
            self.completed = m.get('completed')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('errorType') is not None:
            self.error_type = m.get('errorType')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('input') is not None:
            self.input = m.get('input')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ChatAiAgentResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('toolCallId') is not None:
            self.tool_call_id = m.get('toolCallId')

        if m.get('toolName') is not None:
            self.tool_name = m.get('toolName')

        if m.get('usage') is not None:
            temp_model = main_models.ChatAiAgentResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class ChatAiAgentResponseBodyUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        # The number of input tokens.
        self.input_tokens = input_tokens
        # The number of output tokens.
        self.output_tokens = output_tokens
        # The total number of tokens.
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

class ChatAiAgentResponseBodyItems(DaraModel):
    def __init__(
        self,
        args: Any = None,
        display_name: str = None,
        hitl_id: str = None,
        tool_name: str = None,
    ):
        # The original tool parameter key-value pairs.
        self.args = args
        # The display name of the tool.
        self.display_name = display_name
        # The approval item ID, used when returning hitlDecisions.
        self.hitl_id = hitl_id
        # The name of the intercepted tool.
        self.tool_name = tool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['args'] = self.args

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.hitl_id is not None:
            result['hitlId'] = self.hitl_id

        if self.tool_name is not None:
            result['toolName'] = self.tool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('hitlId') is not None:
            self.hitl_id = m.get('hitlId')

        if m.get('toolName') is not None:
            self.tool_name = m.get('toolName')

        return self

