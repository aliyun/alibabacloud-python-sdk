# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNatFirewallQuotaResponseBody(DaraModel):
    def __init__(
        self,
        exception_count: int = None,
        request_id: str = None,
        total_count: int = None,
        unprotected_count: int = None,
        used_count: int = None,
    ):
        self.exception_count = exception_count
        self.request_id = request_id
        self.total_count = total_count
        self.unprotected_count = unprotected_count
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exception_count is not None:
            result['ExceptionCount'] = self.exception_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.unprotected_count is not None:
            result['UnprotectedCount'] = self.unprotected_count

        if self.used_count is not None:
            result['UsedCount'] = self.used_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionCount') is not None:
            self.exception_count = m.get('ExceptionCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UnprotectedCount') is not None:
            self.unprotected_count = m.get('UnprotectedCount')

        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')

        return self

