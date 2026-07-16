# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DecryptResponseBody(DaraModel):
    def __init__(
        self,
        ciphertext_for_recipient: str = None,
        key_id: str = None,
        key_version_id: str = None,
        plaintext: str = None,
        request_id: str = None,
    ):
        self.ciphertext_for_recipient = ciphertext_for_recipient
        # The ID of the master key that is used to decrypt the ciphertext.<br> The globally unique identifier of the master key.<br>
        self.key_id = key_id
        # The ID of the key version that is used to decrypt the ciphertext. This key version is a version of the master key.
        self.key_version_id = key_version_id
        # The decrypted plaintext.
        self.plaintext = plaintext
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ciphertext_for_recipient is not None:
            result['CiphertextForRecipient'] = self.ciphertext_for_recipient

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id

        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphertextForRecipient') is not None:
            self.ciphertext_for_recipient = m.get('CiphertextForRecipient')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')

        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

