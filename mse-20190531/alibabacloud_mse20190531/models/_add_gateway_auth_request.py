# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class AddGatewayAuthRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        auth_resource_config: str = None,
        auth_resource_list: List[main_models.AddGatewayAuthRequestAuthResourceList] = None,
        auth_resource_mode: int = None,
        client_id: str = None,
        client_secret: str = None,
        cookie_domain: str = None,
        external_auth_zjson: main_models.AddGatewayAuthRequestExternalAuthZJSON = None,
        gateway_unique_id: str = None,
        is_white: bool = None,
        issuer: str = None,
        jwks: str = None,
        login_url: str = None,
        name: str = None,
        redirect_url: str = None,
        scopes_list: List[str] = None,
        status: bool = None,
        sub: str = None,
        token_name: str = None,
        token_name_prefix: str = None,
        token_pass: bool = None,
        token_position: str = None,
        type: str = None,
    ):
        self.accept_language = accept_language
        self.auth_resource_config = auth_resource_config
        # The information about the resource to be authorized.
        self.auth_resource_list = auth_resource_list
        self.auth_resource_mode = auth_resource_mode
        # The application ID registered with the OIDC authentication service.
        self.client_id = client_id
        # The application secret registered with the OIDC authentication service.
        self.client_secret = client_secret
        # The domain name of the cookie. After the authentication is passed, the cookie is sent to the specified domain name to maintain the logon status. For example, if you set `Cookie-domain` to a.example.com, the cookie is sent to the domain name `a.example.com`. If you set `Cookie-domain` to .example.com, the cookie is sent to all subdomains of `example.com`.
        self.cookie_domain = cookie_domain
        # The information about the custom authentication service.
        self.external_auth_zjson = external_auth_zjson
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # Specifies whether to enable the whitelist feature.
        self.is_white = is_white
        # The iss value of JWT claims, which indicates the issuer. You must make sure that the value of this parameter is the same as the iss value in the payload of JWT claims.
        self.issuer = issuer
        # The JWT public key. The JSON format is supported.
        self.jwks = jwks
        # The URL that is used to log on to the IDaaS instance.
        self.login_url = login_url
        # The name.
        self.name = name
        # The redirect URL.
        self.redirect_url = redirect_url
        # The OIDC scope.
        self.scopes_list = scopes_list
        # The status.
        self.status = status
        # The sub value of JWT claims, which indicates the subject. You must make sure that the value of this parameter is the same as the sub value in the payload of JWT claims. If you do not set this parameter or leave it empty, the default value, which is the value of the Issuer parameter, is used.
        self.sub = sub
        # The name of the parameter that is required to verify a token. By default, a token is prefixed with Bearer and stored in the authorization header. Example: `Authorization: Bearer token`.
        self.token_name = token_name
        # The name prefix of the parameter that is required to verify a token. By default, a token is prefixed with Bearer and stored in the authorization header. Example: `Authorization: Bearer token`
        self.token_name_prefix = token_name_prefix
        # Specifies whether to enable pass-through.
        self.token_pass = token_pass
        # The position of the parameter that is required to verify a token. By default, a token is prefixed with Bearer and stored in the authorization header. Example: `Authorization: Bearer token`.
        self.token_position = token_position
        # The authentication type. JSON Web Token (JWT) authentication, OpenID Connect (OIDC) authentication, Identity as a Service (IDaaS) authentication, or custom authentication are supported.
        self.type = type

    def validate(self):
        if self.auth_resource_list:
            for v1 in self.auth_resource_list:
                 if v1:
                    v1.validate()
        if self.external_auth_zjson:
            self.external_auth_zjson.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.auth_resource_config is not None:
            result['AuthResourceConfig'] = self.auth_resource_config

        result['AuthResourceList'] = []
        if self.auth_resource_list is not None:
            for k1 in self.auth_resource_list:
                result['AuthResourceList'].append(k1.to_map() if k1 else None)

        if self.auth_resource_mode is not None:
            result['AuthResourceMode'] = self.auth_resource_mode

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.cookie_domain is not None:
            result['CookieDomain'] = self.cookie_domain

        if self.external_auth_zjson is not None:
            result['ExternalAuthZJSON'] = self.external_auth_zjson.to_map()

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

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
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AuthResourceConfig') is not None:
            self.auth_resource_config = m.get('AuthResourceConfig')

        self.auth_resource_list = []
        if m.get('AuthResourceList') is not None:
            for k1 in m.get('AuthResourceList'):
                temp_model = main_models.AddGatewayAuthRequestAuthResourceList()
                self.auth_resource_list.append(temp_model.from_map(k1))

        if m.get('AuthResourceMode') is not None:
            self.auth_resource_mode = m.get('AuthResourceMode')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('CookieDomain') is not None:
            self.cookie_domain = m.get('CookieDomain')

        if m.get('ExternalAuthZJSON') is not None:
            temp_model = main_models.AddGatewayAuthRequestExternalAuthZJSON()
            self.external_auth_zjson = temp_model.from_map(m.get('ExternalAuthZJSON'))

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

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

