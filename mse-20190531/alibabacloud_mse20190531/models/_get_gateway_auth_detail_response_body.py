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
        # The response code. It synchronizes with the Success parameter. If Success is true, the code is 200.
        self.code = code
        # The authentication details.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
        # The YAML configuration for the complex mode.
        self.auth_resource_config = auth_resource_config
        # The authorization resource mode. Valid values:
        # - 0: Simple mode.
        # - 1: Complex mode.
        self.auth_resource_mode = auth_resource_mode
        # The application ID registered for the service. This parameter is used for OIDC and IDaaS.
        self.client_id = client_id
        # The application secret registered for the service. This parameter is used for OIDC and IDaaS.
        self.client_secret = client_secret
        # The domain name of the cookie. After authentication, the cookie is sent to the specified domain name to maintain the logon state. This parameter is used for OIDC and IDaaS.
        self.cookie_domain = cookie_domain
        # The custom authentication information.
        self.external_auth_z = external_auth_z
        # The ID of the gateway to which the authentication belongs.
        self.gateway_id = gateway_id
        # The unique ID of the gateway to which the authentication belongs.
        self.gateway_unique_id = gateway_unique_id
        # The GMT time when the authentication was created.
        self.gmt_create = gmt_create
        # The GMT time when the authentication was modified.
        self.gmt_modified = gmt_modified
        # The authentication ID.
        self.id = id
        # Authorization blacklist and whitelist mode:
        # 
        # - true: whitelist mode (hosts and paths in the list can be accessed without authentication, while all others require authentication).
        # - false: blacklist mode (hosts and paths in the list require authentication, while all others can be accessed directly).
        self.is_white = is_white
        # Used when the authentication type is JWT or OIDC. For JWT, it represents the iss (issuer) claim in the JWT. For OIDC, it represents the iss (issuer) claim in the OIDC token.
        self.issuer = issuer
        # The JWT public key in JSON format.
        self.jwks = jwks
        # The URL of the user logon page for the IDaaS instance. This parameter is used for IDaaS.
        self.login_url = login_url
        # The authentication name.
        self.name = name
        # The redirect URL after successful authorization. This parameter is used for OIDC and IDaaS, and must be consistent with the redirect URL configured in OIDC or IDaaS.
        self.redirect_url = redirect_url
        # The list of authorization rules for authentication. Multiple rule conditions have an OR relationship, and multiple matching items within a rule condition have an AND relationship.
        self.resource_list = resource_list
        # The OIDC scopes. This parameter is used for OIDC.
        self.scopes_list = scopes_list
        # Indicates whether authentication is enabled.
        self.status = status
        # Used when the authentication type is JWT. It represents the sub (subject) claim in the JWT.
        self.sub = sub
        # The location where the JWT token is stored.
        self.token_name = token_name
        # The prefix of the JWT token.
        self.token_name_prefix = token_name_prefix
        # Specifies whether to pass through the token.
        self.token_pass = token_pass
        # The position of the JWT token. Valid values:
        # - HEADER: Transmitted through the HTTP header.
        self.token_position = token_position
        # The authentication type. Valid values:
        # - JWT
        # - OIDC
        # - IDaaS
        # - ExternalAuthZ (self-managed authentication service)
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
        # The ID of the authentication to which the rule belongs.
        self.auth_id = auth_id
        # The request headers of the rule. This parameter is currently only used for custom authentication.
        self.auth_resource_header_list = auth_resource_header_list
        # The ID of the domain name in the rule.
        self.domain_id = domain_id
        # The domain name in the rule.
        self.domain_name = domain_name
        # The ID of the gateway to which the rule belongs.
        self.gateway_id = gateway_id
        # The unique ID of the gateway to which the rule belongs.
        self.gateway_unique_id = gateway_unique_id
        # The GMT time when the authorization rule was created.
        self.gmt_create = gmt_create
        # The GMT time when the authorization rule was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the authorization rule.
        self.id = id
        # Specifies whether case sensitivity is enabled for the path. Valid values:
        # - true: Case sensitivity is enabled.
        # - false: Case sensitivity is disabled.
        self.ignore_case = ignore_case
        # The authorization blacklist and whitelist mode. Valid values:
        # - true: Whitelist mode. Hosts and paths in the list can be accessed without verification, while all others require verification.
        # - false: Blacklist mode. Hosts and paths in the list require verification, while all others can be accessed directly.
        self.is_white = is_white
        # The matching type for the request path. Valid values:
        # - EQUAL: Exact match.
        # - PRE: Prefix match.
        # - ERGULAR: Regular expression match.
        self.match_type = match_type
        # The matching path of the rule.
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
        # The name of the request header.
        self.header_key = header_key
        # The matching condition. Valid values:
        # - EQUAL: Equal to.
        # - NOT_EQUAL: Not equal to.
        # - EXIST: Exists.
        # - NOT_EXIST: Does not exist.
        # - INCLUDE: Includes.
        # - EXCLUDE: Excludes.
        # - PREFIX: Prefix.
        # - SUFFIX: Suffix.
        # - REGREX: Regular expression.
        self.header_method = header_method
        # The value of the request header.
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
        # The allowed request headers.
        self.allow_request_headers = allow_request_headers
        # The allowed response headers.
        self.allow_upstream_headers = allow_upstream_headers
        # The maximum size of the request body in bytes.
        self.body_max_bytes = body_max_bytes
        # Specifies the custom authentication mode. Valid values:
        # - true: Strict mode. If the authentication service is unavailable (for example, the connection fails or a 5xx status code is returned), the gateway rejects the client request.
        # - false: Loose mode. If the authentication service is unavailable (for example, the connection fails or a 5xx status code is returned), the gateway allows the client request.
        self.is_restrict = is_restrict
        # The path of the authentication API.
        self.prefix_path = prefix_path
        # The authentication service information.
        self.service = service
        # The ID of the authentication service.
        self.service_id = service_id
        # The timeout period of the authentication service, in seconds.
        self.timeout = timeout
        # The position of the token, which indicates the HTTP header that contains the token in the request. Common values include Authorization and Cookie.
        self.token_key = token_key
        # Specifies whether to rematch the route after authentication is completed.
        self.with_rematch_route = with_rematch_route
        # Specifies whether the request body is allowed.
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
        # The group to which the authentication service belongs.
        self.group_name = group_name
        # The authentication service name.
        self.name = name
        # The namespace of the authentication service.
        self.namespace = namespace
        # The source type of the authentication service.
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

