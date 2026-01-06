# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class GetModifyBEClusterInquiryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetModifyBEClusterInquiryResponseBodyData = None,
        request_id: str = None,
    ):
        # The information returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetModifyBEClusterInquiryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetModifyBEClusterInquiryResponseBodyData(DaraModel):
    def __init__(
        self,
        currency: str = None,
        optional_promotions: List[main_models.GetModifyBEClusterInquiryResponseBodyDataOptionalPromotions] = None,
        pricing_rules: Dict[str, str] = None,
        refund_amount: str = None,
        trade_amount: str = None,
    ):
        # The currency.
        self.currency = currency
        self.optional_promotions = optional_promotions
        self.pricing_rules = pricing_rules
        # The estimated refund amount when the subscription cluster of a subscription instance is changed to a pay-as-you-go cluster.
        self.refund_amount = refund_amount
        # The amount of money.
        self.trade_amount = trade_amount

    def validate(self):
        if self.optional_promotions:
            for v1 in self.optional_promotions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        result['OptionalPromotions'] = []
        if self.optional_promotions is not None:
            for k1 in self.optional_promotions:
                result['OptionalPromotions'].append(k1.to_map() if k1 else None)

        if self.pricing_rules is not None:
            result['PricingRules'] = self.pricing_rules

        if self.refund_amount is not None:
            result['RefundAmount'] = self.refund_amount

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        self.optional_promotions = []
        if m.get('OptionalPromotions') is not None:
            for k1 in m.get('OptionalPromotions'):
                temp_model = main_models.GetModifyBEClusterInquiryResponseBodyDataOptionalPromotions()
                self.optional_promotions.append(temp_model.from_map(k1))

        if m.get('PricingRules') is not None:
            self.pricing_rules = m.get('PricingRules')

        if m.get('RefundAmount') is not None:
            self.refund_amount = m.get('RefundAmount')

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

class GetModifyBEClusterInquiryResponseBodyDataOptionalPromotions(DaraModel):
    def __init__(
        self,
        can_prom_fee: str = None,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_name: str = None,
        promotion_option_no: str = None,
    ):
        self.can_prom_fee = can_prom_fee
        self.option_code = option_code
        self.promotion_desc = promotion_desc
        self.promotion_name = promotion_name
        self.promotion_option_no = promotion_option_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_prom_fee is not None:
            result['CanPromFee'] = self.can_prom_fee

        if self.option_code is not None:
            result['OptionCode'] = self.option_code

        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc

        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanPromFee') is not None:
            self.can_prom_fee = m.get('CanPromFee')

        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')

        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        return self

