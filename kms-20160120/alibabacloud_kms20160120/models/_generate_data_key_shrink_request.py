# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateDataKeyShrinkRequest(DaraModel):
    def __init__(
        self,
        dry_run: str = None,
        encryption_context_shrink: str = None,
        key_id: str = None,
        key_spec: str = None,
        number_of_bytes: int = None,
        recipient: str = None,
    ):
        # Specifies whether to enable the DryRun mode.
        # 
        # - true: enables the DryRun mode.
        # 
        # - false (default): disables the DryRun mode.
        # 
        # The DryRun mode is used to test the API call. It verifies whether you have the permissions to access the specified resources and whether the request parameters are valid. If you enable the DryRun mode, KMS always returns a failure response and a failure reason. The failure reasons include the following:
        # 
        # - DryRunOperationError: The request succeeds if the DryRun parameter is not specified.
        # 
        # - ValidationError: The parameters specified in the request are invalid.
        # 
        # - AccessDeniedError: You are not authorized to perform this operation on the KMS resource.
        self.dry_run = dry_run
        # A JSON string that consists of key-value pairs.
        # 
        # If you specify this parameter, you must also specify the same parameter when you call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation. For more information, see [EncryptionContext](https://help.aliyun.com/document_detail/42975.html).
        self.encryption_context_shrink = encryption_context_shrink
        # The ID of the key. You can also specify the alias or the key resource name (ARN) of the key. For more information about aliases, see [Manage aliases](https://help.aliyun.com/document_detail/480655.html).
        # 
        # > When you access a key in another Alibaba Cloud account, you must enter the ARN of the key. The key ARN is in the format of `acs:kms:${region}:${account}:key/${keyid}`.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The length of the data key to be generated. Valid values:
        # 
        # - AES_256: a 256-bit symmetric key.
        # 
        # - AES_128: a 128-bit symmetric key.
        # 
        # > We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If you do not specify either of the parameters, KMS generates a 256-bit data key. If you specify both parameters, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec
        # The length of the data key that you want to generate. Unit: bytes.
        # 
        # Valid values: 1 to 1024.
        # 
        # Default values:
        # 
        # - If you set KeySpec to AES_256, the default value of NumberOfBytes is 32.
        # 
        # - If you set KeySpec to AES_128, the default value of NumberOfBytes is 16.
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

        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink

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
            self.encryption_context_shrink = m.get('EncryptionContext')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')

        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')

        if m.get('Recipient') is not None:
            self.recipient = m.get('Recipient')

        return self

