# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyRequest(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        custom_identifier: str = None,
        message: str = None,
        message_type: str = None,
        signature_value: str = None,
        signing_algorithm: str = None,
        warehouse_id: str = None,
    ):
        # The unique identifier of the certificate. To get this parameter, call the [ListCert](https://help.aliyun.com/document_detail/455806.html) operation.
        # 
        # - The identifier for an SSL certificate is typically in the format \\`{Certificate ID}-cn-hangzhou\\`.
        # 
        # - For a PCA certificate, this is the value of the \\`Identifier\\` field.
        self.cert_identifier = cert_identifier
        # The custom identifier. This key must be unique.
        self.custom_identifier = custom_identifier
        # The data to verify. The data must be Base64-encoded. For example, if the hexadecimal content of the data to sign is \\`[0x31, 0x32, 0x33, 0x34]\\`, the Base64-encoded value is \\`MTIzNA==\\`. If you set \\`MessageType\\` to \\`RAW\\`, the data size must be less than 4 KB. If the data to sign is larger than 4 KB, set \\`MessageType\\` to \\`DIGEST\\`. Then, set \\`Message\\` to the message digest, or hash, that you calculate locally. The hashing algorithm for the digest must be compatible with the signature algorithm:<br>
        # 
        # - The hashing algorithm for \\`SHA256withRSA\\`, \\`SHA256withRSA/PSS\\`, and \\`SHA256withECDSA\\` is SHA-256.
        # 
        # - The hashing algorithm for \\`SM3withSM2\\` is SM3.
        # 
        # This parameter is required.
        self.message = message
        # The message type. Valid values:
        # 
        # - **RAW** (default): The raw data.
        # 
        # - **DIGEST**: The message digest of the raw data.
        # 
        # This parameter is required.
        self.message_type = message_type
        # The signature value. The value must be Base64-encoded.
        # 
        # This parameter is required.
        self.signature_value = signature_value
        # The signature algorithm. Valid values:
        # 
        # - **SHA256withRSA**
        # 
        # - **SHA256withRSA/PSS**
        # 
        # - **SHA256withECDSA**
        # 
        # - **SM3withSM2**
        # 
        # This parameter is required.
        self.signing_algorithm = signing_algorithm
        # The ID of the repository. To get this parameter, call the [ListCertWarehouse](https://help.aliyun.com/document_detail/453246.html) operation.
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

        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value

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

        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')

        if m.get('SigningAlgorithm') is not None:
            self.signing_algorithm = m.get('SigningAlgorithm')

        if m.get('WarehouseId') is not None:
            self.warehouse_id = m.get('WarehouseId')

        return self

