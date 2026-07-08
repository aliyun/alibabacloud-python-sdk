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
        # The unique identifier of the certificate. You can get this value by calling the [ListCert](https://help.aliyun.com/document_detail/455806.html) operation.
        # 
        # - The identifier of an SSL certificate is typically in the format \\"{Certificate ID}-cn-hangzhou\\".
        # 
        # - For a PCA certificate, this is the Identifier from the corresponding private certificate.
        self.cert_identifier = cert_identifier
        # A unique, user-defined identifier.
        self.custom_identifier = custom_identifier
        # The data to sign. The MessageType parameter determines the format of this data. If MessageType is set to RAW, Message is the raw data. If MessageType is set to BASE64, Message is the Base64-encoded raw data. If MessageType is set to DIGEST, Message is the message digest (hash value). If MessageType is set to BLIND, Message is the Base64-encoded blinded message.
        # 
        # This parameter is required.
        self.message = message
        # The message type. Valid values:
        # 
        # - `RAW` (default): The raw data.
        # 
        # - `DIGEST`: The message digest (hash value) of the raw data.
        # 
        # - `BASE64`: The Base64-encoded raw data.
        # 
        # - `BLIND`: Enables blind signing. This is supported only for certificates that use an RSA algorithm.
        # 
        # This parameter is required.
        self.message_type = message_type
        # The signature algorithm. Valid values:
        # 
        # - `SHA256withRSA`
        # 
        # - `SHA256withRSA/PSS`
        # 
        # - `SHA256withECDSA`
        # 
        # - `SM3withSM2`
        # 
        # - `SHA256withRSA/P7`
        # 
        # This parameter is required.
        self.signing_algorithm = signing_algorithm
        # The repository ID.
        # 
        # > You can get this ID by calling the [ListCertWarehouse](https://help.aliyun.com/document_detail/455805.html) operation.
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

