# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWhiteListStrategyUuidCountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        uuid_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The number of the servers on which the application whitelist policy takes effect.
        self.uuid_count = uuid_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.uuid_count is not None:
            result['UuidCount'] = self.uuid_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UuidCount') is not None:
            self.uuid_count = m.get('UuidCount')

        return self

