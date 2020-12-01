# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class GetUserSsoSettingsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetUserSsoSettingsResponse(TeaModel):
    def __init__(self, request_id=None, user_sso_settings=None):
        self.request_id = request_id    # type: str
        self.user_sso_settings = user_sso_settings  # type: GetUserSsoSettingsResponseUserSsoSettings

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.user_sso_settings, 'user_sso_settings')
        if self.user_sso_settings:
            self.user_sso_settings.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_sso_settings is not None:
            result['UserSsoSettings'] = self.user_sso_settings.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('UserSsoSettings') is not None:
            temp_model = GetUserSsoSettingsResponseUserSsoSettings()
            self.user_sso_settings = temp_model.from_map(map['UserSsoSettings'])
        return self


class GetUserSsoSettingsResponseUserSsoSettings(TeaModel):
    def __init__(self, sso_enabled=None, metadata_document=None, auxiliary_domain=None):
        self.sso_enabled = sso_enabled  # type: bool
        self.metadata_document = metadata_document  # type: str
        self.auxiliary_domain = auxiliary_domain  # type: str

    def validate(self):
        self.validate_required(self.sso_enabled, 'sso_enabled')
        self.validate_required(self.metadata_document, 'metadata_document')
        self.validate_required(self.auxiliary_domain, 'auxiliary_domain')

    def to_map(self):
        result = {}
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        return result

    def from_map(self, map={}):
        if map.get('SsoEnabled') is not None:
            self.sso_enabled = map.get('SsoEnabled')
        if map.get('MetadataDocument') is not None:
            self.metadata_document = map.get('MetadataDocument')
        if map.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = map.get('AuxiliaryDomain')
        return self


class SetUserSsoSettingsRequest(TeaModel):
    def __init__(self, metadata_document=None, sso_enabled=None, auxiliary_domain=None):
        self.metadata_document = metadata_document  # type: str
        self.sso_enabled = sso_enabled  # type: bool
        self.auxiliary_domain = auxiliary_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        return result

    def from_map(self, map={}):
        if map.get('MetadataDocument') is not None:
            self.metadata_document = map.get('MetadataDocument')
        if map.get('SsoEnabled') is not None:
            self.sso_enabled = map.get('SsoEnabled')
        if map.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = map.get('AuxiliaryDomain')
        return self


class SetUserSsoSettingsResponse(TeaModel):
    def __init__(self, request_id=None, user_sso_settings=None):
        self.request_id = request_id    # type: str
        self.user_sso_settings = user_sso_settings  # type: SetUserSsoSettingsResponseUserSsoSettings

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.user_sso_settings, 'user_sso_settings')
        if self.user_sso_settings:
            self.user_sso_settings.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_sso_settings is not None:
            result['UserSsoSettings'] = self.user_sso_settings.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('UserSsoSettings') is not None:
            temp_model = SetUserSsoSettingsResponseUserSsoSettings()
            self.user_sso_settings = temp_model.from_map(map['UserSsoSettings'])
        return self


class SetUserSsoSettingsResponseUserSsoSettings(TeaModel):
    def __init__(self, sso_enabled=None, metadata_document=None, auxiliary_domain=None):
        self.sso_enabled = sso_enabled  # type: bool
        self.metadata_document = metadata_document  # type: str
        self.auxiliary_domain = auxiliary_domain  # type: str

    def validate(self):
        self.validate_required(self.sso_enabled, 'sso_enabled')
        self.validate_required(self.metadata_document, 'metadata_document')
        self.validate_required(self.auxiliary_domain, 'auxiliary_domain')

    def to_map(self):
        result = {}
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        return result

    def from_map(self, map={}):
        if map.get('SsoEnabled') is not None:
            self.sso_enabled = map.get('SsoEnabled')
        if map.get('MetadataDocument') is not None:
            self.metadata_document = map.get('MetadataDocument')
        if map.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = map.get('AuxiliaryDomain')
        return self


class SetDefaultDomainRequest(TeaModel):
    def __init__(self, default_domain_name=None):
        self.default_domain_name = default_domain_name  # type: str

    def validate(self):
        self.validate_required(self.default_domain_name, 'default_domain_name')

    def to_map(self):
        result = {}
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        return result

    def from_map(self, map={}):
        if map.get('DefaultDomainName') is not None:
            self.default_domain_name = map.get('DefaultDomainName')
        return self


class SetDefaultDomainResponse(TeaModel):
    def __init__(self, request_id=None, default_domain_name=None):
        self.request_id = request_id    # type: str
        self.default_domain_name = default_domain_name  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.default_domain_name, 'default_domain_name')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('DefaultDomainName') is not None:
            self.default_domain_name = map.get('DefaultDomainName')
        return self


class ListUserBasicInfosRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        self.marker = marker            # type: str
        self.max_items = max_items      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, map={}):
        if map.get('Marker') is not None:
            self.marker = map.get('Marker')
        if map.get('MaxItems') is not None:
            self.max_items = map.get('MaxItems')
        return self


class ListUserBasicInfosResponse(TeaModel):
    def __init__(self, request_id=None, marker=None, is_truncated=None, user_basic_infos=None):
        self.request_id = request_id    # type: str
        self.marker = marker            # type: str
        self.is_truncated = is_truncated  # type: bool
        self.user_basic_infos = user_basic_infos  # type: ListUserBasicInfosResponseUserBasicInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.is_truncated, 'is_truncated')
        self.validate_required(self.user_basic_infos, 'user_basic_infos')
        if self.user_basic_infos:
            self.user_basic_infos.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.user_basic_infos is not None:
            result['UserBasicInfos'] = self.user_basic_infos.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Marker') is not None:
            self.marker = map.get('Marker')
        if map.get('IsTruncated') is not None:
            self.is_truncated = map.get('IsTruncated')
        if map.get('UserBasicInfos') is not None:
            temp_model = ListUserBasicInfosResponseUserBasicInfos()
            self.user_basic_infos = temp_model.from_map(map['UserBasicInfos'])
        return self


class ListUserBasicInfosResponseUserBasicInfosUserBasicInfo(TeaModel):
    def __init__(self, user_id=None, user_principal_name=None, display_name=None):
        self.user_id = user_id          # type: str
        self.user_principal_name = user_principal_name  # type: str
        self.display_name = display_name  # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.display_name, 'display_name')

    def to_map(self):
        result = {}
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        return result

    def from_map(self, map={}):
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        return self


class ListUserBasicInfosResponseUserBasicInfos(TeaModel):
    def __init__(self, user_basic_info=None):
        self.user_basic_info = user_basic_info  # type: List[ListUserBasicInfosResponseUserBasicInfosUserBasicInfo]

    def validate(self):
        self.validate_required(self.user_basic_info, 'user_basic_info')
        if self.user_basic_info:
            for k in self.user_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UserBasicInfo'] = []
        if self.user_basic_info is not None:
            for k in self.user_basic_info:
                result['UserBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.user_basic_info = []
        if map.get('UserBasicInfo') is not None:
            for k in map.get('UserBasicInfo'):
                temp_model = ListUserBasicInfosResponseUserBasicInfosUserBasicInfo()
                self.user_basic_info.append(temp_model.from_map(k))
        return self


class UpdateApplicationRequest(TeaModel):
    def __init__(self, app_id=None, new_display_name=None, new_redirect_uris=None, new_predefined_scopes=None,
                 new_secret_required=None, new_access_token_validity=None, new_refresh_token_validity=None, new_is_multi_tenant=None):
        self.app_id = app_id            # type: str
        self.new_display_name = new_display_name  # type: str
        self.new_redirect_uris = new_redirect_uris  # type: str
        self.new_predefined_scopes = new_predefined_scopes  # type: str
        self.new_secret_required = new_secret_required  # type: bool
        self.new_access_token_validity = new_access_token_validity  # type: int
        self.new_refresh_token_validity = new_refresh_token_validity  # type: int
        self.new_is_multi_tenant = new_is_multi_tenant  # type: bool

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        if map.get('NewDisplayName') is not None:
            self.new_display_name = map.get('NewDisplayName')
        if map.get('NewRedirectUris') is not None:
            self.new_redirect_uris = map.get('NewRedirectUris')
        if map.get('NewPredefinedScopes') is not None:
            self.new_predefined_scopes = map.get('NewPredefinedScopes')
        if map.get('NewSecretRequired') is not None:
            self.new_secret_required = map.get('NewSecretRequired')
        if map.get('NewAccessTokenValidity') is not None:
            self.new_access_token_validity = map.get('NewAccessTokenValidity')
        if map.get('NewRefreshTokenValidity') is not None:
            self.new_refresh_token_validity = map.get('NewRefreshTokenValidity')
        if map.get('NewIsMultiTenant') is not None:
            self.new_is_multi_tenant = map.get('NewIsMultiTenant')
        return self


class UpdateApplicationResponse(TeaModel):
    def __init__(self, request_id=None, application=None):
        self.request_id = request_id    # type: str
        self.application = application  # type: UpdateApplicationResponseApplication

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.application, 'application')
        if self.application:
            self.application.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.application is not None:
            result['Application'] = self.application.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Application') is not None:
            temp_model = UpdateApplicationResponseApplication()
            self.application = temp_model.from_map(map['Application'])
        return self


class UpdateApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(self, name=None, description=None):
        self.name = name                # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        return self


class UpdateApplicationResponseApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(self, predefined_scope=None):
        self.predefined_scope = predefined_scope  # type: List[UpdateApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope]

    def validate(self):
        self.validate_required(self.predefined_scope, 'predefined_scope')
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.predefined_scope = []
        if map.get('PredefinedScope') is not None:
            for k in map.get('PredefinedScope'):
                temp_model = UpdateApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class UpdateApplicationResponseApplicationDelegatedScope(TeaModel):
    def __init__(self, predefined_scopes=None):
        self.predefined_scopes = predefined_scopes  # type: UpdateApplicationResponseApplicationDelegatedScopePredefinedScopes

    def validate(self):
        self.validate_required(self.predefined_scopes, 'predefined_scopes')
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        result = {}
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, map={}):
        if map.get('PredefinedScopes') is not None:
            temp_model = UpdateApplicationResponseApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(map['PredefinedScopes'])
        return self


class UpdateApplicationResponseApplicationRedirectUris(TeaModel):
    def __init__(self, redirect_uri=None):
        # RedirectUri
        self.redirect_uri = redirect_uri  # type: List[str]

    def validate(self):
        self.validate_required(self.redirect_uri, 'redirect_uri')

    def to_map(self):
        result = {}
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, map={}):
        if map.get('RedirectUri') is not None:
            self.redirect_uri = map.get('RedirectUri')
        return self


class UpdateApplicationResponseApplication(TeaModel):
    def __init__(self, app_id=None, display_name=None, app_type=None, secret_required=None,
                 access_token_validity=None, refresh_token_validity=None, is_multi_tenant=None, create_date=None, update_date=None,
                 app_name=None, account_id=None, delegated_scope=None, redirect_uris=None):
        self.app_id = app_id            # type: str
        self.display_name = display_name  # type: str
        self.app_type = app_type        # type: str
        self.secret_required = secret_required  # type: bool
        self.access_token_validity = access_token_validity  # type: int
        self.refresh_token_validity = refresh_token_validity  # type: int
        self.is_multi_tenant = is_multi_tenant  # type: bool
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.app_name = app_name        # type: str
        self.account_id = account_id    # type: str
        self.delegated_scope = delegated_scope  # type: UpdateApplicationResponseApplicationDelegatedScope
        self.redirect_uris = redirect_uris  # type: UpdateApplicationResponseApplicationRedirectUris

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.app_type, 'app_type')
        self.validate_required(self.secret_required, 'secret_required')
        self.validate_required(self.access_token_validity, 'access_token_validity')
        self.validate_required(self.refresh_token_validity, 'refresh_token_validity')
        self.validate_required(self.is_multi_tenant, 'is_multi_tenant')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.delegated_scope, 'delegated_scope')
        if self.delegated_scope:
            self.delegated_scope.validate()
        self.validate_required(self.redirect_uris, 'redirect_uris')
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('AppType') is not None:
            self.app_type = map.get('AppType')
        if map.get('SecretRequired') is not None:
            self.secret_required = map.get('SecretRequired')
        if map.get('AccessTokenValidity') is not None:
            self.access_token_validity = map.get('AccessTokenValidity')
        if map.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = map.get('RefreshTokenValidity')
        if map.get('IsMultiTenant') is not None:
            self.is_multi_tenant = map.get('IsMultiTenant')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('AppName') is not None:
            self.app_name = map.get('AppName')
        if map.get('AccountId') is not None:
            self.account_id = map.get('AccountId')
        if map.get('DelegatedScope') is not None:
            temp_model = UpdateApplicationResponseApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(map['DelegatedScope'])
        if map.get('RedirectUris') is not None:
            temp_model = UpdateApplicationResponseApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(map['RedirectUris'])
        return self


class ListApplicationsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(self, request_id=None, applications=None):
        self.request_id = request_id    # type: str
        self.applications = applications  # type: ListApplicationsResponseApplications

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.applications, 'applications')
        if self.applications:
            self.applications.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Applications') is not None:
            temp_model = ListApplicationsResponseApplications()
            self.applications = temp_model.from_map(map['Applications'])
        return self


class ListApplicationsResponseApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(self, name=None, description=None):
        self.name = name                # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        return self


class ListApplicationsResponseApplicationsApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(self, predefined_scope=None):
        self.predefined_scope = predefined_scope  # type: List[ListApplicationsResponseApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope]

    def validate(self):
        self.validate_required(self.predefined_scope, 'predefined_scope')
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.predefined_scope = []
        if map.get('PredefinedScope') is not None:
            for k in map.get('PredefinedScope'):
                temp_model = ListApplicationsResponseApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseApplicationsApplicationDelegatedScope(TeaModel):
    def __init__(self, predefined_scopes=None):
        self.predefined_scopes = predefined_scopes  # type: ListApplicationsResponseApplicationsApplicationDelegatedScopePredefinedScopes

    def validate(self):
        self.validate_required(self.predefined_scopes, 'predefined_scopes')
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        result = {}
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, map={}):
        if map.get('PredefinedScopes') is not None:
            temp_model = ListApplicationsResponseApplicationsApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(map['PredefinedScopes'])
        return self


class ListApplicationsResponseApplicationsApplicationRedirectUris(TeaModel):
    def __init__(self, redirect_uri=None):
        # RedirectUri
        self.redirect_uri = redirect_uri  # type: List[str]

    def validate(self):
        self.validate_required(self.redirect_uri, 'redirect_uri')

    def to_map(self):
        result = {}
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, map={}):
        if map.get('RedirectUri') is not None:
            self.redirect_uri = map.get('RedirectUri')
        return self


