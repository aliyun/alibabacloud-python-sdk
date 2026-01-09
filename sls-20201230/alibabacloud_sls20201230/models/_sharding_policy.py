# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ShardingPolicy(DaraModel):
    def __init__(
        self,
        query_active_time: int = None,
        shard_group: main_models.ShardingPolicyShardGroup = None,
        shard_hash: main_models.ShardingPolicyShardHash = None,
    ):
        self.query_active_time = query_active_time
        self.shard_group = shard_group
        # This parameter is required.
        self.shard_hash = shard_hash

    def validate(self):
        if self.shard_group:
            self.shard_group.validate()
        if self.shard_hash:
            self.shard_hash.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_active_time is not None:
            result['queryActiveTime'] = self.query_active_time

        if self.shard_group is not None:
            result['shardGroup'] = self.shard_group.to_map()

        if self.shard_hash is not None:
            result['shardHash'] = self.shard_hash.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryActiveTime') is not None:
            self.query_active_time = m.get('queryActiveTime')

        if m.get('shardGroup') is not None:
            temp_model = main_models.ShardingPolicyShardGroup()
            self.shard_group = temp_model.from_map(m.get('shardGroup'))

        if m.get('shardHash') is not None:
            temp_model = main_models.ShardingPolicyShardHash()
            self.shard_hash = temp_model.from_map(m.get('shardHash'))

        return self

class ShardingPolicyShardHash(DaraModel):
    def __init__(
        self,
        keys: List[str] = None,
        max_hash_count: int = None,
    ):
        # This parameter is required.
        self.keys = keys
        # This parameter is required.
        self.max_hash_count = max_hash_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keys is not None:
            result['keys'] = self.keys

        if self.max_hash_count is not None:
            result['maxHashCount'] = self.max_hash_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keys') is not None:
            self.keys = m.get('keys')

        if m.get('maxHashCount') is not None:
            self.max_hash_count = m.get('maxHashCount')

        return self

class ShardingPolicyShardGroup(DaraModel):
    def __init__(
        self,
        group_count: int = None,
        keys: List[str] = None,
    ):
        # This parameter is required.
        self.group_count = group_count
        # This parameter is required.
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_count is not None:
            result['groupCount'] = self.group_count

        if self.keys is not None:
            result['keys'] = self.keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupCount') is not None:
            self.group_count = m.get('groupCount')

        if m.get('keys') is not None:
            self.keys = m.get('keys')

        return self

