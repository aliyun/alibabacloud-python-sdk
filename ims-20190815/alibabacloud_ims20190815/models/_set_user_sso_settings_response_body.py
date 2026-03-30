# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class SetUserSsoSettingsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_sso_settings: main_models.SetUserSsoSettingsResponseBodyUserSsoSettings = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The configurations of user-based SSO.
        self.user_sso_settings = user_sso_settings

    def validate(self):
        if self.user_sso_settings:
            self.user_sso_settings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.SetUserSsoSettingsResponseBodyUserSsoSettings()
            self.user_sso_settings = temp_model.from_map(m.get('UserSsoSettings'))

        return self

class SetUserSsoSettingsResponseBodyUserSsoSettings(DaraModel):
    def __init__(
        self,
        authn_sign_algo: str = None,
        auxiliary_domain: str = None,
        metadata_document: str = None,
        sso_enabled: bool = None,
        sso_login_with_domain: bool = None,
    ):
        self.authn_sign_algo = authn_sign_algo
        # The auxiliary domain name.
        self.auxiliary_domain = auxiliary_domain
        # The metadata file, which is Base64-encoded.
        self.metadata_document = metadata_document
        # Indicates whether user-based SSO is enabled.
        self.sso_enabled = sso_enabled
        # Indicates whether the SAML SSO requires a domain name in the `<saml:NameID>` element of the SAML response. If yes, the username specified by the IdP for SSO must have a domain name as the suffix.
        # 
        # *   If the value of the parameter is `true`, the `<saml:NameID>` element **must** be in the `username@domain` format. You can set `domain` to the default domain name or the configured domain alias.
        # *   If the value of the parameter is `false`, the `<saml:NameID>` element **must** be in the `username` format and **cannot** contain the `domain` suffix.
        # 
        # The default value is `true`.
        self.sso_login_with_domain = sso_login_with_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authn_sign_algo is not None:
            result['AuthnSignAlgo'] = self.authn_sign_algo

        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain

        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document

        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled

        if self.sso_login_with_domain is not None:
            result['SsoLoginWithDomain'] = self.sso_login_with_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthnSignAlgo') is not None:
            self.authn_sign_algo = m.get('AuthnSignAlgo')

        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')

        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')

        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')

        if m.get('SsoLoginWithDomain') is not None:
            self.sso_login_with_domain = m.get('SsoLoginWithDomain')

        return self

