# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetEncryptionConfigRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        kms_key_id: str = None,
        kms_region_id: str = None,
    ):
        # The idempotence token. Format: [0-9a-zA-Z-]{1,64}. Use a UUID.
        self.client_token = client_token
        # The ID of the KMS key used for encryption.
        self.kms_key_id = kms_key_id
        # The region ID of the KMS key.
        self.kms_region_id = kms_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.kms_key_id is not None:
            result['kmsKeyId'] = self.kms_key_id

        if self.kms_region_id is not None:
            result['kmsRegionId'] = self.kms_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('kmsKeyId') is not None:
            self.kms_key_id = m.get('kmsKeyId')

        if m.get('kmsRegionId') is not None:
            self.kms_region_id = m.get('kmsRegionId')

        return self

