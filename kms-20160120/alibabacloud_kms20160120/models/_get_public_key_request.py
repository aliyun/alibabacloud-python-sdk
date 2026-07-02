# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPublicKeyRequest(DaraModel):
    def __init__(
        self,
        dry_run: str = None,
        key_id: str = None,
        key_version_id: str = None,
    ):
        # Specifies whether to enable the DryRun mode.
        # 
        # - true: enables the DryRun mode.
        # 
        # - false (default): disables the DryRun mode.
        # 
        # The DryRun mode is used to test API calls, verify your permissions on resources, and check whether the parameters are valid. If you enable the DryRun mode, KMS always returns a failed response and a failure reason. The failure reasons include the following:
        # 
        # - DryRunOperationError: The request would have succeeded if the DryRun parameter is not specified.
        # 
        # - ValidationError: The specified parameters in the request are invalid.
        # 
        # - AccessDeniedError: You are not authorized to perform the operation on the KMS resource.
        self.dry_run = dry_run
        # The globally unique identifier of the customer master key (CMK). This parameter can also be an alias that is bound to the CMK. For more information, see [Use of aliases](https://help.aliyun.com/document_detail/68522.html).
        # 
        # This parameter is required.
        self.key_id = key_id
        # The globally unique identifier of the key version.
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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')

        return self

