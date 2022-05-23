# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class TakeAccessTokenRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
    ):
        self.app_key = app_key
        self.app_secret = app_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['app_key'] = self.app_key
        if self.app_secret is not None:
            result['app_secret'] = self.app_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_key') is not None:
            self.app_key = m.get('app_key')
        if m.get('app_secret') is not None:
            self.app_secret = m.get('app_secret')
        return self


class TakeAccessTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        expire: int = None,
    ):
        self.access_token = access_token
        self.expire = expire

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.expire is not None:
            result['expire'] = self.expire
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')
        if m.get('expire') is not None:
            self.expire = m.get('expire')
        return self


class TakeAccessTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: TakeAccessTokenResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = TakeAccessTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class TakeAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TakeAccessTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TakeAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


