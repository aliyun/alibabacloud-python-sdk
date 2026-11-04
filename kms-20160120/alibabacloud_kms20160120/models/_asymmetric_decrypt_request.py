# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsymmetricDecryptRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        ciphertext_blob: str = None,
        dry_run: str = None,
        key_id: str = None,
        key_version_id: str = None,
        recipient: str = None,
    ):
        # The decryption algorithm.
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The ciphertext to be decrypted, which is Base64-encoded. 
        # 
        # > You can call the [AsymmetricEncrypt](https://help.aliyun.com/document_detail/148131.html) operation to generate ciphertext.
        # 
        # This parameter is required.
        self.ciphertext_blob = ciphertext_blob
        # Specifies whether to enable the dry run mode.
        # 
        # - true: enables the dry run mode.
        # - false: disables the dry run mode. This is the default value.
        # 
        # The dry run mode is used to test API calls and verify whether you have the required permissions on the resources and whether the request parameters are correctly configured. When the dry run mode is enabled, KMS always returns a failure and provides the cause of the failure. The causes include:
        # 
        # - DryRunOperationError: The request would succeed if the DryRun parameter is not specified.
        # - ValidationError: A parameter specified in the request is invalid.
        # - AccessDeniedError: You are not authorized to perform the operation on the KMS resource.
        self.dry_run = dry_run
        # The ID of the key. You can also specify the alias or Alibaba Cloud Resource Name (ARN) of the key. For more information about aliases, refer to [Manage key aliases](https://help.aliyun.com/document_detail/480655.html).
        # > To access a key that belongs to another Alibaba Cloud account, you must enter the ARN of the key. The ARN of a key is in the `acs:kms:${region}:${account}:key/${keyid}` format.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The ID of the key version, which is the globally unique identifier of the key version.
        # 
        # This parameter is required.
        self.key_version_id = key_version_id
        # The remote attestation.
        self.recipient = recipient

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id

        if self.recipient is not None:
            result['Recipient'] = self.recipient

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')

        if m.get('Recipient') is not None:
            self.recipient = m.get('Recipient')

        return self

