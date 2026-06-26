# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DebugDialogueRequest(DaraModel):
    def __init__(
        self,
        additional_context: str = None,
        conversation_id: str = None,
        instance_id: str = None,
        utterance: str = None,
    ):
        # The context of the conversation.
        self.additional_context = additional_context
        # The ID of the conversation.
        # 
        # This parameter is required.
        self.conversation_id = conversation_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The user\\"s utterance.
        # 
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

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.utterance is not None:
            result['Utterance'] = self.utterance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalContext') is not None:
            self.additional_context = m.get('AdditionalContext')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')

        return self

