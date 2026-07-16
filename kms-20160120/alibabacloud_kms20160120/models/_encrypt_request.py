# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class EncryptRequest(DaraModel):
    def __init__(
        self,
        dry_run: str = None,
        encryption_context: Dict[str, Any] = None,
        key_id: str = None,
        plaintext: str = None,
    ):
        # Specifies whether to enable the dry run feature.
        # 
        # - true: enables the dry run feature.
        # 
        # - false (default): disables the dry run feature.
        # 
        # The dry run feature is used to test API calls and verify the permissions on the resources that you have and the validity of the request parameters. You can view the check results in the response.
        # 
        # - DryRunOperationError: The permissions and parameters are valid. If you do not specify the DryRun parameter, the request is successful.
        # 
        # - ValidationError: The parameters in the request are invalid.
        # 
        # - AccessDeniedError: You are not authorized to perform this operation on the KMS resource.
        self.dry_run = dry_run
        # A JSON string that consists of key-value pairs. If you specify this parameter, you must specify the same parameter when you call the Decrypt operation. For more information, see [EncryptionContext](https://help.aliyun.com/document_detail/42975.html).
        self.encryption_context = encryption_context
        # The ID of the key. You can also specify the alias or Amazon Resource Name (ARN) of the key. For more information about aliases, see [Manage aliases](https://help.aliyun.com/document_detail/480655.html).
        # 
        # > When you access a key in another Alibaba Cloud account, you must specify the ARN of the key. The ARN of a key is in the `acs:kms:${region}:${account}:key/${keyid}` format.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The plaintext to be encrypted. The plaintext must be Base64-encoded.
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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')

        return self

