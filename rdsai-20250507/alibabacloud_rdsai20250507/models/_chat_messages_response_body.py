# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ChatMessagesResponseBody(DaraModel):
    def __init__(
        self,
        answer: str = None,
        approval_status: str = None,
        call_id: str = None,
        conversation_id: str = None,
        created_at: int = None,
        description: str = None,
        event: str = None,
        id: str = None,
        message_id: str = None,
        mode: str = None,
        request_id: str = None,
        round_id: str = None,
        task_id: str = None,
        tool_arguments: Dict[str, Any] = None,
        tool_name: str = None,
    ):
        # The answer content.
        self.answer = answer
        # The tool invocation approval status.
        self.approval_status = approval_status
        # The tool invocation ID.
        self.call_id = call_id
        # The conversation ID.
        self.conversation_id = conversation_id
        # The creation time.
        self.created_at = created_at
        # The tool invocation description.
        self.description = description
        # The event.
        self.event = event
        # The message ID.
        self.id = id
        # The message ID.
        self.message_id = message_id
        # The query mode.
        self.mode = mode
        # The request ID.
        self.request_id = request_id
        # The tool approval round ID.
        self.round_id = round_id
        # The asynchronous task ID.
        self.task_id = task_id
        # The tool invocation parameters.
        self.tool_arguments = tool_arguments
        # The tool name.
        self.tool_name = tool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.description is not None:
            result['Description'] = self.description

        if self.event is not None:
            result['Event'] = self.event

        if self.id is not None:
            result['Id'] = self.id

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.round_id is not None:
            result['RoundId'] = self.round_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.tool_arguments is not None:
            result['ToolArguments'] = self.tool_arguments

        if self.tool_name is not None:
            result['ToolName'] = self.tool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoundId') is not None:
            self.round_id = m.get('RoundId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('ToolArguments') is not None:
            self.tool_arguments = m.get('ToolArguments')

        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')

        return self

