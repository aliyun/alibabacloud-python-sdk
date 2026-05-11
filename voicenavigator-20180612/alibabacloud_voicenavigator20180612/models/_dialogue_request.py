# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DialogueRequest(DaraModel):
    def __init__(
        self,
        additional_context: str = None,
        called_number: str = None,
        calling_number: str = None,
        conversation_id: str = None,
        emotion: str = None,
        instance_id: str = None,
        instance_owner_id: int = None,
        utterance: str = None,
    ):
        self.additional_context = additional_context
        self.called_number = called_number
        self.calling_number = calling_number
        # This parameter is required.
        self.conversation_id = conversation_id
        self.emotion = emotion
        # This parameter is required.
        self.instance_id = instance_id
        self.instance_owner_id = instance_owner_id
        # This parameter is required.
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_context is not None:
            result['AdditionalContext'] = self.additional_context

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.emotion is not None:
            result['Emotion'] = self.emotion

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id

        if self.utterance is not None:
            result['Utterance'] = self.utterance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalContext') is not None:
            self.additional_context = m.get('AdditionalContext')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')

        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')

        return self

