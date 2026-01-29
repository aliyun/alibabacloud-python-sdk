# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAccountBillRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        billing_cycle: str = None,
        billing_date: str = None,
        granularity: str = None,
        is_group_by_product: bool = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        product_code: str = None,
    ):
        # The ID of the member. If you specify a value for this parameter, you can query the bills of the specified member. If you leave this parameter empty, the bills of the current account are queried by default.
        self.bill_owner_id = bill_owner_id
        # The billing cycle. Format: YYYY-MM.
        # 
        # This parameter is required.
        self.billing_cycle = billing_cycle
        # The billing date. This parameter is required only if the Granularity parameter is set to DAILY. Format: YYYY-MM-DD.
        self.billing_date = billing_date
        # The granularity at which bills are queried. Valid values:
        # 
        # *   MONTHLY: queries bills by month. The data queried is consistent with the data that is displayed for the specified billing cycle on the Billing Details tab of the Bill Details page in User Center.
        # *   DAILY: queries bills by day. The data queried is consistent with the data that is displayed for the specified day on the Billing Details tab of the Bill Details page in User Center.
        # 
        # You must set the BillingDate parameter before you can set the Granularity parameter to DAILY.
        self.granularity = granularity
        # Specifies whether to summarize bills based on service codes. Valid values:
        # 
        # *   true: summarizes bills based on service codes.
        # *   false: does not summarize bills based on service codes.
        # 
        # Default value: false.
        self.is_group_by_product = is_group_by_product
        self.owner_id = owner_id
        # The number of the page to return. Default value: 1.
        self.page_num = page_num
        # The number of entries to return on each page. Default value: 20. Maximum value: 300.
        self.page_size = page_size
        # The code of the service.
        self.product_code = product_code

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

        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.is_group_by_product is not None:
            result['IsGroupByProduct'] = self.is_group_by_product

        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('IsGroupByProduct') is not None:
            self.is_group_by_product = m.get('IsGroupByProduct')

        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

