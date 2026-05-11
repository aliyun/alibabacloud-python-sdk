# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20180612 import models as main_models
from darabonba.model import DaraModel

class QueryConversationsResponseBody(DaraModel):
    def __init__(
        self,
        conversations: List[main_models.QueryConversationsResponseBodyConversations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.conversations = conversations
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.conversations:
            for v1 in self.conversations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conversations'] = []
        if self.conversations is not None:
            for k1 in self.conversations:
                result['Conversations'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conversations = []
        if m.get('Conversations') is not None:
            for k1 in m.get('Conversations'):
                temp_model = main_models.QueryConversationsResponseBodyConversations()
                self.conversations.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryConversationsResponseBodyConversations(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        calling_number: str = None,
        conversation_id: str = None,
        effective_answer_count: int = None,
        end_time: int = None,
        skill_group_id: str = None,
        transferred_to_agent: bool = None,
        user_utterance_count: int = None,
    ):
        self.begin_time = begin_time
        self.calling_number = calling_number
        self.conversation_id = conversation_id
        self.effective_answer_count = effective_answer_count
        self.end_time = end_time
        self.skill_group_id = skill_group_id
        self.transferred_to_agent = transferred_to_agent
        self.user_utterance_count = user_utterance_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.effective_answer_count is not None:
            result['EffectiveAnswerCount'] = self.effective_answer_count

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.transferred_to_agent is not None:
            result['TransferredToAgent'] = self.transferred_to_agent

        if self.user_utterance_count is not None:
            result['UserUtteranceCount'] = self.user_utterance_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('EffectiveAnswerCount') is not None:
            self.effective_answer_count = m.get('EffectiveAnswerCount')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('TransferredToAgent') is not None:
            self.transferred_to_agent = m.get('TransferredToAgent')

        if m.get('UserUtteranceCount') is not None:
            self.user_utterance_count = m.get('UserUtteranceCount')

        return self

