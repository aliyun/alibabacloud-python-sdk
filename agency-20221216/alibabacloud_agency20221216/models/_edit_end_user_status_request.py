# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditEndUserStatusRequest(DaraModel):
    def __init__(
        self,
        credit_status: str = None,
        uid: int = None,
    ):
        # ### Shutdown status
        # 
        # - postPayFreeze: pay-as-you-go resource suspension
        # - postPayThaw: pay-as-you-go resource resumption.
        self.credit_status = credit_status
        # The UID of the customer to be processed.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit_status is not None:
            result['CreditStatus'] = self.credit_status

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditStatus') is not None:
            self.credit_status = m.get('CreditStatus')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

