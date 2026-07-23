# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatConversationResponseBody(DaraModel):
    def __init__(
        self,
        answer: str = None,
        call_id: str = None,
        conversation_id: str = None,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        func: str = None,
        gmt_create_time: str = None,
        message_id: str = None,
        request_id: str = None,
        skill_name: str = None,
    ):
        # The reply content.
        self.answer = answer
        # The call ID.
        self.call_id = call_id
        # The session ID.
        self.conversation_id = conversation_id
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The event.
        self.event = event
        # The function name.
        self.func = func
        # The creation time.
        self.gmt_create_time = gmt_create_time
        # The message ID.
        self.message_id = message_id
        # The request ID.
        self.request_id = request_id
        # The skill name.
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.event is not None:
            result['Event'] = self.event

        if self.func is not None:
            result['Func'] = self.func

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('Func') is not None:
            self.func = m.get('Func')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        return self

