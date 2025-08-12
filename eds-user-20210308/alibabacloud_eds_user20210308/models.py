# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class GroupResources(TeaModel):
    def __init__(
        self,
        region: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.region = region
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ThirdAppOidcSsoConfigEndpoints(TeaModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        discovery_endpoint: str = None,
        guest_authorization_endpoint: str = None,
        issuer: str = None,
        jwks_endpoint: str = None,
        logout_endpoint: str = None,
        revoke_endpoint: str = None,
        token_endpoint: str = None,
        userinfo_endpoint: str = None,
    ):
        self.authorization_endpoint = authorization_endpoint
        self.discovery_endpoint = discovery_endpoint
        self.guest_authorization_endpoint = guest_authorization_endpoint
        self.issuer = issuer
        self.jwks_endpoint = jwks_endpoint
        self.logout_endpoint = logout_endpoint
        self.revoke_endpoint = revoke_endpoint
        self.token_endpoint = token_endpoint
        self.userinfo_endpoint = userinfo_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_endpoint is not None:
            result['AuthorizationEndpoint'] = self.authorization_endpoint
        if self.discovery_endpoint is not None:
            result['DiscoveryEndpoint'] = self.discovery_endpoint
        if self.guest_authorization_endpoint is not None:
            result['GuestAuthorizationEndpoint'] = self.guest_authorization_endpoint
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.jwks_endpoint is not None:
            result['JwksEndpoint'] = self.jwks_endpoint
        if self.logout_endpoint is not None:
            result['LogoutEndpoint'] = self.logout_endpoint
        if self.revoke_endpoint is not None:
            result['RevokeEndpoint'] = self.revoke_endpoint
        if self.token_endpoint is not None:
            result['TokenEndpoint'] = self.token_endpoint
        if self.userinfo_endpoint is not None:
            result['UserinfoEndpoint'] = self.userinfo_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('AuthorizationEndpoint')
        if m.get('DiscoveryEndpoint') is not None:
            self.discovery_endpoint = m.get('DiscoveryEndpoint')
        if m.get('GuestAuthorizationEndpoint') is not None:
            self.guest_authorization_endpoint = m.get('GuestAuthorizationEndpoint')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('JwksEndpoint') is not None:
            self.jwks_endpoint = m.get('JwksEndpoint')
        if m.get('LogoutEndpoint') is not None:
            self.logout_endpoint = m.get('LogoutEndpoint')
        if m.get('RevokeEndpoint') is not None:
            self.revoke_endpoint = m.get('RevokeEndpoint')
        if m.get('TokenEndpoint') is not None:
            self.token_endpoint = m.get('TokenEndpoint')
        if m.get('UserinfoEndpoint') is not None:
            self.userinfo_endpoint = m.get('UserinfoEndpoint')
        return self


class ThirdAppOidcSsoConfig(TeaModel):
    def __init__(
        self,
        access_token_effective_time: int = None,
        code_effective_time: int = None,
        enable_auth_login: bool = None,
        endpoints: ThirdAppOidcSsoConfigEndpoints = None,
        grant_scopes: List[str] = None,
        grant_types: List[str] = None,
        id_token_algorithm_type: str = None,
        id_token_effective_time: int = None,
        redirect_uris: List[str] = None,
        refresh_token_effective: int = None,
    ):
        self.access_token_effective_time = access_token_effective_time
        self.code_effective_time = code_effective_time
        self.enable_auth_login = enable_auth_login
        self.endpoints = endpoints
        self.grant_scopes = grant_scopes
        self.grant_types = grant_types
        self.id_token_algorithm_type = id_token_algorithm_type
        self.id_token_effective_time = id_token_effective_time
        self.redirect_uris = redirect_uris
        self.refresh_token_effective = refresh_token_effective

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_effective_time is not None:
            result['AccessTokenEffectiveTime'] = self.access_token_effective_time
        if self.code_effective_time is not None:
            result['CodeEffectiveTime'] = self.code_effective_time
        if self.enable_auth_login is not None:
            result['EnableAuthLogin'] = self.enable_auth_login
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.grant_scopes is not None:
            result['GrantScopes'] = self.grant_scopes
        if self.grant_types is not None:
            result['GrantTypes'] = self.grant_types
        if self.id_token_algorithm_type is not None:
            result['IdTokenAlgorithmType'] = self.id_token_algorithm_type
        if self.id_token_effective_time is not None:
            result['IdTokenEffectiveTime'] = self.id_token_effective_time
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris
        if self.refresh_token_effective is not None:
            result['RefreshTokenEffective'] = self.refresh_token_effective
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenEffectiveTime') is not None:
            self.access_token_effective_time = m.get('AccessTokenEffectiveTime')
        if m.get('CodeEffectiveTime') is not None:
            self.code_effective_time = m.get('CodeEffectiveTime')
        if m.get('EnableAuthLogin') is not None:
            self.enable_auth_login = m.get('EnableAuthLogin')
        if m.get('Endpoints') is not None:
            temp_model = ThirdAppOidcSsoConfigEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('GrantScopes') is not None:
            self.grant_scopes = m.get('GrantScopes')
        if m.get('GrantTypes') is not None:
            self.grant_types = m.get('GrantTypes')
        if m.get('IdTokenAlgorithmType') is not None:
            self.id_token_algorithm_type = m.get('IdTokenAlgorithmType')
        if m.get('IdTokenEffectiveTime') is not None:
            self.id_token_effective_time = m.get('IdTokenEffectiveTime')
        if m.get('RedirectUris') is not None:
            self.redirect_uris = m.get('RedirectUris')
        if m.get('RefreshTokenEffective') is not None:
            self.refresh_token_effective = m.get('RefreshTokenEffective')
        return self


class ThirdAppSecrets(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        secret: str = None,
    ):
        self.enable = enable
        self.secret = secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.secret is not None:
            result['Secret'] = self.secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        return self


class ThirdApp(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        name: str = None,
        oidc_sso_config: ThirdAppOidcSsoConfig = None,
        secrets: List[ThirdAppSecrets] = None,
    ):
        self.app_key = app_key
        self.name = name
        self.oidc_sso_config = oidc_sso_config
        self.secrets = secrets

    def validate(self):
        if self.oidc_sso_config:
            self.oidc_sso_config.validate()
        if self.secrets:
            for k in self.secrets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.name is not None:
            result['Name'] = self.name
        if self.oidc_sso_config is not None:
            result['OidcSsoConfig'] = self.oidc_sso_config.to_map()
        result['Secrets'] = []
        if self.secrets is not None:
            for k in self.secrets:
                result['Secrets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OidcSsoConfig') is not None:
            temp_model = ThirdAppOidcSsoConfig()
            self.oidc_sso_config = temp_model.from_map(m['OidcSsoConfig'])
        self.secrets = []
        if m.get('Secrets') is not None:
            for k in m.get('Secrets'):
                temp_model = ThirdAppSecrets()
                self.secrets.append(temp_model.from_map(k))
        return self


class WaIdPermissions(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_basic_child: bool = None,
        name: str = None,
        sub_permissions: List['WaIdPermissions'] = None,
        type: str = None,
    ):
        self.code = code
        self.is_basic_child = is_basic_child
        self.name = name
        self.sub_permissions = sub_permissions
        self.type = type

    def validate(self):
        if self.sub_permissions:
            for k in self.sub_permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_basic_child is not None:
            result['IsBasicChild'] = self.is_basic_child
        if self.name is not None:
            result['Name'] = self.name
        result['SubPermissions'] = []
        if self.sub_permissions is not None:
            for k in self.sub_permissions:
                result['SubPermissions'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsBasicChild') is not None:
            self.is_basic_child = m.get('IsBasicChild')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.sub_permissions = []
        if m.get('SubPermissions') is not None:
            for k in m.get('SubPermissions'):
                temp_model = WaIdPermissions()
                self.sub_permissions.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class BatchSetDesktopManagerRequest(TeaModel):
    def __init__(
        self,
        is_desktop_manager: str = None,
        users: List[str] = None,
    ):
        self.is_desktop_manager = is_desktop_manager
        # This parameter is required.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_desktop_manager is not None:
            result['IsDesktopManager'] = self.is_desktop_manager
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDesktopManager') is not None:
            self.is_desktop_manager = m.get('IsDesktopManager')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class BatchSetDesktopManagerResponseBody(TeaModel):
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


class BatchSetDesktopManagerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchSetDesktopManagerResponseBody = None,
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
            temp_model = BatchSetDesktopManagerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeUserPasswordRequest(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        new_password: str = None,
    ):
        self.end_user_id = end_user_id
        self.new_password = new_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        return self


class ChangeUserPasswordResponseBody(TeaModel):
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


class ChangeUserPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeUserPasswordResponseBody = None,
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
            temp_model = ChangeUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUsedPropertyRequest(TeaModel):
    def __init__(
        self,
        property_id: int = None,
    ):
        # The ID of the property. You can call the [ListProperty](https://help.aliyun.com/document_detail/410890.html) operation to query the property ID.
        # 
        # This parameter is required.
        self.property_id = property_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        return self


class CheckUsedPropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        use_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The number of convenience users that are associated with the property.
        self.use_count = use_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.use_count is not None:
            result['UseCount'] = self.use_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')
        return self


class CheckUsedPropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckUsedPropertyResponseBody = None,
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
            temp_model = CheckUsedPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUsedPropertyValueRequest(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_value_id: int = None,
    ):
        # The property ID. You can call the [ListProperty](~~ListProperty~~) operation to query property ID.
        # 
        # This parameter is required.
        self.property_id = property_id
        # The ID of the property value. You can call the [ListProperty](~~ListProperty~~) operation to query the ID of the property value.
        # 
        # This parameter is required.
        self.property_value_id = property_value_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class CheckUsedPropertyValueResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        use_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The number of convenience accounts that are associated with the specified custom property value.
        self.use_count = use_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.use_count is not None:
            result['UseCount'] = self.use_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')
        return self


class CheckUsedPropertyValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckUsedPropertyValueResponseBody = None,
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
            temp_model = CheckUsedPropertyValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        description: str = None,
        group_name: str = None,
        parent_group_id: str = None,
        solution_id: str = None,
    ):
        self.biz_type = biz_type
        self.description = description
        self.group_name = group_name
        self.parent_group_id = parent_group_id
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.parent_group_id is not None:
            result['ParentGroupId'] = self.parent_group_id
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ParentGroupId') is not None:
            self.parent_group_id = m.get('ParentGroupId')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        request_id: str = None,
    ):
        self.group_id = group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGroupResponseBody = None,
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
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrgRequest(TeaModel):
    def __init__(
        self,
        org_name: str = None,
        parent_org_id: str = None,
    ):
        # This parameter is required.
        self.org_name = org_name
        # This parameter is required.
        self.parent_org_id = parent_org_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.parent_org_id is not None:
            result['ParentOrgId'] = self.parent_org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('ParentOrgId') is not None:
            self.parent_org_id = m.get('ParentOrgId')
        return self


class CreateOrgResponseBody(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        request_id: str = None,
    ):
        self.org_id = org_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrgResponseBody = None,
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
            temp_model = CreateOrgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePropertyRequest(TeaModel):
    def __init__(
        self,
        property_key: str = None,
        property_values: List[str] = None,
    ):
        # The property name.
        # 
        # This parameter is required.
        self.property_key = property_key
        # The values of the property. You can specify up to 50 values for a property.
        self.property_values = property_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_values is not None:
            result['PropertyValues'] = self.property_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyValues') is not None:
            self.property_values = m.get('PropertyValues')
        return self


