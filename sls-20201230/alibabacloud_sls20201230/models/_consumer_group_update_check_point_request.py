# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConsumerGroupUpdateCheckPointRequest(DaraModel):
    def __init__(
        self,
        checkpoint: str = None,
        shard: int = None,
        consumer: str = None,
        force_success: bool = None,
    ):
        # The value of the checkpoint.
        # 
        # This parameter is required.
        self.checkpoint = checkpoint
        # The ID of the shard.
        # 
        # This parameter is required.
        self.shard = shard
        # The consumer.
        # 
        # This parameter is required.
        self.consumer = consumer
        # Specifies whether to enable forceful updates. Valid values:
        # 
        # *   true
        # *   false
        self.force_success = force_success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint

        if self.shard is not None:
            result['shard'] = self.shard

        if self.consumer is not None:
            result['consumer'] = self.consumer

        if self.force_success is not None:
            result['forceSuccess'] = self.force_success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkpoint') is not None:
            self.checkpoint = m.get('checkpoint')

        if m.get('shard') is not None:
            self.shard = m.get('shard')

        if m.get('consumer') is not None:
            self.consumer = m.get('consumer')

        if m.get('forceSuccess') is not None:
            self.force_success = m.get('forceSuccess')

        return self

