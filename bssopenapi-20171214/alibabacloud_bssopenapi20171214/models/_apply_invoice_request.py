# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ApplyInvoiceRequest(DaraModel):
    def __init__(
        self,
        address_id: int = None,
        apply_user_nick: str = None,
        customer_id: int = None,
        invoice_amount: int = None,
        invoice_by_amount: bool = None,
        invoicing_type: int = None,
        owner_id: int = None,
        process_way: int = None,
        selected_ids: List[int] = None,
        user_remark: str = None,
        emails: str = None,
    ):
        # The ID of the address to which the invoice is delivered. This parameter is required if the invoice is a paper invoice. Set the ID to the value of the AddressId parameter returned by calling the QueryCustomerAddressList operation.
        # 
        # This parameter is required.
        self.address_id = address_id
        # The nickname of the applicant. The system does not verify the nickname.
        # 
        # This parameter is required.
        self.apply_user_nick = apply_user_nick
        # The ID of the customer. Set the ID to the value of the CustomerId parameter returned by calling the QueryInvoicingCustomerList operation.
        # 
        # This parameter is required.
        self.customer_id = customer_id
        # The amount of the invoice. Unit: Cent.
        # 
        # This parameter is required.
        self.invoice_amount = invoice_amount
        # Specifies whether to invoice by amount. A value of true indicates that the user applies for the invoice based on the InvoiceAmount parameter. A value of false indicates that the user applies for the invoice based on the total amount of the invoicing items.
        self.invoice_by_amount = invoice_by_amount
        # The type of the invoice. Valid values:
        # 
        # *   0: paper invoice
        # *   1: electronic invoice
        self.invoicing_type = invoicing_type
        self.owner_id = owner_id
        # The channel that is used to process the invoice. A value of 0 indicates that the invoice is processed by Alibaba Cloud. A value of 1 indicates that the invoice is processed by the tax platform. Set the value to 1.
        self.process_way = process_way
        # The IDs of the selected invoicing items. Set the IDs to the IDs returned by calling the QueryEvaluateList operation.
        # 
        # This parameter is required.
        self.selected_ids = selected_ids
        # The remarks made by the user.
        self.user_remark = user_remark
        self.emails = emails

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_id is not None:
            result['AddressId'] = self.address_id

        if self.apply_user_nick is not None:
            result['ApplyUserNick'] = self.apply_user_nick

        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id

        if self.invoice_amount is not None:
            result['InvoiceAmount'] = self.invoice_amount

        if self.invoice_by_amount is not None:
            result['InvoiceByAmount'] = self.invoice_by_amount

        if self.invoicing_type is not None:
            result['InvoicingType'] = self.invoicing_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.process_way is not None:
            result['ProcessWay'] = self.process_way

        if self.selected_ids is not None:
            result['SelectedIds'] = self.selected_ids

        if self.user_remark is not None:
            result['UserRemark'] = self.user_remark

        if self.emails is not None:
            result['emails'] = self.emails

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')

        if m.get('ApplyUserNick') is not None:
            self.apply_user_nick = m.get('ApplyUserNick')

        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')

        if m.get('InvoiceAmount') is not None:
            self.invoice_amount = m.get('InvoiceAmount')

        if m.get('InvoiceByAmount') is not None:
            self.invoice_by_amount = m.get('InvoiceByAmount')

        if m.get('InvoicingType') is not None:
            self.invoicing_type = m.get('InvoicingType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProcessWay') is not None:
            self.process_way = m.get('ProcessWay')

        if m.get('SelectedIds') is not None:
            self.selected_ids = m.get('SelectedIds')

        if m.get('UserRemark') is not None:
            self.user_remark = m.get('UserRemark')

        if m.get('emails') is not None:
            self.emails = m.get('emails')

        return self

