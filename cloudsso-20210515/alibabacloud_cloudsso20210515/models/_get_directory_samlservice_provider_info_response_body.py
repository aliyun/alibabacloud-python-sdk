# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetDirectorySAMLServiceProviderInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        samlservice_provider: main_models.GetDirectorySAMLServiceProviderInfoResponseBodySAMLServiceProvider = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the SP.
        self.samlservice_provider = samlservice_provider

    def validate(self):
        if self.samlservice_provider:
            self.samlservice_provider.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.samlservice_provider is not None:
            result['SAMLServiceProvider'] = self.samlservice_provider.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SAMLServiceProvider') is not None:
            temp_model = main_models.GetDirectorySAMLServiceProviderInfoResponseBodySAMLServiceProvider()
            self.samlservice_provider = temp_model.from_map(m.get('SAMLServiceProvider'))

        return self

class GetDirectorySAMLServiceProviderInfoResponseBodySAMLServiceProvider(DaraModel):
    def __init__(
        self,
        acs_url: str = None,
        authn_sign_algo: str = None,
        certificate_type: str = None,
        directory_id: str = None,
        encoded_metadata_document: str = None,
        entity_id: str = None,
        support_encrypted_assertion: bool = None,
    ):
        # The Assertion Consumer Service (ACS) URL of the SP.
        self.acs_url = acs_url
        # The signature algorithm supported by the AuthNRequest initiated by Alibaba Cloud. Value:
        # 
        # - rsa-sha256
        # 
        # - rsa-sha1
        self.authn_sign_algo = authn_sign_algo
        # The certificate type used by Alibaba Cloud for signing during the SSO process. Value:
        # 
        # - self-signed: Use a self-signed certificate.
        # 
        # - public: Use a certificate issued by CA.
        self.certificate_type = certificate_type
        # The ID of the directory.
        self.directory_id = directory_id
        # The metadata file of the SP. The value of this parameter is Base64-encoded.
        self.encoded_metadata_document = encoded_metadata_document
        # The entity ID of the SP.
        self.entity_id = entity_id
        # Whether to support Assertion encryption on the IdP side.
        self.support_encrypted_assertion = support_encrypted_assertion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acs_url is not None:
            result['AcsUrl'] = self.acs_url

        if self.authn_sign_algo is not None:
            result['AuthnSignAlgo'] = self.authn_sign_algo

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.encoded_metadata_document is not None:
            result['EncodedMetadataDocument'] = self.encoded_metadata_document

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.support_encrypted_assertion is not None:
            result['SupportEncryptedAssertion'] = self.support_encrypted_assertion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcsUrl') is not None:
            self.acs_url = m.get('AcsUrl')

        if m.get('AuthnSignAlgo') is not None:
            self.authn_sign_algo = m.get('AuthnSignAlgo')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('EncodedMetadataDocument') is not None:
            self.encoded_metadata_document = m.get('EncodedMetadataDocument')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('SupportEncryptedAssertion') is not None:
            self.support_encrypted_assertion = m.get('SupportEncryptedAssertion')

        return self

