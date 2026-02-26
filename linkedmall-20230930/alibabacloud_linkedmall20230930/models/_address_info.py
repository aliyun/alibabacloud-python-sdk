# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddressInfo(DaraModel):
    def __init__(
        self,
        address_detail: str = None,
        address_id: int = None,
        division_code: str = None,
        receiver: str = None,
        receiver_phone: str = None,
        town_division_code: str = None,
    ):
        # This parameter is required.
        self.address_detail = address_detail
        self.address_id = address_id
        self.division_code = division_code
        # This parameter is required.
        self.receiver = receiver
        # This parameter is required.
        self.receiver_phone = receiver_phone
        self.town_division_code = town_division_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_detail is not None:
            result['addressDetail'] = self.address_detail

        if self.address_id is not None:
            result['addressId'] = self.address_id

        if self.division_code is not None:
            result['divisionCode'] = self.division_code

        if self.receiver is not None:
            result['receiver'] = self.receiver

        if self.receiver_phone is not None:
            result['receiverPhone'] = self.receiver_phone

        if self.town_division_code is not None:
            result['townDivisionCode'] = self.town_division_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addressDetail') is not None:
            self.address_detail = m.get('addressDetail')

        if m.get('addressId') is not None:
            self.address_id = m.get('addressId')

        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')

        if m.get('receiver') is not None:
            self.receiver = m.get('receiver')

        if m.get('receiverPhone') is not None:
            self.receiver_phone = m.get('receiverPhone')

        if m.get('townDivisionCode') is not None:
            self.town_division_code = m.get('townDivisionCode')

        return self

