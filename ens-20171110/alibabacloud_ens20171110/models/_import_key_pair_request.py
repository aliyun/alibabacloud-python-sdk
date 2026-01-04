# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportKeyPairRequest(DaraModel):
    def __init__(
        self,
        key_pair_name: str = None,
        public_key_body: str = None,
    ):
        # The name of the key pair. The name must conform to the following naming conventions:
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   The name must start with a letter but cannot start with `http://` or `https://`.
        # *   The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        # 
        # You can specify the name of only one key pair.
        # 
        # This parameter is required.
        self.key_pair_name = key_pair_name
        # The public key of the key pair. You can specify only one public key.
        # 
        # This parameter is required.
        self.public_key_body = public_key_body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.public_key_body is not None:
            result['PublicKeyBody'] = self.public_key_body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('PublicKeyBody') is not None:
            self.public_key_body = m.get('PublicKeyBody')

        return self

