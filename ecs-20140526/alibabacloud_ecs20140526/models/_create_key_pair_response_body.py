# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKeyPairResponseBody(DaraModel):
    def __init__(
        self,
        key_pair_finger_print: str = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
        private_key_body: str = None,
        request_id: str = None,
    ):
        # The fingerprint of the key pair. The message-digest algorithm 5 (MD5) is used based on the public key fingerprint format defined in RFC 4716. For more information, see [RFC 4716](https://tools.ietf.org/html/rfc4716).
        self.key_pair_finger_print = key_pair_finger_print
        # The ID of the key pair.
        self.key_pair_id = key_pair_id
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The private key of the key pair. The private key is encoded with PEM in the PKCS#8 format.
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
        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print

        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.private_key_body is not None:
            result['PrivateKeyBody'] = self.private_key_body

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')

        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('PrivateKeyBody') is not None:
            self.private_key_body = m.get('PrivateKeyBody')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

