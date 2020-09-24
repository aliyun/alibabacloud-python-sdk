# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class QueryAccountTransactionDetailsRequest(TeaModel):
    def __init__(self, transaction_number=None, record_id=None, transaction_channel_sn=None,
                 create_time_start=None, create_time_end=None, transaction_type=None, transaction_channel=None, next_token=None,
                 max_results=None):
        self.transaction_number = transaction_number  # type: str
        self.record_id = record_id      # type: str
        self.transaction_channel_sn = transaction_channel_sn  # type: str
        self.create_time_start = create_time_start  # type: str
        self.create_time_end = create_time_end  # type: str
        self.transaction_type = transaction_type  # type: str
        self.transaction_channel = transaction_channel  # type: str
        self.next_token = next_token    # type: str
        self.max_results = max_results  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['TransactionNumber'] = self.transaction_number
        result['RecordID'] = self.record_id
        result['TransactionChannelSN'] = self.transaction_channel_sn
        result['CreateTimeStart'] = self.create_time_start
        result['CreateTimeEnd'] = self.create_time_end
        result['TransactionType'] = self.transaction_type
        result['TransactionChannel'] = self.transaction_channel
        result['NextToken'] = self.next_token
        result['MaxResults'] = self.max_results
        return result

    def from_map(self, map={}):
        self.transaction_number = map.get('TransactionNumber')
        self.record_id = map.get('RecordID')
        self.transaction_channel_sn = map.get('TransactionChannelSN')
        self.create_time_start = map.get('CreateTimeStart')
        self.create_time_end = map.get('CreateTimeEnd')
        self.transaction_type = map.get('TransactionType')
        self.transaction_channel = map.get('TransactionChannel')
        self.next_token = map.get('NextToken')
        self.max_results = map.get('MaxResults')
        return self


class QueryAccountTransactionDetailsResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryAccountTransactionDetailsResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryAccountTransactionDetailsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryAccountTransactionDetailsResponseDataAccountTransactionsListAccountTransactionsList(TeaModel):
    def __init__(self, transaction_number=None, transaction_time=None, transaction_flow=None,
                 transaction_type=None, transaction_channel=None, transaction_channel_sn=None, fund_type=None, record_id=None,
                 remarks=None, billing_cycle=None, amount=None, balance=None, transaction_account=None):
        self.transaction_number = transaction_number  # type: str
        self.transaction_time = transaction_time  # type: str
        self.transaction_flow = transaction_flow  # type: str
        self.transaction_type = transaction_type  # type: str
        self.transaction_channel = transaction_channel  # type: str
        self.transaction_channel_sn = transaction_channel_sn  # type: str
        self.fund_type = fund_type      # type: str
        self.record_id = record_id      # type: str
        self.remarks = remarks          # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.amount = amount            # type: str
        self.balance = balance          # type: str
        self.transaction_account = transaction_account  # type: str

    def validate(self):
        self.validate_required(self.transaction_number, 'transaction_number')
        self.validate_required(self.transaction_time, 'transaction_time')
        self.validate_required(self.transaction_flow, 'transaction_flow')
        self.validate_required(self.transaction_type, 'transaction_type')
        self.validate_required(self.transaction_channel, 'transaction_channel')
        self.validate_required(self.transaction_channel_sn, 'transaction_channel_sn')
        self.validate_required(self.fund_type, 'fund_type')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.remarks, 'remarks')
        self.validate_required(self.billing_cycle, 'billing_cycle')
        self.validate_required(self.amount, 'amount')
        self.validate_required(self.balance, 'balance')
        self.validate_required(self.transaction_account, 'transaction_account')

    def to_map(self):
        result = {}
        result['TransactionNumber'] = self.transaction_number
        result['TransactionTime'] = self.transaction_time
        result['TransactionFlow'] = self.transaction_flow
        result['TransactionType'] = self.transaction_type
        result['TransactionChannel'] = self.transaction_channel
        result['TransactionChannelSN'] = self.transaction_channel_sn
        result['FundType'] = self.fund_type
        result['RecordID'] = self.record_id
        result['Remarks'] = self.remarks
        result['BillingCycle'] = self.billing_cycle
        result['Amount'] = self.amount
        result['Balance'] = self.balance
        result['TransactionAccount'] = self.transaction_account
        return result

    def from_map(self, map={}):
        self.transaction_number = map.get('TransactionNumber')
        self.transaction_time = map.get('TransactionTime')
        self.transaction_flow = map.get('TransactionFlow')
        self.transaction_type = map.get('TransactionType')
        self.transaction_channel = map.get('TransactionChannel')
        self.transaction_channel_sn = map.get('TransactionChannelSN')
        self.fund_type = map.get('FundType')
        self.record_id = map.get('RecordID')
        self.remarks = map.get('Remarks')
        self.billing_cycle = map.get('BillingCycle')
        self.amount = map.get('Amount')
        self.balance = map.get('Balance')
        self.transaction_account = map.get('TransactionAccount')
        return self


class QueryAccountTransactionDetailsResponseDataAccountTransactionsList(TeaModel):
    def __init__(self, account_transactions_list=None):
        self.account_transactions_list = account_transactions_list  # type: List[QueryAccountTransactionDetailsResponseDataAccountTransactionsListAccountTransactionsList]

    def validate(self):
        self.validate_required(self.account_transactions_list, 'account_transactions_list')
        if self.account_transactions_list:
            for k in self.account_transactions_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AccountTransactionsList'] = []
        if self.account_transactions_list is not None:
            for k in self.account_transactions_list:
                result['AccountTransactionsList'].append(k.to_map() if k else None)
        else:
            result['AccountTransactionsList'] = None
        return result

    def from_map(self, map={}):
        self.account_transactions_list = []
        if map.get('AccountTransactionsList') is not None:
            for k in map.get('AccountTransactionsList'):
                temp_model = QueryAccountTransactionDetailsResponseDataAccountTransactionsListAccountTransactionsList()
                self.account_transactions_list.append(temp_model.from_map(k))
        else:
            self.account_transactions_list = None
        return self


class QueryAccountTransactionDetailsResponseData(TeaModel):
    def __init__(self, account_name=None, total_count=None, next_token=None, max_results=None,
                 account_transactions_list=None):
        self.account_name = account_name  # type: str
        self.total_count = total_count  # type: int
        self.next_token = next_token    # type: str
        self.max_results = max_results  # type: int
        self.account_transactions_list = account_transactions_list  # type: QueryAccountTransactionDetailsResponseDataAccountTransactionsList

    def validate(self):
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.max_results, 'max_results')
        self.validate_required(self.account_transactions_list, 'account_transactions_list')
        if self.account_transactions_list:
            self.account_transactions_list.validate()

    def to_map(self):
        result = {}
        result['AccountName'] = self.account_name
        result['TotalCount'] = self.total_count
        result['NextToken'] = self.next_token
        result['MaxResults'] = self.max_results
        if self.account_transactions_list is not None:
            result['AccountTransactionsList'] = self.account_transactions_list.to_map()
        else:
            result['AccountTransactionsList'] = None
        return result

    def from_map(self, map={}):
        self.account_name = map.get('AccountName')
        self.total_count = map.get('TotalCount')
        self.next_token = map.get('NextToken')
        self.max_results = map.get('MaxResults')
        if map.get('AccountTransactionsList') is not None:
            temp_model = QueryAccountTransactionDetailsResponseDataAccountTransactionsList()
            self.account_transactions_list = temp_model.from_map(map['AccountTransactionsList'])
        else:
            self.account_transactions_list = None
        return self


class QuerySettleBillRequest(TeaModel):
    def __init__(self, billing_cycle=None, type=None, product_code=None, product_type=None, subscription_type=None,
                 is_hide_zero_charge=None, is_display_local_currency=None, next_token=None, max_results=None, bill_owner_id=None):
        self.billing_cycle = billing_cycle  # type: str
        self.type = type                # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.is_hide_zero_charge = is_hide_zero_charge  # type: bool
        self.is_display_local_currency = is_display_local_currency  # type: bool
        self.next_token = next_token    # type: str
        self.max_results = max_results  # type: int
        self.bill_owner_id = bill_owner_id  # type: int

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['Type'] = self.type
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['IsHideZeroCharge'] = self.is_hide_zero_charge
        result['IsDisplayLocalCurrency'] = self.is_display_local_currency
        result['NextToken'] = self.next_token
        result['MaxResults'] = self.max_results
        result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.type = map.get('Type')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.is_hide_zero_charge = map.get('IsHideZeroCharge')
        self.is_display_local_currency = map.get('IsDisplayLocalCurrency')
        self.next_token = map.get('NextToken')
        self.max_results = map.get('MaxResults')
        self.bill_owner_id = map.get('BillOwnerId')
        return self


class QuerySettleBillResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QuerySettleBillResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QuerySettleBillResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QuerySettleBillResponseDataItemsItem(TeaModel):
    def __init__(self, record_id=None, item=None, owner_id=None, usage_start_time=None, usage_end_time=None,
                 payment_time=None, product_code=None, product_type=None, subscription_type=None, product_name=None,
                 product_detail=None, pretax_gross_amount=None, deducted_by_coupons=None, invoice_discount=None,
                 pretax_amount=None, currency=None, pretax_amount_local=None, tax=None, payment_amount=None,
                 deducted_by_cash_coupons=None, deducted_by_prepaid_card=None, outstanding_amount=None, after_tax_amount=None, status=None,
                 payment_currency=None, payment_transaction_id=None, round_down_discount=None, sub_order_id=None, pip_code=None,
                 commodity_code=None):
        self.record_id = record_id      # type: str
        self.item = item                # type: str
        self.owner_id = owner_id        # type: str
        self.usage_start_time = usage_start_time  # type: str
        self.usage_end_time = usage_end_time  # type: str
        self.payment_time = payment_time  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.product_name = product_name  # type: str
        self.product_detail = product_detail  # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.pretax_amount = pretax_amount  # type: float
        self.currency = currency        # type: str
        self.pretax_amount_local = pretax_amount_local  # type: float
        self.tax = tax                  # type: float
        self.payment_amount = payment_amount  # type: float
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.outstanding_amount = outstanding_amount  # type: float
        self.after_tax_amount = after_tax_amount  # type: float
        self.status = status            # type: str
        self.payment_currency = payment_currency  # type: str
        self.payment_transaction_id = payment_transaction_id  # type: str
        self.round_down_discount = round_down_discount  # type: str
        self.sub_order_id = sub_order_id  # type: str
        self.pip_code = pip_code        # type: str
        self.commodity_code = commodity_code  # type: str

    def validate(self):
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.item, 'item')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.usage_start_time, 'usage_start_time')
        self.validate_required(self.usage_end_time, 'usage_end_time')
        self.validate_required(self.payment_time, 'payment_time')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.product_name, 'product_name')
        self.validate_required(self.product_detail, 'product_detail')
        self.validate_required(self.pretax_gross_amount, 'pretax_gross_amount')
        self.validate_required(self.deducted_by_coupons, 'deducted_by_coupons')
        self.validate_required(self.invoice_discount, 'invoice_discount')
        self.validate_required(self.pretax_amount, 'pretax_amount')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.pretax_amount_local, 'pretax_amount_local')
        self.validate_required(self.tax, 'tax')
        self.validate_required(self.payment_amount, 'payment_amount')
        self.validate_required(self.deducted_by_cash_coupons, 'deducted_by_cash_coupons')
        self.validate_required(self.deducted_by_prepaid_card, 'deducted_by_prepaid_card')
        self.validate_required(self.outstanding_amount, 'outstanding_amount')
        self.validate_required(self.after_tax_amount, 'after_tax_amount')
        self.validate_required(self.status, 'status')
        self.validate_required(self.payment_currency, 'payment_currency')
        self.validate_required(self.payment_transaction_id, 'payment_transaction_id')
        self.validate_required(self.round_down_discount, 'round_down_discount')
        self.validate_required(self.sub_order_id, 'sub_order_id')
        self.validate_required(self.pip_code, 'pip_code')
        self.validate_required(self.commodity_code, 'commodity_code')

    def to_map(self):
        result = {}
        result['RecordID'] = self.record_id
        result['Item'] = self.item
        result['OwnerID'] = self.owner_id
        result['UsageStartTime'] = self.usage_start_time
        result['UsageEndTime'] = self.usage_end_time
        result['PaymentTime'] = self.payment_time
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['ProductName'] = self.product_name
        result['ProductDetail'] = self.product_detail
        result['PretaxGrossAmount'] = self.pretax_gross_amount
        result['DeductedByCoupons'] = self.deducted_by_coupons
        result['InvoiceDiscount'] = self.invoice_discount
        result['PretaxAmount'] = self.pretax_amount
        result['Currency'] = self.currency
        result['PretaxAmountLocal'] = self.pretax_amount_local
        result['Tax'] = self.tax
        result['PaymentAmount'] = self.payment_amount
        result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        result['OutstandingAmount'] = self.outstanding_amount
        result['AfterTaxAmount'] = self.after_tax_amount
        result['Status'] = self.status
        result['PaymentCurrency'] = self.payment_currency
        result['PaymentTransactionID'] = self.payment_transaction_id
        result['RoundDownDiscount'] = self.round_down_discount
        result['SubOrderId'] = self.sub_order_id
        result['PipCode'] = self.pip_code
        result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, map={}):
        self.record_id = map.get('RecordID')
        self.item = map.get('Item')
        self.owner_id = map.get('OwnerID')
        self.usage_start_time = map.get('UsageStartTime')
        self.usage_end_time = map.get('UsageEndTime')
        self.payment_time = map.get('PaymentTime')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.product_name = map.get('ProductName')
        self.product_detail = map.get('ProductDetail')
        self.pretax_gross_amount = map.get('PretaxGrossAmount')
        self.deducted_by_coupons = map.get('DeductedByCoupons')
        self.invoice_discount = map.get('InvoiceDiscount')
        self.pretax_amount = map.get('PretaxAmount')
        self.currency = map.get('Currency')
        self.pretax_amount_local = map.get('PretaxAmountLocal')
        self.tax = map.get('Tax')
        self.payment_amount = map.get('PaymentAmount')
        self.deducted_by_cash_coupons = map.get('DeductedByCashCoupons')
        self.deducted_by_prepaid_card = map.get('DeductedByPrepaidCard')
        self.outstanding_amount = map.get('OutstandingAmount')
        self.after_tax_amount = map.get('AfterTaxAmount')
        self.status = map.get('Status')
        self.payment_currency = map.get('PaymentCurrency')
        self.payment_transaction_id = map.get('PaymentTransactionID')
        self.round_down_discount = map.get('RoundDownDiscount')
        self.sub_order_id = map.get('SubOrderId')
        self.pip_code = map.get('PipCode')
        self.commodity_code = map.get('CommodityCode')
        return self


class QuerySettleBillResponseDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[QuerySettleBillResponseDataItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = QuerySettleBillResponseDataItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class QuerySettleBillResponseData(TeaModel):
    def __init__(self, billing_cycle=None, account_id=None, account_name=None, next_token=None, max_results=None,
                 total_count=None, items=None):
        self.billing_cycle = billing_cycle  # type: str
        self.account_id = account_id    # type: str
        self.account_name = account_name  # type: str
        self.next_token = next_token    # type: str
        self.max_results = max_results  # type: int
        self.total_count = total_count  # type: int
        self.items = items              # type: QuerySettleBillResponseDataItems

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.max_results, 'max_results')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['AccountID'] = self.account_id
        result['AccountName'] = self.account_name
        result['NextToken'] = self.next_token
        result['MaxResults'] = self.max_results
        result['TotalCount'] = self.total_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.account_id = map.get('AccountID')
        self.account_name = map.get('AccountName')
        self.next_token = map.get('NextToken')
        self.max_results = map.get('MaxResults')
        self.total_count = map.get('TotalCount')
        if map.get('Items') is not None:
            temp_model = QuerySettleBillResponseDataItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class QuerySplitItemBillRequest(TeaModel):
    def __init__(self, billing_cycle=None, product_code=None, product_type=None, subscription_type=None,
                 page_num=None, page_size=None, bill_owner_id=None):
        self.billing_cycle = billing_cycle  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.bill_owner_id = bill_owner_id  # type: int

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.bill_owner_id = map.get('BillOwnerId')
        return self


class QuerySplitItemBillResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QuerySplitItemBillResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QuerySplitItemBillResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QuerySplitItemBillResponseDataItemsItem(TeaModel):
    def __init__(self, instance_id=None, billing_type=None, cost_unit=None, product_code=None, product_type=None,
                 subscription_type=None, product_name=None, product_detail=None, owner_id=None, billing_item=None, list_price=None,
                 list_price_unit=None, usage=None, usage_unit=None, deducted_by_resource_package=None, pretax_gross_amount=None,
                 invoice_discount=None, deducted_by_coupons=None, pretax_amount=None, deducted_by_cash_coupons=None,
                 deducted_by_prepaid_card=None, payment_amount=None, outstanding_amount=None, currency=None, nick_name=None,
                 resource_group=None, tag=None, instance_config=None, instance_spec=None, internet_ip=None, intranet_ip=None,
                 region=None, zone=None, item=None, service_period=None, billing_date=None, split_item_id=None,
                 split_item_name=None, pip_code=None, commodity_code=None):
        self.instance_id = instance_id  # type: str
        self.billing_type = billing_type  # type: str
        self.cost_unit = cost_unit      # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.product_name = product_name  # type: str
        self.product_detail = product_detail  # type: str
        self.owner_id = owner_id        # type: str
        self.billing_item = billing_item  # type: str
        self.list_price = list_price    # type: str
        self.list_price_unit = list_price_unit  # type: str
        self.usage = usage              # type: str
        self.usage_unit = usage_unit    # type: str
        self.deducted_by_resource_package = deducted_by_resource_package  # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.pretax_amount = pretax_amount  # type: float
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.payment_amount = payment_amount  # type: float
        self.outstanding_amount = outstanding_amount  # type: float
        self.currency = currency        # type: str
        self.nick_name = nick_name      # type: str
        self.resource_group = resource_group  # type: str
        self.tag = tag                  # type: str
        self.instance_config = instance_config  # type: str
        self.instance_spec = instance_spec  # type: str
        self.internet_ip = internet_ip  # type: str
        self.intranet_ip = intranet_ip  # type: str
        self.region = region            # type: str
        self.zone = zone                # type: str
        self.item = item                # type: str
        self.service_period = service_period  # type: str
        self.billing_date = billing_date  # type: str
        self.split_item_id = split_item_id  # type: str
        self.split_item_name = split_item_name  # type: str
        self.pip_code = pip_code        # type: str
        self.commodity_code = commodity_code  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.billing_type, 'billing_type')
        self.validate_required(self.cost_unit, 'cost_unit')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.product_name, 'product_name')
        self.validate_required(self.product_detail, 'product_detail')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.billing_item, 'billing_item')
        self.validate_required(self.list_price, 'list_price')
        self.validate_required(self.list_price_unit, 'list_price_unit')
        self.validate_required(self.usage, 'usage')
        self.validate_required(self.usage_unit, 'usage_unit')
        self.validate_required(self.deducted_by_resource_package, 'deducted_by_resource_package')
        self.validate_required(self.pretax_gross_amount, 'pretax_gross_amount')
        self.validate_required(self.invoice_discount, 'invoice_discount')
        self.validate_required(self.deducted_by_coupons, 'deducted_by_coupons')
        self.validate_required(self.pretax_amount, 'pretax_amount')
        self.validate_required(self.deducted_by_cash_coupons, 'deducted_by_cash_coupons')
        self.validate_required(self.deducted_by_prepaid_card, 'deducted_by_prepaid_card')
        self.validate_required(self.payment_amount, 'payment_amount')
        self.validate_required(self.outstanding_amount, 'outstanding_amount')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.nick_name, 'nick_name')
        self.validate_required(self.resource_group, 'resource_group')
        self.validate_required(self.tag, 'tag')
        self.validate_required(self.instance_config, 'instance_config')
        self.validate_required(self.instance_spec, 'instance_spec')
        self.validate_required(self.internet_ip, 'internet_ip')
        self.validate_required(self.intranet_ip, 'intranet_ip')
        self.validate_required(self.region, 'region')
        self.validate_required(self.zone, 'zone')
        self.validate_required(self.item, 'item')
        self.validate_required(self.service_period, 'service_period')
        self.validate_required(self.billing_date, 'billing_date')
        self.validate_required(self.split_item_id, 'split_item_id')
        self.validate_required(self.split_item_name, 'split_item_name')
        self.validate_required(self.pip_code, 'pip_code')
        self.validate_required(self.commodity_code, 'commodity_code')

    def to_map(self):
        result = {}
        result['InstanceID'] = self.instance_id
        result['BillingType'] = self.billing_type
        result['CostUnit'] = self.cost_unit
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['ProductName'] = self.product_name
        result['ProductDetail'] = self.product_detail
        result['OwnerID'] = self.owner_id
        result['BillingItem'] = self.billing_item
        result['ListPrice'] = self.list_price
        result['ListPriceUnit'] = self.list_price_unit
        result['Usage'] = self.usage
        result['UsageUnit'] = self.usage_unit
        result['DeductedByResourcePackage'] = self.deducted_by_resource_package
        result['PretaxGrossAmount'] = self.pretax_gross_amount
        result['InvoiceDiscount'] = self.invoice_discount
        result['DeductedByCoupons'] = self.deducted_by_coupons
        result['PretaxAmount'] = self.pretax_amount
        result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        result['PaymentAmount'] = self.payment_amount
        result['OutstandingAmount'] = self.outstanding_amount
        result['Currency'] = self.currency
        result['NickName'] = self.nick_name
        result['ResourceGroup'] = self.resource_group
        result['Tag'] = self.tag
        result['InstanceConfig'] = self.instance_config
        result['InstanceSpec'] = self.instance_spec
        result['InternetIP'] = self.internet_ip
        result['IntranetIP'] = self.intranet_ip
        result['Region'] = self.region
        result['Zone'] = self.zone
        result['Item'] = self.item
        result['ServicePeriod'] = self.service_period
        result['BillingDate'] = self.billing_date
        result['SplitItemID'] = self.split_item_id
        result['SplitItemName'] = self.split_item_name
        result['PipCode'] = self.pip_code
        result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceID')
        self.billing_type = map.get('BillingType')
        self.cost_unit = map.get('CostUnit')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.product_name = map.get('ProductName')
        self.product_detail = map.get('ProductDetail')
        self.owner_id = map.get('OwnerID')
        self.billing_item = map.get('BillingItem')
        self.list_price = map.get('ListPrice')
        self.list_price_unit = map.get('ListPriceUnit')
        self.usage = map.get('Usage')
        self.usage_unit = map.get('UsageUnit')
        self.deducted_by_resource_package = map.get('DeductedByResourcePackage')
        self.pretax_gross_amount = map.get('PretaxGrossAmount')
        self.invoice_discount = map.get('InvoiceDiscount')
        self.deducted_by_coupons = map.get('DeductedByCoupons')
        self.pretax_amount = map.get('PretaxAmount')
        self.deducted_by_cash_coupons = map.get('DeductedByCashCoupons')
        self.deducted_by_prepaid_card = map.get('DeductedByPrepaidCard')
        self.payment_amount = map.get('PaymentAmount')
        self.outstanding_amount = map.get('OutstandingAmount')
        self.currency = map.get('Currency')
        self.nick_name = map.get('NickName')
        self.resource_group = map.get('ResourceGroup')
        self.tag = map.get('Tag')
        self.instance_config = map.get('InstanceConfig')
        self.instance_spec = map.get('InstanceSpec')
        self.internet_ip = map.get('InternetIP')
        self.intranet_ip = map.get('IntranetIP')
        self.region = map.get('Region')
        self.zone = map.get('Zone')
        self.item = map.get('Item')
        self.service_period = map.get('ServicePeriod')
        self.billing_date = map.get('BillingDate')
        self.split_item_id = map.get('SplitItemID')
        self.split_item_name = map.get('SplitItemName')
        self.pip_code = map.get('PipCode')
        self.commodity_code = map.get('CommodityCode')
        return self


class QuerySplitItemBillResponseDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[QuerySplitItemBillResponseDataItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = QuerySplitItemBillResponseDataItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class QuerySplitItemBillResponseData(TeaModel):
    def __init__(self, billing_cycle=None, account_id=None, account_name=None, total_count=None, page_num=None,
                 page_size=None, items=None):
        self.billing_cycle = billing_cycle  # type: str
        self.account_id = account_id    # type: str
        self.account_name = account_name  # type: str
        self.total_count = total_count  # type: int
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.items = items              # type: QuerySplitItemBillResponseDataItems

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['AccountID'] = self.account_id
        result['AccountName'] = self.account_name
        result['TotalCount'] = self.total_count
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.account_id = map.get('AccountID')
        self.account_name = map.get('AccountName')
        self.total_count = map.get('TotalCount')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        if map.get('Items') is not None:
            temp_model = QuerySplitItemBillResponseDataItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class QueryRIUtilizationDetailRequest(TeaModel):
    def __init__(self, riinstance_id=None, instance_spec=None, ricommodity_code=None, deducted_instance_id=None,
                 start_time=None, end_time=None, page_num=None, page_size=None):
        self.riinstance_id = riinstance_id  # type: str
        self.instance_spec = instance_spec  # type: str
        self.ricommodity_code = ricommodity_code  # type: str
        self.deducted_instance_id = deducted_instance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.ricommodity_code, 'ricommodity_code')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['RIInstanceId'] = self.riinstance_id
        result['InstanceSpec'] = self.instance_spec
        result['RICommodityCode'] = self.ricommodity_code
        result['DeductedInstanceId'] = self.deducted_instance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.riinstance_id = map.get('RIInstanceId')
        self.instance_spec = map.get('InstanceSpec')
        self.ricommodity_code = map.get('RICommodityCode')
        self.deducted_instance_id = map.get('DeductedInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class QueryRIUtilizationDetailResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryRIUtilizationDetailResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryRIUtilizationDetailResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryRIUtilizationDetailResponseDataDetailListDetailList(TeaModel):
    def __init__(self, riinstance_id=None, instance_spec=None, deducted_instance_id=None,
                 deducted_commodity_code=None, deduct_date=None, deduct_hours=None, deducted_product_detail=None, deduct_quantity=None,
                 deduct_factor_total=None):
        self.riinstance_id = riinstance_id  # type: str
        self.instance_spec = instance_spec  # type: str
        self.deducted_instance_id = deducted_instance_id  # type: str
        self.deducted_commodity_code = deducted_commodity_code  # type: str
        self.deduct_date = deduct_date  # type: str
        self.deduct_hours = deduct_hours  # type: str
        self.deducted_product_detail = deducted_product_detail  # type: str
        self.deduct_quantity = deduct_quantity  # type: float
        self.deduct_factor_total = deduct_factor_total  # type: float

    def validate(self):
        self.validate_required(self.riinstance_id, 'riinstance_id')
        self.validate_required(self.instance_spec, 'instance_spec')
        self.validate_required(self.deducted_instance_id, 'deducted_instance_id')
        self.validate_required(self.deducted_commodity_code, 'deducted_commodity_code')
        self.validate_required(self.deduct_date, 'deduct_date')
        self.validate_required(self.deduct_hours, 'deduct_hours')
        self.validate_required(self.deducted_product_detail, 'deducted_product_detail')
        self.validate_required(self.deduct_quantity, 'deduct_quantity')
        self.validate_required(self.deduct_factor_total, 'deduct_factor_total')

    def to_map(self):
        result = {}
        result['RIInstanceId'] = self.riinstance_id
        result['InstanceSpec'] = self.instance_spec
        result['DeductedInstanceId'] = self.deducted_instance_id
        result['DeductedCommodityCode'] = self.deducted_commodity_code
        result['DeductDate'] = self.deduct_date
        result['DeductHours'] = self.deduct_hours
        result['DeductedProductDetail'] = self.deducted_product_detail
        result['DeductQuantity'] = self.deduct_quantity
        result['DeductFactorTotal'] = self.deduct_factor_total
        return result

    def from_map(self, map={}):
        self.riinstance_id = map.get('RIInstanceId')
        self.instance_spec = map.get('InstanceSpec')
        self.deducted_instance_id = map.get('DeductedInstanceId')
        self.deducted_commodity_code = map.get('DeductedCommodityCode')
        self.deduct_date = map.get('DeductDate')
        self.deduct_hours = map.get('DeductHours')
        self.deducted_product_detail = map.get('DeductedProductDetail')
        self.deduct_quantity = map.get('DeductQuantity')
        self.deduct_factor_total = map.get('DeductFactorTotal')
        return self


class QueryRIUtilizationDetailResponseDataDetailList(TeaModel):
    def __init__(self, detail_list=None):
        self.detail_list = detail_list  # type: List[QueryRIUtilizationDetailResponseDataDetailListDetailList]

    def validate(self):
        self.validate_required(self.detail_list, 'detail_list')
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DetailList'] = []
        if self.detail_list is not None:
            for k in self.detail_list:
                result['DetailList'].append(k.to_map() if k else None)
        else:
            result['DetailList'] = None
        return result

    def from_map(self, map={}):
        self.detail_list = []
        if map.get('DetailList') is not None:
            for k in map.get('DetailList'):
                temp_model = QueryRIUtilizationDetailResponseDataDetailListDetailList()
                self.detail_list.append(temp_model.from_map(k))
        else:
            self.detail_list = None
        return self


class QueryRIUtilizationDetailResponseData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_count=None, detail_list=None):
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.detail_list = detail_list  # type: QueryRIUtilizationDetailResponseDataDetailList

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.detail_list, 'detail_list')
        if self.detail_list:
            self.detail_list.validate()

    def to_map(self):
        result = {}
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.detail_list is not None:
            result['DetailList'] = self.detail_list.to_map()
        else:
            result['DetailList'] = None
        return result

    def from_map(self, map={}):
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('DetailList') is not None:
            temp_model = QueryRIUtilizationDetailResponseDataDetailList()
            self.detail_list = temp_model.from_map(map['DetailList'])
        else:
            self.detail_list = None
        return self


class QueryBillToOSSSubscriptionRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class QueryBillToOSSSubscriptionResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryBillToOSSSubscriptionResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryBillToOSSSubscriptionResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryBillToOSSSubscriptionResponseDataItemsItem(TeaModel):
    def __init__(self, subscribe_type=None, subscribe_bucket=None, bucket_owner_id=None, subscribe_time=None,
                 subscribe_language=None, mult_account_rel_subscribe=None):
        self.subscribe_type = subscribe_type  # type: str
        self.subscribe_bucket = subscribe_bucket  # type: str
        self.bucket_owner_id = bucket_owner_id  # type: int
        self.subscribe_time = subscribe_time  # type: str
        self.subscribe_language = subscribe_language  # type: str
        self.mult_account_rel_subscribe = mult_account_rel_subscribe  # type: str

    def validate(self):
        self.validate_required(self.subscribe_type, 'subscribe_type')
        self.validate_required(self.subscribe_bucket, 'subscribe_bucket')
        self.validate_required(self.bucket_owner_id, 'bucket_owner_id')
        self.validate_required(self.subscribe_time, 'subscribe_time')
        self.validate_required(self.subscribe_language, 'subscribe_language')
        self.validate_required(self.mult_account_rel_subscribe, 'mult_account_rel_subscribe')

    def to_map(self):
        result = {}
        result['SubscribeType'] = self.subscribe_type
        result['SubscribeBucket'] = self.subscribe_bucket
        result['BucketOwnerId'] = self.bucket_owner_id
        result['SubscribeTime'] = self.subscribe_time
        result['SubscribeLanguage'] = self.subscribe_language
        result['MultAccountRelSubscribe'] = self.mult_account_rel_subscribe
        return result

    def from_map(self, map={}):
        self.subscribe_type = map.get('SubscribeType')
        self.subscribe_bucket = map.get('SubscribeBucket')
        self.bucket_owner_id = map.get('BucketOwnerId')
        self.subscribe_time = map.get('SubscribeTime')
        self.subscribe_language = map.get('SubscribeLanguage')
        self.mult_account_rel_subscribe = map.get('MultAccountRelSubscribe')
        return self


class QueryBillToOSSSubscriptionResponseDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[QueryBillToOSSSubscriptionResponseDataItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = QueryBillToOSSSubscriptionResponseDataItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class QueryBillToOSSSubscriptionResponseData(TeaModel):
    def __init__(self, account_id=None, account_name=None, items=None):
        self.account_id = account_id    # type: str
        self.account_name = account_name  # type: str
        self.items = items              # type: QueryBillToOSSSubscriptionResponseDataItems

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['AccountID'] = self.account_id
        result['AccountName'] = self.account_name
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.account_id = map.get('AccountID')
        self.account_name = map.get('AccountName')
        if map.get('Items') is not None:
            temp_model = QueryBillToOSSSubscriptionResponseDataItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class QueryAccountBillRequest(TeaModel):
    def __init__(self, billing_cycle=None, page_num=None, page_size=None, owner_id=None, is_group_by_product=None,
                 product_code=None, bill_owner_id=None):
        self.billing_cycle = billing_cycle  # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.owner_id = owner_id        # type: int
        self.is_group_by_product = is_group_by_product  # type: bool
        self.product_code = product_code  # type: str
        self.bill_owner_id = bill_owner_id  # type: int

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['OwnerID'] = self.owner_id
        result['IsGroupByProduct'] = self.is_group_by_product
        result['ProductCode'] = self.product_code
        result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.owner_id = map.get('OwnerID')
        self.is_group_by_product = map.get('IsGroupByProduct')
        self.product_code = map.get('ProductCode')
        self.bill_owner_id = map.get('BillOwnerId')
        return self


class QueryAccountBillResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryAccountBillResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryAccountBillResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryAccountBillResponseDataItemsItem(TeaModel):
    def __init__(self, cost_unit=None, owner_id=None, pretax_gross_amount=None, invoice_discount=None,
                 deducted_by_coupons=None, pretax_amount=None, deducted_by_cash_coupons=None, deducted_by_prepaid_card=None,
                 payment_amount=None, outstanding_amount=None, currency=None, owner_name=None, product_code=None,
                 product_name=None, subscription_type=None, pip_code=None):
        self.cost_unit = cost_unit      # type: str
        self.owner_id = owner_id        # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.pretax_amount = pretax_amount  # type: float
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.payment_amount = payment_amount  # type: float
        self.outstanding_amount = outstanding_amount  # type: float
        self.currency = currency        # type: str
        self.owner_name = owner_name    # type: str
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str
        self.subscription_type = subscription_type  # type: str
        self.pip_code = pip_code        # type: str

    def validate(self):
        self.validate_required(self.cost_unit, 'cost_unit')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.pretax_gross_amount, 'pretax_gross_amount')
        self.validate_required(self.invoice_discount, 'invoice_discount')
        self.validate_required(self.deducted_by_coupons, 'deducted_by_coupons')
        self.validate_required(self.pretax_amount, 'pretax_amount')
        self.validate_required(self.deducted_by_cash_coupons, 'deducted_by_cash_coupons')
        self.validate_required(self.deducted_by_prepaid_card, 'deducted_by_prepaid_card')
        self.validate_required(self.payment_amount, 'payment_amount')
        self.validate_required(self.outstanding_amount, 'outstanding_amount')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.owner_name, 'owner_name')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_name, 'product_name')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.pip_code, 'pip_code')

    def to_map(self):
        result = {}
        result['CostUnit'] = self.cost_unit
        result['OwnerID'] = self.owner_id
        result['PretaxGrossAmount'] = self.pretax_gross_amount
        result['InvoiceDiscount'] = self.invoice_discount
        result['DeductedByCoupons'] = self.deducted_by_coupons
        result['PretaxAmount'] = self.pretax_amount
        result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        result['PaymentAmount'] = self.payment_amount
        result['OutstandingAmount'] = self.outstanding_amount
        result['Currency'] = self.currency
        result['OwnerName'] = self.owner_name
        result['ProductCode'] = self.product_code
        result['ProductName'] = self.product_name
        result['SubscriptionType'] = self.subscription_type
        result['PipCode'] = self.pip_code
        return result

    def from_map(self, map={}):
        self.cost_unit = map.get('CostUnit')
        self.owner_id = map.get('OwnerID')
        self.pretax_gross_amount = map.get('PretaxGrossAmount')
        self.invoice_discount = map.get('InvoiceDiscount')
        self.deducted_by_coupons = map.get('DeductedByCoupons')
        self.pretax_amount = map.get('PretaxAmount')
        self.deducted_by_cash_coupons = map.get('DeductedByCashCoupons')
        self.deducted_by_prepaid_card = map.get('DeductedByPrepaidCard')
        self.payment_amount = map.get('PaymentAmount')
        self.outstanding_amount = map.get('OutstandingAmount')
        self.currency = map.get('Currency')
        self.owner_name = map.get('OwnerName')
        self.product_code = map.get('ProductCode')
        self.product_name = map.get('ProductName')
        self.subscription_type = map.get('SubscriptionType')
        self.pip_code = map.get('PipCode')
        return self


class QueryAccountBillResponseDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[QueryAccountBillResponseDataItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = QueryAccountBillResponseDataItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class QueryAccountBillResponseData(TeaModel):
    def __init__(self, billing_cycle=None, account_id=None, account_name=None, total_count=None, page_num=None,
                 page_size=None, items=None):
        self.billing_cycle = billing_cycle  # type: str
        self.account_id = account_id    # type: str
        self.account_name = account_name  # type: str
        self.total_count = total_count  # type: int
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.items = items              # type: QueryAccountBillResponseDataItems

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['AccountID'] = self.account_id
        result['AccountName'] = self.account_name
        result['TotalCount'] = self.total_count
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.account_id = map.get('AccountID')
        self.account_name = map.get('AccountName')
        self.total_count = map.get('TotalCount')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        if map.get('Items') is not None:
            temp_model = QueryAccountBillResponseDataItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class CreateCostUnitRequest(TeaModel):
    def __init__(self, unit_entity_list=None):
        self.unit_entity_list = unit_entity_list  # type: List[CreateCostUnitRequestUnitEntityList]

    def validate(self):
        if self.unit_entity_list:
            for k in self.unit_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UnitEntityList'] = []
        if self.unit_entity_list is not None:
            for k in self.unit_entity_list:
                result['UnitEntityList'].append(k.to_map() if k else None)
        else:
            result['UnitEntityList'] = None
        return result

    def from_map(self, map={}):
        self.unit_entity_list = []
        if map.get('UnitEntityList') is not None:
            for k in map.get('UnitEntityList'):
                temp_model = CreateCostUnitRequestUnitEntityList()
                self.unit_entity_list.append(temp_model.from_map(k))
        else:
            self.unit_entity_list = None
        return self


class CreateCostUnitRequestUnitEntityList(TeaModel):
    def __init__(self, owner_uid=None, parent_unit_id=None, unit_name=None):
        self.owner_uid = owner_uid      # type: int
        self.parent_unit_id = parent_unit_id  # type: int
        self.unit_name = unit_name      # type: str

    def validate(self):
        self.validate_required(self.owner_uid, 'owner_uid')
        self.validate_required(self.parent_unit_id, 'parent_unit_id')
        self.validate_required(self.unit_name, 'unit_name')

    def to_map(self):
        result = {}
        result['OwnerUid'] = self.owner_uid
        result['ParentUnitId'] = self.parent_unit_id
        result['UnitName'] = self.unit_name
        return result

    def from_map(self, map={}):
        self.owner_uid = map.get('OwnerUid')
        self.parent_unit_id = map.get('ParentUnitId')
        self.unit_name = map.get('UnitName')
        return self


class CreateCostUnitResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: CreateCostUnitResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = CreateCostUnitResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class CreateCostUnitResponseDataCostUnitDtoList(TeaModel):
    def __init__(self, owner_uid=None, parent_unit_id=None, unit_id=None, unit_name=None):
        self.owner_uid = owner_uid      # type: int
        self.parent_unit_id = parent_unit_id  # type: int
        self.unit_id = unit_id          # type: int
        self.unit_name = unit_name      # type: str

    def validate(self):
        self.validate_required(self.owner_uid, 'owner_uid')
        self.validate_required(self.parent_unit_id, 'parent_unit_id')
        self.validate_required(self.unit_id, 'unit_id')
        self.validate_required(self.unit_name, 'unit_name')

    def to_map(self):
        result = {}
        result['OwnerUid'] = self.owner_uid
        result['ParentUnitId'] = self.parent_unit_id
        result['UnitId'] = self.unit_id
        result['UnitName'] = self.unit_name
        return result

    def from_map(self, map={}):
        self.owner_uid = map.get('OwnerUid')
        self.parent_unit_id = map.get('ParentUnitId')
        self.unit_id = map.get('UnitId')
        self.unit_name = map.get('UnitName')
        return self


class CreateCostUnitResponseData(TeaModel):
    def __init__(self, cost_unit_dto_list=None):
        self.cost_unit_dto_list = cost_unit_dto_list  # type: List[CreateCostUnitResponseDataCostUnitDtoList]

    def validate(self):
        self.validate_required(self.cost_unit_dto_list, 'cost_unit_dto_list')
        if self.cost_unit_dto_list:
            for k in self.cost_unit_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CostUnitDtoList'] = []
        if self.cost_unit_dto_list is not None:
            for k in self.cost_unit_dto_list:
                result['CostUnitDtoList'].append(k.to_map() if k else None)
        else:
            result['CostUnitDtoList'] = None
        return result

    def from_map(self, map={}):
        self.cost_unit_dto_list = []
        if map.get('CostUnitDtoList') is not None:
            for k in map.get('CostUnitDtoList'):
                temp_model = CreateCostUnitResponseDataCostUnitDtoList()
                self.cost_unit_dto_list.append(temp_model.from_map(k))
        else:
            self.cost_unit_dto_list = None
        return self


class ModifyCostUnitRequest(TeaModel):
    def __init__(self, unit_entity_list=None):
        self.unit_entity_list = unit_entity_list  # type: List[ModifyCostUnitRequestUnitEntityList]

    def validate(self):
        if self.unit_entity_list:
            for k in self.unit_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UnitEntityList'] = []
        if self.unit_entity_list is not None:
            for k in self.unit_entity_list:
                result['UnitEntityList'].append(k.to_map() if k else None)
        else:
            result['UnitEntityList'] = None
        return result

    def from_map(self, map={}):
        self.unit_entity_list = []
        if map.get('UnitEntityList') is not None:
            for k in map.get('UnitEntityList'):
                temp_model = ModifyCostUnitRequestUnitEntityList()
                self.unit_entity_list.append(temp_model.from_map(k))
        else:
            self.unit_entity_list = None
        return self


class ModifyCostUnitRequestUnitEntityList(TeaModel):
    def __init__(self, owner_uid=None, unit_id=None, new_unit_name=None):
        self.owner_uid = owner_uid      # type: int
        self.unit_id = unit_id          # type: int
        self.new_unit_name = new_unit_name  # type: str

    def validate(self):
        self.validate_required(self.owner_uid, 'owner_uid')
        self.validate_required(self.unit_id, 'unit_id')
        self.validate_required(self.new_unit_name, 'new_unit_name')

    def to_map(self):
        result = {}
        result['OwnerUid'] = self.owner_uid
        result['UnitId'] = self.unit_id
        result['NewUnitName'] = self.new_unit_name
        return result

    def from_map(self, map={}):
        self.owner_uid = map.get('OwnerUid')
        self.unit_id = map.get('UnitId')
        self.new_unit_name = map.get('NewUnitName')
        return self


class ModifyCostUnitResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: List[ModifyCostUnitResponseData]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ModifyCostUnitResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ModifyCostUnitResponseData(TeaModel):
    def __init__(self, owner_uid=None, unit_id=None, is_success=None):
        self.owner_uid = owner_uid      # type: int
        self.unit_id = unit_id          # type: int
        self.is_success = is_success    # type: bool

    def validate(self):
        self.validate_required(self.owner_uid, 'owner_uid')
        self.validate_required(self.unit_id, 'unit_id')
        self.validate_required(self.is_success, 'is_success')

    def to_map(self):
        result = {}
        result['OwnerUid'] = self.owner_uid
        result['UnitId'] = self.unit_id
        result['IsSuccess'] = self.is_success
        return result

    def from_map(self, map={}):
        self.owner_uid = map.get('OwnerUid')
        self.unit_id = map.get('UnitId')
        self.is_success = map.get('IsSuccess')
        return self


class QueryCostUnitRequest(TeaModel):
    def __init__(self, owner_uid=None, parent_unit_id=None, page_num=None, page_size=None):
        self.owner_uid = owner_uid      # type: int
        self.parent_unit_id = parent_unit_id  # type: int
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.owner_uid, 'owner_uid')
        self.validate_required(self.parent_unit_id, 'parent_unit_id')

    def to_map(self):
        result = {}
        result['OwnerUid'] = self.owner_uid
        result['ParentUnitId'] = self.parent_unit_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.owner_uid = map.get('OwnerUid')
        self.parent_unit_id = map.get('ParentUnitId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class QueryCostUnitResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryCostUnitResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryCostUnitResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryCostUnitResponseDataCostUnitDtoList(TeaModel):
    def __init__(self, owner_uid=None, parent_unit_id=None, unit_id=None, unit_name=None):
        self.owner_uid = owner_uid      # type: int
        self.parent_unit_id = parent_unit_id  # type: int
        self.unit_id = unit_id          # type: int
        self.unit_name = unit_name      # type: str

    def validate(self):
        self.validate_required(self.owner_uid, 'owner_uid')
        self.validate_required(self.parent_unit_id, 'parent_unit_id')
        self.validate_required(self.unit_id, 'unit_id')
        self.validate_required(self.unit_name, 'unit_name')

    def to_map(self):
        result = {}
        result['OwnerUid'] = self.owner_uid
        result['ParentUnitId'] = self.parent_unit_id
        result['UnitId'] = self.unit_id
        result['UnitName'] = self.unit_name
        return result

    def from_map(self, map={}):
        self.owner_uid = map.get('OwnerUid')
        self.parent_unit_id = map.get('ParentUnitId')
        self.unit_id = map.get('UnitId')
        self.unit_name = map.get('UnitName')
        return self


class QueryCostUnitResponseData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_count=None, cost_unit_dto_list=None):
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.cost_unit_dto_list = cost_unit_dto_list  # type: List[QueryCostUnitResponseDataCostUnitDtoList]

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.cost_unit_dto_list, 'cost_unit_dto_list')
        if self.cost_unit_dto_list:
            for k in self.cost_unit_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['CostUnitDtoList'] = []
        if self.cost_unit_dto_list is not None:
            for k in self.cost_unit_dto_list:
                result['CostUnitDtoList'].append(k.to_map() if k else None)
        else:
            result['CostUnitDtoList'] = None
        return result

    def from_map(self, map={}):
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.cost_unit_dto_list = []
        if map.get('CostUnitDtoList') is not None:
            for k in map.get('CostUnitDtoList'):
                temp_model = QueryCostUnitResponseDataCostUnitDtoList()
                self.cost_unit_dto_list.append(temp_model.from_map(k))
        else:
            self.cost_unit_dto_list = None
        return self


class DeleteCostUnitRequest(TeaModel):
    def __init__(self, owner_uid=None, unit_id=None):
        self.owner_uid = owner_uid      # type: int
        self.unit_id = unit_id          # type: int

    def validate(self):
        self.validate_required(self.owner_uid, 'owner_uid')
        self.validate_required(self.unit_id, 'unit_id')

    def to_map(self):
        result = {}
        result['OwnerUid'] = self.owner_uid
        result['UnitId'] = self.unit_id
        return result

    def from_map(self, map={}):
        self.owner_uid = map.get('OwnerUid')
        self.unit_id = map.get('UnitId')
        return self


class DeleteCostUnitResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: DeleteCostUnitResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = DeleteCostUnitResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DeleteCostUnitResponseData(TeaModel):
    def __init__(self, owner_uid=None, unit_id=None, is_success=None):
        self.owner_uid = owner_uid      # type: int
        self.unit_id = unit_id          # type: int
        self.is_success = is_success    # type: bool

    def validate(self):
        self.validate_required(self.owner_uid, 'owner_uid')
        self.validate_required(self.unit_id, 'unit_id')
        self.validate_required(self.is_success, 'is_success')

    def to_map(self):
        result = {}
        result['OwnerUid'] = self.owner_uid
        result['UnitId'] = self.unit_id
        result['IsSuccess'] = self.is_success
        return result

    def from_map(self, map={}):
        self.owner_uid = map.get('OwnerUid')
        self.unit_id = map.get('UnitId')
        self.is_success = map.get('IsSuccess')
        return self


class AllocateCostUnitResourceRequest(TeaModel):
    def __init__(self, from_unit_user_id=None, from_unit_id=None, resource_instance_list=None,
                 to_unit_user_id=None, to_unit_id=None):
        self.from_unit_user_id = from_unit_user_id  # type: int
        self.from_unit_id = from_unit_id  # type: int
        self.resource_instance_list = resource_instance_list  # type: List[AllocateCostUnitResourceRequestResourceInstanceList]
        self.to_unit_user_id = to_unit_user_id  # type: int
        self.to_unit_id = to_unit_id    # type: int

    def validate(self):
        self.validate_required(self.from_unit_user_id, 'from_unit_user_id')
        self.validate_required(self.from_unit_id, 'from_unit_id')
        self.validate_required(self.resource_instance_list, 'resource_instance_list')
        if self.resource_instance_list:
            for k in self.resource_instance_list:
                if k:
                    k.validate()
        self.validate_required(self.to_unit_user_id, 'to_unit_user_id')
        self.validate_required(self.to_unit_id, 'to_unit_id')

    def to_map(self):
        result = {}
        result['FromUnitUserId'] = self.from_unit_user_id
        result['FromUnitId'] = self.from_unit_id
        result['ResourceInstanceList'] = []
        if self.resource_instance_list is not None:
            for k in self.resource_instance_list:
                result['ResourceInstanceList'].append(k.to_map() if k else None)
        else:
            result['ResourceInstanceList'] = None
        result['ToUnitUserId'] = self.to_unit_user_id
        result['ToUnitId'] = self.to_unit_id
        return result

    def from_map(self, map={}):
        self.from_unit_user_id = map.get('FromUnitUserId')
        self.from_unit_id = map.get('FromUnitId')
        self.resource_instance_list = []
        if map.get('ResourceInstanceList') is not None:
            for k in map.get('ResourceInstanceList'):
                temp_model = AllocateCostUnitResourceRequestResourceInstanceList()
                self.resource_instance_list.append(temp_model.from_map(k))
        else:
            self.resource_instance_list = None
        self.to_unit_user_id = map.get('ToUnitUserId')
        self.to_unit_id = map.get('ToUnitId')
        return self


class AllocateCostUnitResourceRequestResourceInstanceList(TeaModel):
    def __init__(self, resource_user_id=None, resource_id=None, commodity_code=None, apportion_code=None):
        self.resource_user_id = resource_user_id  # type: int
        self.resource_id = resource_id  # type: str
        self.commodity_code = commodity_code  # type: str
        self.apportion_code = apportion_code  # type: str

    def validate(self):
        self.validate_required(self.resource_user_id, 'resource_user_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.commodity_code, 'commodity_code')

    def to_map(self):
        result = {}
        result['ResourceUserId'] = self.resource_user_id
        result['ResourceId'] = self.resource_id
        result['CommodityCode'] = self.commodity_code
        result['ApportionCode'] = self.apportion_code
        return result

    def from_map(self, map={}):
        self.resource_user_id = map.get('ResourceUserId')
        self.resource_id = map.get('ResourceId')
        self.commodity_code = map.get('CommodityCode')
        self.apportion_code = map.get('ApportionCode')
        return self


class AllocateCostUnitResourceResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: AllocateCostUnitResourceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = AllocateCostUnitResourceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class AllocateCostUnitResourceResponseData(TeaModel):
    def __init__(self, to_unit_user_id=None, to_unit_id=None, is_success=None):
        self.to_unit_user_id = to_unit_user_id  # type: int
        self.to_unit_id = to_unit_id    # type: int
        self.is_success = is_success    # type: bool

    def validate(self):
        self.validate_required(self.to_unit_user_id, 'to_unit_user_id')
        self.validate_required(self.to_unit_id, 'to_unit_id')
        self.validate_required(self.is_success, 'is_success')

    def to_map(self):
        result = {}
        result['ToUnitUserId'] = self.to_unit_user_id
        result['ToUnitId'] = self.to_unit_id
        result['IsSuccess'] = self.is_success
        return result

    def from_map(self, map={}):
        self.to_unit_user_id = map.get('ToUnitUserId')
        self.to_unit_id = map.get('ToUnitId')
        self.is_success = map.get('IsSuccess')
        return self


class QueryCostUnitResourceRequest(TeaModel):
    def __init__(self, owner_uid=None, unit_id=None, page_num=None, page_size=None):
        self.owner_uid = owner_uid      # type: int
        self.unit_id = unit_id          # type: int
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.owner_uid, 'owner_uid')
        self.validate_required(self.unit_id, 'unit_id')

    def to_map(self):
        result = {}
        result['OwnerUid'] = self.owner_uid
        result['UnitId'] = self.unit_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.owner_uid = map.get('OwnerUid')
        self.unit_id = map.get('UnitId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class QueryCostUnitResourceResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryCostUnitResourceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryCostUnitResourceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryCostUnitResourceResponseDataResourceInstanceDtoList(TeaModel):
    def __init__(self, resource_user_id=None, resource_id=None, commodity_code=None, resource_user_name=None,
                 commodity_name=None, resource_group=None, resource_tag=None, resource_nick=None, resource_type=None,
                 resource_status=None, related_resources=None, apportion_code=None, apportion_name=None):
        self.resource_user_id = resource_user_id  # type: int
        self.resource_id = resource_id  # type: str
        self.commodity_code = commodity_code  # type: str
        self.resource_user_name = resource_user_name  # type: str
        self.commodity_name = commodity_name  # type: str
        self.resource_group = resource_group  # type: str
        self.resource_tag = resource_tag  # type: str
        self.resource_nick = resource_nick  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_status = resource_status  # type: str
        self.related_resources = related_resources  # type: str
        self.apportion_code = apportion_code  # type: str
        self.apportion_name = apportion_name  # type: str

    def validate(self):
        self.validate_required(self.resource_user_id, 'resource_user_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.commodity_code, 'commodity_code')
        self.validate_required(self.resource_user_name, 'resource_user_name')
        self.validate_required(self.commodity_name, 'commodity_name')
        self.validate_required(self.resource_group, 'resource_group')
        self.validate_required(self.resource_tag, 'resource_tag')
        self.validate_required(self.resource_nick, 'resource_nick')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_status, 'resource_status')
        self.validate_required(self.related_resources, 'related_resources')
        self.validate_required(self.apportion_code, 'apportion_code')
        self.validate_required(self.apportion_name, 'apportion_name')

    def to_map(self):
        result = {}
        result['ResourceUserId'] = self.resource_user_id
        result['ResourceId'] = self.resource_id
        result['CommodityCode'] = self.commodity_code
        result['ResourceUserName'] = self.resource_user_name
        result['CommodityName'] = self.commodity_name
        result['ResourceGroup'] = self.resource_group
        result['ResourceTag'] = self.resource_tag
        result['ResourceNick'] = self.resource_nick
        result['ResourceType'] = self.resource_type
        result['ResourceStatus'] = self.resource_status
        result['RelatedResources'] = self.related_resources
        result['ApportionCode'] = self.apportion_code
        result['ApportionName'] = self.apportion_name
        return result

    def from_map(self, map={}):
        self.resource_user_id = map.get('ResourceUserId')
        self.resource_id = map.get('ResourceId')
        self.commodity_code = map.get('CommodityCode')
        self.resource_user_name = map.get('ResourceUserName')
        self.commodity_name = map.get('CommodityName')
        self.resource_group = map.get('ResourceGroup')
        self.resource_tag = map.get('ResourceTag')
        self.resource_nick = map.get('ResourceNick')
        self.resource_type = map.get('ResourceType')
        self.resource_status = map.get('ResourceStatus')
        self.related_resources = map.get('RelatedResources')
        self.apportion_code = map.get('ApportionCode')
        self.apportion_name = map.get('ApportionName')
        return self


class QueryCostUnitResourceResponseDataCostUnit(TeaModel):
    def __init__(self, owner_uid=None, parent_unit_id=None, unit_id=None, unit_name=None):
        self.owner_uid = owner_uid      # type: int
        self.parent_unit_id = parent_unit_id  # type: int
        self.unit_id = unit_id          # type: int
        self.unit_name = unit_name      # type: str

    def validate(self):
        self.validate_required(self.owner_uid, 'owner_uid')
        self.validate_required(self.parent_unit_id, 'parent_unit_id')
        self.validate_required(self.unit_id, 'unit_id')
        self.validate_required(self.unit_name, 'unit_name')

    def to_map(self):
        result = {}
        result['OwnerUid'] = self.owner_uid
        result['ParentUnitId'] = self.parent_unit_id
        result['UnitId'] = self.unit_id
        result['UnitName'] = self.unit_name
        return result

    def from_map(self, map={}):
        self.owner_uid = map.get('OwnerUid')
        self.parent_unit_id = map.get('ParentUnitId')
        self.unit_id = map.get('UnitId')
        self.unit_name = map.get('UnitName')
        return self


class QueryCostUnitResourceResponseDataCostUnitStatisInfo(TeaModel):
    def __init__(self, resource_count=None, resource_group_count=None, sub_unit_count=None, user_count=None,
                 total_resource_count=None, total_user_count=None, total_resource_group_count=None):
        self.resource_count = resource_count  # type: int
        self.resource_group_count = resource_group_count  # type: int
        self.sub_unit_count = sub_unit_count  # type: int
        self.user_count = user_count    # type: int
        self.total_resource_count = total_resource_count  # type: int
        self.total_user_count = total_user_count  # type: int
        self.total_resource_group_count = total_resource_group_count  # type: int

    def validate(self):
        self.validate_required(self.resource_count, 'resource_count')
        self.validate_required(self.resource_group_count, 'resource_group_count')
        self.validate_required(self.sub_unit_count, 'sub_unit_count')
        self.validate_required(self.user_count, 'user_count')
        self.validate_required(self.total_resource_count, 'total_resource_count')
        self.validate_required(self.total_user_count, 'total_user_count')
        self.validate_required(self.total_resource_group_count, 'total_resource_group_count')

    def to_map(self):
        result = {}
        result['ResourceCount'] = self.resource_count
        result['ResourceGroupCount'] = self.resource_group_count
        result['SubUnitCount'] = self.sub_unit_count
        result['UserCount'] = self.user_count
        result['TotalResourceCount'] = self.total_resource_count
        result['TotalUserCount'] = self.total_user_count
        result['TotalResourceGroupCount'] = self.total_resource_group_count
        return result

    def from_map(self, map={}):
        self.resource_count = map.get('ResourceCount')
        self.resource_group_count = map.get('ResourceGroupCount')
        self.sub_unit_count = map.get('SubUnitCount')
        self.user_count = map.get('UserCount')
        self.total_resource_count = map.get('TotalResourceCount')
        self.total_user_count = map.get('TotalUserCount')
        self.total_resource_group_count = map.get('TotalResourceGroupCount')
        return self


class QueryCostUnitResourceResponseData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_count=None, resource_instance_dto_list=None,
                 cost_unit=None, cost_unit_statis_info=None):
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.resource_instance_dto_list = resource_instance_dto_list  # type: List[QueryCostUnitResourceResponseDataResourceInstanceDtoList]
        self.cost_unit = cost_unit      # type: QueryCostUnitResourceResponseDataCostUnit
        self.cost_unit_statis_info = cost_unit_statis_info  # type: QueryCostUnitResourceResponseDataCostUnitStatisInfo

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.resource_instance_dto_list, 'resource_instance_dto_list')
        if self.resource_instance_dto_list:
            for k in self.resource_instance_dto_list:
                if k:
                    k.validate()
        self.validate_required(self.cost_unit, 'cost_unit')
        if self.cost_unit:
            self.cost_unit.validate()
        self.validate_required(self.cost_unit_statis_info, 'cost_unit_statis_info')
        if self.cost_unit_statis_info:
            self.cost_unit_statis_info.validate()

    def to_map(self):
        result = {}
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['ResourceInstanceDtoList'] = []
        if self.resource_instance_dto_list is not None:
            for k in self.resource_instance_dto_list:
                result['ResourceInstanceDtoList'].append(k.to_map() if k else None)
        else:
            result['ResourceInstanceDtoList'] = None
        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit.to_map()
        else:
            result['CostUnit'] = None
        if self.cost_unit_statis_info is not None:
            result['CostUnitStatisInfo'] = self.cost_unit_statis_info.to_map()
        else:
            result['CostUnitStatisInfo'] = None
        return result

    def from_map(self, map={}):
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.resource_instance_dto_list = []
        if map.get('ResourceInstanceDtoList') is not None:
            for k in map.get('ResourceInstanceDtoList'):
                temp_model = QueryCostUnitResourceResponseDataResourceInstanceDtoList()
                self.resource_instance_dto_list.append(temp_model.from_map(k))
        else:
            self.resource_instance_dto_list = None
        if map.get('CostUnit') is not None:
            temp_model = QueryCostUnitResourceResponseDataCostUnit()
            self.cost_unit = temp_model.from_map(map['CostUnit'])
        else:
            self.cost_unit = None
        if map.get('CostUnitStatisInfo') is not None:
            temp_model = QueryCostUnitResourceResponseDataCostUnitStatisInfo()
            self.cost_unit_statis_info = temp_model.from_map(map['CostUnitStatisInfo'])
        else:
            self.cost_unit_statis_info = None
        return self


