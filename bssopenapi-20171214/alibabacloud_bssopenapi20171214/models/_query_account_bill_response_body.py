# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryAccountBillResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryAccountBillResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
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
            temp_model = main_models.QueryAccountBillResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAccountBillResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        billing_cycle: str = None,
        items: main_models.QueryAccountBillResponseBodyDataItems = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id
        # The name of the Alibaba Cloud account.
        self.account_name = account_name
        # The billing cycle. Format: YYYY-MM.
        self.billing_cycle = billing_cycle
        # The details of the bills.
        self.items = items
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of returned entries.
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
            temp_model = main_models.QueryAccountBillResponseBodyDataItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryAccountBillResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        item: List[main_models.QueryAccountBillResponseBodyDataItemsItem] = None,
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
                temp_model = main_models.QueryAccountBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k1))

        return self

class QueryAccountBillResponseBodyDataItemsItem(DaraModel):
    def __init__(
        self,
        adjust_amount: float = None,
        bill_account_id: str = None,
        bill_account_name: str = None,
        billing_date: str = None,
        biz_type: str = None,
        cash_amount: float = None,
        cost_unit: str = None,
        currency: str = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        invoice_discount: float = None,
        outstanding_amount: float = None,
        owner_id: str = None,
        owner_name: str = None,
        payment_amount: float = None,
        pip_code: str = None,
        pretax_amount: float = None,
        pretax_gross_amount: float = None,
        product_code: str = None,
        product_name: str = None,
        subscription_type: str = None,
    ):
        # The amount deducted by using credit refunds.
        self.adjust_amount = adjust_amount
        # The ID of the account to which the bill belongs.
        self.bill_account_id = bill_account_id
        # The name of the account to which the bill belongs.
        self.bill_account_name = bill_account_name
        # The billing date.
        self.billing_date = billing_date
        # The business type.
        self.biz_type = biz_type
        # The amount paid in cash. The amount that was deducted by using credit refunds is not included.
        self.cash_amount = cash_amount
        # The cost center.
        self.cost_unit = cost_unit
        # The type of the currency. Valid values:
        # 
        # *   CNY
        # *   USD
        # *   JPY
        self.currency = currency
        # The amount deducted by using vouchers.
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        # The amount deducted by using coupons.
        self.deducted_by_coupons = deducted_by_coupons
        # The amount deducted by using prepaid cards.
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        # The discount amount.
        self.invoice_discount = invoice_discount
        # The unsettled amount or the amount settled with credits.
        self.outstanding_amount = outstanding_amount
        # The ID of the member.
        self.owner_id = owner_id
        # The name of the member.
        self.owner_name = owner_name
        # The amount paid in cash. The amount that was deducted by using credit refunds is included.
        self.payment_amount = payment_amount
        # The code of the service. The service code is consistent with that displayed in User Center.
        self.pip_code = pip_code
        # The pretax amount.
        self.pretax_amount = pretax_amount
        # The pretax gross amount.
        self.pretax_gross_amount = pretax_gross_amount
        # The code of the service.
        # 
        # > A value is returned only if the **IsGroupByProduct** parameter is set to true.
        self.product_code = product_code
        # The name of the service.
        # 
        # > A value is returned only if the **IsGroupByProduct** parameter is set to true.
        self.product_name = product_name
        # The billing method. Valid values:
        # 
        # *   Subscription: the subscription billing method
        # *   PayAsYouGo: the pay-as-you-go billing method
        # 
        # > A value is returned only if the IsGroupByProduct parameter is set to true.
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjust_amount is not None:
            result['AdjustAmount'] = self.adjust_amount

        if self.bill_account_id is not None:
            result['BillAccountID'] = self.bill_account_id

        if self.bill_account_name is not None:
            result['BillAccountName'] = self.bill_account_name

        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount

        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit

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

        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount

        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount

        if self.pip_code is not None:
            result['PipCode'] = self.pip_code

        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount

        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustAmount') is not None:
            self.adjust_amount = m.get('AdjustAmount')

        if m.get('BillAccountID') is not None:
            self.bill_account_id = m.get('BillAccountID')

        if m.get('BillAccountName') is not None:
            self.bill_account_name = m.get('BillAccountName')

        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')

        if m.get('CostUnit') is not None:
            self.cost_unit = m.get('CostUnit')

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

        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')

        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')

        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')

        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')

        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

