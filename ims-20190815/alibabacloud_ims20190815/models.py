# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class GetUserSsoSettingsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetUserSsoSettingsResponseUserSsoSettings(TeaModel):
    def __init__(
        self,
        metadata_document: str = None,
        sso_enabled: bool = None,
        auxiliary_domain: str = None,
    ):
        self.metadata_document = metadata_document
        self.sso_enabled = sso_enabled
        self.auxiliary_domain = auxiliary_domain

    def validate(self):
        self.validate_required(self.metadata_document, 'metadata_document')
        self.validate_required(self.sso_enabled, 'sso_enabled')
        self.validate_required(self.auxiliary_domain, 'auxiliary_domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')
        return self


class GetUserSsoSettingsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_sso_settings: GetUserSsoSettingsResponseUserSsoSettings = None,
    ):
        self.request_id = request_id
        self.user_sso_settings = user_sso_settings

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.user_sso_settings, 'user_sso_settings')
        if self.user_sso_settings:
            self.user_sso_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_sso_settings is not None:
            result['UserSsoSettings'] = self.user_sso_settings.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSsoSettings') is not None:
            temp_model = GetUserSsoSettingsResponseUserSsoSettings()
            self.user_sso_settings = temp_model.from_map(m['UserSsoSettings'])
        return self


class SetUserSsoSettingsRequest(TeaModel):
    def __init__(
        self,
        metadata_document: str = None,
        sso_enabled: bool = None,
        auxiliary_domain: str = None,
    ):
        self.metadata_document = metadata_document
        self.sso_enabled = sso_enabled
        self.auxiliary_domain = auxiliary_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')
        return self


class SetUserSsoSettingsResponseUserSsoSettings(TeaModel):
    def __init__(
        self,
        metadata_document: str = None,
        sso_enabled: bool = None,
        auxiliary_domain: str = None,
    ):
        self.metadata_document = metadata_document
        self.sso_enabled = sso_enabled
        self.auxiliary_domain = auxiliary_domain

    def validate(self):
        self.validate_required(self.metadata_document, 'metadata_document')
        self.validate_required(self.sso_enabled, 'sso_enabled')
        self.validate_required(self.auxiliary_domain, 'auxiliary_domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')
        return self


class SetUserSsoSettingsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_sso_settings: SetUserSsoSettingsResponseUserSsoSettings = None,
    ):
        self.request_id = request_id
        self.user_sso_settings = user_sso_settings

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.user_sso_settings, 'user_sso_settings')
        if self.user_sso_settings:
            self.user_sso_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_sso_settings is not None:
            result['UserSsoSettings'] = self.user_sso_settings.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSsoSettings') is not None:
            temp_model = SetUserSsoSettingsResponseUserSsoSettings()
            self.user_sso_settings = temp_model.from_map(m['UserSsoSettings'])
        return self


class SetDefaultDomainRequest(TeaModel):
    def __init__(
        self,
        default_domain_name: str = None,
    ):
        self.default_domain_name = default_domain_name

    def validate(self):
        self.validate_required(self.default_domain_name, 'default_domain_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultDomainName') is not None:
            self.default_domain_name = m.get('DefaultDomainName')
        return self


class SetDefaultDomainResponse(TeaModel):
    def __init__(
        self,
        default_domain_name: str = None,
        request_id: str = None,
    ):
        self.default_domain_name = default_domain_name
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.default_domain_name, 'default_domain_name')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListUserBasicInfosRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListUserBasicInfosResponseUserBasicInfosUserBasicInfo(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        display_name: str = None,
        user_principal_name: str = None,
    ):
        self.user_id = user_id
        self.display_name = display_name
        self.user_principal_name = user_principal_name

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListUserBasicInfosResponseUserBasicInfos(TeaModel):
    def __init__(
        self,
        user_basic_info: List[ListUserBasicInfosResponseUserBasicInfosUserBasicInfo] = None,
    ):
        self.user_basic_info = user_basic_info

    def validate(self):
        self.validate_required(self.user_basic_info, 'user_basic_info')
        if self.user_basic_info:
            for k in self.user_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListUserBasicInfosResponseUserBasicInfosUserBasicInfo()
                self.user_basic_info.append(temp_model.from_map(k))
        return self


class ListUserBasicInfosResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_truncated: bool = None,
        marker: str = None,
        user_basic_infos: ListUserBasicInfosResponseUserBasicInfos = None,
    ):
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker
        self.user_basic_infos = user_basic_infos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_truncated, 'is_truncated')
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.user_basic_infos, 'user_basic_infos')
        if self.user_basic_infos:
            self.user_basic_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.user_basic_infos is not None:
            result['UserBasicInfos'] = self.user_basic_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('UserBasicInfos') is not None:
            temp_model = ListUserBasicInfosResponseUserBasicInfos()
            self.user_basic_infos = temp_model.from_map(m['UserBasicInfos'])
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
    ):
        self.app_id = app_id
        self.new_display_name = new_display_name
        self.new_redirect_uris = new_redirect_uris
        self.new_predefined_scopes = new_predefined_scopes
        self.new_secret_required = new_secret_required
        self.new_access_token_validity = new_access_token_validity
        self.new_refresh_token_validity = new_refresh_token_validity
        self.new_is_multi_tenant = new_is_multi_tenant

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        return self


class UpdateApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        self.validate_required(self.description, 'description')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateApplicationResponseApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[UpdateApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        self.validate_required(self.predefined_scope, 'predefined_scope')
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = UpdateApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class UpdateApplicationResponseApplicationDelegatedScope(TeaModel):
    def __init__(
        self,
        predefined_scopes: UpdateApplicationResponseApplicationDelegatedScopePredefinedScopes = None,
    ):
        self.predefined_scopes = predefined_scopes

    def validate(self):
        self.validate_required(self.predefined_scopes, 'predefined_scopes')
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = UpdateApplicationResponseApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class UpdateApplicationResponseApplicationRedirectUris(TeaModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        # RedirectUri
        self.redirect_uri = redirect_uri

    def validate(self):
        self.validate_required(self.redirect_uri, 'redirect_uri')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class UpdateApplicationResponseApplication(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        account_id: str = None,
        app_id: str = None,
        secret_required: bool = None,
        display_name: str = None,
        is_multi_tenant: bool = None,
        access_token_validity: int = None,
        refresh_token_validity: int = None,
        app_type: str = None,
        create_date: str = None,
        app_name: str = None,
        delegated_scope: UpdateApplicationResponseApplicationDelegatedScope = None,
        redirect_uris: UpdateApplicationResponseApplicationRedirectUris = None,
    ):
        self.update_date = update_date
        self.account_id = account_id
        self.app_id = app_id
        self.secret_required = secret_required
        self.display_name = display_name
        self.is_multi_tenant = is_multi_tenant
        self.access_token_validity = access_token_validity
        self.refresh_token_validity = refresh_token_validity
        self.app_type = app_type
        self.create_date = create_date
        self.app_name = app_name
        self.delegated_scope = delegated_scope
        self.redirect_uris = redirect_uris

    def validate(self):
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.secret_required, 'secret_required')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.is_multi_tenant, 'is_multi_tenant')
        self.validate_required(self.access_token_validity, 'access_token_validity')
        self.validate_required(self.refresh_token_validity, 'refresh_token_validity')
        self.validate_required(self.app_type, 'app_type')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.delegated_scope, 'delegated_scope')
        if self.delegated_scope:
            self.delegated_scope.validate()
        self.validate_required(self.redirect_uris, 'redirect_uris')
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DelegatedScope') is not None:
            temp_model = UpdateApplicationResponseApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('RedirectUris') is not None:
            temp_model = UpdateApplicationResponseApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        return self


class UpdateApplicationResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        application: UpdateApplicationResponseApplication = None,
    ):
        self.request_id = request_id
        self.application = application

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.application, 'application')
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateApplicationResponseApplication()
            self.application = temp_model.from_map(m['Application'])
        return self


class ListApplicationsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListApplicationsResponseApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        self.validate_required(self.description, 'description')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListApplicationsResponseApplicationsApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[ListApplicationsResponseApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        self.validate_required(self.predefined_scope, 'predefined_scope')
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListApplicationsResponseApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseApplicationsApplicationDelegatedScope(TeaModel):
    def __init__(
        self,
        predefined_scopes: ListApplicationsResponseApplicationsApplicationDelegatedScopePredefinedScopes = None,
    ):
        self.predefined_scopes = predefined_scopes

    def validate(self):
        self.validate_required(self.predefined_scopes, 'predefined_scopes')
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = ListApplicationsResponseApplicationsApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class ListApplicationsResponseApplicationsApplicationRedirectUris(TeaModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        # RedirectUri
        self.redirect_uri = redirect_uri

    def validate(self):
        self.validate_required(self.redirect_uri, 'redirect_uri')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class ListApplicationsResponseApplicationsApplication(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        account_id: str = None,
        app_id: str = None,
        secret_required: bool = None,
        display_name: str = None,
        is_multi_tenant: bool = None,
        access_token_validity: int = None,
        refresh_token_validity: int = None,
        app_type: str = None,
        create_date: str = None,
        app_name: str = None,
        delegated_scope: ListApplicationsResponseApplicationsApplicationDelegatedScope = None,
        redirect_uris: ListApplicationsResponseApplicationsApplicationRedirectUris = None,
    ):
        self.update_date = update_date
        self.account_id = account_id
        self.app_id = app_id
        self.secret_required = secret_required
        self.display_name = display_name
        self.is_multi_tenant = is_multi_tenant
        self.access_token_validity = access_token_validity
        self.refresh_token_validity = refresh_token_validity
        self.app_type = app_type
        self.create_date = create_date
        self.app_name = app_name
        self.delegated_scope = delegated_scope
        self.redirect_uris = redirect_uris

    def validate(self):
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.secret_required, 'secret_required')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.is_multi_tenant, 'is_multi_tenant')
        self.validate_required(self.access_token_validity, 'access_token_validity')
        self.validate_required(self.refresh_token_validity, 'refresh_token_validity')
        self.validate_required(self.app_type, 'app_type')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.delegated_scope, 'delegated_scope')
        if self.delegated_scope:
            self.delegated_scope.validate()
        self.validate_required(self.redirect_uris, 'redirect_uris')
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DelegatedScope') is not None:
            temp_model = ListApplicationsResponseApplicationsApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('RedirectUris') is not None:
            temp_model = ListApplicationsResponseApplicationsApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        return self


