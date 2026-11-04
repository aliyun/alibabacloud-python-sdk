# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsymmetricSignRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        digest: str = None,
        dry_run: str = None,
        key_id: str = None,
        key_version_id: str = None,
    ):
        # The signature algorithm.
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The digest generated from the original message by using the hash algorithm that corresponds to the value of the Algorithm parameter.
        # 
        # > - The value is Base64-encoded.
        # - For more information about how to calculate a message digest, see the **Signature preprocessing: Calculate the message digest** section in [Asymmetric digital signatures](https://help.aliyun.com/document_detail/148146.html).
        # 
        # This parameter is required.
        self.digest = digest
        # Specifies whether to enable the dry run mode.
        # 
        # - true: Enables the dry run mode.
        # - false: Disables the dry run mode. This is the default value.
        # 
        # The dry run mode is used to test API calls, verify whether you have the required permissions on the resources, and check whether the request parameters are correctly configured. When the dry run mode is enabled, KMS always returns a failure and provides the cause of the failure. The causes include:
        # 
        # - DryRunOperationError: The request would succeed if the DryRun parameter is not configured.
        # - ValidationError: The specified parameters in the request are invalid.
        # - AccessDeniedError: You are not authorized to perform the operation on the KMS resources.
        self.dry_run = dry_run
        # The globally unique identifier of the customer master key (CMK).
        # 
        # > You can also set this parameter to the alias that is bound to the CMK. For more information, see [Usage notes for aliases](https://help.aliyun.com/document_detail/68522.html).
        # 
        # This parameter is required.
        self.key_id = key_id
        # The key version ID, which is the globally unique identifier of the key version.
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

        if self.digest is not None:
            result['Digest'] = self.digest

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

        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')

        return self

