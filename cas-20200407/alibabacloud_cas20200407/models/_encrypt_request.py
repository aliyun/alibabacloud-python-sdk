# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EncryptRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_identifier: str = None,
        custom_identifier: str = None,
        message_type: str = None,
        plaintext: str = None,
        warehouse_id: int = None,
    ):
        # The encryption algorithm. Valid values:
        # 
        # - **RSAES_OAEP_SHA_1**
        # 
        # - **RSAES_OAEP_SHA_256**
        # 
        # - **SM2PKE**
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The unique identifier of the certificate. To obtain this parameter, call the [ListCert](https://help.aliyun.com/document_detail/455806.html) operation.
        # 
        # - The identifier of an SSL certificate is usually in the {Certificate ID}-cn-hangzhou format.
        # 
        # - For a private certificate authority (PCA) certificate, this is the value of the Identifier field of the private certificate.
        self.cert_identifier = cert_identifier
        # The custom identifier, which serves as a unique key.
        self.custom_identifier = custom_identifier
        # The message type. Valid values:
        # 
        # - RAW (default): Directly encrypts the value of Plaintext.
        # 
        # - Base64: Decodes the Base64-encoded value of Plaintext and then encrypts the decoded data.
        self.message_type = message_type
        # The data to encrypt. The data can be plaintext or Base64-encoded plaintext. For more information, see the MessageType parameter. If you use Base64 encoding, for example, if the hexadecimal content of the data to be encrypted is `[0x31, 0x32, 0x33, 0x34]`, the corresponding Base64-encoded string is MTIzNA==. The maximum size of Plaintext depends on the Algorithm:
        # 
        # - **RSAES_OAEP_SHA_1**: 214 bytes.
        # 
        # - **RSAES_OAEP_SHA_256**: 190 bytes.
        # 
        # - **SM2PKE**: 6047 bytes.
        # 
        # This parameter is required.
        self.plaintext = plaintext
        # The repository ID.
        # 
        # > To obtain this ID, call the [ListCertWarehouse](https://help.aliyun.com/document_detail/455805.html) operation.
        self.warehouse_id = warehouse_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.custom_identifier is not None:
            result['CustomIdentifier'] = self.custom_identifier

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext

        if self.warehouse_id is not None:
            result['WarehouseId'] = self.warehouse_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CustomIdentifier') is not None:
            self.custom_identifier = m.get('CustomIdentifier')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')

        if m.get('WarehouseId') is not None:
            self.warehouse_id = m.get('WarehouseId')

        return self

