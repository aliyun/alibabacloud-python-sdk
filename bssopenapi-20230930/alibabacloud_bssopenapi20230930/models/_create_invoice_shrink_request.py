# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInvoiceShrinkRequest(DaraModel):
    def __init__(
        self,
        amount: str = None,
        ec_id_account_ids_shrink: str = None,
        invoice_candidate_ids_shrink: str = None,
        invoice_mode: int = None,
        invoice_remark: str = None,
        invoice_title_id: str = None,
        invoice_type: int = None,
        nbid: str = None,
        recipient_emails_shrink: str = None,
    ):
        self.amount = amount
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        # This parameter is required.
        self.invoice_candidate_ids_shrink = invoice_candidate_ids_shrink
        # This parameter is required.
        self.invoice_mode = invoice_mode
        self.invoice_remark = invoice_remark
        # This parameter is required.
        self.invoice_title_id = invoice_title_id
        # This parameter is required.
        self.invoice_type = invoice_type
        self.nbid = nbid
        # This parameter is required.
        self.recipient_emails_shrink = recipient_emails_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink

        if self.invoice_candidate_ids_shrink is not None:
            result['InvoiceCandidateIds'] = self.invoice_candidate_ids_shrink

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

        if self.recipient_emails_shrink is not None:
            result['RecipientEmails'] = self.recipient_emails_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')

        if m.get('InvoiceCandidateIds') is not None:
            self.invoice_candidate_ids_shrink = m.get('InvoiceCandidateIds')

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
            self.recipient_emails_shrink = m.get('RecipientEmails')

        return self

