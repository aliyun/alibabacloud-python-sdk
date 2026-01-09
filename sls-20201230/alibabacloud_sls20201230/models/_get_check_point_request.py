# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCheckPointRequest(DaraModel):
    def __init__(
        self,
        shard: int = None,
    ):
        # The shard ID.
        # 
        # *   If the specified shard does not exist, an empty list is returned.
        # *   If no shard ID is specified, the checkpoints of all shards are returned.
        self.shard = shard

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.shard is not None:
            result['shard'] = self.shard

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shard') is not None:
            self.shard = m.get('shard')

        return self

