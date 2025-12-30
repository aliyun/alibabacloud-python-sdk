# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDNSSLBStatusResponseBody(DaraModel):
    def __init__(
        self,
        open: bool = None,
        record_count: int = None,
        request_id: str = None,
    ):
        # Indicates whether weighted round-robin is enabled for the subdomain name.
        self.open = open
        # The number of A records that are matched.
        self.record_count = record_count
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open is not None:
            result['Open'] = self.open

        if self.record_count is not None:
            result['RecordCount'] = self.record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Open') is not None:
            self.open = m.get('Open')

        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