class RenewResourcePackageRequest(TeaModel):
    def __init__(self, instance_id=None, effective_date=None, duration=None, pricing_cycle=None):
        self.instance_id = instance_id  # type: str
        self.effective_date = effective_date  # type: str
        self.duration = duration        # type: int
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.pricing_cycle, 'pricing_cycle')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['EffectiveDate'] = self.effective_date
        result['Duration'] = self.duration
        result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.effective_date = map.get('EffectiveDate')
        self.duration = map.get('Duration')
        self.pricing_cycle = map.get('PricingCycle')
        return self


class RenewResourcePackageResponse(TeaModel):
    def __init__(self, request_id=None, order_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.order_id = order_id        # type: int
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: RenewResourcePackageResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrderId'] = self.order_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.order_id = map.get('OrderId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = RenewResourcePackageResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RenewResourcePackageResponseData(TeaModel):
    def __init__(self, order_id=None, instance_id=None):
        self.order_id = order_id        # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['OrderId'] = self.order_id
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.order_id = map.get('OrderId')
        self.instance_id = map.get('InstanceId')
        return self


class UpgradeResourcePackageRequest(TeaModel):
    def __init__(self, instance_id=None, effective_date=None, specification=None):
        self.instance_id = instance_id  # type: str
        self.effective_date = effective_date  # type: str
        self.specification = specification  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['EffectiveDate'] = self.effective_date
        result['Specification'] = self.specification
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.effective_date = map.get('EffectiveDate')
        self.specification = map.get('Specification')
        return self


class UpgradeResourcePackageResponse(TeaModel):
    def __init__(self, request_id=None, order_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.order_id = order_id        # type: int
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: UpgradeResourcePackageResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrderId'] = self.order_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.order_id = map.get('OrderId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = UpgradeResourcePackageResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class UpgradeResourcePackageResponseData(TeaModel):
    def __init__(self, order_id=None, instance_id=None):
        self.order_id = order_id        # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['OrderId'] = self.order_id
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.order_id = map.get('OrderId')
        self.instance_id = map.get('InstanceId')
        return self


class CreateAgAccountRequest(TeaModel):
    def __init__(self, login_email=None, account_attr=None, enterprise_name=None, first_name=None, last_name=None,
                 nation_code=None, province_name=None, city_name=None, postcode=None):
        self.login_email = login_email  # type: str
        self.account_attr = account_attr  # type: str
        self.enterprise_name = enterprise_name  # type: str
        self.first_name = first_name    # type: str
        self.last_name = last_name      # type: str
        self.nation_code = nation_code  # type: str
        self.province_name = province_name  # type: str
        self.city_name = city_name      # type: str
        self.postcode = postcode        # type: str

    def validate(self):
        self.validate_required(self.login_email, 'login_email')

    def to_map(self):
        result = {}
        result['LoginEmail'] = self.login_email
        result['AccountAttr'] = self.account_attr
        result['EnterpriseName'] = self.enterprise_name
        result['FirstName'] = self.first_name
        result['LastName'] = self.last_name
        result['NationCode'] = self.nation_code
        result['ProvinceName'] = self.province_name
        result['CityName'] = self.city_name
        result['Postcode'] = self.postcode
        return result

    def from_map(self, map={}):
        self.login_email = map.get('LoginEmail')
        self.account_attr = map.get('AccountAttr')
        self.enterprise_name = map.get('EnterpriseName')
        self.first_name = map.get('FirstName')
        self.last_name = map.get('LastName')
        self.nation_code = map.get('NationCode')
        self.province_name = map.get('ProvinceName')
        self.city_name = map.get('CityName')
        self.postcode = map.get('Postcode')
        return self


class CreateAgAccountResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None, ag_relation_dto=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool
        self.ag_relation_dto = ag_relation_dto  # type: CreateAgAccountResponseAgRelationDto

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.ag_relation_dto, 'ag_relation_dto')
        if self.ag_relation_dto:
            self.ag_relation_dto.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        if self.ag_relation_dto is not None:
            result['AgRelationDto'] = self.ag_relation_dto.to_map()
        else:
            result['AgRelationDto'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        if map.get('AgRelationDto') is not None:
            temp_model = CreateAgAccountResponseAgRelationDto()
            self.ag_relation_dto = temp_model.from_map(map['AgRelationDto'])
        else:
            self.ag_relation_dto = None
        return self


class CreateAgAccountResponseAgRelationDto(TeaModel):
    def __init__(self, pk=None, type=None, mpk=None, ram_admin_role_name=None):
        self.pk = pk                    # type: str
        self.type = type                # type: str
        self.mpk = mpk                  # type: str
        self.ram_admin_role_name = ram_admin_role_name  # type: str

    def validate(self):
        self.validate_required(self.pk, 'pk')
        self.validate_required(self.type, 'type')
        self.validate_required(self.mpk, 'mpk')
        self.validate_required(self.ram_admin_role_name, 'ram_admin_role_name')

    def to_map(self):
        result = {}
        result['Pk'] = self.pk
        result['Type'] = self.type
        result['Mpk'] = self.mpk
        result['RamAdminRoleName'] = self.ram_admin_role_name
        return result

    def from_map(self, map={}):
        self.pk = map.get('Pk')
        self.type = map.get('Type')
        self.mpk = map.get('Mpk')
        self.ram_admin_role_name = map.get('RamAdminRoleName')
        return self


class GetCustomerAccountInfoRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetCustomerAccountInfoResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: GetCustomerAccountInfoResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = GetCustomerAccountInfoResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetCustomerAccountInfoResponseData(TeaModel):
    def __init__(self, login_email=None, account_type=None, mpk=None, hosting_status=None, credit_limit_status=None,
                 is_certified=None):
        self.login_email = login_email  # type: str
        self.account_type = account_type  # type: str
        self.mpk = mpk                  # type: int
        self.hosting_status = hosting_status  # type: str
        self.credit_limit_status = credit_limit_status  # type: str
        self.is_certified = is_certified  # type: bool

    def validate(self):
        self.validate_required(self.login_email, 'login_email')
        self.validate_required(self.account_type, 'account_type')
        self.validate_required(self.mpk, 'mpk')
        self.validate_required(self.hosting_status, 'hosting_status')
        self.validate_required(self.credit_limit_status, 'credit_limit_status')
        self.validate_required(self.is_certified, 'is_certified')

    def to_map(self):
        result = {}
        result['LoginEmail'] = self.login_email
        result['AccountType'] = self.account_type
        result['Mpk'] = self.mpk
        result['HostingStatus'] = self.hosting_status
        result['CreditLimitStatus'] = self.credit_limit_status
        result['IsCertified'] = self.is_certified
        return result

    def from_map(self, map={}):
        self.login_email = map.get('LoginEmail')
        self.account_type = map.get('AccountType')
        self.mpk = map.get('Mpk')
        self.hosting_status = map.get('HostingStatus')
        self.credit_limit_status = map.get('CreditLimitStatus')
        self.is_certified = map.get('IsCertified')
        return self


class GetCustomerListRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetCustomerListResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: GetCustomerListResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = GetCustomerListResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetCustomerListResponseData(TeaModel):
    def __init__(self, uid_list=None):
        self.uid_list = uid_list        # type: List[str]

    def validate(self):
        self.validate_required(self.uid_list, 'uid_list')

    def to_map(self):
        result = {}
        result['UidList'] = self.uid_list
        return result

    def from_map(self, map={}):
        self.uid_list = map.get('UidList')
        return self


class ChangeResellerConsumeAmountRequest(TeaModel):
    def __init__(self, adjust_type=None, amount=None, currency=None, business_type=None, source=None,
                 out_biz_id=None, extend_map=None):
        self.adjust_type = adjust_type  # type: str
        self.amount = amount            # type: str
        self.currency = currency        # type: str
        self.business_type = business_type  # type: str
        self.source = source            # type: str
        self.out_biz_id = out_biz_id    # type: str
        self.extend_map = extend_map    # type: str

    def validate(self):
        self.validate_required(self.adjust_type, 'adjust_type')
        self.validate_required(self.amount, 'amount')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.source, 'source')
        self.validate_required(self.out_biz_id, 'out_biz_id')

    def to_map(self):
        result = {}
        result['AdjustType'] = self.adjust_type
        result['Amount'] = self.amount
        result['Currency'] = self.currency
        result['BusinessType'] = self.business_type
        result['Source'] = self.source
        result['OutBizId'] = self.out_biz_id
        result['ExtendMap'] = self.extend_map
        return result

    def from_map(self, map={}):
        self.adjust_type = map.get('AdjustType')
        self.amount = map.get('Amount')
        self.currency = map.get('Currency')
        self.business_type = map.get('BusinessType')
        self.source = map.get('Source')
        self.out_biz_id = map.get('OutBizId')
        self.extend_map = map.get('ExtendMap')
        return self


class ChangeResellerConsumeAmountResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class SetResellerUserStatusRequest(TeaModel):
    def __init__(self, status=None, business_type=None):
        self.status = status            # type: str
        self.business_type = business_type  # type: str

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.business_type, 'business_type')

    def to_map(self):
        result = {}
        result['Status'] = self.status
        result['BusinessType'] = self.business_type
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        self.business_type = map.get('BusinessType')
        return self


class SetResellerUserStatusResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class CreateResellerUserQuotaRequest(TeaModel):
    def __init__(self, amount=None, currency=None, out_biz_id=None):
        self.amount = amount            # type: str
        self.currency = currency        # type: str
        self.out_biz_id = out_biz_id    # type: str

    def validate(self):
        self.validate_required(self.amount, 'amount')
        self.validate_required(self.currency, 'currency')

    def to_map(self):
        result = {}
        result['Amount'] = self.amount
        result['Currency'] = self.currency
        result['OutBizId'] = self.out_biz_id
        return result

    def from_map(self, map={}):
        self.amount = map.get('Amount')
        self.currency = map.get('Currency')
        self.out_biz_id = map.get('OutBizId')
        return self


class CreateResellerUserQuotaResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class SetResellerUserQuotaRequest(TeaModel):
    def __init__(self, amount=None, currency=None, out_biz_id=None):
        self.amount = amount            # type: str
        self.currency = currency        # type: str
        self.out_biz_id = out_biz_id    # type: str

    def validate(self):
        self.validate_required(self.amount, 'amount')

    def to_map(self):
        result = {}
        result['Amount'] = self.amount
        result['Currency'] = self.currency
        result['OutBizId'] = self.out_biz_id
        return result

    def from_map(self, map={}):
        self.amount = map.get('Amount')
        self.currency = map.get('Currency')
        self.out_biz_id = map.get('OutBizId')
        return self


class SetResellerUserQuotaResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class QueryResellerAvailableQuotaRequest(TeaModel):
    def __init__(self, item_codes=None):
        self.item_codes = item_codes    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ItemCodes'] = self.item_codes
        return result

    def from_map(self, map={}):
        self.item_codes = map.get('ItemCodes')
        return self


class QueryResellerAvailableQuotaResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class SetResellerUserAlarmThresholdRequest(TeaModel):
    def __init__(self, alarm_type=None, alarm_thresholds=None):
        self.alarm_type = alarm_type    # type: str
        self.alarm_thresholds = alarm_thresholds  # type: str

    def validate(self):
        self.validate_required(self.alarm_type, 'alarm_type')

    def to_map(self):
        result = {}
        result['AlarmType'] = self.alarm_type
        result['AlarmThresholds'] = self.alarm_thresholds
        return result

    def from_map(self, map={}):
        self.alarm_type = map.get('AlarmType')
        self.alarm_thresholds = map.get('AlarmThresholds')
        return self


class SetResellerUserAlarmThresholdResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class QueryAccountTransactionsRequest(TeaModel):
    def __init__(self, transaction_number=None, record_id=None, transaction_channel_sn=None,
                 create_time_start=None, create_time_end=None, page_num=None, page_size=None):
        self.transaction_number = transaction_number  # type: str
        self.record_id = record_id      # type: str
        self.transaction_channel_sn = transaction_channel_sn  # type: str
        self.create_time_start = create_time_start  # type: str
        self.create_time_end = create_time_end  # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['TransactionNumber'] = self.transaction_number
        result['RecordID'] = self.record_id
        result['TransactionChannelSN'] = self.transaction_channel_sn
        result['CreateTimeStart'] = self.create_time_start
        result['CreateTimeEnd'] = self.create_time_end
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.transaction_number = map.get('TransactionNumber')
        self.record_id = map.get('RecordID')
        self.transaction_channel_sn = map.get('TransactionChannelSN')
        self.create_time_start = map.get('CreateTimeStart')
        self.create_time_end = map.get('CreateTimeEnd')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class QueryAccountTransactionsResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryAccountTransactionsResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryAccountTransactionsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryAccountTransactionsResponseDataAccountTransactionsListAccountTransactionsList(TeaModel):
    def __init__(self, transaction_number=None, transaction_time=None, transaction_flow=None,
                 transaction_type=None, transaction_channel=None, transaction_channel_sn=None, fund_type=None, record_id=None,
                 remarks=None, billing_cycle=None, amount=None, balance=None, transaction_account=None):
        self.transaction_number = transaction_number  # type: str
        self.transaction_time = transaction_time  # type: str
        self.transaction_flow = transaction_flow  # type: str
        self.transaction_type = transaction_type  # type: str
        self.transaction_channel = transaction_channel  # type: str
        self.transaction_channel_sn = transaction_channel_sn  # type: str
        self.fund_type = fund_type      # type: str
        self.record_id = record_id      # type: str
        self.remarks = remarks          # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.amount = amount            # type: str
        self.balance = balance          # type: str
        self.transaction_account = transaction_account  # type: str

    def validate(self):
        self.validate_required(self.transaction_number, 'transaction_number')
        self.validate_required(self.transaction_time, 'transaction_time')
        self.validate_required(self.transaction_flow, 'transaction_flow')
        self.validate_required(self.transaction_type, 'transaction_type')
        self.validate_required(self.transaction_channel, 'transaction_channel')
        self.validate_required(self.transaction_channel_sn, 'transaction_channel_sn')
        self.validate_required(self.fund_type, 'fund_type')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.remarks, 'remarks')
        self.validate_required(self.billing_cycle, 'billing_cycle')
        self.validate_required(self.amount, 'amount')
        self.validate_required(self.balance, 'balance')
        self.validate_required(self.transaction_account, 'transaction_account')

    def to_map(self):
        result = {}
        result['TransactionNumber'] = self.transaction_number
        result['TransactionTime'] = self.transaction_time
        result['TransactionFlow'] = self.transaction_flow
        result['TransactionType'] = self.transaction_type
        result['TransactionChannel'] = self.transaction_channel
        result['TransactionChannelSN'] = self.transaction_channel_sn
        result['FundType'] = self.fund_type
        result['RecordID'] = self.record_id
        result['Remarks'] = self.remarks
        result['BillingCycle'] = self.billing_cycle
        result['Amount'] = self.amount
        result['Balance'] = self.balance
        result['TransactionAccount'] = self.transaction_account
        return result

    def from_map(self, map={}):
        self.transaction_number = map.get('TransactionNumber')
        self.transaction_time = map.get('TransactionTime')
        self.transaction_flow = map.get('TransactionFlow')
        self.transaction_type = map.get('TransactionType')
        self.transaction_channel = map.get('TransactionChannel')
        self.transaction_channel_sn = map.get('TransactionChannelSN')
        self.fund_type = map.get('FundType')
        self.record_id = map.get('RecordID')
        self.remarks = map.get('Remarks')
        self.billing_cycle = map.get('BillingCycle')
        self.amount = map.get('Amount')
        self.balance = map.get('Balance')
        self.transaction_account = map.get('TransactionAccount')
        return self


class QueryAccountTransactionsResponseDataAccountTransactionsList(TeaModel):
    def __init__(self, account_transactions_list=None):
        self.account_transactions_list = account_transactions_list  # type: List[QueryAccountTransactionsResponseDataAccountTransactionsListAccountTransactionsList]

    def validate(self):
        self.validate_required(self.account_transactions_list, 'account_transactions_list')
        if self.account_transactions_list:
            for k in self.account_transactions_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AccountTransactionsList'] = []
        if self.account_transactions_list is not None:
            for k in self.account_transactions_list:
                result['AccountTransactionsList'].append(k.to_map() if k else None)
        else:
            result['AccountTransactionsList'] = None
        return result

    def from_map(self, map={}):
        self.account_transactions_list = []
        if map.get('AccountTransactionsList') is not None:
            for k in map.get('AccountTransactionsList'):
                temp_model = QueryAccountTransactionsResponseDataAccountTransactionsListAccountTransactionsList()
                self.account_transactions_list.append(temp_model.from_map(k))
        else:
            self.account_transactions_list = None
        return self


class QueryAccountTransactionsResponseData(TeaModel):
    def __init__(self, account_name=None, total_count=None, page_num=None, page_size=None,
                 account_transactions_list=None):
        self.account_name = account_name  # type: str
        self.total_count = total_count  # type: int
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.account_transactions_list = account_transactions_list  # type: QueryAccountTransactionsResponseDataAccountTransactionsList

    def validate(self):
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.account_transactions_list, 'account_transactions_list')
        if self.account_transactions_list:
            self.account_transactions_list.validate()

    def to_map(self):
        result = {}
        result['AccountName'] = self.account_name
        result['TotalCount'] = self.total_count
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        if self.account_transactions_list is not None:
            result['AccountTransactionsList'] = self.account_transactions_list.to_map()
        else:
            result['AccountTransactionsList'] = None
        return result

    def from_map(self, map={}):
        self.account_name = map.get('AccountName')
        self.total_count = map.get('TotalCount')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        if map.get('AccountTransactionsList') is not None:
            temp_model = QueryAccountTransactionsResponseDataAccountTransactionsList()
            self.account_transactions_list = temp_model.from_map(map['AccountTransactionsList'])
        else:
            self.account_transactions_list = None
        return self


class UnsubscribeBillToOSSRequest(TeaModel):
    def __init__(self, subscribe_type=None, mult_account_rel_subscribe=None):
        self.subscribe_type = subscribe_type  # type: str
        self.mult_account_rel_subscribe = mult_account_rel_subscribe  # type: str

    def validate(self):
        self.validate_required(self.subscribe_type, 'subscribe_type')

    def to_map(self):
        result = {}
        result['SubscribeType'] = self.subscribe_type
        result['MultAccountRelSubscribe'] = self.mult_account_rel_subscribe
        return result

    def from_map(self, map={}):
        self.subscribe_type = map.get('SubscribeType')
        self.mult_account_rel_subscribe = map.get('MultAccountRelSubscribe')
        return self


class UnsubscribeBillToOSSResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        return self


class SubscribeBillToOSSRequest(TeaModel):
    def __init__(self, subscribe_bucket=None, subscribe_type=None, mult_account_rel_subscribe=None,
                 bucket_owner_id=None):
        self.subscribe_bucket = subscribe_bucket  # type: str
        self.subscribe_type = subscribe_type  # type: str
        self.mult_account_rel_subscribe = mult_account_rel_subscribe  # type: str
        self.bucket_owner_id = bucket_owner_id  # type: int

    def validate(self):
        self.validate_required(self.subscribe_bucket, 'subscribe_bucket')

    def to_map(self):
        result = {}
        result['SubscribeBucket'] = self.subscribe_bucket
        result['SubscribeType'] = self.subscribe_type
        result['MultAccountRelSubscribe'] = self.mult_account_rel_subscribe
        result['BucketOwnerId'] = self.bucket_owner_id
        return result

    def from_map(self, map={}):
        self.subscribe_bucket = map.get('SubscribeBucket')
        self.subscribe_type = map.get('SubscribeType')
        self.mult_account_rel_subscribe = map.get('MultAccountRelSubscribe')
        self.bucket_owner_id = map.get('BucketOwnerId')
        return self


class SubscribeBillToOSSResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        return self


class QueryUserOmsDataRequest(TeaModel):
    def __init__(self, table=None, data_type=None, start_time=None, end_time=None, marker=None, page_size=None):
        self.table = table              # type: str
        self.data_type = data_type      # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.marker = marker            # type: str
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.table, 'table')
        self.validate_required(self.data_type, 'data_type')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['Table'] = self.table
        result['DataType'] = self.data_type
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Marker'] = self.marker
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.table = map.get('Table')
        self.data_type = map.get('DataType')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.marker = map.get('Marker')
        self.page_size = map.get('PageSize')
        return self


class QueryUserOmsDataResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryUserOmsDataResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryUserOmsDataResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryUserOmsDataResponseData(TeaModel):
    def __init__(self, marker=None, host_id=None, oms_data=None):
        self.marker = marker            # type: str
        self.host_id = host_id          # type: str
        self.oms_data = oms_data        # type: List[Dict[str, Any]]

    def validate(self):
        self.validate_required(self.marker, 'marker')
        self.validate_required(self.host_id, 'host_id')
        self.validate_required(self.oms_data, 'oms_data')

    def to_map(self):
        result = {}
        result['Marker'] = self.marker
        result['HostId'] = self.host_id
        result['OmsData'] = self.oms_data
        return result

    def from_map(self, map={}):
        self.marker = map.get('Marker')
        self.host_id = map.get('HostId')
        self.oms_data = map.get('OmsData')
        return self


class CancelOrderRequest(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id        # type: str

    def validate(self):
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.order_id = map.get('OrderId')
        return self


class CancelOrderResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: CancelOrderResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = CancelOrderResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class CancelOrderResponseData(TeaModel):
    def __init__(self, host_id=None):
        self.host_id = host_id          # type: str

    def validate(self):
        self.validate_required(self.host_id, 'host_id')

    def to_map(self):
        result = {}
        result['HostId'] = self.host_id
        return result

    def from_map(self, map={}):
        self.host_id = map.get('HostId')
        return self


class ApplyInvoiceRequest(TeaModel):
    def __init__(self, invoice_amount=None, customer_id=None, address_id=None, invoicing_type=None,
                 process_way=None, apply_user_nick=None, selected_ids=None, invoice_by_amount=None):
        self.invoice_amount = invoice_amount  # type: int
        self.customer_id = customer_id  # type: int
        self.address_id = address_id    # type: int
        self.invoicing_type = invoicing_type  # type: int
        self.process_way = process_way  # type: int
        self.apply_user_nick = apply_user_nick  # type: str
        self.selected_ids = selected_ids  # type: List[int]
        self.invoice_by_amount = invoice_by_amount  # type: bool

    def validate(self):
        self.validate_required(self.invoice_amount, 'invoice_amount')
        self.validate_required(self.customer_id, 'customer_id')
        self.validate_required(self.address_id, 'address_id')
        self.validate_required(self.apply_user_nick, 'apply_user_nick')
        self.validate_required(self.selected_ids, 'selected_ids')

    def to_map(self):
        result = {}
        result['InvoiceAmount'] = self.invoice_amount
        result['CustomerId'] = self.customer_id
        result['AddressId'] = self.address_id
        result['InvoicingType'] = self.invoicing_type
        result['ProcessWay'] = self.process_way
        result['ApplyUserNick'] = self.apply_user_nick
        result['SelectedIds'] = self.selected_ids
        result['InvoiceByAmount'] = self.invoice_by_amount
        return result

    def from_map(self, map={}):
        self.invoice_amount = map.get('InvoiceAmount')
        self.customer_id = map.get('CustomerId')
        self.address_id = map.get('AddressId')
        self.invoicing_type = map.get('InvoicingType')
        self.process_way = map.get('ProcessWay')
        self.apply_user_nick = map.get('ApplyUserNick')
        self.selected_ids = map.get('SelectedIds')
        self.invoice_by_amount = map.get('InvoiceByAmount')
        return self


class ApplyInvoiceResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: ApplyInvoiceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = ApplyInvoiceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ApplyInvoiceResponseData(TeaModel):
    def __init__(self, invoice_apply_id=None):
        self.invoice_apply_id = invoice_apply_id  # type: int

    def validate(self):
        self.validate_required(self.invoice_apply_id, 'invoice_apply_id')

    def to_map(self):
        result = {}
        result['InvoiceApplyId'] = self.invoice_apply_id
        return result

    def from_map(self, map={}):
        self.invoice_apply_id = map.get('InvoiceApplyId')
        return self


class QueryCustomerAddressListRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class QueryCustomerAddressListResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryCustomerAddressListResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryCustomerAddressListResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryCustomerAddressListResponseDataCustomerInvoiceAddressListCustomerInvoiceAddress(TeaModel):
    def __init__(self, id=None, user_id=None, user_nick=None, addressee=None, province=None, city=None, county=None,
                 street=None, postal_code=None, phone=None, biz_type=None, delivery_address=None):
        self.id = id                    # type: int
        self.user_id = user_id          # type: int
        self.user_nick = user_nick      # type: str
        self.addressee = addressee      # type: str
        self.province = province        # type: str
        self.city = city                # type: str
        self.county = county            # type: str
        self.street = street            # type: str
        self.postal_code = postal_code  # type: str
        self.phone = phone              # type: str
        self.biz_type = biz_type        # type: str
        self.delivery_address = delivery_address  # type: str

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_nick, 'user_nick')
        self.validate_required(self.addressee, 'addressee')
        self.validate_required(self.province, 'province')
        self.validate_required(self.city, 'city')
        self.validate_required(self.county, 'county')
        self.validate_required(self.street, 'street')
        self.validate_required(self.postal_code, 'postal_code')
        self.validate_required(self.phone, 'phone')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.delivery_address, 'delivery_address')

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['UserId'] = self.user_id
        result['UserNick'] = self.user_nick
        result['Addressee'] = self.addressee
        result['Province'] = self.province
        result['City'] = self.city
        result['County'] = self.county
        result['Street'] = self.street
        result['PostalCode'] = self.postal_code
        result['Phone'] = self.phone
        result['BizType'] = self.biz_type
        result['DeliveryAddress'] = self.delivery_address
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.user_id = map.get('UserId')
        self.user_nick = map.get('UserNick')
        self.addressee = map.get('Addressee')
        self.province = map.get('Province')
        self.city = map.get('City')
        self.county = map.get('County')
        self.street = map.get('Street')
        self.postal_code = map.get('PostalCode')
        self.phone = map.get('Phone')
        self.biz_type = map.get('BizType')
        self.delivery_address = map.get('DeliveryAddress')
        return self


class QueryCustomerAddressListResponseDataCustomerInvoiceAddressList(TeaModel):
    def __init__(self, customer_invoice_address=None):
        self.customer_invoice_address = customer_invoice_address  # type: List[QueryCustomerAddressListResponseDataCustomerInvoiceAddressListCustomerInvoiceAddress]

    def validate(self):
        self.validate_required(self.customer_invoice_address, 'customer_invoice_address')
        if self.customer_invoice_address:
            for k in self.customer_invoice_address:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CustomerInvoiceAddress'] = []
        if self.customer_invoice_address is not None:
            for k in self.customer_invoice_address:
                result['CustomerInvoiceAddress'].append(k.to_map() if k else None)
        else:
            result['CustomerInvoiceAddress'] = None
        return result

    def from_map(self, map={}):
        self.customer_invoice_address = []
        if map.get('CustomerInvoiceAddress') is not None:
            for k in map.get('CustomerInvoiceAddress'):
                temp_model = QueryCustomerAddressListResponseDataCustomerInvoiceAddressListCustomerInvoiceAddress()
                self.customer_invoice_address.append(temp_model.from_map(k))
        else:
            self.customer_invoice_address = None
        return self


class QueryCustomerAddressListResponseData(TeaModel):
    def __init__(self, customer_invoice_address_list=None):
        self.customer_invoice_address_list = customer_invoice_address_list  # type: QueryCustomerAddressListResponseDataCustomerInvoiceAddressList

    def validate(self):
        self.validate_required(self.customer_invoice_address_list, 'customer_invoice_address_list')
        if self.customer_invoice_address_list:
            self.customer_invoice_address_list.validate()

    def to_map(self):
        result = {}
        if self.customer_invoice_address_list is not None:
            result['CustomerInvoiceAddressList'] = self.customer_invoice_address_list.to_map()
        else:
            result['CustomerInvoiceAddressList'] = None
        return result

    def from_map(self, map={}):
        if map.get('CustomerInvoiceAddressList') is not None:
            temp_model = QueryCustomerAddressListResponseDataCustomerInvoiceAddressList()
            self.customer_invoice_address_list = temp_model.from_map(map['CustomerInvoiceAddressList'])
        else:
            self.customer_invoice_address_list = None
        return self


