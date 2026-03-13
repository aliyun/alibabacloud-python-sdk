# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotelOrderPayRequest(DaraModel):
    def __init__(
        self,
        btrip_order_id: int = None,
        btrip_user_id: str = None,
        company_pay_fee: int = None,
        person_pay_fee: int = None,
        third_pay_account: str = None,
        third_trade_no: str = None,
        total_price: int = None,
    ):
        # 供应商订单号（取自创单返回的订单号）
        # 
        # This parameter is required.
        self.btrip_order_id = btrip_order_id
        # This parameter is required.
        self.btrip_user_id = btrip_user_id
        # This parameter is required.
        self.company_pay_fee = company_pay_fee
        # This parameter is required.
        self.person_pay_fee = person_pay_fee
        self.third_pay_account = third_pay_account
        self.third_trade_no = third_trade_no
        # This parameter is required.
        self.total_price = total_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_order_id is not None:
            result['btrip_order_id'] = self.btrip_order_id

        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.company_pay_fee is not None:
            result['company_pay_fee'] = self.company_pay_fee

        if self.person_pay_fee is not None:
            result['person_pay_fee'] = self.person_pay_fee

        if self.third_pay_account is not None:
            result['third_pay_account'] = self.third_pay_account

        if self.third_trade_no is not None:
            result['third_trade_no'] = self.third_trade_no

        if self.total_price is not None:
            result['total_price'] = self.total_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_order_id') is not None:
            self.btrip_order_id = m.get('btrip_order_id')

        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('company_pay_fee') is not None:
            self.company_pay_fee = m.get('company_pay_fee')

        if m.get('person_pay_fee') is not None:
            self.person_pay_fee = m.get('person_pay_fee')

        if m.get('third_pay_account') is not None:
            self.third_pay_account = m.get('third_pay_account')

        if m.get('third_trade_no') is not None:
            self.third_trade_no = m.get('third_trade_no')

        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')

        return self

