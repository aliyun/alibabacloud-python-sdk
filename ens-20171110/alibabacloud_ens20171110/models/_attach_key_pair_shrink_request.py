# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachKeyPairShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_ids_shrink: str = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
    ):
        # The instance IDs.
        # 
        # This parameter is required.
        self.instance_ids_shrink = instance_ids_shrink
        # The key pair ID.
        self.key_pair_id = key_pair_id
        # The name of the SSH key pair.
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        return self

