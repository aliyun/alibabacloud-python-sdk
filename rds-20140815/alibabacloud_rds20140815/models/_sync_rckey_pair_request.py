# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncRCKeyPairRequest(DaraModel):
    def __init__(
        self,
        key_pair_name: str = None,
        region_id: str = None,
        sync_mode: bool = None,
    ):
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The region ID.
        self.region_id = region_id
        self.sync_mode = sync_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')

        return self