class QueryEvaluateListRequest(TeaModel):
    def __init__(self, type=None, out_biz_id=None, page_num=None, page_size=None, start_amount=None, end_amount=None,
                 start_biz_time=None, end_biz_time=None, sort_type=None, start_search_time=None, end_search_time=None,
                 bill_cycle=None, biz_type_list=None):
        self.type = type                # type: int
        self.out_biz_id = out_biz_id    # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.start_amount = start_amount  # type: int
        self.end_amount = end_amount    # type: int
        self.start_biz_time = start_biz_time  # type: str
        self.end_biz_time = end_biz_time  # type: str
        self.sort_type = sort_type      # type: int
        self.start_search_time = start_search_time  # type: str
        self.end_search_time = end_search_time  # type: str
        self.bill_cycle = bill_cycle    # type: str
        self.biz_type_list = biz_type_list  # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Type'] = self.type
        result['OutBizId'] = self.out_biz_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['StartAmount'] = self.start_amount
        result['EndAmount'] = self.end_amount
        result['StartBizTime'] = self.start_biz_time
        result['EndBizTime'] = self.end_biz_time
        result['SortType'] = self.sort_type
        result['StartSearchTime'] = self.start_search_time
        result['EndSearchTime'] = self.end_search_time
        result['BillCycle'] = self.bill_cycle
        result['BizTypeList'] = self.biz_type_list
        return result

    def from_map(self, map={}):
        self.type = map.get('Type')
        self.out_biz_id = map.get('OutBizId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.start_amount = map.get('StartAmount')
        self.end_amount = map.get('EndAmount')
        self.start_biz_time = map.get('StartBizTime')
        self.end_biz_time = map.get('EndBizTime')
        self.sort_type = map.get('SortType')
        self.start_search_time = map.get('StartSearchTime')
        self.end_search_time = map.get('EndSearchTime')
        self.bill_cycle = map.get('BillCycle')
        self.biz_type_list = map.get('BizTypeList')
        return self


class QueryEvaluateListResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryEvaluateListResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryEvaluateListResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryEvaluateListResponseDataEvaluateListEvaluate(TeaModel):
    def __init__(self, id=None, gmt_create=None, gmt_modified=None, user_id=None, user_nick=None, out_biz_id=None,
                 bill_id=None, item_id=None, bill_cycle=None, biz_type=None, original_amount=None, present_amount=None,
                 can_invoice_amount=None, invoiced_amount=None, offset_cost_amount=None, offset_accept_amount=None, status=None,
                 op_id=None, name=None, biz_time=None, type=None):
        self.id = id                    # type: int
        self.gmt_create = gmt_create    # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.user_id = user_id          # type: int
        self.user_nick = user_nick      # type: str
        self.out_biz_id = out_biz_id    # type: str
        self.bill_id = bill_id          # type: int
        self.item_id = item_id          # type: int
        self.bill_cycle = bill_cycle    # type: str
        self.biz_type = biz_type        # type: str
        self.original_amount = original_amount  # type: int
        self.present_amount = present_amount  # type: int
        self.can_invoice_amount = can_invoice_amount  # type: int
        self.invoiced_amount = invoiced_amount  # type: int
        self.offset_cost_amount = offset_cost_amount  # type: int
        self.offset_accept_amount = offset_accept_amount  # type: int
        self.status = status            # type: int
        self.op_id = op_id              # type: str
        self.name = name                # type: str
        self.biz_time = biz_time        # type: str
        self.type = type                # type: int

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.gmt_modified, 'gmt_modified')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_nick, 'user_nick')
        self.validate_required(self.out_biz_id, 'out_biz_id')
        self.validate_required(self.bill_id, 'bill_id')
        self.validate_required(self.item_id, 'item_id')
        self.validate_required(self.bill_cycle, 'bill_cycle')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.original_amount, 'original_amount')
        self.validate_required(self.present_amount, 'present_amount')
        self.validate_required(self.can_invoice_amount, 'can_invoice_amount')
        self.validate_required(self.invoiced_amount, 'invoiced_amount')
        self.validate_required(self.offset_cost_amount, 'offset_cost_amount')
        self.validate_required(self.offset_accept_amount, 'offset_accept_amount')
        self.validate_required(self.status, 'status')
        self.validate_required(self.op_id, 'op_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.biz_time, 'biz_time')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['GmtCreate'] = self.gmt_create
        result['GmtModified'] = self.gmt_modified
        result['UserId'] = self.user_id
        result['UserNick'] = self.user_nick
        result['OutBizId'] = self.out_biz_id
        result['BillId'] = self.bill_id
        result['ItemId'] = self.item_id
        result['BillCycle'] = self.bill_cycle
        result['BizType'] = self.biz_type
        result['OriginalAmount'] = self.original_amount
        result['PresentAmount'] = self.present_amount
        result['CanInvoiceAmount'] = self.can_invoice_amount
        result['InvoicedAmount'] = self.invoiced_amount
        result['OffsetCostAmount'] = self.offset_cost_amount
        result['OffsetAcceptAmount'] = self.offset_accept_amount
        result['Status'] = self.status
        result['OpId'] = self.op_id
        result['Name'] = self.name
        result['BizTime'] = self.biz_time
        result['Type'] = self.type
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.gmt_create = map.get('GmtCreate')
        self.gmt_modified = map.get('GmtModified')
        self.user_id = map.get('UserId')
        self.user_nick = map.get('UserNick')
        self.out_biz_id = map.get('OutBizId')
        self.bill_id = map.get('BillId')
        self.item_id = map.get('ItemId')
        self.bill_cycle = map.get('BillCycle')
        self.biz_type = map.get('BizType')
        self.original_amount = map.get('OriginalAmount')
        self.present_amount = map.get('PresentAmount')
        self.can_invoice_amount = map.get('CanInvoiceAmount')
        self.invoiced_amount = map.get('InvoicedAmount')
        self.offset_cost_amount = map.get('OffsetCostAmount')
        self.offset_accept_amount = map.get('OffsetAcceptAmount')
        self.status = map.get('Status')
        self.op_id = map.get('OpId')
        self.name = map.get('Name')
        self.biz_time = map.get('BizTime')
        self.type = map.get('Type')
        return self


class QueryEvaluateListResponseDataEvaluateList(TeaModel):
    def __init__(self, evaluate=None):
        self.evaluate = evaluate        # type: List[QueryEvaluateListResponseDataEvaluateListEvaluate]

    def validate(self):
        self.validate_required(self.evaluate, 'evaluate')
        if self.evaluate:
            for k in self.evaluate:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Evaluate'] = []
        if self.evaluate is not None:
            for k in self.evaluate:
                result['Evaluate'].append(k.to_map() if k else None)
        else:
            result['Evaluate'] = None
        return result

    def from_map(self, map={}):
        self.evaluate = []
        if map.get('Evaluate') is not None:
            for k in map.get('Evaluate'):
                temp_model = QueryEvaluateListResponseDataEvaluateListEvaluate()
                self.evaluate.append(temp_model.from_map(k))
        else:
            self.evaluate = None
        return self


class QueryEvaluateListResponseData(TeaModel):
    def __init__(self, host_id=None, page_num=None, page_size=None, total_count=None, total_invoice_amount=None,
                 total_un_applied_invoice_amount=None, evaluate_list=None):
        self.host_id = host_id          # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_invoice_amount = total_invoice_amount  # type: int
        self.total_un_applied_invoice_amount = total_un_applied_invoice_amount  # type: int
        self.evaluate_list = evaluate_list  # type: QueryEvaluateListResponseDataEvaluateList

    def validate(self):
        self.validate_required(self.host_id, 'host_id')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_invoice_amount, 'total_invoice_amount')
        self.validate_required(self.total_un_applied_invoice_amount, 'total_un_applied_invoice_amount')
        self.validate_required(self.evaluate_list, 'evaluate_list')
        if self.evaluate_list:
            self.evaluate_list.validate()

    def to_map(self):
        result = {}
        result['HostId'] = self.host_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalInvoiceAmount'] = self.total_invoice_amount
        result['TotalUnAppliedInvoiceAmount'] = self.total_un_applied_invoice_amount
        if self.evaluate_list is not None:
            result['EvaluateList'] = self.evaluate_list.to_map()
        else:
            result['EvaluateList'] = None
        return result

    def from_map(self, map={}):
        self.host_id = map.get('HostId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_invoice_amount = map.get('TotalInvoiceAmount')
        self.total_un_applied_invoice_amount = map.get('TotalUnAppliedInvoiceAmount')
        if map.get('EvaluateList') is not None:
            temp_model = QueryEvaluateListResponseDataEvaluateList()
            self.evaluate_list = temp_model.from_map(map['EvaluateList'])
        else:
            self.evaluate_list = None
        return self


class QueryInvoicingCustomerListRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class QueryInvoicingCustomerListResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryInvoicingCustomerListResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryInvoicingCustomerListResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryInvoicingCustomerListResponseDataCustomerInvoiceListCustomerInvoice(TeaModel):
    def __init__(self, id=None, user_id=None, user_nick=None, invoice_title=None, customer_type=None,
                 taxpayer_type=None, bank=None, bank_no=None, operating_license_address=None, operating_license_phone=None,
                 register_no=None, start_cycle=None, status=None, gmt_create=None, taxation_license=None, adjust_type=None,
                 end_cycle=None, title_change_instructions=None, issue_type=None, type=None, default_remark=None):
        self.id = id                    # type: int
        self.user_id = user_id          # type: int
        self.user_nick = user_nick      # type: str
        self.invoice_title = invoice_title  # type: str
        self.customer_type = customer_type  # type: int
        self.taxpayer_type = taxpayer_type  # type: int
        self.bank = bank                # type: str
        self.bank_no = bank_no          # type: str
        self.operating_license_address = operating_license_address  # type: str
        self.operating_license_phone = operating_license_phone  # type: str
        self.register_no = register_no  # type: str
        self.start_cycle = start_cycle  # type: int
        self.status = status            # type: int
        self.gmt_create = gmt_create    # type: str
        self.taxation_license = taxation_license  # type: str
        self.adjust_type = adjust_type  # type: int
        self.end_cycle = end_cycle      # type: int
        self.title_change_instructions = title_change_instructions  # type: str
        self.issue_type = issue_type    # type: int
        self.type = type                # type: int
        self.default_remark = default_remark  # type: str

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_nick, 'user_nick')
        self.validate_required(self.invoice_title, 'invoice_title')
        self.validate_required(self.customer_type, 'customer_type')
        self.validate_required(self.taxpayer_type, 'taxpayer_type')
        self.validate_required(self.bank, 'bank')
        self.validate_required(self.bank_no, 'bank_no')
        self.validate_required(self.operating_license_address, 'operating_license_address')
        self.validate_required(self.operating_license_phone, 'operating_license_phone')
        self.validate_required(self.register_no, 'register_no')
        self.validate_required(self.start_cycle, 'start_cycle')
        self.validate_required(self.status, 'status')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.taxation_license, 'taxation_license')
        self.validate_required(self.adjust_type, 'adjust_type')
        self.validate_required(self.end_cycle, 'end_cycle')
        self.validate_required(self.title_change_instructions, 'title_change_instructions')
        self.validate_required(self.issue_type, 'issue_type')
        self.validate_required(self.type, 'type')
        self.validate_required(self.default_remark, 'default_remark')

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['UserId'] = self.user_id
        result['UserNick'] = self.user_nick
        result['InvoiceTitle'] = self.invoice_title
        result['CustomerType'] = self.customer_type
        result['TaxpayerType'] = self.taxpayer_type
        result['Bank'] = self.bank
        result['BankNo'] = self.bank_no
        result['OperatingLicenseAddress'] = self.operating_license_address
        result['OperatingLicensePhone'] = self.operating_license_phone
        result['RegisterNo'] = self.register_no
        result['StartCycle'] = self.start_cycle
        result['Status'] = self.status
        result['GmtCreate'] = self.gmt_create
        result['TaxationLicense'] = self.taxation_license
        result['AdjustType'] = self.adjust_type
        result['EndCycle'] = self.end_cycle
        result['TitleChangeInstructions'] = self.title_change_instructions
        result['IssueType'] = self.issue_type
        result['Type'] = self.type
        result['DefaultRemark'] = self.default_remark
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.user_id = map.get('UserId')
        self.user_nick = map.get('UserNick')
        self.invoice_title = map.get('InvoiceTitle')
        self.customer_type = map.get('CustomerType')
        self.taxpayer_type = map.get('TaxpayerType')
        self.bank = map.get('Bank')
        self.bank_no = map.get('BankNo')
        self.operating_license_address = map.get('OperatingLicenseAddress')
        self.operating_license_phone = map.get('OperatingLicensePhone')
        self.register_no = map.get('RegisterNo')
        self.start_cycle = map.get('StartCycle')
        self.status = map.get('Status')
        self.gmt_create = map.get('GmtCreate')
        self.taxation_license = map.get('TaxationLicense')
        self.adjust_type = map.get('AdjustType')
        self.end_cycle = map.get('EndCycle')
        self.title_change_instructions = map.get('TitleChangeInstructions')
        self.issue_type = map.get('IssueType')
        self.type = map.get('Type')
        self.default_remark = map.get('DefaultRemark')
        return self


class QueryInvoicingCustomerListResponseDataCustomerInvoiceList(TeaModel):
    def __init__(self, customer_invoice=None):
        self.customer_invoice = customer_invoice  # type: List[QueryInvoicingCustomerListResponseDataCustomerInvoiceListCustomerInvoice]

    def validate(self):
        self.validate_required(self.customer_invoice, 'customer_invoice')
        if self.customer_invoice:
            for k in self.customer_invoice:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CustomerInvoice'] = []
        if self.customer_invoice is not None:
            for k in self.customer_invoice:
                result['CustomerInvoice'].append(k.to_map() if k else None)
        else:
            result['CustomerInvoice'] = None
        return result

    def from_map(self, map={}):
        self.customer_invoice = []
        if map.get('CustomerInvoice') is not None:
            for k in map.get('CustomerInvoice'):
                temp_model = QueryInvoicingCustomerListResponseDataCustomerInvoiceListCustomerInvoice()
                self.customer_invoice.append(temp_model.from_map(k))
        else:
            self.customer_invoice = None
        return self


class QueryInvoicingCustomerListResponseData(TeaModel):
    def __init__(self, customer_invoice_list=None):
        self.customer_invoice_list = customer_invoice_list  # type: QueryInvoicingCustomerListResponseDataCustomerInvoiceList

    def validate(self):
        self.validate_required(self.customer_invoice_list, 'customer_invoice_list')
        if self.customer_invoice_list:
            self.customer_invoice_list.validate()

    def to_map(self):
        result = {}
        if self.customer_invoice_list is not None:
            result['CustomerInvoiceList'] = self.customer_invoice_list.to_map()
        else:
            result['CustomerInvoiceList'] = None
        return result

    def from_map(self, map={}):
        if map.get('CustomerInvoiceList') is not None:
            temp_model = QueryInvoicingCustomerListResponseDataCustomerInvoiceList()
            self.customer_invoice_list = temp_model.from_map(map['CustomerInvoiceList'])
        else:
            self.customer_invoice_list = None
        return self


class QueryBillOverviewRequest(TeaModel):
    def __init__(self, billing_cycle=None, product_code=None, product_type=None, subscription_type=None,
                 bill_owner_id=None):
        self.billing_cycle = billing_cycle  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.bill_owner_id = bill_owner_id  # type: int

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.bill_owner_id = map.get('BillOwnerId')
        return self


class QueryBillOverviewResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryBillOverviewResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryBillOverviewResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryBillOverviewResponseDataItemsItem(TeaModel):
    def __init__(self, item=None, product_code=None, product_type=None, subscription_type=None, product_name=None,
                 product_detail=None, pretax_gross_amount=None, invoice_discount=None, deducted_by_coupons=None,
                 pretax_amount=None, currency=None, payment_amount=None, outstanding_amount=None, deducted_by_cash_coupons=None,
                 deducted_by_prepaid_card=None, pretax_amount_local=None, tax=None, after_tax_amount=None, payment_currency=None,
                 round_down_discount=None, pip_code=None, commodity_code=None):
        self.item = item                # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.product_name = product_name  # type: str
        self.product_detail = product_detail  # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.pretax_amount = pretax_amount  # type: float
        self.currency = currency        # type: str
        self.payment_amount = payment_amount  # type: float
        self.outstanding_amount = outstanding_amount  # type: float
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.pretax_amount_local = pretax_amount_local  # type: float
        self.tax = tax                  # type: float
        self.after_tax_amount = after_tax_amount  # type: float
        self.payment_currency = payment_currency  # type: str
        self.round_down_discount = round_down_discount  # type: str
        self.pip_code = pip_code        # type: str
        self.commodity_code = commodity_code  # type: str

    def validate(self):
        self.validate_required(self.item, 'item')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.product_name, 'product_name')
        self.validate_required(self.product_detail, 'product_detail')
        self.validate_required(self.pretax_gross_amount, 'pretax_gross_amount')
        self.validate_required(self.invoice_discount, 'invoice_discount')
        self.validate_required(self.deducted_by_coupons, 'deducted_by_coupons')
        self.validate_required(self.pretax_amount, 'pretax_amount')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.payment_amount, 'payment_amount')
        self.validate_required(self.outstanding_amount, 'outstanding_amount')
        self.validate_required(self.deducted_by_cash_coupons, 'deducted_by_cash_coupons')
        self.validate_required(self.deducted_by_prepaid_card, 'deducted_by_prepaid_card')
        self.validate_required(self.pretax_amount_local, 'pretax_amount_local')
        self.validate_required(self.tax, 'tax')
        self.validate_required(self.after_tax_amount, 'after_tax_amount')
        self.validate_required(self.payment_currency, 'payment_currency')
        self.validate_required(self.round_down_discount, 'round_down_discount')
        self.validate_required(self.pip_code, 'pip_code')
        self.validate_required(self.commodity_code, 'commodity_code')

    def to_map(self):
        result = {}
        result['Item'] = self.item
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['ProductName'] = self.product_name
        result['ProductDetail'] = self.product_detail
        result['PretaxGrossAmount'] = self.pretax_gross_amount
        result['InvoiceDiscount'] = self.invoice_discount
        result['DeductedByCoupons'] = self.deducted_by_coupons
        result['PretaxAmount'] = self.pretax_amount
        result['Currency'] = self.currency
        result['PaymentAmount'] = self.payment_amount
        result['OutstandingAmount'] = self.outstanding_amount
        result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        result['PretaxAmountLocal'] = self.pretax_amount_local
        result['Tax'] = self.tax
        result['AfterTaxAmount'] = self.after_tax_amount
        result['PaymentCurrency'] = self.payment_currency
        result['RoundDownDiscount'] = self.round_down_discount
        result['PipCode'] = self.pip_code
        result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, map={}):
        self.item = map.get('Item')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.product_name = map.get('ProductName')
        self.product_detail = map.get('ProductDetail')
        self.pretax_gross_amount = map.get('PretaxGrossAmount')
        self.invoice_discount = map.get('InvoiceDiscount')
        self.deducted_by_coupons = map.get('DeductedByCoupons')
        self.pretax_amount = map.get('PretaxAmount')
        self.currency = map.get('Currency')
        self.payment_amount = map.get('PaymentAmount')
        self.outstanding_amount = map.get('OutstandingAmount')
        self.deducted_by_cash_coupons = map.get('DeductedByCashCoupons')
        self.deducted_by_prepaid_card = map.get('DeductedByPrepaidCard')
        self.pretax_amount_local = map.get('PretaxAmountLocal')
        self.tax = map.get('Tax')
        self.after_tax_amount = map.get('AfterTaxAmount')
        self.payment_currency = map.get('PaymentCurrency')
        self.round_down_discount = map.get('RoundDownDiscount')
        self.pip_code = map.get('PipCode')
        self.commodity_code = map.get('CommodityCode')
        return self


class QueryBillOverviewResponseDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[QueryBillOverviewResponseDataItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = QueryBillOverviewResponseDataItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class QueryBillOverviewResponseData(TeaModel):
    def __init__(self, billing_cycle=None, account_id=None, account_name=None, items=None):
        self.billing_cycle = billing_cycle  # type: str
        self.account_id = account_id    # type: str
        self.account_name = account_name  # type: str
        self.items = items              # type: QueryBillOverviewResponseDataItems

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['AccountID'] = self.account_id
        result['AccountName'] = self.account_name
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.account_id = map.get('AccountID')
        self.account_name = map.get('AccountName')
        if map.get('Items') is not None:
            temp_model = QueryBillOverviewResponseDataItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class QueryBillRequest(TeaModel):
    def __init__(self, billing_cycle=None, type=None, product_code=None, product_type=None, subscription_type=None,
                 is_hide_zero_charge=None, is_display_local_currency=None, page_num=None, page_size=None, bill_owner_id=None):
        self.billing_cycle = billing_cycle  # type: str
        self.type = type                # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.is_hide_zero_charge = is_hide_zero_charge  # type: bool
        self.is_display_local_currency = is_display_local_currency  # type: bool
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.bill_owner_id = bill_owner_id  # type: int

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['Type'] = self.type
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['IsHideZeroCharge'] = self.is_hide_zero_charge
        result['IsDisplayLocalCurrency'] = self.is_display_local_currency
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.type = map.get('Type')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.is_hide_zero_charge = map.get('IsHideZeroCharge')
        self.is_display_local_currency = map.get('IsDisplayLocalCurrency')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.bill_owner_id = map.get('BillOwnerId')
        return self


class QueryBillResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryBillResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryBillResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryBillResponseDataItemsItem(TeaModel):
    def __init__(self, record_id=None, item=None, owner_id=None, usage_start_time=None, usage_end_time=None,
                 payment_time=None, product_code=None, product_type=None, subscription_type=None, product_name=None,
                 product_detail=None, pretax_gross_amount=None, deducted_by_coupons=None, invoice_discount=None,
                 pretax_amount=None, currency=None, pretax_amount_local=None, tax=None, payment_amount=None,
                 deducted_by_cash_coupons=None, deducted_by_prepaid_card=None, outstanding_amount=None, after_tax_amount=None, status=None,
                 payment_currency=None, payment_transaction_id=None, round_down_discount=None, sub_order_id=None, pip_code=None,
                 commodity_code=None):
        self.record_id = record_id      # type: str
        self.item = item                # type: str
        self.owner_id = owner_id        # type: str
        self.usage_start_time = usage_start_time  # type: str
        self.usage_end_time = usage_end_time  # type: str
        self.payment_time = payment_time  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.product_name = product_name  # type: str
        self.product_detail = product_detail  # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.pretax_amount = pretax_amount  # type: float
        self.currency = currency        # type: str
        self.pretax_amount_local = pretax_amount_local  # type: float
        self.tax = tax                  # type: float
        self.payment_amount = payment_amount  # type: float
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.outstanding_amount = outstanding_amount  # type: float
        self.after_tax_amount = after_tax_amount  # type: float
        self.status = status            # type: str
        self.payment_currency = payment_currency  # type: str
        self.payment_transaction_id = payment_transaction_id  # type: str
        self.round_down_discount = round_down_discount  # type: str
        self.sub_order_id = sub_order_id  # type: str
        self.pip_code = pip_code        # type: str
        self.commodity_code = commodity_code  # type: str

    def validate(self):
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.item, 'item')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.usage_start_time, 'usage_start_time')
        self.validate_required(self.usage_end_time, 'usage_end_time')
        self.validate_required(self.payment_time, 'payment_time')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.product_name, 'product_name')
        self.validate_required(self.product_detail, 'product_detail')
        self.validate_required(self.pretax_gross_amount, 'pretax_gross_amount')
        self.validate_required(self.deducted_by_coupons, 'deducted_by_coupons')
        self.validate_required(self.invoice_discount, 'invoice_discount')
        self.validate_required(self.pretax_amount, 'pretax_amount')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.pretax_amount_local, 'pretax_amount_local')
        self.validate_required(self.tax, 'tax')
        self.validate_required(self.payment_amount, 'payment_amount')
        self.validate_required(self.deducted_by_cash_coupons, 'deducted_by_cash_coupons')
        self.validate_required(self.deducted_by_prepaid_card, 'deducted_by_prepaid_card')
        self.validate_required(self.outstanding_amount, 'outstanding_amount')
        self.validate_required(self.after_tax_amount, 'after_tax_amount')
        self.validate_required(self.status, 'status')
        self.validate_required(self.payment_currency, 'payment_currency')
        self.validate_required(self.payment_transaction_id, 'payment_transaction_id')
        self.validate_required(self.round_down_discount, 'round_down_discount')
        self.validate_required(self.sub_order_id, 'sub_order_id')
        self.validate_required(self.pip_code, 'pip_code')
        self.validate_required(self.commodity_code, 'commodity_code')

    def to_map(self):
        result = {}
        result['RecordID'] = self.record_id
        result['Item'] = self.item
        result['OwnerID'] = self.owner_id
        result['UsageStartTime'] = self.usage_start_time
        result['UsageEndTime'] = self.usage_end_time
        result['PaymentTime'] = self.payment_time
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['ProductName'] = self.product_name
        result['ProductDetail'] = self.product_detail
        result['PretaxGrossAmount'] = self.pretax_gross_amount
        result['DeductedByCoupons'] = self.deducted_by_coupons
        result['InvoiceDiscount'] = self.invoice_discount
        result['PretaxAmount'] = self.pretax_amount
        result['Currency'] = self.currency
        result['PretaxAmountLocal'] = self.pretax_amount_local
        result['Tax'] = self.tax
        result['PaymentAmount'] = self.payment_amount
        result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        result['OutstandingAmount'] = self.outstanding_amount
        result['AfterTaxAmount'] = self.after_tax_amount
        result['Status'] = self.status
        result['PaymentCurrency'] = self.payment_currency
        result['PaymentTransactionID'] = self.payment_transaction_id
        result['RoundDownDiscount'] = self.round_down_discount
        result['SubOrderId'] = self.sub_order_id
        result['PipCode'] = self.pip_code
        result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, map={}):
        self.record_id = map.get('RecordID')
        self.item = map.get('Item')
        self.owner_id = map.get('OwnerID')
        self.usage_start_time = map.get('UsageStartTime')
        self.usage_end_time = map.get('UsageEndTime')
        self.payment_time = map.get('PaymentTime')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.product_name = map.get('ProductName')
        self.product_detail = map.get('ProductDetail')
        self.pretax_gross_amount = map.get('PretaxGrossAmount')
        self.deducted_by_coupons = map.get('DeductedByCoupons')
        self.invoice_discount = map.get('InvoiceDiscount')
        self.pretax_amount = map.get('PretaxAmount')
        self.currency = map.get('Currency')
        self.pretax_amount_local = map.get('PretaxAmountLocal')
        self.tax = map.get('Tax')
        self.payment_amount = map.get('PaymentAmount')
        self.deducted_by_cash_coupons = map.get('DeductedByCashCoupons')
        self.deducted_by_prepaid_card = map.get('DeductedByPrepaidCard')
        self.outstanding_amount = map.get('OutstandingAmount')
        self.after_tax_amount = map.get('AfterTaxAmount')
        self.status = map.get('Status')
        self.payment_currency = map.get('PaymentCurrency')
        self.payment_transaction_id = map.get('PaymentTransactionID')
        self.round_down_discount = map.get('RoundDownDiscount')
        self.sub_order_id = map.get('SubOrderId')
        self.pip_code = map.get('PipCode')
        self.commodity_code = map.get('CommodityCode')
        return self


class QueryBillResponseDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[QueryBillResponseDataItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = QueryBillResponseDataItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class QueryBillResponseData(TeaModel):
    def __init__(self, billing_cycle=None, account_id=None, account_name=None, page_num=None, page_size=None,
                 total_count=None, items=None):
        self.billing_cycle = billing_cycle  # type: str
        self.account_id = account_id    # type: str
        self.account_name = account_name  # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.items = items              # type: QueryBillResponseDataItems

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['AccountID'] = self.account_id
        result['AccountName'] = self.account_name
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.account_id = map.get('AccountID')
        self.account_name = map.get('AccountName')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('Items') is not None:
            temp_model = QueryBillResponseDataItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class QueryInstanceBillRequest(TeaModel):
    def __init__(self, billing_cycle=None, product_code=None, product_type=None, subscription_type=None,
                 is_billing_item=None, page_num=None, page_size=None, is_hide_zero_charge=None, billing_date=None, granularity=None,
                 bill_owner_id=None):
        self.billing_cycle = billing_cycle  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.is_billing_item = is_billing_item  # type: bool
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.is_hide_zero_charge = is_hide_zero_charge  # type: bool
        self.billing_date = billing_date  # type: str
        self.granularity = granularity  # type: str
        self.bill_owner_id = bill_owner_id  # type: int

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['IsBillingItem'] = self.is_billing_item
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['IsHideZeroCharge'] = self.is_hide_zero_charge
        result['BillingDate'] = self.billing_date
        result['Granularity'] = self.granularity
        result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.is_billing_item = map.get('IsBillingItem')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.is_hide_zero_charge = map.get('IsHideZeroCharge')
        self.billing_date = map.get('BillingDate')
        self.granularity = map.get('Granularity')
        self.bill_owner_id = map.get('BillOwnerId')
        return self


class QueryInstanceBillResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryInstanceBillResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryInstanceBillResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryInstanceBillResponseDataItemsItem(TeaModel):
    def __init__(self, instance_id=None, billing_type=None, cost_unit=None, product_code=None, product_type=None,
                 subscription_type=None, product_name=None, product_detail=None, owner_id=None, billing_item=None, list_price=None,
                 list_price_unit=None, usage=None, usage_unit=None, deducted_by_resource_package=None, pretax_gross_amount=None,
                 invoice_discount=None, deducted_by_coupons=None, pretax_amount=None, deducted_by_cash_coupons=None,
                 deducted_by_prepaid_card=None, payment_amount=None, outstanding_amount=None, currency=None, nick_name=None,
                 resource_group=None, tag=None, instance_config=None, instance_spec=None, internet_ip=None, intranet_ip=None,
                 region=None, zone=None, item=None, service_period=None, billing_date=None, service_period_unit=None,
                 pip_code=None, commodity_code=None):
        self.instance_id = instance_id  # type: str
        self.billing_type = billing_type  # type: str
        self.cost_unit = cost_unit      # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.product_name = product_name  # type: str
        self.product_detail = product_detail  # type: str
        self.owner_id = owner_id        # type: str
        self.billing_item = billing_item  # type: str
        self.list_price = list_price    # type: str
        self.list_price_unit = list_price_unit  # type: str
        self.usage = usage              # type: str
        self.usage_unit = usage_unit    # type: str
        self.deducted_by_resource_package = deducted_by_resource_package  # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.pretax_amount = pretax_amount  # type: float
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.payment_amount = payment_amount  # type: float
        self.outstanding_amount = outstanding_amount  # type: float
        self.currency = currency        # type: str
        self.nick_name = nick_name      # type: str
        self.resource_group = resource_group  # type: str
        self.tag = tag                  # type: str
        self.instance_config = instance_config  # type: str
        self.instance_spec = instance_spec  # type: str
        self.internet_ip = internet_ip  # type: str
        self.intranet_ip = intranet_ip  # type: str
        self.region = region            # type: str
        self.zone = zone                # type: str
        self.item = item                # type: str
        self.service_period = service_period  # type: str
        self.billing_date = billing_date  # type: str
        self.service_period_unit = service_period_unit  # type: str
        self.pip_code = pip_code        # type: str
        self.commodity_code = commodity_code  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.billing_type, 'billing_type')
        self.validate_required(self.cost_unit, 'cost_unit')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.product_name, 'product_name')
        self.validate_required(self.product_detail, 'product_detail')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.billing_item, 'billing_item')
        self.validate_required(self.list_price, 'list_price')
        self.validate_required(self.list_price_unit, 'list_price_unit')
        self.validate_required(self.usage, 'usage')
        self.validate_required(self.usage_unit, 'usage_unit')
        self.validate_required(self.deducted_by_resource_package, 'deducted_by_resource_package')
        self.validate_required(self.pretax_gross_amount, 'pretax_gross_amount')
        self.validate_required(self.invoice_discount, 'invoice_discount')
        self.validate_required(self.deducted_by_coupons, 'deducted_by_coupons')
        self.validate_required(self.pretax_amount, 'pretax_amount')
        self.validate_required(self.deducted_by_cash_coupons, 'deducted_by_cash_coupons')
        self.validate_required(self.deducted_by_prepaid_card, 'deducted_by_prepaid_card')
        self.validate_required(self.payment_amount, 'payment_amount')
        self.validate_required(self.outstanding_amount, 'outstanding_amount')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.nick_name, 'nick_name')
        self.validate_required(self.resource_group, 'resource_group')
        self.validate_required(self.tag, 'tag')
        self.validate_required(self.instance_config, 'instance_config')
        self.validate_required(self.instance_spec, 'instance_spec')
        self.validate_required(self.internet_ip, 'internet_ip')
        self.validate_required(self.intranet_ip, 'intranet_ip')
        self.validate_required(self.region, 'region')
        self.validate_required(self.zone, 'zone')
        self.validate_required(self.item, 'item')
        self.validate_required(self.service_period, 'service_period')
        self.validate_required(self.billing_date, 'billing_date')
        self.validate_required(self.service_period_unit, 'service_period_unit')
        self.validate_required(self.pip_code, 'pip_code')
        self.validate_required(self.commodity_code, 'commodity_code')

    def to_map(self):
        result = {}
        result['InstanceID'] = self.instance_id
        result['BillingType'] = self.billing_type
        result['CostUnit'] = self.cost_unit
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['ProductName'] = self.product_name
        result['ProductDetail'] = self.product_detail
        result['OwnerID'] = self.owner_id
        result['BillingItem'] = self.billing_item
        result['ListPrice'] = self.list_price
        result['ListPriceUnit'] = self.list_price_unit
        result['Usage'] = self.usage
        result['UsageUnit'] = self.usage_unit
        result['DeductedByResourcePackage'] = self.deducted_by_resource_package
        result['PretaxGrossAmount'] = self.pretax_gross_amount
        result['InvoiceDiscount'] = self.invoice_discount
        result['DeductedByCoupons'] = self.deducted_by_coupons
        result['PretaxAmount'] = self.pretax_amount
        result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        result['PaymentAmount'] = self.payment_amount
        result['OutstandingAmount'] = self.outstanding_amount
        result['Currency'] = self.currency
        result['NickName'] = self.nick_name
        result['ResourceGroup'] = self.resource_group
        result['Tag'] = self.tag
        result['InstanceConfig'] = self.instance_config
        result['InstanceSpec'] = self.instance_spec
        result['InternetIP'] = self.internet_ip
        result['IntranetIP'] = self.intranet_ip
        result['Region'] = self.region
        result['Zone'] = self.zone
        result['Item'] = self.item
        result['ServicePeriod'] = self.service_period
        result['BillingDate'] = self.billing_date
        result['ServicePeriodUnit'] = self.service_period_unit
        result['PipCode'] = self.pip_code
        result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceID')
        self.billing_type = map.get('BillingType')
        self.cost_unit = map.get('CostUnit')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.product_name = map.get('ProductName')
        self.product_detail = map.get('ProductDetail')
        self.owner_id = map.get('OwnerID')
        self.billing_item = map.get('BillingItem')
        self.list_price = map.get('ListPrice')
        self.list_price_unit = map.get('ListPriceUnit')
        self.usage = map.get('Usage')
        self.usage_unit = map.get('UsageUnit')
        self.deducted_by_resource_package = map.get('DeductedByResourcePackage')
        self.pretax_gross_amount = map.get('PretaxGrossAmount')
        self.invoice_discount = map.get('InvoiceDiscount')
        self.deducted_by_coupons = map.get('DeductedByCoupons')
        self.pretax_amount = map.get('PretaxAmount')
        self.deducted_by_cash_coupons = map.get('DeductedByCashCoupons')
        self.deducted_by_prepaid_card = map.get('DeductedByPrepaidCard')
        self.payment_amount = map.get('PaymentAmount')
        self.outstanding_amount = map.get('OutstandingAmount')
        self.currency = map.get('Currency')
        self.nick_name = map.get('NickName')
        self.resource_group = map.get('ResourceGroup')
        self.tag = map.get('Tag')
        self.instance_config = map.get('InstanceConfig')
        self.instance_spec = map.get('InstanceSpec')
        self.internet_ip = map.get('InternetIP')
        self.intranet_ip = map.get('IntranetIP')
        self.region = map.get('Region')
        self.zone = map.get('Zone')
        self.item = map.get('Item')
        self.service_period = map.get('ServicePeriod')
        self.billing_date = map.get('BillingDate')
        self.service_period_unit = map.get('ServicePeriodUnit')
        self.pip_code = map.get('PipCode')
        self.commodity_code = map.get('CommodityCode')
        return self


class QueryInstanceBillResponseDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[QueryInstanceBillResponseDataItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = QueryInstanceBillResponseDataItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class QueryInstanceBillResponseData(TeaModel):
    def __init__(self, billing_cycle=None, account_id=None, account_name=None, total_count=None, page_num=None,
                 page_size=None, items=None):
        self.billing_cycle = billing_cycle  # type: str
        self.account_id = account_id    # type: str
        self.account_name = account_name  # type: str
        self.total_count = total_count  # type: int
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.items = items              # type: QueryInstanceBillResponseDataItems

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['AccountID'] = self.account_id
        result['AccountName'] = self.account_name
        result['TotalCount'] = self.total_count
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.account_id = map.get('AccountID')
        self.account_name = map.get('AccountName')
        self.total_count = map.get('TotalCount')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        if map.get('Items') is not None:
            temp_model = QueryInstanceBillResponseDataItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class EnableBillGenerationRequest(TeaModel):
    def __init__(self, product_code=None):
        self.product_code = product_code  # type: str

    def validate(self):
        self.validate_required(self.product_code, 'product_code')

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        return self


class EnableBillGenerationResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: EnableBillGenerationResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = EnableBillGenerationResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class EnableBillGenerationResponseData(TeaModel):
    def __init__(self, boolean=None):
        self.boolean = boolean          # type: bool

    def validate(self):
        self.validate_required(self.boolean, 'boolean')

    def to_map(self):
        result = {}
        result['Boolean'] = self.boolean
        return result

    def from_map(self, map={}):
        self.boolean = map.get('Boolean')
        return self


class QueryRedeemRequest(TeaModel):
    def __init__(self, expiry_time_start=None, expiry_time_end=None, effective_or_not=None, page_num=None,
                 page_size=None):
        self.expiry_time_start = expiry_time_start  # type: str
        self.expiry_time_end = expiry_time_end  # type: str
        self.effective_or_not = effective_or_not  # type: bool
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ExpiryTimeStart'] = self.expiry_time_start
        result['ExpiryTimeEnd'] = self.expiry_time_end
        result['EffectiveOrNot'] = self.effective_or_not
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.expiry_time_start = map.get('ExpiryTimeStart')
        self.expiry_time_end = map.get('ExpiryTimeEnd')
        self.effective_or_not = map.get('EffectiveOrNot')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class QueryRedeemResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryRedeemResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryRedeemResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryRedeemResponseDataRedeemRedeem(TeaModel):
    def __init__(self, redeem_id=None, redeem_no=None, status=None, granted_time=None, effective_time=None,
                 expiry_time=None, nominal_value=None, balance=None, applicable_products=None, specification=None):
        self.redeem_id = redeem_id      # type: str
        self.redeem_no = redeem_no      # type: str
        self.status = status            # type: str
        self.granted_time = granted_time  # type: str
        self.effective_time = effective_time  # type: str
        self.expiry_time = expiry_time  # type: str
        self.nominal_value = nominal_value  # type: str
        self.balance = balance          # type: str
        self.applicable_products = applicable_products  # type: str
        self.specification = specification  # type: str

    def validate(self):
        self.validate_required(self.redeem_id, 'redeem_id')
        self.validate_required(self.redeem_no, 'redeem_no')
        self.validate_required(self.status, 'status')
        self.validate_required(self.granted_time, 'granted_time')
        self.validate_required(self.effective_time, 'effective_time')
        self.validate_required(self.expiry_time, 'expiry_time')
        self.validate_required(self.nominal_value, 'nominal_value')
        self.validate_required(self.balance, 'balance')
        self.validate_required(self.applicable_products, 'applicable_products')
        self.validate_required(self.specification, 'specification')

    def to_map(self):
        result = {}
        result['RedeemId'] = self.redeem_id
        result['RedeemNo'] = self.redeem_no
        result['Status'] = self.status
        result['GrantedTime'] = self.granted_time
        result['EffectiveTime'] = self.effective_time
        result['ExpiryTime'] = self.expiry_time
        result['NominalValue'] = self.nominal_value
        result['Balance'] = self.balance
        result['ApplicableProducts'] = self.applicable_products
        result['Specification'] = self.specification
        return result

    def from_map(self, map={}):
        self.redeem_id = map.get('RedeemId')
        self.redeem_no = map.get('RedeemNo')
        self.status = map.get('Status')
        self.granted_time = map.get('GrantedTime')
        self.effective_time = map.get('EffectiveTime')
        self.expiry_time = map.get('ExpiryTime')
        self.nominal_value = map.get('NominalValue')
        self.balance = map.get('Balance')
        self.applicable_products = map.get('ApplicableProducts')
        self.specification = map.get('Specification')
        return self


class QueryRedeemResponseDataRedeem(TeaModel):
    def __init__(self, redeem=None):
        self.redeem = redeem            # type: List[QueryRedeemResponseDataRedeemRedeem]

    def validate(self):
        self.validate_required(self.redeem, 'redeem')
        if self.redeem:
            for k in self.redeem:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Redeem'] = []
        if self.redeem is not None:
            for k in self.redeem:
                result['Redeem'].append(k.to_map() if k else None)
        else:
            result['Redeem'] = None
        return result

    def from_map(self, map={}):
        self.redeem = []
        if map.get('Redeem') is not None:
            for k in map.get('Redeem'):
                temp_model = QueryRedeemResponseDataRedeemRedeem()
                self.redeem.append(temp_model.from_map(k))
        else:
            self.redeem = None
        return self


class QueryRedeemResponseData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_count=None, redeem=None):
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.redeem = redeem            # type: QueryRedeemResponseDataRedeem

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.redeem, 'redeem')
        if self.redeem:
            self.redeem.validate()

    def to_map(self):
        result = {}
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.redeem is not None:
            result['Redeem'] = self.redeem.to_map()
        else:
            result['Redeem'] = None
        return result

    def from_map(self, map={}):
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('Redeem') is not None:
            temp_model = QueryRedeemResponseDataRedeem()
            self.redeem = temp_model.from_map(map['Redeem'])
        else:
            self.redeem = None
        return self


class ConvertChargeTypeRequest(TeaModel):
    def __init__(self, product_type=None, subscription_type=None, period=None, product_code=None, instance_id=None):
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.period = period            # type: int
        self.product_code = product_code  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['Period'] = self.period
        result['ProductCode'] = self.product_code
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.period = map.get('Period')
        self.product_code = map.get('ProductCode')
        self.instance_id = map.get('InstanceId')
        return self


class ConvertChargeTypeResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: ConvertChargeTypeResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = ConvertChargeTypeResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ConvertChargeTypeResponseData(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id        # type: str

    def validate(self):
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.order_id = map.get('OrderId')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, product_code=None, parameter=None, product_type=None, subscription_type=None, period=None,
                 renewal_status=None, renew_period=None, client_token=None):
        self.product_code = product_code  # type: str
        self.parameter = parameter      # type: List[CreateInstanceRequestParameter]
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.period = period            # type: int
        self.renewal_status = renewal_status  # type: str
        self.renew_period = renew_period  # type: int
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.product_code, 'product_code')
        if self.parameter:
            for k in self.parameter:
                if k:
                    k.validate()
        self.validate_required(self.subscription_type, 'subscription_type')

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        result['Parameter'] = []
        if self.parameter is not None:
            for k in self.parameter:
                result['Parameter'].append(k.to_map() if k else None)
        else:
            result['Parameter'] = None
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['Period'] = self.period
        result['RenewalStatus'] = self.renewal_status
        result['RenewPeriod'] = self.renew_period
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        self.parameter = []
        if map.get('Parameter') is not None:
            for k in map.get('Parameter'):
                temp_model = CreateInstanceRequestParameter()
                self.parameter.append(temp_model.from_map(k))
        else:
            self.parameter = None
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.period = map.get('Period')
        self.renewal_status = map.get('RenewalStatus')
        self.renew_period = map.get('RenewPeriod')
        self.client_token = map.get('ClientToken')
        return self


class CreateInstanceRequestParameter(TeaModel):
    def __init__(self, code=None, value=None):
        self.code = code                # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.value = map.get('Value')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: CreateInstanceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = CreateInstanceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class CreateInstanceResponseData(TeaModel):
    def __init__(self, instance_id=None, order_id=None):
        self.instance_id = instance_id  # type: str
        self.order_id = order_id        # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.order_id = map.get('OrderId')
        return self


class ModifyInstanceRequest(TeaModel):
    def __init__(self, product_code=None, product_type=None, subscription_type=None, modify_type=None,
                 instance_id=None, parameter=None, client_token=None):
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.modify_type = modify_type  # type: str
        self.instance_id = instance_id  # type: str
        self.parameter = parameter      # type: List[ModifyInstanceRequestParameter]
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.modify_type, 'modify_type')
        if self.parameter:
            for k in self.parameter:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['ModifyType'] = self.modify_type
        result['InstanceId'] = self.instance_id
        result['Parameter'] = []
        if self.parameter is not None:
            for k in self.parameter:
                result['Parameter'].append(k.to_map() if k else None)
        else:
            result['Parameter'] = None
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.modify_type = map.get('ModifyType')
        self.instance_id = map.get('InstanceId')
        self.parameter = []
        if map.get('Parameter') is not None:
            for k in map.get('Parameter'):
                temp_model = ModifyInstanceRequestParameter()
                self.parameter.append(temp_model.from_map(k))
        else:
            self.parameter = None
        self.client_token = map.get('ClientToken')
        return self


class ModifyInstanceRequestParameter(TeaModel):
    def __init__(self, code=None, value=None):
        self.code = code                # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.value = map.get('Value')
        return self


class ModifyInstanceResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: ModifyInstanceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = ModifyInstanceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ModifyInstanceResponseData(TeaModel):
    def __init__(self, host_id=None, order_id=None):
        self.host_id = host_id          # type: str
        self.order_id = order_id        # type: str

    def validate(self):
        self.validate_required(self.host_id, 'host_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['HostId'] = self.host_id
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.host_id = map.get('HostId')
        self.order_id = map.get('OrderId')
        return self


class DescribePricingModuleRequest(TeaModel):
    def __init__(self, product_code=None, product_type=None, subscription_type=None):
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str

    def validate(self):
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.subscription_type, 'subscription_type')

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        return self


class DescribePricingModuleResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: DescribePricingModuleResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = DescribePricingModuleResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DescribePricingModuleResponseDataModuleListModuleConfigList(TeaModel):
    def __init__(self, config_list=None):
        # ConfigList
        self.config_list = config_list  # type: List[str]

    def validate(self):
        self.validate_required(self.config_list, 'config_list')

    def to_map(self):
        result = {}
        result['ConfigList'] = self.config_list
        return result

    def from_map(self, map={}):
        self.config_list = map.get('ConfigList')
        return self


class DescribePricingModuleResponseDataModuleListModule(TeaModel):
    def __init__(self, module_code=None, module_name=None, price_type=None, currency=None, config_list=None):
        self.module_code = module_code  # type: str
        self.module_name = module_name  # type: str
        self.price_type = price_type    # type: str
        self.currency = currency        # type: str
        self.config_list = config_list  # type: DescribePricingModuleResponseDataModuleListModuleConfigList

    def validate(self):
        self.validate_required(self.module_code, 'module_code')
        self.validate_required(self.module_name, 'module_name')
        self.validate_required(self.price_type, 'price_type')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.config_list, 'config_list')
        if self.config_list:
            self.config_list.validate()

    def to_map(self):
        result = {}
        result['ModuleCode'] = self.module_code
        result['ModuleName'] = self.module_name
        result['PriceType'] = self.price_type
        result['Currency'] = self.currency
        if self.config_list is not None:
            result['ConfigList'] = self.config_list.to_map()
        else:
            result['ConfigList'] = None
        return result

    def from_map(self, map={}):
        self.module_code = map.get('ModuleCode')
        self.module_name = map.get('ModuleName')
        self.price_type = map.get('PriceType')
        self.currency = map.get('Currency')
        if map.get('ConfigList') is not None:
            temp_model = DescribePricingModuleResponseDataModuleListModuleConfigList()
            self.config_list = temp_model.from_map(map['ConfigList'])
        else:
            self.config_list = None
        return self


class DescribePricingModuleResponseDataModuleList(TeaModel):
    def __init__(self, module=None):
        self.module = module            # type: List[DescribePricingModuleResponseDataModuleListModule]

    def validate(self):
        self.validate_required(self.module, 'module')
        if self.module:
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Module'] = []
        if self.module is not None:
            for k in self.module:
                result['Module'].append(k.to_map() if k else None)
        else:
            result['Module'] = None
        return result

    def from_map(self, map={}):
        self.module = []
        if map.get('Module') is not None:
            for k in map.get('Module'):
                temp_model = DescribePricingModuleResponseDataModuleListModule()
                self.module.append(temp_model.from_map(k))
        else:
            self.module = None
        return self


class DescribePricingModuleResponseDataAttributeListAttributeValuesAttributeValue(TeaModel):
    def __init__(self, type=None, name=None, value=None, remark=None):
        self.type = type                # type: str
        self.name = name                # type: str
        self.value = value              # type: str
        self.remark = remark            # type: str

    def validate(self):
        self.validate_required(self.type, 'type')
        self.validate_required(self.name, 'name')
        self.validate_required(self.value, 'value')
        self.validate_required(self.remark, 'remark')

    def to_map(self):
        result = {}
        result['Type'] = self.type
        result['Name'] = self.name
        result['Value'] = self.value
        result['Remark'] = self.remark
        return result

    def from_map(self, map={}):
        self.type = map.get('Type')
        self.name = map.get('Name')
        self.value = map.get('Value')
        self.remark = map.get('Remark')
        return self


class DescribePricingModuleResponseDataAttributeListAttributeValues(TeaModel):
    def __init__(self, attribute_value=None):
        self.attribute_value = attribute_value  # type: List[DescribePricingModuleResponseDataAttributeListAttributeValuesAttributeValue]

    def validate(self):
        self.validate_required(self.attribute_value, 'attribute_value')
        if self.attribute_value:
            for k in self.attribute_value:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AttributeValue'] = []
        if self.attribute_value is not None:
            for k in self.attribute_value:
                result['AttributeValue'].append(k.to_map() if k else None)
        else:
            result['AttributeValue'] = None
        return result

    def from_map(self, map={}):
        self.attribute_value = []
        if map.get('AttributeValue') is not None:
            for k in map.get('AttributeValue'):
                temp_model = DescribePricingModuleResponseDataAttributeListAttributeValuesAttributeValue()
                self.attribute_value.append(temp_model.from_map(k))
        else:
            self.attribute_value = None
        return self


class DescribePricingModuleResponseDataAttributeListAttribute(TeaModel):
    def __init__(self, code=None, name=None, unit=None, values=None):
        self.code = code                # type: str
        self.name = name                # type: str
        self.unit = unit                # type: str
        self.values = values            # type: DescribePricingModuleResponseDataAttributeListAttributeValues

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.name, 'name')
        self.validate_required(self.unit, 'unit')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Name'] = self.name
        result['Unit'] = self.unit
        if self.values is not None:
            result['Values'] = self.values.to_map()
        else:
            result['Values'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.name = map.get('Name')
        self.unit = map.get('Unit')
        if map.get('Values') is not None:
            temp_model = DescribePricingModuleResponseDataAttributeListAttributeValues()
            self.values = temp_model.from_map(map['Values'])
        else:
            self.values = None
        return self


class DescribePricingModuleResponseDataAttributeList(TeaModel):
    def __init__(self, attribute=None):
        self.attribute = attribute      # type: List[DescribePricingModuleResponseDataAttributeListAttribute]

    def validate(self):
        self.validate_required(self.attribute, 'attribute')
        if self.attribute:
            for k in self.attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Attribute'] = []
        if self.attribute is not None:
            for k in self.attribute:
                result['Attribute'].append(k.to_map() if k else None)
        else:
            result['Attribute'] = None
        return result

    def from_map(self, map={}):
        self.attribute = []
        if map.get('Attribute') is not None:
            for k in map.get('Attribute'):
                temp_model = DescribePricingModuleResponseDataAttributeListAttribute()
                self.attribute.append(temp_model.from_map(k))
        else:
            self.attribute = None
        return self


class DescribePricingModuleResponseData(TeaModel):
    def __init__(self, module_list=None, attribute_list=None):
        self.module_list = module_list  # type: DescribePricingModuleResponseDataModuleList
        self.attribute_list = attribute_list  # type: DescribePricingModuleResponseDataAttributeList

    def validate(self):
        self.validate_required(self.module_list, 'module_list')
        if self.module_list:
            self.module_list.validate()
        self.validate_required(self.attribute_list, 'attribute_list')
        if self.attribute_list:
            self.attribute_list.validate()

    def to_map(self):
        result = {}
        if self.module_list is not None:
            result['ModuleList'] = self.module_list.to_map()
        else:
            result['ModuleList'] = None
        if self.attribute_list is not None:
            result['AttributeList'] = self.attribute_list.to_map()
        else:
            result['AttributeList'] = None
        return result

    def from_map(self, map={}):
        if map.get('ModuleList') is not None:
            temp_model = DescribePricingModuleResponseDataModuleList()
            self.module_list = temp_model.from_map(map['ModuleList'])
        else:
            self.module_list = None
        if map.get('AttributeList') is not None:
            temp_model = DescribePricingModuleResponseDataAttributeList()
            self.attribute_list = temp_model.from_map(map['AttributeList'])
        else:
            self.attribute_list = None
        return self


class QueryProductListRequest(TeaModel):
    def __init__(self, query_total_count=None, page_num=None, page_size=None):
        self.query_total_count = query_total_count  # type: bool
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.page_num, 'page_num')

    def to_map(self):
        result = {}
        result['QueryTotalCount'] = self.query_total_count
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.query_total_count = map.get('QueryTotalCount')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class QueryProductListResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryProductListResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryProductListResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryProductListResponseDataProductListProduct(TeaModel):
    def __init__(self, product_code=None, product_name=None, product_type=None, subscription_type=None):
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str

    def validate(self):
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_name, 'product_name')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        result['ProductName'] = self.product_name
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        self.product_name = map.get('ProductName')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        return self


class QueryProductListResponseDataProductList(TeaModel):
    def __init__(self, product=None):
        self.product = product          # type: List[QueryProductListResponseDataProductListProduct]

    def validate(self):
        self.validate_required(self.product, 'product')
        if self.product:
            for k in self.product:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Product'] = []
        if self.product is not None:
            for k in self.product:
                result['Product'].append(k.to_map() if k else None)
        else:
            result['Product'] = None
        return result

    def from_map(self, map={}):
        self.product = []
        if map.get('Product') is not None:
            for k in map.get('Product'):
                temp_model = QueryProductListResponseDataProductListProduct()
                self.product.append(temp_model.from_map(k))
        else:
            self.product = None
        return self


class QueryProductListResponseData(TeaModel):
    def __init__(self, total_count=None, page_num=None, page_size=None, product_list=None):
        self.total_count = total_count  # type: int
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.product_list = product_list  # type: QueryProductListResponseDataProductList

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.product_list, 'product_list')
        if self.product_list:
            self.product_list.validate()

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        if self.product_list is not None:
            result['ProductList'] = self.product_list.to_map()
        else:
            result['ProductList'] = None
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        if map.get('ProductList') is not None:
            temp_model = QueryProductListResponseDataProductList()
            self.product_list = temp_model.from_map(map['ProductList'])
        else:
            self.product_list = None
        return self


class QueryInstanceGaapCostRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, billing_cycle=None, product_code=None, product_type=None,
                 subscription_type=None):
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.billing_cycle = billing_cycle  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')

    def to_map(self):
        result = {}
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['BillingCycle'] = self.billing_cycle
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, map={}):
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.billing_cycle = map.get('BillingCycle')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        return self


class QueryInstanceGaapCostResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryInstanceGaapCostResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryInstanceGaapCostResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryInstanceGaapCostResponseDataModulesModule(TeaModel):
    def __init__(self, billing_cycle=None, instance_id=None, product_code=None, product_type=None,
                 subscription_type=None, tag=None, resource_group=None, accounting_unit=None, payer_account=None, owner_id=None,
                 region=None, currency=None, payment_currency=None, order_type=None, pay_time=None,
                 pretax_gross_amount=None, pricing_discount=None, deducted_by_coupons=None, pretax_amount=None,
                 pretax_amount_local=None, deducted_by_cash_coupons=None, deducted_by_prepaid_card=None, payment_amount=None,
                 gaap_pretax_gross_amount=None, gaap_pricing_discount=None, gaap_deducted_by_coupons=None, gaap_pretax_amount=None,
                 gaap_pretax_amount_local=None, gaap_deducted_by_cash_coupons=None, gaap_deducted_by_prepaid_card=None,
                 gaap_payment_amount=None, month_gaap_pretax_gross_amount=None, month_gaap_pricing_discount=None,
                 month_gaap_deducted_by_coupons=None, month_gaap_pretax_amount=None, month_gaap_pretax_amount_local=None,
                 month_gaap_deducted_by_cash_coupons=None, month_gaap_deducted_by_prepaid_card=None, month_gaap_payment_amount=None,
                 unallocated_payment_amount=None, usage_start_date=None, usage_end_date=None, bill_type=None, order_id=None, sub_order_id=None,
                 unallocated_pretax_gross_amount=None, unallocated_pricing_discount=None, unallocated_deducted_by_coupons=None,
                 unallocated_pretax_amount=None, unallocated_pretax_amount_local=None, unallocated_deducted_by_cash_coupons=None,
                 unallocated_deducted_by_prepaid_card=None):
        self.billing_cycle = billing_cycle  # type: str
        self.instance_id = instance_id  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tag = tag                  # type: str
        self.resource_group = resource_group  # type: str
        self.accounting_unit = accounting_unit  # type: str
        self.payer_account = payer_account  # type: str
        self.owner_id = owner_id        # type: str
        self.region = region            # type: str
        self.currency = currency        # type: str
        self.payment_currency = payment_currency  # type: str
        self.order_type = order_type    # type: str
        self.pay_time = pay_time        # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: str
        self.pricing_discount = pricing_discount  # type: str
        self.deducted_by_coupons = deducted_by_coupons  # type: str
        self.pretax_amount = pretax_amount  # type: str
        self.pretax_amount_local = pretax_amount_local  # type: str
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: str
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: str
        self.payment_amount = payment_amount  # type: str
        self.gaap_pretax_gross_amount = gaap_pretax_gross_amount  # type: str
        self.gaap_pricing_discount = gaap_pricing_discount  # type: str
        self.gaap_deducted_by_coupons = gaap_deducted_by_coupons  # type: str
        self.gaap_pretax_amount = gaap_pretax_amount  # type: str
        self.gaap_pretax_amount_local = gaap_pretax_amount_local  # type: str
        self.gaap_deducted_by_cash_coupons = gaap_deducted_by_cash_coupons  # type: str
        self.gaap_deducted_by_prepaid_card = gaap_deducted_by_prepaid_card  # type: str
        self.gaap_payment_amount = gaap_payment_amount  # type: str
        self.month_gaap_pretax_gross_amount = month_gaap_pretax_gross_amount  # type: str
        self.month_gaap_pricing_discount = month_gaap_pricing_discount  # type: str
        self.month_gaap_deducted_by_coupons = month_gaap_deducted_by_coupons  # type: str
        self.month_gaap_pretax_amount = month_gaap_pretax_amount  # type: str
        self.month_gaap_pretax_amount_local = month_gaap_pretax_amount_local  # type: str
        self.month_gaap_deducted_by_cash_coupons = month_gaap_deducted_by_cash_coupons  # type: str
        self.month_gaap_deducted_by_prepaid_card = month_gaap_deducted_by_prepaid_card  # type: str
        self.month_gaap_payment_amount = month_gaap_payment_amount  # type: str
        self.unallocated_payment_amount = unallocated_payment_amount  # type: str
        self.usage_start_date = usage_start_date  # type: str
        self.usage_end_date = usage_end_date  # type: str
        self.bill_type = bill_type      # type: str
        self.order_id = order_id        # type: str
        self.sub_order_id = sub_order_id  # type: str
        self.unallocated_pretax_gross_amount = unallocated_pretax_gross_amount  # type: str
        self.unallocated_pricing_discount = unallocated_pricing_discount  # type: str
        self.unallocated_deducted_by_coupons = unallocated_deducted_by_coupons  # type: str
        self.unallocated_pretax_amount = unallocated_pretax_amount  # type: str
        self.unallocated_pretax_amount_local = unallocated_pretax_amount_local  # type: str
        self.unallocated_deducted_by_cash_coupons = unallocated_deducted_by_cash_coupons  # type: str
        self.unallocated_deducted_by_prepaid_card = unallocated_deducted_by_prepaid_card  # type: str

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.tag, 'tag')
        self.validate_required(self.resource_group, 'resource_group')
        self.validate_required(self.accounting_unit, 'accounting_unit')
        self.validate_required(self.payer_account, 'payer_account')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.region, 'region')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.payment_currency, 'payment_currency')
        self.validate_required(self.order_type, 'order_type')
        self.validate_required(self.pay_time, 'pay_time')
        self.validate_required(self.pretax_gross_amount, 'pretax_gross_amount')
        self.validate_required(self.pricing_discount, 'pricing_discount')
        self.validate_required(self.deducted_by_coupons, 'deducted_by_coupons')
        self.validate_required(self.pretax_amount, 'pretax_amount')
        self.validate_required(self.pretax_amount_local, 'pretax_amount_local')
        self.validate_required(self.deducted_by_cash_coupons, 'deducted_by_cash_coupons')
        self.validate_required(self.deducted_by_prepaid_card, 'deducted_by_prepaid_card')
        self.validate_required(self.payment_amount, 'payment_amount')
        self.validate_required(self.gaap_pretax_gross_amount, 'gaap_pretax_gross_amount')
        self.validate_required(self.gaap_pricing_discount, 'gaap_pricing_discount')
        self.validate_required(self.gaap_deducted_by_coupons, 'gaap_deducted_by_coupons')
        self.validate_required(self.gaap_pretax_amount, 'gaap_pretax_amount')
        self.validate_required(self.gaap_pretax_amount_local, 'gaap_pretax_amount_local')
        self.validate_required(self.gaap_deducted_by_cash_coupons, 'gaap_deducted_by_cash_coupons')
        self.validate_required(self.gaap_deducted_by_prepaid_card, 'gaap_deducted_by_prepaid_card')
        self.validate_required(self.gaap_payment_amount, 'gaap_payment_amount')
        self.validate_required(self.month_gaap_pretax_gross_amount, 'month_gaap_pretax_gross_amount')
        self.validate_required(self.month_gaap_pricing_discount, 'month_gaap_pricing_discount')
        self.validate_required(self.month_gaap_deducted_by_coupons, 'month_gaap_deducted_by_coupons')
        self.validate_required(self.month_gaap_pretax_amount, 'month_gaap_pretax_amount')
        self.validate_required(self.month_gaap_pretax_amount_local, 'month_gaap_pretax_amount_local')
        self.validate_required(self.month_gaap_deducted_by_cash_coupons, 'month_gaap_deducted_by_cash_coupons')
        self.validate_required(self.month_gaap_deducted_by_prepaid_card, 'month_gaap_deducted_by_prepaid_card')
        self.validate_required(self.month_gaap_payment_amount, 'month_gaap_payment_amount')
        self.validate_required(self.unallocated_payment_amount, 'unallocated_payment_amount')
        self.validate_required(self.usage_start_date, 'usage_start_date')
        self.validate_required(self.usage_end_date, 'usage_end_date')
        self.validate_required(self.bill_type, 'bill_type')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.sub_order_id, 'sub_order_id')
        self.validate_required(self.unallocated_pretax_gross_amount, 'unallocated_pretax_gross_amount')
        self.validate_required(self.unallocated_pricing_discount, 'unallocated_pricing_discount')
        self.validate_required(self.unallocated_deducted_by_coupons, 'unallocated_deducted_by_coupons')
        self.validate_required(self.unallocated_pretax_amount, 'unallocated_pretax_amount')
        self.validate_required(self.unallocated_pretax_amount_local, 'unallocated_pretax_amount_local')
        self.validate_required(self.unallocated_deducted_by_cash_coupons, 'unallocated_deducted_by_cash_coupons')
        self.validate_required(self.unallocated_deducted_by_prepaid_card, 'unallocated_deducted_by_prepaid_card')

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        result['InstanceID'] = self.instance_id
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['Tag'] = self.tag
        result['ResourceGroup'] = self.resource_group
        result['AccountingUnit'] = self.accounting_unit
        result['PayerAccount'] = self.payer_account
        result['OwnerID'] = self.owner_id
        result['Region'] = self.region
        result['Currency'] = self.currency
        result['PaymentCurrency'] = self.payment_currency
        result['OrderType'] = self.order_type
        result['PayTime'] = self.pay_time
        result['PretaxGrossAmount'] = self.pretax_gross_amount
        result['PricingDiscount'] = self.pricing_discount
        result['DeductedByCoupons'] = self.deducted_by_coupons
        result['PretaxAmount'] = self.pretax_amount
        result['PretaxAmountLocal'] = self.pretax_amount_local
        result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        result['PaymentAmount'] = self.payment_amount
        result['GaapPretaxGrossAmount'] = self.gaap_pretax_gross_amount
        result['GaapPricingDiscount'] = self.gaap_pricing_discount
        result['GaapDeductedByCoupons'] = self.gaap_deducted_by_coupons
        result['GaapPretaxAmount'] = self.gaap_pretax_amount
        result['GaapPretaxAmountLocal'] = self.gaap_pretax_amount_local
        result['GaapDeductedByCashCoupons'] = self.gaap_deducted_by_cash_coupons
        result['GaapDeductedByPrepaidCard'] = self.gaap_deducted_by_prepaid_card
        result['GaapPaymentAmount'] = self.gaap_payment_amount
        result['MonthGaapPretaxGrossAmount'] = self.month_gaap_pretax_gross_amount
        result['MonthGaapPricingDiscount'] = self.month_gaap_pricing_discount
        result['MonthGaapDeductedByCoupons'] = self.month_gaap_deducted_by_coupons
        result['MonthGaapPretaxAmount'] = self.month_gaap_pretax_amount
        result['MonthGaapPretaxAmountLocal'] = self.month_gaap_pretax_amount_local
        result['MonthGaapDeductedByCashCoupons'] = self.month_gaap_deducted_by_cash_coupons
        result['MonthGaapDeductedByPrepaidCard'] = self.month_gaap_deducted_by_prepaid_card
        result['MonthGaapPaymentAmount'] = self.month_gaap_payment_amount
        result['UnallocatedPaymentAmount'] = self.unallocated_payment_amount
        result['UsageStartDate'] = self.usage_start_date
        result['UsageEndDate'] = self.usage_end_date
        result['BillType'] = self.bill_type
        result['OrderId'] = self.order_id
        result['SubOrderId'] = self.sub_order_id
        result['UnallocatedPretaxGrossAmount'] = self.unallocated_pretax_gross_amount
        result['UnallocatedPricingDiscount'] = self.unallocated_pricing_discount
        result['UnallocatedDeductedByCoupons'] = self.unallocated_deducted_by_coupons
        result['UnallocatedPretaxAmount'] = self.unallocated_pretax_amount
        result['UnallocatedPretaxAmountLocal'] = self.unallocated_pretax_amount_local
        result['UnallocatedDeductedByCashCoupons'] = self.unallocated_deducted_by_cash_coupons
        result['UnallocatedDeductedByPrepaidCard'] = self.unallocated_deducted_by_prepaid_card
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        self.instance_id = map.get('InstanceID')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.tag = map.get('Tag')
        self.resource_group = map.get('ResourceGroup')
        self.accounting_unit = map.get('AccountingUnit')
        self.payer_account = map.get('PayerAccount')
        self.owner_id = map.get('OwnerID')
        self.region = map.get('Region')
        self.currency = map.get('Currency')
        self.payment_currency = map.get('PaymentCurrency')
        self.order_type = map.get('OrderType')
        self.pay_time = map.get('PayTime')
        self.pretax_gross_amount = map.get('PretaxGrossAmount')
        self.pricing_discount = map.get('PricingDiscount')
        self.deducted_by_coupons = map.get('DeductedByCoupons')
        self.pretax_amount = map.get('PretaxAmount')
        self.pretax_amount_local = map.get('PretaxAmountLocal')
        self.deducted_by_cash_coupons = map.get('DeductedByCashCoupons')
        self.deducted_by_prepaid_card = map.get('DeductedByPrepaidCard')
        self.payment_amount = map.get('PaymentAmount')
        self.gaap_pretax_gross_amount = map.get('GaapPretaxGrossAmount')
        self.gaap_pricing_discount = map.get('GaapPricingDiscount')
        self.gaap_deducted_by_coupons = map.get('GaapDeductedByCoupons')
        self.gaap_pretax_amount = map.get('GaapPretaxAmount')
        self.gaap_pretax_amount_local = map.get('GaapPretaxAmountLocal')
        self.gaap_deducted_by_cash_coupons = map.get('GaapDeductedByCashCoupons')
        self.gaap_deducted_by_prepaid_card = map.get('GaapDeductedByPrepaidCard')
        self.gaap_payment_amount = map.get('GaapPaymentAmount')
        self.month_gaap_pretax_gross_amount = map.get('MonthGaapPretaxGrossAmount')
        self.month_gaap_pricing_discount = map.get('MonthGaapPricingDiscount')
        self.month_gaap_deducted_by_coupons = map.get('MonthGaapDeductedByCoupons')
        self.month_gaap_pretax_amount = map.get('MonthGaapPretaxAmount')
        self.month_gaap_pretax_amount_local = map.get('MonthGaapPretaxAmountLocal')
        self.month_gaap_deducted_by_cash_coupons = map.get('MonthGaapDeductedByCashCoupons')
        self.month_gaap_deducted_by_prepaid_card = map.get('MonthGaapDeductedByPrepaidCard')
        self.month_gaap_payment_amount = map.get('MonthGaapPaymentAmount')
        self.unallocated_payment_amount = map.get('UnallocatedPaymentAmount')
        self.usage_start_date = map.get('UsageStartDate')
        self.usage_end_date = map.get('UsageEndDate')
        self.bill_type = map.get('BillType')
        self.order_id = map.get('OrderId')
        self.sub_order_id = map.get('SubOrderId')
        self.unallocated_pretax_gross_amount = map.get('UnallocatedPretaxGrossAmount')
        self.unallocated_pricing_discount = map.get('UnallocatedPricingDiscount')
        self.unallocated_deducted_by_coupons = map.get('UnallocatedDeductedByCoupons')
        self.unallocated_pretax_amount = map.get('UnallocatedPretaxAmount')
        self.unallocated_pretax_amount_local = map.get('UnallocatedPretaxAmountLocal')
        self.unallocated_deducted_by_cash_coupons = map.get('UnallocatedDeductedByCashCoupons')
        self.unallocated_deducted_by_prepaid_card = map.get('UnallocatedDeductedByPrepaidCard')
        return self


