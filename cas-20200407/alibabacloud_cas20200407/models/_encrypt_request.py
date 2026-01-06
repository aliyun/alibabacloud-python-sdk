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
        # *   **RSAES_OAEP_SHA_1**
        # *   **RSAES_OAEP_SHA_256**
        # *   **SM2PKE**
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The unique identifier of the certificate. You can call the [ListCert](https://help.aliyun.com/document_detail/455806.html) operation to obtain the identifier.
        # 
        # *   If the certificate is an SSL certificate, the value of this parameter must be in the {Certificate ID}-cn-hangzhou format.
        # *   If the certificate is a private certificate, the value of this parameter must be the value of the Identifier field for the private certificate.
        self.cert_identifier = cert_identifier
        self.custom_identifier = custom_identifier
        # The value type of the Message parameter. Valid values:
        # 
        # *   RAW: The value of the Plaintext parameter is directly encrypted. This is the default value.
        # *   Base64: The value of the Plaintext parameter is Base64-encoded data. The data is decoded and then encrypted.
        self.message_type = message_type
        # The data that you want to encrypt. The value of this parameter can be raw data or Base64-encoded data. For more information, see the description of the MessageType parameter. For example, if the hexadecimal data that you want to encrypt is `[0x31, 0x32, 0x33, 0x34]`, the Base64-encoded data is MTIzNA==. The size of data that can be encrypted varies based on the encryption algorithm that you use. The following list describes the relationship between the encryption algorithms and data sizes:
        # 
        # *   **RSAES_OAEP_SHA_1**: 214 bytes
        # *   **RSAES_OAEP_SHA_256**: 190 bytes
        # *   **SM2PKE**: 6,047 bytes
        # 
        # This parameter is required.
        self.plaintext = plaintext
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

