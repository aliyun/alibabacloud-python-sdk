# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeStreamURLResponseBody(DaraModel):
    def __init__(
        self,
        expire_time: int = None,
        request_id: str = None,
        url: str = None,
    ):
        self.expire_time = expire_time
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