class QueryInstanceGaapCostResponseDataModules(TeaModel):
    def __init__(self, module=None):
        self.module = module            # type: List[QueryInstanceGaapCostResponseDataModulesModule]

    def validate(self):
        self.validate_required(self.module, 'module')
        if self.module:
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Module'] = []
        if self.module is not None:
            for k in self.module:
                result['Module'].append(k.to_map() if k else None)
        else:
            result['Module'] = None
        return result

    def from_map(self, map={}):
        self.module = []
        if map.get('Module') is not None:
            for k in map.get('Module'):
                temp_model = QueryInstanceGaapCostResponseDataModulesModule()
                self.module.append(temp_model.from_map(k))
        else:
            self.module = None
        return self


class QueryInstanceGaapCostResponseData(TeaModel):
    def __init__(self, host_id=None, page_num=None, page_size=None, total_count=None, modules=None):
        self.host_id = host_id          # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.modules = modules          # type: QueryInstanceGaapCostResponseDataModules

    def validate(self):
        self.validate_required(self.host_id, 'host_id')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.modules, 'modules')
        if self.modules:
            self.modules.validate()

    def to_map(self):
        result = {}
        result['HostId'] = self.host_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.modules is not None:
            result['Modules'] = self.modules.to_map()
        else:
            result['Modules'] = None
        return result

    def from_map(self, map={}):
        self.host_id = map.get('HostId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('Modules') is not None:
            temp_model = QueryInstanceGaapCostResponseDataModules()
            self.modules = temp_model.from_map(map['Modules'])
        else:
            self.modules = None
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(self, product_code=None, instance_id=None, renew_period=None, client_token=None, product_type=None):
        self.product_code = product_code  # type: str
        self.instance_id = instance_id  # type: str
        self.renew_period = renew_period  # type: int
        self.client_token = client_token  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.renew_period, 'renew_period')

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        result['InstanceId'] = self.instance_id
        result['RenewPeriod'] = self.renew_period
        result['ClientToken'] = self.client_token
        result['ProductType'] = self.product_type
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        self.instance_id = map.get('InstanceId')
        self.renew_period = map.get('RenewPeriod')
        self.client_token = map.get('ClientToken')
        self.product_type = map.get('ProductType')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: RenewInstanceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = RenewInstanceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RenewInstanceResponseData(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id        # type: str

    def validate(self):
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.order_id = map.get('OrderId')
        return self


class GetOrderDetailRequest(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id        # type: str

    def validate(self):
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.order_id = map.get('OrderId')
        return self


class GetOrderDetailResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: GetOrderDetailResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = GetOrderDetailResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetOrderDetailResponseDataOrderListOrder(TeaModel):
    def __init__(self, order_id=None, sub_order_id=None, product_code=None, product_type=None,
                 subscription_type=None, order_type=None, create_time=None, payment_time=None, payment_status=None, region=None,
                 config=None, quantity=None, usage_start_time=None, usage_end_time=None, instance_ids=None,
                 pretax_gross_amount=None, pretax_amount=None, currency=None, pretax_amount_local=None, tax=None, after_tax_amount=None,
                 payment_currency=None, operator=None, related_order_id=None, order_sub_type=None, original_config=None):
        self.order_id = order_id        # type: str
        self.sub_order_id = sub_order_id  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.order_type = order_type    # type: str
        self.create_time = create_time  # type: str
        self.payment_time = payment_time  # type: str
        self.payment_status = payment_status  # type: str
        self.region = region            # type: str
        self.config = config            # type: str
        self.quantity = quantity        # type: str
        self.usage_start_time = usage_start_time  # type: str
        self.usage_end_time = usage_end_time  # type: str
        self.instance_ids = instance_ids  # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: str
        self.pretax_amount = pretax_amount  # type: str
        self.currency = currency        # type: str
        self.pretax_amount_local = pretax_amount_local  # type: str
        self.tax = tax                  # type: str
        self.after_tax_amount = after_tax_amount  # type: str
        self.payment_currency = payment_currency  # type: str
        self.operator = operator        # type: str
        self.related_order_id = related_order_id  # type: str
        self.order_sub_type = order_sub_type  # type: str
        self.original_config = original_config  # type: str

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.sub_order_id, 'sub_order_id')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.order_type, 'order_type')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.payment_time, 'payment_time')
        self.validate_required(self.payment_status, 'payment_status')
        self.validate_required(self.region, 'region')
        self.validate_required(self.config, 'config')
        self.validate_required(self.quantity, 'quantity')
        self.validate_required(self.usage_start_time, 'usage_start_time')
        self.validate_required(self.usage_end_time, 'usage_end_time')
        self.validate_required(self.instance_ids, 'instance_ids')
        self.validate_required(self.pretax_gross_amount, 'pretax_gross_amount')
        self.validate_required(self.pretax_amount, 'pretax_amount')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.pretax_amount_local, 'pretax_amount_local')
        self.validate_required(self.tax, 'tax')
        self.validate_required(self.after_tax_amount, 'after_tax_amount')
        self.validate_required(self.payment_currency, 'payment_currency')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.related_order_id, 'related_order_id')
        self.validate_required(self.order_sub_type, 'order_sub_type')
        self.validate_required(self.original_config, 'original_config')

    def to_map(self):
        result = {}
        result['OrderId'] = self.order_id
        result['SubOrderId'] = self.sub_order_id
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['OrderType'] = self.order_type
        result['CreateTime'] = self.create_time
        result['PaymentTime'] = self.payment_time
        result['PaymentStatus'] = self.payment_status
        result['Region'] = self.region
        result['Config'] = self.config
        result['Quantity'] = self.quantity
        result['UsageStartTime'] = self.usage_start_time
        result['UsageEndTime'] = self.usage_end_time
        result['InstanceIDs'] = self.instance_ids
        result['PretaxGrossAmount'] = self.pretax_gross_amount
        result['PretaxAmount'] = self.pretax_amount
        result['Currency'] = self.currency
        result['PretaxAmountLocal'] = self.pretax_amount_local
        result['Tax'] = self.tax
        result['AfterTaxAmount'] = self.after_tax_amount
        result['PaymentCurrency'] = self.payment_currency
        result['Operator'] = self.operator
        result['RelatedOrderId'] = self.related_order_id
        result['OrderSubType'] = self.order_sub_type
        result['OriginalConfig'] = self.original_config
        return result

    def from_map(self, map={}):
        self.order_id = map.get('OrderId')
        self.sub_order_id = map.get('SubOrderId')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.order_type = map.get('OrderType')
        self.create_time = map.get('CreateTime')
        self.payment_time = map.get('PaymentTime')
        self.payment_status = map.get('PaymentStatus')
        self.region = map.get('Region')
        self.config = map.get('Config')
        self.quantity = map.get('Quantity')
        self.usage_start_time = map.get('UsageStartTime')
        self.usage_end_time = map.get('UsageEndTime')
        self.instance_ids = map.get('InstanceIDs')
        self.pretax_gross_amount = map.get('PretaxGrossAmount')
        self.pretax_amount = map.get('PretaxAmount')
        self.currency = map.get('Currency')
        self.pretax_amount_local = map.get('PretaxAmountLocal')
        self.tax = map.get('Tax')
        self.after_tax_amount = map.get('AfterTaxAmount')
        self.payment_currency = map.get('PaymentCurrency')
        self.operator = map.get('Operator')
        self.related_order_id = map.get('RelatedOrderId')
        self.order_sub_type = map.get('OrderSubType')
        self.original_config = map.get('OriginalConfig')
        return self


class GetOrderDetailResponseDataOrderList(TeaModel):
    def __init__(self, order=None):
        self.order = order              # type: List[GetOrderDetailResponseDataOrderListOrder]

    def validate(self):
        self.validate_required(self.order, 'order')
        if self.order:
            for k in self.order:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Order'] = []
        if self.order is not None:
            for k in self.order:
                result['Order'].append(k.to_map() if k else None)
        else:
            result['Order'] = None
        return result

    def from_map(self, map={}):
        self.order = []
        if map.get('Order') is not None:
            for k in map.get('Order'):
                temp_model = GetOrderDetailResponseDataOrderListOrder()
                self.order.append(temp_model.from_map(k))
        else:
            self.order = None
        return self


class GetOrderDetailResponseData(TeaModel):
    def __init__(self, host_name=None, page_num=None, page_size=None, total_count=None, order_list=None):
        self.host_name = host_name      # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.order_list = order_list    # type: GetOrderDetailResponseDataOrderList

    def validate(self):
        self.validate_required(self.host_name, 'host_name')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.order_list, 'order_list')
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        result = {}
        result['HostName'] = self.host_name
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.order_list is not None:
            result['OrderList'] = self.order_list.to_map()
        else:
            result['OrderList'] = None
        return result

    def from_map(self, map={}):
        self.host_name = map.get('HostName')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('OrderList') is not None:
            temp_model = GetOrderDetailResponseDataOrderList()
            self.order_list = temp_model.from_map(map['OrderList'])
        else:
            self.order_list = None
        return self


class QueryOrdersRequest(TeaModel):
    def __init__(self, create_time_end=None, page_num=None, page_size=None, product_code=None, product_type=None,
                 subscription_type=None, order_type=None, payment_status=None, create_time_start=None):
        self.create_time_end = create_time_end  # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.order_type = order_type    # type: str
        self.payment_status = payment_status  # type: str
        self.create_time_start = create_time_start  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CreateTimeEnd'] = self.create_time_end
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['OrderType'] = self.order_type
        result['PaymentStatus'] = self.payment_status
        result['CreateTimeStart'] = self.create_time_start
        return result

    def from_map(self, map={}):
        self.create_time_end = map.get('CreateTimeEnd')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.order_type = map.get('OrderType')
        self.payment_status = map.get('PaymentStatus')
        self.create_time_start = map.get('CreateTimeStart')
        return self


class QueryOrdersResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryOrdersResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryOrdersResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryOrdersResponseDataOrderListOrder(TeaModel):
    def __init__(self, order_id=None, product_code=None, product_type=None, subscription_type=None, order_type=None,
                 create_time=None, payment_time=None, payment_status=None, pretax_gross_amount=None, pretax_amount=None,
                 currency=None, pretax_amount_local=None, tax=None, after_tax_amount=None, payment_currency=None,
                 related_order_id=None):
        self.order_id = order_id        # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.order_type = order_type    # type: str
        self.create_time = create_time  # type: str
        self.payment_time = payment_time  # type: str
        self.payment_status = payment_status  # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: str
        self.pretax_amount = pretax_amount  # type: str
        self.currency = currency        # type: str
        self.pretax_amount_local = pretax_amount_local  # type: str
        self.tax = tax                  # type: str
        self.after_tax_amount = after_tax_amount  # type: str
        self.payment_currency = payment_currency  # type: str
        self.related_order_id = related_order_id  # type: str

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.order_type, 'order_type')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.payment_time, 'payment_time')
        self.validate_required(self.payment_status, 'payment_status')
        self.validate_required(self.pretax_gross_amount, 'pretax_gross_amount')
        self.validate_required(self.pretax_amount, 'pretax_amount')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.pretax_amount_local, 'pretax_amount_local')
        self.validate_required(self.tax, 'tax')
        self.validate_required(self.after_tax_amount, 'after_tax_amount')
        self.validate_required(self.payment_currency, 'payment_currency')
        self.validate_required(self.related_order_id, 'related_order_id')

    def to_map(self):
        result = {}
        result['OrderId'] = self.order_id
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['OrderType'] = self.order_type
        result['CreateTime'] = self.create_time
        result['PaymentTime'] = self.payment_time
        result['PaymentStatus'] = self.payment_status
        result['PretaxGrossAmount'] = self.pretax_gross_amount
        result['PretaxAmount'] = self.pretax_amount
        result['Currency'] = self.currency
        result['PretaxAmountLocal'] = self.pretax_amount_local
        result['Tax'] = self.tax
        result['AfterTaxAmount'] = self.after_tax_amount
        result['PaymentCurrency'] = self.payment_currency
        result['RelatedOrderId'] = self.related_order_id
        return result

    def from_map(self, map={}):
        self.order_id = map.get('OrderId')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.order_type = map.get('OrderType')
        self.create_time = map.get('CreateTime')
        self.payment_time = map.get('PaymentTime')
        self.payment_status = map.get('PaymentStatus')
        self.pretax_gross_amount = map.get('PretaxGrossAmount')
        self.pretax_amount = map.get('PretaxAmount')
        self.currency = map.get('Currency')
        self.pretax_amount_local = map.get('PretaxAmountLocal')
        self.tax = map.get('Tax')
        self.after_tax_amount = map.get('AfterTaxAmount')
        self.payment_currency = map.get('PaymentCurrency')
        self.related_order_id = map.get('RelatedOrderId')
        return self


class QueryOrdersResponseDataOrderList(TeaModel):
    def __init__(self, order=None):
        self.order = order              # type: List[QueryOrdersResponseDataOrderListOrder]

    def validate(self):
        self.validate_required(self.order, 'order')
        if self.order:
            for k in self.order:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Order'] = []
        if self.order is not None:
            for k in self.order:
                result['Order'].append(k.to_map() if k else None)
        else:
            result['Order'] = None
        return result

    def from_map(self, map={}):
        self.order = []
        if map.get('Order') is not None:
            for k in map.get('Order'):
                temp_model = QueryOrdersResponseDataOrderListOrder()
                self.order.append(temp_model.from_map(k))
        else:
            self.order = None
        return self


class QueryOrdersResponseData(TeaModel):
    def __init__(self, host_name=None, page_num=None, page_size=None, total_count=None, order_list=None):
        self.host_name = host_name      # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.order_list = order_list    # type: QueryOrdersResponseDataOrderList

    def validate(self):
        self.validate_required(self.host_name, 'host_name')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.order_list, 'order_list')
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        result = {}
        result['HostName'] = self.host_name
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.order_list is not None:
            result['OrderList'] = self.order_list.to_map()
        else:
            result['OrderList'] = None
        return result

    def from_map(self, map={}):
        self.host_name = map.get('HostName')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('OrderList') is not None:
            temp_model = QueryOrdersResponseDataOrderList()
            self.order_list = temp_model.from_map(map['OrderList'])
        else:
            self.order_list = None
        return self


class QueryMonthlyInstanceConsumptionRequest(TeaModel):
    def __init__(self, product_code=None, page_num=None, page_size=None, billing_cycle=None, product_type=None,
                 subscription_type=None):
        self.product_code = product_code  # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.billing_cycle = billing_cycle  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['BillingCycle'] = self.billing_cycle
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.billing_cycle = map.get('BillingCycle')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        return self


class QueryMonthlyInstanceConsumptionResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryMonthlyInstanceConsumptionResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryMonthlyInstanceConsumptionResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryMonthlyInstanceConsumptionResponseDataItemsItem(TeaModel):
    def __init__(self, instance_id=None, product_code=None, product_type=None, subscription_type=None, tag=None,
                 resource_group=None, payer_account=None, owner_id=None, region=None, pretax_gross_amount=None,
                 discount_amount=None, pretax_amount=None, currency=None, pretax_amount_local=None, tax=None, after_tax_amount=None,
                 payment_currency=None):
        self.instance_id = instance_id  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tag = tag                  # type: str
        self.resource_group = resource_group  # type: str
        self.payer_account = payer_account  # type: str
        self.owner_id = owner_id        # type: str
        self.region = region            # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.discount_amount = discount_amount  # type: float
        self.pretax_amount = pretax_amount  # type: float
        self.currency = currency        # type: str
        self.pretax_amount_local = pretax_amount_local  # type: float
        self.tax = tax                  # type: float
        self.after_tax_amount = after_tax_amount  # type: float
        self.payment_currency = payment_currency  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.tag, 'tag')
        self.validate_required(self.resource_group, 'resource_group')
        self.validate_required(self.payer_account, 'payer_account')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.region, 'region')
        self.validate_required(self.pretax_gross_amount, 'pretax_gross_amount')
        self.validate_required(self.discount_amount, 'discount_amount')
        self.validate_required(self.pretax_amount, 'pretax_amount')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.pretax_amount_local, 'pretax_amount_local')
        self.validate_required(self.tax, 'tax')
        self.validate_required(self.after_tax_amount, 'after_tax_amount')
        self.validate_required(self.payment_currency, 'payment_currency')

    def to_map(self):
        result = {}
        result['InstanceID'] = self.instance_id
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['Tag'] = self.tag
        result['ResourceGroup'] = self.resource_group
        result['PayerAccount'] = self.payer_account
        result['OwnerID'] = self.owner_id
        result['Region'] = self.region
        result['PretaxGrossAmount'] = self.pretax_gross_amount
        result['DiscountAmount'] = self.discount_amount
        result['PretaxAmount'] = self.pretax_amount
        result['Currency'] = self.currency
        result['PretaxAmountLocal'] = self.pretax_amount_local
        result['Tax'] = self.tax
        result['AfterTaxAmount'] = self.after_tax_amount
        result['PaymentCurrency'] = self.payment_currency
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceID')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.tag = map.get('Tag')
        self.resource_group = map.get('ResourceGroup')
        self.payer_account = map.get('PayerAccount')
        self.owner_id = map.get('OwnerID')
        self.region = map.get('Region')
        self.pretax_gross_amount = map.get('PretaxGrossAmount')
        self.discount_amount = map.get('DiscountAmount')
        self.pretax_amount = map.get('PretaxAmount')
        self.currency = map.get('Currency')
        self.pretax_amount_local = map.get('PretaxAmountLocal')
        self.tax = map.get('Tax')
        self.after_tax_amount = map.get('AfterTaxAmount')
        self.payment_currency = map.get('PaymentCurrency')
        return self


class QueryMonthlyInstanceConsumptionResponseDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[QueryMonthlyInstanceConsumptionResponseDataItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = QueryMonthlyInstanceConsumptionResponseDataItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class QueryMonthlyInstanceConsumptionResponseData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_count=None, billing_cycle=None, items=None):
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.billing_cycle = billing_cycle  # type: str
        self.items = items              # type: QueryMonthlyInstanceConsumptionResponseDataItems

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.billing_cycle, 'billing_cycle')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.billing_cycle = map.get('BillingCycle')
        if map.get('Items') is not None:
            temp_model = QueryMonthlyInstanceConsumptionResponseDataItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class QuerySettlementBillRequest(TeaModel):
    def __init__(self, page_size=None, page_num=None, billing_cycle=None, start_time=None, end_time=None, type=None,
                 product_code=None, product_type=None, subscription_type=None, is_hide_zero_charge=None):
        self.page_size = page_size      # type: int
        self.page_num = page_num        # type: int
        self.billing_cycle = billing_cycle  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.type = type                # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.is_hide_zero_charge = is_hide_zero_charge  # type: bool

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')

    def to_map(self):
        result = {}
        result['PageSize'] = self.page_size
        result['PageNum'] = self.page_num
        result['BillingCycle'] = self.billing_cycle
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Type'] = self.type
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['IsHideZeroCharge'] = self.is_hide_zero_charge
        return result

    def from_map(self, map={}):
        self.page_size = map.get('PageSize')
        self.page_num = map.get('PageNum')
        self.billing_cycle = map.get('BillingCycle')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.type = map.get('Type')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.is_hide_zero_charge = map.get('IsHideZeroCharge')
        return self


class QuerySettlementBillResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QuerySettlementBillResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QuerySettlementBillResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QuerySettlementBillResponseDataItemsItem(TeaModel):
    def __init__(self, record_id=None, item=None, payer_account=None, owner_id=None, create_time=None,
                 usage_start_time=None, usage_end_time=None, suborder_id=None, order_id=None, order_type=None,
                 linked_customer_order_id=None, original_order_id=None, payment_time=None, solution_id=None, solution_name=None,
                 bill_id=None, product_code=None, product_type=None, subscription_type=None, region=None, config=None,
                 quantity=None, pretax_gross_amount=None, charge_discount=None, deducted_by_coupons=None,
                 account_discount=None, promotion=None, pretax_amount=None, currency=None, pretax_amount_local=None,
                 previous_billing_cycle_balance=None, tax=None, after_tax_amount=None, status=None, cleared_time=None, outstanding_amount=None,
                 deducted_by_cash_coupons=None, deducted_by_prepaid_card=None, mybank_payment_amount=None, payment_amount=None,
                 payment_currency=None, seller=None, invoice_no=None):
        self.record_id = record_id      # type: str
        self.item = item                # type: str
        self.payer_account = payer_account  # type: str
        self.owner_id = owner_id        # type: str
        self.create_time = create_time  # type: str
        self.usage_start_time = usage_start_time  # type: str
        self.usage_end_time = usage_end_time  # type: str
        self.suborder_id = suborder_id  # type: str
        self.order_id = order_id        # type: str
        self.order_type = order_type    # type: str
        self.linked_customer_order_id = linked_customer_order_id  # type: str
        self.original_order_id = original_order_id  # type: str
        self.payment_time = payment_time  # type: str
        self.solution_id = solution_id  # type: str
        self.solution_name = solution_name  # type: str
        self.bill_id = bill_id          # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.region = region            # type: str
        self.config = config            # type: str
        self.quantity = quantity        # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.charge_discount = charge_discount  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.account_discount = account_discount  # type: float
        self.promotion = promotion      # type: str
        self.pretax_amount = pretax_amount  # type: float
        self.currency = currency        # type: str
        self.pretax_amount_local = pretax_amount_local  # type: float
        self.previous_billing_cycle_balance = previous_billing_cycle_balance  # type: float
        self.tax = tax                  # type: float
        self.after_tax_amount = after_tax_amount  # type: float
        self.status = status            # type: str
        self.cleared_time = cleared_time  # type: str
        self.outstanding_amount = outstanding_amount  # type: float
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.mybank_payment_amount = mybank_payment_amount  # type: float
        self.payment_amount = payment_amount  # type: float
        self.payment_currency = payment_currency  # type: str
        self.seller = seller            # type: str
        self.invoice_no = invoice_no    # type: str

    def validate(self):
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.item, 'item')
        self.validate_required(self.payer_account, 'payer_account')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.usage_start_time, 'usage_start_time')
        self.validate_required(self.usage_end_time, 'usage_end_time')
        self.validate_required(self.suborder_id, 'suborder_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.order_type, 'order_type')
        self.validate_required(self.linked_customer_order_id, 'linked_customer_order_id')
        self.validate_required(self.original_order_id, 'original_order_id')
        self.validate_required(self.payment_time, 'payment_time')
        self.validate_required(self.solution_id, 'solution_id')
        self.validate_required(self.solution_name, 'solution_name')
        self.validate_required(self.bill_id, 'bill_id')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.region, 'region')
        self.validate_required(self.config, 'config')
        self.validate_required(self.quantity, 'quantity')
        self.validate_required(self.pretax_gross_amount, 'pretax_gross_amount')
        self.validate_required(self.charge_discount, 'charge_discount')
        self.validate_required(self.deducted_by_coupons, 'deducted_by_coupons')
        self.validate_required(self.account_discount, 'account_discount')
        self.validate_required(self.promotion, 'promotion')
        self.validate_required(self.pretax_amount, 'pretax_amount')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.pretax_amount_local, 'pretax_amount_local')
        self.validate_required(self.previous_billing_cycle_balance, 'previous_billing_cycle_balance')
        self.validate_required(self.tax, 'tax')
        self.validate_required(self.after_tax_amount, 'after_tax_amount')
        self.validate_required(self.status, 'status')
        self.validate_required(self.cleared_time, 'cleared_time')
        self.validate_required(self.outstanding_amount, 'outstanding_amount')
        self.validate_required(self.deducted_by_cash_coupons, 'deducted_by_cash_coupons')
        self.validate_required(self.deducted_by_prepaid_card, 'deducted_by_prepaid_card')
        self.validate_required(self.mybank_payment_amount, 'mybank_payment_amount')
        self.validate_required(self.payment_amount, 'payment_amount')
        self.validate_required(self.payment_currency, 'payment_currency')
        self.validate_required(self.seller, 'seller')
        self.validate_required(self.invoice_no, 'invoice_no')

    def to_map(self):
        result = {}
        result['RecordID'] = self.record_id
        result['Item'] = self.item
        result['PayerAccount'] = self.payer_account
        result['OwnerID'] = self.owner_id
        result['CreateTime'] = self.create_time
        result['UsageStartTime'] = self.usage_start_time
        result['UsageEndTime'] = self.usage_end_time
        result['SuborderID'] = self.suborder_id
        result['OrderID'] = self.order_id
        result['OrderType'] = self.order_type
        result['LinkedCustomerOrderID'] = self.linked_customer_order_id
        result['OriginalOrderID'] = self.original_order_id
        result['PaymentTime'] = self.payment_time
        result['SolutionID'] = self.solution_id
        result['SolutionName'] = self.solution_name
        result['BillID'] = self.bill_id
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['Region'] = self.region
        result['Config'] = self.config
        result['Quantity'] = self.quantity
        result['PretaxGrossAmount'] = self.pretax_gross_amount
        result['ChargeDiscount'] = self.charge_discount
        result['DeductedByCoupons'] = self.deducted_by_coupons
        result['AccountDiscount'] = self.account_discount
        result['Promotion'] = self.promotion
        result['PretaxAmount'] = self.pretax_amount
        result['Currency'] = self.currency
        result['PretaxAmountLocal'] = self.pretax_amount_local
        result['PreviousBillingCycleBalance'] = self.previous_billing_cycle_balance
        result['Tax'] = self.tax
        result['AfterTaxAmount'] = self.after_tax_amount
        result['Status'] = self.status
        result['ClearedTime'] = self.cleared_time
        result['OutstandingAmount'] = self.outstanding_amount
        result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        result['MybankPaymentAmount'] = self.mybank_payment_amount
        result['PaymentAmount'] = self.payment_amount
        result['PaymentCurrency'] = self.payment_currency
        result['Seller'] = self.seller
        result['InvoiceNo'] = self.invoice_no
        return result

    def from_map(self, map={}):
        self.record_id = map.get('RecordID')
        self.item = map.get('Item')
        self.payer_account = map.get('PayerAccount')
        self.owner_id = map.get('OwnerID')
        self.create_time = map.get('CreateTime')
        self.usage_start_time = map.get('UsageStartTime')
        self.usage_end_time = map.get('UsageEndTime')
        self.suborder_id = map.get('SuborderID')
        self.order_id = map.get('OrderID')
        self.order_type = map.get('OrderType')
        self.linked_customer_order_id = map.get('LinkedCustomerOrderID')
        self.original_order_id = map.get('OriginalOrderID')
        self.payment_time = map.get('PaymentTime')
        self.solution_id = map.get('SolutionID')
        self.solution_name = map.get('SolutionName')
        self.bill_id = map.get('BillID')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.region = map.get('Region')
        self.config = map.get('Config')
        self.quantity = map.get('Quantity')
        self.pretax_gross_amount = map.get('PretaxGrossAmount')
        self.charge_discount = map.get('ChargeDiscount')
        self.deducted_by_coupons = map.get('DeductedByCoupons')
        self.account_discount = map.get('AccountDiscount')
        self.promotion = map.get('Promotion')
        self.pretax_amount = map.get('PretaxAmount')
        self.currency = map.get('Currency')
        self.pretax_amount_local = map.get('PretaxAmountLocal')
        self.previous_billing_cycle_balance = map.get('PreviousBillingCycleBalance')
        self.tax = map.get('Tax')
        self.after_tax_amount = map.get('AfterTaxAmount')
        self.status = map.get('Status')
        self.cleared_time = map.get('ClearedTime')
        self.outstanding_amount = map.get('OutstandingAmount')
        self.deducted_by_cash_coupons = map.get('DeductedByCashCoupons')
        self.deducted_by_prepaid_card = map.get('DeductedByPrepaidCard')
        self.mybank_payment_amount = map.get('MybankPaymentAmount')
        self.payment_amount = map.get('PaymentAmount')
        self.payment_currency = map.get('PaymentCurrency')
        self.seller = map.get('Seller')
        self.invoice_no = map.get('InvoiceNo')
        return self


class QuerySettlementBillResponseDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[QuerySettlementBillResponseDataItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = QuerySettlementBillResponseDataItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class QuerySettlementBillResponseData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_count=None, billing_cycle=None, items=None):
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.billing_cycle = billing_cycle  # type: str
        self.items = items              # type: QuerySettlementBillResponseDataItems

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.billing_cycle, 'billing_cycle')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.billing_cycle = map.get('BillingCycle')
        if map.get('Items') is not None:
            temp_model = QuerySettlementBillResponseDataItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class QueryMonthlyBillRequest(TeaModel):
    def __init__(self, billing_cycle=None):
        self.billing_cycle = billing_cycle  # type: str

    def validate(self):
        self.validate_required(self.billing_cycle, 'billing_cycle')

    def to_map(self):
        result = {}
        result['BillingCycle'] = self.billing_cycle
        return result

    def from_map(self, map={}):
        self.billing_cycle = map.get('BillingCycle')
        return self


class QueryMonthlyBillResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryMonthlyBillResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryMonthlyBillResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryMonthlyBillResponseDataItemsItem(TeaModel):
    def __init__(self, item=None, product_code=None, product_type=None, subscription_type=None, solution_code=None,
                 solution_name=None, pretax_gross_amount=None, invoice_discount=None, deducted_by_coupons=None,
                 pretax_amount=None, currency=None, pretax_amount_local=None, tax=None, after_tax_amount=None,
                 outstanding_amount=None, deducted_by_cash_coupons=None, deducted_by_prepaid_card=None, payment_amount=None,
                 payment_currency=None):
        self.item = item                # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.solution_code = solution_code  # type: str
        self.solution_name = solution_name  # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.pretax_amount = pretax_amount  # type: float
        self.currency = currency        # type: str
        self.pretax_amount_local = pretax_amount_local  # type: float
        self.tax = tax                  # type: float
        self.after_tax_amount = after_tax_amount  # type: float
        self.outstanding_amount = outstanding_amount  # type: float
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.payment_amount = payment_amount  # type: float
        self.payment_currency = payment_currency  # type: str

    def validate(self):
        self.validate_required(self.item, 'item')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.solution_code, 'solution_code')
        self.validate_required(self.solution_name, 'solution_name')
        self.validate_required(self.pretax_gross_amount, 'pretax_gross_amount')
        self.validate_required(self.invoice_discount, 'invoice_discount')
        self.validate_required(self.deducted_by_coupons, 'deducted_by_coupons')
        self.validate_required(self.pretax_amount, 'pretax_amount')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.pretax_amount_local, 'pretax_amount_local')
        self.validate_required(self.tax, 'tax')
        self.validate_required(self.after_tax_amount, 'after_tax_amount')
        self.validate_required(self.outstanding_amount, 'outstanding_amount')
        self.validate_required(self.deducted_by_cash_coupons, 'deducted_by_cash_coupons')
        self.validate_required(self.deducted_by_prepaid_card, 'deducted_by_prepaid_card')
        self.validate_required(self.payment_amount, 'payment_amount')
        self.validate_required(self.payment_currency, 'payment_currency')

    def to_map(self):
        result = {}
        result['Item'] = self.item
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['SolutionCode'] = self.solution_code
        result['SolutionName'] = self.solution_name
        result['PretaxGrossAmount'] = self.pretax_gross_amount
        result['InvoiceDiscount'] = self.invoice_discount
        result['DeductedByCoupons'] = self.deducted_by_coupons
        result['PretaxAmount'] = self.pretax_amount
        result['Currency'] = self.currency
        result['PretaxAmountLocal'] = self.pretax_amount_local
        result['Tax'] = self.tax
        result['AfterTaxAmount'] = self.after_tax_amount
        result['OutstandingAmount'] = self.outstanding_amount
        result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        result['PaymentAmount'] = self.payment_amount
        result['PaymentCurrency'] = self.payment_currency
        return result

    def from_map(self, map={}):
        self.item = map.get('Item')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.solution_code = map.get('SolutionCode')
        self.solution_name = map.get('SolutionName')
        self.pretax_gross_amount = map.get('PretaxGrossAmount')
        self.invoice_discount = map.get('InvoiceDiscount')
        self.deducted_by_coupons = map.get('DeductedByCoupons')
        self.pretax_amount = map.get('PretaxAmount')
        self.currency = map.get('Currency')
        self.pretax_amount_local = map.get('PretaxAmountLocal')
        self.tax = map.get('Tax')
        self.after_tax_amount = map.get('AfterTaxAmount')
        self.outstanding_amount = map.get('OutstandingAmount')
        self.deducted_by_cash_coupons = map.get('DeductedByCashCoupons')
        self.deducted_by_prepaid_card = map.get('DeductedByPrepaidCard')
        self.payment_amount = map.get('PaymentAmount')
        self.payment_currency = map.get('PaymentCurrency')
        return self


class QueryMonthlyBillResponseDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[QueryMonthlyBillResponseDataItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = QueryMonthlyBillResponseDataItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class QueryMonthlyBillResponseData(TeaModel):
    def __init__(self, outstanding_amount=None, total_outstanding_amount=None, new_invoice_amount=None,
                 billing_cycle=None, items=None):
        self.outstanding_amount = outstanding_amount  # type: float
        self.total_outstanding_amount = total_outstanding_amount  # type: float
        self.new_invoice_amount = new_invoice_amount  # type: float
        self.billing_cycle = billing_cycle  # type: str
        self.items = items              # type: QueryMonthlyBillResponseDataItems

    def validate(self):
        self.validate_required(self.outstanding_amount, 'outstanding_amount')
        self.validate_required(self.total_outstanding_amount, 'total_outstanding_amount')
        self.validate_required(self.new_invoice_amount, 'new_invoice_amount')
        self.validate_required(self.billing_cycle, 'billing_cycle')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['OutstandingAmount'] = self.outstanding_amount
        result['TotalOutstandingAmount'] = self.total_outstanding_amount
        result['NewInvoiceAmount'] = self.new_invoice_amount
        result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.outstanding_amount = map.get('OutstandingAmount')
        self.total_outstanding_amount = map.get('TotalOutstandingAmount')
        self.new_invoice_amount = map.get('NewInvoiceAmount')
        self.billing_cycle = map.get('BillingCycle')
        if map.get('Items') is not None:
            temp_model = QueryMonthlyBillResponseDataItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class SetRenewalRequest(TeaModel):
    def __init__(self, renewal_period=None, instance_ids=None, product_code=None, product_type=None,
                 subscription_type=None, renewal_period_unit=None, renewal_status=None):
        self.renewal_period = renewal_period  # type: int
        self.instance_ids = instance_ids  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.renewal_period_unit = renewal_period_unit  # type: str
        self.renewal_status = renewal_status  # type: str

    def validate(self):
        self.validate_required(self.instance_ids, 'instance_ids')
        self.validate_required(self.renewal_status, 'renewal_status')

    def to_map(self):
        result = {}
        result['RenewalPeriod'] = self.renewal_period
        result['InstanceIDs'] = self.instance_ids
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['RenewalPeriodUnit'] = self.renewal_period_unit
        result['RenewalStatus'] = self.renewal_status
        return result

    def from_map(self, map={}):
        self.renewal_period = map.get('RenewalPeriod')
        self.instance_ids = map.get('InstanceIDs')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.renewal_period_unit = map.get('RenewalPeriodUnit')
        self.renewal_status = map.get('RenewalStatus')
        return self


class SetRenewalResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        return self


class QueryAvailableInstancesRequest(TeaModel):
    def __init__(self, region=None, page_num=None, page_size=None, product_code=None, product_type=None,
                 subscription_type=None, instance_ids=None, end_time_start=None, end_time_end=None, create_time_start=None,
                 create_time_end=None, renew_status=None):
        self.region = region            # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.instance_ids = instance_ids  # type: str
        self.end_time_start = end_time_start  # type: str
        self.end_time_end = end_time_end  # type: str
        self.create_time_start = create_time_start  # type: str
        self.create_time_end = create_time_end  # type: str
        self.renew_status = renew_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Region'] = self.region
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['InstanceIDs'] = self.instance_ids
        result['EndTimeStart'] = self.end_time_start
        result['EndTimeEnd'] = self.end_time_end
        result['CreateTimeStart'] = self.create_time_start
        result['CreateTimeEnd'] = self.create_time_end
        result['RenewStatus'] = self.renew_status
        return result

    def from_map(self, map={}):
        self.region = map.get('Region')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.instance_ids = map.get('InstanceIDs')
        self.end_time_start = map.get('EndTimeStart')
        self.end_time_end = map.get('EndTimeEnd')
        self.create_time_start = map.get('CreateTimeStart')
        self.create_time_end = map.get('CreateTimeEnd')
        self.renew_status = map.get('RenewStatus')
        return self


class QueryAvailableInstancesResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryAvailableInstancesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryAvailableInstancesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryAvailableInstancesResponseDataInstanceList(TeaModel):
    def __init__(self, owner_id=None, seller_id=None, product_code=None, product_type=None, subscription_type=None,
                 instance_id=None, region=None, create_time=None, end_time=None, stop_time=None, release_time=None,
                 expected_release_time=None, status=None, sub_status=None, renew_status=None, renewal_duration=None,
                 renewal_duration_unit=None, seller=None):
        self.owner_id = owner_id        # type: int
        self.seller_id = seller_id      # type: int
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.instance_id = instance_id  # type: str
        self.region = region            # type: str
        self.create_time = create_time  # type: str
        self.end_time = end_time        # type: str
        self.stop_time = stop_time      # type: str
        self.release_time = release_time  # type: str
        self.expected_release_time = expected_release_time  # type: str
        self.status = status            # type: str
        self.sub_status = sub_status    # type: str
        self.renew_status = renew_status  # type: str
        self.renewal_duration = renewal_duration  # type: int
        self.renewal_duration_unit = renewal_duration_unit  # type: str
        self.seller = seller            # type: str

    def validate(self):
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.seller_id, 'seller_id')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.region, 'region')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.stop_time, 'stop_time')
        self.validate_required(self.release_time, 'release_time')
        self.validate_required(self.expected_release_time, 'expected_release_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.sub_status, 'sub_status')
        self.validate_required(self.renew_status, 'renew_status')
        self.validate_required(self.renewal_duration, 'renewal_duration')
        self.validate_required(self.renewal_duration_unit, 'renewal_duration_unit')
        self.validate_required(self.seller, 'seller')

    def to_map(self):
        result = {}
        result['OwnerId'] = self.owner_id
        result['SellerId'] = self.seller_id
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['InstanceID'] = self.instance_id
        result['Region'] = self.region
        result['CreateTime'] = self.create_time
        result['EndTime'] = self.end_time
        result['StopTime'] = self.stop_time
        result['ReleaseTime'] = self.release_time
        result['ExpectedReleaseTime'] = self.expected_release_time
        result['Status'] = self.status
        result['SubStatus'] = self.sub_status
        result['RenewStatus'] = self.renew_status
        result['RenewalDuration'] = self.renewal_duration
        result['RenewalDurationUnit'] = self.renewal_duration_unit
        result['Seller'] = self.seller
        return result

    def from_map(self, map={}):
        self.owner_id = map.get('OwnerId')
        self.seller_id = map.get('SellerId')
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.instance_id = map.get('InstanceID')
        self.region = map.get('Region')
        self.create_time = map.get('CreateTime')
        self.end_time = map.get('EndTime')
        self.stop_time = map.get('StopTime')
        self.release_time = map.get('ReleaseTime')
        self.expected_release_time = map.get('ExpectedReleaseTime')
        self.status = map.get('Status')
        self.sub_status = map.get('SubStatus')
        self.renew_status = map.get('RenewStatus')
        self.renewal_duration = map.get('RenewalDuration')
        self.renewal_duration_unit = map.get('RenewalDurationUnit')
        self.seller = map.get('Seller')
        return self


class QueryAvailableInstancesResponseData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_count=None, instance_list=None):
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.instance_list = instance_list  # type: List[QueryAvailableInstancesResponseDataInstanceList]

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.instance_list, 'instance_list')
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        else:
            result['InstanceList'] = None
        return result

    def from_map(self, map={}):
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.instance_list = []
        if map.get('InstanceList') is not None:
            for k in map.get('InstanceList'):
                temp_model = QueryAvailableInstancesResponseDataInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        else:
            self.instance_list = None
        return self


class CreateResourcePackageRequest(TeaModel):
    def __init__(self, product_code=None, package_type=None, effective_date=None, specification=None, duration=None,
                 pricing_cycle=None):
        self.product_code = product_code  # type: str
        self.package_type = package_type  # type: str
        self.effective_date = effective_date  # type: str
        self.specification = specification  # type: str
        self.duration = duration        # type: int
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        result['PackageType'] = self.package_type
        result['EffectiveDate'] = self.effective_date
        result['Specification'] = self.specification
        result['Duration'] = self.duration
        result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        self.package_type = map.get('PackageType')
        self.effective_date = map.get('EffectiveDate')
        self.specification = map.get('Specification')
        self.duration = map.get('Duration')
        self.pricing_cycle = map.get('PricingCycle')
        return self


class CreateResourcePackageResponse(TeaModel):
    def __init__(self, request_id=None, order_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.order_id = order_id        # type: int
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: CreateResourcePackageResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrderId'] = self.order_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.order_id = map.get('OrderId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = CreateResourcePackageResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class CreateResourcePackageResponseData(TeaModel):
    def __init__(self, order_id=None, instance_id=None):
        self.order_id = order_id        # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['OrderId'] = self.order_id
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.order_id = map.get('OrderId')
        self.instance_id = map.get('InstanceId')
        return self


class QueryResourcePackageInstancesRequest(TeaModel):
    def __init__(self, product_code=None, expiry_time_start=None, expiry_time_end=None, page_num=None,
                 page_size=None):
        self.product_code = product_code  # type: str
        self.expiry_time_start = expiry_time_start  # type: str
        self.expiry_time_end = expiry_time_end  # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        result['ExpiryTimeStart'] = self.expiry_time_start
        result['ExpiryTimeEnd'] = self.expiry_time_end
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        self.expiry_time_start = map.get('ExpiryTimeStart')
        self.expiry_time_end = map.get('ExpiryTimeEnd')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class QueryResourcePackageInstancesResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, page=None, page_size=None, total=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.page = page                # type: int
        self.page_size = page_size      # type: int
        self.total = total              # type: int
        self.data = data                # type: QueryResourcePackageInstancesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.page, 'page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total, 'total')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        result['Page'] = self.page
        result['PageSize'] = self.page_size
        result['Total'] = self.total
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.page = map.get('Page')
        self.page_size = map.get('PageSize')
        self.total = map.get('Total')
        if map.get('Data') is not None:
            temp_model = QueryResourcePackageInstancesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryResourcePackageInstancesResponseDataInstancesInstanceApplicableProducts(TeaModel):
    def __init__(self, product=None):
        # Product
        self.product = product          # type: List[str]

    def validate(self):
        self.validate_required(self.product, 'product')

    def to_map(self):
        result = {}
        result['Product'] = self.product
        return result

    def from_map(self, map={}):
        self.product = map.get('Product')
        return self


class QueryResourcePackageInstancesResponseDataInstancesInstance(TeaModel):
    def __init__(self, instance_id=None, region=None, total_amount=None, total_amount_unit=None,
                 remaining_amount=None, remaining_amount_unit=None, effective_time=None, expiry_time=None, remark=None,
                 package_type=None, status=None, deduct_type=None, applicable_products=None):
        self.instance_id = instance_id  # type: str
        self.region = region            # type: str
        self.total_amount = total_amount  # type: str
        self.total_amount_unit = total_amount_unit  # type: str
        self.remaining_amount = remaining_amount  # type: str
        self.remaining_amount_unit = remaining_amount_unit  # type: str
        self.effective_time = effective_time  # type: str
        self.expiry_time = expiry_time  # type: str
        self.remark = remark            # type: str
        self.package_type = package_type  # type: str
        self.status = status            # type: str
        self.deduct_type = deduct_type  # type: str
        self.applicable_products = applicable_products  # type: QueryResourcePackageInstancesResponseDataInstancesInstanceApplicableProducts

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.region, 'region')
        self.validate_required(self.total_amount, 'total_amount')
        self.validate_required(self.total_amount_unit, 'total_amount_unit')
        self.validate_required(self.remaining_amount, 'remaining_amount')
        self.validate_required(self.remaining_amount_unit, 'remaining_amount_unit')
        self.validate_required(self.effective_time, 'effective_time')
        self.validate_required(self.expiry_time, 'expiry_time')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.package_type, 'package_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.deduct_type, 'deduct_type')
        self.validate_required(self.applicable_products, 'applicable_products')
        if self.applicable_products:
            self.applicable_products.validate()

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['Region'] = self.region
        result['TotalAmount'] = self.total_amount
        result['TotalAmountUnit'] = self.total_amount_unit
        result['RemainingAmount'] = self.remaining_amount
        result['RemainingAmountUnit'] = self.remaining_amount_unit
        result['EffectiveTime'] = self.effective_time
        result['ExpiryTime'] = self.expiry_time
        result['Remark'] = self.remark
        result['PackageType'] = self.package_type
        result['Status'] = self.status
        result['DeductType'] = self.deduct_type
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products.to_map()
        else:
            result['ApplicableProducts'] = None
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.region = map.get('Region')
        self.total_amount = map.get('TotalAmount')
        self.total_amount_unit = map.get('TotalAmountUnit')
        self.remaining_amount = map.get('RemainingAmount')
        self.remaining_amount_unit = map.get('RemainingAmountUnit')
        self.effective_time = map.get('EffectiveTime')
        self.expiry_time = map.get('ExpiryTime')
        self.remark = map.get('Remark')
        self.package_type = map.get('PackageType')
        self.status = map.get('Status')
        self.deduct_type = map.get('DeductType')
        if map.get('ApplicableProducts') is not None:
            temp_model = QueryResourcePackageInstancesResponseDataInstancesInstanceApplicableProducts()
            self.applicable_products = temp_model.from_map(map['ApplicableProducts'])
        else:
            self.applicable_products = None
        return self


class QueryResourcePackageInstancesResponseDataInstances(TeaModel):
    def __init__(self, instance=None):
        self.instance = instance        # type: List[QueryResourcePackageInstancesResponseDataInstancesInstance]

    def validate(self):
        self.validate_required(self.instance, 'instance')
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        else:
            result['Instance'] = None
        return result

    def from_map(self, map={}):
        self.instance = []
        if map.get('Instance') is not None:
            for k in map.get('Instance'):
                temp_model = QueryResourcePackageInstancesResponseDataInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        else:
            self.instance = None
        return self


class QueryResourcePackageInstancesResponseData(TeaModel):
    def __init__(self, host_id=None, page_num=None, page_size=None, total_count=None, instances=None):
        self.host_id = host_id          # type: str
        self.page_num = page_num        # type: str
        self.page_size = page_size      # type: str
        self.total_count = total_count  # type: str
        self.instances = instances      # type: QueryResourcePackageInstancesResponseDataInstances

    def validate(self):
        self.validate_required(self.host_id, 'host_id')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = {}
        result['HostId'] = self.host_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        else:
            result['Instances'] = None
        return result

    def from_map(self, map={}):
        self.host_id = map.get('HostId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('Instances') is not None:
            temp_model = QueryResourcePackageInstancesResponseDataInstances()
            self.instances = temp_model.from_map(map['Instances'])
        else:
            self.instances = None
        return self


class GetResourcePackagePriceRequest(TeaModel):
    def __init__(self, product_code=None, package_type=None, effective_date=None, specification=None, duration=None,
                 pricing_cycle=None, order_type=None, instance_id=None):
        self.product_code = product_code  # type: str
        self.package_type = package_type  # type: str
        self.effective_date = effective_date  # type: str
        self.specification = specification  # type: str
        self.duration = duration        # type: int
        self.pricing_cycle = pricing_cycle  # type: str
        self.order_type = order_type    # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        result['PackageType'] = self.package_type
        result['EffectiveDate'] = self.effective_date
        result['Specification'] = self.specification
        result['Duration'] = self.duration
        result['PricingCycle'] = self.pricing_cycle
        result['OrderType'] = self.order_type
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        self.package_type = map.get('PackageType')
        self.effective_date = map.get('EffectiveDate')
        self.specification = map.get('Specification')
        self.duration = map.get('Duration')
        self.pricing_cycle = map.get('PricingCycle')
        self.order_type = map.get('OrderType')
        self.instance_id = map.get('InstanceId')
        return self


class GetResourcePackagePriceResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: GetResourcePackagePriceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = GetResourcePackagePriceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetResourcePackagePriceResponseDataPromotionsPromotion(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id                    # type: int
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.name = map.get('Name')
        return self


class GetResourcePackagePriceResponseDataPromotions(TeaModel):
    def __init__(self, promotion=None):
        self.promotion = promotion      # type: List[GetResourcePackagePriceResponseDataPromotionsPromotion]

    def validate(self):
        self.validate_required(self.promotion, 'promotion')
        if self.promotion:
            for k in self.promotion:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Promotion'] = []
        if self.promotion is not None:
            for k in self.promotion:
                result['Promotion'].append(k.to_map() if k else None)
        else:
            result['Promotion'] = None
        return result

    def from_map(self, map={}):
        self.promotion = []
        if map.get('Promotion') is not None:
            for k in map.get('Promotion'):
                temp_model = GetResourcePackagePriceResponseDataPromotionsPromotion()
                self.promotion.append(temp_model.from_map(k))
        else:
            self.promotion = None
        return self


class GetResourcePackagePriceResponseData(TeaModel):
    def __init__(self, currency=None, original_price=None, trade_price=None, discount_price=None, promotions=None):
        self.currency = currency        # type: str
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float
        self.discount_price = discount_price  # type: float
        self.promotions = promotions    # type: GetResourcePackagePriceResponseDataPromotions

    def validate(self):
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.original_price, 'original_price')
        self.validate_required(self.trade_price, 'trade_price')
        self.validate_required(self.discount_price, 'discount_price')
        self.validate_required(self.promotions, 'promotions')
        if self.promotions:
            self.promotions.validate()

    def to_map(self):
        result = {}
        result['Currency'] = self.currency
        result['OriginalPrice'] = self.original_price
        result['TradePrice'] = self.trade_price
        result['DiscountPrice'] = self.discount_price
        if self.promotions is not None:
            result['Promotions'] = self.promotions.to_map()
        else:
            result['Promotions'] = None
        return result

    def from_map(self, map={}):
        self.currency = map.get('Currency')
        self.original_price = map.get('OriginalPrice')
        self.trade_price = map.get('TradePrice')
        self.discount_price = map.get('DiscountPrice')
        if map.get('Promotions') is not None:
            temp_model = GetResourcePackagePriceResponseDataPromotions()
            self.promotions = temp_model.from_map(map['Promotions'])
        else:
            self.promotions = None
        return self


class GetSubscriptionPriceRequest(TeaModel):
    def __init__(self, service_period_unit=None, subscription_type=None, product_code=None, order_type=None,
                 service_period_quantity=None, product_type=None, region=None, instance_id=None, module_list=None, quantity=None):
        self.service_period_unit = service_period_unit  # type: str
        self.subscription_type = subscription_type  # type: str
        self.product_code = product_code  # type: str
        self.order_type = order_type    # type: str
        self.service_period_quantity = service_period_quantity  # type: int
        self.product_type = product_type  # type: str
        self.region = region            # type: str
        self.instance_id = instance_id  # type: str
        self.module_list = module_list  # type: List[GetSubscriptionPriceRequestModuleList]
        self.quantity = quantity        # type: int

    def validate(self):
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.order_type, 'order_type')
        self.validate_required(self.module_list, 'module_list')
        if self.module_list:
            for k in self.module_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ServicePeriodUnit'] = self.service_period_unit
        result['SubscriptionType'] = self.subscription_type
        result['ProductCode'] = self.product_code
        result['OrderType'] = self.order_type
        result['ServicePeriodQuantity'] = self.service_period_quantity
        result['ProductType'] = self.product_type
        result['Region'] = self.region
        result['InstanceId'] = self.instance_id
        result['ModuleList'] = []
        if self.module_list is not None:
            for k in self.module_list:
                result['ModuleList'].append(k.to_map() if k else None)
        else:
            result['ModuleList'] = None
        result['Quantity'] = self.quantity
        return result

    def from_map(self, map={}):
        self.service_period_unit = map.get('ServicePeriodUnit')
        self.subscription_type = map.get('SubscriptionType')
        self.product_code = map.get('ProductCode')
        self.order_type = map.get('OrderType')
        self.service_period_quantity = map.get('ServicePeriodQuantity')
        self.product_type = map.get('ProductType')
        self.region = map.get('Region')
        self.instance_id = map.get('InstanceId')
        self.module_list = []
        if map.get('ModuleList') is not None:
            for k in map.get('ModuleList'):
                temp_model = GetSubscriptionPriceRequestModuleList()
                self.module_list.append(temp_model.from_map(k))
        else:
            self.module_list = None
        self.quantity = map.get('Quantity')
        return self


class GetSubscriptionPriceRequestModuleList(TeaModel):
    def __init__(self, module_code=None, config=None, module_status=None, tag=None):
        self.module_code = module_code  # type: str
        self.config = config            # type: str
        self.module_status = module_status  # type: int
        self.tag = tag                  # type: str

    def validate(self):
        self.validate_required(self.module_code, 'module_code')
        self.validate_required(self.config, 'config')

    def to_map(self):
        result = {}
        result['ModuleCode'] = self.module_code
        result['Config'] = self.config
        result['ModuleStatus'] = self.module_status
        result['Tag'] = self.tag
        return result

    def from_map(self, map={}):
        self.module_code = map.get('ModuleCode')
        self.config = map.get('Config')
        self.module_status = map.get('ModuleStatus')
        self.tag = map.get('Tag')
        return self


class GetSubscriptionPriceResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: GetSubscriptionPriceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = GetSubscriptionPriceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetSubscriptionPriceResponseDataModuleDetailsModuleDetail(TeaModel):
    def __init__(self, module_code=None, original_cost=None, invoice_discount=None, cost_after_discount=None,
                 unit_price=None):
        self.module_code = module_code  # type: str
        self.original_cost = original_cost  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.cost_after_discount = cost_after_discount  # type: float
        self.unit_price = unit_price    # type: float

    def validate(self):
        self.validate_required(self.module_code, 'module_code')
        self.validate_required(self.original_cost, 'original_cost')
        self.validate_required(self.invoice_discount, 'invoice_discount')
        self.validate_required(self.cost_after_discount, 'cost_after_discount')
        self.validate_required(self.unit_price, 'unit_price')

    def to_map(self):
        result = {}
        result['ModuleCode'] = self.module_code
        result['OriginalCost'] = self.original_cost
        result['InvoiceDiscount'] = self.invoice_discount
        result['CostAfterDiscount'] = self.cost_after_discount
        result['UnitPrice'] = self.unit_price
        return result

    def from_map(self, map={}):
        self.module_code = map.get('ModuleCode')
        self.original_cost = map.get('OriginalCost')
        self.invoice_discount = map.get('InvoiceDiscount')
        self.cost_after_discount = map.get('CostAfterDiscount')
        self.unit_price = map.get('UnitPrice')
        return self


class GetSubscriptionPriceResponseDataModuleDetails(TeaModel):
    def __init__(self, module_detail=None):
        self.module_detail = module_detail  # type: List[GetSubscriptionPriceResponseDataModuleDetailsModuleDetail]

    def validate(self):
        self.validate_required(self.module_detail, 'module_detail')
        if self.module_detail:
            for k in self.module_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ModuleDetail'] = []
        if self.module_detail is not None:
            for k in self.module_detail:
                result['ModuleDetail'].append(k.to_map() if k else None)
        else:
            result['ModuleDetail'] = None
        return result

    def from_map(self, map={}):
        self.module_detail = []
        if map.get('ModuleDetail') is not None:
            for k in map.get('ModuleDetail'):
                temp_model = GetSubscriptionPriceResponseDataModuleDetailsModuleDetail()
                self.module_detail.append(temp_model.from_map(k))
        else:
            self.module_detail = None
        return self


class GetSubscriptionPriceResponseDataPromotionDetailsPromotionDetail(TeaModel):
    def __init__(self, promotion_name=None, promotion_desc=None, promotion_id=None):
        self.promotion_name = promotion_name  # type: str
        self.promotion_desc = promotion_desc  # type: str
        self.promotion_id = promotion_id  # type: int

    def validate(self):
        self.validate_required(self.promotion_name, 'promotion_name')
        self.validate_required(self.promotion_desc, 'promotion_desc')
        self.validate_required(self.promotion_id, 'promotion_id')

    def to_map(self):
        result = {}
        result['PromotionName'] = self.promotion_name
        result['PromotionDesc'] = self.promotion_desc
        result['PromotionId'] = self.promotion_id
        return result

    def from_map(self, map={}):
        self.promotion_name = map.get('PromotionName')
        self.promotion_desc = map.get('PromotionDesc')
        self.promotion_id = map.get('PromotionId')
        return self


class GetSubscriptionPriceResponseDataPromotionDetails(TeaModel):
    def __init__(self, promotion_detail=None):
        self.promotion_detail = promotion_detail  # type: List[GetSubscriptionPriceResponseDataPromotionDetailsPromotionDetail]

    def validate(self):
        self.validate_required(self.promotion_detail, 'promotion_detail')
        if self.promotion_detail:
            for k in self.promotion_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PromotionDetail'] = []
        if self.promotion_detail is not None:
            for k in self.promotion_detail:
                result['PromotionDetail'].append(k.to_map() if k else None)
        else:
            result['PromotionDetail'] = None
        return result

    def from_map(self, map={}):
        self.promotion_detail = []
        if map.get('PromotionDetail') is not None:
            for k in map.get('PromotionDetail'):
                temp_model = GetSubscriptionPriceResponseDataPromotionDetailsPromotionDetail()
                self.promotion_detail.append(temp_model.from_map(k))
        else:
            self.promotion_detail = None
        return self


class GetSubscriptionPriceResponseData(TeaModel):
    def __init__(self, original_price=None, discount_price=None, trade_price=None, currency=None, quantity=None,
                 module_details=None, promotion_details=None):
        self.original_price = original_price  # type: float
        self.discount_price = discount_price  # type: float
        self.trade_price = trade_price  # type: float
        self.currency = currency        # type: str
        self.quantity = quantity        # type: int
        self.module_details = module_details  # type: GetSubscriptionPriceResponseDataModuleDetails
        self.promotion_details = promotion_details  # type: GetSubscriptionPriceResponseDataPromotionDetails

    def validate(self):
        self.validate_required(self.original_price, 'original_price')
        self.validate_required(self.discount_price, 'discount_price')
        self.validate_required(self.trade_price, 'trade_price')
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.quantity, 'quantity')
        self.validate_required(self.module_details, 'module_details')
        if self.module_details:
            self.module_details.validate()
        self.validate_required(self.promotion_details, 'promotion_details')
        if self.promotion_details:
            self.promotion_details.validate()

    def to_map(self):
        result = {}
        result['OriginalPrice'] = self.original_price
        result['DiscountPrice'] = self.discount_price
        result['TradePrice'] = self.trade_price
        result['Currency'] = self.currency
        result['Quantity'] = self.quantity
        if self.module_details is not None:
            result['ModuleDetails'] = self.module_details.to_map()
        else:
            result['ModuleDetails'] = None
        if self.promotion_details is not None:
            result['PromotionDetails'] = self.promotion_details.to_map()
        else:
            result['PromotionDetails'] = None
        return result

    def from_map(self, map={}):
        self.original_price = map.get('OriginalPrice')
        self.discount_price = map.get('DiscountPrice')
        self.trade_price = map.get('TradePrice')
        self.currency = map.get('Currency')
        self.quantity = map.get('Quantity')
        if map.get('ModuleDetails') is not None:
            temp_model = GetSubscriptionPriceResponseDataModuleDetails()
            self.module_details = temp_model.from_map(map['ModuleDetails'])
        else:
            self.module_details = None
        if map.get('PromotionDetails') is not None:
            temp_model = GetSubscriptionPriceResponseDataPromotionDetails()
            self.promotion_details = temp_model.from_map(map['PromotionDetails'])
        else:
            self.promotion_details = None
        return self


class GetPayAsYouGoPriceRequest(TeaModel):
    def __init__(self, product_code=None, product_type=None, subscription_type=None, region=None, module_list=None):
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.region = region            # type: str
        self.module_list = module_list  # type: List[GetPayAsYouGoPriceRequestModuleList]

    def validate(self):
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.subscription_type, 'subscription_type')
        self.validate_required(self.module_list, 'module_list')
        if self.module_list:
            for k in self.module_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['SubscriptionType'] = self.subscription_type
        result['Region'] = self.region
        result['ModuleList'] = []
        if self.module_list is not None:
            for k in self.module_list:
                result['ModuleList'].append(k.to_map() if k else None)
        else:
            result['ModuleList'] = None
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.subscription_type = map.get('SubscriptionType')
        self.region = map.get('Region')
        self.module_list = []
        if map.get('ModuleList') is not None:
            for k in map.get('ModuleList'):
                temp_model = GetPayAsYouGoPriceRequestModuleList()
                self.module_list.append(temp_model.from_map(k))
        else:
            self.module_list = None
        return self


class GetPayAsYouGoPriceRequestModuleList(TeaModel):
    def __init__(self, module_code=None, config=None, price_type=None):
        self.module_code = module_code  # type: str
        self.config = config            # type: str
        self.price_type = price_type    # type: str

    def validate(self):
        self.validate_required(self.module_code, 'module_code')
        self.validate_required(self.config, 'config')
        self.validate_required(self.price_type, 'price_type')

    def to_map(self):
        result = {}
        result['ModuleCode'] = self.module_code
        result['Config'] = self.config
        result['PriceType'] = self.price_type
        return result

    def from_map(self, map={}):
        self.module_code = map.get('ModuleCode')
        self.config = map.get('Config')
        self.price_type = map.get('PriceType')
        return self


class GetPayAsYouGoPriceResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: GetPayAsYouGoPriceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = GetPayAsYouGoPriceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetPayAsYouGoPriceResponseDataModuleDetailsModuleDetail(TeaModel):
    def __init__(self, module_code=None, original_cost=None, invoice_discount=None, cost_after_discount=None,
                 unit_price=None):
        self.module_code = module_code  # type: str
        self.original_cost = original_cost  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.cost_after_discount = cost_after_discount  # type: float
        self.unit_price = unit_price    # type: float

    def validate(self):
        self.validate_required(self.module_code, 'module_code')
        self.validate_required(self.original_cost, 'original_cost')
        self.validate_required(self.invoice_discount, 'invoice_discount')
        self.validate_required(self.cost_after_discount, 'cost_after_discount')
        self.validate_required(self.unit_price, 'unit_price')

    def to_map(self):
        result = {}
        result['ModuleCode'] = self.module_code
        result['OriginalCost'] = self.original_cost
        result['InvoiceDiscount'] = self.invoice_discount
        result['CostAfterDiscount'] = self.cost_after_discount
        result['UnitPrice'] = self.unit_price
        return result

    def from_map(self, map={}):
        self.module_code = map.get('ModuleCode')
        self.original_cost = map.get('OriginalCost')
        self.invoice_discount = map.get('InvoiceDiscount')
        self.cost_after_discount = map.get('CostAfterDiscount')
        self.unit_price = map.get('UnitPrice')
        return self


class GetPayAsYouGoPriceResponseDataModuleDetails(TeaModel):
    def __init__(self, module_detail=None):
        self.module_detail = module_detail  # type: List[GetPayAsYouGoPriceResponseDataModuleDetailsModuleDetail]

    def validate(self):
        self.validate_required(self.module_detail, 'module_detail')
        if self.module_detail:
            for k in self.module_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ModuleDetail'] = []
        if self.module_detail is not None:
            for k in self.module_detail:
                result['ModuleDetail'].append(k.to_map() if k else None)
        else:
            result['ModuleDetail'] = None
        return result

    def from_map(self, map={}):
        self.module_detail = []
        if map.get('ModuleDetail') is not None:
            for k in map.get('ModuleDetail'):
                temp_model = GetPayAsYouGoPriceResponseDataModuleDetailsModuleDetail()
                self.module_detail.append(temp_model.from_map(k))
        else:
            self.module_detail = None
        return self


class GetPayAsYouGoPriceResponseDataPromotionDetailsPromotionDetail(TeaModel):
    def __init__(self, promotion_name=None, promotion_desc=None, promotion_id=None):
        self.promotion_name = promotion_name  # type: str
        self.promotion_desc = promotion_desc  # type: str
        self.promotion_id = promotion_id  # type: int

    def validate(self):
        self.validate_required(self.promotion_name, 'promotion_name')
        self.validate_required(self.promotion_desc, 'promotion_desc')
        self.validate_required(self.promotion_id, 'promotion_id')

    def to_map(self):
        result = {}
        result['PromotionName'] = self.promotion_name
        result['PromotionDesc'] = self.promotion_desc
        result['PromotionId'] = self.promotion_id
        return result

    def from_map(self, map={}):
        self.promotion_name = map.get('PromotionName')
        self.promotion_desc = map.get('PromotionDesc')
        self.promotion_id = map.get('PromotionId')
        return self


class GetPayAsYouGoPriceResponseDataPromotionDetails(TeaModel):
    def __init__(self, promotion_detail=None):
        self.promotion_detail = promotion_detail  # type: List[GetPayAsYouGoPriceResponseDataPromotionDetailsPromotionDetail]

    def validate(self):
        self.validate_required(self.promotion_detail, 'promotion_detail')
        if self.promotion_detail:
            for k in self.promotion_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PromotionDetail'] = []
        if self.promotion_detail is not None:
            for k in self.promotion_detail:
                result['PromotionDetail'].append(k.to_map() if k else None)
        else:
            result['PromotionDetail'] = None
        return result

    def from_map(self, map={}):
        self.promotion_detail = []
        if map.get('PromotionDetail') is not None:
            for k in map.get('PromotionDetail'):
                temp_model = GetPayAsYouGoPriceResponseDataPromotionDetailsPromotionDetail()
                self.promotion_detail.append(temp_model.from_map(k))
        else:
            self.promotion_detail = None
        return self


class GetPayAsYouGoPriceResponseData(TeaModel):
    def __init__(self, currency=None, module_details=None, promotion_details=None):
        self.currency = currency        # type: str
        self.module_details = module_details  # type: GetPayAsYouGoPriceResponseDataModuleDetails
        self.promotion_details = promotion_details  # type: GetPayAsYouGoPriceResponseDataPromotionDetails

    def validate(self):
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.module_details, 'module_details')
        if self.module_details:
            self.module_details.validate()
        self.validate_required(self.promotion_details, 'promotion_details')
        if self.promotion_details:
            self.promotion_details.validate()

    def to_map(self):
        result = {}
        result['Currency'] = self.currency
        if self.module_details is not None:
            result['ModuleDetails'] = self.module_details.to_map()
        else:
            result['ModuleDetails'] = None
        if self.promotion_details is not None:
            result['PromotionDetails'] = self.promotion_details.to_map()
        else:
            result['PromotionDetails'] = None
        return result

    def from_map(self, map={}):
        self.currency = map.get('Currency')
        if map.get('ModuleDetails') is not None:
            temp_model = GetPayAsYouGoPriceResponseDataModuleDetails()
            self.module_details = temp_model.from_map(map['ModuleDetails'])
        else:
            self.module_details = None
        if map.get('PromotionDetails') is not None:
            temp_model = GetPayAsYouGoPriceResponseDataPromotionDetails()
            self.promotion_details = temp_model.from_map(map['PromotionDetails'])
        else:
            self.promotion_details = None
        return self


class QueryPrepaidCardsRequest(TeaModel):
    def __init__(self, expiry_time_end=None, expiry_time_start=None, effective_or_not=None):
        self.expiry_time_end = expiry_time_end  # type: str
        self.expiry_time_start = expiry_time_start  # type: str
        self.effective_or_not = effective_or_not  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ExpiryTimeEnd'] = self.expiry_time_end
        result['ExpiryTimeStart'] = self.expiry_time_start
        result['EffectiveOrNot'] = self.effective_or_not
        return result

    def from_map(self, map={}):
        self.expiry_time_end = map.get('ExpiryTimeEnd')
        self.expiry_time_start = map.get('ExpiryTimeStart')
        self.effective_or_not = map.get('EffectiveOrNot')
        return self


class QueryPrepaidCardsResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryPrepaidCardsResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryPrepaidCardsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryPrepaidCardsResponseDataPrepaidCard(TeaModel):
    def __init__(self, prepaid_card_id=None, prepaid_card_no=None, granted_time=None, effective_time=None,
                 expiry_time=None, applicable_products=None, applicable_scenarios=None, nominal_value=None, balance=None,
                 status=None):
        self.prepaid_card_id = prepaid_card_id  # type: int
        self.prepaid_card_no = prepaid_card_no  # type: str
        self.granted_time = granted_time  # type: str
        self.effective_time = effective_time  # type: str
        self.expiry_time = expiry_time  # type: str
        self.applicable_products = applicable_products  # type: str
        self.applicable_scenarios = applicable_scenarios  # type: str
        self.nominal_value = nominal_value  # type: str
        self.balance = balance          # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.prepaid_card_id, 'prepaid_card_id')
        self.validate_required(self.prepaid_card_no, 'prepaid_card_no')
        self.validate_required(self.granted_time, 'granted_time')
        self.validate_required(self.effective_time, 'effective_time')
        self.validate_required(self.expiry_time, 'expiry_time')
        self.validate_required(self.applicable_products, 'applicable_products')
        self.validate_required(self.applicable_scenarios, 'applicable_scenarios')
        self.validate_required(self.nominal_value, 'nominal_value')
        self.validate_required(self.balance, 'balance')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['PrepaidCardId'] = self.prepaid_card_id
        result['PrepaidCardNo'] = self.prepaid_card_no
        result['GrantedTime'] = self.granted_time
        result['EffectiveTime'] = self.effective_time
        result['ExpiryTime'] = self.expiry_time
        result['ApplicableProducts'] = self.applicable_products
        result['ApplicableScenarios'] = self.applicable_scenarios
        result['NominalValue'] = self.nominal_value
        result['Balance'] = self.balance
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.prepaid_card_id = map.get('PrepaidCardId')
        self.prepaid_card_no = map.get('PrepaidCardNo')
        self.granted_time = map.get('GrantedTime')
        self.effective_time = map.get('EffectiveTime')
        self.expiry_time = map.get('ExpiryTime')
        self.applicable_products = map.get('ApplicableProducts')
        self.applicable_scenarios = map.get('ApplicableScenarios')
        self.nominal_value = map.get('NominalValue')
        self.balance = map.get('Balance')
        self.status = map.get('Status')
        return self


class QueryPrepaidCardsResponseData(TeaModel):
    def __init__(self, prepaid_card=None):
        self.prepaid_card = prepaid_card  # type: List[QueryPrepaidCardsResponseDataPrepaidCard]

    def validate(self):
        self.validate_required(self.prepaid_card, 'prepaid_card')
        if self.prepaid_card:
            for k in self.prepaid_card:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PrepaidCard'] = []
        if self.prepaid_card is not None:
            for k in self.prepaid_card:
                result['PrepaidCard'].append(k.to_map() if k else None)
        else:
            result['PrepaidCard'] = None
        return result

    def from_map(self, map={}):
        self.prepaid_card = []
        if map.get('PrepaidCard') is not None:
            for k in map.get('PrepaidCard'):
                temp_model = QueryPrepaidCardsResponseDataPrepaidCard()
                self.prepaid_card.append(temp_model.from_map(k))
        else:
            self.prepaid_card = None
        return self


class QueryCashCouponsRequest(TeaModel):
    def __init__(self, expiry_time_end=None, expiry_time_start=None, effective_or_not=None):
        self.expiry_time_end = expiry_time_end  # type: str
        self.expiry_time_start = expiry_time_start  # type: str
        self.effective_or_not = effective_or_not  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ExpiryTimeEnd'] = self.expiry_time_end
        result['ExpiryTimeStart'] = self.expiry_time_start
        result['EffectiveOrNot'] = self.effective_or_not
        return result

    def from_map(self, map={}):
        self.expiry_time_end = map.get('ExpiryTimeEnd')
        self.expiry_time_start = map.get('ExpiryTimeStart')
        self.effective_or_not = map.get('EffectiveOrNot')
        return self


class QueryCashCouponsResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryCashCouponsResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryCashCouponsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryCashCouponsResponseDataCashCoupon(TeaModel):
    def __init__(self, cash_coupon_id=None, cash_coupon_no=None, granted_time=None, effective_time=None,
                 expiry_time=None, applicable_products=None, applicable_scenarios=None, nominal_value=None, balance=None,
                 status=None):
        self.cash_coupon_id = cash_coupon_id  # type: int
        self.cash_coupon_no = cash_coupon_no  # type: str
        self.granted_time = granted_time  # type: str
        self.effective_time = effective_time  # type: str
        self.expiry_time = expiry_time  # type: str
        self.applicable_products = applicable_products  # type: str
        self.applicable_scenarios = applicable_scenarios  # type: str
        self.nominal_value = nominal_value  # type: str
        self.balance = balance          # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.cash_coupon_id, 'cash_coupon_id')
        self.validate_required(self.cash_coupon_no, 'cash_coupon_no')
        self.validate_required(self.granted_time, 'granted_time')
        self.validate_required(self.effective_time, 'effective_time')
        self.validate_required(self.expiry_time, 'expiry_time')
        self.validate_required(self.applicable_products, 'applicable_products')
        self.validate_required(self.applicable_scenarios, 'applicable_scenarios')
        self.validate_required(self.nominal_value, 'nominal_value')
        self.validate_required(self.balance, 'balance')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['CashCouponId'] = self.cash_coupon_id
        result['CashCouponNo'] = self.cash_coupon_no
        result['GrantedTime'] = self.granted_time
        result['EffectiveTime'] = self.effective_time
        result['ExpiryTime'] = self.expiry_time
        result['ApplicableProducts'] = self.applicable_products
        result['ApplicableScenarios'] = self.applicable_scenarios
        result['NominalValue'] = self.nominal_value
        result['Balance'] = self.balance
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.cash_coupon_id = map.get('CashCouponId')
        self.cash_coupon_no = map.get('CashCouponNo')
        self.granted_time = map.get('GrantedTime')
        self.effective_time = map.get('EffectiveTime')
        self.expiry_time = map.get('ExpiryTime')
        self.applicable_products = map.get('ApplicableProducts')
        self.applicable_scenarios = map.get('ApplicableScenarios')
        self.nominal_value = map.get('NominalValue')
        self.balance = map.get('Balance')
        self.status = map.get('Status')
        return self


class QueryCashCouponsResponseData(TeaModel):
    def __init__(self, cash_coupon=None):
        self.cash_coupon = cash_coupon  # type: List[QueryCashCouponsResponseDataCashCoupon]

    def validate(self):
        self.validate_required(self.cash_coupon, 'cash_coupon')
        if self.cash_coupon:
            for k in self.cash_coupon:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CashCoupon'] = []
        if self.cash_coupon is not None:
            for k in self.cash_coupon:
                result['CashCoupon'].append(k.to_map() if k else None)
        else:
            result['CashCoupon'] = None
        return result

    def from_map(self, map={}):
        self.cash_coupon = []
        if map.get('CashCoupon') is not None:
            for k in map.get('CashCoupon'):
                temp_model = QueryCashCouponsResponseDataCashCoupon()
                self.cash_coupon.append(temp_model.from_map(k))
        else:
            self.cash_coupon = None
        return self


class QueryAccountBalanceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class QueryAccountBalanceResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: QueryAccountBalanceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = QueryAccountBalanceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class QueryAccountBalanceResponseData(TeaModel):
    def __init__(self, available_amount=None, available_cash_amount=None, credit_amount=None,
                 mybank_credit_amount=None, currency=None):
        self.available_amount = available_amount  # type: str
        self.available_cash_amount = available_cash_amount  # type: str
        self.credit_amount = credit_amount  # type: str
        self.mybank_credit_amount = mybank_credit_amount  # type: str
        self.currency = currency        # type: str

    def validate(self):
        self.validate_required(self.available_amount, 'available_amount')
        self.validate_required(self.available_cash_amount, 'available_cash_amount')
        self.validate_required(self.credit_amount, 'credit_amount')
        self.validate_required(self.mybank_credit_amount, 'mybank_credit_amount')
        self.validate_required(self.currency, 'currency')

    def to_map(self):
        result = {}
        result['AvailableAmount'] = self.available_amount
        result['AvailableCashAmount'] = self.available_cash_amount
        result['CreditAmount'] = self.credit_amount
        result['MybankCreditAmount'] = self.mybank_credit_amount
        result['Currency'] = self.currency
        return result

    def from_map(self, map={}):
        self.available_amount = map.get('AvailableAmount')
        self.available_cash_amount = map.get('AvailableCashAmount')
        self.credit_amount = map.get('CreditAmount')
        self.mybank_credit_amount = map.get('MybankCreditAmount')
        self.currency = map.get('Currency')
        return self


class DescribeResourcePackageProductRequest(TeaModel):
    def __init__(self, product_code=None):
        self.product_code = product_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        return self


class DescribeResourcePackageProductResponse(TeaModel):
    def __init__(self, request_id=None, order_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.order_id = order_id        # type: int
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: DescribeResourcePackageProductResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrderId'] = self.order_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.order_id = map.get('OrderId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = DescribeResourcePackageProductResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypePropertiesProperty(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name                # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.value = map.get('Value')
        return self


class DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeProperties(TeaModel):
    def __init__(self, property=None):
        self.property = property        # type: List[DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypePropertiesProperty]

    def validate(self):
        self.validate_required(self.property, 'property')
        if self.property:
            for k in self.property:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Property'] = []
        if self.property is not None:
            for k in self.property:
                result['Property'].append(k.to_map() if k else None)
        else:
            result['Property'] = None
        return result

    def from_map(self, map={}):
        self.property = []
        if map.get('Property') is not None:
            for k in map.get('Property'):
                temp_model = DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypePropertiesProperty()
                self.property.append(temp_model.from_map(k))
        else:
            self.property = None
        return self


class DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurationsAvailableDuration(TeaModel):
    def __init__(self, name=None, value=None, unit=None):
        self.name = name                # type: str
        self.value = value              # type: int
        self.unit = unit                # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.value, 'value')
        self.validate_required(self.unit, 'unit')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Value'] = self.value
        result['Unit'] = self.unit
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.value = map.get('Value')
        self.unit = map.get('Unit')
        return self


class DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurations(TeaModel):
    def __init__(self, available_duration=None):
        self.available_duration = available_duration  # type: List[DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurationsAvailableDuration]

    def validate(self):
        self.validate_required(self.available_duration, 'available_duration')
        if self.available_duration:
            for k in self.available_duration:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AvailableDuration'] = []
        if self.available_duration is not None:
            for k in self.available_duration:
                result['AvailableDuration'].append(k.to_map() if k else None)
        else:
            result['AvailableDuration'] = None
        return result

    def from_map(self, map={}):
        self.available_duration = []
        if map.get('AvailableDuration') is not None:
            for k in map.get('AvailableDuration'):
                temp_model = DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurationsAvailableDuration()
                self.available_duration.append(temp_model.from_map(k))
        else:
            self.available_duration = None
        return self


class DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecification(TeaModel):
    def __init__(self, name=None, value=None, available_durations=None):
        self.name = name                # type: str
        self.value = value              # type: str
        self.available_durations = available_durations  # type: DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurations

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.value, 'value')
        self.validate_required(self.available_durations, 'available_durations')
        if self.available_durations:
            self.available_durations.validate()

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Value'] = self.value
        if self.available_durations is not None:
            result['AvailableDurations'] = self.available_durations.to_map()
        else:
            result['AvailableDurations'] = None
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.value = map.get('Value')
        if map.get('AvailableDurations') is not None:
            temp_model = DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurations()
            self.available_durations = temp_model.from_map(map['AvailableDurations'])
        else:
            self.available_durations = None
        return self


class DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecifications(TeaModel):
    def __init__(self, specification=None):
        self.specification = specification  # type: List[DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecification]

    def validate(self):
        self.validate_required(self.specification, 'specification')
        if self.specification:
            for k in self.specification:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Specification'] = []
        if self.specification is not None:
            for k in self.specification:
                result['Specification'].append(k.to_map() if k else None)
        else:
            result['Specification'] = None
        return result

    def from_map(self, map={}):
        self.specification = []
        if map.get('Specification') is not None:
            for k in map.get('Specification'):
                temp_model = DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecification()
                self.specification.append(temp_model.from_map(k))
        else:
            self.specification = None
        return self


class DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageType(TeaModel):
    def __init__(self, name=None, code=None, properties=None, specifications=None):
        self.name = name                # type: str
        self.code = code                # type: str
        self.properties = properties    # type: DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeProperties
        self.specifications = specifications  # type: DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecifications

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.code, 'code')
        self.validate_required(self.properties, 'properties')
        if self.properties:
            self.properties.validate()
        self.validate_required(self.specifications, 'specifications')
        if self.specifications:
            self.specifications.validate()

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Code'] = self.code
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        else:
            result['Properties'] = None
        if self.specifications is not None:
            result['Specifications'] = self.specifications.to_map()
        else:
            result['Specifications'] = None
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.code = map.get('Code')
        if map.get('Properties') is not None:
            temp_model = DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeProperties()
            self.properties = temp_model.from_map(map['Properties'])
        else:
            self.properties = None
        if map.get('Specifications') is not None:
            temp_model = DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecifications()
            self.specifications = temp_model.from_map(map['Specifications'])
        else:
            self.specifications = None
        return self


class DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypes(TeaModel):
    def __init__(self, package_type=None):
        self.package_type = package_type  # type: List[DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageType]

    def validate(self):
        self.validate_required(self.package_type, 'package_type')
        if self.package_type:
            for k in self.package_type:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PackageType'] = []
        if self.package_type is not None:
            for k in self.package_type:
                result['PackageType'].append(k.to_map() if k else None)
        else:
            result['PackageType'] = None
        return result

    def from_map(self, map={}):
        self.package_type = []
        if map.get('PackageType') is not None:
            for k in map.get('PackageType'):
                temp_model = DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypesPackageType()
                self.package_type.append(temp_model.from_map(k))
        else:
            self.package_type = None
        return self


class DescribeResourcePackageProductResponseDataResourcePackagesResourcePackage(TeaModel):
    def __init__(self, product_code=None, product_type=None, name=None, package_types=None):
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.name = name                # type: str
        self.package_types = package_types  # type: DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypes

    def validate(self):
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.product_type, 'product_type')
        self.validate_required(self.name, 'name')
        self.validate_required(self.package_types, 'package_types')
        if self.package_types:
            self.package_types.validate()

    def to_map(self):
        result = {}
        result['ProductCode'] = self.product_code
        result['ProductType'] = self.product_type
        result['Name'] = self.name
        if self.package_types is not None:
            result['PackageTypes'] = self.package_types.to_map()
        else:
            result['PackageTypes'] = None
        return result

    def from_map(self, map={}):
        self.product_code = map.get('ProductCode')
        self.product_type = map.get('ProductType')
        self.name = map.get('Name')
        if map.get('PackageTypes') is not None:
            temp_model = DescribeResourcePackageProductResponseDataResourcePackagesResourcePackagePackageTypes()
            self.package_types = temp_model.from_map(map['PackageTypes'])
        else:
            self.package_types = None
        return self


class DescribeResourcePackageProductResponseDataResourcePackages(TeaModel):
    def __init__(self, resource_package=None):
        self.resource_package = resource_package  # type: List[DescribeResourcePackageProductResponseDataResourcePackagesResourcePackage]

    def validate(self):
        self.validate_required(self.resource_package, 'resource_package')
        if self.resource_package:
            for k in self.resource_package:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResourcePackage'] = []
        if self.resource_package is not None:
            for k in self.resource_package:
                result['ResourcePackage'].append(k.to_map() if k else None)
        else:
            result['ResourcePackage'] = None
        return result

    def from_map(self, map={}):
        self.resource_package = []
        if map.get('ResourcePackage') is not None:
            for k in map.get('ResourcePackage'):
                temp_model = DescribeResourcePackageProductResponseDataResourcePackagesResourcePackage()
                self.resource_package.append(temp_model.from_map(k))
        else:
            self.resource_package = None
        return self


class DescribeResourcePackageProductResponseData(TeaModel):
    def __init__(self, resource_packages=None):
        self.resource_packages = resource_packages  # type: DescribeResourcePackageProductResponseDataResourcePackages

    def validate(self):
        self.validate_required(self.resource_packages, 'resource_packages')
        if self.resource_packages:
            self.resource_packages.validate()

    def to_map(self):
        result = {}
        if self.resource_packages is not None:
            result['ResourcePackages'] = self.resource_packages.to_map()
        else:
            result['ResourcePackages'] = None
        return result

    def from_map(self, map={}):
        if map.get('ResourcePackages') is not None:
            temp_model = DescribeResourcePackageProductResponseDataResourcePackages()
            self.resource_packages = temp_model.from_map(map['ResourcePackages'])
        else:
            self.resource_packages = None
        return self


