# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAutoCcListCountResponseBody(DaraModel):
    def __init__(
        self,
        black_count: int = None,
        request_id: str = None,
        white_count: int = None,
    ):
        # The total number of IP addresses in the blacklist.
        self.black_count = black_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of IP addresses in the whitelist.
        self.white_count = white_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_count is not None:
            result['BlackCount'] = self.black_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.white_count is not None:
            result['WhiteCount'] = self.white_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackCount') is not None:
            self.black_count = m.get('BlackCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WhiteCount') is not None:
            self.white_count = m.get('WhiteCount')

        return self

