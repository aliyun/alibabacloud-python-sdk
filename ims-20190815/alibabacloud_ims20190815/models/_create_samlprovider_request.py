# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSAMLProviderRequest(DaraModel):
    def __init__(
        self,
        authn_sign_algo: str = None,
        description: str = None,
        encoded_samlmetadata_document: str = None,
        samlprovider_name: str = None,
    ):
        self.authn_sign_algo = authn_sign_algo
        # The description.
        self.description = description
        # The metadata file which is Base64-encoded.
        # 
        # The file is provided by an IdP that supports Security Assertion Markup Language (SAML) 2.0.
        self.encoded_samlmetadata_document = encoded_samlmetadata_document
        # The name of the IdP.
        # 
        # The name can be up to 128 characters in length. The name can contain letters, digits, `periods (.), hyphens (-), and underscores (_)`. The name cannot start or end with `periods (.), hyphens (-), or underscores (_)`.
        # 
        # This parameter is required.
        self.samlprovider_name = samlprovider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authn_sign_algo is not None:
            result['AuthnSignAlgo'] = self.authn_sign_algo

        if self.description is not None:
            result['Description'] = self.description

        if self.encoded_samlmetadata_document is not None:
            result['EncodedSAMLMetadataDocument'] = self.encoded_samlmetadata_document

        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthnSignAlgo') is not None:
            self.authn_sign_algo = m.get('AuthnSignAlgo')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncodedSAMLMetadataDocument') is not None:
            self.encoded_samlmetadata_document = m.get('EncodedSAMLMetadataDocument')

        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')

        return self