class AddGatewayAuthRequestExternalAuthZJSON(DaraModel):
    def __init__(
        self,
        allow_request_headers: List[str] = None,
        allow_upstream_headers: List[str] = None,
        body_max_bytes: int = None,
        is_restrict: bool = None,
        prefix_path: str = None,
        service_id: int = None,
        timeout: int = None,
        token_key: str = None,
        with_rematch_route: bool = None,
        with_request_body: bool = None,
    ):
        # The header that can be carried in an authentication request.
        self.allow_request_headers = allow_request_headers
        # The header that can be retained in an authentication response.
        self.allow_upstream_headers = allow_upstream_headers
        self.body_max_bytes = body_max_bytes
        # Specifies whether the gateway allows a client request when the authentication server is unavailable. If a connection to the authentication server fails to be established or a 5xx error code is returned, the authentication server is unavailable.
        self.is_restrict = is_restrict
        # The path of the authentication API provided by the authentication service. The path supports the prefix match method.
        self.prefix_path = prefix_path
        # The ID of the service.
        self.service_id = service_id
        # The timeout period. Unit: seconds.
        self.timeout = timeout
        # The header that stores a token in an authentication request. In most cases, a token is stored in the Authorization or Cookie header.
        self.token_key = token_key
        self.with_rematch_route = with_rematch_route
        self.with_request_body = with_request_body

    def validate(self):
        pass

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

class AddGatewayAuthRequestAuthResourceList(DaraModel):
    def __init__(
        self,
        auth_resource_header_list: List[main_models.AddGatewayAuthRequestAuthResourceListAuthResourceHeaderList] = None,
        domain_id: int = None,
        ignore_case: bool = None,
        match_type: str = None,
        path: str = None,
    ):
        self.auth_resource_header_list = auth_resource_header_list
        # The domain ID.
        self.domain_id = domain_id
        self.ignore_case = ignore_case
        self.match_type = match_type
        # The request path.
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
        result['AuthResourceHeaderList'] = []
        if self.auth_resource_header_list is not None:
            for k1 in self.auth_resource_header_list:
                result['AuthResourceHeaderList'].append(k1.to_map() if k1 else None)

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.ignore_case is not None:
            result['IgnoreCase'] = self.ignore_case

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_resource_header_list = []
        if m.get('AuthResourceHeaderList') is not None:
            for k1 in m.get('AuthResourceHeaderList'):
                temp_model = main_models.AddGatewayAuthRequestAuthResourceListAuthResourceHeaderList()
                self.auth_resource_header_list.append(temp_model.from_map(k1))

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('IgnoreCase') is not None:
            self.ignore_case = m.get('IgnoreCase')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

class AddGatewayAuthRequestAuthResourceListAuthResourceHeaderList(DaraModel):
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

