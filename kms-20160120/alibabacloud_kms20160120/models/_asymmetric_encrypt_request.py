# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsymmetricEncryptRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        dry_run: str = None,
        key_id: str = None,
        key_version_id: str = None,
        plaintext: str = None,
    ):
        # The encryption algorithm.
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # Specifies whether to enable the dry run feature.
        # 
        # - true: enables the feature.
        # 
        # - false (default): disables the feature.
        # 
        # The dry run feature is used to test the API call and verify the permissions on the specified resources and the validity of the request parameters. If you enable the dry run feature, KMS always returns a failed result and a failure reason. The failure reasons include the following:
        # 
        # - DryRunOperationError: The request would have succeeded if the DryRun parameter was not specified.
        # 
        # - ValidationError: The specified parameters in the request are invalid.
        # 
        # - AccessDeniedError: You are not authorized to perform this operation on the KMS resource.
        self.dry_run = dry_run
        # The ID of the key. You can also specify the alias or the Amazon Resource Name (ARN) of the key. For more information about aliases, see [Manage aliases](https://help.aliyun.com/document_detail/480655.html).
        # 
        # > To access a key of another Alibaba Cloud account, you must specify the ARN of the key. The key ARN is in the format of `acs:kms:${region}:${account}:key/${keyid}`.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The ID of the key version. The ID must be a globally unique identifier.
        # 
        # > To obtain the key version ID, call the [ListKeyVersions](https://help.aliyun.com/document_detail/133966.html) operation.
        # 
        # This parameter is required.
        self.key_version_id = key_version_id
        # The plaintext to be encrypted. The value must be Base64-encoded.
        # 
        # This parameter is required.
        self.plaintext = plaintext

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id

        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')

        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')

        return self

