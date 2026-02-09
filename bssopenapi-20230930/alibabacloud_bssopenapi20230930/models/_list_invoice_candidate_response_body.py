# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ListInvoiceCandidateResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.ListInvoiceCandidateResponseBodyData] = None,
        metadata: Any = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.metadata = metadata
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListInvoiceCandidateResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInvoiceCandidateResponseBodyData(DaraModel):
    def __init__(
        self,
        accepted_offset_amount: str = None,
        account_id: int = None,
        account_name: str = None,
        billing_cycle: int = None,
        business_id: str = None,
        business_time: str = None,
        commodity_code: str = None,
        commodity_name: str = None,
        create_time: str = None,
        id: str = None,
        invoice_issuer: str = None,
        invoiceable_amount: str = None,
        invoiced_amount: str = None,
        offset_amount: str = None,
        product_code: str = None,
        product_name: str = None,
        resource_owner_account_id: int = None,
        resource_owner_account_name: str = None,
        status: int = None,
        total_amount: str = None,
        type: int = None,
    ):
        self.accepted_offset_amount = accepted_offset_amount
        self.account_id = account_id
        self.account_name = account_name
        self.billing_cycle = billing_cycle
        self.business_id = business_id
        self.business_time = business_time
        self.commodity_code = commodity_code
        self.commodity_name = commodity_name
        self.create_time = create_time
        self.id = id
        self.invoice_issuer = invoice_issuer
        self.invoiceable_amount = invoiceable_amount
        self.invoiced_amount = invoiced_amount
        self.offset_amount = offset_amount
        self.product_code = product_code
        self.product_name = product_name
        self.resource_owner_account_id = resource_owner_account_id
        self.resource_owner_account_name = resource_owner_account_name
        self.status = status
        self.total_amount = total_amount
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accepted_offset_amount is not None:
            result['AcceptedOffsetAmount'] = self.accepted_offset_amount

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.business_time is not None:
            result['BusinessTime'] = self.business_time

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.invoice_issuer is not None:
            result['InvoiceIssuer'] = self.invoice_issuer

        if self.invoiceable_amount is not None:
            result['InvoiceableAmount'] = self.invoiceable_amount

        if self.invoiced_amount is not None:
            result['InvoicedAmount'] = self.invoiced_amount

        if self.offset_amount is not None:
            result['OffsetAmount'] = self.offset_amount

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.resource_owner_account_id is not None:
            result['ResourceOwnerAccountId'] = self.resource_owner_account_id

        if self.resource_owner_account_name is not None:
            result['ResourceOwnerAccountName'] = self.resource_owner_account_name

        if self.status is not None:
            result['Status'] = self.status

        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptedOffsetAmount') is not None:
            self.accepted_offset_amount = m.get('AcceptedOffsetAmount')

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('BusinessTime') is not None:
            self.business_time = m.get('BusinessTime')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InvoiceIssuer') is not None:
            self.invoice_issuer = m.get('InvoiceIssuer')

        if m.get('InvoiceableAmount') is not None:
            self.invoiceable_amount = m.get('InvoiceableAmount')

        if m.get('InvoicedAmount') is not None:
            self.invoiced_amount = m.get('InvoicedAmount')

        if m.get('OffsetAmount') is not None:
            self.offset_amount = m.get('OffsetAmount')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ResourceOwnerAccountId') is not None:
            self.resource_owner_account_id = m.get('ResourceOwnerAccountId')

        if m.get('ResourceOwnerAccountName') is not None:
            self.resource_owner_account_name = m.get('ResourceOwnerAccountName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

