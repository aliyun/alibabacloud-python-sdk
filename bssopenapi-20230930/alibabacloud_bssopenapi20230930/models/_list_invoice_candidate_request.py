# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ListInvoiceCandidateRequest(DaraModel):
    def __init__(
        self,
        billing_cycles: List[int] = None,
        business_ids: List[str] = None,
        current_page: int = None,
        ec_id_account_ids: List[main_models.ListInvoiceCandidateRequestEcIdAccountIds] = None,
        end_time: str = None,
        invoice_issuers: List[str] = None,
        nbid: str = None,
        page_size: int = None,
        start_time: str = None,
        status: List[int] = None,
        types: List[int] = None,
    ):
        self.billing_cycles = billing_cycles
        self.business_ids = business_ids
        self.current_page = current_page
        self.ec_id_account_ids = ec_id_account_ids
        self.end_time = end_time
        self.invoice_issuers = invoice_issuers
        self.nbid = nbid
        self.page_size = page_size
        self.start_time = start_time
        self.status = status
        self.types = types

    def validate(self):
        if self.ec_id_account_ids:
            for v1 in self.ec_id_account_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_cycles is not None:
            result['BillingCycles'] = self.billing_cycles

        if self.business_ids is not None:
            result['BusinessIds'] = self.business_ids

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k1 in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.invoice_issuers is not None:
            result['InvoiceIssuers'] = self.invoice_issuers

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.types is not None:
            result['Types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycles') is not None:
            self.billing_cycles = m.get('BillingCycles')

        if m.get('BusinessIds') is not None:
            self.business_ids = m.get('BusinessIds')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.ListInvoiceCandidateRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InvoiceIssuers') is not None:
            self.invoice_issuers = m.get('InvoiceIssuers')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        return self

class ListInvoiceCandidateRequestEcIdAccountIds(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.ec_id is not None:
            result['EcId'] = self.ec_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')

        return self

