# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvoiceModifyRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        bank_name: str = None,
        bank_no: str = None,
        mail_third_part_id: str = None,
        tax_no: str = None,
        tel: str = None,
        third_part_id: str = None,
        title: str = None,
        type: int = None,
        unit_type: int = None,
    ):
        self.address = address
        self.bank_name = bank_name
        self.bank_no = bank_no
        self.mail_third_part_id = mail_third_part_id
        self.tax_no = tax_no
        self.tel = tel
        # This parameter is required.
        self.third_part_id = third_part_id
        # This parameter is required.
        self.title = title
        # This parameter is required.
        self.type = type
        self.unit_type = unit_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.bank_name is not None:
            result['bank_name'] = self.bank_name

        if self.bank_no is not None:
            result['bank_no'] = self.bank_no

        if self.mail_third_part_id is not None:
            result['mail_third_part_id'] = self.mail_third_part_id

        if self.tax_no is not None:
            result['tax_no'] = self.tax_no

        if self.tel is not None:
            result['tel'] = self.tel

        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.unit_type is not None:
            result['unit_type'] = self.unit_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('bank_name') is not None:
            self.bank_name = m.get('bank_name')

        if m.get('bank_no') is not None:
            self.bank_no = m.get('bank_no')

        if m.get('mail_third_part_id') is not None:
            self.mail_third_part_id = m.get('mail_third_part_id')

        if m.get('tax_no') is not None:
            self.tax_no = m.get('tax_no')

        if m.get('tel') is not None:
            self.tel = m.get('tel')

        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('unit_type') is not None:
            self.unit_type = m.get('unit_type')

        return self

