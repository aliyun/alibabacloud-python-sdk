# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeRefundPriceResponseBody(DaraModel):
    def __init__(
        self,
        price_info: main_models.DescribeRefundPriceResponseBodyPriceInfo = None,
        request_id: str = None,
    ):
        # The price details.
        self.price_info = price_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = main_models.DescribeRefundPriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m.get('PriceInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRefundPriceResponseBodyPriceInfo(DaraModel):
    def __init__(
        self,
        currency: str = None,
        refund_fee: float = None,
    ):
        # The unit of currency (USD).
        self.currency = currency
        # The amount of the refund.
        self.refund_fee = refund_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.refund_fee is not None:
            result['RefundFee'] = self.refund_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('RefundFee') is not None:
            self.refund_fee = m.get('RefundFee')

        return self

