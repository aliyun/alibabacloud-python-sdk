# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExcpetionCountResponseBody(DaraModel):
    def __init__(
        self,
        exception_ip_count: int = None,
        expire_time_count: int = None,
        request_id: str = None,
    ):
        # The number of assets that are in an abnormal state.
        self.exception_ip_count = exception_ip_count
        # The number of Anti-DDoS Origin instances that are about to expire.
        self.expire_time_count = expire_time_count
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exception_ip_count is not None:
            result['ExceptionIpCount'] = self.exception_ip_count

        if self.expire_time_count is not None:
            result['ExpireTimeCount'] = self.expire_time_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionIpCount') is not None:
            self.exception_ip_count = m.get('ExceptionIpCount')

        if m.get('ExpireTimeCount') is not None:
            self.expire_time_count = m.get('ExpireTimeCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

