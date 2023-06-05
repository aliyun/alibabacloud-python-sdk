# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class ExpireLoginTokenRequest(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        login_token: str = None,
        office_site_id: str = None,
        session_id: str = None,
    ):
        self.end_user_id = end_user_id
        self.login_token = login_token
        self.office_site_id = office_site_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ExpireLoginTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExpireLoginTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExpireLoginTokenResponseBody = None,
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
            temp_model = ExpireLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthCodeRequest(TeaModel):
    def __init__(
        self,
        auto_create_user: bool = None,
        end_user_id: str = None,
        external_user_id: str = None,
        policy: str = None,
    ):
        self.auto_create_user = auto_create_user
        self.end_user_id = end_user_id
        self.external_user_id = external_user_id
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_user is not None:
            result['AutoCreateUser'] = self.auto_create_user
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateUser') is not None:
            self.auto_create_user = m.get('AutoCreateUser')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class GetAuthCodeResponseBodyAuthModel(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        end_user_id: str = None,
        expire_time: str = None,
    ):
        self.auth_code = auth_code
        self.end_user_id = end_user_id
        self.expire_time = expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class GetAuthCodeResponseBody(TeaModel):
    def __init__(
        self,
        auth_model: GetAuthCodeResponseBodyAuthModel = None,
        request_id: str = None,
    ):
        self.auth_model = auth_model
        self.request_id = request_id

    def validate(self):
        if self.auth_model:
            self.auth_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_model is not None:
            result['AuthModel'] = self.auth_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthModel') is not None:
            temp_model = GetAuthCodeResponseBodyAuthModel()
            self.auth_model = temp_model.from_map(m['AuthModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuthCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAuthCodeResponseBody = None,
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
            temp_model = GetAuthCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


