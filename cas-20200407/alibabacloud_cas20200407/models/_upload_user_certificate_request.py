# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class UploadUserCertificateRequest(DaraModel):
    def __init__(
        self,
        cert: str = None,
        encrypt_cert: str = None,
        encrypt_private_key: str = None,
        key: str = None,
        name: str = None,
        resource_group_id: str = None,
        sign_cert: str = None,
        sign_private_key: str = None,
        tags: List[main_models.UploadUserCertificateRequestTags] = None,
    ):
        # The content of the certificate in the PEM format.
        self.cert = cert
        # The content of the encryption certificate in PEM format.
        self.encrypt_cert = encrypt_cert
        # The private key of the encryption certificate in the PEM format.
        self.encrypt_private_key = encrypt_private_key
        # The private key of the certificate in the PEM format.
        self.key = key
        # The name of the certificate. The name can be up to 64 characters in length, and can contain all types of characters, such as letters, digits, and underscores (_).
        # 
        # >  The name must be unique within an Alibaba Cloud account.
        # 
        # This parameter is required.
        self.name = name
        # the resource group id.
        self.resource_group_id = resource_group_id
        # The content of the signing certificate in the PEM format.
        self.sign_cert = sign_cert
        # The private key of the signing certificate in the PEM format.
        self.sign_private_key = sign_private_key
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert is not None:
            result['Cert'] = self.cert

        if self.encrypt_cert is not None:
            result['EncryptCert'] = self.encrypt_cert

        if self.encrypt_private_key is not None:
            result['EncryptPrivateKey'] = self.encrypt_private_key

        if self.key is not None:
            result['Key'] = self.key

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sign_cert is not None:
            result['SignCert'] = self.sign_cert

        if self.sign_private_key is not None:
            result['SignPrivateKey'] = self.sign_private_key

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')

        if m.get('EncryptCert') is not None:
            self.encrypt_cert = m.get('EncryptCert')

        if m.get('EncryptPrivateKey') is not None:
            self.encrypt_private_key = m.get('EncryptPrivateKey')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SignCert') is not None:
            self.sign_cert = m.get('SignCert')

        if m.get('SignPrivateKey') is not None:
            self.sign_private_key = m.get('SignPrivateKey')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UploadUserCertificateRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class UploadUserCertificateRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

