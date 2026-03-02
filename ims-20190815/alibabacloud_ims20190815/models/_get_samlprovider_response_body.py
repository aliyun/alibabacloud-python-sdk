# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetSAMLProviderResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        samlprovider: main_models.GetSAMLProviderResponseBodySAMLProvider = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the SAML provider.
        self.samlprovider = samlprovider

    def validate(self):
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SAMLProvider') is not None:
            temp_model = main_models.GetSAMLProviderResponseBodySAMLProvider()
            self.samlprovider = temp_model.from_map(m.get('SAMLProvider'))

        return self

class GetSAMLProviderResponseBodySAMLProvider(DaraModel):
    def __init__(
        self,
        arn: str = None,
        authn_sign_algo: str = None,
        create_date: str = None,
        description: str = None,
        encoded_samlmetadata_document: str = None,
        samlprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the SAML provider.
        self.arn = arn
        # The signature algorithm supported by the Alibaba Cloud service provider (SP). Valid values:
        # 
        # - rsa-sha256
        # 
        # - rsa-sha1
        self.authn_sign_algo = authn_sign_algo
        # The time when the SAML provider was created.
        self.create_date = create_date
        # The description.
        self.description = description
        # The Base64-encoded metadata file.
        self.encoded_samlmetadata_document = encoded_samlmetadata_document
        # The name of the SAML provider.
        self.samlprovider_name = samlprovider_name
        # The time when the SAML provider was last updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.authn_sign_algo is not None:
            result['AuthnSignAlgo'] = self.authn_sign_algo

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.description is not None:
            result['Description'] = self.description

        if self.encoded_samlmetadata_document is not None:
            result['EncodedSAMLMetadataDocument'] = self.encoded_samlmetadata_document

        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('AuthnSignAlgo') is not None:
            self.authn_sign_algo = m.get('AuthnSignAlgo')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncodedSAMLMetadataDocument') is not None:
            self.encoded_samlmetadata_document = m.get('EncodedSAMLMetadataDocument')

        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

