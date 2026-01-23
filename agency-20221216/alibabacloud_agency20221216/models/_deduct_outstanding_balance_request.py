# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeductOutstandingBalanceRequest(DaraModel):
    def __init__(
        self,
        deduct_amount: str = None,
        uid: int = None,
    ):
        # The Deducted Credit to be offset.
        # 
        # This parameter is required.
        self.deduct_amount = deduct_amount
        # Account UID of Distribution Customer.
        # 
        # This parameter is required.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deduct_amount is not None:
            result['DeductAmount'] = self.deduct_amount

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeductAmount') is not None:
            self.deduct_amount = m.get('DeductAmount')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

