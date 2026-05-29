# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AutomaticWriteOffRequest(DaraModel):
    def __init__(
        self,
        automatic_write_off_amount: int = None,
        automatic_write_off_enabled: bool = None,
        customer_uid: int = None,
        language: str = None,
    ):
        self.automatic_write_off_amount = automatic_write_off_amount
        # This parameter is required.
        self.automatic_write_off_enabled = automatic_write_off_enabled
        # This parameter is required.
        self.customer_uid = customer_uid
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.automatic_write_off_amount is not None:
            result['AutomaticWriteOffAmount'] = self.automatic_write_off_amount

        if self.automatic_write_off_enabled is not None:
            result['AutomaticWriteOffEnabled'] = self.automatic_write_off_enabled

        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid

        if self.language is not None:
            result['Language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutomaticWriteOffAmount') is not None:
            self.automatic_write_off_amount = m.get('AutomaticWriteOffAmount')

        if m.get('AutomaticWriteOffEnabled') is not None:
            self.automatic_write_off_enabled = m.get('AutomaticWriteOffEnabled')

        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        return self

