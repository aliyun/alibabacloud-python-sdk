# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class AskLumaResult(DaraModel):
    def __init__(
        self,
        clarification_needed: bool = None,
        clarification_question: str = None,
        constraints: main_models.Constraints = None,
        content: main_models.Content = None,
        conversation_id: str = None,
        error_code: str = None,
        error_message: str = None,
        is_error: bool = None,
        message_id: str = None,
        status: str = None,
        storage_truncated: bool = None,
    ):
        self.clarification_needed = clarification_needed
        self.clarification_question = clarification_question
        self.constraints = constraints
        self.content = content
        self.conversation_id = conversation_id
        self.error_code = error_code
        self.error_message = error_message
        self.is_error = is_error
        self.message_id = message_id
        self.status = status
        self.storage_truncated = storage_truncated

    def validate(self):
        if self.constraints:
            self.constraints.validate()
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clarification_needed is not None:
            result['ClarificationNeeded'] = self.clarification_needed

        if self.clarification_question is not None:
            result['ClarificationQuestion'] = self.clarification_question

        if self.constraints is not None:
            result['Constraints'] = self.constraints.to_map()

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.is_error is not None:
            result['IsError'] = self.is_error

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_truncated is not None:
            result['StorageTruncated'] = self.storage_truncated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClarificationNeeded') is not None:
            self.clarification_needed = m.get('ClarificationNeeded')

        if m.get('ClarificationQuestion') is not None:
            self.clarification_question = m.get('ClarificationQuestion')

        if m.get('Constraints') is not None:
            temp_model = main_models.Constraints()
            self.constraints = temp_model.from_map(m.get('Constraints'))

        if m.get('Content') is not None:
            temp_model = main_models.Content()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('IsError') is not None:
            self.is_error = m.get('IsError')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageTruncated') is not None:
            self.storage_truncated = m.get('StorageTruncated')

        return self

