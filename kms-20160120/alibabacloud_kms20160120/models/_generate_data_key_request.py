# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GenerateDataKeyRequest(DaraModel):
    def __init__(
        self,
        dry_run: str = None,
        encryption_context: Dict[str, Any] = None,
        key_id: str = None,
        key_spec: str = None,
        number_of_bytes: int = None,
        recipient: str = None,
    ):
        # Specifies whether to enable DryRun mode.
        # 
        # - true: enabled.
        # - false (default): disabled.
        # 
        # DryRun mode is used to test API calls, verify that you have the required permissions on the relevant resources, and check whether request parameters are configured correctly. When DryRun mode is enabled, KMS always returns a failure with a reason. Possible failure reasons include:
        # 
        # - DryRunOperationError: The request would succeed if the DryRun parameter were not set.
        # - ValidationError: A parameter specified in the request is invalid.
        # - AccessDeniedError: You do not have permission to perform the operation on the KMS resource.
        self.dry_run = dry_run
        # A JSON string of key-value pairs.
        # 
        # If you specify this parameter, you must provide the same parameter when you call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation. For more information, see [EncryptionContext](https://help.aliyun.com/document_detail/42975.html).
        self.encryption_context = encryption_context
        # The ID of the key. You can also specify a key alias or a key Amazon Resource Name (ARN). For more information about aliases, see [Manage key aliases](https://help.aliyun.com/document_detail/480655.html).
        # >To access a key in another Alibaba Cloud account, you must specify the key ARN. The key ARN format is `acs:kms:${region}:${account}:key/${keyid}`.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The length of the data key (DK) to generate. Valid values:
        # 
        # - AES_256: a 256-bit symmetric key.
        # 
        # - AES_128: a 128-bit symmetric key.
        # 
        # > Use KeySpec or NumberOfBytes to specify the DK length. If neither is specified, KMS generates a 256-bit DK. If both are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec
        # The length of the data key (DK) to generate, in bytes.
        # 
        # Valid values: 1 to 1024.
        # 
        # Default value:
        # - When KeySpec is set to AES_256, the default value of NumberOfBytes is 32.
        # - When KeySpec is set to AES_128, the default value of NumberOfBytes is 16.
        self.number_of_bytes = number_of_bytes
        self.recipient = recipient

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

        if self.recipient is not None:
            result['Recipient'] = self.recipient

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

        if m.get('Recipient') is not None:
            self.recipient = m.get('Recipient')

        return self

