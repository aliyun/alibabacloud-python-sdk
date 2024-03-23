# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class RefreshLoginTokenRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_type: str = None,
        end_user_id: str = None,
        login_identifier: str = None,
        login_token: str = None,
        office_site_id: str = None,
        session_id: str = None,
        uuid: str = None,
    ):
        self.client_id = client_id
        self.client_type = client_type
        self.end_user_id = end_user_id
        self.login_identifier = login_identifier
        self.login_token = login_token
        self.office_site_id = office_site_id
        self.session_id = session_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_identifier is not None:
            result['LoginIdentifier'] = self.login_identifier
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginIdentifier') is not None:
            self.login_identifier = m.get('LoginIdentifier')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class RefreshLoginTokenResponseBody(TeaModel):
    def __init__(
        self,
        login_token: str = None,
        request_id: str = None,
    ):
        self.login_token = login_token
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshLoginTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshLoginTokenResponseBody = None,
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
            temp_model = RefreshLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


