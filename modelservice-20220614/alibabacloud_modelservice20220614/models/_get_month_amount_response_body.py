# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMonthAmountResponseBody(DaraModel):
    def __init__(
        self,
        background_amount: int = None,
        postpay_amount: int = None,
        prepay_amount: int = None,
        request_id: str = None,
        total_amount: int = None,
    ):
        self.background_amount = background_amount
        self.postpay_amount = postpay_amount
        self.prepay_amount = prepay_amount
        self.request_id = request_id
        self.total_amount = total_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_amount is not None:
            result['BackgroundAmount'] = self.background_amount

        if self.postpay_amount is not None:
            result['PostpayAmount'] = self.postpay_amount

        if self.prepay_amount is not None:
            result['PrepayAmount'] = self.prepay_amount

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundAmount') is not None:
            self.background_amount = m.get('BackgroundAmount')

        if m.get('PostpayAmount') is not None:
            self.postpay_amount = m.get('PostpayAmount')

        if m.get('PrepayAmount') is not None:
            self.prepay_amount = m.get('PrepayAmount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')

        return self

