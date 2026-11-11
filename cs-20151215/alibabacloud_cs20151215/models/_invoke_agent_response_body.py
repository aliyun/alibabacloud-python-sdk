# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List, Dict

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class InvokeAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        content: str = None,
        delta: str = None,
        message: str = None,
        message_id: str = None,
        name: str = None,
        outcome: main_models.InvokeAgentResponseBodyOutcome = None,
        parent_message_id: str = None,
        role: str = None,
        run_id: str = None,
        snapshot: Any = None,
        thread_id: str = None,
        tool_call_id: str = None,
        tool_call_name: str = None,
        type: str = None,
        value: Any = None,
    ):
        # The error code for the RUN_ERROR event.
        self.code = code
        # The tool output text for the TOOL_CALL_RESULT event. The text may be truncated.
        self.content = content
        # The incremental fragment of text, reasoning, or tool parameters. Fragments with the same ID are concatenated in order.
        self.delta = delta
        # The error description for the RUN_ERROR event.
        self.message = message
        # The ID of the message to which the text, reasoning, or tool result belongs.
        self.message_id = message_id
        # The name of the CUSTOM extension event, such as analysis_result.
        self.name = name
        # The completion reason for the RUN_FINISHED event. A value of success indicates normal completion, and interrupt indicates waiting for a response.
        self.outcome = outcome
        # The optional parent message ID for the TOOL_CALL_START event.
        self.parent_message_id = parent_message_id
        # The role of the message. The role is assistant for text messages and tool for tool results.
        self.role = role
        # The run ID of the current run for RUN_STARTED and RUN_FINISHED events.
        self.run_id = run_id
        # The thread snapshot for the STATE_SNAPSHOT event, including sessionId and requestId.
        self.snapshot = snapshot
        # The thread ID for RUN_STARTED and RUN_FINISHED events. It is consistent with the request and the thread snapshot.
        self.thread_id = thread_id
        # The tool invoke ID. It associates TOOL_CALL_START/ARGS/END/RESULT events with approval interrupts.
        self.tool_call_id = tool_call_id
        # The name of the tool for the TOOL_CALL_START event.
        self.tool_call_name = tool_call_name
        # The event type of the SSE data object. For the required fields of each event type, see the response description.
        # 
        # This parameter is required.
        self.type = type
        # The extension value of the CUSTOM event. It can be any JSON object or null.
        self.value = value

    def validate(self):
        if self.outcome:
            self.outcome.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.content is not None:
            result['content'] = self.content

        if self.delta is not None:
            result['delta'] = self.delta

        if self.message is not None:
            result['message'] = self.message

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.name is not None:
            result['name'] = self.name

        if self.outcome is not None:
            result['outcome'] = self.outcome.to_map()

        if self.parent_message_id is not None:
            result['parentMessageId'] = self.parent_message_id

        if self.role is not None:
            result['role'] = self.role

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.snapshot is not None:
            result['snapshot'] = self.snapshot

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        if self.tool_call_id is not None:
            result['toolCallId'] = self.tool_call_id

        if self.tool_call_name is not None:
            result['toolCallName'] = self.tool_call_name

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('delta') is not None:
            self.delta = m.get('delta')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outcome') is not None:
            temp_model = main_models.InvokeAgentResponseBodyOutcome()
            self.outcome = temp_model.from_map(m.get('outcome'))

        if m.get('parentMessageId') is not None:
            self.parent_message_id = m.get('parentMessageId')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('snapshot') is not None:
            self.snapshot = m.get('snapshot')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        if m.get('toolCallId') is not None:
            self.tool_call_id = m.get('toolCallId')

        if m.get('toolCallName') is not None:
            self.tool_call_name = m.get('toolCallName')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class InvokeAgentResponseBodyOutcome(DaraModel):
    def __init__(
        self,
        interrupts: List[main_models.InvokeAgentResponseBodyOutcomeInterrupts] = None,
        type: str = None,
    ):
        # The list of interrupts waiting for a response. This field appears only when outcome.type is interrupt and contains at least one item.
        self.interrupts = interrupts
        # The outcome type. A value of success indicates normal completion. A value of interrupt indicates waiting for a response, in which case the interrupts array contains at least one item.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.interrupts:
            for v1 in self.interrupts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['interrupts'] = []
        if self.interrupts is not None:
            for k1 in self.interrupts:
                result['interrupts'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.interrupts = []
        if m.get('interrupts') is not None:
            for k1 in m.get('interrupts'):
                temp_model = main_models.InvokeAgentResponseBodyOutcomeInterrupts()
                self.interrupts.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class InvokeAgentResponseBodyOutcomeInterrupts(DaraModel):
    def __init__(
        self,
        expires_at: str = None,
        id: str = None,
        message: str = None,
        metadata: Dict[str, Any] = None,
        reason: str = None,
        response_schema: Dict[str, Any] = None,
        tool_call_id: str = None,
    ):
        # The optional expiration time string of the interrupt. This field is not output for current tool approvals.
        self.expires_at = expires_at
        # The ID of the interrupt. It is used as resume[].interruptId when resuming the run.
        # 
        # This parameter is required.
        self.id = id
        # The approval description or follow-up question text displayed to the user.
        self.message = message
        # The optional extension information of the interrupt. It cannot replace tool events.
        self.metadata = metadata
        # The reason for the interrupt. The value is tool_call_approve for tool approval and ask_human for follow-up questions.
        # 
        # This parameter is required.
        self.reason = reason
        # The JSON Schema for the response. Tool approval requires decision=yes/no, and follow-up questions use strings.
        self.response_schema = response_schema
        # The optional associated tool invoke ID. It is the same as the toolCallId of the preceding TOOL_CALL_START event.
        self.tool_call_id = tool_call_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at

        if self.id is not None:
            result['id'] = self.id

        if self.message is not None:
            result['message'] = self.message

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.reason is not None:
            result['reason'] = self.reason

        if self.response_schema is not None:
            result['responseSchema'] = self.response_schema

        if self.tool_call_id is not None:
            result['toolCallId'] = self.tool_call_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('responseSchema') is not None:
            self.response_schema = m.get('responseSchema')

        if m.get('toolCallId') is not None:
            self.tool_call_id = m.get('toolCallId')

        return self

