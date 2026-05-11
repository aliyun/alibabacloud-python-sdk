# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SilenceTimeoutRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        initial_context: str = None,
        instance_id: str = None,
        instance_owner_id: int = None,
    ):
        # This parameter is required.
        self.conversation_id = conversation_id
        self.initial_context = initial_context
        # This parameter is required.
        self.instance_id = instance_id
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

        if self.initial_context is not None:
            result['InitialContext'] = self.initial_context

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('InitialContext') is not None:
            self.initial_context = m.get('InitialContext')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')

        return self

