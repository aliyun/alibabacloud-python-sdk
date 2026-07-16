# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInvoiceForIsvRequest(DaraModel):
    def __init__(
        self,
        check_notice: str = None,
        electron_url: str = None,
        invoice_id: int = None,
        number: str = None,
        operate_type: int = None,
        type: int = None,
    ):
        self.check_notice = check_notice
        self.electron_url = electron_url
        self.invoice_id = invoice_id
        self.number = number
        # This parameter is required.
        self.operate_type = operate_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_notice is not None:
            result['CheckNotice'] = self.check_notice

        if self.electron_url is not None:
            result['ElectronUrl'] = self.electron_url

        if self.invoice_id is not None:
            result['InvoiceId'] = self.invoice_id

        if self.number is not None:
            result['Number'] = self.number

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckNotice') is not None:
            self.check_notice = m.get('CheckNotice')

        if m.get('ElectronUrl') is not None:
            self.electron_url = m.get('ElectronUrl')

        if m.get('InvoiceId') is not None:
            self.invoice_id = m.get('InvoiceId')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

