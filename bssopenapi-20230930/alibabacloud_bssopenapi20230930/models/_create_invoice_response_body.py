# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class CreateInvoiceResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.CreateInvoiceResponseBodyData] = None,
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
                temp_model = main_models.CreateInvoiceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateInvoiceResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        amount: str = None,
        error_code: str = None,
        invoice_issuer: str = None,
        message: str = None,
    ):
        self.account_id = account_id
        self.amount = amount
        self.error_code = error_code
        self.invoice_issuer = invoice_issuer
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.amount is not None:
            result['Amount'] = self.amount

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.invoice_issuer is not None:
            result['InvoiceIssuer'] = self.invoice_issuer

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('InvoiceIssuer') is not None:
            self.invoice_issuer = m.get('InvoiceIssuer')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

