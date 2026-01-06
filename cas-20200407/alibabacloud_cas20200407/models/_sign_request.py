# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SignRequest(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        custom_identifier: str = None,
        message: str = None,
        message_type: str = None,
        signing_algorithm: str = None,
        warehouse_id: int = None,
    ):
        # The unique identifier of the certificate. You can call the [ListCert](https://help.aliyun.com/document_detail/455806.html) operation to obtain the identifier.
        # 
        # *   If the certificate is an SSL certificate, the value of this parameter must be in the {Certificate ID}-cn-hangzhou format.
        # *   If the certificate is a private certificate, the value of this parameter must be the value of the Identifier field for the private certificate.
        self.cert_identifier = cert_identifier
        self.custom_identifier = custom_identifier
        # The data to sign. The value must be encoded in Base64.\\
        # For example, if the hexadecimal data that you want to sign is [0x31, 0x32, 0x33, 0x34], set the parameter to the Base64-encoded value MTIzNA==. If you set MessageType to RAW, the size of the data must be less than 4 KB. If the size of the data is greater than 4 KB, you can set MessageType to DIGEST and set Message to the digest of the data. The digest is a hash value. You can compute the digest of the data on an on-premises machine. The certificate application repository uses the digest that you compute in your own certificate application system. The message digest algorithm that you use must match the specified signature algorithm. The following items describe the details:
        # 
        # *   If the signature algorithm is SHA256withRSA, SHA256withRSA/PSS, or SHA256withECDSA, the message digest algorithm must be SHA-256.
        # *   If the signature algorithm is SM3withSM2, the message digest algorithm must be SM3.
        # 
        # This parameter is required.
        self.message = message
        # The value type of the Message parameter. Valid values:
        # 
        # *   RAW: the raw data. This is the default value.
        # *   DIGEST: the message digest (hash value) of the raw data.
        # 
        # This parameter is required.
        self.message_type = message_type
        # The signature algorithm. Valid values:
        # 
        # *   SHA256withRSA
        # *   SHA256withRSA/PSS
        # *   SHA256withECDSA
        # *   SM3withSM2
        # 
        # This parameter is required.
        self.signing_algorithm = signing_algorithm
        self.warehouse_id = warehouse_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.custom_identifier is not None:
            result['CustomIdentifier'] = self.custom_identifier

        if self.message is not None:
            result['Message'] = self.message

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.signing_algorithm is not None:
            result['SigningAlgorithm'] = self.signing_algorithm

        if self.warehouse_id is not None:
            result['WarehouseId'] = self.warehouse_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CustomIdentifier') is not None:
            self.custom_identifier = m.get('CustomIdentifier')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('SigningAlgorithm') is not None:
            self.signing_algorithm = m.get('SigningAlgorithm')

        if m.get('WarehouseId') is not None:
            self.warehouse_id = m.get('WarehouseId')

        return self

