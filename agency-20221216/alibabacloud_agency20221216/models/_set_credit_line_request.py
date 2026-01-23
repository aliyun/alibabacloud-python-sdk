# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetCreditLineRequest(DaraModel):
    def __init__(
        self,
        credit_line: str = None,
        uid: int = None,
    ):
        # New Credit Line
        # 
        # This parameter is required.
        self.credit_line = credit_line
        # The UID of Sub Account.
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
        if self.credit_line is not None:
            result['CreditLine'] = self.credit_line

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditLine') is not None:
            self.credit_line = m.get('CreditLine')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