class ListApplicationsResponseApplications(TeaModel):
    def __init__(
        self,
        application: List[ListApplicationsResponseApplicationsApplication] = None,
    ):
        self.application = application

    def validate(self):
        self.validate_required(self.application, 'application')
        if self.application:
            for k in self.application:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListApplicationsResponseApplicationsApplication()
                self.application.append(temp_model.from_map(k))
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        applications: ListApplicationsResponseApplications = None,
    ):
        self.request_id = request_id
        self.applications = applications

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.applications, 'applications')
        if self.applications:
            self.applications.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListApplicationsResponseApplications()
            self.applications = temp_model.from_map(m['Applications'])
        return self


class GetApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        self.validate_required(self.description, 'description')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetApplicationResponseApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[GetApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        self.validate_required(self.predefined_scope, 'predefined_scope')
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = GetApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class GetApplicationResponseApplicationDelegatedScope(TeaModel):
    def __init__(
        self,
        predefined_scopes: GetApplicationResponseApplicationDelegatedScopePredefinedScopes = None,
    ):
        self.predefined_scopes = predefined_scopes

    def validate(self):
        self.validate_required(self.predefined_scopes, 'predefined_scopes')
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = GetApplicationResponseApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class GetApplicationResponseApplicationRedirectUris(TeaModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        # RedirectUri
        self.redirect_uri = redirect_uri

    def validate(self):
        self.validate_required(self.redirect_uri, 'redirect_uri')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class GetApplicationResponseApplication(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        account_id: str = None,
        app_id: str = None,
        secret_required: bool = None,
        display_name: str = None,
        is_multi_tenant: bool = None,
        access_token_validity: int = None,
        refresh_token_validity: int = None,
        app_type: str = None,
        create_date: str = None,
        app_name: str = None,
        delegated_scope: GetApplicationResponseApplicationDelegatedScope = None,
        redirect_uris: GetApplicationResponseApplicationRedirectUris = None,
    ):
        self.update_date = update_date
        self.account_id = account_id
        self.app_id = app_id
        self.secret_required = secret_required
        self.display_name = display_name
        self.is_multi_tenant = is_multi_tenant
        self.access_token_validity = access_token_validity
        self.refresh_token_validity = refresh_token_validity
        self.app_type = app_type
        self.create_date = create_date
        self.app_name = app_name
        self.delegated_scope = delegated_scope
        self.redirect_uris = redirect_uris

    def validate(self):
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.secret_required, 'secret_required')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.is_multi_tenant, 'is_multi_tenant')
        self.validate_required(self.access_token_validity, 'access_token_validity')
        self.validate_required(self.refresh_token_validity, 'refresh_token_validity')
        self.validate_required(self.app_type, 'app_type')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.delegated_scope, 'delegated_scope')
        if self.delegated_scope:
            self.delegated_scope.validate()
        self.validate_required(self.redirect_uris, 'redirect_uris')
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DelegatedScope') is not None:
            temp_model = GetApplicationResponseApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('RedirectUris') is not None:
            temp_model = GetApplicationResponseApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        return self


class GetApplicationResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        application: GetApplicationResponseApplication = None,
    ):
        self.request_id = request_id
        self.application = application

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.application, 'application')
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetApplicationResponseApplication()
            self.application = temp_model.from_map(m['Application'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class GetAppSecretRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
    ):
        self.app_id = app_id
        self.app_secret_id = app_secret_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_secret_id, 'app_secret_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        return self


class GetAppSecretResponseAppSecret(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_value: str = None,
        app_secret_id: str = None,
        create_date: str = None,
    ):
        self.app_id = app_id
        self.app_secret_value = app_secret_value
        self.app_secret_id = app_secret_id
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_secret_value, 'app_secret_value')
        self.validate_required(self.app_secret_id, 'app_secret_id')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_value is not None:
            result['AppSecretValue'] = self.app_secret_value
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretValue') is not None:
            self.app_secret_value = m.get('AppSecretValue')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class GetAppSecretResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_secret: GetAppSecretResponseAppSecret = None,
    ):
        self.request_id = request_id
        self.app_secret = app_secret

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.app_secret, 'app_secret')
        if self.app_secret:
            self.app_secret.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetAppSecretResponseAppSecret()
            self.app_secret = temp_model.from_map(m['AppSecret'])
        return self


class CreateAppSecretRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class CreateAppSecretResponseAppSecret(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_value: str = None,
        app_secret_id: str = None,
        create_date: str = None,
    ):
        self.app_id = app_id
        self.app_secret_value = app_secret_value
        self.app_secret_id = app_secret_id
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_secret_value, 'app_secret_value')
        self.validate_required(self.app_secret_id, 'app_secret_id')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_value is not None:
            result['AppSecretValue'] = self.app_secret_value
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretValue') is not None:
            self.app_secret_value = m.get('AppSecretValue')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreateAppSecretResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_secret: CreateAppSecretResponseAppSecret = None,
    ):
        self.request_id = request_id
        self.app_secret = app_secret

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.app_secret, 'app_secret')
        if self.app_secret:
            self.app_secret.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateAppSecretResponseAppSecret()
            self.app_secret = temp_model.from_map(m['AppSecret'])
        return self


class ListPredefinedScopesRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
    ):
        self.app_type = app_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class ListPredefinedScopesResponsePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        self.validate_required(self.description, 'description')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListPredefinedScopesResponsePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[ListPredefinedScopesResponsePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        self.validate_required(self.predefined_scope, 'predefined_scope')
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListPredefinedScopesResponsePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class ListPredefinedScopesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        predefined_scopes: ListPredefinedScopesResponsePredefinedScopes = None,
    ):
        self.request_id = request_id
        self.predefined_scopes = predefined_scopes

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.predefined_scopes, 'predefined_scopes')
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PredefinedScopes') is not None:
            temp_model = ListPredefinedScopesResponsePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        app_type: str = None,
        redirect_uris: str = None,
        secret_required: bool = None,
        access_token_validity: int = None,
        refresh_token_validity: int = None,
        predefined_scopes: str = None,
        is_multi_tenant: bool = None,
        app_name: str = None,
    ):
        self.display_name = display_name
        self.app_type = app_type
        self.redirect_uris = redirect_uris
        self.secret_required = secret_required
        self.access_token_validity = access_token_validity
        self.refresh_token_validity = refresh_token_validity
        self.predefined_scopes = predefined_scopes
        self.is_multi_tenant = is_multi_tenant
        self.app_name = app_name

    def validate(self):
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.app_type, 'app_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
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
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
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
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class CreateApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        self.validate_required(self.description, 'description')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateApplicationResponseApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[CreateApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        self.validate_required(self.predefined_scope, 'predefined_scope')
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = CreateApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class CreateApplicationResponseApplicationDelegatedScope(TeaModel):
    def __init__(
        self,
        predefined_scopes: CreateApplicationResponseApplicationDelegatedScopePredefinedScopes = None,
    ):
        self.predefined_scopes = predefined_scopes

    def validate(self):
        self.validate_required(self.predefined_scopes, 'predefined_scopes')
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = CreateApplicationResponseApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class CreateApplicationResponseApplicationRedirectUris(TeaModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        # RedirectUri
        self.redirect_uri = redirect_uri

    def validate(self):
        self.validate_required(self.redirect_uri, 'redirect_uri')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class CreateApplicationResponseApplication(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        account_id: str = None,
        app_id: str = None,
        secret_required: bool = None,
        display_name: str = None,
        is_multi_tenant: bool = None,
        access_token_validity: int = None,
        refresh_token_validity: int = None,
        app_type: str = None,
        create_date: str = None,
        app_name: str = None,
        delegated_scope: CreateApplicationResponseApplicationDelegatedScope = None,
        redirect_uris: CreateApplicationResponseApplicationRedirectUris = None,
    ):
        self.update_date = update_date
        self.account_id = account_id
        self.app_id = app_id
        self.secret_required = secret_required
        self.display_name = display_name
        self.is_multi_tenant = is_multi_tenant
        self.access_token_validity = access_token_validity
        self.refresh_token_validity = refresh_token_validity
        self.app_type = app_type
        self.create_date = create_date
        self.app_name = app_name
        self.delegated_scope = delegated_scope
        self.redirect_uris = redirect_uris

    def validate(self):
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.secret_required, 'secret_required')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.is_multi_tenant, 'is_multi_tenant')
        self.validate_required(self.access_token_validity, 'access_token_validity')
        self.validate_required(self.refresh_token_validity, 'refresh_token_validity')
        self.validate_required(self.app_type, 'app_type')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.delegated_scope, 'delegated_scope')
        if self.delegated_scope:
            self.delegated_scope.validate()
        self.validate_required(self.redirect_uris, 'redirect_uris')
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DelegatedScope') is not None:
            temp_model = CreateApplicationResponseApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('RedirectUris') is not None:
            temp_model = CreateApplicationResponseApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        application: CreateApplicationResponseApplication = None,
    ):
        self.request_id = request_id
        self.application = application

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.application, 'application')
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateApplicationResponseApplication()
            self.application = temp_model.from_map(m['Application'])
        return self


class DeleteAppSecretRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
    ):
        self.app_id = app_id
        self.app_secret_id = app_secret_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_secret_id, 'app_secret_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        return self


class DeleteAppSecretResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class ListAppSecretIdsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListAppSecretIdsResponseAppSecretsAppSecret(TeaModel):
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
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_secret_id, 'app_secret_id')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListAppSecretIdsResponseAppSecrets(TeaModel):
    def __init__(
        self,
        app_secret: List[ListAppSecretIdsResponseAppSecretsAppSecret] = None,
    ):
        self.app_secret = app_secret

    def validate(self):
        self.validate_required(self.app_secret, 'app_secret')
        if self.app_secret:
            for k in self.app_secret:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListAppSecretIdsResponseAppSecretsAppSecret()
                self.app_secret.append(temp_model.from_map(k))
        return self


class ListAppSecretIdsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_secrets: ListAppSecretIdsResponseAppSecrets = None,
    ):
        self.request_id = request_id
        self.app_secrets = app_secrets

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.app_secrets, 'app_secrets')
        if self.app_secrets:
            self.app_secrets.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_secrets is not None:
            result['AppSecrets'] = self.app_secrets.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppSecrets') is not None:
            temp_model = ListAppSecretIdsResponseAppSecrets()
            self.app_secrets = temp_model.from_map(m['AppSecrets'])
        return self


class GenerateCredentialReportRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GenerateCredentialReportResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state: str = None,
    ):
        self.request_id = request_id
        self.state = state

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.state, 'state')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetCredentialReportRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetCredentialReportResponse(TeaModel):
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
        self.validate_required(self.generated_time, 'generated_time')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.content, 'content')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
    ):
        self.user_principal_name = user_principal_name
        self.user_id = user_id
        self.new_user_principal_name = new_user_principal_name
        self.new_display_name = new_display_name
        self.new_mobile_phone = new_mobile_phone
        self.new_email = new_email
        self.new_comments = new_comments

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        return self


class UpdateUserResponseUser(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        email: str = None,
        comments: str = None,
        user_id: str = None,
        last_login_date: str = None,
        display_name: str = None,
        user_principal_name: str = None,
        create_date: str = None,
        mobile_phone: str = None,
    ):
        self.update_date = update_date
        self.email = email
        self.comments = comments
        self.user_id = user_id
        self.last_login_date = last_login_date
        self.display_name = display_name
        self.user_principal_name = user_principal_name
        self.create_date = create_date
        self.mobile_phone = mobile_phone

    def validate(self):
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.email, 'email')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.last_login_date, 'last_login_date')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.mobile_phone, 'mobile_phone')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.email is not None:
            result['Email'] = self.email
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user: UpdateUserResponseUser = None,
    ):
        self.request_id = request_id
        self.user = user

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.user, 'user')
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('User') is not None:
            temp_model = UpdateUserResponseUser()
            self.user = temp_model.from_map(m['User'])
        return self


class UpdateSAMLProviderRequest(TeaModel):
    def __init__(
        self,
        samlprovider_name: str = None,
        new_description: str = None,
        new_encoded_samlmetadata_document: str = None,
    ):
        self.samlprovider_name = samlprovider_name
        self.new_description = new_description
        self.new_encoded_samlmetadata_document = new_encoded_samlmetadata_document

    def validate(self):
        self.validate_required(self.samlprovider_name, 'samlprovider_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_encoded_samlmetadata_document is not None:
            result['NewEncodedSAMLMetadataDocument'] = self.new_encoded_samlmetadata_document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('NewEncodedSAMLMetadataDocument') is not None:
            self.new_encoded_samlmetadata_document = m.get('NewEncodedSAMLMetadataDocument')
        return self


class UpdateSAMLProviderResponseSAMLProvider(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        samlprovider_name: str = None,
        description: str = None,
        arn: str = None,
        create_date: str = None,
    ):
        self.update_date = update_date
        self.samlprovider_name = samlprovider_name
        self.description = description
        self.arn = arn
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.samlprovider_name, 'samlprovider_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.description is not None:
            result['Description'] = self.description
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class UpdateSAMLProviderResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlprovider: UpdateSAMLProviderResponseSAMLProvider = None,
    ):
        self.request_id = request_id
        self.samlprovider = samlprovider

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.samlprovider, 'samlprovider')
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateSAMLProviderResponseSAMLProvider()
            self.samlprovider = temp_model.from_map(m['SAMLProvider'])
        return self


class UpdateLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        password: str = None,
        password_reset_required: bool = None,
        mfabind_required: bool = None,
        status: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.password = password
        self.password_reset_required = password_reset_required
        self.mfabind_required = mfabind_required
        self.status = status

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.password is not None:
            result['Password'] = self.password
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateLoginProfileResponseLoginProfile(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_date: str = None,
        password_reset_required: bool = None,
        user_principal_name: str = None,
        mfabind_required: bool = None,
    ):
        self.status = status
        self.update_date = update_date
        self.password_reset_required = password_reset_required
        self.user_principal_name = user_principal_name
        self.mfabind_required = mfabind_required

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.password_reset_required, 'password_reset_required')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.mfabind_required, 'mfabind_required')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        return self


class UpdateLoginProfileResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        login_profile: UpdateLoginProfileResponseLoginProfile = None,
    ):
        self.request_id = request_id
        self.login_profile = login_profile

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.login_profile, 'login_profile')
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateLoginProfileResponseLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(
        self,
        new_comments: str = None,
        new_display_name: str = None,
        new_group_name: str = None,
        group_name: str = None,
    ):
        self.new_comments = new_comments
        self.new_display_name = new_display_name
        self.new_group_name = new_group_name
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_comments is not None:
            result['NewComments'] = self.new_comments
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.new_group_name is not None:
            result['NewGroupName'] = self.new_group_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewComments') is not None:
            self.new_comments = m.get('NewComments')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('NewGroupName') is not None:
            self.new_group_name = m.get('NewGroupName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class UpdateGroupResponseGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        update_date: str = None,
        comments: str = None,
        display_name: str = None,
        create_date: str = None,
        group_id: str = None,
    ):
        self.group_name = group_name
        self.update_date = update_date
        self.comments = comments
        self.display_name = display_name
        self.create_date = create_date
        self.group_id = group_id

    def validate(self):
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class UpdateGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group: UpdateGroupResponseGroup = None,
    ):
        self.request_id = request_id
        self.group = group

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group, 'group')
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group is not None:
            result['Group'] = self.group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Group') is not None:
            temp_model = UpdateGroupResponseGroup()
            self.group = temp_model.from_map(m['Group'])
        return self


class UpdateAccessKeyRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        user_access_key_id: str = None,
        status: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.user_access_key_id = user_access_key_id
        self.status = status

    def validate(self):
        self.validate_required(self.user_access_key_id, 'user_access_key_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateAccessKeyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class UnbindMFADeviceRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        self.user_principal_name = user_principal_name

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UnbindMFADeviceResponseMFADevice(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
    ):
        self.serial_number = serial_number

    def validate(self):
        self.validate_required(self.serial_number, 'serial_number')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class UnbindMFADeviceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        mfadevice: UnbindMFADeviceResponseMFADevice = None,
    ):
        self.request_id = request_id
        self.mfadevice = mfadevice

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.mfadevice, 'mfadevice')
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MFADevice') is not None:
            temp_model = UnbindMFADeviceResponseMFADevice()
            self.mfadevice = temp_model.from_map(m['MFADevice'])
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
    ):
        self.enable_save_mfaticket = enable_save_mfaticket
        self.allow_user_to_change_password = allow_user_to_change_password
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices
        self.login_session_duration = login_session_duration
        self.login_network_masks = login_network_masks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        return self


class SetSecurityPreferenceResponseSecurityPreferenceLoginProfilePreference(TeaModel):
    def __init__(
        self,
        login_session_duration: int = None,
        login_network_masks: str = None,
        allow_user_to_change_password: bool = None,
        enable_save_mfaticket: bool = None,
    ):
        self.login_session_duration = login_session_duration
        self.login_network_masks = login_network_masks
        self.allow_user_to_change_password = allow_user_to_change_password
        self.enable_save_mfaticket = enable_save_mfaticket

    def validate(self):
        self.validate_required(self.login_session_duration, 'login_session_duration')
        self.validate_required(self.login_network_masks, 'login_network_masks')
        self.validate_required(self.allow_user_to_change_password, 'allow_user_to_change_password')
        self.validate_required(self.enable_save_mfaticket, 'enable_save_mfaticket')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        return self


class SetSecurityPreferenceResponseSecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_access_keys: bool = None,
    ):
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys

    def validate(self):
        self.validate_required(self.allow_user_to_manage_access_keys, 'allow_user_to_manage_access_keys')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        return self


class SetSecurityPreferenceResponseSecurityPreferenceMFAPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_mfadevices: bool = None,
    ):
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices

    def validate(self):
        self.validate_required(self.allow_user_to_manage_mfadevices, 'allow_user_to_manage_mfadevices')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        return self


