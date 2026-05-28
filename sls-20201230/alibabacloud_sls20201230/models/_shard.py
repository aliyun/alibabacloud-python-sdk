# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Shard(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        exclusive_end_key: str = None,
        inclusive_begin_key: str = None,
        shard_id: int = None,
        status: str = None,
    ):
        # The time at which the shard was created. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The end of the MD5 hash range.
        self.exclusive_end_key = exclusive_end_key
        # The start of the MD5 hash range. The value is included in the MD5 hash range of the shard.
        self.inclusive_begin_key = inclusive_begin_key
        # shard id
        self.shard_id = shard_id
        # The status of the shard. After you create a shard, the shard enters the readwrite state. If you split a shard or merge shards, the shard status changes to readonly. The newly generated shards are in the readwrite state. The status of a shard does not affect the performance of read operations that are performed on the shard. Data can be written to the shards that are in the readwrite state, but data cannot be written to the shards that are in the readonly state. Valid values:
        # 
        # *   readwrite
        # *   readonly
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.exclusive_end_key is not None:
            result['exclusiveEndKey'] = self.exclusive_end_key

        if self.inclusive_begin_key is not None:
            result['inclusiveBeginKey'] = self.inclusive_begin_key

        if self.shard_id is not None:
            result['shardID'] = self.shard_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('exclusiveEndKey') is not None:
            self.exclusive_end_key = m.get('exclusiveEndKey')

        if m.get('inclusiveBeginKey') is not None:
            self.inclusive_begin_key = m.get('inclusiveBeginKey')

        if m.get('shardID') is not None:
            self.shard_id = m.get('shardID')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

