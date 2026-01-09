# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConsumerGroupHeartBeatRequest(DaraModel):
    def __init__(
        self,
        body: List[int] = None,
        consumer: str = None,
    ):
        # The IDs of shards whose data is being consumed.
        # 
        # This parameter is required.
        self.body = body
        # The consumer.
        # 
        # This parameter is required.
        self.consumer = consumer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.consumer is not None:
            result['consumer'] = self.consumer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('consumer') is not None:
            self.consumer = m.get('consumer')

        return self

