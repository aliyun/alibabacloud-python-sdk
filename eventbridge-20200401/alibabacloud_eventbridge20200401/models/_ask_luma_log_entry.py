# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class AskLumaLogEntry(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        clarification_needed: bool = None,
        clarification_question: str = None,
        content: main_models.Content = None,
        conversation_id: str = None,
        created_at: str = None,
        duration_ms: int = None,
        error_code: str = None,
        error_message: str = None,
        is_error: bool = None,
        message_id: str = None,
        question: str = None,
        source: str = None,
        status: str = None,
    ):
        self.agent_name = agent_name
        self.clarification_needed = clarification_needed
        self.clarification_question = clarification_question
        self.content = content
        self.conversation_id = conversation_id
        self.created_at = created_at
        self.duration_ms = duration_ms
        self.error_code = error_code
        self.error_message = error_message
        self.is_error = is_error
        self.message_id = message_id
        self.question = question
        self.source = source
        self.status = status

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.clarification_needed is not None:
            result['ClarificationNeeded'] = self.clarification_needed

        if self.clarification_question is not None:
            result['ClarificationQuestion'] = self.clarification_question

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.duration_ms is not None:
            result['DurationMs'] = self.duration_ms

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.is_error is not None:
            result['IsError'] = self.is_error

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.question is not None:
            result['Question'] = self.question

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('ClarificationNeeded') is not None:
            self.clarification_needed = m.get('ClarificationNeeded')

        if m.get('ClarificationQuestion') is not None:
            self.clarification_question = m.get('ClarificationQuestion')

        if m.get('Content') is not None:
            temp_model = main_models.Content()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('DurationMs') is not None:
            self.duration_ms = m.get('DurationMs')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('IsError') is not None:
            self.is_error = m.get('IsError')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

