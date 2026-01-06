# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DecryptRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_identifier: str = None,
        ciphertext_blob: str = None,
        custom_identifier: str = None,
        message_type: str = None,
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
        # The unique identifier of the certificate. You can call the [ListCert](https://help.aliyun.com/document_detail/455806.html) operation to query the identifier.
        # 
        # *   If the certificate is an SSL certificate, the value of this parameter must be in the {Certificate ID}-cn-hangzhou format.
        # *   If the certificate is a private certificate, the value of this parameter must be the value of the Identifier field for the private certificate.
        self.cert_identifier = cert_identifier
        # The data that you want to decrypt. The value is encoded in Base64.
        # 
        # This parameter is required.
        self.ciphertext_blob = ciphertext_blob
        self.custom_identifier = custom_identifier
        # The value type of the Message parameter. Valid values:
        # 
        # *   RAW: The returned result is raw data encoded in UTF-8.
        # *   Base64: The returned result is Base64-encoded data. This is the default value.
        self.message_type = message_type
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

        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob

        if self.custom_identifier is not None:
            result['CustomIdentifier'] = self.custom_identifier

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.warehouse_id is not None:
            result['WarehouseId'] = self.warehouse_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')

        if m.get('CustomIdentifier') is not None:
            self.custom_identifier = m.get('CustomIdentifier')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('WarehouseId') is not None:
            self.warehouse_id = m.get('WarehouseId')

        return self

