# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCertificatePrivateKeyRequest(DaraModel):
    def __init__(
        self,
        encrypted_code: str = None,
        identifier: str = None,
        resource_group_id: str = None,
    ):
        # The password to encrypt the private key. The password can contain uppercase letters, lowercase letters, digits, and special characters, such as `,.+-_#`. The maximum length is 32 bytes.
        # 
        # >Warning: 
        # 
        # Remember the password you set. You need this password to decrypt the encrypted private key. If you forget the password, you cannot decrypt the private key that you get from this API call. You must call this API again to get a new encrypted key.
        # 
        # This parameter is required.
        self.encrypted_code = encrypted_code
        # The unique identifier of the client or server-side certificate for which you want to get the private key.
        # 
        # > Call [ListClientCertificate](https://help.aliyun.com/document_detail/465990.html) to query the unique identifiers of all client and server-side certificates.
        # 
        # This parameter is required.
        self.identifier = identifier
        # The ID of the resource group to which the certificate belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted_code is not None:
            result['EncryptedCode'] = self.encrypted_code

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedCode') is not None:
            self.encrypted_code = m.get('EncryptedCode')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

