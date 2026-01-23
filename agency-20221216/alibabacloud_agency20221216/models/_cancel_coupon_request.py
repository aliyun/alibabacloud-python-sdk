# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelCouponRequest(DaraModel):
    def __init__(
        self,
        coupon_id: int = None,
    ):
        # This parameter is required.
        self.coupon_id = coupon_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')

        return self

