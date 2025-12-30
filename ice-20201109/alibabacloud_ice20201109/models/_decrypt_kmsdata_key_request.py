# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DecryptKMSDataKeyRequest(DaraModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
    ):
        # The ciphertext that you want to decrypt.
        # 
        # This parameter is required.
        self.ciphertext_blob = ciphertext_blob

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')

        return self

