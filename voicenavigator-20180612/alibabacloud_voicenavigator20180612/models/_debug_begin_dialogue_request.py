# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DebugBeginDialogueRequest(DaraModel):
    def __init__(
        self,
        called_number: str = None,
        calling_number: str = None,
        conversation_id: str = None,
        initial_context: str = None,
        instance_id: str = None,
    ):
        self.called_number = called_number
        # This parameter is required.
        self.calling_number = calling_number
        # This parameter is required.
        self.conversation_id = conversation_id
        self.initial_context = initial_context
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.initial_context is not None:
            result['InitialContext'] = self.initial_context

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('InitialContext') is not None:
            self.initial_context = m.get('InitialContext')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

