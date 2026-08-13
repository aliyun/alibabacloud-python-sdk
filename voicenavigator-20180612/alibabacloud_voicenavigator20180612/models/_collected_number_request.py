# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CollectedNumberRequest(DaraModel):
    def __init__(
        self,
        additional_context: str = None,
        conversation_id: str = None,
        instance_id: str = None,
        instance_owner_id: int = None,
        number: str = None,
    ):
        self.additional_context = additional_context
        # The session ID.
        # 
        # This parameter is required.
        self.conversation_id = conversation_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The instance owner ID.
        self.instance_owner_id = instance_owner_id
        # The phone number.
        self.number = number

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

        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id

        if self.number is not None:
            result['Number'] = self.number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalContext') is not None:
            self.additional_context = m.get('AdditionalContext')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        return self

