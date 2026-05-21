# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class SubmitSlaCouponApplyResponseBody(DaraModel):
    def __init__(
        self,
        metadata: Any = None,
        request_id: str = None,
        sum_coupon: float = None,
        valid_end_time: str = None,
        valid_start_time: str = None,
    ):
        self.metadata = metadata
        self.request_id = request_id
        self.sum_coupon = sum_coupon
        self.valid_end_time = valid_end_time
        self.valid_start_time = valid_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sum_coupon is not None:
            result['SumCoupon'] = self.sum_coupon

        if self.valid_end_time is not None:
            result['ValidEndTime'] = self.valid_end_time

        if self.valid_start_time is not None:
            result['ValidStartTime'] = self.valid_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SumCoupon') is not None:
            self.sum_coupon = m.get('SumCoupon')

        if m.get('ValidEndTime') is not None:
            self.valid_end_time = m.get('ValidEndTime')

        if m.get('ValidStartTime') is not None:
            self.valid_start_time = m.get('ValidStartTime')

        return self

