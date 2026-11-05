# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationRequest(DaraModel):
    def __init__(
        self,
        access_token_validity: int = None,
        app_name: str = None,
        app_type: str = None,
        assignment_type: str = None,
        display_name: str = None,
        is_multi_tenant: bool = None,
        need_principal_consent: bool = None,
        predefined_scopes: str = None,
        protocol_version: str = None,
        redirect_uris: str = None,
        refresh_token_validity: int = None,
        required_scopes: str = None,
        secret_required: bool = None,
    ):
        # The validity period of the access token.
        # 
        # Valid values: 900 to 10800. Unit: seconds.
        # 
        # Default value: 3600.
        self.access_token_validity = access_token_validity
        # The application name.
        # 
        # The maximum length is 64 characters. Only letters, digits, periods (.), underscores (_), and hyphens (-) are allowed.
        self.app_name = app_name
        # The application type. Valid values:
        # 
        # - WebApp: web applications that interact with users through browsers. 
        # - NativeApp: native applications that run in operating systems, primarily on desktop or shift operating systems. 
        # - ServerApp: applications that directly access Alibaba Cloud services without requiring user logons. Currently, only user synchronization applications based on the System for Cross-domain Identity Management protocol are supported.
        # 
        # This parameter is required.
        self.app_type = app_type
        # The application assignment type. Valid values:
        # 
        # + AllowAll: assigns the application to all RAM users and roles in the account, allowing them to use the application.
        # + OnDemand: assigns the application only to specified RAM users and roles in the account, allowing only them to use the application.
        self.assignment_type = assignment_type
        # The display name of the application.
        # 
        # Maximum length: 24 characters.
        # 
        # This parameter is required.
        self.display_name = display_name
        # Specifies whether the application can be installed by other accounts. Valid values:
        # 
        # - true: For NativeApp and ServerApp applications, if this value is empty, the default value is true.
        # - false: For WebApp applications, if this value is empty, the default value is false.
        self.is_multi_tenant = is_multi_tenant
        # Specifies whether user authorization is required. Valid values:
        # 
        # + true: In addition to the authorization required during application installation, users must also authorize the application **each time** they use it for OAuth logon.
        # + false: Authorization is required only during application installation. Users do not need additional authorization when they use the application for OAuth logon later.
        self.need_principal_consent = need_principal_consent
        # The scopes of the application.
        # 
        # For the valid values and descriptions of application scopes, see [OAuth scopes](https://help.aliyun.com/document_detail/93693.html). You can also call the [ListPredefinedScopes](https://help.aliyun.com/document_detail/187206.html) operation to obtain the scopes supported by different application types.
        # 
        # Separate multiple scopes with semicolons (;).
        self.predefined_scopes = predefined_scopes
        # The OAuth protocol version of the application. Valid values:
        # + 2.0: OAuth 2.0 protocol.
        # + 2.1: OAuth 2.1 protocol.
        # 
        # Default value: 2.0.
        self.protocol_version = protocol_version
        # The redirect URIs.
        # 
        # Separate multiple URIs with semicolons (;).
        self.redirect_uris = redirect_uris
        # The validity period of the refresh token.
        # 
        # Valid values: 7200 to 31536000. Unit: seconds.
        # 
        # Default value:
        # 
        # - For NativeApp and ServerApp applications, if this value is empty, the default value is 2592000 seconds (30 days).
        # - For WebApp applications, if this value is empty, the default value is 7776000 seconds (90 days).
        self.refresh_token_validity = refresh_token_validity
        # The required scopes of the application.
        # 
        # You can set one or more scopes in RequiredScopes as required. After a scope is set as required, it is selected by default and cannot be deselected when a user authorizes the application.
        # 
        # Separate multiple scopes with semicolons (;).
        # 
        # > If a scope that you specify in RequiredScopes is not included in PredefinedScopes, the required scope does not take effect.
        self.required_scopes = required_scopes
        # Specifies whether an application secret is required. Valid values:
        # 
        # - true
        # - false
        # 
        # > - + For WebApp and ServerApp applications, this value is forcibly set to true and cannot be modified.
        # > - + For NativeApp applications, you can set this value to true or false. If you do not specify this value, the default value is false. Because such applications often run in untrusted environments and cannot effectively protect application secrets, do not set this value to true unless necessary. For more information, see [Log on to Alibaba Cloud from a native application](https://help.aliyun.com/document_detail/93697.html).
        self.secret_required = secret_required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.assignment_type is not None:
            result['AssignmentType'] = self.assignment_type

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant

        if self.need_principal_consent is not None:
            result['NeedPrincipalConsent'] = self.need_principal_consent

        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes

        if self.protocol_version is not None:
            result['ProtocolVersion'] = self.protocol_version

        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris

        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity

        if self.required_scopes is not None:
            result['RequiredScopes'] = self.required_scopes

        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('AssignmentType') is not None:
            self.assignment_type = m.get('AssignmentType')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')

        if m.get('NeedPrincipalConsent') is not None:
            self.need_principal_consent = m.get('NeedPrincipalConsent')

        if m.get('PredefinedScopes') is not None:
            self.predefined_scopes = m.get('PredefinedScopes')

        if m.get('ProtocolVersion') is not None:
            self.protocol_version = m.get('ProtocolVersion')

        if m.get('RedirectUris') is not None:
            self.redirect_uris = m.get('RedirectUris')

        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')

        if m.get('RequiredScopes') is not None:
            self.required_scopes = m.get('RequiredScopes')

        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')

        return self