class ListApplicationsResponseApplicationsApplication(TeaModel):
    def __init__(self, app_id=None, display_name=None, app_type=None, secret_required=None,
                 access_token_validity=None, refresh_token_validity=None, is_multi_tenant=None, create_date=None, update_date=None,
                 app_name=None, account_id=None, delegated_scope=None, redirect_uris=None):
        self.app_id = app_id            # type: str
        self.display_name = display_name  # type: str
        self.app_type = app_type        # type: str
        self.secret_required = secret_required  # type: bool
        self.access_token_validity = access_token_validity  # type: int
        self.refresh_token_validity = refresh_token_validity  # type: int
        self.is_multi_tenant = is_multi_tenant  # type: bool
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.app_name = app_name        # type: str
        self.account_id = account_id    # type: str
        self.delegated_scope = delegated_scope  # type: ListApplicationsResponseApplicationsApplicationDelegatedScope
        self.redirect_uris = redirect_uris  # type: ListApplicationsResponseApplicationsApplicationRedirectUris

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.app_type, 'app_type')
        self.validate_required(self.secret_required, 'secret_required')
        self.validate_required(self.access_token_validity, 'access_token_validity')
        self.validate_required(self.refresh_token_validity, 'refresh_token_validity')
        self.validate_required(self.is_multi_tenant, 'is_multi_tenant')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.delegated_scope, 'delegated_scope')
        if self.delegated_scope:
            self.delegated_scope.validate()
        self.validate_required(self.redirect_uris, 'redirect_uris')
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('AppType') is not None:
            self.app_type = map.get('AppType')
        if map.get('SecretRequired') is not None:
            self.secret_required = map.get('SecretRequired')
        if map.get('AccessTokenValidity') is not None:
            self.access_token_validity = map.get('AccessTokenValidity')
        if map.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = map.get('RefreshTokenValidity')
        if map.get('IsMultiTenant') is not None:
            self.is_multi_tenant = map.get('IsMultiTenant')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('AppName') is not None:
            self.app_name = map.get('AppName')
        if map.get('AccountId') is not None:
            self.account_id = map.get('AccountId')
        if map.get('DelegatedScope') is not None:
            temp_model = ListApplicationsResponseApplicationsApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(map['DelegatedScope'])
        if map.get('RedirectUris') is not None:
            temp_model = ListApplicationsResponseApplicationsApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(map['RedirectUris'])
        return self


class ListApplicationsResponseApplications(TeaModel):
    def __init__(self, application=None):
        self.application = application  # type: List[ListApplicationsResponseApplicationsApplication]

    def validate(self):
        self.validate_required(self.application, 'application')
        if self.application:
            for k in self.application:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.application = []
        if map.get('Application') is not None:
            for k in map.get('Application'):
                temp_model = ListApplicationsResponseApplicationsApplication()
                self.application.append(temp_model.from_map(k))
        return self


class GetApplicationRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id            # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        return self


class GetApplicationResponse(TeaModel):
    def __init__(self, request_id=None, application=None):
        self.request_id = request_id    # type: str
        self.application = application  # type: GetApplicationResponseApplication

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.application, 'application')
        if self.application:
            self.application.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.application is not None:
            result['Application'] = self.application.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Application') is not None:
            temp_model = GetApplicationResponseApplication()
            self.application = temp_model.from_map(map['Application'])
        return self


class GetApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(self, name=None, description=None):
        self.name = name                # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        return self


class GetApplicationResponseApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(self, predefined_scope=None):
        self.predefined_scope = predefined_scope  # type: List[GetApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope]

    def validate(self):
        self.validate_required(self.predefined_scope, 'predefined_scope')
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.predefined_scope = []
        if map.get('PredefinedScope') is not None:
            for k in map.get('PredefinedScope'):
                temp_model = GetApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class GetApplicationResponseApplicationDelegatedScope(TeaModel):
    def __init__(self, predefined_scopes=None):
        self.predefined_scopes = predefined_scopes  # type: GetApplicationResponseApplicationDelegatedScopePredefinedScopes

    def validate(self):
        self.validate_required(self.predefined_scopes, 'predefined_scopes')
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        result = {}
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, map={}):
        if map.get('PredefinedScopes') is not None:
            temp_model = GetApplicationResponseApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(map['PredefinedScopes'])
        return self


class GetApplicationResponseApplicationRedirectUris(TeaModel):
    def __init__(self, redirect_uri=None):
        # RedirectUri
        self.redirect_uri = redirect_uri  # type: List[str]

    def validate(self):
        self.validate_required(self.redirect_uri, 'redirect_uri')

    def to_map(self):
        result = {}
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, map={}):
        if map.get('RedirectUri') is not None:
            self.redirect_uri = map.get('RedirectUri')
        return self


class GetApplicationResponseApplication(TeaModel):
    def __init__(self, app_id=None, display_name=None, app_type=None, secret_required=None,
                 access_token_validity=None, refresh_token_validity=None, is_multi_tenant=None, create_date=None, update_date=None,
                 app_name=None, account_id=None, delegated_scope=None, redirect_uris=None):
        self.app_id = app_id            # type: str
        self.display_name = display_name  # type: str
        self.app_type = app_type        # type: str
        self.secret_required = secret_required  # type: bool
        self.access_token_validity = access_token_validity  # type: int
        self.refresh_token_validity = refresh_token_validity  # type: int
        self.is_multi_tenant = is_multi_tenant  # type: bool
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.app_name = app_name        # type: str
        self.account_id = account_id    # type: str
        self.delegated_scope = delegated_scope  # type: GetApplicationResponseApplicationDelegatedScope
        self.redirect_uris = redirect_uris  # type: GetApplicationResponseApplicationRedirectUris

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.app_type, 'app_type')
        self.validate_required(self.secret_required, 'secret_required')
        self.validate_required(self.access_token_validity, 'access_token_validity')
        self.validate_required(self.refresh_token_validity, 'refresh_token_validity')
        self.validate_required(self.is_multi_tenant, 'is_multi_tenant')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.delegated_scope, 'delegated_scope')
        if self.delegated_scope:
            self.delegated_scope.validate()
        self.validate_required(self.redirect_uris, 'redirect_uris')
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('AppType') is not None:
            self.app_type = map.get('AppType')
        if map.get('SecretRequired') is not None:
            self.secret_required = map.get('SecretRequired')
        if map.get('AccessTokenValidity') is not None:
            self.access_token_validity = map.get('AccessTokenValidity')
        if map.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = map.get('RefreshTokenValidity')
        if map.get('IsMultiTenant') is not None:
            self.is_multi_tenant = map.get('IsMultiTenant')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('AppName') is not None:
            self.app_name = map.get('AppName')
        if map.get('AccountId') is not None:
            self.account_id = map.get('AccountId')
        if map.get('DelegatedScope') is not None:
            temp_model = GetApplicationResponseApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(map['DelegatedScope'])
        if map.get('RedirectUris') is not None:
            temp_model = GetApplicationResponseApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(map['RedirectUris'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id            # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class GetAppSecretRequest(TeaModel):
    def __init__(self, app_id=None, app_secret_id=None):
        self.app_id = app_id            # type: str
        self.app_secret_id = app_secret_id  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_secret_id, 'app_secret_id')

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        if map.get('AppSecretId') is not None:
            self.app_secret_id = map.get('AppSecretId')
        return self


class GetAppSecretResponse(TeaModel):
    def __init__(self, request_id=None, app_secret=None):
        self.request_id = request_id    # type: str
        self.app_secret = app_secret    # type: GetAppSecretResponseAppSecret

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.app_secret, 'app_secret')
        if self.app_secret:
            self.app_secret.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('AppSecret') is not None:
            temp_model = GetAppSecretResponseAppSecret()
            self.app_secret = temp_model.from_map(map['AppSecret'])
        return self


class GetAppSecretResponseAppSecret(TeaModel):
    def __init__(self, app_id=None, app_secret_id=None, app_secret_value=None, create_date=None):
        self.app_id = app_id            # type: str
        self.app_secret_id = app_secret_id  # type: str
        self.app_secret_value = app_secret_value  # type: str
        self.create_date = create_date  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_secret_id, 'app_secret_id')
        self.validate_required(self.app_secret_value, 'app_secret_value')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.app_secret_value is not None:
            result['AppSecretValue'] = self.app_secret_value
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        if map.get('AppSecretId') is not None:
            self.app_secret_id = map.get('AppSecretId')
        if map.get('AppSecretValue') is not None:
            self.app_secret_value = map.get('AppSecretValue')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        return self


class CreateAppSecretRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id            # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        return self


class CreateAppSecretResponse(TeaModel):
    def __init__(self, request_id=None, app_secret=None):
        self.request_id = request_id    # type: str
        self.app_secret = app_secret    # type: CreateAppSecretResponseAppSecret

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.app_secret, 'app_secret')
        if self.app_secret:
            self.app_secret.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('AppSecret') is not None:
            temp_model = CreateAppSecretResponseAppSecret()
            self.app_secret = temp_model.from_map(map['AppSecret'])
        return self


class CreateAppSecretResponseAppSecret(TeaModel):
    def __init__(self, app_id=None, app_secret_id=None, app_secret_value=None, create_date=None):
        self.app_id = app_id            # type: str
        self.app_secret_id = app_secret_id  # type: str
        self.app_secret_value = app_secret_value  # type: str
        self.create_date = create_date  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_secret_id, 'app_secret_id')
        self.validate_required(self.app_secret_value, 'app_secret_value')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.app_secret_value is not None:
            result['AppSecretValue'] = self.app_secret_value
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        if map.get('AppSecretId') is not None:
            self.app_secret_id = map.get('AppSecretId')
        if map.get('AppSecretValue') is not None:
            self.app_secret_value = map.get('AppSecretValue')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        return self


class ListPredefinedScopesRequest(TeaModel):
    def __init__(self, app_type=None):
        self.app_type = app_type        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, map={}):
        if map.get('AppType') is not None:
            self.app_type = map.get('AppType')
        return self


class ListPredefinedScopesResponse(TeaModel):
    def __init__(self, request_id=None, predefined_scopes=None):
        self.request_id = request_id    # type: str
        self.predefined_scopes = predefined_scopes  # type: ListPredefinedScopesResponsePredefinedScopes

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.predefined_scopes, 'predefined_scopes')
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('PredefinedScopes') is not None:
            temp_model = ListPredefinedScopesResponsePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(map['PredefinedScopes'])
        return self


class ListPredefinedScopesResponsePredefinedScopesPredefinedScope(TeaModel):
    def __init__(self, name=None, description=None):
        self.name = name                # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        return self


class ListPredefinedScopesResponsePredefinedScopes(TeaModel):
    def __init__(self, predefined_scope=None):
        self.predefined_scope = predefined_scope  # type: List[ListPredefinedScopesResponsePredefinedScopesPredefinedScope]

    def validate(self):
        self.validate_required(self.predefined_scope, 'predefined_scope')
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.predefined_scope = []
        if map.get('PredefinedScope') is not None:
            for k in map.get('PredefinedScope'):
                temp_model = ListPredefinedScopesResponsePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(self, display_name=None, app_type=None, redirect_uris=None, secret_required=None,
                 access_token_validity=None, refresh_token_validity=None, predefined_scopes=None, is_multi_tenant=None, app_name=None):
        self.display_name = display_name  # type: str
        self.app_type = app_type        # type: str
        self.redirect_uris = redirect_uris  # type: str
        self.secret_required = secret_required  # type: bool
        self.access_token_validity = access_token_validity  # type: int
        self.refresh_token_validity = refresh_token_validity  # type: int
        self.predefined_scopes = predefined_scopes  # type: str
        self.is_multi_tenant = is_multi_tenant  # type: bool
        self.app_name = app_name        # type: str

    def validate(self):
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.app_type, 'app_type')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('AppType') is not None:
            self.app_type = map.get('AppType')
        if map.get('RedirectUris') is not None:
            self.redirect_uris = map.get('RedirectUris')
        if map.get('SecretRequired') is not None:
            self.secret_required = map.get('SecretRequired')
        if map.get('AccessTokenValidity') is not None:
            self.access_token_validity = map.get('AccessTokenValidity')
        if map.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = map.get('RefreshTokenValidity')
        if map.get('PredefinedScopes') is not None:
            self.predefined_scopes = map.get('PredefinedScopes')
        if map.get('IsMultiTenant') is not None:
            self.is_multi_tenant = map.get('IsMultiTenant')
        if map.get('AppName') is not None:
            self.app_name = map.get('AppName')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(self, request_id=None, application=None):
        self.request_id = request_id    # type: str
        self.application = application  # type: CreateApplicationResponseApplication

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.application, 'application')
        if self.application:
            self.application.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.application is not None:
            result['Application'] = self.application.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Application') is not None:
            temp_model = CreateApplicationResponseApplication()
            self.application = temp_model.from_map(map['Application'])
        return self


class CreateApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(self, name=None, description=None):
        self.name = name                # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        return self


class CreateApplicationResponseApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(self, predefined_scope=None):
        self.predefined_scope = predefined_scope  # type: List[CreateApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope]

    def validate(self):
        self.validate_required(self.predefined_scope, 'predefined_scope')
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.predefined_scope = []
        if map.get('PredefinedScope') is not None:
            for k in map.get('PredefinedScope'):
                temp_model = CreateApplicationResponseApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class CreateApplicationResponseApplicationDelegatedScope(TeaModel):
    def __init__(self, predefined_scopes=None):
        self.predefined_scopes = predefined_scopes  # type: CreateApplicationResponseApplicationDelegatedScopePredefinedScopes

    def validate(self):
        self.validate_required(self.predefined_scopes, 'predefined_scopes')
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        result = {}
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, map={}):
        if map.get('PredefinedScopes') is not None:
            temp_model = CreateApplicationResponseApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(map['PredefinedScopes'])
        return self


class CreateApplicationResponseApplicationRedirectUris(TeaModel):
    def __init__(self, redirect_uri=None):
        # RedirectUri
        self.redirect_uri = redirect_uri  # type: List[str]

    def validate(self):
        self.validate_required(self.redirect_uri, 'redirect_uri')

    def to_map(self):
        result = {}
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, map={}):
        if map.get('RedirectUri') is not None:
            self.redirect_uri = map.get('RedirectUri')
        return self


