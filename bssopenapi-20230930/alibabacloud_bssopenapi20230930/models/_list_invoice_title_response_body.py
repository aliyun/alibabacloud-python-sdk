# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ListInvoiceTitleResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListInvoiceTitleResponseBodyData] = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListInvoiceTitleResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInvoiceTitleResponseBodyData(DaraModel):
    def __init__(
        self,
        account_bank_name: str = None,
        account_id: int = None,
        bank_account_number: str = None,
        create_time: str = None,
        id: str = None,
        invoice_title: str = None,
        registered_address: str = None,
        registered_landline: str = None,
        unified_social_credit_code: str = None,
    ):
        self.account_bank_name = account_bank_name
        self.account_id = account_id
        self.bank_account_number = bank_account_number
        self.create_time = create_time
        self.id = id
        self.invoice_title = invoice_title
        self.registered_address = registered_address
        self.registered_landline = registered_landline
        self.unified_social_credit_code = unified_social_credit_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_bank_name is not None:
            result['AccountBankName'] = self.account_bank_name

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.bank_account_number is not None:
            result['BankAccountNumber'] = self.bank_account_number

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.invoice_title is not None:
            result['InvoiceTitle'] = self.invoice_title

        if self.registered_address is not None:
            result['RegisteredAddress'] = self.registered_address

        if self.registered_landline is not None:
            result['RegisteredLandline'] = self.registered_landline

        if self.unified_social_credit_code is not None:
            result['UnifiedSocialCreditCode'] = self.unified_social_credit_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountBankName') is not None:
            self.account_bank_name = m.get('AccountBankName')

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('BankAccountNumber') is not None:
            self.bank_account_number = m.get('BankAccountNumber')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InvoiceTitle') is not None:
            self.invoice_title = m.get('InvoiceTitle')

        if m.get('RegisteredAddress') is not None:
            self.registered_address = m.get('RegisteredAddress')

        if m.get('RegisteredLandline') is not None:
            self.registered_landline = m.get('RegisteredLandline')

        if m.get('UnifiedSocialCreditCode') is not None:
            self.unified_social_credit_code = m.get('UnifiedSocialCreditCode')

        return self

