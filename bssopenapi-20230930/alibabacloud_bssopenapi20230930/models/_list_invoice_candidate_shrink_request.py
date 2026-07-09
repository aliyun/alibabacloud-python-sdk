# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInvoiceCandidateShrinkRequest(DaraModel):
    def __init__(
        self,
        billing_cycles_shrink: str = None,
        business_ids_shrink: str = None,
        current_page: int = None,
        ec_id_account_ids_shrink: str = None,
        end_time: str = None,
        invoice_issuers_shrink: str = None,
        nbid: str = None,
        page_size: int = None,
        start_time: str = None,
        status_shrink: str = None,
        types_shrink: str = None,
    ):
        # List of billing cycles.
        self.billing_cycles_shrink = billing_cycles_shrink
        # List of business document numbers.
        self.business_ids_shrink = business_ids_shrink
        # The current page number.
        self.current_page = current_page
        # List of enterprises and accounts. If empty, the current account itself is queried.
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        # The end time. Format: yyyy-mm-dd hh:mm:ss.
        self.end_time = end_time
        # List of invoice issuers.
        self.invoice_issuers_shrink = invoice_issuers_shrink
        # Primary marketplace ID. If empty, the marketplace ID of the current user is used by default.
        self.nbid = nbid
        # The number of entries per page.
        self.page_size = page_size
        # The start time. Format: yyyy-mm-dd hh:mm:ss.
        self.start_time = start_time
        # List of invoice candidate statuses.
        self.status_shrink = status_shrink
        # List of invoice candidate types.
        self.types_shrink = types_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_cycles_shrink is not None:
            result['BillingCycles'] = self.billing_cycles_shrink

        if self.business_ids_shrink is not None:
            result['BusinessIds'] = self.business_ids_shrink

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.invoice_issuers_shrink is not None:
            result['InvoiceIssuers'] = self.invoice_issuers_shrink

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status_shrink is not None:
            result['Status'] = self.status_shrink

        if self.types_shrink is not None:
            result['Types'] = self.types_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycles') is not None:
            self.billing_cycles_shrink = m.get('BillingCycles')

        if m.get('BusinessIds') is not None:
            self.business_ids_shrink = m.get('BusinessIds')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InvoiceIssuers') is not None:
            self.invoice_issuers_shrink = m.get('InvoiceIssuers')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status_shrink = m.get('Status')

        if m.get('Types') is not None:
            self.types_shrink = m.get('Types')

        return self