class CreateApplicationResponseApplication(TeaModel):
    def __init__(self, app_id=None, display_name=None, app_type=None, secret_required=None,
                 access_token_validity=None, refresh_token_validity=None, is_multi_tenant=None, create_date=None, update_date=None,
                 app_name=None, account_id=None, delegated_scope=None, redirect_uris=None):
        self.app_id = app_id            # type: str
        self.display_name = display_name  # type: str
        self.app_type = app_type        # type: str
        self.secret_required = secret_required  # type: bool
        self.access_token_validity = access_token_validity  # type: int
        self.refresh_token_validity = refresh_token_validity  # type: int
        self.is_multi_tenant = is_multi_tenant  # type: bool
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.app_name = app_name        # type: str
        self.account_id = account_id    # type: str
        self.delegated_scope = delegated_scope  # type: CreateApplicationResponseApplicationDelegatedScope
        self.redirect_uris = redirect_uris  # type: CreateApplicationResponseApplicationRedirectUris

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.app_type, 'app_type')
        self.validate_required(self.secret_required, 'secret_required')
        self.validate_required(self.access_token_validity, 'access_token_validity')
        self.validate_required(self.refresh_token_validity, 'refresh_token_validity')
        self.validate_required(self.is_multi_tenant, 'is_multi_tenant')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.delegated_scope, 'delegated_scope')
        if self.delegated_scope:
            self.delegated_scope.validate()
        self.validate_required(self.redirect_uris, 'redirect_uris')
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('AppType') is not None:
            self.app_type = map.get('AppType')
        if map.get('SecretRequired') is not None:
            self.secret_required = map.get('SecretRequired')
        if map.get('AccessTokenValidity') is not None:
            self.access_token_validity = map.get('AccessTokenValidity')
        if map.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = map.get('RefreshTokenValidity')
        if map.get('IsMultiTenant') is not None:
            self.is_multi_tenant = map.get('IsMultiTenant')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('AppName') is not None:
            self.app_name = map.get('AppName')
        if map.get('AccountId') is not None:
            self.account_id = map.get('AccountId')
        if map.get('DelegatedScope') is not None:
            temp_model = CreateApplicationResponseApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(map['DelegatedScope'])
        if map.get('RedirectUris') is not None:
            temp_model = CreateApplicationResponseApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(map['RedirectUris'])
        return self


class DeleteAppSecretRequest(TeaModel):
    def __init__(self, app_id=None, app_secret_id=None):
        self.app_id = app_id            # type: str
        self.app_secret_id = app_secret_id  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_secret_id, 'app_secret_id')

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        if map.get('AppSecretId') is not None:
            self.app_secret_id = map.get('AppSecretId')
        return self


class DeleteAppSecretResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ListAppSecretIdsRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id            # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        return self


class ListAppSecretIdsResponse(TeaModel):
    def __init__(self, request_id=None, app_secrets=None):
        self.request_id = request_id    # type: str
        self.app_secrets = app_secrets  # type: ListAppSecretIdsResponseAppSecrets

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.app_secrets, 'app_secrets')
        if self.app_secrets:
            self.app_secrets.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_secrets is not None:
            result['AppSecrets'] = self.app_secrets.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('AppSecrets') is not None:
            temp_model = ListAppSecretIdsResponseAppSecrets()
            self.app_secrets = temp_model.from_map(map['AppSecrets'])
        return self


class ListAppSecretIdsResponseAppSecretsAppSecret(TeaModel):
    def __init__(self, app_id=None, app_secret_id=None, create_date=None):
        self.app_id = app_id            # type: str
        self.app_secret_id = app_secret_id  # type: str
        self.create_date = create_date  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_secret_id, 'app_secret_id')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, map={}):
        if map.get('AppId') is not None:
            self.app_id = map.get('AppId')
        if map.get('AppSecretId') is not None:
            self.app_secret_id = map.get('AppSecretId')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        return self


class ListAppSecretIdsResponseAppSecrets(TeaModel):
    def __init__(self, app_secret=None):
        self.app_secret = app_secret    # type: List[ListAppSecretIdsResponseAppSecretsAppSecret]

    def validate(self):
        self.validate_required(self.app_secret, 'app_secret')
        if self.app_secret:
            for k in self.app_secret:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AppSecret'] = []
        if self.app_secret is not None:
            for k in self.app_secret:
                result['AppSecret'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.app_secret = []
        if map.get('AppSecret') is not None:
            for k in map.get('AppSecret'):
                temp_model = ListAppSecretIdsResponseAppSecretsAppSecret()
                self.app_secret.append(temp_model.from_map(k))
        return self


class GenerateCredentialReportRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GenerateCredentialReportResponse(TeaModel):
    def __init__(self, request_id=None, state=None):
        self.request_id = request_id    # type: str
        self.state = state              # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('State') is not None:
            self.state = map.get('State')
        return self


class GetCredentialReportRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetCredentialReportResponse(TeaModel):
    def __init__(self, request_id=None, content=None, generated_time=None):
        self.request_id = request_id    # type: str
        self.content = content          # type: str
        self.generated_time = generated_time  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.content, 'content')
        self.validate_required(self.generated_time, 'generated_time')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        if self.generated_time is not None:
            result['GeneratedTime'] = self.generated_time
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Content') is not None:
            self.content = map.get('Content')
        if map.get('GeneratedTime') is not None:
            self.generated_time = map.get('GeneratedTime')
        return self


class UpdateUserRequest(TeaModel):
    def __init__(self, user_principal_name=None, user_id=None, new_user_principal_name=None, new_display_name=None,
                 new_mobile_phone=None, new_email=None, new_comments=None):
        self.user_principal_name = user_principal_name  # type: str
        self.user_id = user_id          # type: str
        self.new_user_principal_name = new_user_principal_name  # type: str
        self.new_display_name = new_display_name  # type: str
        self.new_mobile_phone = new_mobile_phone  # type: str
        self.new_email = new_email      # type: str
        self.new_comments = new_comments  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('NewUserPrincipalName') is not None:
            self.new_user_principal_name = map.get('NewUserPrincipalName')
        if map.get('NewDisplayName') is not None:
            self.new_display_name = map.get('NewDisplayName')
        if map.get('NewMobilePhone') is not None:
            self.new_mobile_phone = map.get('NewMobilePhone')
        if map.get('NewEmail') is not None:
            self.new_email = map.get('NewEmail')
        if map.get('NewComments') is not None:
            self.new_comments = map.get('NewComments')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(self, request_id=None, user=None):
        self.request_id = request_id    # type: str
        self.user = user                # type: UpdateUserResponseUser

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.user, 'user')
        if self.user:
            self.user.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('User') is not None:
            temp_model = UpdateUserResponseUser()
            self.user = temp_model.from_map(map['User'])
        return self


class UpdateUserResponseUser(TeaModel):
    def __init__(self, user_id=None, user_principal_name=None, display_name=None, comments=None, create_date=None,
                 update_date=None, last_login_date=None, mobile_phone=None, email=None):
        self.user_id = user_id          # type: str
        self.user_principal_name = user_principal_name  # type: str
        self.display_name = display_name  # type: str
        self.comments = comments        # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.last_login_date = last_login_date  # type: str
        self.mobile_phone = mobile_phone  # type: str
        self.email = email              # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.last_login_date, 'last_login_date')
        self.validate_required(self.mobile_phone, 'mobile_phone')
        self.validate_required(self.email, 'email')

    def to_map(self):
        result = {}
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, map={}):
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('Comments') is not None:
            self.comments = map.get('Comments')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('LastLoginDate') is not None:
            self.last_login_date = map.get('LastLoginDate')
        if map.get('MobilePhone') is not None:
            self.mobile_phone = map.get('MobilePhone')
        if map.get('Email') is not None:
            self.email = map.get('Email')
        return self


class UpdateSAMLProviderRequest(TeaModel):
    def __init__(self, samlprovider_name=None, new_description=None, new_encoded_samlmetadata_document=None):
        self.samlprovider_name = samlprovider_name  # type: str
        self.new_description = new_description  # type: str
        self.new_encoded_samlmetadata_document = new_encoded_samlmetadata_document  # type: str

    def validate(self):
        self.validate_required(self.samlprovider_name, 'samlprovider_name')

    def to_map(self):
        result = {}
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_encoded_samlmetadata_document is not None:
            result['NewEncodedSAMLMetadataDocument'] = self.new_encoded_samlmetadata_document
        return result

    def from_map(self, map={}):
        if map.get('SAMLProviderName') is not None:
            self.samlprovider_name = map.get('SAMLProviderName')
        if map.get('NewDescription') is not None:
            self.new_description = map.get('NewDescription')
        if map.get('NewEncodedSAMLMetadataDocument') is not None:
            self.new_encoded_samlmetadata_document = map.get('NewEncodedSAMLMetadataDocument')
        return self


class UpdateSAMLProviderResponse(TeaModel):
    def __init__(self, request_id=None, samlprovider=None):
        self.request_id = request_id    # type: str
        self.samlprovider = samlprovider  # type: UpdateSAMLProviderResponseSAMLProvider

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.samlprovider, 'samlprovider')
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('SAMLProvider') is not None:
            temp_model = UpdateSAMLProviderResponseSAMLProvider()
            self.samlprovider = temp_model.from_map(map['SAMLProvider'])
        return self


class UpdateSAMLProviderResponseSAMLProvider(TeaModel):
    def __init__(self, samlprovider_name=None, arn=None, description=None, create_date=None, update_date=None):
        self.samlprovider_name = samlprovider_name  # type: str
        self.arn = arn                  # type: str
        self.description = description  # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        self.validate_required(self.samlprovider_name, 'samlprovider_name')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.description, 'description')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')

    def to_map(self):
        result = {}
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.description is not None:
            result['Description'] = self.description
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, map={}):
        if map.get('SAMLProviderName') is not None:
            self.samlprovider_name = map.get('SAMLProviderName')
        if map.get('Arn') is not None:
            self.arn = map.get('Arn')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        return self


class UpdateLoginProfileRequest(TeaModel):
    def __init__(self, user_principal_name=None, password=None, password_reset_required=None,
                 mfabind_required=None, status=None):
        self.user_principal_name = user_principal_name  # type: str
        self.password = password        # type: str
        self.password_reset_required = password_reset_required  # type: bool
        self.mfabind_required = mfabind_required  # type: bool
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('Password') is not None:
            self.password = map.get('Password')
        if map.get('PasswordResetRequired') is not None:
            self.password_reset_required = map.get('PasswordResetRequired')
        if map.get('MFABindRequired') is not None:
            self.mfabind_required = map.get('MFABindRequired')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class UpdateLoginProfileResponse(TeaModel):
    def __init__(self, request_id=None, login_profile=None):
        self.request_id = request_id    # type: str
        self.login_profile = login_profile  # type: UpdateLoginProfileResponseLoginProfile

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.login_profile, 'login_profile')
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('LoginProfile') is not None:
            temp_model = UpdateLoginProfileResponseLoginProfile()
            self.login_profile = temp_model.from_map(map['LoginProfile'])
        return self


class UpdateLoginProfileResponseLoginProfile(TeaModel):
    def __init__(self, user_principal_name=None, password_reset_required=None, mfabind_required=None,
                 update_date=None, status=None):
        self.user_principal_name = user_principal_name  # type: str
        self.password_reset_required = password_reset_required  # type: bool
        self.mfabind_required = mfabind_required  # type: bool
        self.update_date = update_date  # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.password_reset_required, 'password_reset_required')
        self.validate_required(self.mfabind_required, 'mfabind_required')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('PasswordResetRequired') is not None:
            self.password_reset_required = map.get('PasswordResetRequired')
        if map.get('MFABindRequired') is not None:
            self.mfabind_required = map.get('MFABindRequired')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(self, new_comments=None, new_display_name=None, new_group_name=None, group_name=None):
        self.new_comments = new_comments  # type: str
        self.new_display_name = new_display_name  # type: str
        self.new_group_name = new_group_name  # type: str
        self.group_name = group_name    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.new_comments is not None:
            result['NewComments'] = self.new_comments
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.new_group_name is not None:
            result['NewGroupName'] = self.new_group_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, map={}):
        if map.get('NewComments') is not None:
            self.new_comments = map.get('NewComments')
        if map.get('NewDisplayName') is not None:
            self.new_display_name = map.get('NewDisplayName')
        if map.get('NewGroupName') is not None:
            self.new_group_name = map.get('NewGroupName')
        if map.get('GroupName') is not None:
            self.group_name = map.get('GroupName')
        return self


class UpdateGroupResponse(TeaModel):
    def __init__(self, request_id=None, group=None):
        self.request_id = request_id    # type: str
        self.group = group              # type: UpdateGroupResponseGroup

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group, 'group')
        if self.group:
            self.group.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group is not None:
            result['Group'] = self.group.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Group') is not None:
            temp_model = UpdateGroupResponseGroup()
            self.group = temp_model.from_map(map['Group'])
        return self


class UpdateGroupResponseGroup(TeaModel):
    def __init__(self, display_name=None, comments=None, create_date=None, update_date=None, group_name=None,
                 group_id=None):
        self.display_name = display_name  # type: str
        self.comments = comments        # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.group_name = group_name    # type: str
        self.group_id = group_id        # type: str

    def validate(self):
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = {}
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, map={}):
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('Comments') is not None:
            self.comments = map.get('Comments')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('GroupName') is not None:
            self.group_name = map.get('GroupName')
        if map.get('GroupId') is not None:
            self.group_id = map.get('GroupId')
        return self


class UpdateAccessKeyRequest(TeaModel):
    def __init__(self, user_principal_name=None, user_access_key_id=None, status=None):
        self.user_principal_name = user_principal_name  # type: str
        self.user_access_key_id = user_access_key_id  # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.user_access_key_id, 'user_access_key_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('UserAccessKeyId') is not None:
            self.user_access_key_id = map.get('UserAccessKeyId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class UpdateAccessKeyResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class UnbindMFADeviceRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        return self


class UnbindMFADeviceResponse(TeaModel):
    def __init__(self, request_id=None, mfadevice=None):
        self.request_id = request_id    # type: str
        self.mfadevice = mfadevice      # type: UnbindMFADeviceResponseMFADevice

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.mfadevice, 'mfadevice')
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('MFADevice') is not None:
            temp_model = UnbindMFADeviceResponseMFADevice()
            self.mfadevice = temp_model.from_map(map['MFADevice'])
        return self


class UnbindMFADeviceResponseMFADevice(TeaModel):
    def __init__(self, serial_number=None):
        self.serial_number = serial_number  # type: str

    def validate(self):
        self.validate_required(self.serial_number, 'serial_number')

    def to_map(self):
        result = {}
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, map={}):
        if map.get('SerialNumber') is not None:
            self.serial_number = map.get('SerialNumber')
        return self


