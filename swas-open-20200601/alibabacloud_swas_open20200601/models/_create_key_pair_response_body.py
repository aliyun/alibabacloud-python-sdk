# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKeyPairResponseBody(DaraModel):
    def __init__(
        self,
        key_pair_name: str = None,
        private_key_body: str = None,
        request_id: str = None,
    ):
        # The name of the key pair. The name must be 2 to 64 characters in length, and can contain English letters and Chinese characters. It must start with a letter or a Chinese character and cannot start with http:// or https://. It can contain digits, colons (:), underscores (_), and hyphens (-).
        self.key_pair_name = key_pair_name
        # The private key of the key pair. The private key is in the PEM-encoded PKCS#8 format.
        self.private_key_body = private_key_body
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.private_key_body is not None:
            result['PrivateKeyBody'] = self.private_key_body

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('PrivateKeyBody') is not None:
            self.private_key_body = m.get('PrivateKeyBody')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

