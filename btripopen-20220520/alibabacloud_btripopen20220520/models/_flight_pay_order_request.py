# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class FlightPayOrderRequest(DaraModel):
    def __init__(
        self,
        corp_pay_price: int = None,
        dis_order_id: str = None,
        extra: Dict[str, str] = None,
        personal_pay_price: int = None,
        total_pay_price: int = None,
    ):
        # This parameter is required.
        self.corp_pay_price = corp_pay_price
        # This parameter is required.
        self.dis_order_id = dis_order_id
        self.extra = extra
        # This parameter is required.
        self.personal_pay_price = personal_pay_price
        # This parameter is required.
        self.total_pay_price = total_pay_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_pay_price is not None:
            result['corp_pay_price'] = self.corp_pay_price

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.extra is not None:
            result['extra'] = self.extra

        if self.personal_pay_price is not None:
            result['personal_pay_price'] = self.personal_pay_price

        if self.total_pay_price is not None:
            result['total_pay_price'] = self.total_pay_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_pay_price') is not None:
            self.corp_pay_price = m.get('corp_pay_price')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('personal_pay_price') is not None:
            self.personal_pay_price = m.get('personal_pay_price')

        if m.get('total_pay_price') is not None:
            self.total_pay_price = m.get('total_pay_price')

        return self