class SetSecurityPreferenceRequest(TeaModel):
    def __init__(self, enable_save_mfaticket=None, allow_user_to_change_password=None,
                 allow_user_to_manage_access_keys=None, allow_user_to_manage_mfadevices=None, login_session_duration=None,
                 login_network_masks=None):
        self.enable_save_mfaticket = enable_save_mfaticket  # type: bool
        self.allow_user_to_change_password = allow_user_to_change_password  # type: bool
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys  # type: bool
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices  # type: bool
        self.login_session_duration = login_session_duration  # type: int
        self.login_network_masks = login_network_masks  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = map.get('EnableSaveMFATicket')
        if map.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = map.get('AllowUserToChangePassword')
        if map.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = map.get('AllowUserToManageAccessKeys')
        if map.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = map.get('AllowUserToManageMFADevices')
        if map.get('LoginSessionDuration') is not None:
            self.login_session_duration = map.get('LoginSessionDuration')
        if map.get('LoginNetworkMasks') is not None:
            self.login_network_masks = map.get('LoginNetworkMasks')
        return self


class SetSecurityPreferenceResponse(TeaModel):
    def __init__(self, request_id=None, security_preference=None):
        self.request_id = request_id    # type: str
        self.security_preference = security_preference  # type: SetSecurityPreferenceResponseSecurityPreference

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.security_preference, 'security_preference')
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('SecurityPreference') is not None:
            temp_model = SetSecurityPreferenceResponseSecurityPreference()
            self.security_preference = temp_model.from_map(map['SecurityPreference'])
        return self


class SetSecurityPreferenceResponseSecurityPreferenceLoginProfilePreference(TeaModel):
    def __init__(self, enable_save_mfaticket=None, allow_user_to_change_password=None,
                 login_session_duration=None, login_network_masks=None):
        self.enable_save_mfaticket = enable_save_mfaticket  # type: bool
        self.allow_user_to_change_password = allow_user_to_change_password  # type: bool
        self.login_session_duration = login_session_duration  # type: int
        self.login_network_masks = login_network_masks  # type: str

    def validate(self):
        self.validate_required(self.enable_save_mfaticket, 'enable_save_mfaticket')
        self.validate_required(self.allow_user_to_change_password, 'allow_user_to_change_password')
        self.validate_required(self.login_session_duration, 'login_session_duration')
        self.validate_required(self.login_network_masks, 'login_network_masks')

    def to_map(self):
        result = {}
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        return result

    def from_map(self, map={}):
        if map.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = map.get('EnableSaveMFATicket')
        if map.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = map.get('AllowUserToChangePassword')
        if map.get('LoginSessionDuration') is not None:
            self.login_session_duration = map.get('LoginSessionDuration')
        if map.get('LoginNetworkMasks') is not None:
            self.login_network_masks = map.get('LoginNetworkMasks')
        return self


class SetSecurityPreferenceResponseSecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(self, allow_user_to_manage_access_keys=None):
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys  # type: bool

    def validate(self):
        self.validate_required(self.allow_user_to_manage_access_keys, 'allow_user_to_manage_access_keys')

    def to_map(self):
        result = {}
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        return result

    def from_map(self, map={}):
        if map.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = map.get('AllowUserToManageAccessKeys')
        return self


class SetSecurityPreferenceResponseSecurityPreferenceMFAPreference(TeaModel):
    def __init__(self, allow_user_to_manage_mfadevices=None):
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices  # type: bool

    def validate(self):
        self.validate_required(self.allow_user_to_manage_mfadevices, 'allow_user_to_manage_mfadevices')

    def to_map(self):
        result = {}
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        return result

    def from_map(self, map={}):
        if map.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = map.get('AllowUserToManageMFADevices')
        return self


class SetSecurityPreferenceResponseSecurityPreference(TeaModel):
    def __init__(self, login_profile_preference=None, access_key_preference=None, mfapreference=None):
        self.login_profile_preference = login_profile_preference  # type: SetSecurityPreferenceResponseSecurityPreferenceLoginProfilePreference
        self.access_key_preference = access_key_preference  # type: SetSecurityPreferenceResponseSecurityPreferenceAccessKeyPreference
        self.mfapreference = mfapreference  # type: SetSecurityPreferenceResponseSecurityPreferenceMFAPreference

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
        result = {}
        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()
        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()
        return result

    def from_map(self, map={}):
        if map.get('LoginProfilePreference') is not None:
            temp_model = SetSecurityPreferenceResponseSecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(map['LoginProfilePreference'])
        if map.get('AccessKeyPreference') is not None:
            temp_model = SetSecurityPreferenceResponseSecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(map['AccessKeyPreference'])
        if map.get('MFAPreference') is not None:
            temp_model = SetSecurityPreferenceResponseSecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(map['MFAPreference'])
        return self


class SetPasswordPolicyRequest(TeaModel):
    def __init__(self, minimum_password_length=None, require_lowercase_characters=None,
                 require_uppercase_characters=None, require_numbers=None, require_symbols=None, hard_expire=None, max_login_attemps=None,
                 password_reuse_prevention=None, max_password_age=None, minimum_password_different_character=None,
                 password_not_contain_user_name=None):
        self.minimum_password_length = minimum_password_length  # type: int
        self.require_lowercase_characters = require_lowercase_characters  # type: bool
        self.require_uppercase_characters = require_uppercase_characters  # type: bool
        self.require_numbers = require_numbers  # type: bool
        self.require_symbols = require_symbols  # type: bool
        self.hard_expire = hard_expire  # type: bool
        self.max_login_attemps = max_login_attemps  # type: int
        self.password_reuse_prevention = password_reuse_prevention  # type: int
        self.max_password_age = max_password_age  # type: int
        self.minimum_password_different_character = minimum_password_different_character  # type: int
        self.password_not_contain_user_name = password_not_contain_user_name  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = map.get('MinimumPasswordLength')
        if map.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = map.get('RequireLowercaseCharacters')
        if map.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = map.get('RequireUppercaseCharacters')
        if map.get('RequireNumbers') is not None:
            self.require_numbers = map.get('RequireNumbers')
        if map.get('RequireSymbols') is not None:
            self.require_symbols = map.get('RequireSymbols')
        if map.get('HardExpire') is not None:
            self.hard_expire = map.get('HardExpire')
        if map.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = map.get('MaxLoginAttemps')
        if map.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = map.get('PasswordReusePrevention')
        if map.get('MaxPasswordAge') is not None:
            self.max_password_age = map.get('MaxPasswordAge')
        if map.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = map.get('MinimumPasswordDifferentCharacter')
        if map.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = map.get('PasswordNotContainUserName')
        return self


class SetPasswordPolicyResponse(TeaModel):
    def __init__(self, request_id=None, password_policy=None):
        self.request_id = request_id    # type: str
        self.password_policy = password_policy  # type: SetPasswordPolicyResponsePasswordPolicy

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.password_policy, 'password_policy')
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('PasswordPolicy') is not None:
            temp_model = SetPasswordPolicyResponsePasswordPolicy()
            self.password_policy = temp_model.from_map(map['PasswordPolicy'])
        return self


class SetPasswordPolicyResponsePasswordPolicy(TeaModel):
    def __init__(self, minimum_password_length=None, require_lowercase_characters=None,
                 require_uppercase_characters=None, require_numbers=None, require_symbols=None, hard_expire=None, max_login_attemps=None,
                 password_reuse_prevention=None, max_password_age=None, minimum_password_different_character=None,
                 password_not_contain_user_name=None):
        self.minimum_password_length = minimum_password_length  # type: int
        self.require_lowercase_characters = require_lowercase_characters  # type: bool
        self.require_uppercase_characters = require_uppercase_characters  # type: bool
        self.require_numbers = require_numbers  # type: bool
        self.require_symbols = require_symbols  # type: bool
        self.hard_expire = hard_expire  # type: bool
        self.max_login_attemps = max_login_attemps  # type: int
        self.password_reuse_prevention = password_reuse_prevention  # type: int
        self.max_password_age = max_password_age  # type: int
        self.minimum_password_different_character = minimum_password_different_character  # type: int
        self.password_not_contain_user_name = password_not_contain_user_name  # type: bool

    def validate(self):
        self.validate_required(self.minimum_password_length, 'minimum_password_length')
        self.validate_required(self.require_lowercase_characters, 'require_lowercase_characters')
        self.validate_required(self.require_uppercase_characters, 'require_uppercase_characters')
        self.validate_required(self.require_numbers, 'require_numbers')
        self.validate_required(self.require_symbols, 'require_symbols')
        self.validate_required(self.hard_expire, 'hard_expire')
        self.validate_required(self.max_login_attemps, 'max_login_attemps')
        self.validate_required(self.password_reuse_prevention, 'password_reuse_prevention')
        self.validate_required(self.max_password_age, 'max_password_age')
        self.validate_required(self.minimum_password_different_character, 'minimum_password_different_character')
        self.validate_required(self.password_not_contain_user_name, 'password_not_contain_user_name')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = map.get('MinimumPasswordLength')
        if map.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = map.get('RequireLowercaseCharacters')
        if map.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = map.get('RequireUppercaseCharacters')
        if map.get('RequireNumbers') is not None:
            self.require_numbers = map.get('RequireNumbers')
        if map.get('RequireSymbols') is not None:
            self.require_symbols = map.get('RequireSymbols')
        if map.get('HardExpire') is not None:
            self.hard_expire = map.get('HardExpire')
        if map.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = map.get('MaxLoginAttemps')
        if map.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = map.get('PasswordReusePrevention')
        if map.get('MaxPasswordAge') is not None:
            self.max_password_age = map.get('MaxPasswordAge')
        if map.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = map.get('MinimumPasswordDifferentCharacter')
        if map.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = map.get('PasswordNotContainUserName')
        return self


class RemoveUserFromGroupRequest(TeaModel):
    def __init__(self, user_principal_name=None, group_name=None):
        self.user_principal_name = user_principal_name  # type: str
        self.group_name = group_name    # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('GroupName') is not None:
            self.group_name = map.get('GroupName')
        return self


class RemoveUserFromGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ListVirtualMFADevicesRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        self.marker = marker            # type: str
        self.max_items = max_items      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, map={}):
        if map.get('Marker') is not None:
            self.marker = map.get('Marker')
        if map.get('MaxItems') is not None:
            self.max_items = map.get('MaxItems')
        return self


class ListVirtualMFADevicesResponse(TeaModel):
    def __init__(self, request_id=None, is_truncated=None, marker=None, virtual_mfadevices=None):
        self.request_id = request_id    # type: str
        self.is_truncated = is_truncated  # type: bool
        self.marker = marker            # type: str
        self.virtual_mfadevices = virtual_mfadevices  # type: ListVirtualMFADevicesResponseVirtualMFADevices

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_truncated, 'is_truncated')
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.virtual_mfadevices, 'virtual_mfadevices')
        if self.virtual_mfadevices:
            self.virtual_mfadevices.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.virtual_mfadevices is not None:
            result['VirtualMFADevices'] = self.virtual_mfadevices.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('IsTruncated') is not None:
            self.is_truncated = map.get('IsTruncated')
        if map.get('Marker') is not None:
            self.marker = map.get('Marker')
        if map.get('VirtualMFADevices') is not None:
            temp_model = ListVirtualMFADevicesResponseVirtualMFADevices()
            self.virtual_mfadevices = temp_model.from_map(map['VirtualMFADevices'])
        return self


class ListVirtualMFADevicesResponseVirtualMFADevicesVirtualMFADeviceUser(TeaModel):
    def __init__(self, user_principal_name=None, user_id=None, display_name=None):
        self.user_principal_name = user_principal_name  # type: str
        self.user_id = user_id          # type: str
        self.display_name = display_name  # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.display_name, 'display_name')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        return self


class ListVirtualMFADevicesResponseVirtualMFADevicesVirtualMFADevice(TeaModel):
    def __init__(self, serial_number=None, activate_date=None, user=None):
        self.serial_number = serial_number  # type: str
        self.activate_date = activate_date  # type: str
        self.user = user                # type: ListVirtualMFADevicesResponseVirtualMFADevicesVirtualMFADeviceUser

    def validate(self):
        self.validate_required(self.serial_number, 'serial_number')
        self.validate_required(self.activate_date, 'activate_date')
        self.validate_required(self.user, 'user')
        if self.user:
            self.user.validate()

    def to_map(self):
        result = {}
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.activate_date is not None:
            result['ActivateDate'] = self.activate_date
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, map={}):
        if map.get('SerialNumber') is not None:
            self.serial_number = map.get('SerialNumber')
        if map.get('ActivateDate') is not None:
            self.activate_date = map.get('ActivateDate')
        if map.get('User') is not None:
            temp_model = ListVirtualMFADevicesResponseVirtualMFADevicesVirtualMFADeviceUser()
            self.user = temp_model.from_map(map['User'])
        return self


class ListVirtualMFADevicesResponseVirtualMFADevices(TeaModel):
    def __init__(self, virtual_mfadevice=None):
        self.virtual_mfadevice = virtual_mfadevice  # type: List[ListVirtualMFADevicesResponseVirtualMFADevicesVirtualMFADevice]

    def validate(self):
        self.validate_required(self.virtual_mfadevice, 'virtual_mfadevice')
        if self.virtual_mfadevice:
            for k in self.virtual_mfadevice:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VirtualMFADevice'] = []
        if self.virtual_mfadevice is not None:
            for k in self.virtual_mfadevice:
                result['VirtualMFADevice'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.virtual_mfadevice = []
        if map.get('VirtualMFADevice') is not None:
            for k in map.get('VirtualMFADevice'):
                temp_model = ListVirtualMFADevicesResponseVirtualMFADevicesVirtualMFADevice()
                self.virtual_mfadevice.append(temp_model.from_map(k))
        return self


class ListUsersForGroupRequest(TeaModel):
    def __init__(self, group_name=None, marker=None, max_items=None):
        self.group_name = group_name    # type: str
        self.marker = marker            # type: str
        self.max_items = max_items      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, map={}):
        if map.get('GroupName') is not None:
            self.group_name = map.get('GroupName')
        if map.get('Marker') is not None:
            self.marker = map.get('Marker')
        if map.get('MaxItems') is not None:
            self.max_items = map.get('MaxItems')
        return self


class ListUsersForGroupResponse(TeaModel):
    def __init__(self, request_id=None, marker=None, is_truncated=None, users=None):
        self.request_id = request_id    # type: str
        self.marker = marker            # type: str
        self.is_truncated = is_truncated  # type: bool
        self.users = users              # type: ListUsersForGroupResponseUsers

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.is_truncated, 'is_truncated')
        self.validate_required(self.users, 'users')
        if self.users:
            self.users.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Marker') is not None:
            self.marker = map.get('Marker')
        if map.get('IsTruncated') is not None:
            self.is_truncated = map.get('IsTruncated')
        if map.get('Users') is not None:
            temp_model = ListUsersForGroupResponseUsers()
            self.users = temp_model.from_map(map['Users'])
        return self


