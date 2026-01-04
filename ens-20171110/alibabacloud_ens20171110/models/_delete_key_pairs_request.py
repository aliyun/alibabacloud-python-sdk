# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteKeyPairsRequest(DaraModel):
    def __init__(
        self,
        key_pair_id: str = None,
        key_pair_name: str = None,
    ):
        # The ID of the SSH key pair.
        self.key_pair_id = key_pair_id
        # The name of the key pair. The name must conform to the following naming conventions:
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   The name must start with a letter and cannot start with `http://` or `https://`.
        # *   The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        # 
        # Before you delete a key pair, you can call the DescribeKeyPairs operation to query existing key pairs.
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        return self

