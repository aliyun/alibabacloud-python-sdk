# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKMSEncryptionRequest(DaraModel):
    def __init__(
        self,
        disable_encryption: bool = None,
        kms_key_id: str = None,
    ):
        self.disable_encryption = disable_encryption
        self.kms_key_id = kms_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable_encryption is not None:
            result['disable_encryption'] = self.disable_encryption

        if self.kms_key_id is not None:
            result['kms_key_id'] = self.kms_key_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disable_encryption') is not None:
            self.disable_encryption = m.get('disable_encryption')

        if m.get('kms_key_id') is not None:
            self.kms_key_id = m.get('kms_key_id')

        return self

