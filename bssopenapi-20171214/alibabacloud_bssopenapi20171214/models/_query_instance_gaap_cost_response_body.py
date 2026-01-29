# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryInstanceGaapCostResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryInstanceGaapCostResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.QueryInstanceGaapCostResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryInstanceGaapCostResponseBodyData(DaraModel):
    def __init__(
        self,
        host_id: str = None,
        modules: main_models.QueryInstanceGaapCostResponseBodyDataModules = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.host_id = host_id
        self.modules = modules
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.modules:
            self.modules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.modules is not None:
            result['Modules'] = self.modules.to_map()

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('Modules') is not None:
            temp_model = main_models.QueryInstanceGaapCostResponseBodyDataModules()
            self.modules = temp_model.from_map(m.get('Modules'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryInstanceGaapCostResponseBodyDataModules(DaraModel):
    def __init__(
        self,
        module: List[main_models.QueryInstanceGaapCostResponseBodyDataModulesModule] = None,
    ):
        self.module = module

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['Module'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module = []
        if m.get('Module') is not None:
            for k1 in m.get('Module'):
                temp_model = main_models.QueryInstanceGaapCostResponseBodyDataModulesModule()
                self.module.append(temp_model.from_map(k1))

        return self

class QueryInstanceGaapCostResponseBodyDataModulesModule(DaraModel):
    def __init__(
        self,
        accounting_unit: str = None,
        bill_type: str = None,
        billing_cycle: str = None,
        currency: str = None,
        deducted_by_cash_coupons: str = None,
        deducted_by_coupons: str = None,
        deducted_by_prepaid_card: str = None,
        gaap_deducted_by_cash_coupons: str = None,
        gaap_deducted_by_coupons: str = None,
        gaap_deducted_by_prepaid_card: str = None,
        gaap_payment_amount: str = None,
        gaap_pretax_amount: str = None,
        gaap_pretax_amount_local: str = None,
        gaap_pretax_gross_amount: str = None,
        gaap_pricing_discount: str = None,
        instance_id: str = None,
        month_gaap_deducted_by_cash_coupons: str = None,
        month_gaap_deducted_by_coupons: str = None,
        month_gaap_deducted_by_prepaid_card: str = None,
        month_gaap_payment_amount: str = None,
        month_gaap_pretax_amount: str = None,
        month_gaap_pretax_amount_local: str = None,
        month_gaap_pretax_gross_amount: str = None,
        month_gaap_pricing_discount: str = None,
        order_id: str = None,
        order_type: str = None,
        owner_id: str = None,
        pay_time: str = None,
        payer_account: str = None,
        payment_amount: str = None,
        payment_currency: str = None,
        pretax_amount: str = None,
        pretax_amount_local: str = None,
        pretax_gross_amount: str = None,
        pricing_discount: str = None,
        product_code: str = None,
        product_type: str = None,
        region: str = None,
        resource_group: str = None,
        sub_order_id: str = None,
        subscription_type: str = None,
        tag: str = None,
        unallocated_deducted_by_cash_coupons: str = None,
        unallocated_deducted_by_coupons: str = None,
        unallocated_deducted_by_prepaid_card: str = None,
        unallocated_payment_amount: str = None,
        unallocated_pretax_amount: str = None,
        unallocated_pretax_amount_local: str = None,
        unallocated_pretax_gross_amount: str = None,
        unallocated_pricing_discount: str = None,
        usage_end_date: str = None,
        usage_start_date: str = None,
    ):
        self.accounting_unit = accounting_unit
        self.bill_type = bill_type
        self.billing_cycle = billing_cycle
        self.currency = currency
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        self.deducted_by_coupons = deducted_by_coupons
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        self.gaap_deducted_by_cash_coupons = gaap_deducted_by_cash_coupons
        self.gaap_deducted_by_coupons = gaap_deducted_by_coupons
        self.gaap_deducted_by_prepaid_card = gaap_deducted_by_prepaid_card
        self.gaap_payment_amount = gaap_payment_amount
        self.gaap_pretax_amount = gaap_pretax_amount
        self.gaap_pretax_amount_local = gaap_pretax_amount_local
        self.gaap_pretax_gross_amount = gaap_pretax_gross_amount
        self.gaap_pricing_discount = gaap_pricing_discount
        self.instance_id = instance_id
        self.month_gaap_deducted_by_cash_coupons = month_gaap_deducted_by_cash_coupons
        self.month_gaap_deducted_by_coupons = month_gaap_deducted_by_coupons
        self.month_gaap_deducted_by_prepaid_card = month_gaap_deducted_by_prepaid_card
        self.month_gaap_payment_amount = month_gaap_payment_amount
        self.month_gaap_pretax_amount = month_gaap_pretax_amount
        self.month_gaap_pretax_amount_local = month_gaap_pretax_amount_local
        self.month_gaap_pretax_gross_amount = month_gaap_pretax_gross_amount
        self.month_gaap_pricing_discount = month_gaap_pricing_discount
        self.order_id = order_id
        self.order_type = order_type
        self.owner_id = owner_id
        self.pay_time = pay_time
        self.payer_account = payer_account
        self.payment_amount = payment_amount
        self.payment_currency = payment_currency
        self.pretax_amount = pretax_amount
        self.pretax_amount_local = pretax_amount_local
        self.pretax_gross_amount = pretax_gross_amount
        self.pricing_discount = pricing_discount
        self.product_code = product_code
        self.product_type = product_type
        self.region = region
        self.resource_group = resource_group
        self.sub_order_id = sub_order_id
        self.subscription_type = subscription_type
        self.tag = tag
        self.unallocated_deducted_by_cash_coupons = unallocated_deducted_by_cash_coupons
        self.unallocated_deducted_by_coupons = unallocated_deducted_by_coupons
        self.unallocated_deducted_by_prepaid_card = unallocated_deducted_by_prepaid_card
        self.unallocated_payment_amount = unallocated_payment_amount
        self.unallocated_pretax_amount = unallocated_pretax_amount
        self.unallocated_pretax_amount_local = unallocated_pretax_amount_local
        self.unallocated_pretax_gross_amount = unallocated_pretax_gross_amount
        self.unallocated_pricing_discount = unallocated_pricing_discount
        self.usage_end_date = usage_end_date
        self.usage_start_date = usage_start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accounting_unit is not None:
            result['AccountingUnit'] = self.accounting_unit

        if self.bill_type is not None:
            result['BillType'] = self.bill_type

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons

        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons

        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card

        if self.gaap_deducted_by_cash_coupons is not None:
            result['GaapDeductedByCashCoupons'] = self.gaap_deducted_by_cash_coupons

        if self.gaap_deducted_by_coupons is not None:
            result['GaapDeductedByCoupons'] = self.gaap_deducted_by_coupons

        if self.gaap_deducted_by_prepaid_card is not None:
            result['GaapDeductedByPrepaidCard'] = self.gaap_deducted_by_prepaid_card

        if self.gaap_payment_amount is not None:
            result['GaapPaymentAmount'] = self.gaap_payment_amount

        if self.gaap_pretax_amount is not None:
            result['GaapPretaxAmount'] = self.gaap_pretax_amount

        if self.gaap_pretax_amount_local is not None:
            result['GaapPretaxAmountLocal'] = self.gaap_pretax_amount_local

        if self.gaap_pretax_gross_amount is not None:
            result['GaapPretaxGrossAmount'] = self.gaap_pretax_gross_amount

        if self.gaap_pricing_discount is not None:
            result['GaapPricingDiscount'] = self.gaap_pricing_discount

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.month_gaap_deducted_by_cash_coupons is not None:
            result['MonthGaapDeductedByCashCoupons'] = self.month_gaap_deducted_by_cash_coupons

        if self.month_gaap_deducted_by_coupons is not None:
            result['MonthGaapDeductedByCoupons'] = self.month_gaap_deducted_by_coupons

        if self.month_gaap_deducted_by_prepaid_card is not None:
            result['MonthGaapDeductedByPrepaidCard'] = self.month_gaap_deducted_by_prepaid_card

        if self.month_gaap_payment_amount is not None:
            result['MonthGaapPaymentAmount'] = self.month_gaap_payment_amount

        if self.month_gaap_pretax_amount is not None:
            result['MonthGaapPretaxAmount'] = self.month_gaap_pretax_amount

        if self.month_gaap_pretax_amount_local is not None:
            result['MonthGaapPretaxAmountLocal'] = self.month_gaap_pretax_amount_local

        if self.month_gaap_pretax_gross_amount is not None:
            result['MonthGaapPretaxGrossAmount'] = self.month_gaap_pretax_gross_amount

        if self.month_gaap_pricing_discount is not None:
            result['MonthGaapPricingDiscount'] = self.month_gaap_pricing_discount

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id

        if self.pay_time is not None:
            result['PayTime'] = self.pay_time

        if self.payer_account is not None:
            result['PayerAccount'] = self.payer_account

        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount

        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency

        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount

        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local

        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount

        if self.pricing_discount is not None:
            result['PricingDiscount'] = self.pricing_discount

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.sub_order_id is not None:
            result['SubOrderId'] = self.sub_order_id

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.unallocated_deducted_by_cash_coupons is not None:
            result['UnallocatedDeductedByCashCoupons'] = self.unallocated_deducted_by_cash_coupons

        if self.unallocated_deducted_by_coupons is not None:
            result['UnallocatedDeductedByCoupons'] = self.unallocated_deducted_by_coupons

        if self.unallocated_deducted_by_prepaid_card is not None:
            result['UnallocatedDeductedByPrepaidCard'] = self.unallocated_deducted_by_prepaid_card

        if self.unallocated_payment_amount is not None:
            result['UnallocatedPaymentAmount'] = self.unallocated_payment_amount

        if self.unallocated_pretax_amount is not None:
            result['UnallocatedPretaxAmount'] = self.unallocated_pretax_amount

        if self.unallocated_pretax_amount_local is not None:
            result['UnallocatedPretaxAmountLocal'] = self.unallocated_pretax_amount_local

        if self.unallocated_pretax_gross_amount is not None:
            result['UnallocatedPretaxGrossAmount'] = self.unallocated_pretax_gross_amount

        if self.unallocated_pricing_discount is not None:
            result['UnallocatedPricingDiscount'] = self.unallocated_pricing_discount

        if self.usage_end_date is not None:
            result['UsageEndDate'] = self.usage_end_date

        if self.usage_start_date is not None:
            result['UsageStartDate'] = self.usage_start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountingUnit') is not None:
            self.accounting_unit = m.get('AccountingUnit')

        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')

        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')

        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')

        if m.get('GaapDeductedByCashCoupons') is not None:
            self.gaap_deducted_by_cash_coupons = m.get('GaapDeductedByCashCoupons')

        if m.get('GaapDeductedByCoupons') is not None:
            self.gaap_deducted_by_coupons = m.get('GaapDeductedByCoupons')

        if m.get('GaapDeductedByPrepaidCard') is not None:
            self.gaap_deducted_by_prepaid_card = m.get('GaapDeductedByPrepaidCard')

        if m.get('GaapPaymentAmount') is not None:
            self.gaap_payment_amount = m.get('GaapPaymentAmount')

        if m.get('GaapPretaxAmount') is not None:
            self.gaap_pretax_amount = m.get('GaapPretaxAmount')

        if m.get('GaapPretaxAmountLocal') is not None:
            self.gaap_pretax_amount_local = m.get('GaapPretaxAmountLocal')

        if m.get('GaapPretaxGrossAmount') is not None:
            self.gaap_pretax_gross_amount = m.get('GaapPretaxGrossAmount')

        if m.get('GaapPricingDiscount') is not None:
            self.gaap_pricing_discount = m.get('GaapPricingDiscount')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('MonthGaapDeductedByCashCoupons') is not None:
            self.month_gaap_deducted_by_cash_coupons = m.get('MonthGaapDeductedByCashCoupons')

        if m.get('MonthGaapDeductedByCoupons') is not None:
            self.month_gaap_deducted_by_coupons = m.get('MonthGaapDeductedByCoupons')

        if m.get('MonthGaapDeductedByPrepaidCard') is not None:
            self.month_gaap_deducted_by_prepaid_card = m.get('MonthGaapDeductedByPrepaidCard')

        if m.get('MonthGaapPaymentAmount') is not None:
            self.month_gaap_payment_amount = m.get('MonthGaapPaymentAmount')

        if m.get('MonthGaapPretaxAmount') is not None:
            self.month_gaap_pretax_amount = m.get('MonthGaapPretaxAmount')

        if m.get('MonthGaapPretaxAmountLocal') is not None:
            self.month_gaap_pretax_amount_local = m.get('MonthGaapPretaxAmountLocal')

        if m.get('MonthGaapPretaxGrossAmount') is not None:
            self.month_gaap_pretax_gross_amount = m.get('MonthGaapPretaxGrossAmount')

        if m.get('MonthGaapPricingDiscount') is not None:
            self.month_gaap_pricing_discount = m.get('MonthGaapPricingDiscount')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')

        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')

        if m.get('PayerAccount') is not None:
            self.payer_account = m.get('PayerAccount')

        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')

        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')

        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')

        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')

        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')

        if m.get('PricingDiscount') is not None:
            self.pricing_discount = m.get('PricingDiscount')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('SubOrderId') is not None:
            self.sub_order_id = m.get('SubOrderId')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('UnallocatedDeductedByCashCoupons') is not None:
            self.unallocated_deducted_by_cash_coupons = m.get('UnallocatedDeductedByCashCoupons')

        if m.get('UnallocatedDeductedByCoupons') is not None:
            self.unallocated_deducted_by_coupons = m.get('UnallocatedDeductedByCoupons')

        if m.get('UnallocatedDeductedByPrepaidCard') is not None:
            self.unallocated_deducted_by_prepaid_card = m.get('UnallocatedDeductedByPrepaidCard')

        if m.get('UnallocatedPaymentAmount') is not None:
            self.unallocated_payment_amount = m.get('UnallocatedPaymentAmount')

        if m.get('UnallocatedPretaxAmount') is not None:
            self.unallocated_pretax_amount = m.get('UnallocatedPretaxAmount')

        if m.get('UnallocatedPretaxAmountLocal') is not None:
            self.unallocated_pretax_amount_local = m.get('UnallocatedPretaxAmountLocal')

        if m.get('UnallocatedPretaxGrossAmount') is not None:
            self.unallocated_pretax_gross_amount = m.get('UnallocatedPretaxGrossAmount')

        if m.get('UnallocatedPricingDiscount') is not None:
            self.unallocated_pricing_discount = m.get('UnallocatedPricingDiscount')

        if m.get('UsageEndDate') is not None:
            self.usage_end_date = m.get('UsageEndDate')

        if m.get('UsageStartDate') is not None:
            self.usage_start_date = m.get('UsageStartDate')

        return self

