# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSubDomainRecordsResponseBody(DaraModel):
    def __init__(
        self,
        rr: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The hostname.
        self.rr = rr
        # The request ID.
        self.request_id = request_id
        # The total number of the DNS records to be deleted.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rr is not None:
            result['RR'] = self.rr

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RR') is not None:
            self.rr = m.get('RR')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

