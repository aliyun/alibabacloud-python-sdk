# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSAMLProviderRequest(DaraModel):
    def __init__(
        self,
        authn_sign_algo: str = None,
        new_description: str = None,
        new_encoded_samlmetadata_document: str = None,
        samlprovider_name: str = None,
    ):
        # The signature algorithm supported by the Alibaba Cloud service provider (SP). Valid values:
        # 
        # - rsa-sha256
        # 
        # - rsa-sha1
        self.authn_sign_algo = authn_sign_algo
        # The new description.
        # 
        # > Specify at least one of the `NewDescription` and `NewEncodedSAMLMetadataDocument` parameters.
        self.new_description = new_description
        # The new metadata file.
        # 
        # > Specify at least one of the `NewDescription` and `NewEncodedSAMLMetadataDocument` parameters.
        self.new_encoded_samlmetadata_document = new_encoded_samlmetadata_document
        # The name of the identity provider to modify.
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

        if self.new_description is not None:
            result['NewDescription'] = self.new_description

        if self.new_encoded_samlmetadata_document is not None:
            result['NewEncodedSAMLMetadataDocument'] = self.new_encoded_samlmetadata_document

        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthnSignAlgo') is not None:
            self.authn_sign_algo = m.get('AuthnSignAlgo')

        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')

        if m.get('NewEncodedSAMLMetadataDocument') is not None:
            self.new_encoded_samlmetadata_document = m.get('NewEncodedSAMLMetadataDocument')

        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')

        return self

