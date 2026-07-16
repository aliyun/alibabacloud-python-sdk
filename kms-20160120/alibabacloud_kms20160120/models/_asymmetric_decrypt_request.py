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
    ):
        # The decryption algorithm.
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The ciphertext to be decrypted. The ciphertext is encoded in Base64.
        # 
        # > You can generate a ciphertext by calling the [AsymmetricEncrypt](https://help.aliyun.com/document_detail/148131.html) operation.
        # 
        # This parameter is required.
        self.ciphertext_blob = ciphertext_blob
        # Specifies whether to enable the dry run feature.
        # 
        # - true: enables the dry run feature.
        # 
        # - false: disables the dry run feature. This is the default value.
        # 
        # The dry run feature is used to test API calls, verify the permissions on the specified resources, and check the validity of the request parameters. If you enable the dry run feature, KMS always returns a failure response and the cause of the failure. The causes of the failure include the following:
        # 
        # - DryRunOperationError: The request would have succeeded if the DryRun parameter is not specified.
        # 
        # - ValidationError: The specified parameter in the request is invalid.
        # 
        # - AccessDeniedError: You are not authorized to perform this operation on the KMS resource.
        self.dry_run = dry_run
        # The ID of the key. You can also specify the alias or Amazon Resource Name (ARN) of the key. For more information about aliases, see [Manage aliases](https://help.aliyun.com/document_detail/480655.html).
        # 
        # > When you access a key in another Alibaba Cloud account, you must specify the ARN of the key. The ARN of a key is in the `acs:kms:${region}:${account}:key/${keyid}` format.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The ID of the key version. The globally unique identifier of the key version.
        # 
        # This parameter is required.
        self.key_version_id = key_version_id

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

        return self

