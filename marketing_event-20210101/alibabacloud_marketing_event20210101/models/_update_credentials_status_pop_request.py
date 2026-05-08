# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCredentialsStatusPopRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        proxy_recipient_name: str = None,
        proxy_recipient_phone_number: str = None,
        receipt_location: str = None,
        time: str = None,
    ):
        self.code = code
        self.proxy_recipient_name = proxy_recipient_name
        self.proxy_recipient_phone_number = proxy_recipient_phone_number
        self.receipt_location = receipt_location
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.proxy_recipient_name is not None:
            result['ProxyRecipientName'] = self.proxy_recipient_name

        if self.proxy_recipient_phone_number is not None:
            result['ProxyRecipientPhoneNumber'] = self.proxy_recipient_phone_number

        if self.receipt_location is not None:
            result['ReceiptLocation'] = self.receipt_location

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ProxyRecipientName') is not None:
            self.proxy_recipient_name = m.get('ProxyRecipientName')

        if m.get('ProxyRecipientPhoneNumber') is not None:
            self.proxy_recipient_phone_number = m.get('ProxyRecipientPhoneNumber')

        if m.get('ReceiptLocation') is not None:
            self.receipt_location = m.get('ReceiptLocation')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

