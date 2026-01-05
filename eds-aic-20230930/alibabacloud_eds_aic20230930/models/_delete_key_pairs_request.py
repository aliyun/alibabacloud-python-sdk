# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteKeyPairsRequest(DaraModel):
    def __init__(
        self,
        key_pair_ids: List[str] = None,
    ):
        # The IDs of the ADB key pairs.
        self.key_pair_ids = key_pair_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_pair_ids is not None:
            result['KeyPairIds'] = self.key_pair_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairIds') is not None:
            self.key_pair_ids = m.get('KeyPairIds')

        return self

