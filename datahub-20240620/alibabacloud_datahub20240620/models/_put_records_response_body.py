# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutRecordsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        shard_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.shard_id = shard_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.shard_id is not None:
            result['ShardId'] = self.shard_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShardId') is not None:
            self.shard_id = m.get('ShardId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

