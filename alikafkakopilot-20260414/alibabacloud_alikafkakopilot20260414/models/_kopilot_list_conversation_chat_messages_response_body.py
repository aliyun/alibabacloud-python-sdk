# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafkakopilot20260414 import models as main_models
from darabonba.model import DaraModel

class KopilotListConversationChatMessagesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.KopilotListConversationChatMessagesResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.KopilotListConversationChatMessagesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class KopilotListConversationChatMessagesResponseBodyData(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        messages: List[main_models.KopilotListConversationChatMessagesResponseBodyDataMessages] = None,
        next_before_turn_id: int = None,
        session_id: str = None,
        total_turns: int = None,
    ):
        self.has_more = has_more
        self.messages = messages
        self.next_before_turn_id = next_before_turn_id
        self.session_id = session_id
        self.total_turns = total_turns

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more is not None:
            result['HasMore'] = self.has_more

        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        if self.next_before_turn_id is not None:
            result['NextBeforeTurnId'] = self.next_before_turn_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.total_turns is not None:
            result['TotalTurns'] = self.total_turns

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.KopilotListConversationChatMessagesResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('NextBeforeTurnId') is not None:
            self.next_before_turn_id = m.get('NextBeforeTurnId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TotalTurns') is not None:
            self.total_turns = m.get('TotalTurns')

        return self



class KopilotListConversationChatMessagesResponseBodyDataMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        feedback: str = None,
        role: str = None,
        turn_id: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.feedback = feedback
        self.role = role
        self.turn_id = turn_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.role is not None:
            result['Role'] = self.role

        if self.turn_id is not None:
            result['TurnId'] = self.turn_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('TurnId') is not None:
            self.turn_id = m.get('TurnId')

        return self

