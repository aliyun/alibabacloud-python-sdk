# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DistributionMaxRefundFee(DaraModel):
    def __init__(
        self,
        max_refund_fee: int = None,
        min_refund_fee: int = None,
    ):
        self.max_refund_fee = max_refund_fee
        self.min_refund_fee = min_refund_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_refund_fee is not None:
            result['maxRefundFee'] = self.max_refund_fee

        if self.min_refund_fee is not None:
            result['minRefundFee'] = self.min_refund_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxRefundFee') is not None:
            self.max_refund_fee = m.get('maxRefundFee')

        if m.get('minRefundFee') is not None:
            self.min_refund_fee = m.get('minRefundFee')

        return self

