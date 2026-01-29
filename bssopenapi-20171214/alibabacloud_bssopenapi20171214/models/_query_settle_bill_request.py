# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySettleBillRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        billing_cycle: str = None,
        is_display_local_currency: bool = None,
        is_hide_zero_charge: bool = None,
        max_results: int = None,
        next_token: str = None,
        owner_id: int = None,
        product_code: str = None,
        product_type: str = None,
        record_id: str = None,
        subscription_type: str = None,
        type: str = None,
    ):
        self.bill_owner_id = bill_owner_id
        # This parameter is required.
        self.billing_cycle = billing_cycle
        self.is_display_local_currency = is_display_local_currency
        self.is_hide_zero_charge = is_hide_zero_charge
        self.max_results = max_results
        self.next_token = next_token
        self.owner_id = owner_id
        self.product_code = product_code
        self.product_type = product_type
        self.record_id = record_id
        self.subscription_type = subscription_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.is_display_local_currency is not None:
            result['IsDisplayLocalCurrency'] = self.is_display_local_currency

        if self.is_hide_zero_charge is not None:
            result['IsHideZeroCharge'] = self.is_hide_zero_charge

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.record_id is not None:
            result['RecordID'] = self.record_id

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('IsDisplayLocalCurrency') is not None:
            self.is_display_local_currency = m.get('IsDisplayLocalCurrency')

        if m.get('IsHideZeroCharge') is not None:
            self.is_hide_zero_charge = m.get('IsHideZeroCharge')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

