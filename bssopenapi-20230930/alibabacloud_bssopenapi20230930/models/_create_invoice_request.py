# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class CreateInvoiceRequest(DaraModel):
    def __init__(
        self,
        amount: str = None,
        ec_id_account_ids: List[main_models.CreateInvoiceRequestEcIdAccountIds] = None,
        invoice_candidate_ids: List[str] = None,
        invoice_mode: int = None,
        invoice_remark: str = None,
        invoice_title_id: str = None,
        invoice_type: int = None,
        nbid: str = None,
        recipient_emails: List[str] = None,
    ):
        self.amount = amount
        self.ec_id_account_ids = ec_id_account_ids
        # This parameter is required.
        self.invoice_candidate_ids = invoice_candidate_ids
        # This parameter is required.
        self.invoice_mode = invoice_mode
        self.invoice_remark = invoice_remark
        # This parameter is required.
        self.invoice_title_id = invoice_title_id
        # This parameter is required.
        self.invoice_type = invoice_type
        self.nbid = nbid
        # This parameter is required.
        self.recipient_emails = recipient_emails

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
        if self.amount is not None:
            result['Amount'] = self.amount

        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k1 in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k1.to_map() if k1 else None)

        if self.invoice_candidate_ids is not None:
            result['InvoiceCandidateIds'] = self.invoice_candidate_ids

        if self.invoice_mode is not None:
            result['InvoiceMode'] = self.invoice_mode

        if self.invoice_remark is not None:
            result['InvoiceRemark'] = self.invoice_remark

        if self.invoice_title_id is not None:
            result['InvoiceTitleId'] = self.invoice_title_id

        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.recipient_emails is not None:
            result['RecipientEmails'] = self.recipient_emails

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.CreateInvoiceRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('InvoiceCandidateIds') is not None:
            self.invoice_candidate_ids = m.get('InvoiceCandidateIds')

        if m.get('InvoiceMode') is not None:
            self.invoice_mode = m.get('InvoiceMode')

        if m.get('InvoiceRemark') is not None:
            self.invoice_remark = m.get('InvoiceRemark')

        if m.get('InvoiceTitleId') is not None:
            self.invoice_title_id = m.get('InvoiceTitleId')

        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('RecipientEmails') is not None:
            self.recipient_emails = m.get('RecipientEmails')

        return self

class CreateInvoiceRequestEcIdAccountIds(DaraModel):
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

