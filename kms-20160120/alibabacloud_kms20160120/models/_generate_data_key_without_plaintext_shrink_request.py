# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateDataKeyWithoutPlaintextShrinkRequest(DaraModel):
    def __init__(
        self,
        dry_run: str = None,
        encryption_context_shrink: str = None,
        key_id: str = None,
        key_spec: str = None,
        number_of_bytes: int = None,
    ):
        # Specifies whether to enable the DryRun mode.
        # 
        # - true: enables the DryRun mode.
        # 
        # - false (default): disables the DryRun mode.
        # 
        # The DryRun mode is used to test API calls, verify your permissions on the required resources, and check if the request parameters are valid. If you enable the DryRun mode, KMS returns a failure response with a reason. The failure reasons include the following:
        # 
        # - DryRunOperationError: The request would have succeeded if the DryRun parameter was not specified.
        # 
        # - ValidationError: The request parameters are invalid.
        # 
        # - AccessDeniedError: You are not authorized to perform this operation on the KMS resource.
        self.dry_run = dry_run
        # A JSON string of key-value pairs. If you specify this parameter, you must provide the same parameter when you call the Decrypt operation. For more information, see [EncryptionContext](https://help.aliyun.com/document_detail/42975.html).
        self.encryption_context_shrink = encryption_context_shrink
        # The globally unique identifier of the CMK. You can also specify an alias that is bound to the CMK. For more information about how to use an alias, see Alias overview.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The length of the data key to generate. Valid values:
        # 
        # - AES_256: a 256-bit symmetric key
        # 
        # - AES_128: a 128-bit symmetric key
        # 
        # > Use KeySpec or NumberOfBytes to specify the length of the data key. If you do not specify either parameter, KMS generates a 256-bit data key. If you specify both parameters, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec
        # The length of the data key to generate.<br> Valid values: 1 to 1024.<br> Unit: bytes<br><br><br><br><br>
        self.number_of_bytes = number_of_bytes

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

        return self

