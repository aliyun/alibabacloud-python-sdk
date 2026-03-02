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
        display_name: str = None,
        is_multi_tenant: bool = None,
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
        # The name can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.app_name = app_name
        # The type of the application. Valid values:
        # 
        # - WebApp: a web application that is based on browser interaction.
        # 
        # - NativeApp: a native application that runs on an operating system, such as a desktop or mobile operating system.
        # 
        # - ServerApp: an application that directly accesses Alibaba Cloud services without user logon. Currently, only applications that use the System for Cross-domain Identity Management (SCIM) protocol for user synchronization are supported.
        # 
        # This parameter is required.
        self.app_type = app_type
        # The display name of the application.
        # 
        # The name can be up to 24 characters in length.
        # 
        # This parameter is required.
        self.display_name = display_name
        # Specifies whether the application can be installed by other Alibaba Cloud accounts. Valid values:
        # 
        # - true: For NativeApp and ServerApp applications, the default value is \\`true\\` if you leave this parameter empty.
        # 
        # - false: For WebApp applications, the default value is \\`false\\` if you leave this parameter empty.
        self.is_multi_tenant = is_multi_tenant
        # The scopes of the application.
        # 
        # For information about the valid values and descriptions of scopes, see [OAuth scopes](https://help.aliyun.com/document_detail/93693.html). You can also call the [ListPredefinedScopes](https://help.aliyun.com/document_detail/187206.html) operation to obtain the scopes that are supported by different application types.
        # 
        # To enter multiple scopes, separate them with semicolons (;).
        self.predefined_scopes = predefined_scopes
        # The OAuth protocol version of the application. Valid values:
        # 
        # - `2.0`: OAuth 2.0.
        # 
        # - `2.1`: OAuth 2.1.
        # 
        # Default value: `2.0`.
        self.protocol_version = protocol_version
        # The webhook address.
        # 
        # To enter multiple webhook addresses, separate them with semicolons (;).
        self.redirect_uris = redirect_uris
        # The validity period of the refresh token.
        # 
        # Valid values: 7200 to 31536000. Unit: seconds.
        # 
        # Default value:
        # 
        # - For NativeApp and ServerApp applications, the default value is 2,592,000 seconds (30 days) if you leave this parameter empty.
        # 
        # - For WebApp applications, the default value is 7,776,000 seconds (90 days) if you leave this parameter empty.
        self.refresh_token_validity = refresh_token_validity
        # The required scopes.
        # 
        # You can specify one or more scopes in `RequiredScopes` as required. When a user grants permissions to the application, the required scopes are selected by default and cannot be deselected.
        # 
        # To enter multiple scopes, separate them with semicolons (;).
        # 
        # > If a scope that you specify in `RequiredScopes` is not within the range of `PredefinedScopes`, the required setting for that scope does not take effect.
        self.required_scopes = required_scopes
        # Specifies whether an application key is required. Valid values:
        # 
        # - true
        # 
        # - false
        # 
        # > * For WebApp and ServerApp applications, this parameter is forcibly set to \\`true\\` and cannot be changed.
        # 
        # - For NativeApp applications, you can set this parameter to \\`true\\` or \\`false\\`. If you do not set this parameter, the default value is \\`false\\`. Because these applications often run in untrusted environments where application keys cannot be effectively protected, do not set this parameter to \\`true\\` unless necessary. For more information, see [Log on to Alibaba Cloud from a native application](https://help.aliyun.com/document_detail/93697.html).
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

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant

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

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')

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

