# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SplitShardRequest(DaraModel):
    def __init__(
        self,
        key: str = None,
        shard_count: int = None,
    ):
        # The position where the shard is split.
        self.key = key
        # The number of new shards that are generated after splitting.
        self.shard_count = shard_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.shard_count is not None:
            result['shardCount'] = self.shard_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')

        return self