class ListUsersForGroupResponseUsersUser(TeaModel):
    def __init__(self, user_id=None, user_principal_name=None, display_name=None, join_date=None):
        self.user_id = user_id          # type: str
        self.user_principal_name = user_principal_name  # type: str
        self.display_name = display_name  # type: str
        self.join_date = join_date      # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.join_date, 'join_date')

    def to_map(self):
        result = {}
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.join_date is not None:
            result['JoinDate'] = self.join_date
        return result

    def from_map(self, map={}):
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('JoinDate') is not None:
            self.join_date = map.get('JoinDate')
        return self


class ListUsersForGroupResponseUsers(TeaModel):
    def __init__(self, user=None):
        self.user = user                # type: List[ListUsersForGroupResponseUsersUser]

    def validate(self):
        self.validate_required(self.user, 'user')
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.user = []
        if map.get('User') is not None:
            for k in map.get('User'):
                temp_model = ListUsersForGroupResponseUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        self.marker = marker            # type: str
        self.max_items = max_items      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, map={}):
        if map.get('Marker') is not None:
            self.marker = map.get('Marker')
        if map.get('MaxItems') is not None:
            self.max_items = map.get('MaxItems')
        return self


class ListUsersResponse(TeaModel):
    def __init__(self, request_id=None, marker=None, is_truncated=None, users=None):
        self.request_id = request_id    # type: str
        self.marker = marker            # type: str
        self.is_truncated = is_truncated  # type: bool
        self.users = users              # type: ListUsersResponseUsers

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.is_truncated, 'is_truncated')
        self.validate_required(self.users, 'users')
        if self.users:
            self.users.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Marker') is not None:
            self.marker = map.get('Marker')
        if map.get('IsTruncated') is not None:
            self.is_truncated = map.get('IsTruncated')
        if map.get('Users') is not None:
            temp_model = ListUsersResponseUsers()
            self.users = temp_model.from_map(map['Users'])
        return self


class ListUsersResponseUsersUser(TeaModel):
    def __init__(self, user_id=None, user_principal_name=None, display_name=None, comments=None, create_date=None,
                 update_date=None, last_login_date=None, mobile_phone=None, email=None):
        self.user_id = user_id          # type: str
        self.user_principal_name = user_principal_name  # type: str
        self.display_name = display_name  # type: str
        self.comments = comments        # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.last_login_date = last_login_date  # type: str
        self.mobile_phone = mobile_phone  # type: str
        self.email = email              # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.last_login_date, 'last_login_date')
        self.validate_required(self.mobile_phone, 'mobile_phone')
        self.validate_required(self.email, 'email')

    def to_map(self):
        result = {}
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, map={}):
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('Comments') is not None:
            self.comments = map.get('Comments')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('LastLoginDate') is not None:
            self.last_login_date = map.get('LastLoginDate')
        if map.get('MobilePhone') is not None:
            self.mobile_phone = map.get('MobilePhone')
        if map.get('Email') is not None:
            self.email = map.get('Email')
        return self


class ListUsersResponseUsers(TeaModel):
    def __init__(self, user=None):
        self.user = user                # type: List[ListUsersResponseUsersUser]

    def validate(self):
        self.validate_required(self.user, 'user')
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.user = []
        if map.get('User') is not None:
            for k in map.get('User'):
                temp_model = ListUsersResponseUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListSAMLProvidersRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        self.marker = marker            # type: str
        self.max_items = max_items      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, map={}):
        if map.get('Marker') is not None:
            self.marker = map.get('Marker')
        if map.get('MaxItems') is not None:
            self.max_items = map.get('MaxItems')
        return self


class ListSAMLProvidersResponse(TeaModel):
    def __init__(self, request_id=None, is_truncated=None, marker=None, samlproviders=None):
        self.request_id = request_id    # type: str
        self.is_truncated = is_truncated  # type: bool
        self.marker = marker            # type: str
        self.samlproviders = samlproviders  # type: ListSAMLProvidersResponseSAMLProviders

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_truncated, 'is_truncated')
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.samlproviders, 'samlproviders')
        if self.samlproviders:
            self.samlproviders.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.samlproviders is not None:
            result['SAMLProviders'] = self.samlproviders.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('IsTruncated') is not None:
            self.is_truncated = map.get('IsTruncated')
        if map.get('Marker') is not None:
            self.marker = map.get('Marker')
        if map.get('SAMLProviders') is not None:
            temp_model = ListSAMLProvidersResponseSAMLProviders()
            self.samlproviders = temp_model.from_map(map['SAMLProviders'])
        return self


class ListSAMLProvidersResponseSAMLProvidersSAMLProvider(TeaModel):
    def __init__(self, samlprovider_name=None, arn=None, description=None, create_date=None, update_date=None):
        self.samlprovider_name = samlprovider_name  # type: str
        self.arn = arn                  # type: str
        self.description = description  # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        self.validate_required(self.samlprovider_name, 'samlprovider_name')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.description, 'description')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')

    def to_map(self):
        result = {}
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.description is not None:
            result['Description'] = self.description
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, map={}):
        if map.get('SAMLProviderName') is not None:
            self.samlprovider_name = map.get('SAMLProviderName')
        if map.get('Arn') is not None:
            self.arn = map.get('Arn')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        return self


class ListSAMLProvidersResponseSAMLProviders(TeaModel):
    def __init__(self, samlprovider=None):
        self.samlprovider = samlprovider  # type: List[ListSAMLProvidersResponseSAMLProvidersSAMLProvider]

    def validate(self):
        self.validate_required(self.samlprovider, 'samlprovider')
        if self.samlprovider:
            for k in self.samlprovider:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SAMLProvider'] = []
        if self.samlprovider is not None:
            for k in self.samlprovider:
                result['SAMLProvider'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.samlprovider = []
        if map.get('SAMLProvider') is not None:
            for k in map.get('SAMLProvider'):
                temp_model = ListSAMLProvidersResponseSAMLProvidersSAMLProvider()
                self.samlprovider.append(temp_model.from_map(k))
        return self


class ListGroupsForUserRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        return self


class ListGroupsForUserResponse(TeaModel):
    def __init__(self, request_id=None, groups=None):
        self.request_id = request_id    # type: str
        self.groups = groups            # type: ListGroupsForUserResponseGroups

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.groups, 'groups')
        if self.groups:
            self.groups.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Groups') is not None:
            temp_model = ListGroupsForUserResponseGroups()
            self.groups = temp_model.from_map(map['Groups'])
        return self


class ListGroupsForUserResponseGroupsGroup(TeaModel):
    def __init__(self, display_name=None, comments=None, join_date=None, group_name=None, group_id=None):
        self.display_name = display_name  # type: str
        self.comments = comments        # type: str
        self.join_date = join_date      # type: str
        self.group_name = group_name    # type: str
        self.group_id = group_id        # type: str

    def validate(self):
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.join_date, 'join_date')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = {}
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.join_date is not None:
            result['JoinDate'] = self.join_date
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, map={}):
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('Comments') is not None:
            self.comments = map.get('Comments')
        if map.get('JoinDate') is not None:
            self.join_date = map.get('JoinDate')
        if map.get('GroupName') is not None:
            self.group_name = map.get('GroupName')
        if map.get('GroupId') is not None:
            self.group_id = map.get('GroupId')
        return self


class ListGroupsForUserResponseGroups(TeaModel):
    def __init__(self, group=None):
        self.group = group              # type: List[ListGroupsForUserResponseGroupsGroup]

    def validate(self):
        self.validate_required(self.group, 'group')
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.group = []
        if map.get('Group') is not None:
            for k in map.get('Group'):
                temp_model = ListGroupsForUserResponseGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListGroupsRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        self.marker = marker            # type: str
        self.max_items = max_items      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, map={}):
        if map.get('Marker') is not None:
            self.marker = map.get('Marker')
        if map.get('MaxItems') is not None:
            self.max_items = map.get('MaxItems')
        return self


class ListGroupsResponse(TeaModel):
    def __init__(self, request_id=None, is_truncated=None, marker=None, groups=None):
        self.request_id = request_id    # type: str
        self.is_truncated = is_truncated  # type: bool
        self.marker = marker            # type: str
        self.groups = groups            # type: ListGroupsResponseGroups

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_truncated, 'is_truncated')
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.groups, 'groups')
        if self.groups:
            self.groups.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('IsTruncated') is not None:
            self.is_truncated = map.get('IsTruncated')
        if map.get('Marker') is not None:
            self.marker = map.get('Marker')
        if map.get('Groups') is not None:
            temp_model = ListGroupsResponseGroups()
            self.groups = temp_model.from_map(map['Groups'])
        return self


class ListGroupsResponseGroupsGroup(TeaModel):
    def __init__(self, display_name=None, comments=None, create_date=None, update_date=None, group_name=None,
                 group_id=None):
        self.display_name = display_name  # type: str
        self.comments = comments        # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.group_name = group_name    # type: str
        self.group_id = group_id        # type: str

    def validate(self):
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = {}
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, map={}):
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('Comments') is not None:
            self.comments = map.get('Comments')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('GroupName') is not None:
            self.group_name = map.get('GroupName')
        if map.get('GroupId') is not None:
            self.group_id = map.get('GroupId')
        return self


class ListGroupsResponseGroups(TeaModel):
    def __init__(self, group=None):
        self.group = group              # type: List[ListGroupsResponseGroupsGroup]

    def validate(self):
        self.validate_required(self.group, 'group')
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.group = []
        if map.get('Group') is not None:
            for k in map.get('Group'):
                temp_model = ListGroupsResponseGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListAccessKeysRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        return self


class ListAccessKeysResponse(TeaModel):
    def __init__(self, request_id=None, access_keys=None):
        self.request_id = request_id    # type: str
        self.access_keys = access_keys  # type: ListAccessKeysResponseAccessKeys

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.access_keys, 'access_keys')
        if self.access_keys:
            self.access_keys.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_keys is not None:
            result['AccessKeys'] = self.access_keys.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('AccessKeys') is not None:
            temp_model = ListAccessKeysResponseAccessKeys()
            self.access_keys = temp_model.from_map(map['AccessKeys'])
        return self


class ListAccessKeysResponseAccessKeysAccessKey(TeaModel):
    def __init__(self, access_key_id=None, create_date=None, update_date=None, status=None):
        self.access_key_id = access_key_id  # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.access_key_id, 'access_key_id')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('AccessKeyId') is not None:
            self.access_key_id = map.get('AccessKeyId')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class ListAccessKeysResponseAccessKeys(TeaModel):
    def __init__(self, access_key=None):
        self.access_key = access_key    # type: List[ListAccessKeysResponseAccessKeysAccessKey]

    def validate(self):
        self.validate_required(self.access_key, 'access_key')
        if self.access_key:
            for k in self.access_key:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AccessKey'] = []
        if self.access_key is not None:
            for k in self.access_key:
                result['AccessKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.access_key = []
        if map.get('AccessKey') is not None:
            for k in map.get('AccessKey'):
                temp_model = ListAccessKeysResponseAccessKeysAccessKey()
                self.access_key.append(temp_model.from_map(k))
        return self


class GetUserMFAInfoRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        return self


class GetUserMFAInfoResponse(TeaModel):
    def __init__(self, request_id=None, is_mfaenable=None, mfadevice=None):
        self.request_id = request_id    # type: str
        self.is_mfaenable = is_mfaenable  # type: bool
        self.mfadevice = mfadevice      # type: GetUserMFAInfoResponseMFADevice

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_mfaenable, 'is_mfaenable')
        self.validate_required(self.mfadevice, 'mfadevice')
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_mfaenable is not None:
            result['IsMFAEnable'] = self.is_mfaenable
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('IsMFAEnable') is not None:
            self.is_mfaenable = map.get('IsMFAEnable')
        if map.get('MFADevice') is not None:
            temp_model = GetUserMFAInfoResponseMFADevice()
            self.mfadevice = temp_model.from_map(map['MFADevice'])
        return self


class GetUserMFAInfoResponseMFADevice(TeaModel):
    def __init__(self, serial_number=None):
        self.serial_number = serial_number  # type: str

    def validate(self):
        self.validate_required(self.serial_number, 'serial_number')

    def to_map(self):
        result = {}
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, map={}):
        if map.get('SerialNumber') is not None:
            self.serial_number = map.get('SerialNumber')
        return self


class GetUserRequest(TeaModel):
    def __init__(self, user_principal_name=None, user_id=None, user_access_key_id=None):
        self.user_principal_name = user_principal_name  # type: str
        self.user_id = user_id          # type: str
        self.user_access_key_id = user_access_key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('UserAccessKeyId') is not None:
            self.user_access_key_id = map.get('UserAccessKeyId')
        return self


class GetUserResponse(TeaModel):
    def __init__(self, request_id=None, user=None):
        self.request_id = request_id    # type: str
        self.user = user                # type: GetUserResponseUser

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.user, 'user')
        if self.user:
            self.user.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('User') is not None:
            temp_model = GetUserResponseUser()
            self.user = temp_model.from_map(map['User'])
        return self


class GetUserResponseUser(TeaModel):
    def __init__(self, user_id=None, user_principal_name=None, display_name=None, comments=None, create_date=None,
                 update_date=None, last_login_date=None, mobile_phone=None, email=None):
        self.user_id = user_id          # type: str
        self.user_principal_name = user_principal_name  # type: str
        self.display_name = display_name  # type: str
        self.comments = comments        # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.last_login_date = last_login_date  # type: str
        self.mobile_phone = mobile_phone  # type: str
        self.email = email              # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.last_login_date, 'last_login_date')
        self.validate_required(self.mobile_phone, 'mobile_phone')
        self.validate_required(self.email, 'email')

    def to_map(self):
        result = {}
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, map={}):
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('Comments') is not None:
            self.comments = map.get('Comments')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('LastLoginDate') is not None:
            self.last_login_date = map.get('LastLoginDate')
        if map.get('MobilePhone') is not None:
            self.mobile_phone = map.get('MobilePhone')
        if map.get('Email') is not None:
            self.email = map.get('Email')
        return self


class GetSecurityPreferenceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetSecurityPreferenceResponse(TeaModel):
    def __init__(self, request_id=None, security_preference=None):
        self.request_id = request_id    # type: str
        self.security_preference = security_preference  # type: GetSecurityPreferenceResponseSecurityPreference

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.security_preference, 'security_preference')
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('SecurityPreference') is not None:
            temp_model = GetSecurityPreferenceResponseSecurityPreference()
            self.security_preference = temp_model.from_map(map['SecurityPreference'])
        return self


