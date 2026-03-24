# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserCertificateExpireCountResponseBody(DaraModel):
    def __init__(
        self,
        expire_within_30days_count: int = None,
        expired_count: int = None,
        request_id: str = None,
    ):
        # The number of domain names whose SSL certificates are about to expires within 30 days.
        self.expire_within_30days_count = expire_within_30days_count
        # The number of domain names whose SSL certificates have already expired.
        self.expired_count = expired_count
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_within_30days_count is not None:
            result['ExpireWithin30DaysCount'] = self.expire_within_30days_count

        if self.expired_count is not None:
            result['ExpiredCount'] = self.expired_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireWithin30DaysCount') is not None:
            self.expire_within_30days_count = m.get('ExpireWithin30DaysCount')

        if m.get('ExpiredCount') is not None:
            self.expired_count = m.get('ExpiredCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

