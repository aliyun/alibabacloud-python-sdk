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
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The validity period of the access token.
        # 
        # Valid values: 900 to 10800. Unit: seconds.
        self.new_access_token_validity = new_access_token_validity
        # The new display name.
        self.new_display_name = new_display_name
        # Indicates whether the application can be installed by other Alibaba Cloud accounts. Valid values:
        # 
        # - true: The application can be installed.
        # 
        # - false: The application cannot be installed.
        self.new_is_multi_tenant = new_is_multi_tenant
        # The permission scopes of the application.
        # 
        # For more information about the valid values and descriptions of permission scopes, see [OAuth scopes](https://help.aliyun.com/document_detail/93693.html). You can also call the [ListPredefinedScopes](https://help.aliyun.com/document_detail/187206.html) operation to obtain the permission scopes that are supported by different types of applications.
        # 
        # If you enter multiple permission scopes, separate them with semicolons (;).
        # 
        # The new permission scopes overwrite the original ones. For example, if the original permission scope is `/acs/ccc` and you set the new permission scope to `/acs/alidns`, the permission scope that takes effect is `/acs/alidns`. If you want to add `/acs/alidns` to the original scope, set the new permission scope to `/acs/ccc;/acs/alidns`.
        self.new_predefined_scopes = new_predefined_scopes
        # The webhook address.
        # 
        # If you enter multiple webhook addresses, separate them with semicolons (;).
        self.new_redirect_uris = new_redirect_uris
        # The validity period of the refresh token.
        # 
        # Valid values: 7200 to 31536000. Unit: seconds.
        self.new_refresh_token_validity = new_refresh_token_validity
        # The required permission scopes of the application.
        # 
        # You can set one or more scopes specified in `RequiredScopes` as required. After a scope is set as required, it is selected by default and cannot be deselected when a user grants permissions to the application.
        # 
        # If you also specify `NewPredefinedScopes`, the list of application scopes is reset by `NewPredefinedScopes` first. Then, this parameter is used to configure whether the scopes are required.
        # 
        # If you enter multiple permission scopes, separate them with semicolons (;).
        # 
        # The new required scopes overwrite the original ones.
        # 
        # > If a scope that you specify for `RequiredScopes` is not within the range of `PredefinedScopes`, the required setting for that scope does not take effect.
        self.new_required_scopes = new_required_scopes
        # Indicates whether an application key is required. Valid values:
        # 
        # - true
        # 
        # - false
        # 
        # > * For applications of the WebApp and ServerApp types, this parameter is forcibly set to true and cannot be modified.
        # 
        # - For applications of the NativeApp type, you can set this parameter to true or false. The default value is false. These applications often run in untrusted environments and cannot effectively protect application keys. Do not set this parameter to true unless necessary. For more information, see [Log on to Alibaba Cloud using a native application](https://help.aliyun.com/document_detail/93697.html).
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

