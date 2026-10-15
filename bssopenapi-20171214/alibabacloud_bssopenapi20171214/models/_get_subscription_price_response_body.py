# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class GetSubscriptionPriceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSubscriptionPriceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The product price information.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetSubscriptionPriceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSubscriptionPriceResponseBodyData(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        module_details: main_models.GetSubscriptionPriceResponseBodyDataModuleDetails = None,
        original_price: float = None,
        payment_scheme: main_models.GetSubscriptionPriceResponseBodyDataPaymentScheme = None,
        promotion_details: main_models.GetSubscriptionPriceResponseBodyDataPromotionDetails = None,
        quantity: int = None,
        trade_price: float = None,
    ):
        # The currency. Valid values:
        # - CNY: Chinese yuan.
        # - USD: US dollar.
        # - JPY: Japanese yen.
        self.currency = currency
        # The discount amount.
        self.discount_price = discount_price
        self.module_details = module_details
        # The original price.
        self.original_price = original_price
        # The parameters for fixed-fee installments.
        self.payment_scheme = payment_scheme
        self.promotion_details = promotion_details
        # The quantity.
        self.quantity = quantity
        # The discounted price.
        self.trade_price = trade_price

    def validate(self):
        if self.module_details:
            self.module_details.validate()
        if self.payment_scheme:
            self.payment_scheme.validate()
        if self.promotion_details:
            self.promotion_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.module_details is not None:
            result['ModuleDetails'] = self.module_details.to_map()

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.payment_scheme is not None:
            result['PaymentScheme'] = self.payment_scheme.to_map()

        if self.promotion_details is not None:
            result['PromotionDetails'] = self.promotion_details.to_map()

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('ModuleDetails') is not None:
            temp_model = main_models.GetSubscriptionPriceResponseBodyDataModuleDetails()
            self.module_details = temp_model.from_map(m.get('ModuleDetails'))

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('PaymentScheme') is not None:
            temp_model = main_models.GetSubscriptionPriceResponseBodyDataPaymentScheme()
            self.payment_scheme = temp_model.from_map(m.get('PaymentScheme'))

        if m.get('PromotionDetails') is not None:
            temp_model = main_models.GetSubscriptionPriceResponseBodyDataPromotionDetails()
            self.promotion_details = temp_model.from_map(m.get('PromotionDetails'))

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class GetSubscriptionPriceResponseBodyDataPromotionDetails(DaraModel):
    def __init__(
        self,
        promotion_detail: List[main_models.GetSubscriptionPriceResponseBodyDataPromotionDetailsPromotionDetail] = None,
    ):
        self.promotion_detail = promotion_detail

    def validate(self):
        if self.promotion_detail:
            for v1 in self.promotion_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PromotionDetail'] = []
        if self.promotion_detail is not None:
            for k1 in self.promotion_detail:
                result['PromotionDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.promotion_detail = []
        if m.get('PromotionDetail') is not None:
            for k1 in m.get('PromotionDetail'):
                temp_model = main_models.GetSubscriptionPriceResponseBodyDataPromotionDetailsPromotionDetail()
                self.promotion_detail.append(temp_model.from_map(k1))

        return self

class GetSubscriptionPriceResponseBodyDataPromotionDetailsPromotionDetail(DaraModel):
    def __init__(
        self,
        promotion_desc: str = None,
        promotion_id: int = None,
        promotion_name: str = None,
    ):
        self.promotion_desc = promotion_desc
        self.promotion_id = promotion_id
        self.promotion_name = promotion_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        return self

class GetSubscriptionPriceResponseBodyDataPaymentScheme(DaraModel):
    def __init__(
        self,
        order_down_payment_fee: str = None,
        order_down_payment_settle_fee: str = None,
        order_total_fee: str = None,
        order_total_settle_fee: str = None,
        payment_type: str = None,
    ):
        # The payable amount for the order, in cents.
        self.order_down_payment_fee = order_down_payment_fee
        # The payable amount in the settlement currency for the order, in cents.
        self.order_down_payment_settle_fee = order_down_payment_settle_fee
        # The total payable amount for the order, including the prepayment and installment parts, in cents.
        self.order_total_fee = order_total_fee
        # The total payable amount in the settlement currency for the order, including the prepayment and installment parts, in cents.
        self.order_total_settle_fee = order_total_settle_fee
        # The fixed-fee installment type. Valid values:
        # - PAYMENT_NORMAL: non-fixed-fee installment products.
        # - PAYMENT_PHASED: fixed-fee installment products.
        self.payment_type = payment_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_down_payment_fee is not None:
            result['OrderDownPaymentFee'] = self.order_down_payment_fee

        if self.order_down_payment_settle_fee is not None:
            result['OrderDownPaymentSettleFee'] = self.order_down_payment_settle_fee

        if self.order_total_fee is not None:
            result['OrderTotalFee'] = self.order_total_fee

        if self.order_total_settle_fee is not None:
            result['OrderTotalSettleFee'] = self.order_total_settle_fee

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderDownPaymentFee') is not None:
            self.order_down_payment_fee = m.get('OrderDownPaymentFee')

        if m.get('OrderDownPaymentSettleFee') is not None:
            self.order_down_payment_settle_fee = m.get('OrderDownPaymentSettleFee')

        if m.get('OrderTotalFee') is not None:
            self.order_total_fee = m.get('OrderTotalFee')

        if m.get('OrderTotalSettleFee') is not None:
            self.order_total_settle_fee = m.get('OrderTotalSettleFee')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        return self

class GetSubscriptionPriceResponseBodyDataModuleDetails(DaraModel):
    def __init__(
        self,
        module_detail: List[main_models.GetSubscriptionPriceResponseBodyDataModuleDetailsModuleDetail] = None,
    ):
        self.module_detail = module_detail

    def validate(self):
        if self.module_detail:
            for v1 in self.module_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModuleDetail'] = []
        if self.module_detail is not None:
            for k1 in self.module_detail:
                result['ModuleDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_detail = []
        if m.get('ModuleDetail') is not None:
            for k1 in m.get('ModuleDetail'):
                temp_model = main_models.GetSubscriptionPriceResponseBodyDataModuleDetailsModuleDetail()
                self.module_detail.append(temp_model.from_map(k1))

        return self

class GetSubscriptionPriceResponseBodyDataModuleDetailsModuleDetail(DaraModel):
    def __init__(
        self,
        cost_after_discount: float = None,
        invoice_discount: float = None,
        module_code: str = None,
        original_cost: float = None,
        unit_price: float = None,
    ):
        self.cost_after_discount = cost_after_discount
        self.invoice_discount = invoice_discount
        self.module_code = module_code
        self.original_cost = original_cost
        self.unit_price = unit_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_after_discount is not None:
            result['CostAfterDiscount'] = self.cost_after_discount

        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.original_cost is not None:
            result['OriginalCost'] = self.original_cost

        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostAfterDiscount') is not None:
            self.cost_after_discount = m.get('CostAfterDiscount')

        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('OriginalCost') is not None:
            self.original_cost = m.get('OriginalCost')

        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')

        return self

