# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterShardNumberResponseBody(DaraModel):
    def __init__(
        self,
        available_shard_number_list: List[main_models.DescribeDBClusterShardNumberResponseBodyAvailableShardNumberList] = None,
        available_shard_numbers: List[int] = None,
        request_id: str = None,
        shard_number: int = None,
    ):
        # The supported numbers of shards, including the number of current shards and the number of desired shards.
        self.available_shard_number_list = available_shard_number_list
        # The number of desired shards, excluding the number of current shards.
        self.available_shard_numbers = available_shard_numbers
        # The request ID.
        self.request_id = request_id
        # The number of shards that you want to change during the data migration.
        self.shard_number = shard_number

    def validate(self):
        if self.available_shard_number_list:
            for v1 in self.available_shard_number_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableShardNumberList'] = []
        if self.available_shard_number_list is not None:
            for k1 in self.available_shard_number_list:
                result['AvailableShardNumberList'].append(k1.to_map() if k1 else None)

        if self.available_shard_numbers is not None:
            result['AvailableShardNumbers'] = self.available_shard_numbers

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.shard_number is not None:
            result['ShardNumber'] = self.shard_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_shard_number_list = []
        if m.get('AvailableShardNumberList') is not None:
            for k1 in m.get('AvailableShardNumberList'):
                temp_model = main_models.DescribeDBClusterShardNumberResponseBodyAvailableShardNumberList()
                self.available_shard_number_list.append(temp_model.from_map(k1))

        if m.get('AvailableShardNumbers') is not None:
            self.available_shard_numbers = m.get('AvailableShardNumbers')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShardNumber') is not None:
            self.shard_number = m.get('ShardNumber')

        return self

class DescribeDBClusterShardNumberResponseBodyAvailableShardNumberList(DaraModel):
    def __init__(
        self,
        shard_number: int = None,
    ):
        # The number of shards.
        self.shard_number = shard_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.shard_number is not None:
            result['ShardNumber'] = self.shard_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShardNumber') is not None:
            self.shard_number = m.get('ShardNumber')

        return self