class GetSecurityPreferenceResponseSecurityPreferenceLoginProfilePreference(TeaModel):
    def __init__(self, enable_save_mfaticket=None, allow_user_to_change_password=None,
                 login_session_duration=None, login_network_masks=None):
        self.enable_save_mfaticket = enable_save_mfaticket  # type: bool
        self.allow_user_to_change_password = allow_user_to_change_password  # type: bool
        self.login_session_duration = login_session_duration  # type: int
        self.login_network_masks = login_network_masks  # type: str

    def validate(self):
        self.validate_required(self.enable_save_mfaticket, 'enable_save_mfaticket')
        self.validate_required(self.allow_user_to_change_password, 'allow_user_to_change_password')
        self.validate_required(self.login_session_duration, 'login_session_duration')
        self.validate_required(self.login_network_masks, 'login_network_masks')

    def to_map(self):
        result = {}
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        return result

    def from_map(self, map={}):
        if map.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = map.get('EnableSaveMFATicket')
        if map.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = map.get('AllowUserToChangePassword')
        if map.get('LoginSessionDuration') is not None:
            self.login_session_duration = map.get('LoginSessionDuration')
        if map.get('LoginNetworkMasks') is not None:
            self.login_network_masks = map.get('LoginNetworkMasks')
        return self


class GetSecurityPreferenceResponseSecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(self, allow_user_to_manage_access_keys=None):
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys  # type: bool

    def validate(self):
        self.validate_required(self.allow_user_to_manage_access_keys, 'allow_user_to_manage_access_keys')

    def to_map(self):
        result = {}
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        return result

    def from_map(self, map={}):
        if map.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = map.get('AllowUserToManageAccessKeys')
        return self


class GetSecurityPreferenceResponseSecurityPreferenceMFAPreference(TeaModel):
    def __init__(self, allow_user_to_manage_mfadevices=None):
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices  # type: bool

    def validate(self):
        self.validate_required(self.allow_user_to_manage_mfadevices, 'allow_user_to_manage_mfadevices')

    def to_map(self):
        result = {}
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        return result

    def from_map(self, map={}):
        if map.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = map.get('AllowUserToManageMFADevices')
        return self


class GetSecurityPreferenceResponseSecurityPreference(TeaModel):
    def __init__(self, login_profile_preference=None, access_key_preference=None, mfapreference=None):
        self.login_profile_preference = login_profile_preference  # type: GetSecurityPreferenceResponseSecurityPreferenceLoginProfilePreference
        self.access_key_preference = access_key_preference  # type: GetSecurityPreferenceResponseSecurityPreferenceAccessKeyPreference
        self.mfapreference = mfapreference  # type: GetSecurityPreferenceResponseSecurityPreferenceMFAPreference

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
        result = {}
        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()
        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()
        return result

    def from_map(self, map={}):
        if map.get('LoginProfilePreference') is not None:
            temp_model = GetSecurityPreferenceResponseSecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(map['LoginProfilePreference'])
        if map.get('AccessKeyPreference') is not None:
            temp_model = GetSecurityPreferenceResponseSecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(map['AccessKeyPreference'])
        if map.get('MFAPreference') is not None:
            temp_model = GetSecurityPreferenceResponseSecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(map['MFAPreference'])
        return self


class GetSAMLProviderRequest(TeaModel):
    def __init__(self, samlprovider_name=None):
        self.samlprovider_name = samlprovider_name  # type: str

    def validate(self):
        self.validate_required(self.samlprovider_name, 'samlprovider_name')

    def to_map(self):
        result = {}
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        return result

    def from_map(self, map={}):
        if map.get('SAMLProviderName') is not None:
            self.samlprovider_name = map.get('SAMLProviderName')
        return self


class GetSAMLProviderResponse(TeaModel):
    def __init__(self, request_id=None, samlprovider=None):
        self.request_id = request_id    # type: str
        self.samlprovider = samlprovider  # type: GetSAMLProviderResponseSAMLProvider

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.samlprovider, 'samlprovider')
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('SAMLProvider') is not None:
            temp_model = GetSAMLProviderResponseSAMLProvider()
            self.samlprovider = temp_model.from_map(map['SAMLProvider'])
        return self


class GetSAMLProviderResponseSAMLProvider(TeaModel):
    def __init__(self, samlprovider_name=None, arn=None, description=None, create_date=None, update_date=None,
                 encoded_samlmetadata_document=None):
        self.samlprovider_name = samlprovider_name  # type: str
        self.arn = arn                  # type: str
        self.description = description  # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.encoded_samlmetadata_document = encoded_samlmetadata_document  # type: str

    def validate(self):
        self.validate_required(self.samlprovider_name, 'samlprovider_name')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.description, 'description')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.encoded_samlmetadata_document, 'encoded_samlmetadata_document')

    def to_map(self):
        result = {}
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.description is not None:
            result['Description'] = self.description
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.encoded_samlmetadata_document is not None:
            result['EncodedSAMLMetadataDocument'] = self.encoded_samlmetadata_document
        return result

    def from_map(self, map={}):
        if map.get('SAMLProviderName') is not None:
            self.samlprovider_name = map.get('SAMLProviderName')
        if map.get('Arn') is not None:
            self.arn = map.get('Arn')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('EncodedSAMLMetadataDocument') is not None:
            self.encoded_samlmetadata_document = map.get('EncodedSAMLMetadataDocument')
        return self


class GetPasswordPolicyRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetPasswordPolicyResponse(TeaModel):
    def __init__(self, request_id=None, password_policy=None):
        self.request_id = request_id    # type: str
        self.password_policy = password_policy  # type: GetPasswordPolicyResponsePasswordPolicy

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.password_policy, 'password_policy')
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('PasswordPolicy') is not None:
            temp_model = GetPasswordPolicyResponsePasswordPolicy()
            self.password_policy = temp_model.from_map(map['PasswordPolicy'])
        return self


class GetPasswordPolicyResponsePasswordPolicy(TeaModel):
    def __init__(self, minimum_password_length=None, require_lowercase_characters=None,
                 require_uppercase_characters=None, require_numbers=None, require_symbols=None, hard_expire=None, max_login_attemps=None,
                 password_reuse_prevention=None, max_password_age=None, minimum_password_different_character=None,
                 password_not_contain_user_name=None):
        self.minimum_password_length = minimum_password_length  # type: int
        self.require_lowercase_characters = require_lowercase_characters  # type: bool
        self.require_uppercase_characters = require_uppercase_characters  # type: bool
        self.require_numbers = require_numbers  # type: bool
        self.require_symbols = require_symbols  # type: bool
        self.hard_expire = hard_expire  # type: bool
        self.max_login_attemps = max_login_attemps  # type: int
        self.password_reuse_prevention = password_reuse_prevention  # type: int
        self.max_password_age = max_password_age  # type: int
        self.minimum_password_different_character = minimum_password_different_character  # type: int
        self.password_not_contain_user_name = password_not_contain_user_name  # type: bool

    def validate(self):
        self.validate_required(self.minimum_password_length, 'minimum_password_length')
        self.validate_required(self.require_lowercase_characters, 'require_lowercase_characters')
        self.validate_required(self.require_uppercase_characters, 'require_uppercase_characters')
        self.validate_required(self.require_numbers, 'require_numbers')
        self.validate_required(self.require_symbols, 'require_symbols')
        self.validate_required(self.hard_expire, 'hard_expire')
        self.validate_required(self.max_login_attemps, 'max_login_attemps')
        self.validate_required(self.password_reuse_prevention, 'password_reuse_prevention')
        self.validate_required(self.max_password_age, 'max_password_age')
        self.validate_required(self.minimum_password_different_character, 'minimum_password_different_character')
        self.validate_required(self.password_not_contain_user_name, 'password_not_contain_user_name')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = map.get('MinimumPasswordLength')
        if map.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = map.get('RequireLowercaseCharacters')
        if map.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = map.get('RequireUppercaseCharacters')
        if map.get('RequireNumbers') is not None:
            self.require_numbers = map.get('RequireNumbers')
        if map.get('RequireSymbols') is not None:
            self.require_symbols = map.get('RequireSymbols')
        if map.get('HardExpire') is not None:
            self.hard_expire = map.get('HardExpire')
        if map.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = map.get('MaxLoginAttemps')
        if map.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = map.get('PasswordReusePrevention')
        if map.get('MaxPasswordAge') is not None:
            self.max_password_age = map.get('MaxPasswordAge')
        if map.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = map.get('MinimumPasswordDifferentCharacter')
        if map.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = map.get('PasswordNotContainUserName')
        return self


class GetLoginProfileRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        return self


class GetLoginProfileResponse(TeaModel):
    def __init__(self, request_id=None, login_profile=None):
        self.request_id = request_id    # type: str
        self.login_profile = login_profile  # type: GetLoginProfileResponseLoginProfile

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.login_profile, 'login_profile')
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('LoginProfile') is not None:
            temp_model = GetLoginProfileResponseLoginProfile()
            self.login_profile = temp_model.from_map(map['LoginProfile'])
        return self


class GetLoginProfileResponseLoginProfile(TeaModel):
    def __init__(self, user_principal_name=None, password_reset_required=None, mfabind_required=None,
                 update_date=None, last_login_time=None, status=None):
        self.user_principal_name = user_principal_name  # type: str
        self.password_reset_required = password_reset_required  # type: bool
        self.mfabind_required = mfabind_required  # type: bool
        self.update_date = update_date  # type: str
        self.last_login_time = last_login_time  # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.password_reset_required, 'password_reset_required')
        self.validate_required(self.mfabind_required, 'mfabind_required')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.last_login_time, 'last_login_time')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('PasswordResetRequired') is not None:
            self.password_reset_required = map.get('PasswordResetRequired')
        if map.get('MFABindRequired') is not None:
            self.mfabind_required = map.get('MFABindRequired')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('LastLoginTime') is not None:
            self.last_login_time = map.get('LastLoginTime')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class GetGroupRequest(TeaModel):
    def __init__(self, group_name=None):
        self.group_name = group_name    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, map={}):
        if map.get('GroupName') is not None:
            self.group_name = map.get('GroupName')
        return self


class GetGroupResponse(TeaModel):
    def __init__(self, request_id=None, group=None):
        self.request_id = request_id    # type: str
        self.group = group              # type: GetGroupResponseGroup

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group, 'group')
        if self.group:
            self.group.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group is not None:
            result['Group'] = self.group.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Group') is not None:
            temp_model = GetGroupResponseGroup()
            self.group = temp_model.from_map(map['Group'])
        return self


class GetGroupResponseGroup(TeaModel):
    def __init__(self, display_name=None, comments=None, create_date=None, update_date=None, group_name=None,
                 group_id=None):
        self.display_name = display_name  # type: str
        self.comments = comments        # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.group_name = group_name    # type: str
        self.group_id = group_id        # type: str

    def validate(self):
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = {}
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, map={}):
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('Comments') is not None:
            self.comments = map.get('Comments')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('GroupName') is not None:
            self.group_name = map.get('GroupName')
        if map.get('GroupId') is not None:
            self.group_id = map.get('GroupId')
        return self


class GetDefaultDomainRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetDefaultDomainResponse(TeaModel):
    def __init__(self, request_id=None, default_domain_name=None):
        self.request_id = request_id    # type: str
        self.default_domain_name = default_domain_name  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.default_domain_name, 'default_domain_name')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('DefaultDomainName') is not None:
            self.default_domain_name = map.get('DefaultDomainName')
        return self


class GetAccountSummaryRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetAccountSummaryResponse(TeaModel):
    def __init__(self, request_id=None, summary_map=None):
        self.request_id = request_id    # type: str
        self.summary_map = summary_map  # type: GetAccountSummaryResponseSummaryMap

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.summary_map, 'summary_map')
        if self.summary_map:
            self.summary_map.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.summary_map is not None:
            result['SummaryMap'] = self.summary_map.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('SummaryMap') is not None:
            temp_model = GetAccountSummaryResponseSummaryMap()
            self.summary_map = temp_model.from_map(map['SummaryMap'])
        return self


