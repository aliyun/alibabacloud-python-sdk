# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsymmetricVerifyRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        digest: str = None,
        dry_run: str = None,
        key_id: str = None,
        key_version_id: str = None,
        value: str = None,
    ):
        # The signature algorithm.
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The digest that is generated using the hash algorithm that corresponds to the value of **Algorithm** to hash the original message.
        # 
        # > The value is Base64-encoded.
        # 
        # This parameter is required.
        self.digest = digest
        # Specifies whether to perform a dry run.
        # 
        # - true: performs a dry run.
        # 
        # - false (default): does not perform a dry run.
        # 
        # A dry run is used to test API calls and verify whether you have the permissions to access the specified resources and whether the request parameters are valid. If you perform a dry run, KMS always returns a failure response that indicates the cause of the failure. The following failure causes are included:
        # 
        # - DryRunOperationError: The request would have succeeded if the DryRun parameter is not specified.
        # 
        # - ValidationError: The specified parameters in the request are invalid.
        # 
        # - AccessDeniedError: You are not authorized to perform this operation on the KMS resource.
        self.dry_run = dry_run
        # The globally unique identifier (GUID) of the customer master key (CMK).
        # 
        # > You can also specify the alias that is bound to the CMK. For more information, see [Overview of aliases](https://help.aliyun.com/document_detail/68522.html).
        # 
        # This parameter is required.
        self.key_id = key_id
        # The ID of the key version. The ID must be the GUID of the key version.
        # 
        # This parameter is required.
        self.key_version_id = key_version_id
        # The signature value to be verified.
        # 
        # > The value is Base64-encoded.
        # 
        # This parameter is required.
        self.value = value

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

        if self.value is not None:
            result['Value'] = self.value

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

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

