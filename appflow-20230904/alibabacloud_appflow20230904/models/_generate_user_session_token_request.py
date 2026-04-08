# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateUserSessionTokenRequest(DaraModel):
    def __init__(
        self,
        chatbot_id: str = None,
        expire_second: int = None,
        extra_info: str = None,
        integrate_id: str = None,
        user_avatar: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # AI Assistant ID
        self.chatbot_id = chatbot_id
        # Expiration Time, in seconds, default 24 hours
        self.expire_second = expire_second
        self.extra_info = extra_info
        # Integration ID
        self.integrate_id = integrate_id
        # User Avatar (URL)
        self.user_avatar = user_avatar
        # User ID
        # 
        # This parameter is required.
        self.user_id = user_id
        # User Nickname
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id

        if self.expire_second is not None:
            result['ExpireSecond'] = self.expire_second

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.integrate_id is not None:
            result['IntegrateId'] = self.integrate_id

        if self.user_avatar is not None:
            result['UserAvatar'] = self.user_avatar

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')

        if m.get('ExpireSecond') is not None:
            self.expire_second = m.get('ExpireSecond')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('IntegrateId') is not None:
            self.integrate_id = m.get('IntegrateId')

        if m.get('UserAvatar') is not None:
            self.user_avatar = m.get('UserAvatar')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

