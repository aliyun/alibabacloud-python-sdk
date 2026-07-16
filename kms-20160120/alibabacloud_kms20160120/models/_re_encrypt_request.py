# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ReEncryptRequest(DaraModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        destination_encryption_context: Dict[str, Any] = None,
        destination_key_id: str = None,
        dry_run: str = None,
        source_encryption_algorithm: str = None,
        source_encryption_context: Dict[str, Any] = None,
        source_key_id: str = None,
        source_key_version_id: str = None,
    ):
        # The ciphertext that you want to re-encrypt.<br> This parameter can be the ciphertext that is returned after symmetric or asymmetric key encryption.<br><br>
        # 
        # - Symmetric encryption: the ciphertext that is returned after you call the [Encrypt](https://help.aliyun.com/document_detail/28949.html), [GenerateDataKey](https://help.aliyun.com/document_detail/28948.html), [GenerateDataKeyWithoutPlaintext](https://help.aliyun.com/document_detail/134043.html), or [GenerateAndExportDataKey](https://help.aliyun.com/document_detail/176804.html) operation.
        # 
        # - Asymmetric key encryption: the data that is encrypted using a public key after you call the [GenerateAndExportDataKey](https://help.aliyun.com/document_detail/176804.html) operation, or the data that is encrypted using an asymmetric public key in an external system.
        # 
        # This parameter is required.
        self.ciphertext_blob = ciphertext_blob
        # A JSON string that consists of key-value pairs. This parameter specifies the encryption context for the destination master key.
        self.destination_encryption_context = destination_encryption_context
        # The ID of the symmetric master key that is used to re-encrypt the data after the ciphertext is decrypted.
        # 
        # This parameter is required.
        self.destination_key_id = destination_key_id
        # Specifies whether to enable the DryRun mode.
        # 
        # - true: enables the DryRun mode.
        # 
        # - false (default): disables the DryRun mode.
        # 
        # The DryRun mode is used to test API calls, verify whether you have the permissions to perform operations on the required resources, and check whether the request parameters are valid. If you enable the DryRun mode, KMS always returns a failure and a reason for the failure. The reasons for the failure include the following:
        # 
        # - DryRunOperationError: The request would have succeeded if the DryRun parameter was not configured.
        # 
        # - ValidationError: The parameters specified in the request are invalid.
        # 
        # - AccessDeniedError: You are not authorized to perform the operation on the KMS resource.
        self.dry_run = dry_run
        # If CiphertextBlob is the result of public key encryption, specify the public key encryption algorithm. For more information about the algorithms, see [AsymmetricDecrypt](https://help.aliyun.com/document_detail/148130.html).<br> Valid values:<br><br>
        # 
        # - RSAES_OAEP_SHA_256
        # 
        # - RSAES_OAEP_SHA_1
        # 
        # - SM2PKE
        # 
        # > You must specify this parameter when CiphertextBlob is the data that is encrypted using a public key after asymmetric key encryption.
        self.source_encryption_algorithm = source_encryption_algorithm
        # A JSON string that consists of key-value pairs. If you specify this parameter when you call the [Encrypt](https://help.aliyun.com/document_detail/28949.html), [GenerateDataKey](https://help.aliyun.com/document_detail/28948.html), [GenerateDataKeyWithoutPlaintext](https://help.aliyun.com/document_detail/134043.html), or [GenerateAndExportDataKey](https://help.aliyun.com/document_detail/176804.html) operation, you must specify the same parameter to decrypt the data. For more information, see [EncryptionContext](https://help.aliyun.com/document_detail/42975.html).
        # 
        # > You must specify this parameter when CiphertextBlob is the ciphertext that is returned after symmetric encryption.
        self.source_encryption_context = source_encryption_context
        # The ID of the master key that is used to decrypt the ciphertext.<br> The globally unique identifier of the master key.<br><br>
        # 
        # > You must specify this parameter when CiphertextBlob is the data that is encrypted using a public key after asymmetric key encryption.
        self.source_key_id = source_key_id
        # The ID of the key version that is used to decrypt the ciphertext.
        # 
        # > You must specify this parameter when CiphertextBlob is the data that is encrypted using a public key after asymmetric key encryption.
        self.source_key_version_id = source_key_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob

        if self.destination_encryption_context is not None:
            result['DestinationEncryptionContext'] = self.destination_encryption_context

        if self.destination_key_id is not None:
            result['DestinationKeyId'] = self.destination_key_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.source_encryption_algorithm is not None:
            result['SourceEncryptionAlgorithm'] = self.source_encryption_algorithm

        if self.source_encryption_context is not None:
            result['SourceEncryptionContext'] = self.source_encryption_context

        if self.source_key_id is not None:
            result['SourceKeyId'] = self.source_key_id

        if self.source_key_version_id is not None:
            result['SourceKeyVersionId'] = self.source_key_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')

        if m.get('DestinationEncryptionContext') is not None:
            self.destination_encryption_context = m.get('DestinationEncryptionContext')

        if m.get('DestinationKeyId') is not None:
            self.destination_key_id = m.get('DestinationKeyId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('SourceEncryptionAlgorithm') is not None:
            self.source_encryption_algorithm = m.get('SourceEncryptionAlgorithm')

        if m.get('SourceEncryptionContext') is not None:
            self.source_encryption_context = m.get('SourceEncryptionContext')

        if m.get('SourceKeyId') is not None:
            self.source_key_id = m.get('SourceKeyId')

        if m.get('SourceKeyVersionId') is not None:
            self.source_key_version_id = m.get('SourceKeyVersionId')

        return self

