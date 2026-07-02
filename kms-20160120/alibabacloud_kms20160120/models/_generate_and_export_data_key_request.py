# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GenerateAndExportDataKeyRequest(DaraModel):
    def __init__(
        self,
        dry_run: str = None,
        encryption_context: Dict[str, Any] = None,
        key_id: str = None,
        key_spec: str = None,
        number_of_bytes: int = None,
        public_key_blob: str = None,
        wrapping_algorithm: str = None,
        wrapping_key_spec: str = None,
    ):
        # Specifies whether to enable the dry run feature.
        # 
        # - true: enables the feature.
        # 
        # - false (default): disables the feature.
        # 
        # The DryRun mode is used to test API calls and verify the permissions on the resources that you have access to and the validity of the request parameters. If you enable the DryRun mode, KMS always returns a failure response and the cause of the failure. The following failure causes are included:
        # 
        # - DryRunOperationError: The request would have succeeded if the DryRun parameter is not specified.
        # 
        # - ValidationError: The parameters specified in the request are invalid.
        # 
        # - AccessDeniedError: You are not authorized to perform this operation on the KMS resource.
        self.dry_run = dry_run
        # A JSON string that consists of key-value pairs. If you specify this parameter, you must specify the same parameter when you call the Decrypt operation or other operations to re-encrypt the data key. For more information, see [EncryptionContext](https://help.aliyun.com/document_detail/42975.html).
        self.encryption_context = encryption_context
        # The ID of the key. You can also specify the alias or Amazon Resource Name (ARN) of the key. For more information about aliases, see [Manage aliases](https://help.aliyun.com/document_detail/480655.html).
        # 
        # > To access a key in another Alibaba Cloud account, you must specify the ARN of the key. The key ARN is in the format of `acs:kms:${region}:${account}:key/${keyid}`.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The length of the data key that you want to generate. Valid values:
        # 
        # - AES_256: a 256-bit symmetric key.
        # 
        # - AES_128: a 128-bit symmetric key.
        # 
        # > We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If you do not specify either of the parameters, KMS generates a 256-bit data key. If you specify both parameters, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec
        # The length of the data key that you want to generate.
        # 
        # Valid values: 1 to 1024.
        # 
        # Unit: bytes.
        self.number_of_bytes = number_of_bytes
        # The public key that is encoded in Base64.
        # 
        # This parameter is required.
        self.public_key_blob = public_key_blob
        # The encryption algorithm that is used to encrypt the data key using the public key specified by PublicKeyBlob. For more information about encryption algorithms, see [AsymmetricDecrypt](https://help.aliyun.com/document_detail/148130.html).<br> Valid values:<br><br>
        # 
        # - RSAES_OAEP_SHA_256
        # 
        # - RSAES_OAEP_SHA_1
        # 
        # - SM2PKE
        # 
        # This parameter is required.
        self.wrapping_algorithm = wrapping_algorithm
        # The type of the key specified by PublicKeyBlob. For more information about key types, see [Introduction to asymmetric keys](https://help.aliyun.com/document_detail/148147.html).<br> Valid values:<br><br>
        # 
        # - RSA_2048
        # 
        # - EC_SM2
        # 
        # This parameter is required.
        self.wrapping_key_spec = wrapping_key_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec

        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes

        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob

        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm

        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')

        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')

        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')

        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')

        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')

        return self

