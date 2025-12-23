# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class CreateTokenResponseBodyToken(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        id: str = None,
        user_id: str = None,
    ):
        self.expire_time = expire_time
        self.id = id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.id is not None:
            result['Id'] = self.id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateTokenResponseBody(TeaModel):
    def __init__(
        self,
        err_code: int = None,
        err_msg: str = None,
        nls_request_id: str = None,
        request_id: str = None,
        token: CreateTokenResponseBodyToken = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.nls_request_id = nls_request_id
        self.request_id = request_id
        self.token = token

    def validate(self):
        if self.token:
            self.token.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.nls_request_id is not None:
            result['NlsRequestId'] = self.nls_request_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('NlsRequestId') is not None:
            self.nls_request_id = m.get('NlsRequestId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            temp_model = CreateTokenResponseBodyToken()
            self.token = temp_model.from_map(m['Token'])
        return self


class CreateTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTokenResponseBody = None,
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
            temp_model = CreateTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


