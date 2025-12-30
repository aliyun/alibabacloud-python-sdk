# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateMessageChatTokenResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_sign: str = None,
        nonce: str = None,
        request_id: str = None,
        role: str = None,
        time_stamp: int = None,
        token: str = None,
        user_id: str = None,
    ):
        # The AppID of the user.
        self.app_id = app_id
        # The application signature.
        self.app_sign = app_sign
        # The nonce used to generate the token.
        self.nonce = nonce
        # The request ID.
        self.request_id = request_id
        # The role used to generate the token.
        self.role = role
        # The expiration time. Unit: seconds. Expiration time = Current time + Validity period.
        self.time_stamp = time_stamp
        # The generated token.
        self.token = token
        # The ID of the user for joining the channel.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_sign is not None:
            result['AppSign'] = self.app_sign

        if self.nonce is not None:
            result['Nonce'] = self.nonce

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role is not None:
            result['Role'] = self.role

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.token is not None:
            result['Token'] = self.token

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppSign') is not None:
            self.app_sign = m.get('AppSign')

        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

