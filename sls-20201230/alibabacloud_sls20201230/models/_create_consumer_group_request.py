# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConsumerGroupRequest(DaraModel):
    def __init__(
        self,
        consumer_group: str = None,
        order: bool = None,
        timeout: int = None,
    ):
        # The name of the consumer group. The name must be unique in a project.
        # 
        # This parameter is required.
        self.consumer_group = consumer_group
        # Specifies whether to consume data in sequence. Valid values:
        # 
        # *   true
        # 
        #     *   In a shard, data is consumed in ascending order based on the value of the \\*\\*__tag__:__receive_time__\\*\\* field.
        #     *   If a shard is split, data in the original shard is consumed first. Then, data in the new shards is consumed at the same time.
        #     *   If shards are merged, data in the original shards is consumed first. Then, data in the new shard is consumed.
        # 
        # *   false Data in all shards is consumed at the same time. If a new shard is generated after a shard is split or after shards are merged, data in the new shard is immediately consumed.
        # 
        # This parameter is required.
        self.order = order
        # The timeout period. If the server does not receive heartbeats from a consumer within the timeout period, the server deletes the consumer. Unit: seconds.
        # 
        # This parameter is required.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group is not None:
            result['consumerGroup'] = self.consumer_group

        if self.order is not None:
            result['order'] = self.order

        if self.timeout is not None:
            result['timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroup') is not None:
            self.consumer_group = m.get('consumerGroup')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        return self

