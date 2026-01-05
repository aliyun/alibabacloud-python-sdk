# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyKeyPairNameRequest(DaraModel):
    def __init__(
        self,
        key_pair_id: str = None,
        new_key_pair_name: str = None,
    ):
        # The ID of the ADB key pair.
        # 
        # This parameter is required.
        self.key_pair_id = key_pair_id
        # The name of the ADB key pair.
        # 
        # This parameter is required.
        self.new_key_pair_name = new_key_pair_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.new_key_pair_name is not None:
            result['NewKeyPairName'] = self.new_key_pair_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('NewKeyPairName') is not None:
            self.new_key_pair_name = m.get('NewKeyPairName')

        return self

