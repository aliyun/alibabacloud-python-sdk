# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20180612 import models as main_models
from darabonba.model import DaraModel

class ListConversationDetailsResponseBody(DaraModel):
    def __init__(
        self,
        conversation_details: List[main_models.ListConversationDetailsResponseBodyConversationDetails] = None,
        request_id: str = None,
    ):
        # The list of conversation details.
        self.conversation_details = conversation_details
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.conversation_details:
            for v1 in self.conversation_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConversationDetails'] = []
        if self.conversation_details is not None:
            for k1 in self.conversation_details:
                result['ConversationDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conversation_details = []
        if m.get('ConversationDetails') is not None:
            for k1 in m.get('ConversationDetails'):
                temp_model = main_models.ListConversationDetailsResponseBodyConversationDetails()
                self.conversation_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListConversationDetailsResponseBodyConversationDetails(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_params: str = None,
        conversation_id: str = None,
        create_time: int = None,
        sequence_id: str = None,
        speaker: str = None,
        utterance: str = None,
    ):
        # The action performed during the turn.
        self.action = action
        # The action parameters.
        self.action_params = action_params
        # The conversation ID.
        self.conversation_id = conversation_id
        # The creation time.
        self.create_time = create_time
        # The sequence ID of the conversational turn.
        self.sequence_id = sequence_id
        # The speaker. Valid values: `customer` and `chatbot`.
        self.speaker = speaker
        # The speaker\\"s utterance.
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.action_params is not None:
            result['ActionParams'] = self.action_params

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.sequence_id is not None:
            result['SequenceId'] = self.sequence_id

        if self.speaker is not None:
            result['Speaker'] = self.speaker

        if self.utterance is not None:
            result['Utterance'] = self.utterance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('SequenceId') is not None:
            self.sequence_id = m.get('SequenceId')

        if m.get('Speaker') is not None:
            self.speaker = m.get('Speaker')

        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')

        return self

