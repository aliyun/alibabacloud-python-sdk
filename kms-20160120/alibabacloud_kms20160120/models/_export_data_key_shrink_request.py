# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportDataKeyShrinkRequest(DaraModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        dry_run: str = None,
        encryption_context_shrink: str = None,
        public_key_blob: str = None,
        wrapping_algorithm: str = None,
        wrapping_key_spec: str = None,
    ):
        # The ciphertext of the data key that is encrypted using a master key (CMK).
        # 
        # This parameter is required.
        self.ciphertext_blob = ciphertext_blob
        # Specifies whether to enable the DryRun mode.
        # 
        # - true
        # 
        # - false (default)
        # 
        # The DryRun mode is used to test the API call and verify the permissions on the specified resources and the validity of the request parameters. If you enable the DryRun mode, KMS returns a failure response and a failure reason. The failure reasons include the following:
        # 
        # - DryRunOperationError: The request would have succeeded if the DryRun parameter was not specified.
        # 
        # - ValidationError: The specified parameters in the request are invalid.
        # 
        # - AccessDeniedError: You are not authorized to perform the operation on the KMS resource.
        self.dry_run = dry_run
        # A JSON string that consists of key-value pairs. EncryptionContext is the encryption context that is passed in when the data key is encrypted using a CMK. For more information, see [EncryptionContext](https://help.aliyun.com/document_detail/42975.html).
        self.encryption_context_shrink = encryption_context_shrink
        # The public key in Base64 format.
        # 
        # This parameter is required.
        self.public_key_blob = public_key_blob
        # The encryption algorithm that is used to encrypt the data key using the public key specified by PublicKeyBlob. For more information about the algorithms, see [AsymmetricDecrypt](https://help.aliyun.com/document_detail/148130.html).<br> Valid values:<br><br>
        # 
        # - RSAES_OAEP_SHA_256
        # 
        # - RSAES_OAEP_SHA_1
        # 
        # - SM2PKE
        # 
        # This parameter is required.
        self.wrapping_algorithm = wrapping_algorithm
        # The type of the public key specified by PublicKeyBlob. For more information about key types, see [Introduction to asymmetric keys](https://help.aliyun.com/document_detail/148147.html).<br> Valid values:<br><br>
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
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink

        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob

        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm

        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')

        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')

        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')

        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')

        return self

