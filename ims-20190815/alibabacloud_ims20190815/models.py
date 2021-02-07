# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddUserToGroupRequest(TeaModel):
    def __init__(
        self,
        group_principal_name: str = None,
        user_principal_name: str = None,
        ak_proxy_suffix: str = None,
        group_name: str = None,
    ):
        self.group_principal_name = group_principal_name
        self.user_principal_name = user_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_principal_name is not None:
            result['GroupPrincipalName'] = self.group_principal_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupPrincipalName') is not None:
            self.group_principal_name = m.get('GroupPrincipalName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class AddUserToGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddUserToGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddUserToGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUserToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindMFADeviceRequest(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        user_principal_name: str = None,
        authentication_code_1: str = None,
        authentication_code_2: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.serial_number = serial_number
        self.user_principal_name = user_principal_name
        self.authentication_code_1 = authentication_code_1
        self.authentication_code_2 = authentication_code_2
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.authentication_code_1 is not None:
            result['AuthenticationCode1'] = self.authentication_code_1
        if self.authentication_code_2 is not None:
            result['AuthenticationCode2'] = self.authentication_code_2
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('AuthenticationCode1') is not None:
            self.authentication_code_1 = m.get('AuthenticationCode1')
        if m.get('AuthenticationCode2') is not None:
            self.authentication_code_2 = m.get('AuthenticationCode2')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class BindMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindMFADeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangePasswordRequest(TeaModel):
    def __init__(
        self,
        old_password: str = None,
        new_password: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.old_password = old_password
        self.new_password = new_password
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.old_password is not None:
            result['OldPassword'] = self.old_password
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class ChangePasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangePasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangePasswordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ChangePasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessKeyRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class CreateAccessKeyResponseBodyAccessKey(TeaModel):
    def __init__(
        self,
        status: str = None,
        access_key_secret: str = None,
        access_key_id: str = None,
        create_date: str = None,
    ):
        self.status = status
        self.access_key_secret = access_key_secret
        self.access_key_id = access_key_id
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreateAccessKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        access_key: CreateAccessKeyResponseBodyAccessKey = None,
    ):
        self.request_id = request_id
        self.access_key = access_key

    def validate(self):
        if self.access_key:
            self.access_key.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessKey') is not None:
            temp_model = CreateAccessKeyResponseBodyAccessKey()
            self.access_key = temp_model.from_map(m['AccessKey'])
        return self


class CreateAccessKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAccessKeyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAccessKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        app_principal_name: str = None,
        app_type: str = None,
        redirect_uris: str = None,
        secret_required: bool = None,
        access_token_validity: int = None,
        refresh_token_validity: int = None,
        predefined_scopes: str = None,
        is_multi_tenant: bool = None,
        ak_proxy_suffix: str = None,
        app_name: str = None,
    ):
        self.display_name = display_name
        self.app_principal_name = app_principal_name
        self.app_type = app_type
        self.redirect_uris = redirect_uris
        self.secret_required = secret_required
        self.access_token_validity = access_token_validity
        self.refresh_token_validity = refresh_token_validity
        self.predefined_scopes = predefined_scopes
        self.is_multi_tenant = is_multi_tenant
        self.ak_proxy_suffix = ak_proxy_suffix
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.app_principal_name is not None:
            result['AppPrincipalName'] = self.app_principal_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('AppPrincipalName') is not None:
            self.app_principal_name = m.get('AppPrincipalName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('RedirectUris') is not None:
            self.redirect_uris = m.get('RedirectUris')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('PredefinedScopes') is not None:
            self.predefined_scopes = m.get('PredefinedScopes')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class CreateApplicationResponseBodyApplicationRedirectUris(TeaModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        self.redirect_uri = redirect_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class CreateApplicationResponseBodyApplicationDelegatedScope(TeaModel):
    def __init__(
        self,
        predefined_scopes: CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes = None,
    ):
        self.predefined_scopes = predefined_scopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class CreateApplicationResponseBodyApplication(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        access_token_validity: int = None,
        secret_required: bool = None,
        account_id: str = None,
        create_date: str = None,
        app_name: str = None,
        redirect_uris: CreateApplicationResponseBodyApplicationRedirectUris = None,
        update_date: str = None,
        delegated_scope: CreateApplicationResponseBodyApplicationDelegatedScope = None,
        app_id: str = None,
        refresh_token_validity: int = None,
        is_multi_tenant: bool = None,
        app_type: str = None,
    ):
        self.display_name = display_name
        self.access_token_validity = access_token_validity
        self.secret_required = secret_required
        self.account_id = account_id
        self.create_date = create_date
        self.app_name = app_name
        self.redirect_uris = redirect_uris
        self.update_date = update_date
        self.delegated_scope = delegated_scope
        self.app_id = app_id
        self.refresh_token_validity = refresh_token_validity
        self.is_multi_tenant = is_multi_tenant
        self.app_type = app_type

    def validate(self):
        if self.redirect_uris:
            self.redirect_uris.validate()
        if self.delegated_scope:
            self.delegated_scope.validate()

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RedirectUris') is not None:
            temp_model = CreateApplicationResponseBodyApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('DelegatedScope') is not None:
            temp_model = CreateApplicationResponseBodyApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        application: CreateApplicationResponseBodyApplication = None,
    ):
        self.request_id = request_id
        self.application = application

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.application is not None:
            result['Application'] = self.application.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Application') is not None:
            temp_model = CreateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSecretRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.app_id = app_id
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class CreateAppSecretResponseBodyAppSecret(TeaModel):
    def __init__(
        self,
        app_secret_value: str = None,
        app_id: str = None,
        app_secret_id: str = None,
        create_date: str = None,
    ):
        self.app_secret_value = app_secret_value
        self.app_id = app_id
        self.app_secret_id = app_secret_id
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_secret_value is not None:
            result['AppSecretValue'] = self.app_secret_value
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSecretValue') is not None:
            self.app_secret_value = m.get('AppSecretValue')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreateAppSecretResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_secret: CreateAppSecretResponseBodyAppSecret = None,
    ):
        self.request_id = request_id
        self.app_secret = app_secret

    def validate(self):
        if self.app_secret:
            self.app_secret.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppSecret') is not None:
            temp_model = CreateAppSecretResponseBodyAppSecret()
            self.app_secret = temp_model.from_map(m['AppSecret'])
        return self


class CreateAppSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppSecretResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAppSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        group_principal_name: str = None,
        display_name: str = None,
        comments: str = None,
        ak_proxy_suffix: str = None,
        group_name: str = None,
    ):
        self.group_principal_name = group_principal_name
        self.display_name = display_name
        self.comments = comments
        self.ak_proxy_suffix = ak_proxy_suffix
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_principal_name is not None:
            result['GroupPrincipalName'] = self.group_principal_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupPrincipalName') is not None:
            self.group_principal_name = m.get('GroupPrincipalName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class CreateGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        group_id: str = None,
        update_date: str = None,
        group_name: str = None,
        comments: str = None,
        create_date: str = None,
    ):
        self.display_name = display_name
        self.group_id = group_id
        self.update_date = update_date
        self.group_name = group_name
        self.comments = comments
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(
        self,
        group: CreateGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        self.group = group
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = CreateGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        password: str = None,
        password_reset_required: bool = None,
        mfabind_required: bool = None,
        generate_random_password: bool = None,
        status: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.password = password
        self.password_reset_required = password_reset_required
        self.mfabind_required = mfabind_required
        self.generate_random_password = generate_random_password
        self.status = status
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.password is not None:
            result['Password'] = self.password
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.generate_random_password is not None:
            result['GenerateRandomPassword'] = self.generate_random_password
        if self.status is not None:
            result['Status'] = self.status
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        if m.get('GenerateRandomPassword') is not None:
            self.generate_random_password = m.get('GenerateRandomPassword')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class CreateLoginProfileResponseBodyLoginProfile(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        status: str = None,
        update_date: str = None,
        password_reset_required: bool = None,
        mfabind_required: bool = None,
    ):
        self.user_principal_name = user_principal_name
        self.status = status
        self.update_date = update_date
        self.password_reset_required = password_reset_required
        self.mfabind_required = mfabind_required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        return self


class CreateLoginProfileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        login_profile: CreateLoginProfileResponseBodyLoginProfile = None,
    ):
        self.request_id = request_id
        self.login_profile = login_profile

    def validate(self):
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LoginProfile') is not None:
            temp_model = CreateLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        return self


class CreateLoginProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoginProfileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSAMLProviderRequest(TeaModel):
    def __init__(
        self,
        samlprovider_name: str = None,
        samlmetadata_document: str = None,
        description: str = None,
        ak_proxy_suffix: str = None,
        encoded_samlmetadata_document: str = None,
    ):
        self.samlprovider_name = samlprovider_name
        self.samlmetadata_document = samlmetadata_document
        self.description = description
        self.ak_proxy_suffix = ak_proxy_suffix
        self.encoded_samlmetadata_document = encoded_samlmetadata_document

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.samlmetadata_document is not None:
            result['SAMLMetadataDocument'] = self.samlmetadata_document
        if self.description is not None:
            result['Description'] = self.description
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        if self.encoded_samlmetadata_document is not None:
            result['EncodedSAMLMetadataDocument'] = self.encoded_samlmetadata_document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('SAMLMetadataDocument') is not None:
            self.samlmetadata_document = m.get('SAMLMetadataDocument')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        if m.get('EncodedSAMLMetadataDocument') is not None:
            self.encoded_samlmetadata_document = m.get('EncodedSAMLMetadataDocument')
        return self