class GetAccountSummaryResponseSummaryMap(TeaModel):
    def __init__(self, users_quota=None, users=None, access_keys_per_user_quota=None,
                 virtual_mfadevices_quota=None, mfadevices=None, mfadevices_in_use=None, groups_quota=None, groups=None,
                 groups_per_user_quota=None, roles_quota=None, roles=None, policies_quota=None, policies=None, policy_size_quota=None,
                 versions_per_policy_quota=None, attached_policies_per_user_quota=None, attached_policies_per_group_quota=None,
                 attached_policies_per_role_quota=None, attached_system_policies_per_user_quota=None,
                 attached_system_policies_per_group_quota=None, attached_system_policies_per_role_quota=None):
        self.users_quota = users_quota  # type: int
        self.users = users              # type: int
        self.access_keys_per_user_quota = access_keys_per_user_quota  # type: int
        self.virtual_mfadevices_quota = virtual_mfadevices_quota  # type: int
        self.mfadevices = mfadevices    # type: int
        self.mfadevices_in_use = mfadevices_in_use  # type: int
        self.groups_quota = groups_quota  # type: int
        self.groups = groups            # type: int
        self.groups_per_user_quota = groups_per_user_quota  # type: int
        self.roles_quota = roles_quota  # type: int
        self.roles = roles              # type: int
        self.policies_quota = policies_quota  # type: int
        self.policies = policies        # type: int
        self.policy_size_quota = policy_size_quota  # type: int
        self.versions_per_policy_quota = versions_per_policy_quota  # type: int
        self.attached_policies_per_user_quota = attached_policies_per_user_quota  # type: int
        self.attached_policies_per_group_quota = attached_policies_per_group_quota  # type: int
        self.attached_policies_per_role_quota = attached_policies_per_role_quota  # type: int
        self.attached_system_policies_per_user_quota = attached_system_policies_per_user_quota  # type: int
        self.attached_system_policies_per_group_quota = attached_system_policies_per_group_quota  # type: int
        self.attached_system_policies_per_role_quota = attached_system_policies_per_role_quota  # type: int

    def validate(self):
        self.validate_required(self.users_quota, 'users_quota')
        self.validate_required(self.users, 'users')
        self.validate_required(self.access_keys_per_user_quota, 'access_keys_per_user_quota')
        self.validate_required(self.virtual_mfadevices_quota, 'virtual_mfadevices_quota')
        self.validate_required(self.mfadevices, 'mfadevices')
        self.validate_required(self.mfadevices_in_use, 'mfadevices_in_use')
        self.validate_required(self.groups_quota, 'groups_quota')
        self.validate_required(self.groups, 'groups')
        self.validate_required(self.groups_per_user_quota, 'groups_per_user_quota')
        self.validate_required(self.roles_quota, 'roles_quota')
        self.validate_required(self.roles, 'roles')
        self.validate_required(self.policies_quota, 'policies_quota')
        self.validate_required(self.policies, 'policies')
        self.validate_required(self.policy_size_quota, 'policy_size_quota')
        self.validate_required(self.versions_per_policy_quota, 'versions_per_policy_quota')
        self.validate_required(self.attached_policies_per_user_quota, 'attached_policies_per_user_quota')
        self.validate_required(self.attached_policies_per_group_quota, 'attached_policies_per_group_quota')
        self.validate_required(self.attached_policies_per_role_quota, 'attached_policies_per_role_quota')
        self.validate_required(self.attached_system_policies_per_user_quota, 'attached_system_policies_per_user_quota')
        self.validate_required(self.attached_system_policies_per_group_quota, 'attached_system_policies_per_group_quota')
        self.validate_required(self.attached_system_policies_per_role_quota, 'attached_system_policies_per_role_quota')

    def to_map(self):
        result = {}
        if self.users_quota is not None:
            result['UsersQuota'] = self.users_quota
        if self.users is not None:
            result['Users'] = self.users
        if self.access_keys_per_user_quota is not None:
            result['AccessKeysPerUserQuota'] = self.access_keys_per_user_quota
        if self.virtual_mfadevices_quota is not None:
            result['VirtualMFADevicesQuota'] = self.virtual_mfadevices_quota
        if self.mfadevices is not None:
            result['MFADevices'] = self.mfadevices
        if self.mfadevices_in_use is not None:
            result['MFADevicesInUse'] = self.mfadevices_in_use
        if self.groups_quota is not None:
            result['GroupsQuota'] = self.groups_quota
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.groups_per_user_quota is not None:
            result['GroupsPerUserQuota'] = self.groups_per_user_quota
        if self.roles_quota is not None:
            result['RolesQuota'] = self.roles_quota
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.policies_quota is not None:
            result['PoliciesQuota'] = self.policies_quota
        if self.policies is not None:
            result['Policies'] = self.policies
        if self.policy_size_quota is not None:
            result['PolicySizeQuota'] = self.policy_size_quota
        if self.versions_per_policy_quota is not None:
            result['VersionsPerPolicyQuota'] = self.versions_per_policy_quota
        if self.attached_policies_per_user_quota is not None:
            result['AttachedPoliciesPerUserQuota'] = self.attached_policies_per_user_quota
        if self.attached_policies_per_group_quota is not None:
            result['AttachedPoliciesPerGroupQuota'] = self.attached_policies_per_group_quota
        if self.attached_policies_per_role_quota is not None:
            result['AttachedPoliciesPerRoleQuota'] = self.attached_policies_per_role_quota
        if self.attached_system_policies_per_user_quota is not None:
            result['AttachedSystemPoliciesPerUserQuota'] = self.attached_system_policies_per_user_quota
        if self.attached_system_policies_per_group_quota is not None:
            result['AttachedSystemPoliciesPerGroupQuota'] = self.attached_system_policies_per_group_quota
        if self.attached_system_policies_per_role_quota is not None:
            result['AttachedSystemPoliciesPerRoleQuota'] = self.attached_system_policies_per_role_quota
        return result

    def from_map(self, map={}):
        if map.get('UsersQuota') is not None:
            self.users_quota = map.get('UsersQuota')
        if map.get('Users') is not None:
            self.users = map.get('Users')
        if map.get('AccessKeysPerUserQuota') is not None:
            self.access_keys_per_user_quota = map.get('AccessKeysPerUserQuota')
        if map.get('VirtualMFADevicesQuota') is not None:
            self.virtual_mfadevices_quota = map.get('VirtualMFADevicesQuota')
        if map.get('MFADevices') is not None:
            self.mfadevices = map.get('MFADevices')
        if map.get('MFADevicesInUse') is not None:
            self.mfadevices_in_use = map.get('MFADevicesInUse')
        if map.get('GroupsQuota') is not None:
            self.groups_quota = map.get('GroupsQuota')
        if map.get('Groups') is not None:
            self.groups = map.get('Groups')
        if map.get('GroupsPerUserQuota') is not None:
            self.groups_per_user_quota = map.get('GroupsPerUserQuota')
        if map.get('RolesQuota') is not None:
            self.roles_quota = map.get('RolesQuota')
        if map.get('Roles') is not None:
            self.roles = map.get('Roles')
        if map.get('PoliciesQuota') is not None:
            self.policies_quota = map.get('PoliciesQuota')
        if map.get('Policies') is not None:
            self.policies = map.get('Policies')
        if map.get('PolicySizeQuota') is not None:
            self.policy_size_quota = map.get('PolicySizeQuota')
        if map.get('VersionsPerPolicyQuota') is not None:
            self.versions_per_policy_quota = map.get('VersionsPerPolicyQuota')
        if map.get('AttachedPoliciesPerUserQuota') is not None:
            self.attached_policies_per_user_quota = map.get('AttachedPoliciesPerUserQuota')
        if map.get('AttachedPoliciesPerGroupQuota') is not None:
            self.attached_policies_per_group_quota = map.get('AttachedPoliciesPerGroupQuota')
        if map.get('AttachedPoliciesPerRoleQuota') is not None:
            self.attached_policies_per_role_quota = map.get('AttachedPoliciesPerRoleQuota')
        if map.get('AttachedSystemPoliciesPerUserQuota') is not None:
            self.attached_system_policies_per_user_quota = map.get('AttachedSystemPoliciesPerUserQuota')
        if map.get('AttachedSystemPoliciesPerGroupQuota') is not None:
            self.attached_system_policies_per_group_quota = map.get('AttachedSystemPoliciesPerGroupQuota')
        if map.get('AttachedSystemPoliciesPerRoleQuota') is not None:
            self.attached_system_policies_per_role_quota = map.get('AttachedSystemPoliciesPerRoleQuota')
        return self


class GetAccountSecurityPracticeReportRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetAccountSecurityPracticeReportResponse(TeaModel):
    def __init__(self, request_id=None, account_security_practice_info=None):
        self.request_id = request_id    # type: str
        self.account_security_practice_info = account_security_practice_info  # type: GetAccountSecurityPracticeReportResponseAccountSecurityPracticeInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.account_security_practice_info, 'account_security_practice_info')
        if self.account_security_practice_info:
            self.account_security_practice_info.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account_security_practice_info is not None:
            result['AccountSecurityPracticeInfo'] = self.account_security_practice_info.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('AccountSecurityPracticeInfo') is not None:
            temp_model = GetAccountSecurityPracticeReportResponseAccountSecurityPracticeInfo()
            self.account_security_practice_info = temp_model.from_map(map['AccountSecurityPracticeInfo'])
        return self


class GetAccountSecurityPracticeReportResponseAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo(TeaModel):
    def __init__(self, bind_mfa=None, sub_user_pwd_level=None, root_with_access_key=None, old_ak_num=None,
                 unused_ak_num=None, sub_user=None, sub_user_bind_mfa=None, sub_user_with_old_access_key=None,
                 sub_user_with_unused_access_key=None):
        self.bind_mfa = bind_mfa        # type: bool
        self.sub_user_pwd_level = sub_user_pwd_level  # type: str
        self.root_with_access_key = root_with_access_key  # type: int
        self.old_ak_num = old_ak_num    # type: int
        self.unused_ak_num = unused_ak_num  # type: int
        self.sub_user = sub_user        # type: int
        self.sub_user_bind_mfa = sub_user_bind_mfa  # type: int
        self.sub_user_with_old_access_key = sub_user_with_old_access_key  # type: int
        self.sub_user_with_unused_access_key = sub_user_with_unused_access_key  # type: int

    def validate(self):
        self.validate_required(self.bind_mfa, 'bind_mfa')
        self.validate_required(self.sub_user_pwd_level, 'sub_user_pwd_level')
        self.validate_required(self.root_with_access_key, 'root_with_access_key')
        self.validate_required(self.old_ak_num, 'old_ak_num')
        self.validate_required(self.unused_ak_num, 'unused_ak_num')
        self.validate_required(self.sub_user, 'sub_user')
        self.validate_required(self.sub_user_bind_mfa, 'sub_user_bind_mfa')
        self.validate_required(self.sub_user_with_old_access_key, 'sub_user_with_old_access_key')
        self.validate_required(self.sub_user_with_unused_access_key, 'sub_user_with_unused_access_key')

    def to_map(self):
        result = {}
        if self.bind_mfa is not None:
            result['BindMfa'] = self.bind_mfa
        if self.sub_user_pwd_level is not None:
            result['SubUserPwdLevel'] = self.sub_user_pwd_level
        if self.root_with_access_key is not None:
            result['RootWithAccessKey'] = self.root_with_access_key
        if self.old_ak_num is not None:
            result['OldAkNum'] = self.old_ak_num
        if self.unused_ak_num is not None:
            result['UnusedAkNum'] = self.unused_ak_num
        if self.sub_user is not None:
            result['SubUser'] = self.sub_user
        if self.sub_user_bind_mfa is not None:
            result['SubUserBindMfa'] = self.sub_user_bind_mfa
        if self.sub_user_with_old_access_key is not None:
            result['SubUserWithOldAccessKey'] = self.sub_user_with_old_access_key
        if self.sub_user_with_unused_access_key is not None:
            result['SubUserWithUnusedAccessKey'] = self.sub_user_with_unused_access_key
        return result

    def from_map(self, map={}):
        if map.get('BindMfa') is not None:
            self.bind_mfa = map.get('BindMfa')
        if map.get('SubUserPwdLevel') is not None:
            self.sub_user_pwd_level = map.get('SubUserPwdLevel')
        if map.get('RootWithAccessKey') is not None:
            self.root_with_access_key = map.get('RootWithAccessKey')
        if map.get('OldAkNum') is not None:
            self.old_ak_num = map.get('OldAkNum')
        if map.get('UnusedAkNum') is not None:
            self.unused_ak_num = map.get('UnusedAkNum')
        if map.get('SubUser') is not None:
            self.sub_user = map.get('SubUser')
        if map.get('SubUserBindMfa') is not None:
            self.sub_user_bind_mfa = map.get('SubUserBindMfa')
        if map.get('SubUserWithOldAccessKey') is not None:
            self.sub_user_with_old_access_key = map.get('SubUserWithOldAccessKey')
        if map.get('SubUserWithUnusedAccessKey') is not None:
            self.sub_user_with_unused_access_key = map.get('SubUserWithUnusedAccessKey')
        return self


class GetAccountSecurityPracticeReportResponseAccountSecurityPracticeInfo(TeaModel):
    def __init__(self, score=None, account_security_practice_user_info=None):
        self.score = score              # type: int
        self.account_security_practice_user_info = account_security_practice_user_info  # type: GetAccountSecurityPracticeReportResponseAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo

    def validate(self):
        self.validate_required(self.score, 'score')
        self.validate_required(self.account_security_practice_user_info, 'account_security_practice_user_info')
        if self.account_security_practice_user_info:
            self.account_security_practice_user_info.validate()

    def to_map(self):
        result = {}
        if self.score is not None:
            result['Score'] = self.score
        if self.account_security_practice_user_info is not None:
            result['AccountSecurityPracticeUserInfo'] = self.account_security_practice_user_info.to_map()
        return result

    def from_map(self, map={}):
        if map.get('Score') is not None:
            self.score = map.get('Score')
        if map.get('AccountSecurityPracticeUserInfo') is not None:
            temp_model = GetAccountSecurityPracticeReportResponseAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo()
            self.account_security_practice_user_info = temp_model.from_map(map['AccountSecurityPracticeUserInfo'])
        return self


class GetAccountMFAInfoRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetAccountMFAInfoResponse(TeaModel):
    def __init__(self, request_id=None, is_mfaenable=None):
        self.request_id = request_id    # type: str
        self.is_mfaenable = is_mfaenable  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_mfaenable, 'is_mfaenable')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_mfaenable is not None:
            result['IsMFAEnable'] = self.is_mfaenable
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('IsMFAEnable') is not None:
            self.is_mfaenable = map.get('IsMFAEnable')
        return self


class GetAccessKeyLastUsedRequest(TeaModel):
    def __init__(self, user_principal_name=None, user_access_key_id=None):
        self.user_principal_name = user_principal_name  # type: str
        self.user_access_key_id = user_access_key_id  # type: str

    def validate(self):
        self.validate_required(self.user_access_key_id, 'user_access_key_id')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('UserAccessKeyId') is not None:
            self.user_access_key_id = map.get('UserAccessKeyId')
        return self


class GetAccessKeyLastUsedResponse(TeaModel):
    def __init__(self, request_id=None, access_key_last_used=None):
        self.request_id = request_id    # type: str
        self.access_key_last_used = access_key_last_used  # type: GetAccessKeyLastUsedResponseAccessKeyLastUsed

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.access_key_last_used, 'access_key_last_used')
        if self.access_key_last_used:
            self.access_key_last_used.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_key_last_used is not None:
            result['AccessKeyLastUsed'] = self.access_key_last_used.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('AccessKeyLastUsed') is not None:
            temp_model = GetAccessKeyLastUsedResponseAccessKeyLastUsed()
            self.access_key_last_used = temp_model.from_map(map['AccessKeyLastUsed'])
        return self


class GetAccessKeyLastUsedResponseAccessKeyLastUsed(TeaModel):
    def __init__(self, last_used_date=None):
        self.last_used_date = last_used_date  # type: str

    def validate(self):
        self.validate_required(self.last_used_date, 'last_used_date')

    def to_map(self):
        result = {}
        if self.last_used_date is not None:
            result['LastUsedDate'] = self.last_used_date
        return result

    def from_map(self, map={}):
        if map.get('LastUsedDate') is not None:
            self.last_used_date = map.get('LastUsedDate')
        return self


class DisableVirtualMFARequest(TeaModel):
    def __init__(self, user_principal_name=None):
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        return self


class DisableVirtualMFAResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DeleteVirtualMFADeviceRequest(TeaModel):
    def __init__(self, serial_number=None):
        self.serial_number = serial_number  # type: str

    def validate(self):
        self.validate_required(self.serial_number, 'serial_number')

    def to_map(self):
        result = {}
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, map={}):
        if map.get('SerialNumber') is not None:
            self.serial_number = map.get('SerialNumber')
        return self


class DeleteVirtualMFADeviceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DeleteUserRequest(TeaModel):
    def __init__(self, user_principal_name=None, user_id=None):
        self.user_principal_name = user_principal_name  # type: str
        self.user_id = user_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DeleteSAMLProviderRequest(TeaModel):
    def __init__(self, samlprovider_name=None):
        self.samlprovider_name = samlprovider_name  # type: str

    def validate(self):
        self.validate_required(self.samlprovider_name, 'samlprovider_name')

    def to_map(self):
        result = {}
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        return result

    def from_map(self, map={}):
        if map.get('SAMLProviderName') is not None:
            self.samlprovider_name = map.get('SAMLProviderName')
        return self


class DeleteSAMLProviderResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DeleteLoginProfileRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        return self


class DeleteLoginProfileResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(self, group_name=None):
        self.group_name = group_name    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, map={}):
        if map.get('GroupName') is not None:
            self.group_name = map.get('GroupName')
        return self


class DeleteGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DeleteAccessKeyRequest(TeaModel):
    def __init__(self, user_access_key_id=None, user_principal_name=None):
        self.user_access_key_id = user_access_key_id  # type: str
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        self.validate_required(self.user_access_key_id, 'user_access_key_id')

    def to_map(self):
        result = {}
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, map={}):
        if map.get('UserAccessKeyId') is not None:
            self.user_access_key_id = map.get('UserAccessKeyId')
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        return self


class DeleteAccessKeyResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class CreateVirtualMFADeviceRequest(TeaModel):
    def __init__(self, virtual_mfadevice_name=None):
        self.virtual_mfadevice_name = virtual_mfadevice_name  # type: str

    def validate(self):
        self.validate_required(self.virtual_mfadevice_name, 'virtual_mfadevice_name')

    def to_map(self):
        result = {}
        if self.virtual_mfadevice_name is not None:
            result['VirtualMFADeviceName'] = self.virtual_mfadevice_name
        return result

    def from_map(self, map={}):
        if map.get('VirtualMFADeviceName') is not None:
            self.virtual_mfadevice_name = map.get('VirtualMFADeviceName')
        return self


class CreateVirtualMFADeviceResponse(TeaModel):
    def __init__(self, request_id=None, virtual_mfadevice=None):
        self.request_id = request_id    # type: str
        self.virtual_mfadevice = virtual_mfadevice  # type: CreateVirtualMFADeviceResponseVirtualMFADevice

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.virtual_mfadevice, 'virtual_mfadevice')
        if self.virtual_mfadevice:
            self.virtual_mfadevice.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.virtual_mfadevice is not None:
            result['VirtualMFADevice'] = self.virtual_mfadevice.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('VirtualMFADevice') is not None:
            temp_model = CreateVirtualMFADeviceResponseVirtualMFADevice()
            self.virtual_mfadevice = temp_model.from_map(map['VirtualMFADevice'])
        return self


class CreateVirtualMFADeviceResponseVirtualMFADevice(TeaModel):
    def __init__(self, serial_number=None, base_32string_seed=None, qrcode_png=None):
        self.serial_number = serial_number  # type: str
        self.base_32string_seed = base_32string_seed  # type: str
        self.qrcode_png = qrcode_png    # type: str

    def validate(self):
        self.validate_required(self.serial_number, 'serial_number')
        self.validate_required(self.base_32string_seed, 'base_32string_seed')
        self.validate_required(self.qrcode_png, 'qrcode_png')

    def to_map(self):
        result = {}
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.base_32string_seed is not None:
            result['Base32StringSeed'] = self.base_32string_seed
        if self.qrcode_png is not None:
            result['QRCodePNG'] = self.qrcode_png
        return result

    def from_map(self, map={}):
        if map.get('SerialNumber') is not None:
            self.serial_number = map.get('SerialNumber')
        if map.get('Base32StringSeed') is not None:
            self.base_32string_seed = map.get('Base32StringSeed')
        if map.get('QRCodePNG') is not None:
            self.qrcode_png = map.get('QRCodePNG')
        return self


class CreateUserRequest(TeaModel):
    def __init__(self, user_principal_name=None, display_name=None, mobile_phone=None, email=None, comments=None):
        self.user_principal_name = user_principal_name  # type: str
        self.display_name = display_name  # type: str
        self.mobile_phone = mobile_phone  # type: str
        self.email = email              # type: str
        self.comments = comments        # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.display_name, 'display_name')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('MobilePhone') is not None:
            self.mobile_phone = map.get('MobilePhone')
        if map.get('Email') is not None:
            self.email = map.get('Email')
        if map.get('Comments') is not None:
            self.comments = map.get('Comments')
        return self


class CreateUserResponse(TeaModel):
    def __init__(self, request_id=None, user=None):
        self.request_id = request_id    # type: str
        self.user = user                # type: CreateUserResponseUser

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.user, 'user')
        if self.user:
            self.user.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('User') is not None:
            temp_model = CreateUserResponseUser()
            self.user = temp_model.from_map(map['User'])
        return self


class CreateUserResponseUser(TeaModel):
    def __init__(self, user_id=None, user_principal_name=None, display_name=None, comments=None, create_date=None,
                 update_date=None, last_login_date=None, mobile_phone=None, email=None):
        self.user_id = user_id          # type: str
        self.user_principal_name = user_principal_name  # type: str
        self.display_name = display_name  # type: str
        self.comments = comments        # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.last_login_date = last_login_date  # type: str
        self.mobile_phone = mobile_phone  # type: str
        self.email = email              # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.last_login_date, 'last_login_date')
        self.validate_required(self.mobile_phone, 'mobile_phone')
        self.validate_required(self.email, 'email')

    def to_map(self):
        result = {}
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, map={}):
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('Comments') is not None:
            self.comments = map.get('Comments')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('LastLoginDate') is not None:
            self.last_login_date = map.get('LastLoginDate')
        if map.get('MobilePhone') is not None:
            self.mobile_phone = map.get('MobilePhone')
        if map.get('Email') is not None:
            self.email = map.get('Email')
        return self


class CreateSAMLProviderRequest(TeaModel):
    def __init__(self, samlprovider_name=None, description=None, encoded_samlmetadata_document=None):
        self.samlprovider_name = samlprovider_name  # type: str
        self.description = description  # type: str
        self.encoded_samlmetadata_document = encoded_samlmetadata_document  # type: str

    def validate(self):
        self.validate_required(self.samlprovider_name, 'samlprovider_name')

    def to_map(self):
        result = {}
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.description is not None:
            result['Description'] = self.description
        if self.encoded_samlmetadata_document is not None:
            result['EncodedSAMLMetadataDocument'] = self.encoded_samlmetadata_document
        return result

    def from_map(self, map={}):
        if map.get('SAMLProviderName') is not None:
            self.samlprovider_name = map.get('SAMLProviderName')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('EncodedSAMLMetadataDocument') is not None:
            self.encoded_samlmetadata_document = map.get('EncodedSAMLMetadataDocument')
        return self


class CreateSAMLProviderResponse(TeaModel):
    def __init__(self, request_id=None, samlprovider=None):
        self.request_id = request_id    # type: str
        self.samlprovider = samlprovider  # type: CreateSAMLProviderResponseSAMLProvider

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.samlprovider, 'samlprovider')
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('SAMLProvider') is not None:
            temp_model = CreateSAMLProviderResponseSAMLProvider()
            self.samlprovider = temp_model.from_map(map['SAMLProvider'])
        return self


class CreateSAMLProviderResponseSAMLProvider(TeaModel):
    def __init__(self, samlprovider_name=None, arn=None, description=None, create_date=None, update_date=None):
        self.samlprovider_name = samlprovider_name  # type: str
        self.arn = arn                  # type: str
        self.description = description  # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        self.validate_required(self.samlprovider_name, 'samlprovider_name')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.description, 'description')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')

    def to_map(self):
        result = {}
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.description is not None:
            result['Description'] = self.description
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, map={}):
        if map.get('SAMLProviderName') is not None:
            self.samlprovider_name = map.get('SAMLProviderName')
        if map.get('Arn') is not None:
            self.arn = map.get('Arn')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        return self


class CreateLoginProfileRequest(TeaModel):
    def __init__(self, user_principal_name=None, password=None, password_reset_required=None,
                 mfabind_required=None, status=None):
        self.user_principal_name = user_principal_name  # type: str
        self.password = password        # type: str
        self.password_reset_required = password_reset_required  # type: bool
        self.mfabind_required = mfabind_required  # type: bool
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('Password') is not None:
            self.password = map.get('Password')
        if map.get('PasswordResetRequired') is not None:
            self.password_reset_required = map.get('PasswordResetRequired')
        if map.get('MFABindRequired') is not None:
            self.mfabind_required = map.get('MFABindRequired')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class CreateLoginProfileResponse(TeaModel):
    def __init__(self, request_id=None, login_profile=None):
        self.request_id = request_id    # type: str
        self.login_profile = login_profile  # type: CreateLoginProfileResponseLoginProfile

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.login_profile, 'login_profile')
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('LoginProfile') is not None:
            temp_model = CreateLoginProfileResponseLoginProfile()
            self.login_profile = temp_model.from_map(map['LoginProfile'])
        return self


class CreateLoginProfileResponseLoginProfile(TeaModel):
    def __init__(self, user_principal_name=None, password_reset_required=None, mfabind_required=None,
                 update_date=None, status=None):
        self.user_principal_name = user_principal_name  # type: str
        self.password_reset_required = password_reset_required  # type: bool
        self.mfabind_required = mfabind_required  # type: bool
        self.update_date = update_date  # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.password_reset_required, 'password_reset_required')
        self.validate_required(self.mfabind_required, 'mfabind_required')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('PasswordResetRequired') is not None:
            self.password_reset_required = map.get('PasswordResetRequired')
        if map.get('MFABindRequired') is not None:
            self.mfabind_required = map.get('MFABindRequired')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class CreateGroupRequest(TeaModel):
    def __init__(self, display_name=None, comments=None, group_name=None):
        self.display_name = display_name  # type: str
        self.comments = comments        # type: str
        self.group_name = group_name    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, map={}):
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('Comments') is not None:
            self.comments = map.get('Comments')
        if map.get('GroupName') is not None:
            self.group_name = map.get('GroupName')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(self, request_id=None, group=None):
        self.request_id = request_id    # type: str
        self.group = group              # type: CreateGroupResponseGroup

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group, 'group')
        if self.group:
            self.group.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group is not None:
            result['Group'] = self.group.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Group') is not None:
            temp_model = CreateGroupResponseGroup()
            self.group = temp_model.from_map(map['Group'])
        return self


class CreateGroupResponseGroup(TeaModel):
    def __init__(self, display_name=None, comments=None, create_date=None, update_date=None, group_name=None,
                 group_id=None):
        self.display_name = display_name  # type: str
        self.comments = comments        # type: str
        self.create_date = create_date  # type: str
        self.update_date = update_date  # type: str
        self.group_name = group_name    # type: str
        self.group_id = group_id        # type: str

    def validate(self):
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = {}
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, map={}):
        if map.get('DisplayName') is not None:
            self.display_name = map.get('DisplayName')
        if map.get('Comments') is not None:
            self.comments = map.get('Comments')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('UpdateDate') is not None:
            self.update_date = map.get('UpdateDate')
        if map.get('GroupName') is not None:
            self.group_name = map.get('GroupName')
        if map.get('GroupId') is not None:
            self.group_id = map.get('GroupId')
        return self


class CreateAccessKeyRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        return self


class CreateAccessKeyResponse(TeaModel):
    def __init__(self, request_id=None, access_key=None):
        self.request_id = request_id    # type: str
        self.access_key = access_key    # type: CreateAccessKeyResponseAccessKey

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.access_key, 'access_key')
        if self.access_key:
            self.access_key.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('AccessKey') is not None:
            temp_model = CreateAccessKeyResponseAccessKey()
            self.access_key = temp_model.from_map(map['AccessKey'])
        return self


class CreateAccessKeyResponseAccessKey(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, create_date=None, status=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.create_date = create_date  # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.access_key_id, 'access_key_id')
        self.validate_required(self.access_key_secret, 'access_key_secret')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('AccessKeyId') is not None:
            self.access_key_id = map.get('AccessKeyId')
        if map.get('AccessKeySecret') is not None:
            self.access_key_secret = map.get('AccessKeySecret')
        if map.get('CreateDate') is not None:
            self.create_date = map.get('CreateDate')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class ChangePasswordRequest(TeaModel):
    def __init__(self, old_password=None, new_password=None):
        self.old_password = old_password  # type: str
        self.new_password = new_password  # type: str

    def validate(self):
        self.validate_required(self.old_password, 'old_password')
        self.validate_required(self.new_password, 'new_password')

    def to_map(self):
        result = {}
        if self.old_password is not None:
            result['OldPassword'] = self.old_password
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        return result

    def from_map(self, map={}):
        if map.get('OldPassword') is not None:
            self.old_password = map.get('OldPassword')
        if map.get('NewPassword') is not None:
            self.new_password = map.get('NewPassword')
        return self


class ChangePasswordResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class BindMFADeviceRequest(TeaModel):
    def __init__(self, serial_number=None, user_principal_name=None, authentication_code_1=None,
                 authentication_code_2=None):
        self.serial_number = serial_number  # type: str
        self.user_principal_name = user_principal_name  # type: str
        self.authentication_code_1 = authentication_code_1  # type: str
        self.authentication_code_2 = authentication_code_2  # type: str

    def validate(self):
        self.validate_required(self.serial_number, 'serial_number')
        self.validate_required(self.user_principal_name, 'user_principal_name')
        self.validate_required(self.authentication_code_1, 'authentication_code_1')
        self.validate_required(self.authentication_code_2, 'authentication_code_2')

    def to_map(self):
        result = {}
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.authentication_code_1 is not None:
            result['AuthenticationCode1'] = self.authentication_code_1
        if self.authentication_code_2 is not None:
            result['AuthenticationCode2'] = self.authentication_code_2
        return result

    def from_map(self, map={}):
        if map.get('SerialNumber') is not None:
            self.serial_number = map.get('SerialNumber')
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('AuthenticationCode1') is not None:
            self.authentication_code_1 = map.get('AuthenticationCode1')
        if map.get('AuthenticationCode2') is not None:
            self.authentication_code_2 = map.get('AuthenticationCode2')
        return self


class BindMFADeviceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class AddUserToGroupRequest(TeaModel):
    def __init__(self, user_principal_name=None, group_name=None):
        self.user_principal_name = user_principal_name  # type: str
        self.group_name = group_name    # type: str

    def validate(self):
        self.validate_required(self.user_principal_name, 'user_principal_name')

    def to_map(self):
        result = {}
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, map={}):
        if map.get('UserPrincipalName') is not None:
            self.user_principal_name = map.get('UserPrincipalName')
        if map.get('GroupName') is not None:
            self.group_name = map.get('GroupName')
        return self


class AddUserToGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self