class CreatePropertyResponseBodyCreateResultSavePropertyValueModelFailedPropertyValues(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        property_id: int = None,
        property_value: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the property value.
        self.property_id = property_id
        # The value of the property.
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        return self


class CreatePropertyResponseBodyCreateResultSavePropertyValueModelSavePropertyValues(TeaModel):
    def __init__(
        self,
        property_value: str = None,
        property_value_id: int = None,
    ):
        # The value of the property.
        self.property_value = property_value
        # The ID of the property value.
        self.property_value_id = property_value_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class CreatePropertyResponseBodyCreateResultSavePropertyValueModel(TeaModel):
    def __init__(
        self,
        failed_property_values: List[CreatePropertyResponseBodyCreateResultSavePropertyValueModelFailedPropertyValues] = None,
        save_property_values: List[CreatePropertyResponseBodyCreateResultSavePropertyValueModelSavePropertyValues] = None,
    ):
        # The property values that failed to be created.
        self.failed_property_values = failed_property_values
        # Details of the property values that were created.
        self.save_property_values = save_property_values

    def validate(self):
        if self.failed_property_values:
            for k in self.failed_property_values:
                if k:
                    k.validate()
        if self.save_property_values:
            for k in self.save_property_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedPropertyValues'] = []
        if self.failed_property_values is not None:
            for k in self.failed_property_values:
                result['FailedPropertyValues'].append(k.to_map() if k else None)
        result['SavePropertyValues'] = []
        if self.save_property_values is not None:
            for k in self.save_property_values:
                result['SavePropertyValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_property_values = []
        if m.get('FailedPropertyValues') is not None:
            for k in m.get('FailedPropertyValues'):
                temp_model = CreatePropertyResponseBodyCreateResultSavePropertyValueModelFailedPropertyValues()
                self.failed_property_values.append(temp_model.from_map(k))
        self.save_property_values = []
        if m.get('SavePropertyValues') is not None:
            for k in m.get('SavePropertyValues'):
                temp_model = CreatePropertyResponseBodyCreateResultSavePropertyValueModelSavePropertyValues()
                self.save_property_values.append(temp_model.from_map(k))
        return self


class CreatePropertyResponseBodyCreateResult(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_key: str = None,
        save_property_value_model: CreatePropertyResponseBodyCreateResultSavePropertyValueModel = None,
    ):
        # The ID of the property.
        self.property_id = property_id
        # The name of the property.
        self.property_key = property_key
        # The result of creating the property value.
        self.save_property_value_model = save_property_value_model

    def validate(self):
        if self.save_property_value_model:
            self.save_property_value_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.save_property_value_model is not None:
            result['SavePropertyValueModel'] = self.save_property_value_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('SavePropertyValueModel') is not None:
            temp_model = CreatePropertyResponseBodyCreateResultSavePropertyValueModel()
            self.save_property_value_model = temp_model.from_map(m['SavePropertyValueModel'])
        return self


class CreatePropertyResponseBody(TeaModel):
    def __init__(
        self,
        create_result: CreatePropertyResponseBodyCreateResult = None,
        request_id: str = None,
    ):
        # The result of creating the property.
        self.create_result = create_result
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.create_result:
            self.create_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_result is not None:
            result['CreateResult'] = self.create_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateResult') is not None:
            temp_model = CreatePropertyResponseBodyCreateResult()
            self.create_result = temp_model.from_map(m['CreateResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePropertyResponseBody = None,
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
            temp_model = CreatePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceGroupRequest(TeaModel):
    def __init__(
        self,
        is_resource_group_with_office_site: int = None,
        platform: str = None,
        resource_group_name: str = None,
    ):
        self.is_resource_group_with_office_site = is_resource_group_with_office_site
        self.platform = platform
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_resource_group_with_office_site is not None:
            result['IsResourceGroupWithOfficeSite'] = self.is_resource_group_with_office_site
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsResourceGroupWithOfficeSite') is not None:
            self.is_resource_group_with_office_site = m.get('IsResourceGroupWithOfficeSite')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        return self


class CreateResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        self.request_id = request_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceGroupResponseBody = None,
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
            temp_model = CreateResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUsersRequestUsers(TeaModel):
    def __init__(
        self,
        email: str = None,
        end_user_id: str = None,
        org_id: str = None,
        owner_type: str = None,
        password: str = None,
        phone: str = None,
        real_nick_name: str = None,
        remark: str = None,
    ):
        # The email address of the convenience user. The email address is used to receive notifications about events such as desktop assignment. You must specify an email address or a mobile number to receive notifications.
        self.email = email
        # The username of the convenience user. The name can contain lowercase letters, digits, and underscores (_), and must be 3 to 24 characters in length.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The organization to which the convenience user belongs.
        self.org_id = org_id
        # The type of the account ownership.
        # 
        # Valid values:
        # 
        # *   CreateFromManager: administrator-activated
        # *   Normal: user-activated
        self.owner_type = owner_type
        # The user password.
        # 
        # >  The password must be at least 10 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters (excluding spaces).
        self.password = password
        # Mobile numbers are not supported on the international site (alibabacloud.com).
        self.phone = phone
        # The display name of the end user.
        self.real_nick_name = real_nick_name
        # The remarks on the convenience user.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.password is not None:
            result['Password'] = self.password
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.real_nick_name is not None:
            result['RealNickName'] = self.real_nick_name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RealNickName') is not None:
            self.real_nick_name = m.get('RealNickName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class CreateUsersRequest(TeaModel):
    def __init__(
        self,
        auto_lock_time: str = None,
        is_local_admin: bool = None,
        password: str = None,
        password_expire_days: str = None,
        users: List[CreateUsersRequestUsers] = None,
    ):
        # The date on which the convenience users are automatically locked.
        self.auto_lock_time = auto_lock_time
        self.is_local_admin = is_local_admin
        # The initial password. If this parameter is left empty, an email for password reset is sent to the specified email address.
        self.password = password
        self.password_expire_days = password_expire_days
        # The information about the convenience user.
        # 
        # This parameter is required.
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_lock_time is not None:
            result['AutoLockTime'] = self.auto_lock_time
        if self.is_local_admin is not None:
            result['IsLocalAdmin'] = self.is_local_admin
        if self.password is not None:
            result['Password'] = self.password
        if self.password_expire_days is not None:
            result['PasswordExpireDays'] = self.password_expire_days
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoLockTime') is not None:
            self.auto_lock_time = m.get('AutoLockTime')
        if m.get('IsLocalAdmin') is not None:
            self.is_local_admin = m.get('IsLocalAdmin')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordExpireDays') is not None:
            self.password_expire_days = m.get('PasswordExpireDays')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = CreateUsersRequestUsers()
                self.users.append(temp_model.from_map(k))
        return self


class CreateUsersResponseBodyCreateResultCreatedUsers(TeaModel):
    def __init__(
        self,
        email: str = None,
        end_user_id: str = None,
        phone: str = None,
        real_nick_name: str = None,
        remark: str = None,
    ):
        # The email address of the end user.
        self.email = email
        # The name of the end user.
        self.end_user_id = end_user_id
        # The mobile number of the end user.
        self.phone = phone
        # The display name of the end user.
        self.real_nick_name = real_nick_name
        # The remarks of the end user.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.real_nick_name is not None:
            result['RealNickName'] = self.real_nick_name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RealNickName') is not None:
            self.real_nick_name = m.get('RealNickName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class CreateUsersResponseBodyCreateResultFailedUsers(TeaModel):
    def __init__(
        self,
        email: str = None,
        end_user_id: str = None,
        error_code: str = None,
        error_message: str = None,
        phone: str = None,
    ):
        # The email address of the end user.
        self.email = email
        # The name of the end user.
        self.end_user_id = end_user_id
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The mobile number of the end user.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class CreateUsersResponseBodyCreateResult(TeaModel):
    def __init__(
        self,
        created_users: List[CreateUsersResponseBodyCreateResultCreatedUsers] = None,
        failed_users: List[CreateUsersResponseBodyCreateResultFailedUsers] = None,
    ):
        # Details of the created convenience users.
        self.created_users = created_users
        # Details of the convenience users that failed to be created.
        self.failed_users = failed_users

    def validate(self):
        if self.created_users:
            for k in self.created_users:
                if k:
                    k.validate()
        if self.failed_users:
            for k in self.failed_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CreatedUsers'] = []
        if self.created_users is not None:
            for k in self.created_users:
                result['CreatedUsers'].append(k.to_map() if k else None)
        result['FailedUsers'] = []
        if self.failed_users is not None:
            for k in self.failed_users:
                result['FailedUsers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.created_users = []
        if m.get('CreatedUsers') is not None:
            for k in m.get('CreatedUsers'):
                temp_model = CreateUsersResponseBodyCreateResultCreatedUsers()
                self.created_users.append(temp_model.from_map(k))
        self.failed_users = []
        if m.get('FailedUsers') is not None:
            for k in m.get('FailedUsers'):
                temp_model = CreateUsersResponseBodyCreateResultFailedUsers()
                self.failed_users.append(temp_model.from_map(k))
        return self


class CreateUsersResponseBody(TeaModel):
    def __init__(
        self,
        all_succeed: bool = None,
        create_result: CreateUsersResponseBodyCreateResult = None,
        request_id: str = None,
    ):
        self.all_succeed = all_succeed
        # The result of user creation.
        self.create_result = create_result
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.create_result:
            self.create_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_succeed is not None:
            result['AllSucceed'] = self.all_succeed
        if self.create_result is not None:
            result['CreateResult'] = self.create_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllSucceed') is not None:
            self.all_succeed = m.get('AllSucceed')
        if m.get('CreateResult') is not None:
            temp_model = CreateUsersResponseBodyCreateResult()
            self.create_result = temp_model.from_map(m['CreateResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUsersResponseBody = None,
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
            temp_model = CreateUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_group_ids: List[str] = None,
    ):
        # >  The ID of the resource group that you want to delete.
        # 
        # *   If you also specify ResourceGroupIds, both parameters take effect.
        self.resource_group_id = resource_group_id
        # >  The IDs of the resource groups that you want to delete.
        # 
        # *   If you also specify ResourceGroupId, both parameters take effect.
        self.resource_group_ids = resource_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')
        return self


class DeleteResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceGroupResponseBody = None,
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
            temp_model = DeleteResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserPropertyValueRequest(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_value_id: int = None,
        user_id: int = None,
    ):
        # The property ID. You can call the [ListProperty](~~ListProperty~~) operation to query the property ID.
        # 
        # This parameter is required.
        self.property_id = property_id
        # The property value ID. You can call the [ListProperty](~~ListProperty~~) operation to query the property value ID.
        # 
        # This parameter is required.
        self.property_value_id = property_value_id
        # The user ID. You can call the [DescribeUsers](~~DescribeUsers~~) operation to query the user ID, which is the return value of the `Id` parameter.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserPropertyValueResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteUserPropertyValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserPropertyValueResponseBody = None,
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
            temp_model = DeleteUserPropertyValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupUserRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        filter: str = None,
        group_id: str = None,
        max_results: int = None,
        next_token: str = None,
        solution_id: str = None,
    ):
        self.biz_type = biz_type
        self.filter = filter
        self.group_id = group_id
        self.max_results = max_results
        self.next_token = next_token
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        return self


class DescribeGroupUserResponseBodyGroups(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        user_count: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.user_count = user_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        return self


class DescribeGroupUserResponseBodyUsers(TeaModel):
    def __init__(
        self,
        address: str = None,
        avatar: str = None,
        email: str = None,
        end_user_id: str = None,
        gmt_created: str = None,
        gmt_join_group: str = None,
        job_number: str = None,
        nick_name: str = None,
        phone: str = None,
        remark: str = None,
    ):
        self.address = address
        self.avatar = avatar
        self.email = email
        self.end_user_id = end_user_id
        self.gmt_created = gmt_created
        self.gmt_join_group = gmt_join_group
        self.job_number = job_number
        self.nick_name = nick_name
        self.phone = phone
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_join_group is not None:
            result['GmtJoinGroup'] = self.gmt_join_group
        if self.job_number is not None:
            result['JobNumber'] = self.job_number
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtJoinGroup') is not None:
            self.gmt_join_group = m.get('GmtJoinGroup')
        if m.get('JobNumber') is not None:
            self.job_number = m.get('JobNumber')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class DescribeGroupUserResponseBody(TeaModel):
    def __init__(
        self,
        groups: List[DescribeGroupUserResponseBodyGroups] = None,
        next_token: str = None,
        request_id: str = None,
        users: List[DescribeGroupUserResponseBodyUsers] = None,
    ):
        self.groups = groups
        self.next_token = next_token
        self.request_id = request_id
        self.users = users

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = DescribeGroupUserResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = DescribeGroupUserResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class DescribeGroupUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGroupUserResponseBody = None,
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
            temp_model = DescribeGroupUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupsRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        group_id: str = None,
        group_name: str = None,
        page_number: int = None,
        page_size: int = None,
        solution_id: str = None,
        transfer_file_need_approval: bool = None,
    ):
        self.biz_type = biz_type
        self.group_id = group_id
        self.group_name = group_name
        self.page_number = page_number
        self.page_size = page_size
        self.solution_id = solution_id
        self.transfer_file_need_approval = transfer_file_need_approval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        if self.transfer_file_need_approval is not None:
            result['TransferFileNeedApproval'] = self.transfer_file_need_approval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        if m.get('TransferFileNeedApproval') is not None:
            self.transfer_file_need_approval = m.get('TransferFileNeedApproval')
        return self


class DescribeGroupsResponseBodyGroups(TeaModel):
    def __init__(
        self,
        authed_resources: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        transfer_file_need_approval: bool = None,
        user_count: int = None,
    ):
        self.authed_resources = authed_resources
        self.create_time = create_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.transfer_file_need_approval = transfer_file_need_approval
        self.user_count = user_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authed_resources is not None:
            result['AuthedResources'] = self.authed_resources
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.transfer_file_need_approval is not None:
            result['TransferFileNeedApproval'] = self.transfer_file_need_approval
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthedResources') is not None:
            self.authed_resources = m.get('AuthedResources')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('TransferFileNeedApproval') is not None:
            self.transfer_file_need_approval = m.get('TransferFileNeedApproval')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        return self


class DescribeGroupsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        groups: List[DescribeGroupsResponseBodyGroups] = None,
        request_id: str = None,
    ):
        self.count = count
        self.groups = groups
        self.request_id = request_id

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = DescribeGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGroupsResponseBody = None,
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
            temp_model = DescribeGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMfaDevicesRequest(TeaModel):
    def __init__(
        self,
        ad_domain: str = None,
        end_user_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        serial_numbers: List[str] = None,
    ):
        # The domain of the Active Directory (AD) workspace.
        self.ad_domain = ad_domain
        # The usernames of the convenience users.
        self.end_user_ids = end_user_ids
        # The maximum number of entries to return. Valid values: 1 to 500.\\
        # Default value: 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Set the value to the token that is obtained from the previous query.
        self.next_token = next_token
        # The serial numbers of the virtual MFA devices.
        self.serial_numbers = serial_numbers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.serial_numbers is not None:
            result['SerialNumbers'] = self.serial_numbers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SerialNumbers') is not None:
            self.serial_numbers = m.get('SerialNumbers')
        return self


class DescribeMfaDevicesResponseBodyMfaDevices(TeaModel):
    def __init__(
        self,
        consecutive_fails: int = None,
        device_type: str = None,
        email: str = None,
        end_user_id: str = None,
        gmt_enabled: str = None,
        gmt_unlock: str = None,
        id: int = None,
        serial_number: str = None,
        status: str = None,
    ):
        # The number of consecutive failures to bind the virtual MFA device, or the number of authentication failures based on the virtual MFA device.
        self.consecutive_fails = consecutive_fails
        # The type of the virtual MFA device. The value can only be TOTP_VIRTUAL. This value indicates that the virtual MFA device follows the Time-based One-time Password (TOTP) algorithm.
        self.device_type = device_type
        # >  This parameter is not publicly available.
        self.email = email
        # The username of the convenience user that uses the virtual MFA device.
        self.end_user_id = end_user_id
        # The time when the virtual MFA device was enabled. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.gmt_enabled = gmt_enabled
        # The time when the locked virtual MFA device was automatically unlocked. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.gmt_unlock = gmt_unlock
        # >  This parameter is not publicly available.
        self.id = id
        # The serial number of the virtual MFA device. The serial number is unique for each device.
        self.serial_number = serial_number
        # The status of the virtual MFA device.
        # 
        # Valid values:
        # 
        # *   LOCKED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   UNBOUND
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NORMAL
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consecutive_fails is not None:
            result['ConsecutiveFails'] = self.consecutive_fails
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.gmt_enabled is not None:
            result['GmtEnabled'] = self.gmt_enabled
        if self.gmt_unlock is not None:
            result['GmtUnlock'] = self.gmt_unlock
        if self.id is not None:
            result['Id'] = self.id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsecutiveFails') is not None:
            self.consecutive_fails = m.get('ConsecutiveFails')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('GmtEnabled') is not None:
            self.gmt_enabled = m.get('GmtEnabled')
        if m.get('GmtUnlock') is not None:
            self.gmt_unlock = m.get('GmtUnlock')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMfaDevicesResponseBody(TeaModel):
    def __init__(
        self,
        mfa_devices: List[DescribeMfaDevicesResponseBodyMfaDevices] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The information about the virtual MFA devices.
        self.mfa_devices = mfa_devices
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.mfa_devices:
            for k in self.mfa_devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MfaDevices'] = []
        if self.mfa_devices is not None:
            for k in self.mfa_devices:
                result['MfaDevices'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mfa_devices = []
        if m.get('MfaDevices') is not None:
            for k in m.get('MfaDevices'):
                temp_model = DescribeMfaDevicesResponseBodyMfaDevices()
                self.mfa_devices.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMfaDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMfaDevicesResponseBody = None,
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
            temp_model = DescribeMfaDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOrgByLayerRequest(TeaModel):
    def __init__(
        self,
        org_name: str = None,
        parent_org_id: str = None,
    ):
        self.org_name = org_name
        self.parent_org_id = parent_org_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.parent_org_id is not None:
            result['ParentOrgId'] = self.parent_org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('ParentOrgId') is not None:
            self.parent_org_id = m.get('ParentOrgId')
        return self


class DescribeOrgByLayerResponseBodyOrgs(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
        parent_org_id: str = None,
    ):
        self.org_id = org_id
        self.org_name = org_name
        self.parent_org_id = parent_org_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.parent_org_id is not None:
            result['ParentOrgId'] = self.parent_org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('ParentOrgId') is not None:
            self.parent_org_id = m.get('ParentOrgId')
        return self


class DescribeOrgByLayerResponseBody(TeaModel):
    def __init__(
        self,
        orgs: List[DescribeOrgByLayerResponseBodyOrgs] = None,
        request_id: str = None,
    ):
        self.orgs = orgs
        self.request_id = request_id

    def validate(self):
        if self.orgs:
            for k in self.orgs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Orgs'] = []
        if self.orgs is not None:
            for k in self.orgs:
                result['Orgs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.orgs = []
        if m.get('Orgs') is not None:
            for k in m.get('Orgs'):
                temp_model = DescribeOrgByLayerResponseBodyOrgs()
                self.orgs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOrgByLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOrgByLayerResponseBody = None,
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
            temp_model = DescribeOrgByLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOrgsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        org_name: str = None,
        parent_org_id: str = None,
        show_extras: Dict[str, Any] = None,
    ):
        # The maximum number of entries to return. Valid values: 1 to 100.\\
        # Default value: 100.
        self.max_results = max_results
        # The token that determines the start point of the query. The return value is the value of the NextToken response parameter that was returned last time the DescribeOrgs operation was called.
        self.next_token = next_token
        # The name of the organization.
        self.org_name = org_name
        # The parent organization ID.
        self.parent_org_id = parent_org_id
        self.show_extras = show_extras

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.parent_org_id is not None:
            result['ParentOrgId'] = self.parent_org_id
        if self.show_extras is not None:
            result['ShowExtras'] = self.show_extras
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('ParentOrgId') is not None:
            self.parent_org_id = m.get('ParentOrgId')
        if m.get('ShowExtras') is not None:
            self.show_extras = m.get('ShowExtras')
        return self


class DescribeOrgsShrinkRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        org_name: str = None,
        parent_org_id: str = None,
        show_extras_shrink: str = None,
    ):
        # The maximum number of entries to return. Valid values: 1 to 100.\\
        # Default value: 100.
        self.max_results = max_results
        # The token that determines the start point of the query. The return value is the value of the NextToken response parameter that was returned last time the DescribeOrgs operation was called.
        self.next_token = next_token
        # The name of the organization.
        self.org_name = org_name
        # The parent organization ID.
        self.parent_org_id = parent_org_id
        self.show_extras_shrink = show_extras_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.parent_org_id is not None:
            result['ParentOrgId'] = self.parent_org_id
        if self.show_extras_shrink is not None:
            result['ShowExtras'] = self.show_extras_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('ParentOrgId') is not None:
            self.parent_org_id = m.get('ParentOrgId')
        if m.get('ShowExtras') is not None:
            self.show_extras_shrink = m.get('ShowExtras')
        return self


class DescribeOrgsResponseBodyOrgs(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
        org_name_path: str = None,
        parent_org_id: str = None,
    ):
        # The organization ID.
        self.org_id = org_id
        # The name of the organizational unit.
        self.org_name = org_name
        self.org_name_path = org_name_path
        # The parent organization ID.
        self.parent_org_id = parent_org_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_name_path is not None:
            result['OrgNamePath'] = self.org_name_path
        if self.parent_org_id is not None:
            result['ParentOrgId'] = self.parent_org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgNamePath') is not None:
            self.org_name_path = m.get('OrgNamePath')
        if m.get('ParentOrgId') is not None:
            self.parent_org_id = m.get('ParentOrgId')
        return self


class DescribeOrgsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        orgs: List[DescribeOrgsResponseBodyOrgs] = None,
        request_id: str = None,
    ):
        # The token that determines the start point of the query. The return value is the value of the NextToken response parameter that was returned last time the DescribeOrgs operation was called.
        self.next_token = next_token
        # The organizations.
        self.orgs = orgs
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.orgs:
            for k in self.orgs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Orgs'] = []
        if self.orgs is not None:
            for k in self.orgs:
                result['Orgs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.orgs = []
        if m.get('Orgs') is not None:
            for k in m.get('Orgs'):
                temp_model = DescribeOrgsResponseBodyOrgs()
                self.orgs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOrgsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOrgsResponseBody = None,
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
            temp_model = DescribeOrgsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceGroupsRequest(TeaModel):
    def __init__(
        self,
        need_contain_resource_group_with_office_site: int = None,
        page_number: int = None,
        page_size: int = None,
        platform: str = None,
        resource_group_ids: List[str] = None,
        resource_group_name: str = None,
    ):
        self.need_contain_resource_group_with_office_site = need_contain_resource_group_with_office_site
        self.page_number = page_number
        self.page_size = page_size
        self.platform = platform
        self.resource_group_ids = resource_group_ids
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_contain_resource_group_with_office_site is not None:
            result['NeedContainResourceGroupWithOfficeSite'] = self.need_contain_resource_group_with_office_site
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedContainResourceGroupWithOfficeSite') is not None:
            self.need_contain_resource_group_with_office_site = m.get('NeedContainResourceGroupWithOfficeSite')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        return self


class DescribeResourceGroupsResponseBodyResourceGroupAppRules(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: int = None,
    ):
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeResourceGroupsResponseBodyResourceGroupPolicies(TeaModel):
    def __init__(
        self,
        id: str = None,
        is_default: bool = None,
        name: str = None,
    ):
        self.id = id
        self.is_default = is_default
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeResourceGroupsResponseBodyResourceGroupTimers(TeaModel):
    def __init__(
        self,
        bind_status: str = None,
        id: str = None,
        name: str = None,
        timer_status: str = None,
    ):
        self.bind_status = bind_status
        self.id = id
        self.name = name
        self.timer_status = timer_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_status is not None:
            result['BindStatus'] = self.bind_status
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.timer_status is not None:
            result['TimerStatus'] = self.timer_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindStatus') is not None:
            self.bind_status = m.get('BindStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TimerStatus') is not None:
            self.timer_status = m.get('TimerStatus')
        return self


class DescribeResourceGroupsResponseBodyResourceGroup(TeaModel):
    def __init__(
        self,
        app_rules: List[DescribeResourceGroupsResponseBodyResourceGroupAppRules] = None,
        auth_count: str = None,
        create_time: str = None,
        policies: List[DescribeResourceGroupsResponseBodyResourceGroupPolicies] = None,
        resource_count: str = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        timers: List[DescribeResourceGroupsResponseBodyResourceGroupTimers] = None,
    ):
        self.app_rules = app_rules
        self.auth_count = auth_count
        self.create_time = create_time
        self.policies = policies
        self.resource_count = resource_count
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.timers = timers

    def validate(self):
        if self.app_rules:
            for k in self.app_rules:
                if k:
                    k.validate()
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()
        if self.timers:
            for k in self.timers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppRules'] = []
        if self.app_rules is not None:
            for k in self.app_rules:
                result['AppRules'].append(k.to_map() if k else None)
        if self.auth_count is not None:
            result['AuthCount'] = self.auth_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        result['Timers'] = []
        if self.timers is not None:
            for k in self.timers:
                result['Timers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_rules = []
        if m.get('AppRules') is not None:
            for k in m.get('AppRules'):
                temp_model = DescribeResourceGroupsResponseBodyResourceGroupAppRules()
                self.app_rules.append(temp_model.from_map(k))
        if m.get('AuthCount') is not None:
            self.auth_count = m.get('AuthCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = DescribeResourceGroupsResponseBodyResourceGroupPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        self.timers = []
        if m.get('Timers') is not None:
            for k in m.get('Timers'):
                temp_model = DescribeResourceGroupsResponseBodyResourceGroupTimers()
                self.timers.append(temp_model.from_map(k))
        return self


class DescribeResourceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: List[DescribeResourceGroupsResponseBodyResourceGroup] = None,
        total_count: str = None,
    ):
        self.request_id = request_id
        self.resource_group = resource_group
        self.total_count = total_count

    def validate(self):
        if self.resource_group:
            for k in self.resource_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceGroup'] = []
        if self.resource_group is not None:
            for k in self.resource_group:
                result['ResourceGroup'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_group = []
        if m.get('ResourceGroup') is not None:
            for k in m.get('ResourceGroup'):
                temp_model = DescribeResourceGroupsResponseBodyResourceGroup()
                self.resource_group.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeResourceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResourceGroupsResponseBody = None,
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
            temp_model = DescribeResourceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsersRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        end_user_ids: List[str] = None,
        exclude_end_user_ids: List[str] = None,
        exclude_group_id: str = None,
        filter: str = None,
        filter_with_assigned_resource: Dict[str, str] = None,
        filter_with_assigned_resources: Dict[str, bool] = None,
        group_id: str = None,
        is_query_all_sub_orgs: bool = None,
        max_results: int = None,
        next_token: str = None,
        org_id: str = None,
        show_extras: Dict[str, Any] = None,
        solution_id: str = None,
        status: int = None,
    ):
        self.biz_type = biz_type
        # The usernames that must be exactly matched.
        self.end_user_ids = end_user_ids
        # The usernames that must be exactly excluded.
        self.exclude_end_user_ids = exclude_end_user_ids
        self.exclude_group_id = exclude_group_id
        # The string that is used for fuzzy search. You perform fuzzy search by username (EndUserId) and email address (Email). Wildcard characters (\\*) are supported. For example, if you set this parameter to `a*m`, usernames or email addresses that start with `a` and end with `m` are returned.
        self.filter = filter
        self.filter_with_assigned_resource = filter_with_assigned_resource
        self.filter_with_assigned_resources = filter_with_assigned_resources
        # The ID of the organization in which you want to query convenience users.
        self.group_id = group_id
        self.is_query_all_sub_orgs = is_query_all_sub_orgs
        # The maximum number of entries per page.
        # 
        # *   Valid values: 1 to 500.
        # *   Default value: 500.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.\\
        # If not all results are returned in a query, a value is returned for the NextToken parameter. In this case, you can use the return value of NextToken to perform the next query.
        self.next_token = next_token
        # The ID of the organization in which you want to query users.
        self.org_id = org_id
        self.show_extras = show_extras
        self.solution_id = solution_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.exclude_end_user_ids is not None:
            result['ExcludeEndUserIds'] = self.exclude_end_user_ids
        if self.exclude_group_id is not None:
            result['ExcludeGroupId'] = self.exclude_group_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.filter_with_assigned_resource is not None:
            result['FilterWithAssignedResource'] = self.filter_with_assigned_resource
        if self.filter_with_assigned_resources is not None:
            result['FilterWithAssignedResources'] = self.filter_with_assigned_resources
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.is_query_all_sub_orgs is not None:
            result['IsQueryAllSubOrgs'] = self.is_query_all_sub_orgs
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.show_extras is not None:
            result['ShowExtras'] = self.show_extras
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('ExcludeEndUserIds') is not None:
            self.exclude_end_user_ids = m.get('ExcludeEndUserIds')
        if m.get('ExcludeGroupId') is not None:
            self.exclude_group_id = m.get('ExcludeGroupId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('FilterWithAssignedResource') is not None:
            self.filter_with_assigned_resource = m.get('FilterWithAssignedResource')
        if m.get('FilterWithAssignedResources') is not None:
            self.filter_with_assigned_resources = m.get('FilterWithAssignedResources')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IsQueryAllSubOrgs') is not None:
            self.is_query_all_sub_orgs = m.get('IsQueryAllSubOrgs')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ShowExtras') is not None:
            self.show_extras = m.get('ShowExtras')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeUsersShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        end_user_ids: List[str] = None,
        exclude_end_user_ids: List[str] = None,
        exclude_group_id: str = None,
        filter: str = None,
        filter_with_assigned_resource_shrink: str = None,
        filter_with_assigned_resources_shrink: str = None,
        group_id: str = None,
        is_query_all_sub_orgs: bool = None,
        max_results: int = None,
        next_token: str = None,
        org_id: str = None,
        show_extras_shrink: str = None,
        solution_id: str = None,
        status: int = None,
    ):
        self.biz_type = biz_type
        # The usernames that must be exactly matched.
        self.end_user_ids = end_user_ids
        # The usernames that must be exactly excluded.
        self.exclude_end_user_ids = exclude_end_user_ids
        self.exclude_group_id = exclude_group_id
        # The string that is used for fuzzy search. You perform fuzzy search by username (EndUserId) and email address (Email). Wildcard characters (\\*) are supported. For example, if you set this parameter to `a*m`, usernames or email addresses that start with `a` and end with `m` are returned.
        self.filter = filter
        self.filter_with_assigned_resource_shrink = filter_with_assigned_resource_shrink
        self.filter_with_assigned_resources_shrink = filter_with_assigned_resources_shrink
        # The ID of the organization in which you want to query convenience users.
        self.group_id = group_id
        self.is_query_all_sub_orgs = is_query_all_sub_orgs
        # The maximum number of entries per page.
        # 
        # *   Valid values: 1 to 500.
        # *   Default value: 500.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.\\
        # If not all results are returned in a query, a value is returned for the NextToken parameter. In this case, you can use the return value of NextToken to perform the next query.
        self.next_token = next_token
        # The ID of the organization in which you want to query users.
        self.org_id = org_id
        self.show_extras_shrink = show_extras_shrink
        self.solution_id = solution_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.exclude_end_user_ids is not None:
            result['ExcludeEndUserIds'] = self.exclude_end_user_ids
        if self.exclude_group_id is not None:
            result['ExcludeGroupId'] = self.exclude_group_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.filter_with_assigned_resource_shrink is not None:
            result['FilterWithAssignedResource'] = self.filter_with_assigned_resource_shrink
        if self.filter_with_assigned_resources_shrink is not None:
            result['FilterWithAssignedResources'] = self.filter_with_assigned_resources_shrink
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.is_query_all_sub_orgs is not None:
            result['IsQueryAllSubOrgs'] = self.is_query_all_sub_orgs
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.show_extras_shrink is not None:
            result['ShowExtras'] = self.show_extras_shrink
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('ExcludeEndUserIds') is not None:
            self.exclude_end_user_ids = m.get('ExcludeEndUserIds')
        if m.get('ExcludeGroupId') is not None:
            self.exclude_group_id = m.get('ExcludeGroupId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('FilterWithAssignedResource') is not None:
            self.filter_with_assigned_resource_shrink = m.get('FilterWithAssignedResource')
        if m.get('FilterWithAssignedResources') is not None:
            self.filter_with_assigned_resources_shrink = m.get('FilterWithAssignedResources')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IsQueryAllSubOrgs') is not None:
            self.is_query_all_sub_orgs = m.get('IsQueryAllSubOrgs')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ShowExtras') is not None:
            self.show_extras_shrink = m.get('ShowExtras')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeUsersResponseBodyUsersExtras(TeaModel):
    def __init__(
        self,
        assigned_resource_count: Dict[str, Any] = None,
    ):
        self.assigned_resource_count = assigned_resource_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assigned_resource_count is not None:
            result['AssignedResourceCount'] = self.assigned_resource_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignedResourceCount') is not None:
            self.assigned_resource_count = m.get('AssignedResourceCount')
        return self


class DescribeUsersResponseBodyUsersGroups(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
    ):
        # The ID of the user group.
        self.group_id = group_id
        # The name of the user group.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeUsersResponseBodyUsersOrgs(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
        org_name_path: str = None,
    ):
        # The organization ID.
        self.org_id = org_id
        # The organization name.
        self.org_name = org_name
        self.org_name_path = org_name_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_name_path is not None:
            result['OrgNamePath'] = self.org_name_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgNamePath') is not None:
            self.org_name_path = m.get('OrgNamePath')
        return self


class DescribeUsersResponseBodyUsersProperties(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        address: str = None,
        avatar: str = None,
        email: str = None,
        enable_admin_access: bool = None,
        end_user_id: str = None,
        external_name: str = None,
        extras: DescribeUsersResponseBodyUsersExtras = None,
        groups: List[DescribeUsersResponseBodyUsersGroups] = None,
        id: int = None,
        is_tenant_manager: bool = None,
        job_number: str = None,
        nick_name: str = None,
        org_id: str = None,
        orgs: List[DescribeUsersResponseBodyUsersOrgs] = None,
        owner_type: str = None,
        phone: str = None,
        properties: List[DescribeUsersResponseBodyUsersProperties] = None,
        real_nick_name: str = None,
        remark: str = None,
        status: int = None,
        wy_id: str = None,
    ):
        # The work address of the convenience user.
        self.address = address
        # The profile picture of the convenience user.
        self.avatar = avatar
        # The email address of the convenience user.
        self.email = email
        self.enable_admin_access = enable_admin_access
        # The username of the convenience user.
        self.end_user_id = end_user_id
        self.external_name = external_name
        self.extras = extras
        # The user groups to which the convenience user belongs.
        self.groups = groups
        # The ID of the convenience user.
        self.id = id
        # Indicates whether the convenience user is an administrator. If the convenience user is of the administrator-activated type, you must specify a user administrator. Notifications such as password reset on a client are sent to the email address or mobile number of the user administrator. For more information, see [Create a convenience user](https://help.aliyun.com/document_detail/214472.html).
        self.is_tenant_manager = is_tenant_manager
        # The employee number of the convenience user.
        self.job_number = job_number
        # The nickname of the convenience user.
        self.nick_name = nick_name
        # The ID of the organization to which the convenience user belongs.
        # 
        # >  This parameter will be deprecated in the future.
        self.org_id = org_id
        # The organizations to which the convenience user belongs.
        self.orgs = orgs
        # The type of the convenience account.
        # 
        # *   Administrator-activated type: The administrator specifies the username and password of the convenience account. User notifications such as password reset notifications are sent to the email address or mobile number of the administrator.
        # *   User-activated type: The administrator specifies the username and the email address or mobile number of a convenience user. Notifications such as activation notifications that contain the default password are sent to the email address or mobile number of the convenience user.
        # 
        # Valid values:
        # 
        # *   CreateFromManager
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     administrator-activated
        # 
        #     <!-- -->
        # 
        # *   Normal
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     user-activated
        # 
        #     <!-- -->
        self.owner_type = owner_type
        # The mobile number of the convenience user. If you leave this parameter empty, the value of this parameter is not returned.
        self.phone = phone
        self.properties = properties
        self.real_nick_name = real_nick_name
        # The remarks on the convenience user.
        self.remark = remark
        # The status of the convenience user.
        # 
        # Valid values:
        # 
        # *   0: The convenience user is normal.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   9: The convenience user is locked.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status
        # The globally unique ID of the convenience user.
        self.wy_id = wy_id

    def validate(self):
        if self.extras:
            self.extras.validate()
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()
        if self.orgs:
            for k in self.orgs:
                if k:
                    k.validate()
        if self.properties:
            for k in self.properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.email is not None:
            result['Email'] = self.email
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.external_name is not None:
            result['ExternalName'] = self.external_name
        if self.extras is not None:
            result['Extras'] = self.extras.to_map()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.is_tenant_manager is not None:
            result['IsTenantManager'] = self.is_tenant_manager
        if self.job_number is not None:
            result['JobNumber'] = self.job_number
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        result['Orgs'] = []
        if self.orgs is not None:
            for k in self.orgs:
                result['Orgs'].append(k.to_map() if k else None)
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.phone is not None:
            result['Phone'] = self.phone
        result['Properties'] = []
        if self.properties is not None:
            for k in self.properties:
                result['Properties'].append(k.to_map() if k else None)
        if self.real_nick_name is not None:
            result['RealNickName'] = self.real_nick_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.wy_id is not None:
            result['WyId'] = self.wy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ExternalName') is not None:
            self.external_name = m.get('ExternalName')
        if m.get('Extras') is not None:
            temp_model = DescribeUsersResponseBodyUsersExtras()
            self.extras = temp_model.from_map(m['Extras'])
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = DescribeUsersResponseBodyUsersGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsTenantManager') is not None:
            self.is_tenant_manager = m.get('IsTenantManager')
        if m.get('JobNumber') is not None:
            self.job_number = m.get('JobNumber')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        self.orgs = []
        if m.get('Orgs') is not None:
            for k in m.get('Orgs'):
                temp_model = DescribeUsersResponseBodyUsersOrgs()
                self.orgs.append(temp_model.from_map(k))
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        self.properties = []
        if m.get('Properties') is not None:
            for k in m.get('Properties'):
                temp_model = DescribeUsersResponseBodyUsersProperties()
                self.properties.append(temp_model.from_map(k))
        if m.get('RealNickName') is not None:
            self.real_nick_name = m.get('RealNickName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')
        return self


class DescribeUsersResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        users: List[DescribeUsersResponseBodyUsers] = None,
    ):
        # The token that determines the start point of the next query. If this parameter is left empty, all results are returned.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The convenience accounts.
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = DescribeUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class DescribeUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUsersResponseBody = None,
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
            temp_model = DescribeUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FilterUsersRequestOrderParam(TeaModel):
    def __init__(
        self,
        order_field: str = None,
        order_type: str = None,
    ):
        # The field that you want to sort by.
        # 
        # Valid values:
        # 
        # *   EndUserId: the username.
        # *   id: the ID of the primary key.
        # *   gmt_created: the creation time.
        self.order_field = order_field
        # The direction of the sort.
        # 
        # Valid values:
        # 
        # *   ASC: the ascending order.
        # *   DESC (default): the descending order.
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class FilterUsersRequestPropertyFilterParam(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_value_ids: str = None,
    ):
        # The ID of the property.
        self.property_id = property_id
        # The IDs of the property values.
        self.property_value_ids = property_value_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value_ids is not None:
            result['PropertyValueIds'] = self.property_value_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValueIds') is not None:
            self.property_value_ids = m.get('PropertyValueIds')
        return self


class FilterUsersRequestPropertyKeyValueFilterParam(TeaModel):
    def __init__(
        self,
        property_key: str = None,
        property_values: str = None,
    ):
        # The property name.
        self.property_key = property_key
        # The property values.
        self.property_values = property_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_values is not None:
            result['PropertyValues'] = self.property_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyValues') is not None:
            self.property_values = m.get('PropertyValues')
        return self


class FilterUsersRequest(TeaModel):
    def __init__(
        self,
        exclude_end_user_ids: List[str] = None,
        filter: str = None,
        include_desktop_count: bool = None,
        include_desktop_group_count: bool = None,
        include_org_info: bool = None,
        include_support_idps: bool = None,
        is_query_all_sub_orgs: bool = None,
        max_results: int = None,
        next_token: str = None,
        order_param: FilterUsersRequestOrderParam = None,
        org_id: str = None,
        owner_type: str = None,
        property_filter_param: List[FilterUsersRequestPropertyFilterParam] = None,
        property_key_value_filter_param: List[FilterUsersRequestPropertyKeyValueFilterParam] = None,
        status: int = None,
    ):
        # The list of usernames to be precisely excluded.
        self.exclude_end_user_ids = exclude_end_user_ids
        # The string that is used for fuzzy search. You can use usernames and email addresses to perform fuzzy search. Wildcard characters (\\*) are supported for this parameter. For example, if you set this parameter to a\\*m, the usernames or an email addresses that start with a or end with m are returned.
        self.filter = filter
        # Specifies whether to return the number of cloud desktops that are assigned to the convenience user.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.include_desktop_count = include_desktop_count
        # Specifies whether to return the number of cloud desktop pools that are assigned to the convenience user.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.include_desktop_group_count = include_desktop_group_count
        self.include_org_info = include_org_info
        self.include_support_idps = include_support_idps
        self.is_query_all_sub_orgs = is_query_all_sub_orgs
        # The number of entries per page. If you set this parameter to a value greater than 100, the system resets the value to 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. If not all results are returned in a query, a value is returned for the NextToken parameter. In this case, you can use the returned NextToken value to start the next query.
        self.next_token = next_token
        # The parameter that might affect the sorting logic.
        self.order_param = order_param
        # The ID of the organization.
        self.org_id = org_id
        # The activation type of the convenience account.
        # 
        # Valid values:
        # 
        # *   CreateFromManager: administrator-activated.
        # *   Normal: user-activated.
        self.owner_type = owner_type
        # The list of properties for fuzzy search.
        self.property_filter_param = property_filter_param
        # The list of property names and property values.
        self.property_key_value_filter_param = property_key_value_filter_param
        self.status = status

    def validate(self):
        if self.order_param:
            self.order_param.validate()
        if self.property_filter_param:
            for k in self.property_filter_param:
                if k:
                    k.validate()
        if self.property_key_value_filter_param:
            for k in self.property_key_value_filter_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_end_user_ids is not None:
            result['ExcludeEndUserIds'] = self.exclude_end_user_ids
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.include_desktop_count is not None:
            result['IncludeDesktopCount'] = self.include_desktop_count
        if self.include_desktop_group_count is not None:
            result['IncludeDesktopGroupCount'] = self.include_desktop_group_count
        if self.include_org_info is not None:
            result['IncludeOrgInfo'] = self.include_org_info
        if self.include_support_idps is not None:
            result['IncludeSupportIdps'] = self.include_support_idps
        if self.is_query_all_sub_orgs is not None:
            result['IsQueryAllSubOrgs'] = self.is_query_all_sub_orgs
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_param is not None:
            result['OrderParam'] = self.order_param.to_map()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        result['PropertyFilterParam'] = []
        if self.property_filter_param is not None:
            for k in self.property_filter_param:
                result['PropertyFilterParam'].append(k.to_map() if k else None)
        result['PropertyKeyValueFilterParam'] = []
        if self.property_key_value_filter_param is not None:
            for k in self.property_key_value_filter_param:
                result['PropertyKeyValueFilterParam'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeEndUserIds') is not None:
            self.exclude_end_user_ids = m.get('ExcludeEndUserIds')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('IncludeDesktopCount') is not None:
            self.include_desktop_count = m.get('IncludeDesktopCount')
        if m.get('IncludeDesktopGroupCount') is not None:
            self.include_desktop_group_count = m.get('IncludeDesktopGroupCount')
        if m.get('IncludeOrgInfo') is not None:
            self.include_org_info = m.get('IncludeOrgInfo')
        if m.get('IncludeSupportIdps') is not None:
            self.include_support_idps = m.get('IncludeSupportIdps')
        if m.get('IsQueryAllSubOrgs') is not None:
            self.is_query_all_sub_orgs = m.get('IsQueryAllSubOrgs')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderParam') is not None:
            temp_model = FilterUsersRequestOrderParam()
            self.order_param = temp_model.from_map(m['OrderParam'])
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        self.property_filter_param = []
        if m.get('PropertyFilterParam') is not None:
            for k in m.get('PropertyFilterParam'):
                temp_model = FilterUsersRequestPropertyFilterParam()
                self.property_filter_param.append(temp_model.from_map(k))
        self.property_key_value_filter_param = []
        if m.get('PropertyKeyValueFilterParam') is not None:
            for k in m.get('PropertyKeyValueFilterParam'):
                temp_model = FilterUsersRequestPropertyKeyValueFilterParam()
                self.property_key_value_filter_param.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class FilterUsersShrinkRequestPropertyFilterParam(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_value_ids: str = None,
    ):
        # The ID of the property.
        self.property_id = property_id
        # The IDs of the property values.
        self.property_value_ids = property_value_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value_ids is not None:
            result['PropertyValueIds'] = self.property_value_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValueIds') is not None:
            self.property_value_ids = m.get('PropertyValueIds')
        return self


class FilterUsersShrinkRequestPropertyKeyValueFilterParam(TeaModel):
    def __init__(
        self,
        property_key: str = None,
        property_values: str = None,
    ):
        # The property name.
        self.property_key = property_key
        # The property values.
        self.property_values = property_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_values is not None:
            result['PropertyValues'] = self.property_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyValues') is not None:
            self.property_values = m.get('PropertyValues')
        return self


class FilterUsersShrinkRequest(TeaModel):
    def __init__(
        self,
        exclude_end_user_ids: List[str] = None,
        filter: str = None,
        include_desktop_count: bool = None,
        include_desktop_group_count: bool = None,
        include_org_info: bool = None,
        include_support_idps: bool = None,
        is_query_all_sub_orgs: bool = None,
        max_results: int = None,
        next_token: str = None,
        order_param_shrink: str = None,
        org_id: str = None,
        owner_type: str = None,
        property_filter_param: List[FilterUsersShrinkRequestPropertyFilterParam] = None,
        property_key_value_filter_param: List[FilterUsersShrinkRequestPropertyKeyValueFilterParam] = None,
        status: int = None,
    ):
        # The list of usernames to be precisely excluded.
        self.exclude_end_user_ids = exclude_end_user_ids
        # The string that is used for fuzzy search. You can use usernames and email addresses to perform fuzzy search. Wildcard characters (\\*) are supported for this parameter. For example, if you set this parameter to a\\*m, the usernames or an email addresses that start with a or end with m are returned.
        self.filter = filter
        # Specifies whether to return the number of cloud desktops that are assigned to the convenience user.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.include_desktop_count = include_desktop_count
        # Specifies whether to return the number of cloud desktop pools that are assigned to the convenience user.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.include_desktop_group_count = include_desktop_group_count
        self.include_org_info = include_org_info
        self.include_support_idps = include_support_idps
        self.is_query_all_sub_orgs = is_query_all_sub_orgs
        # The number of entries per page. If you set this parameter to a value greater than 100, the system resets the value to 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. If not all results are returned in a query, a value is returned for the NextToken parameter. In this case, you can use the returned NextToken value to start the next query.
        self.next_token = next_token
        # The parameter that might affect the sorting logic.
        self.order_param_shrink = order_param_shrink
        # The ID of the organization.
        self.org_id = org_id
        # The activation type of the convenience account.
        # 
        # Valid values:
        # 
        # *   CreateFromManager: administrator-activated.
        # *   Normal: user-activated.
        self.owner_type = owner_type
        # The list of properties for fuzzy search.
        self.property_filter_param = property_filter_param
        # The list of property names and property values.
        self.property_key_value_filter_param = property_key_value_filter_param
        self.status = status

    def validate(self):
        if self.property_filter_param:
            for k in self.property_filter_param:
                if k:
                    k.validate()
        if self.property_key_value_filter_param:
            for k in self.property_key_value_filter_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_end_user_ids is not None:
            result['ExcludeEndUserIds'] = self.exclude_end_user_ids
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.include_desktop_count is not None:
            result['IncludeDesktopCount'] = self.include_desktop_count
        if self.include_desktop_group_count is not None:
            result['IncludeDesktopGroupCount'] = self.include_desktop_group_count
        if self.include_org_info is not None:
            result['IncludeOrgInfo'] = self.include_org_info
        if self.include_support_idps is not None:
            result['IncludeSupportIdps'] = self.include_support_idps
        if self.is_query_all_sub_orgs is not None:
            result['IsQueryAllSubOrgs'] = self.is_query_all_sub_orgs
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_param_shrink is not None:
            result['OrderParam'] = self.order_param_shrink
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        result['PropertyFilterParam'] = []
        if self.property_filter_param is not None:
            for k in self.property_filter_param:
                result['PropertyFilterParam'].append(k.to_map() if k else None)
        result['PropertyKeyValueFilterParam'] = []
        if self.property_key_value_filter_param is not None:
            for k in self.property_key_value_filter_param:
                result['PropertyKeyValueFilterParam'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeEndUserIds') is not None:
            self.exclude_end_user_ids = m.get('ExcludeEndUserIds')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('IncludeDesktopCount') is not None:
            self.include_desktop_count = m.get('IncludeDesktopCount')
        if m.get('IncludeDesktopGroupCount') is not None:
            self.include_desktop_group_count = m.get('IncludeDesktopGroupCount')
        if m.get('IncludeOrgInfo') is not None:
            self.include_org_info = m.get('IncludeOrgInfo')
        if m.get('IncludeSupportIdps') is not None:
            self.include_support_idps = m.get('IncludeSupportIdps')
        if m.get('IsQueryAllSubOrgs') is not None:
            self.is_query_all_sub_orgs = m.get('IsQueryAllSubOrgs')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderParam') is not None:
            self.order_param_shrink = m.get('OrderParam')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        self.property_filter_param = []
        if m.get('PropertyFilterParam') is not None:
            for k in m.get('PropertyFilterParam'):
                temp_model = FilterUsersShrinkRequestPropertyFilterParam()
                self.property_filter_param.append(temp_model.from_map(k))
        self.property_key_value_filter_param = []
        if m.get('PropertyKeyValueFilterParam') is not None:
            for k in m.get('PropertyKeyValueFilterParam'):
                temp_model = FilterUsersShrinkRequestPropertyKeyValueFilterParam()
                self.property_key_value_filter_param.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class FilterUsersResponseBodyUsersExternalInfo(TeaModel):
    def __init__(
        self,
        external_name: str = None,
        job_number: str = None,
    ):
        # The account that is associated with the convenience user.
        self.external_name = external_name
        # The account, student ID, or employee ID that is associated with the convenience user.
        self.job_number = job_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_name is not None:
            result['ExternalName'] = self.external_name
        if self.job_number is not None:
            result['JobNumber'] = self.job_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalName') is not None:
            self.external_name = m.get('ExternalName')
        if m.get('JobNumber') is not None:
            self.job_number = m.get('JobNumber')
        return self


class FilterUsersResponseBodyUsersOrgList(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
        org_name_path: str = None,
    ):
        self.org_id = org_id
        self.org_name = org_name
        self.org_name_path = org_name_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_name_path is not None:
            result['OrgNamePath'] = self.org_name_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgNamePath') is not None:
            self.org_name_path = m.get('OrgNamePath')
        return self


class FilterUsersResponseBodyUsersSupportLoginIdps(TeaModel):
    def __init__(
        self,
        idp_id: str = None,
        idp_name: str = None,
    ):
        self.idp_id = idp_id
        self.idp_name = idp_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.idp_name is not None:
            result['IdpName'] = self.idp_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('IdpName') is not None:
            self.idp_name = m.get('IdpName')
        return self


class FilterUsersResponseBodyUsersUserSetPropertiesModelsPropertyValues(TeaModel):
    def __init__(
        self,
        property_value: str = None,
        property_value_id: int = None,
    ):
        # The property value.
        self.property_value = property_value
        # The ID of the property value.
        self.property_value_id = property_value_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class FilterUsersResponseBodyUsersUserSetPropertiesModels(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_key: str = None,
        property_type: int = None,
        property_values: List[FilterUsersResponseBodyUsersUserSetPropertiesModelsPropertyValues] = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # The property ID.
        self.property_id = property_id
        # The property name.
        self.property_key = property_key
        # The property type.
        self.property_type = property_type
        # The property values.
        self.property_values = property_values
        # The ID of the convenience user that is bound to the property.
        self.user_id = user_id
        # The username of the convenience user that is bound to the property.
        self.user_name = user_name

    def validate(self):
        if self.property_values:
            for k in self.property_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_type is not None:
            result['PropertyType'] = self.property_type
        result['PropertyValues'] = []
        if self.property_values is not None:
            for k in self.property_values:
                result['PropertyValues'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyType') is not None:
            self.property_type = m.get('PropertyType')
        self.property_values = []
        if m.get('PropertyValues') is not None:
            for k in m.get('PropertyValues'):
                temp_model = FilterUsersResponseBodyUsersUserSetPropertiesModelsPropertyValues()
                self.property_values.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class FilterUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        auto_lock_time: str = None,
        desktop_count: int = None,
        desktop_group_count: int = None,
        email: str = None,
        enable_admin_access: bool = None,
        end_user_id: str = None,
        external_info: FilterUsersResponseBodyUsersExternalInfo = None,
        id: int = None,
        is_tenant_manager: bool = None,
        org_list: List[FilterUsersResponseBodyUsersOrgList] = None,
        owner_type: str = None,
        password_expire_days: int = None,
        password_expire_rest_days: int = None,
        phone: str = None,
        real_nick_name: str = None,
        remark: str = None,
        status: int = None,
        support_login_idps: List[FilterUsersResponseBodyUsersSupportLoginIdps] = None,
        user_set_properties_models: List[FilterUsersResponseBodyUsersUserSetPropertiesModels] = None,
    ):
        # The date when a convenience account is automatically locked.
        self.auto_lock_time = auto_lock_time
        # The number of cloud desktops that are assigned to the convenience user.
        self.desktop_count = desktop_count
        # The number of cloud desktop pools that are assigned to the convenience user. This value is returned if you set `IncludeDesktopGroupCount` to `true`.
        self.desktop_group_count = desktop_group_count
        # The email address of the convenience user.
        self.email = email
        # Indicates whether the convenience user is a local administrator.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enable_admin_access = enable_admin_access
        # The username of the convenience user.
        self.end_user_id = end_user_id
        # The additional information about the convenience user.
        self.external_info = external_info
        # The ID of the convenience user.
        self.id = id
        # Indicates whether the convenience user is a tenant administrator.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.is_tenant_manager = is_tenant_manager
        self.org_list = org_list
        # The type of the account ownership.
        # 
        # Valid values:
        # 
        # *   CreateFromManager: administrator-activated
        # *   Normal: user-activated
        self.owner_type = owner_type
        # By default, user account passwords do not expire. However, you can set a validity period between 30 and 365 days. Once the period expires, end users must change their password before they can log on to terminals.
        # 
        # >  The feature is in invitational preview. If you want to use this feature, submit a ticket.
        self.password_expire_days = password_expire_days
        # The number of days remaining until the account password expires.
        self.password_expire_rest_days = password_expire_rest_days
        # The mobile number of the convenience user.
        self.phone = phone
        # The nickname of the convenience user.
        self.real_nick_name = real_nick_name
        # The remarks on the convenience user.
        self.remark = remark
        # The remarks on the convenience account.
        # 
        # Valid values:
        # 
        # *   0: The convenience account is normal.
        # *   9: The convenience account is locked.
        self.status = status
        self.support_login_idps = support_login_idps
        # The information about the properties.
        self.user_set_properties_models = user_set_properties_models

    def validate(self):
        if self.external_info:
            self.external_info.validate()
        if self.org_list:
            for k in self.org_list:
                if k:
                    k.validate()
        if self.support_login_idps:
            for k in self.support_login_idps:
                if k:
                    k.validate()
        if self.user_set_properties_models:
            for k in self.user_set_properties_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_lock_time is not None:
            result['AutoLockTime'] = self.auto_lock_time
        if self.desktop_count is not None:
            result['DesktopCount'] = self.desktop_count
        if self.desktop_group_count is not None:
            result['DesktopGroupCount'] = self.desktop_group_count
        if self.email is not None:
            result['Email'] = self.email
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.external_info is not None:
            result['ExternalInfo'] = self.external_info.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_tenant_manager is not None:
            result['IsTenantManager'] = self.is_tenant_manager
        result['OrgList'] = []
        if self.org_list is not None:
            for k in self.org_list:
                result['OrgList'].append(k.to_map() if k else None)
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.password_expire_days is not None:
            result['PasswordExpireDays'] = self.password_expire_days
        if self.password_expire_rest_days is not None:
            result['PasswordExpireRestDays'] = self.password_expire_rest_days
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.real_nick_name is not None:
            result['RealNickName'] = self.real_nick_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        result['SupportLoginIdps'] = []
        if self.support_login_idps is not None:
            for k in self.support_login_idps:
                result['SupportLoginIdps'].append(k.to_map() if k else None)
        result['UserSetPropertiesModels'] = []
        if self.user_set_properties_models is not None:
            for k in self.user_set_properties_models:
                result['UserSetPropertiesModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoLockTime') is not None:
            self.auto_lock_time = m.get('AutoLockTime')
        if m.get('DesktopCount') is not None:
            self.desktop_count = m.get('DesktopCount')
        if m.get('DesktopGroupCount') is not None:
            self.desktop_group_count = m.get('DesktopGroupCount')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ExternalInfo') is not None:
            temp_model = FilterUsersResponseBodyUsersExternalInfo()
            self.external_info = temp_model.from_map(m['ExternalInfo'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsTenantManager') is not None:
            self.is_tenant_manager = m.get('IsTenantManager')
        self.org_list = []
        if m.get('OrgList') is not None:
            for k in m.get('OrgList'):
                temp_model = FilterUsersResponseBodyUsersOrgList()
                self.org_list.append(temp_model.from_map(k))
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('PasswordExpireDays') is not None:
            self.password_expire_days = m.get('PasswordExpireDays')
        if m.get('PasswordExpireRestDays') is not None:
            self.password_expire_rest_days = m.get('PasswordExpireRestDays')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RealNickName') is not None:
            self.real_nick_name = m.get('RealNickName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.support_login_idps = []
        if m.get('SupportLoginIdps') is not None:
            for k in m.get('SupportLoginIdps'):
                temp_model = FilterUsersResponseBodyUsersSupportLoginIdps()
                self.support_login_idps.append(temp_model.from_map(k))
        self.user_set_properties_models = []
        if m.get('UserSetPropertiesModels') is not None:
            for k in m.get('UserSetPropertiesModels'):
                temp_model = FilterUsersResponseBodyUsersUserSetPropertiesModels()
                self.user_set_properties_models.append(temp_model.from_map(k))
        return self


class FilterUsersResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        users: List[FilterUsersResponseBodyUsers] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. If not all results are returned in a query, a value is returned for the NextToken parameter. In this case, you can use the returned NextToken value to start the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The convenience accounts.
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = FilterUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class FilterUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FilterUsersResponseBody = None,
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
            temp_model = FilterUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetManagerInfoByAuthCodeRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
    ):
        # The authorization code.
        # 
        # This parameter is required.
        self.auth_code = auth_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        return self


class GetManagerInfoByAuthCodeResponseBody(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        phone: str = None,
        request_id: str = None,
        team_name: str = None,
        user_name: str = None,
        wa_id: int = None,
    ):
        # The organization ID.
        self.org_id = org_id
        # The mobile number.
        self.phone = phone
        # The request ID.
        self.request_id = request_id
        # The team name.
        self.team_name = team_name
        # The tenant name.
        self.user_name = user_name
        # The ID of the Elastic Desktop Service account.
        self.wa_id = wa_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.team_name is not None:
            result['TeamName'] = self.team_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.wa_id is not None:
            result['WaId'] = self.wa_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TeamName') is not None:
            self.team_name = m.get('TeamName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('WaId') is not None:
            self.wa_id = m.get('WaId')
        return self


class GetManagerInfoByAuthCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetManagerInfoByAuthCodeResponseBody = None,
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
            temp_model = GetManagerInfoByAuthCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitTenantAliasResponseBodyAliasInfo(TeaModel):
    def __init__(
        self,
        alias_edit_disabled_reason: str = None,
        alias_editable: bool = None,
        alias_source_type: str = None,
        next_modify_time: str = None,
    ):
        self.alias_edit_disabled_reason = alias_edit_disabled_reason
        self.alias_editable = alias_editable
        self.alias_source_type = alias_source_type
        self.next_modify_time = next_modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_edit_disabled_reason is not None:
            result['AliasEditDisabledReason'] = self.alias_edit_disabled_reason
        if self.alias_editable is not None:
            result['AliasEditable'] = self.alias_editable
        if self.alias_source_type is not None:
            result['AliasSourceType'] = self.alias_source_type
        if self.next_modify_time is not None:
            result['NextModifyTime'] = self.next_modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasEditDisabledReason') is not None:
            self.alias_edit_disabled_reason = m.get('AliasEditDisabledReason')
        if m.get('AliasEditable') is not None:
            self.alias_editable = m.get('AliasEditable')
        if m.get('AliasSourceType') is not None:
            self.alias_source_type = m.get('AliasSourceType')
        if m.get('NextModifyTime') is not None:
            self.next_modify_time = m.get('NextModifyTime')
        return self


class InitTenantAliasResponseBody(TeaModel):
    def __init__(
        self,
        alias_info: InitTenantAliasResponseBodyAliasInfo = None,
        data: str = None,
        request_id: str = None,
    ):
        self.alias_info = alias_info
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.alias_info:
            self.alias_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_info is not None:
            result['AliasInfo'] = self.alias_info.to_map()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasInfo') is not None:
            temp_model = InitTenantAliasResponseBodyAliasInfo()
            self.alias_info = temp_model.from_map(m['AliasInfo'])
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InitTenantAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitTenantAliasResponseBody = None,
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
            temp_model = InitTenantAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPropertyResponseBodyPropertiesPropertyValues(TeaModel):
    def __init__(
        self,
        property_value: str = None,
        property_value_id: int = None,
    ):
        # The value of the property.
        self.property_value = property_value
        # The ID of the property value.
        self.property_value_id = property_value_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class ListPropertyResponseBodyProperties(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_key: str = None,
        property_values: List[ListPropertyResponseBodyPropertiesPropertyValues] = None,
    ):
        # The ID of the property.
        self.property_id = property_id
        # The name of the property.
        self.property_key = property_key
        # Details about the property values.
        self.property_values = property_values

    def validate(self):
        if self.property_values:
            for k in self.property_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        result['PropertyValues'] = []
        if self.property_values is not None:
            for k in self.property_values:
                result['PropertyValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        self.property_values = []
        if m.get('PropertyValues') is not None:
            for k in m.get('PropertyValues'):
                temp_model = ListPropertyResponseBodyPropertiesPropertyValues()
                self.property_values.append(temp_model.from_map(k))
        return self


class ListPropertyResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        properties: List[ListPropertyResponseBodyProperties] = None,
        request_id: str = None,
    ):
        # The token that is used for the next query. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The information about the properties.
        self.properties = properties
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.properties:
            for k in self.properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Properties'] = []
        if self.properties is not None:
            for k in self.properties:
                result['Properties'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.properties = []
        if m.get('Properties') is not None:
            for k in m.get('Properties'):
                temp_model = ListPropertyResponseBodyProperties()
                self.properties.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPropertyResponseBody = None,
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
            temp_model = ListPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPropertyValueRequest(TeaModel):
    def __init__(
        self,
        property_id: int = None,
    ):
        # The ID of the property. You can call the [ListProperty](https://help.aliyun.com/document_detail/410890.html) operation to query the property ID.
        # 
        # This parameter is required.
        self.property_id = property_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        return self


class ListPropertyValueResponseBodyPropertyValueInfos(TeaModel):
    def __init__(
        self,
        property_value: str = None,
        property_value_id: int = None,
    ):
        # The value of the property.
        self.property_value = property_value
        # The ID of the property value.
        self.property_value_id = property_value_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class ListPropertyValueResponseBody(TeaModel):
    def __init__(
        self,
        property_value_infos: List[ListPropertyValueResponseBodyPropertyValueInfos] = None,
        request_id: str = None,
    ):
        # Details about property values.
        self.property_value_infos = property_value_infos
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.property_value_infos:
            for k in self.property_value_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PropertyValueInfos'] = []
        if self.property_value_infos is not None:
            for k in self.property_value_infos:
                result['PropertyValueInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property_value_infos = []
        if m.get('PropertyValueInfos') is not None:
            for k in m.get('PropertyValueInfos'):
                temp_model = ListPropertyValueResponseBodyPropertyValueInfos()
                self.property_value_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPropertyValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPropertyValueResponseBody = None,
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
            temp_model = ListPropertyValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockMfaDeviceRequest(TeaModel):
    def __init__(
        self,
        ad_domain: str = None,
        serial_number: str = None,
    ):
        # The domain of the Active Directory (AD) workspace.
        self.ad_domain = ad_domain
        # The serial number of the virtual MFA device. The serial number is unique for each device.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class LockMfaDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class LockMfaDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LockMfaDeviceResponseBody = None,
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
            temp_model = LockMfaDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockUsersRequest(TeaModel):
    def __init__(
        self,
        logout_session: bool = None,
        users: List[str] = None,
    ):
        self.logout_session = logout_session
        # The usernames of the convenience users that you want to lock.
        # 
        # This parameter is required.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logout_session is not None:
            result['LogoutSession'] = self.logout_session
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogoutSession') is not None:
            self.logout_session = m.get('LogoutSession')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class LockUsersResponseBodyLockUsersResultFailedUsers(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        # The ID of the convenience user that failed to be locked.
        self.end_user_id = end_user_id
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class LockUsersResponseBodyLockUsersResult(TeaModel):
    def __init__(
        self,
        failed_users: List[LockUsersResponseBodyLockUsersResultFailedUsers] = None,
        locked_users: List[str] = None,
    ):
        # The convenience users that failed to be locked.
        self.failed_users = failed_users
        # The convenience users that were locked.
        self.locked_users = locked_users

    def validate(self):
        if self.failed_users:
            for k in self.failed_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedUsers'] = []
        if self.failed_users is not None:
            for k in self.failed_users:
                result['FailedUsers'].append(k.to_map() if k else None)
        if self.locked_users is not None:
            result['LockedUsers'] = self.locked_users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_users = []
        if m.get('FailedUsers') is not None:
            for k in m.get('FailedUsers'):
                temp_model = LockUsersResponseBodyLockUsersResultFailedUsers()
                self.failed_users.append(temp_model.from_map(k))
        if m.get('LockedUsers') is not None:
            self.locked_users = m.get('LockedUsers')
        return self


class LockUsersResponseBody(TeaModel):
    def __init__(
        self,
        lock_users_result: LockUsersResponseBodyLockUsersResult = None,
        request_id: str = None,
    ):
        # The result of the locking the convenience user.
        self.lock_users_result = lock_users_result
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.lock_users_result:
            self.lock_users_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_users_result is not None:
            result['LockUsersResult'] = self.lock_users_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockUsersResult') is not None:
            temp_model = LockUsersResponseBodyLockUsersResult()
            self.lock_users_result = temp_model.from_map(m['LockUsersResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LockUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LockUsersResponseBody = None,
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
            temp_model = LockUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGroupRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        new_group_name: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.group_id = group_id
        # This parameter is required.
        self.new_group_name = new_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.new_group_name is not None:
            result['NewGroupName'] = self.new_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NewGroupName') is not None:
            self.new_group_name = m.get('NewGroupName')
        return self


class ModifyGroupResponseBody(TeaModel):
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


class ModifyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyGroupResponseBody = None,
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
            temp_model = ModifyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOrgRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
    ):
        # This parameter is required.
        self.org_id = org_id
        # This parameter is required.
        self.org_name = org_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        return self


class ModifyOrgResponseBody(TeaModel):
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


class ModifyOrgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyOrgResponseBody = None,
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
            temp_model = ModifyOrgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserRequest(TeaModel):
    def __init__(
        self,
        email: str = None,
        end_user_id: str = None,
        phone: str = None,
    ):
        # The email address of the convenience user. For a user-activated convenience user, the email address or mobile number must be verified. You can choose to verify the email address or the mobile number. For an administrator-activated convenience user, the email address and mobile number can be left empty.
        self.email = email
        # The name of the user.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The mobile number of the convenience user. For a user-activated convenience user, the email address or mobile number must be verified. You can choose to verify the email address or the mobile number. For an administrator-activated convenience user, the email address and mobile number can be left empty.
        # 
        # >  Accounts created on the International site (alibabacloud.com) do not support mobile number-based authentication.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class ModifyUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyUserResponseBody = None,
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
            temp_model = ModifyUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveOrgRequest(TeaModel):
    def __init__(
        self,
        new_parent_org_id: str = None,
        org_id: str = None,
    ):
        # This parameter is required.
        self.new_parent_org_id = new_parent_org_id
        # This parameter is required.
        self.org_id = org_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_parent_org_id is not None:
            result['NewParentOrgId'] = self.new_parent_org_id
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewParentOrgId') is not None:
            self.new_parent_org_id = m.get('NewParentOrgId')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class MoveOrgResponseBody(TeaModel):
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


class MoveOrgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveOrgResponseBody = None,
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
            temp_model = MoveOrgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveUserOrgRequest(TeaModel):
    def __init__(
        self,
        end_user_ids: List[str] = None,
        org_id: str = None,
    ):
        # This parameter is required.
        self.end_user_ids = end_user_ids
        # This parameter is required.
        self.org_id = org_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class MoveUserOrgResponseBody(TeaModel):
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


class MoveUserOrgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveUserOrgResponseBody = None,
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
            temp_model = MoveUserOrgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySyncStatusByAliUidResponseBodyData(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        corp_id: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        latest_begin_time: str = None,
        latest_end_time: str = None,
        latest_success_time: str = None,
        status: str = None,
    ):
        self.ali_uid = ali_uid
        self.corp_id = corp_id
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.id = id
        self.latest_begin_time = latest_begin_time
        self.latest_end_time = latest_end_time
        self.latest_success_time = latest_success_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.latest_begin_time is not None:
            result['LatestBeginTime'] = self.latest_begin_time
        if self.latest_end_time is not None:
            result['LatestEndTime'] = self.latest_end_time
        if self.latest_success_time is not None:
            result['LatestSuccessTime'] = self.latest_success_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LatestBeginTime') is not None:
            self.latest_begin_time = m.get('LatestBeginTime')
        if m.get('LatestEndTime') is not None:
            self.latest_end_time = m.get('LatestEndTime')
        if m.get('LatestSuccessTime') is not None:
            self.latest_success_time = m.get('LatestSuccessTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QuerySyncStatusByAliUidResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QuerySyncStatusByAliUidResponseBodyData = None,
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
            temp_model = QuerySyncStatusByAliUidResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySyncStatusByAliUidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySyncStatusByAliUidResponseBody = None,
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
            temp_model = QuerySyncStatusByAliUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_ids: List[str] = None,
    ):
        self.group_id = group_id
        self.group_ids = group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        return self


class RemoveGroupResponseBody(TeaModel):
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


class RemoveGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveGroupResponseBody = None,
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
            temp_model = RemoveGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveMfaDeviceRequest(TeaModel):
    def __init__(
        self,
        ad_domain: str = None,
        serial_number: str = None,
    ):
        # The domain of the Active Directory (AD) workspace.
        self.ad_domain = ad_domain
        # The serial number of the virtual MFA device. The serial number is unique for each device.
        # 
        # This parameter is required.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class RemoveMfaDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class RemoveMfaDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveMfaDeviceResponseBody = None,
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
            temp_model = RemoveMfaDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveOrgRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
    ):
        # This parameter is required.
        self.org_id = org_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class RemoveOrgResponseBody(TeaModel):
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


class RemoveOrgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveOrgResponseBody = None,
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
            temp_model = RemoveOrgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemovePropertyRequest(TeaModel):
    def __init__(
        self,
        property_id: int = None,
    ):
        # The ID of the property. You can call the [ListProperty](https://help.aliyun.com/document_detail/410890.html) operation to query the property ID.
        # 
        # This parameter is required.
        self.property_id = property_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        return self


class RemovePropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class RemovePropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemovePropertyResponseBody = None,
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
            temp_model = RemovePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUsersRequest(TeaModel):
    def __init__(
        self,
        users: List[str] = None,
    ):
        # The usernames of the convenience users that you want to remove.
        # 
        # This parameter is required.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class RemoveUsersResponseBodyRemoveUsersResultFailedUsers(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        # The ID of the convenience user that failed to be removed.
        self.end_user_id = end_user_id
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class RemoveUsersResponseBodyRemoveUsersResult(TeaModel):
    def __init__(
        self,
        failed_users: List[RemoveUsersResponseBodyRemoveUsersResultFailedUsers] = None,
        removed_users: List[str] = None,
    ):
        # The convenience users that failed to be removed.
        self.failed_users = failed_users
        # The convenience users that were removed.
        self.removed_users = removed_users

    def validate(self):
        if self.failed_users:
            for k in self.failed_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedUsers'] = []
        if self.failed_users is not None:
            for k in self.failed_users:
                result['FailedUsers'].append(k.to_map() if k else None)
        if self.removed_users is not None:
            result['RemovedUsers'] = self.removed_users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_users = []
        if m.get('FailedUsers') is not None:
            for k in m.get('FailedUsers'):
                temp_model = RemoveUsersResponseBodyRemoveUsersResultFailedUsers()
                self.failed_users.append(temp_model.from_map(k))
        if m.get('RemovedUsers') is not None:
            self.removed_users = m.get('RemovedUsers')
        return self


class RemoveUsersResponseBody(TeaModel):
    def __init__(
        self,
        remove_users_result: RemoveUsersResponseBodyRemoveUsersResult = None,
        request_id: str = None,
    ):
        # The result of removing the convenience user.
        self.remove_users_result = remove_users_result
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.remove_users_result:
            self.remove_users_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remove_users_result is not None:
            result['RemoveUsersResult'] = self.remove_users_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemoveUsersResult') is not None:
            temp_model = RemoveUsersResponseBodyRemoveUsersResult()
            self.remove_users_result = temp_model.from_map(m['RemoveUsersResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveUsersResponseBody = None,
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
            temp_model = RemoveUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetUserPasswordRequest(TeaModel):
    def __init__(
        self,
        notify_type: int = None,
        users: List[str] = None,
    ):
        # The method to notify the user after the password is reset.
        # 
        # > Alibaba Cloud accounts of the international site do not support sending notification through text messages.
        self.notify_type = notify_type
        # The names of the convenience users whose passwords you want to reset.
        # 
        # This parameter is required.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ResetUserPasswordResponseBodyResetUsersResultFailedUsers(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        # The ID of the convenience user whose password failed to be reset.
        self.end_user_id = end_user_id
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class ResetUserPasswordResponseBodyResetUsersResult(TeaModel):
    def __init__(
        self,
        failed_users: List[ResetUserPasswordResponseBodyResetUsersResultFailedUsers] = None,
        reset_users: List[str] = None,
    ):
        # The information about the convenience users whose passwords failed to be reset.
        self.failed_users = failed_users
        # The convenience users to which the system sent a password reset email.
        self.reset_users = reset_users

    def validate(self):
        if self.failed_users:
            for k in self.failed_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedUsers'] = []
        if self.failed_users is not None:
            for k in self.failed_users:
                result['FailedUsers'].append(k.to_map() if k else None)
        if self.reset_users is not None:
            result['ResetUsers'] = self.reset_users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_users = []
        if m.get('FailedUsers') is not None:
            for k in m.get('FailedUsers'):
                temp_model = ResetUserPasswordResponseBodyResetUsersResultFailedUsers()
                self.failed_users.append(temp_model.from_map(k))
        if m.get('ResetUsers') is not None:
            self.reset_users = m.get('ResetUsers')
        return self


class ResetUserPasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        reset_users_result: ResetUserPasswordResponseBodyResetUsersResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of resetting the password of the convenience user.
        self.reset_users_result = reset_users_result

    def validate(self):
        if self.reset_users_result:
            self.reset_users_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reset_users_result is not None:
            result['ResetUsersResult'] = self.reset_users_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResetUsersResult') is not None:
            temp_model = ResetUserPasswordResponseBodyResetUsersResult()
            self.reset_users_result = temp_model.from_map(m['ResetUsersResult'])
        return self


class ResetUserPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetUserPasswordResponseBody = None,
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
            temp_model = ResetUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserPropertyValueRequest(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_value_id: int = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # The property ID. You can call the [ListProperty](~~ListProperty~~) operation to query the property ID.
        # 
        # This parameter is required.
        self.property_id = property_id
        # The ID of the property value. You can call the [ListProperty](~~ListProperty~~) operation to query the ID of the property value.
        # 
        # This parameter is required.
        self.property_value_id = property_value_id
        # The ID of the convenience user. You can call the [DescribeUsers](~~DescribeUsers~~) operation to query the user ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The username of the convenience user.
        # 
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class SetUserPropertyValueResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class SetUserPropertyValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetUserPropertyValueResponseBody = None,
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
            temp_model = SetUserPropertyValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncAllEduInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncAllEduInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncAllEduInfoResponseBody = None,
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
            temp_model = SyncAllEduInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockMfaDeviceRequest(TeaModel):
    def __init__(
        self,
        ad_domain: str = None,
        serial_number: str = None,
    ):
        # The domain of the Active Directory (AD) workspace.
        self.ad_domain = ad_domain
        # The serial number of the virtual MFA device. The serial number is unique for each device.
        # 
        # This parameter is required.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class UnlockMfaDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UnlockMfaDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnlockMfaDeviceResponseBody = None,
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
            temp_model = UnlockMfaDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockUsersRequest(TeaModel):
    def __init__(
        self,
        auto_lock_time: str = None,
        users: List[str] = None,
    ):
        # The date on which the convenience users are automatically locked.
        self.auto_lock_time = auto_lock_time
        # The usernames of the convenience users that you want to unlock.
        # 
        # This parameter is required.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_lock_time is not None:
            result['AutoLockTime'] = self.auto_lock_time
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoLockTime') is not None:
            self.auto_lock_time = m.get('AutoLockTime')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class UnlockUsersResponseBodyUnlockUsersResultFailedUsers(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        # The ID of the convenience user that failed to be unlocked.
        self.end_user_id = end_user_id
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class UnlockUsersResponseBodyUnlockUsersResult(TeaModel):
    def __init__(
        self,
        failed_users: List[UnlockUsersResponseBodyUnlockUsersResultFailedUsers] = None,
        unlocked_users: List[str] = None,
    ):
        # The convenience users that failed to be unlocked.
        self.failed_users = failed_users
        # The convenience users that were unlocked.
        self.unlocked_users = unlocked_users

    def validate(self):
        if self.failed_users:
            for k in self.failed_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedUsers'] = []
        if self.failed_users is not None:
            for k in self.failed_users:
                result['FailedUsers'].append(k.to_map() if k else None)
        if self.unlocked_users is not None:
            result['UnlockedUsers'] = self.unlocked_users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_users = []
        if m.get('FailedUsers') is not None:
            for k in m.get('FailedUsers'):
                temp_model = UnlockUsersResponseBodyUnlockUsersResultFailedUsers()
                self.failed_users.append(temp_model.from_map(k))
        if m.get('UnlockedUsers') is not None:
            self.unlocked_users = m.get('UnlockedUsers')
        return self


class UnlockUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        unlock_users_result: UnlockUsersResponseBodyUnlockUsersResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of unlocking the convenience user.
        self.unlock_users_result = unlock_users_result

    def validate(self):
        if self.unlock_users_result:
            self.unlock_users_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.unlock_users_result is not None:
            result['UnlockUsersResult'] = self.unlock_users_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UnlockUsersResult') is not None:
            temp_model = UnlockUsersResponseBodyUnlockUsersResult()
            self.unlock_users_result = temp_model.from_map(m['UnlockUsersResult'])
        return self


class UnlockUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnlockUsersResponseBody = None,
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
            temp_model = UnlockUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePropertyRequestPropertyValues(TeaModel):
    def __init__(
        self,
        property_value: str = None,
        property_value_id: int = None,
    ):
        # The new property value.
        self.property_value = property_value
        # The ID of property value that you want to modify. You can call the [ListProperty](https://help.aliyun.com/document_detail/410890.html) operation to query the property value ID.
        self.property_value_id = property_value_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class UpdatePropertyRequest(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_key: str = None,
        property_values: List[UpdatePropertyRequestPropertyValues] = None,
    ):
        # The ID of the property that you want to modify. You can call the [ListProperty](https://help.aliyun.com/document_detail/410890.html) operation to query the property ID.
        # 
        # This parameter is required.
        self.property_id = property_id
        # The new property name.
        # 
        # This parameter is required.
        self.property_key = property_key
        # The values of property.
        self.property_values = property_values

    def validate(self):
        if self.property_values:
            for k in self.property_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        result['PropertyValues'] = []
        if self.property_values is not None:
            for k in self.property_values:
                result['PropertyValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        self.property_values = []
        if m.get('PropertyValues') is not None:
            for k in m.get('PropertyValues'):
                temp_model = UpdatePropertyRequestPropertyValues()
                self.property_values.append(temp_model.from_map(k))
        return self


class UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelFailedPropertyValues(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        property_id: int = None,
        property_value: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the property.
        self.property_id = property_id
        # The value of the property.
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        return self


class UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelSavePropertyValues(TeaModel):
    def __init__(
        self,
        property_value: str = None,
        property_value_id: int = None,
    ):
        # The value of the property.
        self.property_value = property_value
        # The ID of the property value.
        self.property_value_id = property_value_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class UpdatePropertyResponseBodyUpdateResultSavePropertyValueModel(TeaModel):
    def __init__(
        self,
        failed_property_values: List[UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelFailedPropertyValues] = None,
        save_property_values: List[UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelSavePropertyValues] = None,
    ):
        # The property values that failed to be modified.
        self.failed_property_values = failed_property_values
        # The property values that were modified.
        self.save_property_values = save_property_values

    def validate(self):
        if self.failed_property_values:
            for k in self.failed_property_values:
                if k:
                    k.validate()
        if self.save_property_values:
            for k in self.save_property_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedPropertyValues'] = []
        if self.failed_property_values is not None:
            for k in self.failed_property_values:
                result['FailedPropertyValues'].append(k.to_map() if k else None)
        result['SavePropertyValues'] = []
        if self.save_property_values is not None:
            for k in self.save_property_values:
                result['SavePropertyValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_property_values = []
        if m.get('FailedPropertyValues') is not None:
            for k in m.get('FailedPropertyValues'):
                temp_model = UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelFailedPropertyValues()
                self.failed_property_values.append(temp_model.from_map(k))
        self.save_property_values = []
        if m.get('SavePropertyValues') is not None:
            for k in m.get('SavePropertyValues'):
                temp_model = UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelSavePropertyValues()
                self.save_property_values.append(temp_model.from_map(k))
        return self


class UpdatePropertyResponseBodyUpdateResult(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_key: str = None,
        save_property_value_model: UpdatePropertyResponseBodyUpdateResultSavePropertyValueModel = None,
    ):
        # The ID of the property.
        self.property_id = property_id
        # The name of the property.
        self.property_key = property_key
        # The result of the property value modification.
        self.save_property_value_model = save_property_value_model

    def validate(self):
        if self.save_property_value_model:
            self.save_property_value_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.save_property_value_model is not None:
            result['SavePropertyValueModel'] = self.save_property_value_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('SavePropertyValueModel') is not None:
            temp_model = UpdatePropertyResponseBodyUpdateResultSavePropertyValueModel()
            self.save_property_value_model = temp_model.from_map(m['SavePropertyValueModel'])
        return self


class UpdatePropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        update_result: UpdatePropertyResponseBodyUpdateResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of the modification.
        self.update_result = update_result

    def validate(self):
        if self.update_result:
            self.update_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.update_result is not None:
            result['UpdateResult'] = self.update_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpdateResult') is not None:
            temp_model = UpdatePropertyResponseBodyUpdateResult()
            self.update_result = temp_model.from_map(m['UpdateResult'])
        return self


class UpdatePropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePropertyResponseBody = None,
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
            temp_model = UpdatePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UserBatchJoinGroupRequest(TeaModel):
    def __init__(
        self,
        end_user_ids: List[str] = None,
        group_id: str = None,
    ):
        self.end_user_ids = end_user_ids
        # This parameter is required.
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class UserBatchJoinGroupResponseBody(TeaModel):
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


class UserBatchJoinGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UserBatchJoinGroupResponseBody = None,
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
            temp_model = UserBatchJoinGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UserBatchQuitGroupRequest(TeaModel):
    def __init__(
        self,
        end_user_ids: List[str] = None,
        group_id: str = None,
    ):
        self.end_user_ids = end_user_ids
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class UserBatchQuitGroupResponseBody(TeaModel):
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


class UserBatchQuitGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UserBatchQuitGroupResponseBody = None,
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
            temp_model = UserBatchQuitGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