class CreateSAMLProviderResponseBodySAMLProvider(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        description: str = None,
        samlprovider_name: str = None,
        create_date: str = None,
        arn: str = None,
    ):
        self.update_date = update_date
        self.description = description
        self.samlprovider_name = samlprovider_name
        self.create_date = create_date
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.description is not None:
            result['Description'] = self.description
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class CreateSAMLProviderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlprovider: CreateSAMLProviderResponseBodySAMLProvider = None,
    ):
        self.request_id = request_id
        self.samlprovider = samlprovider

    def validate(self):
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLProvider') is not None:
            temp_model = CreateSAMLProviderResponseBodySAMLProvider()
            self.samlprovider = temp_model.from_map(m['SAMLProvider'])
        return self


class CreateSAMLProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSAMLProviderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        display_name: str = None,
        mobile_phone: str = None,
        email: str = None,
        comments: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.display_name = display_name
        self.mobile_phone = mobile_phone
        self.email = email
        self.comments = comments
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.email is not None:
            result['Email'] = self.email
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class CreateUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        user_principal_name: str = None,
        email: str = None,
        update_date: str = None,
        mobile_phone: str = None,
        user_id: str = None,
        comments: str = None,
        last_login_date: str = None,
        create_date: str = None,
    ):
        self.display_name = display_name
        self.user_principal_name = user_principal_name
        self.email = email
        self.update_date = update_date
        self.mobile_phone = mobile_phone
        self.user_id = user_id
        self.comments = comments
        self.last_login_date = last_login_date
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.email is not None:
            result['Email'] = self.email
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(
        self,
        user: CreateUserResponseBodyUser = None,
        request_id: str = None,
    ):
        self.user = user
        self.request_id = request_id

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            temp_model = CreateUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        virtual_mfadevice_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.virtual_mfadevice_name = virtual_mfadevice_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.virtual_mfadevice_name is not None:
            result['VirtualMFADeviceName'] = self.virtual_mfadevice_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VirtualMFADeviceName') is not None:
            self.virtual_mfadevice_name = m.get('VirtualMFADeviceName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class CreateVirtualMFADeviceResponseBodyVirtualMFADevice(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        qrcode_png: str = None,
        base_32string_seed: str = None,
    ):
        self.serial_number = serial_number
        self.qrcode_png = qrcode_png
        self.base_32string_seed = base_32string_seed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.qrcode_png is not None:
            result['QRCodePNG'] = self.qrcode_png
        if self.base_32string_seed is not None:
            result['Base32StringSeed'] = self.base_32string_seed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('QRCodePNG') is not None:
            self.qrcode_png = m.get('QRCodePNG')
        if m.get('Base32StringSeed') is not None:
            self.base_32string_seed = m.get('Base32StringSeed')
        return self


class CreateVirtualMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        virtual_mfadevice: CreateVirtualMFADeviceResponseBodyVirtualMFADevice = None,
        request_id: str = None,
    ):
        self.virtual_mfadevice = virtual_mfadevice
        self.request_id = request_id

    def validate(self):
        if self.virtual_mfadevice:
            self.virtual_mfadevice.validate()

    def to_map(self):
        result = dict()
        if self.virtual_mfadevice is not None:
            result['VirtualMFADevice'] = self.virtual_mfadevice.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VirtualMFADevice') is not None:
            temp_model = CreateVirtualMFADeviceResponseBodyVirtualMFADevice()
            self.virtual_mfadevice = temp_model.from_map(m['VirtualMFADevice'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVirtualMFADeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessKeyRequest(TeaModel):
    def __init__(
        self,
        user_access_key_id: str = None,
        user_principal_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_access_key_id = user_access_key_id
        self.user_principal_name = user_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class DeleteAccessKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAccessKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAccessKeyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAccessKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.app_id = app_id
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppSecretRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.app_id = app_id
        self.app_secret_id = app_secret_id
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class DeleteAppSecretResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAppSecretResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAppSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(
        self,
        group_principal_name: str = None,
        ak_proxy_suffix: str = None,
        group_name: str = None,
    ):
        self.group_principal_name = group_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_principal_name is not None:
            result['GroupPrincipalName'] = self.group_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupPrincipalName') is not None:
            self.group_principal_name = m.get('GroupPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DeleteGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class DeleteLoginProfileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLoginProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLoginProfileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSAMLProviderRequest(TeaModel):
    def __init__(
        self,
        samlprovider_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.samlprovider_name = samlprovider_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class DeleteSAMLProviderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSAMLProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSAMLProviderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        user_id: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.user_id = user_id
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.serial_number = serial_number
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class DeleteVirtualMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVirtualMFADeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableVirtualMFARequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class DisableVirtualMFAResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableVirtualMFAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableVirtualMFAResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableVirtualMFAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateCredentialReportRequest(TeaModel):
    def __init__(
        self,
        ak_proxy_suffix: str = None,
    ):
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GenerateCredentialReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state: str = None,
    ):
        self.request_id = request_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GenerateCredentialReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateCredentialReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateCredentialReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessKeyLastUsedRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        user_access_key_id: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.user_access_key_id = user_access_key_id
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed(TeaModel):
    def __init__(
        self,
        last_used_date: str = None,
    ):
        self.last_used_date = last_used_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.last_used_date is not None:
            result['LastUsedDate'] = self.last_used_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastUsedDate') is not None:
            self.last_used_date = m.get('LastUsedDate')
        return self


class GetAccessKeyLastUsedResponseBody(TeaModel):
    def __init__(
        self,
        access_key_last_used: GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed = None,
        request_id: str = None,
    ):
        self.access_key_last_used = access_key_last_used
        self.request_id = request_id

    def validate(self):
        if self.access_key_last_used:
            self.access_key_last_used.validate()

    def to_map(self):
        result = dict()
        if self.access_key_last_used is not None:
            result['AccessKeyLastUsed'] = self.access_key_last_used.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyLastUsed') is not None:
            temp_model = GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed()
            self.access_key_last_used = temp_model.from_map(m['AccessKeyLastUsed'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessKeyLastUsedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccessKeyLastUsedResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAccessKeyLastUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountMFAInfoRequest(TeaModel):
    def __init__(
        self,
        ak_proxy_suffix: str = None,
    ):
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetAccountMFAInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_mfaenable: bool = None,
    ):
        self.request_id = request_id
        self.is_mfaenable = is_mfaenable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_mfaenable is not None:
            result['IsMFAEnable'] = self.is_mfaenable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsMFAEnable') is not None:
            self.is_mfaenable = m.get('IsMFAEnable')
        return self


class GetAccountMFAInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccountMFAInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAccountMFAInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountSecurityPracticeReportRequest(TeaModel):
    def __init__(
        self,
        ak_proxy_suffix: str = None,
    ):
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo(TeaModel):
    def __init__(
        self,
        unused_ak_num: int = None,
        sub_user_with_unused_access_key: int = None,
        root_with_access_key: int = None,
        sub_user: int = None,
        bind_mfa: bool = None,
        old_ak_num: int = None,
        sub_user_pwd_level: str = None,
        sub_user_with_old_access_key: int = None,
        sub_user_bind_mfa: int = None,
    ):
        self.unused_ak_num = unused_ak_num
        self.sub_user_with_unused_access_key = sub_user_with_unused_access_key
        self.root_with_access_key = root_with_access_key
        self.sub_user = sub_user
        self.bind_mfa = bind_mfa
        self.old_ak_num = old_ak_num
        self.sub_user_pwd_level = sub_user_pwd_level
        self.sub_user_with_old_access_key = sub_user_with_old_access_key
        self.sub_user_bind_mfa = sub_user_bind_mfa

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.unused_ak_num is not None:
            result['UnusedAkNum'] = self.unused_ak_num
        if self.sub_user_with_unused_access_key is not None:
            result['SubUserWithUnusedAccessKey'] = self.sub_user_with_unused_access_key
        if self.root_with_access_key is not None:
            result['RootWithAccessKey'] = self.root_with_access_key
        if self.sub_user is not None:
            result['SubUser'] = self.sub_user
        if self.bind_mfa is not None:
            result['BindMfa'] = self.bind_mfa
        if self.old_ak_num is not None:
            result['OldAkNum'] = self.old_ak_num
        if self.sub_user_pwd_level is not None:
            result['SubUserPwdLevel'] = self.sub_user_pwd_level
        if self.sub_user_with_old_access_key is not None:
            result['SubUserWithOldAccessKey'] = self.sub_user_with_old_access_key
        if self.sub_user_bind_mfa is not None:
            result['SubUserBindMfa'] = self.sub_user_bind_mfa
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UnusedAkNum') is not None:
            self.unused_ak_num = m.get('UnusedAkNum')
        if m.get('SubUserWithUnusedAccessKey') is not None:
            self.sub_user_with_unused_access_key = m.get('SubUserWithUnusedAccessKey')
        if m.get('RootWithAccessKey') is not None:
            self.root_with_access_key = m.get('RootWithAccessKey')
        if m.get('SubUser') is not None:
            self.sub_user = m.get('SubUser')
        if m.get('BindMfa') is not None:
            self.bind_mfa = m.get('BindMfa')
        if m.get('OldAkNum') is not None:
            self.old_ak_num = m.get('OldAkNum')
        if m.get('SubUserPwdLevel') is not None:
            self.sub_user_pwd_level = m.get('SubUserPwdLevel')
        if m.get('SubUserWithOldAccessKey') is not None:
            self.sub_user_with_old_access_key = m.get('SubUserWithOldAccessKey')
        if m.get('SubUserBindMfa') is not None:
            self.sub_user_bind_mfa = m.get('SubUserBindMfa')
        return self


class GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo(TeaModel):
    def __init__(
        self,
        account_security_practice_user_info: GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo = None,
        score: int = None,
    ):
        self.account_security_practice_user_info = account_security_practice_user_info
        self.score = score

    def validate(self):
        if self.account_security_practice_user_info:
            self.account_security_practice_user_info.validate()

    def to_map(self):
        result = dict()
        if self.account_security_practice_user_info is not None:
            result['AccountSecurityPracticeUserInfo'] = self.account_security_practice_user_info.to_map()
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountSecurityPracticeUserInfo') is not None:
            temp_model = GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo()
            self.account_security_practice_user_info = temp_model.from_map(m['AccountSecurityPracticeUserInfo'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class GetAccountSecurityPracticeReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account_security_practice_info: GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo = None,
    ):
        self.request_id = request_id
        self.account_security_practice_info = account_security_practice_info

    def validate(self):
        if self.account_security_practice_info:
            self.account_security_practice_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account_security_practice_info is not None:
            result['AccountSecurityPracticeInfo'] = self.account_security_practice_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccountSecurityPracticeInfo') is not None:
            temp_model = GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo()
            self.account_security_practice_info = temp_model.from_map(m['AccountSecurityPracticeInfo'])
        return self


class GetAccountSecurityPracticeReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccountSecurityPracticeReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAccountSecurityPracticeReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountSummaryRequest(TeaModel):
    def __init__(
        self,
        ak_proxy_suffix: str = None,
    ):
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetAccountSummaryResponseBodySummaryMap(TeaModel):
    def __init__(
        self,
        mfadevices: int = None,
        access_keys_per_user_quota: int = None,
        attached_policies_per_group_quota: int = None,
        attached_system_policies_per_role_quota: int = None,
        attached_policies_per_role_quota: int = None,
        groups_per_user_quota: int = None,
        roles: int = None,
        policy_size_quota: int = None,
        attached_system_policies_per_group_quota: int = None,
        attached_system_policies_per_user_quota: int = None,
        attached_policies_per_user_quota: int = None,
        groups_quota: int = None,
        groups: int = None,
        policies_quota: int = None,
        virtual_mfadevices_quota: int = None,
        versions_per_policy_quota: int = None,
        roles_quota: int = None,
        users_quota: int = None,
        policies: int = None,
        users: int = None,
        mfadevices_in_use: int = None,
    ):
        self.mfadevices = mfadevices
        self.access_keys_per_user_quota = access_keys_per_user_quota
        self.attached_policies_per_group_quota = attached_policies_per_group_quota
        self.attached_system_policies_per_role_quota = attached_system_policies_per_role_quota
        self.attached_policies_per_role_quota = attached_policies_per_role_quota
        self.groups_per_user_quota = groups_per_user_quota
        self.roles = roles
        self.policy_size_quota = policy_size_quota
        self.attached_system_policies_per_group_quota = attached_system_policies_per_group_quota
        self.attached_system_policies_per_user_quota = attached_system_policies_per_user_quota
        self.attached_policies_per_user_quota = attached_policies_per_user_quota
        self.groups_quota = groups_quota
        self.groups = groups
        self.policies_quota = policies_quota
        self.virtual_mfadevices_quota = virtual_mfadevices_quota
        self.versions_per_policy_quota = versions_per_policy_quota
        self.roles_quota = roles_quota
        self.users_quota = users_quota
        self.policies = policies
        self.users = users
        self.mfadevices_in_use = mfadevices_in_use

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mfadevices is not None:
            result['MFADevices'] = self.mfadevices
        if self.access_keys_per_user_quota is not None:
            result['AccessKeysPerUserQuota'] = self.access_keys_per_user_quota
        if self.attached_policies_per_group_quota is not None:
            result['AttachedPoliciesPerGroupQuota'] = self.attached_policies_per_group_quota
        if self.attached_system_policies_per_role_quota is not None:
            result['AttachedSystemPoliciesPerRoleQuota'] = self.attached_system_policies_per_role_quota
        if self.attached_policies_per_role_quota is not None:
            result['AttachedPoliciesPerRoleQuota'] = self.attached_policies_per_role_quota
        if self.groups_per_user_quota is not None:
            result['GroupsPerUserQuota'] = self.groups_per_user_quota
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.policy_size_quota is not None:
            result['PolicySizeQuota'] = self.policy_size_quota
        if self.attached_system_policies_per_group_quota is not None:
            result['AttachedSystemPoliciesPerGroupQuota'] = self.attached_system_policies_per_group_quota
        if self.attached_system_policies_per_user_quota is not None:
            result['AttachedSystemPoliciesPerUserQuota'] = self.attached_system_policies_per_user_quota
        if self.attached_policies_per_user_quota is not None:
            result['AttachedPoliciesPerUserQuota'] = self.attached_policies_per_user_quota
        if self.groups_quota is not None:
            result['GroupsQuota'] = self.groups_quota
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.policies_quota is not None:
            result['PoliciesQuota'] = self.policies_quota
        if self.virtual_mfadevices_quota is not None:
            result['VirtualMFADevicesQuota'] = self.virtual_mfadevices_quota
        if self.versions_per_policy_quota is not None:
            result['VersionsPerPolicyQuota'] = self.versions_per_policy_quota
        if self.roles_quota is not None:
            result['RolesQuota'] = self.roles_quota
        if self.users_quota is not None:
            result['UsersQuota'] = self.users_quota
        if self.policies is not None:
            result['Policies'] = self.policies
        if self.users is not None:
            result['Users'] = self.users
        if self.mfadevices_in_use is not None:
            result['MFADevicesInUse'] = self.mfadevices_in_use
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFADevices') is not None:
            self.mfadevices = m.get('MFADevices')
        if m.get('AccessKeysPerUserQuota') is not None:
            self.access_keys_per_user_quota = m.get('AccessKeysPerUserQuota')
        if m.get('AttachedPoliciesPerGroupQuota') is not None:
            self.attached_policies_per_group_quota = m.get('AttachedPoliciesPerGroupQuota')
        if m.get('AttachedSystemPoliciesPerRoleQuota') is not None:
            self.attached_system_policies_per_role_quota = m.get('AttachedSystemPoliciesPerRoleQuota')
        if m.get('AttachedPoliciesPerRoleQuota') is not None:
            self.attached_policies_per_role_quota = m.get('AttachedPoliciesPerRoleQuota')
        if m.get('GroupsPerUserQuota') is not None:
            self.groups_per_user_quota = m.get('GroupsPerUserQuota')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('PolicySizeQuota') is not None:
            self.policy_size_quota = m.get('PolicySizeQuota')
        if m.get('AttachedSystemPoliciesPerGroupQuota') is not None:
            self.attached_system_policies_per_group_quota = m.get('AttachedSystemPoliciesPerGroupQuota')
        if m.get('AttachedSystemPoliciesPerUserQuota') is not None:
            self.attached_system_policies_per_user_quota = m.get('AttachedSystemPoliciesPerUserQuota')
        if m.get('AttachedPoliciesPerUserQuota') is not None:
            self.attached_policies_per_user_quota = m.get('AttachedPoliciesPerUserQuota')
        if m.get('GroupsQuota') is not None:
            self.groups_quota = m.get('GroupsQuota')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('PoliciesQuota') is not None:
            self.policies_quota = m.get('PoliciesQuota')
        if m.get('VirtualMFADevicesQuota') is not None:
            self.virtual_mfadevices_quota = m.get('VirtualMFADevicesQuota')
        if m.get('VersionsPerPolicyQuota') is not None:
            self.versions_per_policy_quota = m.get('VersionsPerPolicyQuota')
        if m.get('RolesQuota') is not None:
            self.roles_quota = m.get('RolesQuota')
        if m.get('UsersQuota') is not None:
            self.users_quota = m.get('UsersQuota')
        if m.get('Policies') is not None:
            self.policies = m.get('Policies')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        if m.get('MFADevicesInUse') is not None:
            self.mfadevices_in_use = m.get('MFADevicesInUse')
        return self


class GetAccountSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        summary_map: GetAccountSummaryResponseBodySummaryMap = None,
    ):
        self.request_id = request_id
        self.summary_map = summary_map

    def validate(self):
        if self.summary_map:
            self.summary_map.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.summary_map is not None:
            result['SummaryMap'] = self.summary_map.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SummaryMap') is not None:
            temp_model = GetAccountSummaryResponseBodySummaryMap()
            self.summary_map = temp_model.from_map(m['SummaryMap'])
        return self


class GetAccountSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccountSummaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAccountSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.app_id = app_id
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetApplicationResponseBodyApplicationRedirectUris(TeaModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        self.redirect_uri = redirect_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class GetApplicationResponseBodyApplicationDelegatedScope(TeaModel):
    def __init__(
        self,
        predefined_scopes: GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopes = None,
    ):
        self.predefined_scopes = predefined_scopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class GetApplicationResponseBodyApplication(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        access_token_validity: int = None,
        secret_required: bool = None,
        account_id: str = None,
        create_date: str = None,
        app_name: str = None,
        redirect_uris: GetApplicationResponseBodyApplicationRedirectUris = None,
        update_date: str = None,
        delegated_scope: GetApplicationResponseBodyApplicationDelegatedScope = None,
        app_id: str = None,
        refresh_token_validity: int = None,
        is_multi_tenant: bool = None,
        app_type: str = None,
    ):
        self.display_name = display_name
        self.access_token_validity = access_token_validity
        self.secret_required = secret_required
        self.account_id = account_id
        self.create_date = create_date
        self.app_name = app_name
        self.redirect_uris = redirect_uris
        self.update_date = update_date
        self.delegated_scope = delegated_scope
        self.app_id = app_id
        self.refresh_token_validity = refresh_token_validity
        self.is_multi_tenant = is_multi_tenant
        self.app_type = app_type

    def validate(self):
        if self.redirect_uris:
            self.redirect_uris.validate()
        if self.delegated_scope:
            self.delegated_scope.validate()

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RedirectUris') is not None:
            temp_model = GetApplicationResponseBodyApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('DelegatedScope') is not None:
            temp_model = GetApplicationResponseBodyApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        application: GetApplicationResponseBodyApplication = None,
    ):
        self.request_id = request_id
        self.application = application

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.application is not None:
            result['Application'] = self.application.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Application') is not None:
            temp_model = GetApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        return self


class GetApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppSecretRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.app_id = app_id
        self.app_secret_id = app_secret_id
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetAppSecretResponseBodyAppSecret(TeaModel):
    def __init__(
        self,
        app_secret_value: str = None,
        app_id: str = None,
        app_secret_id: str = None,
        create_date: str = None,
    ):
        self.app_secret_value = app_secret_value
        self.app_id = app_id
        self.app_secret_id = app_secret_id
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_secret_value is not None:
            result['AppSecretValue'] = self.app_secret_value
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSecretValue') is not None:
            self.app_secret_value = m.get('AppSecretValue')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class GetAppSecretResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_secret: GetAppSecretResponseBodyAppSecret = None,
    ):
        self.request_id = request_id
        self.app_secret = app_secret

    def validate(self):
        if self.app_secret:
            self.app_secret.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppSecret') is not None:
            temp_model = GetAppSecretResponseBodyAppSecret()
            self.app_secret = temp_model.from_map(m['AppSecret'])
        return self


class GetAppSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAppSecretResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAppSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCredentialReportRequest(TeaModel):
    def __init__(
        self,
        ak_proxy_suffix: str = None,
    ):
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetCredentialReportResponseBody(TeaModel):
    def __init__(
        self,
        generated_time: str = None,
        request_id: str = None,
        content: str = None,
    ):
        self.generated_time = generated_time
        self.request_id = request_id
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.generated_time is not None:
            result['GeneratedTime'] = self.generated_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GeneratedTime') is not None:
            self.generated_time = m.get('GeneratedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetCredentialReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCredentialReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCredentialReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultDomainRequest(TeaModel):
    def __init__(
        self,
        ak_proxy_suffix: str = None,
    ):
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetDefaultDomainResponseBody(TeaModel):
    def __init__(
        self,
        default_domain_name: str = None,
        request_id: str = None,
    ):
        self.default_domain_name = default_domain_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultDomainName') is not None:
            self.default_domain_name = m.get('DefaultDomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDefaultDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDefaultDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDefaultDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupRequest(TeaModel):
    def __init__(
        self,
        group_principal_name: str = None,
        ak_proxy_suffix: str = None,
        group_name: str = None,
    ):
        self.group_principal_name = group_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_principal_name is not None:
            result['GroupPrincipalName'] = self.group_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupPrincipalName') is not None:
            self.group_principal_name = m.get('GroupPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        group_id: str = None,
        update_date: str = None,
        group_name: str = None,
        comments: str = None,
        create_date: str = None,
    ):
        self.display_name = display_name
        self.group_id = group_id
        self.update_date = update_date
        self.group_name = group_name
        self.comments = comments
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class GetGroupResponseBody(TeaModel):
    def __init__(
        self,
        group: GetGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        self.group = group
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = GetGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetLoginProfileResponseBodyLoginProfile(TeaModel):
    def __init__(
        self,
        status: str = None,
        user_principal_name: str = None,
        update_date: str = None,
        last_login_time: str = None,
        password_reset_required: bool = None,
        mfabind_required: bool = None,
    ):
        self.status = status
        self.user_principal_name = user_principal_name
        self.update_date = update_date
        self.last_login_time = last_login_time
        self.password_reset_required = password_reset_required
        self.mfabind_required = mfabind_required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        return self


class GetLoginProfileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        login_profile: GetLoginProfileResponseBodyLoginProfile = None,
    ):
        self.request_id = request_id
        self.login_profile = login_profile

    def validate(self):
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LoginProfile') is not None:
            temp_model = GetLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        return self


class GetLoginProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLoginProfileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPasswordPolicyRequest(TeaModel):
    def __init__(
        self,
        ak_proxy_suffix: str = None,
    ):
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetPasswordPolicyResponseBodyPasswordPolicy(TeaModel):
    def __init__(
        self,
        require_numbers: bool = None,
        require_lowercase_characters: bool = None,
        password_reuse_prevention: int = None,
        require_symbols: bool = None,
        password_not_contain_user_name: bool = None,
        minimum_password_different_character: int = None,
        max_password_age: int = None,
        hard_expire: bool = None,
        minimum_password_length: int = None,
        require_uppercase_characters: bool = None,
        max_login_attemps: int = None,
    ):
        self.require_numbers = require_numbers
        self.require_lowercase_characters = require_lowercase_characters
        self.password_reuse_prevention = password_reuse_prevention
        self.require_symbols = require_symbols
        self.password_not_contain_user_name = password_not_contain_user_name
        self.minimum_password_different_character = minimum_password_different_character
        self.max_password_age = max_password_age
        self.hard_expire = hard_expire
        self.minimum_password_length = minimum_password_length
        self.require_uppercase_characters = require_uppercase_characters
        self.max_login_attemps = max_login_attemps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name
        if self.minimum_password_different_character is not None:
            result['MinimumPasswordDifferentCharacter'] = self.minimum_password_different_character
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')
        if m.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = m.get('MinimumPasswordDifferentCharacter')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        return self


class GetPasswordPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        password_policy: GetPasswordPolicyResponseBodyPasswordPolicy = None,
    ):
        self.request_id = request_id
        self.password_policy = password_policy

    def validate(self):
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PasswordPolicy') is not None:
            temp_model = GetPasswordPolicyResponseBodyPasswordPolicy()
            self.password_policy = temp_model.from_map(m['PasswordPolicy'])
        return self


class GetPasswordPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPasswordPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSAMLProviderRequest(TeaModel):
    def __init__(
        self,
        samlprovider_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.samlprovider_name = samlprovider_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetSAMLProviderResponseBodySAMLProvider(TeaModel):
    def __init__(
        self,
        description: str = None,
        update_date: str = None,
        samlprovider_name: str = None,
        create_date: str = None,
        encoded_samlmetadata_document: str = None,
        arn: str = None,
    ):
        self.description = description
        self.update_date = update_date
        self.samlprovider_name = samlprovider_name
        self.create_date = create_date
        self.encoded_samlmetadata_document = encoded_samlmetadata_document
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.encoded_samlmetadata_document is not None:
            result['EncodedSAMLMetadataDocument'] = self.encoded_samlmetadata_document
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('EncodedSAMLMetadataDocument') is not None:
            self.encoded_samlmetadata_document = m.get('EncodedSAMLMetadataDocument')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class GetSAMLProviderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlprovider: GetSAMLProviderResponseBodySAMLProvider = None,
    ):
        self.request_id = request_id
        self.samlprovider = samlprovider

    def validate(self):
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLProvider') is not None:
            temp_model = GetSAMLProviderResponseBodySAMLProvider()
            self.samlprovider = temp_model.from_map(m['SAMLProvider'])
        return self


class GetSAMLProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSAMLProviderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecurityPreferenceRequest(TeaModel):
    def __init__(
        self,
        ak_proxy_suffix: str = None,
    ):
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_access_keys: bool = None,
    ):
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference(TeaModel):
    def __init__(
        self,
        enable_save_mfaticket: bool = None,
        login_session_duration: int = None,
        login_network_masks: str = None,
        allow_user_to_change_password: bool = None,
    ):
        self.enable_save_mfaticket = enable_save_mfaticket
        self.login_session_duration = login_session_duration
        self.login_network_masks = login_network_masks
        self.allow_user_to_change_password = allow_user_to_change_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_mfadevices: bool = None,
    ):
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        return self


class GetSecurityPreferenceResponseBodySecurityPreference(TeaModel):
    def __init__(
        self,
        access_key_preference: GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference = None,
        login_profile_preference: GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference = None,
        mfapreference: GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference = None,
    ):
        self.access_key_preference = access_key_preference
        self.login_profile_preference = login_profile_preference
        self.mfapreference = mfapreference

    def validate(self):
        if self.access_key_preference:
            self.access_key_preference.validate()
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        if self.mfapreference:
            self.mfapreference.validate()

    def to_map(self):
        result = dict()
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()
        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()
        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(m['AccessKeyPreference'])
        if m.get('LoginProfilePreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(m['LoginProfilePreference'])
        if m.get('MFAPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(m['MFAPreference'])
        return self


class GetSecurityPreferenceResponseBody(TeaModel):
    def __init__(
        self,
        security_preference: GetSecurityPreferenceResponseBodySecurityPreference = None,
        request_id: str = None,
    ):
        self.security_preference = security_preference
        self.request_id = request_id

    def validate(self):
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        result = dict()
        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreference()
            self.security_preference = temp_model.from_map(m['SecurityPreference'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSecurityPreferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSecurityPreferenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSecurityPreferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        user_id: str = None,
        user_access_key_id: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.user_id = user_id
        self.user_access_key_id = user_access_key_id
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        user_principal_name: str = None,
        email: str = None,
        update_date: str = None,
        mobile_phone: str = None,
        user_id: str = None,
        comments: str = None,
        last_login_date: str = None,
        create_date: str = None,
    ):
        self.display_name = display_name
        self.user_principal_name = user_principal_name
        self.email = email
        self.update_date = update_date
        self.mobile_phone = mobile_phone
        self.user_id = user_id
        self.comments = comments
        self.last_login_date = last_login_date
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.email is not None:
            result['Email'] = self.email
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        user: GetUserResponseBodyUser = None,
        request_id: str = None,
    ):
        self.user = user
        self.request_id = request_id

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            temp_model = GetUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserMFAInfoRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetUserMFAInfoResponseBodyMFADevice(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
    ):
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class GetUserMFAInfoResponseBody(TeaModel):
    def __init__(
        self,
        mfadevice: GetUserMFAInfoResponseBodyMFADevice = None,
        request_id: str = None,
        is_mfaenable: bool = None,
    ):
        self.mfadevice = mfadevice
        self.request_id = request_id
        self.is_mfaenable = is_mfaenable

    def validate(self):
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        result = dict()
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_mfaenable is not None:
            result['IsMFAEnable'] = self.is_mfaenable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFADevice') is not None:
            temp_model = GetUserMFAInfoResponseBodyMFADevice()
            self.mfadevice = temp_model.from_map(m['MFADevice'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsMFAEnable') is not None:
            self.is_mfaenable = m.get('IsMFAEnable')
        return self


class GetUserMFAInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserMFAInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserMFAInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserSsoSettingsRequest(TeaModel):
    def __init__(
        self,
        ak_proxy_suffix: str = None,
    ):
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class GetUserSsoSettingsResponseBodyUserSsoSettings(TeaModel):
    def __init__(
        self,
        auxiliary_domain: str = None,
        metadata_document: str = None,
        sso_enabled: bool = None,
    ):
        self.auxiliary_domain = auxiliary_domain
        self.metadata_document = metadata_document
        self.sso_enabled = sso_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')
        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        return self


class GetUserSsoSettingsResponseBody(TeaModel):
    def __init__(
        self,
        user_sso_settings: GetUserSsoSettingsResponseBodyUserSsoSettings = None,
        request_id: str = None,
    ):
        self.user_sso_settings = user_sso_settings
        self.request_id = request_id

    def validate(self):
        if self.user_sso_settings:
            self.user_sso_settings.validate()

    def to_map(self):
        result = dict()
        if self.user_sso_settings is not None:
            result['UserSsoSettings'] = self.user_sso_settings.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserSsoSettings') is not None:
            temp_model = GetUserSsoSettingsResponseBodyUserSsoSettings()
            self.user_sso_settings = temp_model.from_map(m['UserSsoSettings'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserSsoSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserSsoSettingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserSsoSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessKeysRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class ListAccessKeysResponseBodyAccessKeysAccessKey(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_date: str = None,
        access_key_id: str = None,
        create_date: str = None,
    ):
        self.status = status
        self.update_date = update_date
        self.access_key_id = access_key_id
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListAccessKeysResponseBodyAccessKeys(TeaModel):
    def __init__(
        self,
        access_key: List[ListAccessKeysResponseBodyAccessKeysAccessKey] = None,
    ):
        self.access_key = access_key

    def validate(self):
        if self.access_key:
            for k in self.access_key:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AccessKey'] = []
        if self.access_key is not None:
            for k in self.access_key:
                result['AccessKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_key = []
        if m.get('AccessKey') is not None:
            for k in m.get('AccessKey'):
                temp_model = ListAccessKeysResponseBodyAccessKeysAccessKey()
                self.access_key.append(temp_model.from_map(k))
        return self


class ListAccessKeysResponseBody(TeaModel):
    def __init__(
        self,
        access_keys: ListAccessKeysResponseBodyAccessKeys = None,
        request_id: str = None,
    ):
        self.access_keys = access_keys
        self.request_id = request_id

    def validate(self):
        if self.access_keys:
            self.access_keys.validate()

    def to_map(self):
        result = dict()
        if self.access_keys is not None:
            result['AccessKeys'] = self.access_keys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeys') is not None:
            temp_model = ListAccessKeysResponseBodyAccessKeys()
            self.access_keys = temp_model.from_map(m['AccessKeys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAccessKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAccessKeysResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAccessKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsRequest(TeaModel):
    def __init__(
        self,
        ak_proxy_suffix: str = None,
    ):
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class ListApplicationsResponseBodyApplicationsApplicationRedirectUris(TeaModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        self.redirect_uri = redirect_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBodyApplicationsApplicationDelegatedScope(TeaModel):
    def __init__(
        self,
        predefined_scopes: ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes = None,
    ):
        self.predefined_scopes = predefined_scopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class ListApplicationsResponseBodyApplicationsApplication(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        access_token_validity: int = None,
        secret_required: bool = None,
        account_id: str = None,
        create_date: str = None,
        app_name: str = None,
        redirect_uris: ListApplicationsResponseBodyApplicationsApplicationRedirectUris = None,
        update_date: str = None,
        delegated_scope: ListApplicationsResponseBodyApplicationsApplicationDelegatedScope = None,
        app_id: str = None,
        refresh_token_validity: int = None,
        is_multi_tenant: bool = None,
        app_type: str = None,
    ):
        self.display_name = display_name
        self.access_token_validity = access_token_validity
        self.secret_required = secret_required
        self.account_id = account_id
        self.create_date = create_date
        self.app_name = app_name
        self.redirect_uris = redirect_uris
        self.update_date = update_date
        self.delegated_scope = delegated_scope
        self.app_id = app_id
        self.refresh_token_validity = refresh_token_validity
        self.is_multi_tenant = is_multi_tenant
        self.app_type = app_type

    def validate(self):
        if self.redirect_uris:
            self.redirect_uris.validate()
        if self.delegated_scope:
            self.delegated_scope.validate()

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RedirectUris') is not None:
            temp_model = ListApplicationsResponseBodyApplicationsApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('DelegatedScope') is not None:
            temp_model = ListApplicationsResponseBodyApplicationsApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class ListApplicationsResponseBodyApplications(TeaModel):
    def __init__(
        self,
        application: List[ListApplicationsResponseBodyApplicationsApplication] = None,
    ):
        self.application = application

    def validate(self):
        if self.application:
            for k in self.application:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application = []
        if m.get('Application') is not None:
            for k in m.get('Application'):
                temp_model = ListApplicationsResponseBodyApplicationsApplication()
                self.application.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        applications: ListApplicationsResponseBodyApplications = None,
    ):
        self.request_id = request_id
        self.applications = applications

    def validate(self):
        if self.applications:
            self.applications.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Applications') is not None:
            temp_model = ListApplicationsResponseBodyApplications()
            self.applications = temp_model.from_map(m['Applications'])
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppSecretIdsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.app_id = app_id
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class ListAppSecretIdsResponseBodyAppSecretsAppSecret(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
        create_date: str = None,
    ):
        self.app_id = app_id
        self.app_secret_id = app_secret_id
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListAppSecretIdsResponseBodyAppSecrets(TeaModel):
    def __init__(
        self,
        app_secret: List[ListAppSecretIdsResponseBodyAppSecretsAppSecret] = None,
    ):
        self.app_secret = app_secret

    def validate(self):
        if self.app_secret:
            for k in self.app_secret:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AppSecret'] = []
        if self.app_secret is not None:
            for k in self.app_secret:
                result['AppSecret'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_secret = []
        if m.get('AppSecret') is not None:
            for k in m.get('AppSecret'):
                temp_model = ListAppSecretIdsResponseBodyAppSecretsAppSecret()
                self.app_secret.append(temp_model.from_map(k))
        return self


class ListAppSecretIdsResponseBody(TeaModel):
    def __init__(
        self,
        app_secrets: ListAppSecretIdsResponseBodyAppSecrets = None,
        request_id: str = None,
    ):
        self.app_secrets = app_secrets
        self.request_id = request_id

    def validate(self):
        if self.app_secrets:
            self.app_secrets.validate()

    def to_map(self):
        result = dict()
        if self.app_secrets is not None:
            result['AppSecrets'] = self.app_secrets.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSecrets') is not None:
            temp_model = ListAppSecretIdsResponseBodyAppSecrets()
            self.app_secrets = temp_model.from_map(m['AppSecrets'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppSecretIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppSecretIdsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAppSecretIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
        ak_proxy_suffix: str = None,
    ):
        self.marker = marker
        self.max_items = max_items
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class ListGroupsResponseBodyGroupsGroup(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        group_id: str = None,
        update_date: str = None,
        group_name: str = None,
        comments: str = None,
        create_date: str = None,
    ):
        self.display_name = display_name
        self.group_id = group_id
        self.update_date = update_date
        self.group_name = group_name
        self.comments = comments
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListGroupsResponseBodyGroups(TeaModel):
    def __init__(
        self,
        group: List[ListGroupsResponseBodyGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k in m.get('Group'):
                temp_model = ListGroupsResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        groups: ListGroupsResponseBodyGroups = None,
        is_truncated: bool = None,
        marker: str = None,
    ):
        self.request_id = request_id
        self.groups = groups
        self.is_truncated = is_truncated
        self.marker = marker

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Groups') is not None:
            temp_model = ListGroupsResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsForUserRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class ListGroupsForUserResponseBodyGroupsGroup(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        group_name: str = None,
        group_id: str = None,
        comments: str = None,
        join_date: str = None,
    ):
        self.display_name = display_name
        self.group_name = group_name
        self.group_id = group_id
        self.comments = comments
        self.join_date = join_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.join_date is not None:
            result['JoinDate'] = self.join_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('JoinDate') is not None:
            self.join_date = m.get('JoinDate')
        return self


class ListGroupsForUserResponseBodyGroups(TeaModel):
    def __init__(
        self,
        group: List[ListGroupsForUserResponseBodyGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k in m.get('Group'):
                temp_model = ListGroupsForUserResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListGroupsForUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        groups: ListGroupsForUserResponseBodyGroups = None,
    ):
        self.request_id = request_id
        self.groups = groups

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Groups') is not None:
            temp_model = ListGroupsForUserResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        return self


class ListGroupsForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGroupsForUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGroupsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPredefinedScopesRequest(TeaModel):
    def __init__(
        self,
        ak_proxy_suffix: str = None,
        app_type: str = None,
    ):
        self.ak_proxy_suffix = ak_proxy_suffix
        self.app_type = app_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListPredefinedScopesResponseBodyPredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class ListPredefinedScopesResponseBody(TeaModel):
    def __init__(
        self,
        predefined_scopes: ListPredefinedScopesResponseBodyPredefinedScopes = None,
        request_id: str = None,
    ):
        self.predefined_scopes = predefined_scopes
        self.request_id = request_id

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = ListPredefinedScopesResponseBodyPredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPredefinedScopesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPredefinedScopesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPredefinedScopesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSAMLProvidersRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
        ak_proxy_suffix: str = None,
    ):
        self.marker = marker
        self.max_items = max_items
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        description: str = None,
        samlprovider_name: str = None,
        create_date: str = None,
        arn: str = None,
    ):
        self.update_date = update_date
        self.description = description
        self.samlprovider_name = samlprovider_name
        self.create_date = create_date
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.description is not None:
            result['Description'] = self.description
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class ListSAMLProvidersResponseBodySAMLProviders(TeaModel):
    def __init__(
        self,
        samlprovider: List[ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider] = None,
    ):
        self.samlprovider = samlprovider

    def validate(self):
        if self.samlprovider:
            for k in self.samlprovider:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SAMLProvider'] = []
        if self.samlprovider is not None:
            for k in self.samlprovider:
                result['SAMLProvider'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.samlprovider = []
        if m.get('SAMLProvider') is not None:
            for k in m.get('SAMLProvider'):
                temp_model = ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider()
                self.samlprovider.append(temp_model.from_map(k))
        return self


class ListSAMLProvidersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlproviders: ListSAMLProvidersResponseBodySAMLProviders = None,
        is_truncated: bool = None,
        marker: str = None,
    ):
        self.request_id = request_id
        self.samlproviders = samlproviders
        self.is_truncated = is_truncated
        self.marker = marker

    def validate(self):
        if self.samlproviders:
            self.samlproviders.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlproviders is not None:
            result['SAMLProviders'] = self.samlproviders.to_map()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLProviders') is not None:
            temp_model = ListSAMLProvidersResponseBodySAMLProviders()
            self.samlproviders = temp_model.from_map(m['SAMLProviders'])
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListSAMLProvidersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSAMLProvidersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSAMLProvidersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserBasicInfosRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
        ak_proxy_suffix: str = None,
    ):
        self.marker = marker
        self.max_items = max_items
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        display_name: str = None,
        user_id: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.display_name = display_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserBasicInfosResponseBodyUserBasicInfos(TeaModel):
    def __init__(
        self,
        user_basic_info: List[ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo] = None,
    ):
        self.user_basic_info = user_basic_info

    def validate(self):
        if self.user_basic_info:
            for k in self.user_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UserBasicInfo'] = []
        if self.user_basic_info is not None:
            for k in self.user_basic_info:
                result['UserBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_basic_info = []
        if m.get('UserBasicInfo') is not None:
            for k in m.get('UserBasicInfo'):
                temp_model = ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo()
                self.user_basic_info.append(temp_model.from_map(k))
        return self


class ListUserBasicInfosResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_truncated: bool = None,
        user_basic_infos: ListUserBasicInfosResponseBodyUserBasicInfos = None,
        marker: str = None,
    ):
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.user_basic_infos = user_basic_infos
        self.marker = marker

    def validate(self):
        if self.user_basic_infos:
            self.user_basic_infos.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.user_basic_infos is not None:
            result['UserBasicInfos'] = self.user_basic_infos.to_map()
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('UserBasicInfos') is not None:
            temp_model = ListUserBasicInfosResponseBodyUserBasicInfos()
            self.user_basic_infos = temp_model.from_map(m['UserBasicInfos'])
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListUserBasicInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserBasicInfosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserBasicInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
        ak_proxy_suffix: str = None,
    ):
        self.marker = marker
        self.max_items = max_items
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class ListUsersResponseBodyUsersUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        user_principal_name: str = None,
        email: str = None,
        update_date: str = None,
        mobile_phone: str = None,
        user_id: str = None,
        comments: str = None,
        last_login_date: str = None,
        create_date: str = None,
    ):
        self.display_name = display_name
        self.user_principal_name = user_principal_name
        self.email = email
        self.update_date = update_date
        self.mobile_phone = mobile_phone
        self.user_id = user_id
        self.comments = comments
        self.last_login_date = last_login_date
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.email is not None:
            result['Email'] = self.email
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user: List[ListUsersResponseBodyUsersUser] = None,
    ):
        self.user = user

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ListUsersResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_truncated: bool = None,
        marker: str = None,
        users: ListUsersResponseBodyUsers = None,
    ):
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('Users') is not None:
            temp_model = ListUsersResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersForGroupRequest(TeaModel):
    def __init__(
        self,
        group_principal_name: str = None,
        ak_proxy_suffix: str = None,
        group_name: str = None,
        marker: str = None,
        max_items: int = None,
    ):
        self.group_principal_name = group_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix
        self.group_name = group_name
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_principal_name is not None:
            result['GroupPrincipalName'] = self.group_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupPrincipalName') is not None:
            self.group_principal_name = m.get('GroupPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListUsersForGroupResponseBodyUsersUser(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        display_name: str = None,
        user_id: str = None,
        join_date: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.display_name = display_name
        self.user_id = user_id
        self.join_date = join_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.join_date is not None:
            result['JoinDate'] = self.join_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('JoinDate') is not None:
            self.join_date = m.get('JoinDate')
        return self


class ListUsersForGroupResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user: List[ListUsersForGroupResponseBodyUsersUser] = None,
    ):
        self.user = user

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ListUsersForGroupResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersForGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_truncated: bool = None,
        marker: str = None,
        users: ListUsersForGroupResponseBodyUsers = None,
    ):
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('Users') is not None:
            temp_model = ListUsersForGroupResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListUsersForGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUsersForGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUsersForGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVirtualMFADevicesRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
        ak_proxy_suffix: str = None,
    ):
        self.marker = marker
        self.max_items = max_items
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        display_name: str = None,
        user_id: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.display_name = display_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        user: ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser = None,
        activate_date: str = None,
    ):
        self.serial_number = serial_number
        self.user = user
        self.activate_date = activate_date

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.activate_date is not None:
            result['ActivateDate'] = self.activate_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('User') is not None:
            temp_model = ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('ActivateDate') is not None:
            self.activate_date = m.get('ActivateDate')
        return self


class ListVirtualMFADevicesResponseBodyVirtualMFADevices(TeaModel):
    def __init__(
        self,
        virtual_mfadevice: List[ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice] = None,
    ):
        self.virtual_mfadevice = virtual_mfadevice

    def validate(self):
        if self.virtual_mfadevice:
            for k in self.virtual_mfadevice:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VirtualMFADevice'] = []
        if self.virtual_mfadevice is not None:
            for k in self.virtual_mfadevice:
                result['VirtualMFADevice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.virtual_mfadevice = []
        if m.get('VirtualMFADevice') is not None:
            for k in m.get('VirtualMFADevice'):
                temp_model = ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice()
                self.virtual_mfadevice.append(temp_model.from_map(k))
        return self


class ListVirtualMFADevicesResponseBody(TeaModel):
    def __init__(
        self,
        virtual_mfadevices: ListVirtualMFADevicesResponseBodyVirtualMFADevices = None,
        request_id: str = None,
        is_truncated: bool = None,
        marker: str = None,
    ):
        self.virtual_mfadevices = virtual_mfadevices
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker

    def validate(self):
        if self.virtual_mfadevices:
            self.virtual_mfadevices.validate()

    def to_map(self):
        result = dict()
        if self.virtual_mfadevices is not None:
            result['VirtualMFADevices'] = self.virtual_mfadevices.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VirtualMFADevices') is not None:
            temp_model = ListVirtualMFADevicesResponseBodyVirtualMFADevices()
            self.virtual_mfadevices = temp_model.from_map(m['VirtualMFADevices'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListVirtualMFADevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVirtualMFADevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListVirtualMFADevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromGroupRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        group_principal_name: str = None,
        ak_proxy_suffix: str = None,
        group_name: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.group_principal_name = group_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.group_principal_name is not None:
            result['GroupPrincipalName'] = self.group_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('GroupPrincipalName') is not None:
            self.group_principal_name = m.get('GroupPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class RemoveUserFromGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveUserFromGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveUserFromGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveUserFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultDomainRequest(TeaModel):
    def __init__(
        self,
        default_domain_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.default_domain_name = default_domain_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultDomainName') is not None:
            self.default_domain_name = m.get('DefaultDomainName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class SetDefaultDomainResponseBody(TeaModel):
    def __init__(
        self,
        default_domain_name: str = None,
        request_id: str = None,
    ):
        self.default_domain_name = default_domain_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultDomainName') is not None:
            self.default_domain_name = m.get('DefaultDomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDefaultDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDefaultDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDefaultDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPasswordPolicyRequest(TeaModel):
    def __init__(
        self,
        minimum_password_length: int = None,
        require_lowercase_characters: bool = None,
        require_uppercase_characters: bool = None,
        require_numbers: bool = None,
        require_symbols: bool = None,
        hard_expire: bool = None,
        max_login_attemps: int = None,
        password_reuse_prevention: int = None,
        max_password_age: int = None,
        minimum_password_different_character: int = None,
        password_not_contain_user_name: bool = None,
        ak_proxy_suffix: str = None,
    ):
        self.minimum_password_length = minimum_password_length
        self.require_lowercase_characters = require_lowercase_characters
        self.require_uppercase_characters = require_uppercase_characters
        self.require_numbers = require_numbers
        self.require_symbols = require_symbols
        self.hard_expire = hard_expire
        self.max_login_attemps = max_login_attemps
        self.password_reuse_prevention = password_reuse_prevention
        self.max_password_age = max_password_age
        self.minimum_password_different_character = minimum_password_different_character
        self.password_not_contain_user_name = password_not_contain_user_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.minimum_password_different_character is not None:
            result['MinimumPasswordDifferentCharacter'] = self.minimum_password_different_character
        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = m.get('MinimumPasswordDifferentCharacter')
        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class SetPasswordPolicyResponseBodyPasswordPolicy(TeaModel):
    def __init__(
        self,
        require_numbers: bool = None,
        require_lowercase_characters: bool = None,
        password_reuse_prevention: int = None,
        require_symbols: bool = None,
        password_not_contain_user_name: bool = None,
        minimum_password_different_character: int = None,
        max_password_age: int = None,
        hard_expire: bool = None,
        minimum_password_length: int = None,
        require_uppercase_characters: bool = None,
        max_login_attemps: int = None,
    ):
        self.require_numbers = require_numbers
        self.require_lowercase_characters = require_lowercase_characters
        self.password_reuse_prevention = password_reuse_prevention
        self.require_symbols = require_symbols
        self.password_not_contain_user_name = password_not_contain_user_name
        self.minimum_password_different_character = minimum_password_different_character
        self.max_password_age = max_password_age
        self.hard_expire = hard_expire
        self.minimum_password_length = minimum_password_length
        self.require_uppercase_characters = require_uppercase_characters
        self.max_login_attemps = max_login_attemps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name
        if self.minimum_password_different_character is not None:
            result['MinimumPasswordDifferentCharacter'] = self.minimum_password_different_character
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')
        if m.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = m.get('MinimumPasswordDifferentCharacter')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        return self


class SetPasswordPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        password_policy: SetPasswordPolicyResponseBodyPasswordPolicy = None,
    ):
        self.request_id = request_id
        self.password_policy = password_policy

    def validate(self):
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PasswordPolicy') is not None:
            temp_model = SetPasswordPolicyResponseBodyPasswordPolicy()
            self.password_policy = temp_model.from_map(m['PasswordPolicy'])
        return self


class SetPasswordPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetPasswordPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSecurityPreferenceRequest(TeaModel):
    def __init__(
        self,
        enable_save_mfaticket: bool = None,
        allow_user_to_change_password: bool = None,
        allow_user_to_manage_access_keys: bool = None,
        allow_user_to_manage_mfadevices: bool = None,
        login_session_duration: int = None,
        login_network_masks: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.enable_save_mfaticket = enable_save_mfaticket
        self.allow_user_to_change_password = allow_user_to_change_password
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices
        self.login_session_duration = login_session_duration
        self.login_network_masks = login_network_masks
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_access_keys: bool = None,
    ):
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference(TeaModel):
    def __init__(
        self,
        enable_save_mfaticket: bool = None,
        login_session_duration: int = None,
        login_network_masks: str = None,
        allow_user_to_change_password: bool = None,
    ):
        self.enable_save_mfaticket = enable_save_mfaticket
        self.login_session_duration = login_session_duration
        self.login_network_masks = login_network_masks
        self.allow_user_to_change_password = allow_user_to_change_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_mfadevices: bool = None,
    ):
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        return self


class SetSecurityPreferenceResponseBodySecurityPreference(TeaModel):
    def __init__(
        self,
        access_key_preference: SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference = None,
        login_profile_preference: SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference = None,
        mfapreference: SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference = None,
    ):
        self.access_key_preference = access_key_preference
        self.login_profile_preference = login_profile_preference
        self.mfapreference = mfapreference

    def validate(self):
        if self.access_key_preference:
            self.access_key_preference.validate()
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        if self.mfapreference:
            self.mfapreference.validate()

    def to_map(self):
        result = dict()
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()
        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()
        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(m['AccessKeyPreference'])
        if m.get('LoginProfilePreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(m['LoginProfilePreference'])
        if m.get('MFAPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(m['MFAPreference'])
        return self


class SetSecurityPreferenceResponseBody(TeaModel):
    def __init__(
        self,
        security_preference: SetSecurityPreferenceResponseBodySecurityPreference = None,
        request_id: str = None,
    ):
        self.security_preference = security_preference
        self.request_id = request_id

    def validate(self):
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        result = dict()
        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreference()
            self.security_preference = temp_model.from_map(m['SecurityPreference'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetSecurityPreferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetSecurityPreferenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetSecurityPreferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserSsoSettingsRequest(TeaModel):
    def __init__(
        self,
        metadata_document: str = None,
        sso_enabled: bool = None,
        auxiliary_domain: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.metadata_document = metadata_document
        self.sso_enabled = sso_enabled
        self.auxiliary_domain = auxiliary_domain
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class SetUserSsoSettingsResponseBodyUserSsoSettings(TeaModel):
    def __init__(
        self,
        auxiliary_domain: str = None,
        metadata_document: str = None,
        sso_enabled: bool = None,
    ):
        self.auxiliary_domain = auxiliary_domain
        self.metadata_document = metadata_document
        self.sso_enabled = sso_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')
        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        return self


class SetUserSsoSettingsResponseBody(TeaModel):
    def __init__(
        self,
        user_sso_settings: SetUserSsoSettingsResponseBodyUserSsoSettings = None,
        request_id: str = None,
    ):
        self.user_sso_settings = user_sso_settings
        self.request_id = request_id

    def validate(self):
        if self.user_sso_settings:
            self.user_sso_settings.validate()

    def to_map(self):
        result = dict()
        if self.user_sso_settings is not None:
            result['UserSsoSettings'] = self.user_sso_settings.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserSsoSettings') is not None:
            temp_model = SetUserSsoSettingsResponseBodyUserSsoSettings()
            self.user_sso_settings = temp_model.from_map(m['UserSsoSettings'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetUserSsoSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetUserSsoSettingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetUserSsoSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindMFADeviceRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class UnbindMFADeviceResponseBodyMFADevice(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
    ):
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class UnbindMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        mfadevice: UnbindMFADeviceResponseBodyMFADevice = None,
        request_id: str = None,
    ):
        self.mfadevice = mfadevice
        self.request_id = request_id

    def validate(self):
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        result = dict()
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFADevice') is not None:
            temp_model = UnbindMFADeviceResponseBodyMFADevice()
            self.mfadevice = temp_model.from_map(m['MFADevice'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindMFADeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnbindMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccessKeyRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        user_access_key_id: str = None,
        status: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.user_access_key_id = user_access_key_id
        self.status = status
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.status is not None:
            result['Status'] = self.status
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class UpdateAccessKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAccessKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAccessKeyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAccessKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        new_display_name: str = None,
        new_redirect_uris: str = None,
        new_predefined_scopes: str = None,
        new_secret_required: bool = None,
        new_access_token_validity: int = None,
        new_refresh_token_validity: int = None,
        new_is_multi_tenant: bool = None,
        ak_proxy_suffix: str = None,
    ):
        self.app_id = app_id
        self.new_display_name = new_display_name
        self.new_redirect_uris = new_redirect_uris
        self.new_predefined_scopes = new_predefined_scopes
        self.new_secret_required = new_secret_required
        self.new_access_token_validity = new_access_token_validity
        self.new_refresh_token_validity = new_refresh_token_validity
        self.new_is_multi_tenant = new_is_multi_tenant
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.new_redirect_uris is not None:
            result['NewRedirectUris'] = self.new_redirect_uris
        if self.new_predefined_scopes is not None:
            result['NewPredefinedScopes'] = self.new_predefined_scopes
        if self.new_secret_required is not None:
            result['NewSecretRequired'] = self.new_secret_required
        if self.new_access_token_validity is not None:
            result['NewAccessTokenValidity'] = self.new_access_token_validity
        if self.new_refresh_token_validity is not None:
            result['NewRefreshTokenValidity'] = self.new_refresh_token_validity
        if self.new_is_multi_tenant is not None:
            result['NewIsMultiTenant'] = self.new_is_multi_tenant
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('NewRedirectUris') is not None:
            self.new_redirect_uris = m.get('NewRedirectUris')
        if m.get('NewPredefinedScopes') is not None:
            self.new_predefined_scopes = m.get('NewPredefinedScopes')
        if m.get('NewSecretRequired') is not None:
            self.new_secret_required = m.get('NewSecretRequired')
        if m.get('NewAccessTokenValidity') is not None:
            self.new_access_token_validity = m.get('NewAccessTokenValidity')
        if m.get('NewRefreshTokenValidity') is not None:
            self.new_refresh_token_validity = m.get('NewRefreshTokenValidity')
        if m.get('NewIsMultiTenant') is not None:
            self.new_is_multi_tenant = m.get('NewIsMultiTenant')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class UpdateApplicationResponseBodyApplicationRedirectUris(TeaModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        self.redirect_uri = redirect_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class UpdateApplicationResponseBodyApplicationDelegatedScope(TeaModel):
    def __init__(
        self,
        predefined_scopes: UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes = None,
    ):
        self.predefined_scopes = predefined_scopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class UpdateApplicationResponseBodyApplication(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        access_token_validity: int = None,
        secret_required: bool = None,
        account_id: str = None,
        create_date: str = None,
        app_name: str = None,
        redirect_uris: UpdateApplicationResponseBodyApplicationRedirectUris = None,
        update_date: str = None,
        delegated_scope: UpdateApplicationResponseBodyApplicationDelegatedScope = None,
        app_id: str = None,
        refresh_token_validity: int = None,
        is_multi_tenant: bool = None,
        app_type: str = None,
    ):
        self.display_name = display_name
        self.access_token_validity = access_token_validity
        self.secret_required = secret_required
        self.account_id = account_id
        self.create_date = create_date
        self.app_name = app_name
        self.redirect_uris = redirect_uris
        self.update_date = update_date
        self.delegated_scope = delegated_scope
        self.app_id = app_id
        self.refresh_token_validity = refresh_token_validity
        self.is_multi_tenant = is_multi_tenant
        self.app_type = app_type

    def validate(self):
        if self.redirect_uris:
            self.redirect_uris.validate()
        if self.delegated_scope:
            self.delegated_scope.validate()

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RedirectUris') is not None:
            temp_model = UpdateApplicationResponseBodyApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('DelegatedScope') is not None:
            temp_model = UpdateApplicationResponseBodyApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class UpdateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        application: UpdateApplicationResponseBodyApplication = None,
    ):
        self.request_id = request_id
        self.application = application

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.application is not None:
            result['Application'] = self.application.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Application') is not None:
            temp_model = UpdateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        return self


class UpdateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(
        self,
        group_principal_name: str = None,
        new_group_principal_name: str = None,
        new_comments: str = None,
        new_display_name: str = None,
        ak_proxy_suffix: str = None,
        new_group_name: str = None,
        group_name: str = None,
    ):
        self.group_principal_name = group_principal_name
        self.new_group_principal_name = new_group_principal_name
        self.new_comments = new_comments
        self.new_display_name = new_display_name
        self.ak_proxy_suffix = ak_proxy_suffix
        self.new_group_name = new_group_name
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_principal_name is not None:
            result['GroupPrincipalName'] = self.group_principal_name
        if self.new_group_principal_name is not None:
            result['NewGroupPrincipalName'] = self.new_group_principal_name
        if self.new_comments is not None:
            result['NewComments'] = self.new_comments
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        if self.new_group_name is not None:
            result['NewGroupName'] = self.new_group_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupPrincipalName') is not None:
            self.group_principal_name = m.get('GroupPrincipalName')
        if m.get('NewGroupPrincipalName') is not None:
            self.new_group_principal_name = m.get('NewGroupPrincipalName')
        if m.get('NewComments') is not None:
            self.new_comments = m.get('NewComments')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        if m.get('NewGroupName') is not None:
            self.new_group_name = m.get('NewGroupName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class UpdateGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        group_id: str = None,
        update_date: str = None,
        group_name: str = None,
        comments: str = None,
        create_date: str = None,
    ):
        self.display_name = display_name
        self.group_id = group_id
        self.update_date = update_date
        self.group_name = group_name
        self.comments = comments
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class UpdateGroupResponseBody(TeaModel):
    def __init__(
        self,
        group: UpdateGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        self.group = group
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = UpdateGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        password: str = None,
        password_reset_required: bool = None,
        mfabind_required: bool = None,
        generate_random_password: bool = None,
        status: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.password = password
        self.password_reset_required = password_reset_required
        self.mfabind_required = mfabind_required
        self.generate_random_password = generate_random_password
        self.status = status
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.password is not None:
            result['Password'] = self.password
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.generate_random_password is not None:
            result['GenerateRandomPassword'] = self.generate_random_password
        if self.status is not None:
            result['Status'] = self.status
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        if m.get('GenerateRandomPassword') is not None:
            self.generate_random_password = m.get('GenerateRandomPassword')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class UpdateLoginProfileResponseBodyLoginProfile(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        status: str = None,
        update_date: str = None,
        password_reset_required: bool = None,
        mfabind_required: bool = None,
    ):
        self.user_principal_name = user_principal_name
        self.status = status
        self.update_date = update_date
        self.password_reset_required = password_reset_required
        self.mfabind_required = mfabind_required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        return self


class UpdateLoginProfileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        login_profile: UpdateLoginProfileResponseBodyLoginProfile = None,
    ):
        self.request_id = request_id
        self.login_profile = login_profile

    def validate(self):
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LoginProfile') is not None:
            temp_model = UpdateLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        return self


class UpdateLoginProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLoginProfileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSAMLProviderRequest(TeaModel):
    def __init__(
        self,
        samlprovider_name: str = None,
        new_samlmetadata_document: str = None,
        new_description: str = None,
        ak_proxy_suffix: str = None,
        new_encoded_samlmetadata_document: str = None,
    ):
        self.samlprovider_name = samlprovider_name
        self.new_samlmetadata_document = new_samlmetadata_document
        self.new_description = new_description
        self.ak_proxy_suffix = ak_proxy_suffix
        self.new_encoded_samlmetadata_document = new_encoded_samlmetadata_document

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.new_samlmetadata_document is not None:
            result['NewSAMLMetadataDocument'] = self.new_samlmetadata_document
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        if self.new_encoded_samlmetadata_document is not None:
            result['NewEncodedSAMLMetadataDocument'] = self.new_encoded_samlmetadata_document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('NewSAMLMetadataDocument') is not None:
            self.new_samlmetadata_document = m.get('NewSAMLMetadataDocument')
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        if m.get('NewEncodedSAMLMetadataDocument') is not None:
            self.new_encoded_samlmetadata_document = m.get('NewEncodedSAMLMetadataDocument')
        return self


class UpdateSAMLProviderResponseBodySAMLProvider(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        description: str = None,
        samlprovider_name: str = None,
        create_date: str = None,
        arn: str = None,
    ):
        self.update_date = update_date
        self.description = description
        self.samlprovider_name = samlprovider_name
        self.create_date = create_date
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.description is not None:
            result['Description'] = self.description
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class UpdateSAMLProviderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlprovider: UpdateSAMLProviderResponseBodySAMLProvider = None,
    ):
        self.request_id = request_id
        self.samlprovider = samlprovider

    def validate(self):
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLProvider') is not None:
            temp_model = UpdateSAMLProviderResponseBodySAMLProvider()
            self.samlprovider = temp_model.from_map(m['SAMLProvider'])
        return self


class UpdateSAMLProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSAMLProviderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        user_id: str = None,
        new_user_principal_name: str = None,
        new_display_name: str = None,
        new_mobile_phone: str = None,
        new_email: str = None,
        new_comments: str = None,
        ak_proxy_suffix: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.user_id = user_id
        self.new_user_principal_name = new_user_principal_name
        self.new_display_name = new_display_name
        self.new_mobile_phone = new_mobile_phone
        self.new_email = new_email
        self.new_comments = new_comments
        self.ak_proxy_suffix = ak_proxy_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.new_user_principal_name is not None:
            result['NewUserPrincipalName'] = self.new_user_principal_name
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.new_mobile_phone is not None:
            result['NewMobilePhone'] = self.new_mobile_phone
        if self.new_email is not None:
            result['NewEmail'] = self.new_email
        if self.new_comments is not None:
            result['NewComments'] = self.new_comments
        if self.ak_proxy_suffix is not None:
            result['AkProxySuffix'] = self.ak_proxy_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('NewUserPrincipalName') is not None:
            self.new_user_principal_name = m.get('NewUserPrincipalName')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('NewMobilePhone') is not None:
            self.new_mobile_phone = m.get('NewMobilePhone')
        if m.get('NewEmail') is not None:
            self.new_email = m.get('NewEmail')
        if m.get('NewComments') is not None:
            self.new_comments = m.get('NewComments')
        if m.get('AkProxySuffix') is not None:
            self.ak_proxy_suffix = m.get('AkProxySuffix')
        return self


class UpdateUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        user_principal_name: str = None,
        email: str = None,
        update_date: str = None,
        mobile_phone: str = None,
        user_id: str = None,
        comments: str = None,
        last_login_date: str = None,
        create_date: str = None,
    ):
        self.display_name = display_name
        self.user_principal_name = user_principal_name
        self.email = email
        self.update_date = update_date
        self.mobile_phone = mobile_phone
        self.user_id = user_id
        self.comments = comments
        self.last_login_date = last_login_date
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.email is not None:
            result['Email'] = self.email
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        user: UpdateUserResponseBodyUser = None,
        request_id: str = None,
    ):
        self.user = user
        self.request_id = request_id

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            temp_model = UpdateUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


