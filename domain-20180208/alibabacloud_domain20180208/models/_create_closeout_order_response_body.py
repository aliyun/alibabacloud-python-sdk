# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class CreateCloseoutOrderResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.CreateCloseoutOrderResponseBodyModule = None,
        request_id: str = None,
    ):
        self.module = module
        self.request_id = request_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            temp_model = main_models.CreateCloseoutOrderResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateCloseoutOrderResponseBodyModule(DaraModel):
    def __init__(
        self,
        biz_ids: Dict[str, str] = None,
        buyer_block_trade: List[str] = None,
        domain_block_trade: List[str] = None,
        domain_name: str = None,
        domain_trade_risk_warn: List[str] = None,
        extend: Dict[str, str] = None,
        ignored_domains: List[Dict[str, str]] = None,
        need_pay: bool = None,
        order_no: str = None,
        order_sum_money: float = None,
        out_order_no: str = None,
        pay_money: float = None,
        pay_url: str = None,
        real_name_template: List[int] = None,
        request_id: str = None,
    ):
        self.biz_ids = biz_ids
        self.buyer_block_trade = buyer_block_trade
        self.domain_block_trade = domain_block_trade
        self.domain_name = domain_name
        self.domain_trade_risk_warn = domain_trade_risk_warn
        self.extend = extend
        self.ignored_domains = ignored_domains
        self.need_pay = need_pay
        self.order_no = order_no
        self.order_sum_money = order_sum_money
        self.out_order_no = out_order_no
        self.pay_money = pay_money
        self.pay_url = pay_url
        self.real_name_template = real_name_template
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_ids is not None:
            result['BizIds'] = self.biz_ids

        if self.buyer_block_trade is not None:
            result['BuyerBlockTrade'] = self.buyer_block_trade

        if self.domain_block_trade is not None:
            result['DomainBlockTrade'] = self.domain_block_trade

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_trade_risk_warn is not None:
            result['DomainTradeRiskWarn'] = self.domain_trade_risk_warn

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.ignored_domains is not None:
            result['IgnoredDomains'] = self.ignored_domains

        if self.need_pay is not None:
            result['NeedPay'] = self.need_pay

        if self.order_no is not None:
            result['OrderNo'] = self.order_no

        if self.order_sum_money is not None:
            result['OrderSumMoney'] = self.order_sum_money

        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no

        if self.pay_money is not None:
            result['PayMoney'] = self.pay_money

        if self.pay_url is not None:
            result['PayUrl'] = self.pay_url

        if self.real_name_template is not None:
            result['RealNameTemplate'] = self.real_name_template

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizIds') is not None:
            self.biz_ids = m.get('BizIds')

        if m.get('BuyerBlockTrade') is not None:
            self.buyer_block_trade = m.get('BuyerBlockTrade')

        if m.get('DomainBlockTrade') is not None:
            self.domain_block_trade = m.get('DomainBlockTrade')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainTradeRiskWarn') is not None:
            self.domain_trade_risk_warn = m.get('DomainTradeRiskWarn')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('IgnoredDomains') is not None:
            self.ignored_domains = m.get('IgnoredDomains')

        if m.get('NeedPay') is not None:
            self.need_pay = m.get('NeedPay')

        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')

        if m.get('OrderSumMoney') is not None:
            self.order_sum_money = m.get('OrderSumMoney')

        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')

        if m.get('PayMoney') is not None:
            self.pay_money = m.get('PayMoney')

        if m.get('PayUrl') is not None:
            self.pay_url = m.get('PayUrl')

        if m.get('RealNameTemplate') is not None:
            self.real_name_template = m.get('RealNameTemplate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

