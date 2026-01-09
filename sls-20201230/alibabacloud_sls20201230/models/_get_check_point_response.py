# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetCheckPointResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.GetCheckPointResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.GetCheckPointResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class GetCheckPointResponseBody(DaraModel):
    def __init__(
        self,
        shard: int = None,
        checkpoint: str = None,
        update_time: int = None,
        consumer: str = None,
    ):
        # The shard ID.
        self.shard = shard
        # The value of the checkpoint.
        self.checkpoint = checkpoint
        # The time when the checkpoint was last updated. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time
        # The consumer at the checkpoint.
        self.consumer = consumer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.shard is not None:
            result['shard'] = self.shard

        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.consumer is not None:
            result['consumer'] = self.consumer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shard') is not None:
            self.shard = m.get('shard')

        if m.get('checkpoint') is not None:
            self.checkpoint = m.get('checkpoint')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('consumer') is not None:
            self.consumer = m.get('consumer')

        return self

