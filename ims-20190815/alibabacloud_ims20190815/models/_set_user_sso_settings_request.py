# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetUserSsoSettingsRequest(DaraModel):
    def __init__(
        self,
        authn_sign_algo: str = None,
        auxiliary_domain: str = None,
        metadata_document: str = None,
        sso_enabled: bool = None,
        sso_login_with_domain: bool = None,
    ):
        # The signature algorithm that is supported by the Alibaba Cloud service provider (SP). Valid values:
        # 
        # - rsa-sha256
        # 
        # - rsa-sha1 (default)
        self.authn_sign_algo = authn_sign_algo
        # The auxiliary domain name.
        self.auxiliary_domain = auxiliary_domain
        # The metadata file. The file must be Base64-encoded.
        # 
        # The file is provided by an identity provider (IdP) that supports the Security Assertion Markup Language (SAML) 2.0 protocol.
        self.metadata_document = metadata_document
        # Specifies whether to enable user-based SSO for Resource Access Management (RAM) users. Valid values:
        # 
        # - true: Enables user-based SSO.
        # 
        # - false (default): Disables user-based SSO.
        self.sso_enabled = sso_enabled
        # Specifies whether the `<saml:NameID>` element in a SAML response must contain a domain name when a user logs on using SAML-based SSO. This applies if the username that is specified on the IdP for logon matching contains a domain name suffix.
        # 
        # - If this parameter is set to `true`, the value of the `<saml:NameID>` element **must** be in the `username@domain` format, which includes a domain name suffix. The `domain` can be the default domain name or a domain alias if one is configured.
        # 
        # - If this parameter is set to `false`, the value of the `<saml:NameID>` element **must** be the `username` only. The value **must not** contain the `domain` part.
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

