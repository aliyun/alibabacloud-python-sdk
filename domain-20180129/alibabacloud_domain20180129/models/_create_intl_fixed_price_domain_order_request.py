# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIntlFixedPriceDomainOrderRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        contact_id: int = None,
        domain: str = None,
        expected_price: int = None,
    ):
        self.auto_pay = auto_pay
        self.contact_id = contact_id
        self.domain = domain
        self.expected_price = expected_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.expected_price is not None:
            result['ExpectedPrice'] = self.expected_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ExpectedPrice') is not None:
            self.expected_price = m.get('ExpectedPrice')

        return self

