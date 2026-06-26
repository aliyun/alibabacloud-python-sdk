# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EndDialogueRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        hang_up_params: str = None,
        instance_id: str = None,
        instance_owner_id: int = None,
    ):
        # The ID of the conversation.
        # 
        # This parameter is required.
        self.conversation_id = conversation_id
        # The hang-up parameters, in a JSON string.
        self.hang_up_params = hang_up_params
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the instance owner.
        self.instance_owner_id = instance_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.hang_up_params is not None:
            result['HangUpParams'] = self.hang_up_params

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('HangUpParams') is not None:
            self.hang_up_params = m.get('HangUpParams')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')

        return self