class SetSecurityPreferenceResponseSecurityPreference(TeaModel):
    def __init__(
        self,
        login_profile_preference: SetSecurityPreferenceResponseSecurityPreferenceLoginProfilePreference = None,
        access_key_preference: SetSecurityPreferenceResponseSecurityPreferenceAccessKeyPreference = None,
        mfapreference: SetSecurityPreferenceResponseSecurityPreferenceMFAPreference = None,
    ):
        self.login_profile_preference = login_profile_preference
        self.access_key_preference = access_key_preference
        self.mfapreference = mfapreference

    def validate(self):
        self.validate_required(self.login_profile_preference, 'login_profile_preference')
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        self.validate_required(self.access_key_preference, 'access_key_preference')
        if self.access_key_preference:
            self.access_key_preference.validate()
        self.validate_required(self.mfapreference, 'mfapreference')
        if self.mfapreference:
            self.mfapreference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()
        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginProfilePreference') is not None:
            temp_model = SetSecurityPreferenceResponseSecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(m['LoginProfilePreference'])
        if m.get('AccessKeyPreference') is not None:
            temp_model = SetSecurityPreferenceResponseSecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(m['AccessKeyPreference'])
        if m.get('MFAPreference') is not None:
            temp_model = SetSecurityPreferenceResponseSecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(m['MFAPreference'])
        return self


class SetSecurityPreferenceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_preference: SetSecurityPreferenceResponseSecurityPreference = None,
    ):
        self.request_id = request_id
        self.security_preference = security_preference

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.security_preference, 'security_preference')
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPreference') is not None:
            temp_model = SetSecurityPreferenceResponseSecurityPreference()
            self.security_preference = temp_model.from_map(m['SecurityPreference'])
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

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        return self


class SetPasswordPolicyResponsePasswordPolicy(TeaModel):
    def __init__(
        self,
        minimum_password_length: int = None,
        hard_expire: bool = None,
        require_lowercase_characters: bool = None,
        require_numbers: bool = None,
        max_login_attemps: int = None,
        max_password_age: int = None,
        password_not_contain_user_name: bool = None,
        password_reuse_prevention: int = None,
        require_uppercase_characters: bool = None,
        minimum_password_different_character: int = None,
        require_symbols: bool = None,
    ):
        self.minimum_password_length = minimum_password_length
        self.hard_expire = hard_expire
        self.require_lowercase_characters = require_lowercase_characters
        self.require_numbers = require_numbers
        self.max_login_attemps = max_login_attemps
        self.max_password_age = max_password_age
        self.password_not_contain_user_name = password_not_contain_user_name
        self.password_reuse_prevention = password_reuse_prevention
        self.require_uppercase_characters = require_uppercase_characters
        self.minimum_password_different_character = minimum_password_different_character
        self.require_symbols = require_symbols

    def validate(self):
        self.validate_required(self.minimum_password_length, 'minimum_password_length')
        self.validate_required(self.hard_expire, 'hard_expire')
        self.validate_required(self.require_lowercase_characters, 'require_lowercase_characters')
        self.validate_required(self.require_numbers, 'require_numbers')
        self.validate_required(self.max_login_attemps, 'max_login_attemps')
        self.validate_required(self.max_password_age, 'max_password_age')
        self.validate_required(self.password_not_contain_user_name, 'password_not_contain_user_name')
        self.validate_required(self.password_reuse_prevention, 'password_reuse_prevention')
        self.validate_required(self.require_uppercase_characters, 'require_uppercase_characters')
        self.validate_required(self.minimum_password_different_character, 'minimum_password_different_character')
        self.validate_required(self.require_symbols, 'require_symbols')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        if self.minimum_password_different_character is not None:
            result['MinimumPasswordDifferentCharacter'] = self.minimum_password_different_character
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        if m.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = m.get('MinimumPasswordDifferentCharacter')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        return self


class SetPasswordPolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        password_policy: SetPasswordPolicyResponsePasswordPolicy = None,
    ):
        self.request_id = request_id
        self.password_policy = password_policy

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.password_policy, 'password_policy')
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = SetPasswordPolicyResponsePasswordPolicy()
            self.password_policy = temp_model.from_map(m['PasswordPolicy'])
        return self


class RemoveUserFromGroupRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        group_name: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class RemoveUserFromGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class ListVirtualMFADevicesRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListVirtualMFADevicesResponseVirtualMFADevicesVirtualMFADeviceUser(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        display_name: str = None,
        user_principal_name: str = None,
    ):
        self.user_id = user_id
        self.display_name = display_name
        self.user_principal_name = user_principal_name

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListVirtualMFADevicesResponseVirtualMFADevicesVirtualMFADevice(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        activate_date: str = None,
        user: ListVirtualMFADevicesResponseVirtualMFADevicesVirtualMFADeviceUser = None,
    ):
        self.serial_number = serial_number
        self.activate_date = activate_date
        self.user = user

    def validate(self):
        self.validate_required(self.serial_number, 'serial_number')
        self.validate_required(self.activate_date, 'activate_date')
        self.validate_required(self.user, 'user')
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.activate_date is not None:
            result['ActivateDate'] = self.activate_date
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('ActivateDate') is not None:
            self.activate_date = m.get('ActivateDate')
        if m.get('User') is not None:
            temp_model = ListVirtualMFADevicesResponseVirtualMFADevicesVirtualMFADeviceUser()
            self.user = temp_model.from_map(m['User'])
        return self


class ListVirtualMFADevicesResponseVirtualMFADevices(TeaModel):
    def __init__(
        self,
        virtual_mfadevice: List[ListVirtualMFADevicesResponseVirtualMFADevicesVirtualMFADevice] = None,
    ):
        self.virtual_mfadevice = virtual_mfadevice

    def validate(self):
        self.validate_required(self.virtual_mfadevice, 'virtual_mfadevice')
        if self.virtual_mfadevice:
            for k in self.virtual_mfadevice:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListVirtualMFADevicesResponseVirtualMFADevicesVirtualMFADevice()
                self.virtual_mfadevice.append(temp_model.from_map(k))
        return self


class ListVirtualMFADevicesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_truncated: bool = None,
        marker: str = None,
        virtual_mfadevices: ListVirtualMFADevicesResponseVirtualMFADevices = None,
    ):
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker
        self.virtual_mfadevices = virtual_mfadevices

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_truncated, 'is_truncated')
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.virtual_mfadevices, 'virtual_mfadevices')
        if self.virtual_mfadevices:
            self.virtual_mfadevices.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.virtual_mfadevices is not None:
            result['VirtualMFADevices'] = self.virtual_mfadevices.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('VirtualMFADevices') is not None:
            temp_model = ListVirtualMFADevicesResponseVirtualMFADevices()
            self.virtual_mfadevices = temp_model.from_map(m['VirtualMFADevices'])
        return self


class ListUsersForGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        marker: str = None,
        max_items: int = None,
    ):
        self.group_name = group_name
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListUsersForGroupResponseUsersUser(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        display_name: str = None,
        user_principal_name: str = None,
        join_date: str = None,
    ):
        self.user_id = user_id
        self.display_name = display_name
        self.user_principal_name = user_principal_name
        self.join_date = join_date

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.join_date, 'join_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.join_date is not None:
            result['JoinDate'] = self.join_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('JoinDate') is not None:
            self.join_date = m.get('JoinDate')
        return self


class ListUsersForGroupResponseUsers(TeaModel):
    def __init__(
        self,
        user: List[ListUsersForGroupResponseUsersUser] = None,
    ):
        self.user = user

    def validate(self):
        self.validate_required(self.user, 'user')
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListUsersForGroupResponseUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersForGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_truncated: bool = None,
        marker: str = None,
        users: ListUsersForGroupResponseUsers = None,
    ):
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker
        self.users = users

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_truncated, 'is_truncated')
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.users, 'users')
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListUsersForGroupResponseUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListUsersResponseUsersUser(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        email: str = None,
        comments: str = None,
        user_id: str = None,
        last_login_date: str = None,
        display_name: str = None,
        user_principal_name: str = None,
        create_date: str = None,
        mobile_phone: str = None,
    ):
        self.update_date = update_date
        self.email = email
        self.comments = comments
        self.user_id = user_id
        self.last_login_date = last_login_date
        self.display_name = display_name
        self.user_principal_name = user_principal_name
        self.create_date = create_date
        self.mobile_phone = mobile_phone

    def validate(self):
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.email, 'email')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.last_login_date, 'last_login_date')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.mobile_phone, 'mobile_phone')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.email is not None:
            result['Email'] = self.email
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        return self


class ListUsersResponseUsers(TeaModel):
    def __init__(
        self,
        user: List[ListUsersResponseUsersUser] = None,
    ):
        self.user = user

    def validate(self):
        self.validate_required(self.user, 'user')
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListUsersResponseUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_truncated: bool = None,
        marker: str = None,
        users: ListUsersResponseUsers = None,
    ):
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker
        self.users = users

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_truncated, 'is_truncated')
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.users, 'users')
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListUsersResponseUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListSAMLProvidersRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListSAMLProvidersResponseSAMLProvidersSAMLProvider(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        samlprovider_name: str = None,
        description: str = None,
        arn: str = None,
        create_date: str = None,
    ):
        self.update_date = update_date
        self.samlprovider_name = samlprovider_name
        self.description = description
        self.arn = arn
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.samlprovider_name, 'samlprovider_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.description is not None:
            result['Description'] = self.description
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListSAMLProvidersResponseSAMLProviders(TeaModel):
    def __init__(
        self,
        samlprovider: List[ListSAMLProvidersResponseSAMLProvidersSAMLProvider] = None,
    ):
        self.samlprovider = samlprovider

    def validate(self):
        self.validate_required(self.samlprovider, 'samlprovider')
        if self.samlprovider:
            for k in self.samlprovider:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListSAMLProvidersResponseSAMLProvidersSAMLProvider()
                self.samlprovider.append(temp_model.from_map(k))
        return self


class ListSAMLProvidersResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_truncated: bool = None,
        marker: str = None,
        samlproviders: ListSAMLProvidersResponseSAMLProviders = None,
    ):
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker
        self.samlproviders = samlproviders

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_truncated, 'is_truncated')
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.samlproviders, 'samlproviders')
        if self.samlproviders:
            self.samlproviders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.samlproviders is not None:
            result['SAMLProviders'] = self.samlproviders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('SAMLProviders') is not None:
            temp_model = ListSAMLProvidersResponseSAMLProviders()
            self.samlproviders = temp_model.from_map(m['SAMLProviders'])
        return self


class ListGroupsForUserRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        self.user_principal_name = user_principal_name

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListGroupsForUserResponseGroupsGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        comments: str = None,
        display_name: str = None,
        join_date: str = None,
        group_id: str = None,
    ):
        self.group_name = group_name
        self.comments = comments
        self.display_name = display_name
        self.join_date = join_date
        self.group_id = group_id

    def validate(self):
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.join_date, 'join_date')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.join_date is not None:
            result['JoinDate'] = self.join_date
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JoinDate') is not None:
            self.join_date = m.get('JoinDate')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class ListGroupsForUserResponseGroups(TeaModel):
    def __init__(
        self,
        group: List[ListGroupsForUserResponseGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        self.validate_required(self.group, 'group')
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListGroupsForUserResponseGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListGroupsForUserResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        groups: ListGroupsForUserResponseGroups = None,
    ):
        self.request_id = request_id
        self.groups = groups

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.groups, 'groups')
        if self.groups:
            self.groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListGroupsForUserResponseGroups()
            self.groups = temp_model.from_map(m['Groups'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListGroupsResponseGroupsGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        update_date: str = None,
        comments: str = None,
        display_name: str = None,
        create_date: str = None,
        group_id: str = None,
    ):
        self.group_name = group_name
        self.update_date = update_date
        self.comments = comments
        self.display_name = display_name
        self.create_date = create_date
        self.group_id = group_id

    def validate(self):
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class ListGroupsResponseGroups(TeaModel):
    def __init__(
        self,
        group: List[ListGroupsResponseGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        self.validate_required(self.group, 'group')
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListGroupsResponseGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListGroupsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_truncated: bool = None,
        marker: str = None,
        groups: ListGroupsResponseGroups = None,
    ):
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker
        self.groups = groups

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_truncated, 'is_truncated')
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.groups, 'groups')
        if self.groups:
            self.groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('Groups') is not None:
            temp_model = ListGroupsResponseGroups()
            self.groups = temp_model.from_map(m['Groups'])
        return self


class ListAccessKeysRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListAccessKeysResponseAccessKeysAccessKey(TeaModel):
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
        self.validate_required(self.status, 'status')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.access_key_id, 'access_key_id')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListAccessKeysResponseAccessKeys(TeaModel):
    def __init__(
        self,
        access_key: List[ListAccessKeysResponseAccessKeysAccessKey] = None,
    ):
        self.access_key = access_key

    def validate(self):
        self.validate_required(self.access_key, 'access_key')
        if self.access_key:
            for k in self.access_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListAccessKeysResponseAccessKeysAccessKey()
                self.access_key.append(temp_model.from_map(k))
        return self


class ListAccessKeysResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        access_keys: ListAccessKeysResponseAccessKeys = None,
    ):
        self.request_id = request_id
        self.access_keys = access_keys

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.access_keys, 'access_keys')
        if self.access_keys:
            self.access_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_keys is not None:
            result['AccessKeys'] = self.access_keys.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessKeys') is not None:
            temp_model = ListAccessKeysResponseAccessKeys()
            self.access_keys = temp_model.from_map(m['AccessKeys'])
        return self


class GetUserMFAInfoRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetUserMFAInfoResponseMFADevice(TeaModel):
    def __init__(
        self,
        type: str = None,
        serial_number: str = None,
    ):
        self.type = type
        self.serial_number = serial_number

    def validate(self):
        self.validate_required(self.type, 'type')
        self.validate_required(self.serial_number, 'serial_number')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class GetUserMFAInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_mfaenable: bool = None,
        mfadevice: GetUserMFAInfoResponseMFADevice = None,
    ):
        self.request_id = request_id
        self.is_mfaenable = is_mfaenable
        self.mfadevice = mfadevice

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_mfaenable, 'is_mfaenable')
        self.validate_required(self.mfadevice, 'mfadevice')
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_mfaenable is not None:
            result['IsMFAEnable'] = self.is_mfaenable
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsMFAEnable') is not None:
            self.is_mfaenable = m.get('IsMFAEnable')
        if m.get('MFADevice') is not None:
            temp_model = GetUserMFAInfoResponseMFADevice()
            self.mfadevice = temp_model.from_map(m['MFADevice'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        user_id: str = None,
        user_access_key_id: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.user_id = user_id
        self.user_access_key_id = user_access_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        return self


class GetUserResponseUser(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        email: str = None,
        comments: str = None,
        user_id: str = None,
        last_login_date: str = None,
        display_name: str = None,
        user_principal_name: str = None,
        create_date: str = None,
        mobile_phone: str = None,
    ):
        self.update_date = update_date
        self.email = email
        self.comments = comments
        self.user_id = user_id
        self.last_login_date = last_login_date
        self.display_name = display_name
        self.user_principal_name = user_principal_name
        self.create_date = create_date
        self.mobile_phone = mobile_phone

    def validate(self):
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.email, 'email')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.last_login_date, 'last_login_date')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.mobile_phone, 'mobile_phone')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.email is not None:
            result['Email'] = self.email
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user: GetUserResponseUser = None,
    ):
        self.request_id = request_id
        self.user = user

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.user, 'user')
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('User') is not None:
            temp_model = GetUserResponseUser()
            self.user = temp_model.from_map(m['User'])
        return self


class GetSecurityPreferenceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSecurityPreferenceResponseSecurityPreferenceLoginProfilePreference(TeaModel):
    def __init__(
        self,
        login_session_duration: int = None,
        login_network_masks: str = None,
        allow_user_to_change_password: bool = None,
        enable_save_mfaticket: bool = None,
    ):
        self.login_session_duration = login_session_duration
        self.login_network_masks = login_network_masks
        self.allow_user_to_change_password = allow_user_to_change_password
        self.enable_save_mfaticket = enable_save_mfaticket

    def validate(self):
        self.validate_required(self.login_session_duration, 'login_session_duration')
        self.validate_required(self.login_network_masks, 'login_network_masks')
        self.validate_required(self.allow_user_to_change_password, 'allow_user_to_change_password')
        self.validate_required(self.enable_save_mfaticket, 'enable_save_mfaticket')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        return self


class GetSecurityPreferenceResponseSecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_access_keys: bool = None,
    ):
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys

    def validate(self):
        self.validate_required(self.allow_user_to_manage_access_keys, 'allow_user_to_manage_access_keys')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        return self


class GetSecurityPreferenceResponseSecurityPreferenceMFAPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_mfadevices: bool = None,
    ):
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices

    def validate(self):
        self.validate_required(self.allow_user_to_manage_mfadevices, 'allow_user_to_manage_mfadevices')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        return self


class GetSecurityPreferenceResponseSecurityPreference(TeaModel):
    def __init__(
        self,
        login_profile_preference: GetSecurityPreferenceResponseSecurityPreferenceLoginProfilePreference = None,
        access_key_preference: GetSecurityPreferenceResponseSecurityPreferenceAccessKeyPreference = None,
        mfapreference: GetSecurityPreferenceResponseSecurityPreferenceMFAPreference = None,
    ):
        self.login_profile_preference = login_profile_preference
        self.access_key_preference = access_key_preference
        self.mfapreference = mfapreference

    def validate(self):
        self.validate_required(self.login_profile_preference, 'login_profile_preference')
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        self.validate_required(self.access_key_preference, 'access_key_preference')
        if self.access_key_preference:
            self.access_key_preference.validate()
        self.validate_required(self.mfapreference, 'mfapreference')
        if self.mfapreference:
            self.mfapreference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()
        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginProfilePreference') is not None:
            temp_model = GetSecurityPreferenceResponseSecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(m['LoginProfilePreference'])
        if m.get('AccessKeyPreference') is not None:
            temp_model = GetSecurityPreferenceResponseSecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(m['AccessKeyPreference'])
        if m.get('MFAPreference') is not None:
            temp_model = GetSecurityPreferenceResponseSecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(m['MFAPreference'])
        return self


class GetSecurityPreferenceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_preference: GetSecurityPreferenceResponseSecurityPreference = None,
    ):
        self.request_id = request_id
        self.security_preference = security_preference

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.security_preference, 'security_preference')
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPreference') is not None:
            temp_model = GetSecurityPreferenceResponseSecurityPreference()
            self.security_preference = temp_model.from_map(m['SecurityPreference'])
        return self


class GetSAMLProviderRequest(TeaModel):
    def __init__(
        self,
        samlprovider_name: str = None,
    ):
        self.samlprovider_name = samlprovider_name

    def validate(self):
        self.validate_required(self.samlprovider_name, 'samlprovider_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        return self


class GetSAMLProviderResponseSAMLProvider(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        samlprovider_name: str = None,
        description: str = None,
        encoded_samlmetadata_document: str = None,
        arn: str = None,
        create_date: str = None,
    ):
        self.update_date = update_date
        self.samlprovider_name = samlprovider_name
        self.description = description
        self.encoded_samlmetadata_document = encoded_samlmetadata_document
        self.arn = arn
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.samlprovider_name, 'samlprovider_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.encoded_samlmetadata_document, 'encoded_samlmetadata_document')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.description is not None:
            result['Description'] = self.description
        if self.encoded_samlmetadata_document is not None:
            result['EncodedSAMLMetadataDocument'] = self.encoded_samlmetadata_document
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncodedSAMLMetadataDocument') is not None:
            self.encoded_samlmetadata_document = m.get('EncodedSAMLMetadataDocument')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class GetSAMLProviderResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlprovider: GetSAMLProviderResponseSAMLProvider = None,
    ):
        self.request_id = request_id
        self.samlprovider = samlprovider

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.samlprovider, 'samlprovider')
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetSAMLProviderResponseSAMLProvider()
            self.samlprovider = temp_model.from_map(m['SAMLProvider'])
        return self


class GetPasswordPolicyRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPasswordPolicyResponsePasswordPolicy(TeaModel):
    def __init__(
        self,
        minimum_password_length: int = None,
        hard_expire: bool = None,
        require_lowercase_characters: bool = None,
        require_numbers: bool = None,
        max_login_attemps: int = None,
        max_password_age: int = None,
        password_not_contain_user_name: bool = None,
        password_reuse_prevention: int = None,
        require_uppercase_characters: bool = None,
        minimum_password_different_character: int = None,
        require_symbols: bool = None,
    ):
        self.minimum_password_length = minimum_password_length
        self.hard_expire = hard_expire
        self.require_lowercase_characters = require_lowercase_characters
        self.require_numbers = require_numbers
        self.max_login_attemps = max_login_attemps
        self.max_password_age = max_password_age
        self.password_not_contain_user_name = password_not_contain_user_name
        self.password_reuse_prevention = password_reuse_prevention
        self.require_uppercase_characters = require_uppercase_characters
        self.minimum_password_different_character = minimum_password_different_character
        self.require_symbols = require_symbols

    def validate(self):
        self.validate_required(self.minimum_password_length, 'minimum_password_length')
        self.validate_required(self.hard_expire, 'hard_expire')
        self.validate_required(self.require_lowercase_characters, 'require_lowercase_characters')
        self.validate_required(self.require_numbers, 'require_numbers')
        self.validate_required(self.max_login_attemps, 'max_login_attemps')
        self.validate_required(self.max_password_age, 'max_password_age')
        self.validate_required(self.password_not_contain_user_name, 'password_not_contain_user_name')
        self.validate_required(self.password_reuse_prevention, 'password_reuse_prevention')
        self.validate_required(self.require_uppercase_characters, 'require_uppercase_characters')
        self.validate_required(self.minimum_password_different_character, 'minimum_password_different_character')
        self.validate_required(self.require_symbols, 'require_symbols')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        if self.minimum_password_different_character is not None:
            result['MinimumPasswordDifferentCharacter'] = self.minimum_password_different_character
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        if m.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = m.get('MinimumPasswordDifferentCharacter')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        return self


class GetPasswordPolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        password_policy: GetPasswordPolicyResponsePasswordPolicy = None,
    ):
        self.request_id = request_id
        self.password_policy = password_policy

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.password_policy, 'password_policy')
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetPasswordPolicyResponsePasswordPolicy()
            self.password_policy = temp_model.from_map(m['PasswordPolicy'])
        return self


class GetLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        self.user_principal_name = user_principal_name

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetLoginProfileResponseLoginProfile(TeaModel):
    def __init__(
        self,
        status: str = None,
        last_login_time: str = None,
        update_date: str = None,
        password_reset_required: bool = None,
        user_principal_name: str = None,
        mfabind_required: bool = None,
    ):
        self.status = status
        self.last_login_time = last_login_time
        self.update_date = update_date
        self.password_reset_required = password_reset_required
        self.user_principal_name = user_principal_name
        self.mfabind_required = mfabind_required

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.last_login_time, 'last_login_time')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.password_reset_required, 'password_reset_required')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.mfabind_required, 'mfabind_required')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        return self


class GetLoginProfileResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        login_profile: GetLoginProfileResponseLoginProfile = None,
    ):
        self.request_id = request_id
        self.login_profile = login_profile

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.login_profile, 'login_profile')
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetLoginProfileResponseLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        return self


class GetGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
    ):
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetGroupResponseGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        update_date: str = None,
        comments: str = None,
        display_name: str = None,
        create_date: str = None,
        group_id: str = None,
    ):
        self.group_name = group_name
        self.update_date = update_date
        self.comments = comments
        self.display_name = display_name
        self.create_date = create_date
        self.group_id = group_id

    def validate(self):
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class GetGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group: GetGroupResponseGroup = None,
    ):
        self.request_id = request_id
        self.group = group

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group, 'group')
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group is not None:
            result['Group'] = self.group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Group') is not None:
            temp_model = GetGroupResponseGroup()
            self.group = temp_model.from_map(m['Group'])
        return self


class GetDefaultDomainRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDefaultDomainResponse(TeaModel):
    def __init__(
        self,
        default_domain_name: str = None,
        request_id: str = None,
    ):
        self.default_domain_name = default_domain_name
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.default_domain_name, 'default_domain_name')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetAccountSummaryRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAccountSummaryResponseSummaryMap(TeaModel):
    def __init__(
        self,
        policies: int = None,
        groups_per_user_quota: int = None,
        attached_policies_per_user_quota: int = None,
        roles: int = None,
        users: int = None,
        roles_quota: int = None,
        virtual_mfadevices_quota: int = None,
        policies_quota: int = None,
        attached_system_policies_per_group_quota: int = None,
        mfadevices_in_use: int = None,
        access_keys_per_user_quota: int = None,
        versions_per_policy_quota: int = None,
        policy_size_quota: int = None,
        attached_policies_per_group_quota: int = None,
        groups: int = None,
        attached_system_policies_per_user_quota: int = None,
        users_quota: int = None,
        attached_policies_per_role_quota: int = None,
        attached_system_policies_per_role_quota: int = None,
        mfadevices: int = None,
        groups_quota: int = None,
    ):
        self.policies = policies
        self.groups_per_user_quota = groups_per_user_quota
        self.attached_policies_per_user_quota = attached_policies_per_user_quota
        self.roles = roles
        self.users = users
        self.roles_quota = roles_quota
        self.virtual_mfadevices_quota = virtual_mfadevices_quota
        self.policies_quota = policies_quota
        self.attached_system_policies_per_group_quota = attached_system_policies_per_group_quota
        self.mfadevices_in_use = mfadevices_in_use
        self.access_keys_per_user_quota = access_keys_per_user_quota
        self.versions_per_policy_quota = versions_per_policy_quota
        self.policy_size_quota = policy_size_quota
        self.attached_policies_per_group_quota = attached_policies_per_group_quota
        self.groups = groups
        self.attached_system_policies_per_user_quota = attached_system_policies_per_user_quota
        self.users_quota = users_quota
        self.attached_policies_per_role_quota = attached_policies_per_role_quota
        self.attached_system_policies_per_role_quota = attached_system_policies_per_role_quota
        self.mfadevices = mfadevices
        self.groups_quota = groups_quota

    def validate(self):
        self.validate_required(self.policies, 'policies')
        self.validate_required(self.groups_per_user_quota, 'groups_per_user_quota')
        self.validate_required(self.attached_policies_per_user_quota, 'attached_policies_per_user_quota')
        self.validate_required(self.roles, 'roles')
        self.validate_required(self.users, 'users')
        self.validate_required(self.roles_quota, 'roles_quota')
        self.validate_required(self.virtual_mfadevices_quota, 'virtual_mfadevices_quota')
        self.validate_required(self.policies_quota, 'policies_quota')
        self.validate_required(self.attached_system_policies_per_group_quota, 'attached_system_policies_per_group_quota')
        self.validate_required(self.mfadevices_in_use, 'mfadevices_in_use')
        self.validate_required(self.access_keys_per_user_quota, 'access_keys_per_user_quota')
        self.validate_required(self.versions_per_policy_quota, 'versions_per_policy_quota')
        self.validate_required(self.policy_size_quota, 'policy_size_quota')
        self.validate_required(self.attached_policies_per_group_quota, 'attached_policies_per_group_quota')
        self.validate_required(self.groups, 'groups')
        self.validate_required(self.attached_system_policies_per_user_quota, 'attached_system_policies_per_user_quota')
        self.validate_required(self.users_quota, 'users_quota')
        self.validate_required(self.attached_policies_per_role_quota, 'attached_policies_per_role_quota')
        self.validate_required(self.attached_system_policies_per_role_quota, 'attached_system_policies_per_role_quota')
        self.validate_required(self.mfadevices, 'mfadevices')
        self.validate_required(self.groups_quota, 'groups_quota')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policies is not None:
            result['Policies'] = self.policies
        if self.groups_per_user_quota is not None:
            result['GroupsPerUserQuota'] = self.groups_per_user_quota
        if self.attached_policies_per_user_quota is not None:
            result['AttachedPoliciesPerUserQuota'] = self.attached_policies_per_user_quota
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.users is not None:
            result['Users'] = self.users
        if self.roles_quota is not None:
            result['RolesQuota'] = self.roles_quota
        if self.virtual_mfadevices_quota is not None:
            result['VirtualMFADevicesQuota'] = self.virtual_mfadevices_quota
        if self.policies_quota is not None:
            result['PoliciesQuota'] = self.policies_quota
        if self.attached_system_policies_per_group_quota is not None:
            result['AttachedSystemPoliciesPerGroupQuota'] = self.attached_system_policies_per_group_quota
        if self.mfadevices_in_use is not None:
            result['MFADevicesInUse'] = self.mfadevices_in_use
        if self.access_keys_per_user_quota is not None:
            result['AccessKeysPerUserQuota'] = self.access_keys_per_user_quota
        if self.versions_per_policy_quota is not None:
            result['VersionsPerPolicyQuota'] = self.versions_per_policy_quota
        if self.policy_size_quota is not None:
            result['PolicySizeQuota'] = self.policy_size_quota
        if self.attached_policies_per_group_quota is not None:
            result['AttachedPoliciesPerGroupQuota'] = self.attached_policies_per_group_quota
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.attached_system_policies_per_user_quota is not None:
            result['AttachedSystemPoliciesPerUserQuota'] = self.attached_system_policies_per_user_quota
        if self.users_quota is not None:
            result['UsersQuota'] = self.users_quota
        if self.attached_policies_per_role_quota is not None:
            result['AttachedPoliciesPerRoleQuota'] = self.attached_policies_per_role_quota
        if self.attached_system_policies_per_role_quota is not None:
            result['AttachedSystemPoliciesPerRoleQuota'] = self.attached_system_policies_per_role_quota
        if self.mfadevices is not None:
            result['MFADevices'] = self.mfadevices
        if self.groups_quota is not None:
            result['GroupsQuota'] = self.groups_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policies') is not None:
            self.policies = m.get('Policies')
        if m.get('GroupsPerUserQuota') is not None:
            self.groups_per_user_quota = m.get('GroupsPerUserQuota')
        if m.get('AttachedPoliciesPerUserQuota') is not None:
            self.attached_policies_per_user_quota = m.get('AttachedPoliciesPerUserQuota')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        if m.get('RolesQuota') is not None:
            self.roles_quota = m.get('RolesQuota')
        if m.get('VirtualMFADevicesQuota') is not None:
            self.virtual_mfadevices_quota = m.get('VirtualMFADevicesQuota')
        if m.get('PoliciesQuota') is not None:
            self.policies_quota = m.get('PoliciesQuota')
        if m.get('AttachedSystemPoliciesPerGroupQuota') is not None:
            self.attached_system_policies_per_group_quota = m.get('AttachedSystemPoliciesPerGroupQuota')
        if m.get('MFADevicesInUse') is not None:
            self.mfadevices_in_use = m.get('MFADevicesInUse')
        if m.get('AccessKeysPerUserQuota') is not None:
            self.access_keys_per_user_quota = m.get('AccessKeysPerUserQuota')
        if m.get('VersionsPerPolicyQuota') is not None:
            self.versions_per_policy_quota = m.get('VersionsPerPolicyQuota')
        if m.get('PolicySizeQuota') is not None:
            self.policy_size_quota = m.get('PolicySizeQuota')
        if m.get('AttachedPoliciesPerGroupQuota') is not None:
            self.attached_policies_per_group_quota = m.get('AttachedPoliciesPerGroupQuota')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('AttachedSystemPoliciesPerUserQuota') is not None:
            self.attached_system_policies_per_user_quota = m.get('AttachedSystemPoliciesPerUserQuota')
        if m.get('UsersQuota') is not None:
            self.users_quota = m.get('UsersQuota')
        if m.get('AttachedPoliciesPerRoleQuota') is not None:
            self.attached_policies_per_role_quota = m.get('AttachedPoliciesPerRoleQuota')
        if m.get('AttachedSystemPoliciesPerRoleQuota') is not None:
            self.attached_system_policies_per_role_quota = m.get('AttachedSystemPoliciesPerRoleQuota')
        if m.get('MFADevices') is not None:
            self.mfadevices = m.get('MFADevices')
        if m.get('GroupsQuota') is not None:
            self.groups_quota = m.get('GroupsQuota')
        return self


class GetAccountSummaryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        summary_map: GetAccountSummaryResponseSummaryMap = None,
    ):
        self.request_id = request_id
        self.summary_map = summary_map

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.summary_map, 'summary_map')
        if self.summary_map:
            self.summary_map.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetAccountSummaryResponseSummaryMap()
            self.summary_map = temp_model.from_map(m['SummaryMap'])
        return self


class GetAccountSecurityPracticeReportRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAccountSecurityPracticeReportResponseAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo(TeaModel):
    def __init__(
        self,
        sub_user: int = None,
        sub_user_bind_mfa: int = None,
        sub_user_with_unused_access_key: int = None,
        root_with_access_key: int = None,
        sub_user_with_old_access_key: int = None,
        sub_user_pwd_level: str = None,
        old_ak_num: int = None,
        unused_ak_num: int = None,
        bind_mfa: bool = None,
    ):
        self.sub_user = sub_user
        self.sub_user_bind_mfa = sub_user_bind_mfa
        self.sub_user_with_unused_access_key = sub_user_with_unused_access_key
        self.root_with_access_key = root_with_access_key
        self.sub_user_with_old_access_key = sub_user_with_old_access_key
        self.sub_user_pwd_level = sub_user_pwd_level
        self.old_ak_num = old_ak_num
        self.unused_ak_num = unused_ak_num
        self.bind_mfa = bind_mfa

    def validate(self):
        self.validate_required(self.sub_user, 'sub_user')
        self.validate_required(self.sub_user_bind_mfa, 'sub_user_bind_mfa')
        self.validate_required(self.sub_user_with_unused_access_key, 'sub_user_with_unused_access_key')
        self.validate_required(self.root_with_access_key, 'root_with_access_key')
        self.validate_required(self.sub_user_with_old_access_key, 'sub_user_with_old_access_key')
        self.validate_required(self.sub_user_pwd_level, 'sub_user_pwd_level')
        self.validate_required(self.old_ak_num, 'old_ak_num')
        self.validate_required(self.unused_ak_num, 'unused_ak_num')
        self.validate_required(self.bind_mfa, 'bind_mfa')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_user is not None:
            result['SubUser'] = self.sub_user
        if self.sub_user_bind_mfa is not None:
            result['SubUserBindMfa'] = self.sub_user_bind_mfa
        if self.sub_user_with_unused_access_key is not None:
            result['SubUserWithUnusedAccessKey'] = self.sub_user_with_unused_access_key
        if self.root_with_access_key is not None:
            result['RootWithAccessKey'] = self.root_with_access_key
        if self.sub_user_with_old_access_key is not None:
            result['SubUserWithOldAccessKey'] = self.sub_user_with_old_access_key
        if self.sub_user_pwd_level is not None:
            result['SubUserPwdLevel'] = self.sub_user_pwd_level
        if self.old_ak_num is not None:
            result['OldAkNum'] = self.old_ak_num
        if self.unused_ak_num is not None:
            result['UnusedAkNum'] = self.unused_ak_num
        if self.bind_mfa is not None:
            result['BindMfa'] = self.bind_mfa
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubUser') is not None:
            self.sub_user = m.get('SubUser')
        if m.get('SubUserBindMfa') is not None:
            self.sub_user_bind_mfa = m.get('SubUserBindMfa')
        if m.get('SubUserWithUnusedAccessKey') is not None:
            self.sub_user_with_unused_access_key = m.get('SubUserWithUnusedAccessKey')
        if m.get('RootWithAccessKey') is not None:
            self.root_with_access_key = m.get('RootWithAccessKey')
        if m.get('SubUserWithOldAccessKey') is not None:
            self.sub_user_with_old_access_key = m.get('SubUserWithOldAccessKey')
        if m.get('SubUserPwdLevel') is not None:
            self.sub_user_pwd_level = m.get('SubUserPwdLevel')
        if m.get('OldAkNum') is not None:
            self.old_ak_num = m.get('OldAkNum')
        if m.get('UnusedAkNum') is not None:
            self.unused_ak_num = m.get('UnusedAkNum')
        if m.get('BindMfa') is not None:
            self.bind_mfa = m.get('BindMfa')
        return self


class GetAccountSecurityPracticeReportResponseAccountSecurityPracticeInfo(TeaModel):
    def __init__(
        self,
        score: int = None,
        account_security_practice_user_info: GetAccountSecurityPracticeReportResponseAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo = None,
    ):
        self.score = score
        self.account_security_practice_user_info = account_security_practice_user_info

    def validate(self):
        self.validate_required(self.score, 'score')
        self.validate_required(self.account_security_practice_user_info, 'account_security_practice_user_info')
        if self.account_security_practice_user_info:
            self.account_security_practice_user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.account_security_practice_user_info is not None:
            result['AccountSecurityPracticeUserInfo'] = self.account_security_practice_user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('AccountSecurityPracticeUserInfo') is not None:
            temp_model = GetAccountSecurityPracticeReportResponseAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo()
            self.account_security_practice_user_info = temp_model.from_map(m['AccountSecurityPracticeUserInfo'])
        return self


class GetAccountSecurityPracticeReportResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account_security_practice_info: GetAccountSecurityPracticeReportResponseAccountSecurityPracticeInfo = None,
    ):
        self.request_id = request_id
        self.account_security_practice_info = account_security_practice_info

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.account_security_practice_info, 'account_security_practice_info')
        if self.account_security_practice_info:
            self.account_security_practice_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetAccountSecurityPracticeReportResponseAccountSecurityPracticeInfo()
            self.account_security_practice_info = temp_model.from_map(m['AccountSecurityPracticeInfo'])
        return self


class GetAccountMFAInfoRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAccountMFAInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_mfaenable: bool = None,
    ):
        self.request_id = request_id
        self.is_mfaenable = is_mfaenable

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_mfaenable, 'is_mfaenable')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetAccessKeyLastUsedRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        user_access_key_id: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.user_access_key_id = user_access_key_id

    def validate(self):
        self.validate_required(self.user_access_key_id, 'user_access_key_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        return self


class GetAccessKeyLastUsedResponseAccessKeyLastUsed(TeaModel):
    def __init__(
        self,
        last_used_date: str = None,
    ):
        self.last_used_date = last_used_date

    def validate(self):
        self.validate_required(self.last_used_date, 'last_used_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_used_date is not None:
            result['LastUsedDate'] = self.last_used_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastUsedDate') is not None:
            self.last_used_date = m.get('LastUsedDate')
        return self


class GetAccessKeyLastUsedResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        access_key_last_used: GetAccessKeyLastUsedResponseAccessKeyLastUsed = None,
    ):
        self.request_id = request_id
        self.access_key_last_used = access_key_last_used

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.access_key_last_used, 'access_key_last_used')
        if self.access_key_last_used:
            self.access_key_last_used.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_key_last_used is not None:
            result['AccessKeyLastUsed'] = self.access_key_last_used.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessKeyLastUsed') is not None:
            temp_model = GetAccessKeyLastUsedResponseAccessKeyLastUsed()
            self.access_key_last_used = temp_model.from_map(m['AccessKeyLastUsed'])
        return self


class DisableVirtualMFARequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        self.user_principal_name = user_principal_name

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class DisableVirtualMFAResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DeleteVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
    ):
        self.serial_number = serial_number

    def validate(self):
        self.validate_required(self.serial_number, 'serial_number')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class DeleteVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        user_id: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DeleteSAMLProviderRequest(TeaModel):
    def __init__(
        self,
        samlprovider_name: str = None,
    ):
        self.samlprovider_name = samlprovider_name

    def validate(self):
        self.validate_required(self.samlprovider_name, 'samlprovider_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        return self


class DeleteSAMLProviderResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DeleteLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        self.user_principal_name = user_principal_name

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class DeleteLoginProfileResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DeleteGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
    ):
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DeleteGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DeleteAccessKeyRequest(TeaModel):
    def __init__(
        self,
        user_access_key_id: str = None,
        user_principal_name: str = None,
    ):
        self.user_access_key_id = user_access_key_id
        self.user_principal_name = user_principal_name

    def validate(self):
        self.validate_required(self.user_access_key_id, 'user_access_key_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class DeleteAccessKeyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class CreateVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        virtual_mfadevice_name: str = None,
    ):
        self.virtual_mfadevice_name = virtual_mfadevice_name

    def validate(self):
        self.validate_required(self.virtual_mfadevice_name, 'virtual_mfadevice_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.virtual_mfadevice_name is not None:
            result['VirtualMFADeviceName'] = self.virtual_mfadevice_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VirtualMFADeviceName') is not None:
            self.virtual_mfadevice_name = m.get('VirtualMFADeviceName')
        return self


class CreateVirtualMFADeviceResponseVirtualMFADevice(TeaModel):
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
        self.validate_required(self.serial_number, 'serial_number')
        self.validate_required(self.qrcode_png, 'qrcode_png')
        self.validate_required(self.base_32string_seed, 'base_32string_seed')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        virtual_mfadevice: CreateVirtualMFADeviceResponseVirtualMFADevice = None,
    ):
        self.request_id = request_id
        self.virtual_mfadevice = virtual_mfadevice

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.virtual_mfadevice, 'virtual_mfadevice')
        if self.virtual_mfadevice:
            self.virtual_mfadevice.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.virtual_mfadevice is not None:
            result['VirtualMFADevice'] = self.virtual_mfadevice.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VirtualMFADevice') is not None:
            temp_model = CreateVirtualMFADeviceResponseVirtualMFADevice()
            self.virtual_mfadevice = temp_model.from_map(m['VirtualMFADevice'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        display_name: str = None,
        mobile_phone: str = None,
        email: str = None,
        comments: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.display_name = display_name
        self.mobile_phone = mobile_phone
        self.email = email
        self.comments = comments

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.display_name, 'display_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        return self


class CreateUserResponseUser(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        email: str = None,
        comments: str = None,
        user_id: str = None,
        last_login_date: str = None,
        display_name: str = None,
        user_principal_name: str = None,
        create_date: str = None,
        mobile_phone: str = None,
    ):
        self.update_date = update_date
        self.email = email
        self.comments = comments
        self.user_id = user_id
        self.last_login_date = last_login_date
        self.display_name = display_name
        self.user_principal_name = user_principal_name
        self.create_date = create_date
        self.mobile_phone = mobile_phone

    def validate(self):
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.email, 'email')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.last_login_date, 'last_login_date')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.mobile_phone, 'mobile_phone')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.email is not None:
            result['Email'] = self.email
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        return self


class CreateUserResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user: CreateUserResponseUser = None,
    ):
        self.request_id = request_id
        self.user = user

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.user, 'user')
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('User') is not None:
            temp_model = CreateUserResponseUser()
            self.user = temp_model.from_map(m['User'])
        return self


class CreateSAMLProviderRequest(TeaModel):
    def __init__(
        self,
        samlprovider_name: str = None,
        description: str = None,
        encoded_samlmetadata_document: str = None,
    ):
        self.samlprovider_name = samlprovider_name
        self.description = description
        self.encoded_samlmetadata_document = encoded_samlmetadata_document

    def validate(self):
        self.validate_required(self.samlprovider_name, 'samlprovider_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.description is not None:
            result['Description'] = self.description
        if self.encoded_samlmetadata_document is not None:
            result['EncodedSAMLMetadataDocument'] = self.encoded_samlmetadata_document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncodedSAMLMetadataDocument') is not None:
            self.encoded_samlmetadata_document = m.get('EncodedSAMLMetadataDocument')
        return self


class CreateSAMLProviderResponseSAMLProvider(TeaModel):
    def __init__(
        self,
        update_date: str = None,
        samlprovider_name: str = None,
        description: str = None,
        arn: str = None,
        create_date: str = None,
    ):
        self.update_date = update_date
        self.samlprovider_name = samlprovider_name
        self.description = description
        self.arn = arn
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.samlprovider_name, 'samlprovider_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.description is not None:
            result['Description'] = self.description
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreateSAMLProviderResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlprovider: CreateSAMLProviderResponseSAMLProvider = None,
    ):
        self.request_id = request_id
        self.samlprovider = samlprovider

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.samlprovider, 'samlprovider')
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateSAMLProviderResponseSAMLProvider()
            self.samlprovider = temp_model.from_map(m['SAMLProvider'])
        return self


class CreateLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        password: str = None,
        password_reset_required: bool = None,
        mfabind_required: bool = None,
        status: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.password = password
        self.password_reset_required = password_reset_required
        self.mfabind_required = mfabind_required
        self.status = status

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.password is not None:
            result['Password'] = self.password
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateLoginProfileResponseLoginProfile(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_date: str = None,
        password_reset_required: bool = None,
        user_principal_name: str = None,
        mfabind_required: bool = None,
    ):
        self.status = status
        self.update_date = update_date
        self.password_reset_required = password_reset_required
        self.user_principal_name = user_principal_name
        self.mfabind_required = mfabind_required

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.password_reset_required, 'password_reset_required')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.mfabind_required, 'mfabind_required')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        return self


class CreateLoginProfileResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        login_profile: CreateLoginProfileResponseLoginProfile = None,
    ):
        self.request_id = request_id
        self.login_profile = login_profile

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.login_profile, 'login_profile')
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateLoginProfileResponseLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        comments: str = None,
        group_name: str = None,
    ):
        self.display_name = display_name
        self.comments = comments
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class CreateGroupResponseGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        update_date: str = None,
        comments: str = None,
        display_name: str = None,
        create_date: str = None,
        group_id: str = None,
    ):
        self.group_name = group_name
        self.update_date = update_date
        self.comments = comments
        self.display_name = display_name
        self.create_date = create_date
        self.group_id = group_id

    def validate(self):
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group: CreateGroupResponseGroup = None,
    ):
        self.request_id = request_id
        self.group = group

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group, 'group')
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group is not None:
            result['Group'] = self.group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Group') is not None:
            temp_model = CreateGroupResponseGroup()
            self.group = temp_model.from_map(m['Group'])
        return self


class CreateAccessKeyRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateAccessKeyResponseAccessKey(TeaModel):
    def __init__(
        self,
        status: str = None,
        access_key_id: str = None,
        access_key_secret: str = None,
        create_date: str = None,
    ):
        self.status = status
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.access_key_id, 'access_key_id')
        self.validate_required(self.access_key_secret, 'access_key_secret')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreateAccessKeyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        access_key: CreateAccessKeyResponseAccessKey = None,
    ):
        self.request_id = request_id
        self.access_key = access_key

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.access_key, 'access_key')
        if self.access_key:
            self.access_key.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateAccessKeyResponseAccessKey()
            self.access_key = temp_model.from_map(m['AccessKey'])
        return self


class ChangePasswordRequest(TeaModel):
    def __init__(
        self,
        old_password: str = None,
        new_password: str = None,
    ):
        self.old_password = old_password
        self.new_password = new_password

    def validate(self):
        self.validate_required(self.old_password, 'old_password')
        self.validate_required(self.new_password, 'new_password')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.old_password is not None:
            result['OldPassword'] = self.old_password
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        return self


class ChangePasswordResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class BindMFADeviceRequest(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        user_principal_name: str = None,
        authentication_code_1: str = None,
        authentication_code_2: str = None,
    ):
        self.serial_number = serial_number
        self.user_principal_name = user_principal_name
        self.authentication_code_1 = authentication_code_1
        self.authentication_code_2 = authentication_code_2

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.authentication_code_1 is not None:
            result['AuthenticationCode1'] = self.authentication_code_1
        if self.authentication_code_2 is not None:
            result['AuthenticationCode2'] = self.authentication_code_2
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
        return self


class BindMFADeviceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class AddUserToGroupRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
        group_name: str = None,
    ):
        self.user_principal_name = user_principal_name
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class AddUserToGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


