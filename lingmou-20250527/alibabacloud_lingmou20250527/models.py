# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class CreateChatSessionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        license: str = None,
        platform: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.license = license
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.license is not None:
            result['license'] = self.license
        if self.platform is not None:
            result['platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('license') is not None:
            self.license = m.get('license')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        return self


class CreateChatSessionResponseBodyDataAvatarAssets(TeaModel):
    def __init__(
        self,
        md_5: str = None,
        min_required_version: str = None,
        secret: str = None,
        type: str = None,
        url: str = None,
    ):
        self.md_5 = md_5
        self.min_required_version = min_required_version
        self.secret = secret
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.md_5 is not None:
            result['md5'] = self.md_5
        if self.min_required_version is not None:
            result['minRequiredVersion'] = self.min_required_version
        if self.secret is not None:
            result['secret'] = self.secret
        if self.type is not None:
            result['type'] = self.type
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('md5') is not None:
            self.md_5 = m.get('md5')
        if m.get('minRequiredVersion') is not None:
            self.min_required_version = m.get('minRequiredVersion')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class CreateChatSessionResponseBodyDataRtcParams(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        avatar_user_id: str = None,
        channel: str = None,
        client_user_id: str = None,
        gslb: str = None,
        nonce: str = None,
        server_user_id: str = None,
        timestamp: int = None,
        token: str = None,
    ):
        self.app_id = app_id
        self.avatar_user_id = avatar_user_id
        self.channel = channel
        self.client_user_id = client_user_id
        self.gslb = gslb
        self.nonce = nonce
        self.server_user_id = server_user_id
        self.timestamp = timestamp
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.avatar_user_id is not None:
            result['avatarUserId'] = self.avatar_user_id
        if self.channel is not None:
            result['channel'] = self.channel
        if self.client_user_id is not None:
            result['clientUserId'] = self.client_user_id
        if self.gslb is not None:
            result['gslb'] = self.gslb
        if self.nonce is not None:
            result['nonce'] = self.nonce
        if self.server_user_id is not None:
            result['serverUserId'] = self.server_user_id
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('avatarUserId') is not None:
            self.avatar_user_id = m.get('avatarUserId')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('clientUserId') is not None:
            self.client_user_id = m.get('clientUserId')
        if m.get('gslb') is not None:
            self.gslb = m.get('gslb')
        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')
        if m.get('serverUserId') is not None:
            self.server_user_id = m.get('serverUserId')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class CreateChatSessionResponseBodyData(TeaModel):
    def __init__(
        self,
        avatar_assets: CreateChatSessionResponseBodyDataAvatarAssets = None,
        rtc_params: CreateChatSessionResponseBodyDataRtcParams = None,
        session_id: str = None,
    ):
        self.avatar_assets = avatar_assets
        self.rtc_params = rtc_params
        self.session_id = session_id

    def validate(self):
        if self.avatar_assets:
            self.avatar_assets.validate()
        if self.rtc_params:
            self.rtc_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_assets is not None:
            result['avatarAssets'] = self.avatar_assets.to_map()
        if self.rtc_params is not None:
            result['rtcParams'] = self.rtc_params.to_map()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarAssets') is not None:
            temp_model = CreateChatSessionResponseBodyDataAvatarAssets()
            self.avatar_assets = temp_model.from_map(m['avatarAssets'])
        if m.get('rtcParams') is not None:
            temp_model = CreateChatSessionResponseBodyDataRtcParams()
            self.rtc_params = temp_model.from_map(m['rtcParams'])
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class CreateChatSessionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateChatSessionResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateChatSessionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateChatSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChatSessionResponseBody = None,
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
            temp_model = CreateChatSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


