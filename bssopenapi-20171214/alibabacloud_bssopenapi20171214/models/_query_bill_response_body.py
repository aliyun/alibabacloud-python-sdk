# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryBillResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryBillResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.QueryBillResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryBillResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        billing_cycle: str = None,
        items: main_models.QueryBillResponseBodyDataItems = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The account ID.
        self.account_id = account_id
        # The account name.
        self.account_name = account_name
        # The billing cycle, in the YYYY-MM format.
        self.billing_cycle = billing_cycle
        self.items = items
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountID'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('Items') is not None:
            temp_model = main_models.QueryBillResponseBodyDataItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryBillResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        item: List[main_models.QueryBillResponseBodyDataItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.QueryBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k1))

        return self

class QueryBillResponseBodyDataItemsItem(DaraModel):
    def __init__(
        self,
        adjust_amount: float = None,
        after_tax_amount: float = None,
        cash_amount: float = None,
        commodity_code: str = None,
        currency: str = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        invoice_discount: float = None,
        item: str = None,
        outstanding_amount: float = None,
        owner_id: str = None,
        payment_amount: float = None,
        payment_currency: str = None,
        payment_time: str = None,
        payment_transaction_id: str = None,
        pip_code: str = None,
        pretax_amount: float = None,
        pretax_amount_local: float = None,
        pretax_gross_amount: float = None,
        product_code: str = None,
        product_detail: str = None,
        product_name: str = None,
        product_type: str = None,
        record_id: str = None,
        round_down_discount: str = None,
        status: str = None,
        sub_order_id: str = None,
        subscription_type: str = None,
        tax: float = None,
        usage_end_time: str = None,
        usage_start_time: str = None,
    ):
        self.adjust_amount = adjust_amount
        self.after_tax_amount = after_tax_amount
        self.cash_amount = cash_amount
        self.commodity_code = commodity_code
        self.currency = currency
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        self.deducted_by_coupons = deducted_by_coupons
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        self.invoice_discount = invoice_discount
        self.item = item
        self.outstanding_amount = outstanding_amount
        self.owner_id = owner_id
        self.payment_amount = payment_amount
        self.payment_currency = payment_currency
        self.payment_time = payment_time
        self.payment_transaction_id = payment_transaction_id
        self.pip_code = pip_code
        self.pretax_amount = pretax_amount
        self.pretax_amount_local = pretax_amount_local
        self.pretax_gross_amount = pretax_gross_amount
        self.product_code = product_code
        self.product_detail = product_detail
        self.product_name = product_name
        self.product_type = product_type
        self.record_id = record_id
        self.round_down_discount = round_down_discount
        self.status = status
        self.sub_order_id = sub_order_id
        self.subscription_type = subscription_type
        self.tax = tax
        self.usage_end_time = usage_end_time
        self.usage_start_time = usage_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjust_amount is not None:
            result['AdjustAmount'] = self.adjust_amount

        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount

        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons

        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons

        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card

        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount

        if self.item is not None:
            result['Item'] = self.item

        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount

        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id

        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount

        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency

        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time

        if self.payment_transaction_id is not None:
            result['PaymentTransactionID'] = self.payment_transaction_id

        if self.pip_code is not None:
            result['PipCode'] = self.pip_code

        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount

        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local

        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.record_id is not None:
            result['RecordID'] = self.record_id

        if self.round_down_discount is not None:
            result['RoundDownDiscount'] = self.round_down_discount

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_order_id is not None:
            result['SubOrderId'] = self.sub_order_id

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        if self.tax is not None:
            result['Tax'] = self.tax

        if self.usage_end_time is not None:
            result['UsageEndTime'] = self.usage_end_time

        if self.usage_start_time is not None:
            result['UsageStartTime'] = self.usage_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustAmount') is not None:
            self.adjust_amount = m.get('AdjustAmount')

        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')

        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')

        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')

        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')

        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')

        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')

        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')

        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')

        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')

        if m.get('PaymentTransactionID') is not None:
            self.payment_transaction_id = m.get('PaymentTransactionID')

        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')

        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')

        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')

        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')

        if m.get('RoundDownDiscount') is not None:
            self.round_down_discount = m.get('RoundDownDiscount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubOrderId') is not None:
            self.sub_order_id = m.get('SubOrderId')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        if m.get('Tax') is not None:
            self.tax = m.get('Tax')

        if m.get('UsageEndTime') is not None:
            self.usage_end_time = m.get('UsageEndTime')

        if m.get('UsageStartTime') is not None:
            self.usage_start_time = m.get('UsageStartTime')

        return self

