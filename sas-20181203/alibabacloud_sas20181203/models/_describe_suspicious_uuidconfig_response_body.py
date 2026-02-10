# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSuspiciousUUIDConfigResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        request_id: str = None,
        uuidlist: List[str] = None,
    ):
        # The total number of servers on which proactive defense of the specified type takes effect.
        self.count = count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The UUIDs of servers on which proactive defense of the specified type takes effect.
        self.uuidlist = uuidlist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.uuidlist is not None:
            result['UUIDList'] = self.uuidlist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UUIDList') is not None:
            self.uuidlist = m.get('UUIDList')

        return self

