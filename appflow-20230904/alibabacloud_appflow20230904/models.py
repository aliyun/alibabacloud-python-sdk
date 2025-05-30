# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class GenerateUserSessionTokenRequest(TeaModel):
    def __init__(
        self,
        chatbot_id: str = None,
        expire_second: int = None,
        integrate_id: str = None,
        user_avatar: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # AI Assistant ID
        self.chatbot_id = chatbot_id
        # Expiration Time, in seconds, default 24 hours
        self.expire_second = expire_second
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id
        if self.expire_second is not None:
            result['ExpireSecond'] = self.expire_second
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
        if m.get('IntegrateId') is not None:
            self.integrate_id = m.get('IntegrateId')
        if m.get('UserAvatar') is not None:
            self.user_avatar = m.get('UserAvatar')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GenerateUserSessionTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_session_token: str = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Token.
        self.user_session_token = user_session_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_session_token is not None:
            result['UserSessionToken'] = self.user_session_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSessionToken') is not None:
            self.user_session_token = m.get('UserSessionToken')
        return self


class GenerateUserSessionTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateUserSessionTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateUserSessionTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


