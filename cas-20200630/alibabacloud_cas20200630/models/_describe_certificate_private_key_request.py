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
        # The password that is used to encrypt the private key. The password can contain letters, digits, and special characters, such as `, + - _ #`. The password can be up to 32 bytes in length.
        # 
        # **Warning** You must remember the password that you specify. The password is required to decrypt the encrypted private key. If you forget the password, the encrypted private key that is returned cannot be decrypted. You must call this operation again.
        # 
        # This parameter is required.
        self.encrypted_code = encrypted_code
        # The unique identifier of the client certificate or server certificate that you want to query.
        # 
        # >  You can call the [ListClientCertificate](https://help.aliyun.com/document_detail/330884.html) operation to query the unique identifiers of all client certificates and server certificates.
        # 
        # This parameter is required.
        self.identifier = identifier
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

