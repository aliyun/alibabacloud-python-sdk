# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyCatalogKmsRequest(DaraModel):
    def __init__(
        self,
        kms_key_id: str = None,
    ):
        # The ID of the KMS customer master key (CMK) to be validated. The server uses this key to perform an SSE-KMS write probe.
        # 
        # This parameter is required.
        self.kms_key_id = kms_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kms_key_id is not None:
            result['kmsKeyId'] = self.kms_key_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kmsKeyId') is not None:
            self.kms_key_id = m.get('kmsKeyId')

        return self

