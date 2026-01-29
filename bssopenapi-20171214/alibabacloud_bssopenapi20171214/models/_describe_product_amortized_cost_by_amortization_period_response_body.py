# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeProductAmortizedCostByAmortizationPeriodResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeProductAmortizedCostByAmortizationPeriodResponseBodyData = None,
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
            temp_model = main_models.DescribeProductAmortizedCostByAmortizationPeriodResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeProductAmortizedCostByAmortizationPeriodResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        items: List[main_models.DescribeProductAmortizedCostByAmortizationPeriodResponseBodyDataItems] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The ID of the account.
        self.account_id = account_id
        # The name of the account.
        self.account_name = account_name
        # The data entries returned.
        self.items = items
        # The maximum number of entries returned.
        self.max_results = max_results
        # The position from which the results started to return. The parameter must be left empty or set to the value of the NextToken parameter returned from the last call. Otherwise, an error is returned. If this parameter is left empty, data is queried from the beginning.
        self.next_token = next_token
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountID'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeProductAmortizedCostByAmortizationPeriodResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeProductAmortizedCostByAmortizationPeriodResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        after_discount_amount: float = None,
        amortization_period: str = None,
        amortization_status: str = None,
        bill_account_id: int = None,
        bill_account_name: str = None,
        bill_owner_id: int = None,
        bill_owner_name: str = None,
        biz_type: str = None,
        consume_period: str = None,
        current_amortization_after_discount_amount: float = None,
        current_amortization_deducted_by_cash_coupons: float = None,
        current_amortization_deducted_by_coupons: float = None,
        current_amortization_deducted_by_prepaid_card: float = None,
        current_amortization_expenditure_amount: float = None,
        current_amortization_invoice_discount: float = None,
        current_amortization_pretax_amount: float = None,
        current_amortization_pretax_gross_amount: float = None,
        current_amortization_round_down_discount: float = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        expenditure_amount: float = None,
        invoice_discount: float = None,
        pretax_amount: float = None,
        pretax_gross_amount: float = None,
        previously_amortized_after_discount_amount: float = None,
        previously_amortized_deducted_by_cash_coupons: float = None,
        previously_amortized_deducted_by_coupons: float = None,
        previously_amortized_deducted_by_prepaid_card: float = None,
        previously_amortized_expenditure_amount: float = None,
        previously_amortized_invoice_discount: float = None,
        previously_amortized_pretax_amount: float = None,
        previously_amortized_pretax_gross_amount: float = None,
        previously_amortized_round_down_discount: float = None,
        product_code: str = None,
        product_detail: str = None,
        product_detail_code: str = None,
        product_name: str = None,
        remaining_amortization_after_discount_amount: float = None,
        remaining_amortization_deducted_by_cash_coupons: float = None,
        remaining_amortization_deducted_by_coupons: float = None,
        remaining_amortization_deducted_by_prepaid_card: float = None,
        remaining_amortization_expenditure_amount: float = None,
        remaining_amortization_invoice_discount: float = None,
        remaining_amortization_pretax_amount: float = None,
        remaining_amortization_pretax_gross_amount: float = None,
        remaining_amortization_round_down_discount: float = None,
        round_down_discount: float = None,
        subscription_type: str = None,
    ):
        self.after_discount_amount = after_discount_amount
        # The allocation month. Format: YYYYMM.
        self.amortization_period = amortization_period
        # The allocation status. Valid values:
        # 
        # *   amortized: allocated
        # *   unAmortized: not allocated
        self.amortization_status = amortization_status
        # The ID of the account to which the bill belongs.
        self.bill_account_id = bill_account_id
        # The name of the account to which the bill belongs.
        self.bill_account_name = bill_account_name
        # The ID of the account to which the resource belongs.
        self.bill_owner_id = bill_owner_id
        # The name of the account to which the resource belongs.
        self.bill_owner_name = bill_owner_name
        # The business type.
        self.biz_type = biz_type
        # The billing cycle. Format: YYYYMM.
        self.consume_period = consume_period
        self.current_amortization_after_discount_amount = current_amortization_after_discount_amount
        # The amount deducted by using vouchers and allocated to the current allocation month.
        self.current_amortization_deducted_by_cash_coupons = current_amortization_deducted_by_cash_coupons
        # The amount deducted by using coupons and allocated to the current allocation month.
        self.current_amortization_deducted_by_coupons = current_amortization_deducted_by_coupons
        # The amount deducted by using prepaid cards and allocated to the current allocation month.
        self.current_amortization_deducted_by_prepaid_card = current_amortization_deducted_by_prepaid_card
        # The expenditure amount allocated to the current allocation month. Invoicing is supported.
        self.current_amortization_expenditure_amount = current_amortization_expenditure_amount
        # The discount amount allocated to the current allocation month.
        self.current_amortization_invoice_discount = current_amortization_invoice_discount
        # The pretax amount allocated to the current allocation month.
        self.current_amortization_pretax_amount = current_amortization_pretax_amount
        # The pretax gross amount allocated to the current allocation month.
        self.current_amortization_pretax_gross_amount = current_amortization_pretax_gross_amount
        # The round-off amount allocated to the current allocation month.
        self.current_amortization_round_down_discount = current_amortization_round_down_discount
        # The amount deducted by using vouchers.
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        # The amount deducted by using coupons.
        self.deducted_by_coupons = deducted_by_coupons
        # The amount deducted by using prepaid cards.
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        # The expenditure amount. Invoicing is supported.
        self.expenditure_amount = expenditure_amount
        # The discount amount.
        self.invoice_discount = invoice_discount
        # The pretax amount.
        self.pretax_amount = pretax_amount
        # The pretax gross amount.
        self.pretax_gross_amount = pretax_gross_amount
        self.previously_amortized_after_discount_amount = previously_amortized_after_discount_amount
        # The amount deducted by using vouchers and allocated before the current allocation month.
        self.previously_amortized_deducted_by_cash_coupons = previously_amortized_deducted_by_cash_coupons
        # The amount deducted by using coupons and allocated before the current allocation month.
        self.previously_amortized_deducted_by_coupons = previously_amortized_deducted_by_coupons
        # The amount deducted by using prepaid cards and allocated before the current allocation month.
        self.previously_amortized_deducted_by_prepaid_card = previously_amortized_deducted_by_prepaid_card
        # The expenditure amount allocated before the current allocation month. Invoicing is supported.
        self.previously_amortized_expenditure_amount = previously_amortized_expenditure_amount
        # The discount amount allocated before the current allocation month.
        self.previously_amortized_invoice_discount = previously_amortized_invoice_discount
        # The pretax amount allocated before the current allocation month.
        self.previously_amortized_pretax_amount = previously_amortized_pretax_amount
        # The pretax gross amount allocated before the current allocation month.
        self.previously_amortized_pretax_gross_amount = previously_amortized_pretax_gross_amount
        # The round-off amount allocated before the current allocation month.
        self.previously_amortized_round_down_discount = previously_amortized_round_down_discount
        # The code of the service.
        self.product_code = product_code
        # The specific service resource.
        self.product_detail = product_detail
        # The code of the specific service resource.
        self.product_detail_code = product_detail_code
        # The name of the service.
        self.product_name = product_name
        self.remaining_amortization_after_discount_amount = remaining_amortization_after_discount_amount
        # The amount deducted by using vouchers and to be allocated to one or more future allocation months.
        self.remaining_amortization_deducted_by_cash_coupons = remaining_amortization_deducted_by_cash_coupons
        # The amount deducted by using coupons and to be allocated to one or more future allocation months.
        self.remaining_amortization_deducted_by_coupons = remaining_amortization_deducted_by_coupons
        # The amount deducted by using prepaid cards and to be allocated to one or more future allocation months.
        self.remaining_amortization_deducted_by_prepaid_card = remaining_amortization_deducted_by_prepaid_card
        # The expenditure amount to be allocated to one or more future allocation months. Invoicing is supported.
        self.remaining_amortization_expenditure_amount = remaining_amortization_expenditure_amount
        # The discount amount to be allocated to one or more future allocation months.
        self.remaining_amortization_invoice_discount = remaining_amortization_invoice_discount
        # The pretax amount to be allocated to one or more future allocation months.
        self.remaining_amortization_pretax_amount = remaining_amortization_pretax_amount
        # The pretax gross amount to be allocated to one or more future allocation months.
        self.remaining_amortization_pretax_gross_amount = remaining_amortization_pretax_gross_amount
        # The round-off amount to be allocated to one or more future allocation months.
        self.remaining_amortization_round_down_discount = remaining_amortization_round_down_discount
        # The round-off amount.
        self.round_down_discount = round_down_discount
        # The billing method. Valid values:
        # 
        # *   Subscription: the subscription billing method
        # *   PayAsYouGo: the pay-as-you-go billing method
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_discount_amount is not None:
            result['AfterDiscountAmount'] = self.after_discount_amount

        if self.amortization_period is not None:
            result['AmortizationPeriod'] = self.amortization_period

        if self.amortization_status is not None:
            result['AmortizationStatus'] = self.amortization_status

        if self.bill_account_id is not None:
            result['BillAccountID'] = self.bill_account_id

        if self.bill_account_name is not None:
            result['BillAccountName'] = self.bill_account_name

        if self.bill_owner_id is not None:
            result['BillOwnerID'] = self.bill_owner_id

        if self.bill_owner_name is not None:
            result['BillOwnerName'] = self.bill_owner_name

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.consume_period is not None:
            result['ConsumePeriod'] = self.consume_period

        if self.current_amortization_after_discount_amount is not None:
            result['CurrentAmortizationAfterDiscountAmount'] = self.current_amortization_after_discount_amount

        if self.current_amortization_deducted_by_cash_coupons is not None:
            result['CurrentAmortizationDeductedByCashCoupons'] = self.current_amortization_deducted_by_cash_coupons

        if self.current_amortization_deducted_by_coupons is not None:
            result['CurrentAmortizationDeductedByCoupons'] = self.current_amortization_deducted_by_coupons

        if self.current_amortization_deducted_by_prepaid_card is not None:
            result['CurrentAmortizationDeductedByPrepaidCard'] = self.current_amortization_deducted_by_prepaid_card

        if self.current_amortization_expenditure_amount is not None:
            result['CurrentAmortizationExpenditureAmount'] = self.current_amortization_expenditure_amount

        if self.current_amortization_invoice_discount is not None:
            result['CurrentAmortizationInvoiceDiscount'] = self.current_amortization_invoice_discount

        if self.current_amortization_pretax_amount is not None:
            result['CurrentAmortizationPretaxAmount'] = self.current_amortization_pretax_amount

        if self.current_amortization_pretax_gross_amount is not None:
            result['CurrentAmortizationPretaxGrossAmount'] = self.current_amortization_pretax_gross_amount

        if self.current_amortization_round_down_discount is not None:
            result['CurrentAmortizationRoundDownDiscount'] = self.current_amortization_round_down_discount

        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons

        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons

        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card

        if self.expenditure_amount is not None:
            result['ExpenditureAmount'] = self.expenditure_amount

        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount

        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount

        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount

        if self.previously_amortized_after_discount_amount is not None:
            result['PreviouslyAmortizedAfterDiscountAmount'] = self.previously_amortized_after_discount_amount

        if self.previously_amortized_deducted_by_cash_coupons is not None:
            result['PreviouslyAmortizedDeductedByCashCoupons'] = self.previously_amortized_deducted_by_cash_coupons

        if self.previously_amortized_deducted_by_coupons is not None:
            result['PreviouslyAmortizedDeductedByCoupons'] = self.previously_amortized_deducted_by_coupons

        if self.previously_amortized_deducted_by_prepaid_card is not None:
            result['PreviouslyAmortizedDeductedByPrepaidCard'] = self.previously_amortized_deducted_by_prepaid_card

        if self.previously_amortized_expenditure_amount is not None:
            result['PreviouslyAmortizedExpenditureAmount'] = self.previously_amortized_expenditure_amount

        if self.previously_amortized_invoice_discount is not None:
            result['PreviouslyAmortizedInvoiceDiscount'] = self.previously_amortized_invoice_discount

        if self.previously_amortized_pretax_amount is not None:
            result['PreviouslyAmortizedPretaxAmount'] = self.previously_amortized_pretax_amount

        if self.previously_amortized_pretax_gross_amount is not None:
            result['PreviouslyAmortizedPretaxGrossAmount'] = self.previously_amortized_pretax_gross_amount

        if self.previously_amortized_round_down_discount is not None:
            result['PreviouslyAmortizedRoundDownDiscount'] = self.previously_amortized_round_down_discount

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail

        if self.product_detail_code is not None:
            result['ProductDetailCode'] = self.product_detail_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.remaining_amortization_after_discount_amount is not None:
            result['RemainingAmortizationAfterDiscountAmount'] = self.remaining_amortization_after_discount_amount

        if self.remaining_amortization_deducted_by_cash_coupons is not None:
            result['RemainingAmortizationDeductedByCashCoupons'] = self.remaining_amortization_deducted_by_cash_coupons

        if self.remaining_amortization_deducted_by_coupons is not None:
            result['RemainingAmortizationDeductedByCoupons'] = self.remaining_amortization_deducted_by_coupons

        if self.remaining_amortization_deducted_by_prepaid_card is not None:
            result['RemainingAmortizationDeductedByPrepaidCard'] = self.remaining_amortization_deducted_by_prepaid_card

        if self.remaining_amortization_expenditure_amount is not None:
            result['RemainingAmortizationExpenditureAmount'] = self.remaining_amortization_expenditure_amount

        if self.remaining_amortization_invoice_discount is not None:
            result['RemainingAmortizationInvoiceDiscount'] = self.remaining_amortization_invoice_discount

        if self.remaining_amortization_pretax_amount is not None:
            result['RemainingAmortizationPretaxAmount'] = self.remaining_amortization_pretax_amount

        if self.remaining_amortization_pretax_gross_amount is not None:
            result['RemainingAmortizationPretaxGrossAmount'] = self.remaining_amortization_pretax_gross_amount

        if self.remaining_amortization_round_down_discount is not None:
            result['RemainingAmortizationRoundDownDiscount'] = self.remaining_amortization_round_down_discount

        if self.round_down_discount is not None:
            result['RoundDownDiscount'] = self.round_down_discount

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDiscountAmount') is not None:
            self.after_discount_amount = m.get('AfterDiscountAmount')

        if m.get('AmortizationPeriod') is not None:
            self.amortization_period = m.get('AmortizationPeriod')

        if m.get('AmortizationStatus') is not None:
            self.amortization_status = m.get('AmortizationStatus')

        if m.get('BillAccountID') is not None:
            self.bill_account_id = m.get('BillAccountID')

        if m.get('BillAccountName') is not None:
            self.bill_account_name = m.get('BillAccountName')

        if m.get('BillOwnerID') is not None:
            self.bill_owner_id = m.get('BillOwnerID')

        if m.get('BillOwnerName') is not None:
            self.bill_owner_name = m.get('BillOwnerName')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ConsumePeriod') is not None:
            self.consume_period = m.get('ConsumePeriod')

        if m.get('CurrentAmortizationAfterDiscountAmount') is not None:
            self.current_amortization_after_discount_amount = m.get('CurrentAmortizationAfterDiscountAmount')

        if m.get('CurrentAmortizationDeductedByCashCoupons') is not None:
            self.current_amortization_deducted_by_cash_coupons = m.get('CurrentAmortizationDeductedByCashCoupons')

        if m.get('CurrentAmortizationDeductedByCoupons') is not None:
            self.current_amortization_deducted_by_coupons = m.get('CurrentAmortizationDeductedByCoupons')

        if m.get('CurrentAmortizationDeductedByPrepaidCard') is not None:
            self.current_amortization_deducted_by_prepaid_card = m.get('CurrentAmortizationDeductedByPrepaidCard')

        if m.get('CurrentAmortizationExpenditureAmount') is not None:
            self.current_amortization_expenditure_amount = m.get('CurrentAmortizationExpenditureAmount')

        if m.get('CurrentAmortizationInvoiceDiscount') is not None:
            self.current_amortization_invoice_discount = m.get('CurrentAmortizationInvoiceDiscount')

        if m.get('CurrentAmortizationPretaxAmount') is not None:
            self.current_amortization_pretax_amount = m.get('CurrentAmortizationPretaxAmount')

        if m.get('CurrentAmortizationPretaxGrossAmount') is not None:
            self.current_amortization_pretax_gross_amount = m.get('CurrentAmortizationPretaxGrossAmount')

        if m.get('CurrentAmortizationRoundDownDiscount') is not None:
            self.current_amortization_round_down_discount = m.get('CurrentAmortizationRoundDownDiscount')

        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')

        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')

        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')

        if m.get('ExpenditureAmount') is not None:
            self.expenditure_amount = m.get('ExpenditureAmount')

        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')

        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')

        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')

        if m.get('PreviouslyAmortizedAfterDiscountAmount') is not None:
            self.previously_amortized_after_discount_amount = m.get('PreviouslyAmortizedAfterDiscountAmount')

        if m.get('PreviouslyAmortizedDeductedByCashCoupons') is not None:
            self.previously_amortized_deducted_by_cash_coupons = m.get('PreviouslyAmortizedDeductedByCashCoupons')

        if m.get('PreviouslyAmortizedDeductedByCoupons') is not None:
            self.previously_amortized_deducted_by_coupons = m.get('PreviouslyAmortizedDeductedByCoupons')

        if m.get('PreviouslyAmortizedDeductedByPrepaidCard') is not None:
            self.previously_amortized_deducted_by_prepaid_card = m.get('PreviouslyAmortizedDeductedByPrepaidCard')

        if m.get('PreviouslyAmortizedExpenditureAmount') is not None:
            self.previously_amortized_expenditure_amount = m.get('PreviouslyAmortizedExpenditureAmount')

        if m.get('PreviouslyAmortizedInvoiceDiscount') is not None:
            self.previously_amortized_invoice_discount = m.get('PreviouslyAmortizedInvoiceDiscount')

        if m.get('PreviouslyAmortizedPretaxAmount') is not None:
            self.previously_amortized_pretax_amount = m.get('PreviouslyAmortizedPretaxAmount')

        if m.get('PreviouslyAmortizedPretaxGrossAmount') is not None:
            self.previously_amortized_pretax_gross_amount = m.get('PreviouslyAmortizedPretaxGrossAmount')

        if m.get('PreviouslyAmortizedRoundDownDiscount') is not None:
            self.previously_amortized_round_down_discount = m.get('PreviouslyAmortizedRoundDownDiscount')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')

        if m.get('ProductDetailCode') is not None:
            self.product_detail_code = m.get('ProductDetailCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('RemainingAmortizationAfterDiscountAmount') is not None:
            self.remaining_amortization_after_discount_amount = m.get('RemainingAmortizationAfterDiscountAmount')

        if m.get('RemainingAmortizationDeductedByCashCoupons') is not None:
            self.remaining_amortization_deducted_by_cash_coupons = m.get('RemainingAmortizationDeductedByCashCoupons')

        if m.get('RemainingAmortizationDeductedByCoupons') is not None:
            self.remaining_amortization_deducted_by_coupons = m.get('RemainingAmortizationDeductedByCoupons')

        if m.get('RemainingAmortizationDeductedByPrepaidCard') is not None:
            self.remaining_amortization_deducted_by_prepaid_card = m.get('RemainingAmortizationDeductedByPrepaidCard')

        if m.get('RemainingAmortizationExpenditureAmount') is not None:
            self.remaining_amortization_expenditure_amount = m.get('RemainingAmortizationExpenditureAmount')

        if m.get('RemainingAmortizationInvoiceDiscount') is not None:
            self.remaining_amortization_invoice_discount = m.get('RemainingAmortizationInvoiceDiscount')

        if m.get('RemainingAmortizationPretaxAmount') is not None:
            self.remaining_amortization_pretax_amount = m.get('RemainingAmortizationPretaxAmount')

        if m.get('RemainingAmortizationPretaxGrossAmount') is not None:
            self.remaining_amortization_pretax_gross_amount = m.get('RemainingAmortizationPretaxGrossAmount')

        if m.get('RemainingAmortizationRoundDownDiscount') is not None:
            self.remaining_amortization_round_down_discount = m.get('RemainingAmortizationRoundDownDiscount')

        if m.get('RoundDownDiscount') is not None:
            self.round_down_discount = m.get('RoundDownDiscount')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

