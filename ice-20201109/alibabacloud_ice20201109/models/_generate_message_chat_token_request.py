# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateMessageChatTokenRequest(DaraModel):
    def __init__(
        self,
        aiagent_id: str = None,
        expire: int = None,
        role: str = None,
        user_id: str = None,
    ):
        # The ID of the AI agent.
        # 
        # This parameter is required.
        self.aiagent_id = aiagent_id
        # The validity period. Unit: seconds. Default value: 3600.
        self.expire = expire
        # The role. A value of admin indicates that the user can perform management operations. This parameter is empty by default.
        self.role = role
        # The ID of the user to sign in. It can be up to 64 characters in length and can contain only letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aiagent_id is not None:
            result['AIAgentId'] = self.aiagent_id

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.role is not None:
            result['Role'] = self.role

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIAgentId') is not None:
            self.aiagent_id = m.get('AIAgentId')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

