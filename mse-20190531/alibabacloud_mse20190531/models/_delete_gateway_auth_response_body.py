# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class DeleteGatewayAuthResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DeleteGatewayAuthResponseBodyData = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DeleteGatewayAuthResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DeleteGatewayAuthResponseBodyData(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        cookie_domain: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_white: bool = None,
        issuer: str = None,
        jwks: str = None,
        login_url: str = None,
        name: str = None,
        redirect_url: str = None,
        scopes_list: List[str] = None,
        status: bool = None,
        token_name: str = None,
        token_name_prefix: str = None,
        token_pass: bool = None,
        token_position: str = None,
        type: str = None,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.cookie_domain = cookie_domain
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.is_white = is_white
        self.issuer = issuer
        self.jwks = jwks
        self.login_url = login_url
        self.name = name
        self.redirect_url = redirect_url
        self.scopes_list = scopes_list
        self.status = status
        self.token_name = token_name
        self.token_name_prefix = token_name_prefix
        self.token_pass = token_pass
        self.token_position = token_position
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.cookie_domain is not None:
            result['CookieDomain'] = self.cookie_domain

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.is_white is not None:
            result['IsWhite'] = self.is_white

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.jwks is not None:
            result['Jwks'] = self.jwks

        if self.login_url is not None:
            result['LoginUrl'] = self.login_url

        if self.name is not None:
            result['Name'] = self.name

        if self.redirect_url is not None:
            result['RedirectUrl'] = self.redirect_url

        if self.scopes_list is not None:
            result['ScopesList'] = self.scopes_list

        if self.status is not None:
            result['Status'] = self.status

        if self.token_name is not None:
            result['TokenName'] = self.token_name

        if self.token_name_prefix is not None:
            result['TokenNamePrefix'] = self.token_name_prefix

        if self.token_pass is not None:
            result['TokenPass'] = self.token_pass

        if self.token_position is not None:
            result['TokenPosition'] = self.token_position

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('CookieDomain') is not None:
            self.cookie_domain = m.get('CookieDomain')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('Jwks') is not None:
            self.jwks = m.get('Jwks')

        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RedirectUrl') is not None:
            self.redirect_url = m.get('RedirectUrl')

        if m.get('ScopesList') is not None:
            self.scopes_list = m.get('ScopesList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TokenName') is not None:
            self.token_name = m.get('TokenName')

        if m.get('TokenNamePrefix') is not None:
            self.token_name_prefix = m.get('TokenNamePrefix')

        if m.get('TokenPass') is not None:
            self.token_pass = m.get('TokenPass')

        if m.get('TokenPosition') is not None:
            self.token_position = m.get('TokenPosition')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

