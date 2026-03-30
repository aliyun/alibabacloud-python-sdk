# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        new_access_token_validity: int = None,
        new_display_name: str = None,
        new_is_multi_tenant: bool = None,
        new_predefined_scopes: str = None,
        new_redirect_uris: str = None,
        new_refresh_token_validity: int = None,
        new_required_scopes: str = None,
        new_secret_required: bool = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The validity period of the access token.
        # 
        # Valid values: 900 to 10800. Unit: seconds.
        self.new_access_token_validity = new_access_token_validity
        # The display name.
        self.new_display_name = new_display_name
        # Specifies whether the application can be installed by using other Alibaba Cloud accounts. Valid values:
        # 
        # *   true
        # *   false
        self.new_is_multi_tenant = new_is_multi_tenant
        # The permission that is granted on the application.
        # 
        # For more information about the application permission scope, see [OAuth scopes](https://help.aliyun.com/document_detail/93693.html). You can also call the [ListPredefinedScopes](https://help.aliyun.com/document_detail/187206.html) operation to query the permissions that are supported by different types of applications.
        # 
        # If you enter multiple permissions, separate them with semicolons (;).
        # 
        # The new value of this parameter overwrites the original value, and the permission specified by the new value takes effect. For example, if the original value is `/acs/ccc`, and the new value is `/acs/alidns`, `/acs/alidns` takes effect. If you want to retain the original permission and the `/acs/alidns` permission, set the value to `/acs/ccc;/acs/alidns`.
        self.new_predefined_scopes = new_predefined_scopes
        # The callback URL.
        # 
        # If you enter multiple callback URLs, separate them with semicolons (;).
        self.new_redirect_uris = new_redirect_uris
        # The validity period of the refresh token.
        # 
        # Valid values: 7200 to 31536000. Unit: seconds.
        self.new_refresh_token_validity = new_refresh_token_validity
        # The required permission.
        # 
        # You can specify one or more permissions for the `RequiredScopes` parameter. After you specify this parameter, the required permissions are automatically selected and cannot be revoked when a user grants permissions on the application.
        # 
        # If you also specify the `NewPredefinedScopes` parameter, the `NewPredefinedScopes` parameter specifies the permissions that can be granted on the application, and this parameter specifies the required permissions.
        # 
        # If you enter multiple permissions, separate them with semicolons (;).
        # 
        # The new value of this parameter overwrites the original value, and the required permission specified by the new value takes effect.
        # 
        # >  If the permission that you specify for the `RequiredScopes` parameter is not included in value of the `PredefinedScopes` parameter, the permission does not take effect.
        self.new_required_scopes = new_required_scopes
        # Specifies whether a secret is required. Valid values:
        # 
        # *   true
        # *   false
        # 
        # > 
        # 
        # *   For applications of the WebApp and ServerApp types, this parameter is automatically set to true and cannot be changed.
        # *   For applications of the NativeApp type, this parameter can be set to true or false. If you do not set this parameter, false is used. Applications of the NativeApp type run in untrusted environments and the secrets of these applications are not protected. Therefore, we recommend that you do not set this parameter to true unless otherwise specified. For more information, see [Use an application of the NativeApp type to log on to Alibaba Cloud](https://help.aliyun.com/document_detail/93697.html).
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

        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name

        if self.new_is_multi_tenant is not None:
            result['NewIsMultiTenant'] = self.new_is_multi_tenant

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

        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')

        if m.get('NewIsMultiTenant') is not None:
            self.new_is_multi_tenant = m.get('NewIsMultiTenant')

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

