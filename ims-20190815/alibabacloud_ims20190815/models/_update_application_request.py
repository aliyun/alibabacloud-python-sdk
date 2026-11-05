# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        new_access_token_validity: int = None,
        new_assignment_type: str = None,
        new_display_name: str = None,
        new_is_multi_tenant: bool = None,
        new_need_principal_consent: bool = None,
        new_predefined_scopes: str = None,
        new_redirect_uris: str = None,
        new_refresh_token_validity: int = None,
        new_required_scopes: str = None,
        new_secret_required: bool = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The validity period of the access token.
        # 
        # Valid values: 900 to 10800. Unit: seconds.
        self.new_access_token_validity = new_access_token_validity
        # The application assignment type. Valid values:
        # 
        # + AllowAll: Full assignment. All RAM users and roles under the account are allowed to use the application.
        # + OnDemand: On-demand assignment. Only specified RAM users and roles under the account are allowed to use the application.
        self.new_assignment_type = new_assignment_type
        # The display name.
        self.new_display_name = new_display_name
        # Specifies whether the application can be installed by other accounts. Valid values:
        # 
        # - true: Allowed.
        # 
        # - false: Not allowed.
        self.new_is_multi_tenant = new_is_multi_tenant
        # Specifies whether user authorization is required. Valid values:
        # 
        # + true: In addition to the authorization required during application installation, the user must also authorize the application **each time** they use it for OAuth logon.
        # + false: Authorization is required only during application installation. No additional authorization is required when the user uses the application for OAuth logon later.
        self.new_need_principal_consent = new_need_principal_consent
        # The application permission scopes.
        # 
        # For the valid values and descriptions of application permission scopes, see [OAuth scopes](https://help.aliyun.com/document_detail/93693.html). You can also call the [ListPredefinedScopes](https://help.aliyun.com/document_detail/187206.html) operation to obtain the application permission scopes supported by different application types.
        # 
        # Separate multiple scopes with semicolons (;).
        # 
        # The new scopes overwrite the original scopes. For example, if the original scope is /acs/ccc and the new scope is /acs/alidns, the effective scope is /acs/alidns. To add /acs/alidns to the original scopes, set the new scopes to /acs/ccc;/acs/alidns.
        self.new_predefined_scopes = new_predefined_scopes
        # The callback URLs. Separate multiple URLs with semicolons (;).
        self.new_redirect_uris = new_redirect_uris
        # The validity period of the refresh token.
        # 
        # Valid values: 7200 to 31536000. Unit: seconds.
        self.new_refresh_token_validity = new_refresh_token_validity
        # The required application permission scopes.
        # 
        # You can set one or more scopes in RequiredScopes as required. After a scope is set as required, it is selected by default and cannot be deselected when a user authorizes the application.
        # 
        # If you also specify NewPredefinedScopes, the scope list of the application is reset by using NewPredefinedScopes first, and then this parameter is used to specify whether the scopes are required.
        # 
        # Separate multiple scopes with semicolons (;).
        # 
        # The new required scopes overwrite the original required scopes.
        # 
        # > If a scope specified in RequiredScopes is not included in PredefinedScopes, the required setting for this scope does not take effect.
        self.new_required_scopes = new_required_scopes
        # Specifies whether an application secret is required. Valid values:
        # 
        # - true
        # - false
        # 
        # > - + For WebApp and ServerApp applications, this value is forcibly set to true and cannot be modified.
        # > - + For NativeApp applications, you can set this value to true or false. If you do not specify this parameter, the default value is false. Because such applications usually run in untrusted environments and cannot effectively protect application secrets, do not set this value to true unless necessary. For more information, see [Log on to Alibaba Cloud from a native application](https://help.aliyun.com/document_detail/93697.html).
        self.new_secret_required = new_secret_required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.new_access_token_validity is not None:
            result['NewAccessTokenValidity'] = self.new_access_token_validity

        if self.new_assignment_type is not None:
            result['NewAssignmentType'] = self.new_assignment_type

        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name

        if self.new_is_multi_tenant is not None:
            result['NewIsMultiTenant'] = self.new_is_multi_tenant

        if self.new_need_principal_consent is not None:
            result['NewNeedPrincipalConsent'] = self.new_need_principal_consent

        if self.new_predefined_scopes is not None:
            result['NewPredefinedScopes'] = self.new_predefined_scopes

        if self.new_redirect_uris is not None:
            result['NewRedirectUris'] = self.new_redirect_uris

        if self.new_refresh_token_validity is not None:
            result['NewRefreshTokenValidity'] = self.new_refresh_token_validity

        if self.new_required_scopes is not None:
            result['NewRequiredScopes'] = self.new_required_scopes

        if self.new_secret_required is not None:
            result['NewSecretRequired'] = self.new_secret_required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('NewAccessTokenValidity') is not None:
            self.new_access_token_validity = m.get('NewAccessTokenValidity')

        if m.get('NewAssignmentType') is not None:
            self.new_assignment_type = m.get('NewAssignmentType')

        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')

        if m.get('NewIsMultiTenant') is not None:
            self.new_is_multi_tenant = m.get('NewIsMultiTenant')

        if m.get('NewNeedPrincipalConsent') is not None:
            self.new_need_principal_consent = m.get('NewNeedPrincipalConsent')

        if m.get('NewPredefinedScopes') is not None:
            self.new_predefined_scopes = m.get('NewPredefinedScopes')

        if m.get('NewRedirectUris') is not None:
            self.new_redirect_uris = m.get('NewRedirectUris')

        if m.get('NewRefreshTokenValidity') is not None:
            self.new_refresh_token_validity = m.get('NewRefreshTokenValidity')

        if m.get('NewRequiredScopes') is not None:
            self.new_required_scopes = m.get('NewRequiredScopes')

        if m.get('NewSecretRequired') is not None:
            self.new_secret_required = m.get('NewSecretRequired')

        return self

