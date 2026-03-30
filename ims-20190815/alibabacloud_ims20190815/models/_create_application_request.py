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
        # The name can be up to 64 characters in length. The name can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.app_name = app_name
        # The type of the application. Valid values:
        # 
        # *   WebApp: a web application that interacts with a browser.
        # *   NativeApp: a native application that runs on an operating system, such as a desktop operating system or a mobile operating system.
        # *   ServerApp: an application that accesses Alibaba Cloud services without the need of manual user logon. User provisioning is automated based on the System for Cross-Domain Identity Management (SCIM) protocol.
        # 
        # This parameter is required.
        self.app_type = app_type
        # The display name of the application.
        # 
        # The name can be up to 24 characters in length.
        # 
        # This parameter is required.
        self.display_name = display_name
        # Indicates whether the application can be installed by using other Alibaba Cloud accounts. Valid values:
        # 
        # *   true: If you do not set this parameter for applications of the NativeApp and ServerApp types, true is used.
        # *   false: If you do not set this parameter for applications of the WebApp type, false is used.
        self.is_multi_tenant = is_multi_tenant
        # The scope of application permissions.
        # 
        # For more information about the application permission scope, see [Open authorization scope](https://help.aliyun.com/document_detail/93693.html). You can also call the [ListPredefinedScopes](https://help.aliyun.com/document_detail/187206.html) operation to query the permissions that are supported by different types of applications.
        # 
        # If you enter multiple permission scopes, separate them with semicolons (;).
        self.predefined_scopes = predefined_scopes
        self.protocol_version = protocol_version
        # The callback URL.
        # 
        # If you enter multiple callback URLs, separate them with semicolons (;).
        self.redirect_uris = redirect_uris
        # The validity period of the refreshed token.
        # 
        # Valid values: 7200 to 31536000. Unit: seconds.
        # 
        # Default value:
        # 
        # *   For applications of the WebApp and ServerApp types, if this parameter is left empty, the value 2592000 is used. The value 2592000 indicates that the validity period of the refreshed token is 30 days.
        # *   For applications of the NativeApp type, if this parameter is left empty, the value 7776000 is used. The value 7776000 indicates that the validity period of the refreshed token is 90 days.
        self.refresh_token_validity = refresh_token_validity
        # The required permission.
        # 
        # You can specify one or more permissions for the `RequiredScopes` parameter. After you specify this parameter, the required permissions are automatically selected and cannot be revoked when a user grants permissions on the application.
        # 
        # If you enter multiple permission scopes, separate them with semicolons (;).
        # 
        # >  If the permission that you specify for the `RequiredScopes` parameter is not included in the value of the `PredefinedScopes` parameter, the permission does not take effect.
        self.required_scopes = required_scopes
        # Indicates whether a secret is required. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >- For applications of the WebApp and ServerApp types, this parameter is automatically set to true and cannot be changed.
        # >- For applications of the NativeApp type, this parameter can be set to true or false. If you do not set this parameter, false is used. Applications of the NativeApp type run in untrusted environments and the secrets of these applications are not protected. Therefore, we recommend that you do not set this parameter to true unless otherwise specified. For more information, see [Use an application of the NativeApp type to log on to Alibaba Cloud](https://help.aliyun.com/document_detail/93697.html).
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

