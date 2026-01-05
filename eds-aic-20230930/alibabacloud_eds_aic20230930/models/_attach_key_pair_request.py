# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AttachKeyPairRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        key_pair_id: str = None,
    ):
        # The IDs of the cloud phone instances. You can specify a maximum of 50 cloud phone instances.
        self.instance_ids = instance_ids
        # The ID of the ADB key pair.
        # 
        # This parameter is required.
        self.key_pair_id = key_pair_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        return self

