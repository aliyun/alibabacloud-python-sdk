# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetGatewayAuthDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetGatewayAuthDetailResponseBodyData = None,
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
            temp_model = main_models.GetGatewayAuthDetailResponseBodyData()
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

class GetGatewayAuthDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        auth_resource_config: str = None,
        auth_resource_mode: int = None,
        client_id: str = None,
        client_secret: str = None,
        cookie_domain: str = None,
        external_auth_z: main_models.GetGatewayAuthDetailResponseBodyDataExternalAuthZ = None,
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
        resource_list: List[main_models.GetGatewayAuthDetailResponseBodyDataResourceList] = None,
        scopes_list: str = None,
        status: bool = None,
        sub: str = None,
        token_name: str = None,
        token_name_prefix: str = None,
        token_pass: bool = None,
        token_position: str = None,
        type: str = None,
    ):
        self.auth_resource_config = auth_resource_config
        self.auth_resource_mode = auth_resource_mode
        self.client_id = client_id
        self.client_secret = client_secret
        self.cookie_domain = cookie_domain
        self.external_auth_z = external_auth_z
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
        self.resource_list = resource_list
        self.scopes_list = scopes_list
        self.status = status
        self.sub = sub
        self.token_name = token_name
        self.token_name_prefix = token_name_prefix
        self.token_pass = token_pass
        self.token_position = token_position
        self.type = type

    def validate(self):
        if self.external_auth_z:
            self.external_auth_z.validate()
        if self.resource_list:
            for v1 in self.resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_resource_config is not None:
            result['AuthResourceConfig'] = self.auth_resource_config

        if self.auth_resource_mode is not None:
            result['AuthResourceMode'] = self.auth_resource_mode

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.cookie_domain is not None:
            result['CookieDomain'] = self.cookie_domain

        if self.external_auth_z is not None:
            result['ExternalAuthZ'] = self.external_auth_z.to_map()

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

        result['ResourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['ResourceList'].append(k1.to_map() if k1 else None)

        if self.scopes_list is not None:
            result['ScopesList'] = self.scopes_list

        if self.status is not None:
            result['Status'] = self.status

        if self.sub is not None:
            result['Sub'] = self.sub

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
        if m.get('AuthResourceConfig') is not None:
            self.auth_resource_config = m.get('AuthResourceConfig')

        if m.get('AuthResourceMode') is not None:
            self.auth_resource_mode = m.get('AuthResourceMode')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('CookieDomain') is not None:
            self.cookie_domain = m.get('CookieDomain')

        if m.get('ExternalAuthZ') is not None:
            temp_model = main_models.GetGatewayAuthDetailResponseBodyDataExternalAuthZ()
            self.external_auth_z = temp_model.from_map(m.get('ExternalAuthZ'))

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

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.GetGatewayAuthDetailResponseBodyDataResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        if m.get('ScopesList') is not None:
            self.scopes_list = m.get('ScopesList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Sub') is not None:
            self.sub = m.get('Sub')

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

class GetGatewayAuthDetailResponseBodyDataResourceList(DaraModel):
    def __init__(
        self,
        auth_id: int = None,
        auth_resource_header_list: List[main_models.GetGatewayAuthDetailResponseBodyDataResourceListAuthResourceHeaderList] = None,
        domain_id: int = None,
        domain_name: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        ignore_case: bool = None,
        is_white: bool = None,
        match_type: str = None,
        path: str = None,
    ):
        self.auth_id = auth_id
        self.auth_resource_header_list = auth_resource_header_list
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.ignore_case = ignore_case
        self.is_white = is_white
        self.match_type = match_type
        self.path = path

    def validate(self):
        if self.auth_resource_header_list:
            for v1 in self.auth_resource_header_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_id is not None:
            result['AuthId'] = self.auth_id

        result['AuthResourceHeaderList'] = []
        if self.auth_resource_header_list is not None:
            for k1 in self.auth_resource_header_list:
                result['AuthResourceHeaderList'].append(k1.to_map() if k1 else None)

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

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

        if self.ignore_case is not None:
            result['IgnoreCase'] = self.ignore_case

        if self.is_white is not None:
            result['IsWhite'] = self.is_white

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')

        self.auth_resource_header_list = []
        if m.get('AuthResourceHeaderList') is not None:
            for k1 in m.get('AuthResourceHeaderList'):
                temp_model = main_models.GetGatewayAuthDetailResponseBodyDataResourceListAuthResourceHeaderList()
                self.auth_resource_header_list.append(temp_model.from_map(k1))

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

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

        if m.get('IgnoreCase') is not None:
            self.ignore_case = m.get('IgnoreCase')

        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

class GetGatewayAuthDetailResponseBodyDataResourceListAuthResourceHeaderList(DaraModel):
    def __init__(
        self,
        header_key: str = None,
        header_method: str = None,
        header_value: str = None,
    ):
        self.header_key = header_key
        self.header_method = header_method
        self.header_value = header_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.header_key is not None:
            result['HeaderKey'] = self.header_key

        if self.header_method is not None:
            result['HeaderMethod'] = self.header_method

        if self.header_value is not None:
            result['HeaderValue'] = self.header_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')

        if m.get('HeaderMethod') is not None:
            self.header_method = m.get('HeaderMethod')

        if m.get('HeaderValue') is not None:
            self.header_value = m.get('HeaderValue')

        return self

class GetGatewayAuthDetailResponseBodyDataExternalAuthZ(DaraModel):
    def __init__(
        self,
        allow_request_headers: List[str] = None,
        allow_upstream_headers: List[str] = None,
        body_max_bytes: int = None,
        is_restrict: bool = None,
        prefix_path: str = None,
        service: main_models.GetGatewayAuthDetailResponseBodyDataExternalAuthZService = None,
        service_id: int = None,
        timeout: int = None,
        token_key: str = None,
        with_rematch_route: bool = None,
        with_request_body: bool = None,
    ):
        self.allow_request_headers = allow_request_headers
        self.allow_upstream_headers = allow_upstream_headers
        self.body_max_bytes = body_max_bytes
        self.is_restrict = is_restrict
        self.prefix_path = prefix_path
        self.service = service
        self.service_id = service_id
        self.timeout = timeout
        self.token_key = token_key
        self.with_rematch_route = with_rematch_route
        self.with_request_body = with_request_body

    def validate(self):
        if self.service:
            self.service.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_request_headers is not None:
            result['AllowRequestHeaders'] = self.allow_request_headers

        if self.allow_upstream_headers is not None:
            result['AllowUpstreamHeaders'] = self.allow_upstream_headers

        if self.body_max_bytes is not None:
            result['BodyMaxBytes'] = self.body_max_bytes

        if self.is_restrict is not None:
            result['IsRestrict'] = self.is_restrict

        if self.prefix_path is not None:
            result['PrefixPath'] = self.prefix_path

        if self.service is not None:
            result['Service'] = self.service.to_map()

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.token_key is not None:
            result['TokenKey'] = self.token_key

        if self.with_rematch_route is not None:
            result['WithRematchRoute'] = self.with_rematch_route

        if self.with_request_body is not None:
            result['WithRequestBody'] = self.with_request_body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRequestHeaders') is not None:
            self.allow_request_headers = m.get('AllowRequestHeaders')

        if m.get('AllowUpstreamHeaders') is not None:
            self.allow_upstream_headers = m.get('AllowUpstreamHeaders')

        if m.get('BodyMaxBytes') is not None:
            self.body_max_bytes = m.get('BodyMaxBytes')

        if m.get('IsRestrict') is not None:
            self.is_restrict = m.get('IsRestrict')

        if m.get('PrefixPath') is not None:
            self.prefix_path = m.get('PrefixPath')

        if m.get('Service') is not None:
            temp_model = main_models.GetGatewayAuthDetailResponseBodyDataExternalAuthZService()
            self.service = temp_model.from_map(m.get('Service'))

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('TokenKey') is not None:
            self.token_key = m.get('TokenKey')

        if m.get('WithRematchRoute') is not None:
            self.with_rematch_route = m.get('WithRematchRoute')

        if m.get('WithRequestBody') is not None:
            self.with_request_body = m.get('WithRequestBody')

        return self

class GetGatewayAuthDetailResponseBodyDataExternalAuthZService(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        source_type: str = None,
    ):
        self.group_name = group_name
        self.name = name
        self.namespace = namespace
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

