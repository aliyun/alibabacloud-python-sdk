# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatMessagesResponseBody(DaraModel):
    def __init__(
        self,
        answer: str = None,
        conversation_id: str = None,
        created_at: int = None,
        event: str = None,
        id: str = None,
        message_id: str = None,
        mode: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The answer.
        self.answer = answer
        # The ID of the conversation.
        self.conversation_id = conversation_id
        # The creation time of the conversation.
        self.created_at = created_at
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
        # The ID of the asynchronous task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

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

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

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

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

