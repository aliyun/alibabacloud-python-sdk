# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListGatewayAuthResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListGatewayAuthResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. A value of 200 indicates success.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # - true: The request is successful.
        # - false: The request fails.
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
            temp_model = main_models.ListGatewayAuthResponseBodyData()
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

class ListGatewayAuthResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.ListGatewayAuthResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The returned results.
        self.result = result
        # The total number of entries.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListGatewayAuthResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListGatewayAuthResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        auth_resource_mode: int = None,
        client_id: str = None,
        client_secret: str = None,
        cookie_domain: str = None,
        external_auth_z: main_models.ListGatewayAuthResponseBodyDataResultExternalAuthZ = None,
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
        scopes_list: str = None,
        status: bool = None,
        sub: str = None,
        token_name: str = None,
        token_name_prefix: str = None,
        token_pass: bool = None,
        token_position: str = None,
        type: str = None,
    ):
        # The authorization resource mode. Valid values:
        # - 0: simple mode.
        # - 1: complex mode.
        self.auth_resource_mode = auth_resource_mode
        # The application ID registered in the service. This parameter is used for OIDC or IDaaS.
        self.client_id = client_id
        # The application secret registered in the service. This parameter is used for OIDC or IDaaS.
        self.client_secret = client_secret
        # The domain name of the cookie. After authentication, the cookie is sent to the specified domain name to maintain the logon status. This parameter is used for OIDC or IDaaS.
        self.cookie_domain = cookie_domain
        # The custom authentication information.
        self.external_auth_z = external_auth_z
        # The gateway ID.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The authentication ID.
        self.id = id
        # The authorization blacklists and whitelists mode. Valid values:
        # - true: whitelist mode. Hosts and paths in the whitelist can be accessed without verification, while all other hosts and paths require verification.
        # - false: blacklist mode. Hosts and paths in the blacklist require verification, while all other hosts and paths can be accessed directly.
        self.is_white = is_white
        # Used when the authentication type is JWT or OIDC:
        # - JWT: the iss (issuer) claim in the JWT, which represents the issuer.
        # - OIDC: the iss (issuer) claim in the OIDC token, which represents the issuer.
        self.issuer = issuer
        # The JWT public key in JSON format.
        self.jwks = jwks
        # The URL of the user logon page for the IDaaS instance. This parameter is used for IDaaS.
        self.login_url = login_url
        # The name of the authentication rule.
        self.name = name
        # The redirect URL after successful authorization. This parameter is used for OIDC or IDaaS and must be consistent with the redirect URL configured in OIDC or IDaaS.
        self.redirect_url = redirect_url
        # The OIDC authorization scopes. This parameter is used for OIDC.
        self.scopes_list = scopes_list
        # The enabling status. Valid values:
        # - false: disabled.
        # - true: enabled.
        self.status = status
        # Used when the authentication type is JWT. The sub (subject) claim in the JWT, which represents the subject.
        self.sub = sub
        # The location where the JWT token is stored.
        # 
        # By default, the token to be verified is prefixed with Bearer and placed in the Authorization header, for example, `Authorization: Bearer token`.
        self.token_name = token_name
        # The prefix of the JWT token.
        # 
        # By default, the token to be verified is prefixed with Bearer and placed in the Authorization header, for example, `Authorization: Bearer token`.
        self.token_name_prefix = token_name_prefix
        # Specifies whether to pass through the token.
        self.token_pass = token_pass
        # The JWT token position. Valid values:
        # - HEADER: transmitted through the header.
        # 
        # By default, the token to be verified is prefixed with Bearer and placed in the Authorization header, for example, Authorization: Bearer token.
        self.token_position = token_position
        # The authentication type. Valid values:
        # - JWT
        # - OIDC
        # - IDaaS
        # - ExternalAuthZ: self-managed authentication service
        self.type = type

    def validate(self):
        if self.external_auth_z:
            self.external_auth_z.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('AuthResourceMode') is not None:
            self.auth_resource_mode = m.get('AuthResourceMode')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('CookieDomain') is not None:
            self.cookie_domain = m.get('CookieDomain')

        if m.get('ExternalAuthZ') is not None:
            temp_model = main_models.ListGatewayAuthResponseBodyDataResultExternalAuthZ()
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

class ListGatewayAuthResponseBodyDataResultExternalAuthZ(DaraModel):
    def __init__(
        self,
        allow_request_headers: List[str] = None,
        allow_upstream_headers: List[str] = None,
        body_max_bytes: int = None,
        is_restrict: bool = None,
        prefix_path: str = None,
        service: main_models.ListGatewayAuthResponseBodyDataResultExternalAuthZService = None,
        service_id: int = None,
        timeout: int = None,
        token_key: str = None,
        with_rematch_route: bool = None,
        with_request_body: bool = None,
    ):
        # The names of the allowed request headers.
        self.allow_request_headers = allow_request_headers
        # The names of the allowed response headers.
        self.allow_upstream_headers = allow_upstream_headers
        # The maximum number of bytes for the request body.
        self.body_max_bytes = body_max_bytes
        # The custom authentication mode. Valid values:
        # - true: strict mode. When the authentication service is unavailable (connection establishment fails or a 5xx status code is returned), the gateway rejects the client request.
        # - false: loose mode. When the authentication service is unavailable (connection establishment fails or a 5xx status code is returned), the gateway allows the client request.
        self.is_restrict = is_restrict
        # The path of the authentication API provided by the authentication service. The API path must be prefix-matched.
        self.prefix_path = prefix_path
        # The authentication service information.
        self.service = service
        # The ID of the authentication service.
        self.service_id = service_id
        # The timeout period of the authentication service. Unit: seconds.
        self.timeout = timeout
        # The token location, which indicates the header in the request message where the token is located. Common values include Authorization and Cookie.
        self.token_key = token_key
        # Specifies whether to rematch the route after authentication is completed.
        self.with_rematch_route = with_rematch_route
        # Specifies whether to include the request body.
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
            temp_model = main_models.ListGatewayAuthResponseBodyDataResultExternalAuthZService()
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

class ListGatewayAuthResponseBodyDataResultExternalAuthZService(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        source_type: str = None,
    ):
        # The name of the service group.
        self.group_name = group_name
        # The authentication service name.
        self.name = name
        # The namespace.
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

