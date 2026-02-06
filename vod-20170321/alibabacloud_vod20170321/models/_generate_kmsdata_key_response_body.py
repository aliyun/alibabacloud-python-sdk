# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateKMSDataKeyResponseBody(DaraModel):
    def __init__(
        self,
        ciphertext_blob: str = None,
        key_id: str = None,
        plaintext: str = None,
        request_id: str = None,
    ):
        # The ciphertext of the encrypted data key. This is used as CipherText when you create a transcoding job.
        self.ciphertext_blob = ciphertext_blob
        # The ID of the customer master key (CMK). The ID must be globally unique.
        self.key_id = key_id
        # The Base64-encoded plaintext of the data key.
        self.plaintext = plaintext
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

