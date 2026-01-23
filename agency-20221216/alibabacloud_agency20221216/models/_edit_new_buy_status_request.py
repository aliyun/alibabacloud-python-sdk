# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditNewBuyStatusRequest(DaraModel):
    def __init__(
        self,
        new_buy_status: str = None,
        uid: int = None,
    ):
        # New Purchase Status</br>
        # 
        # - cancelBan: Cancel the restriction for New Purchase request</br>
        # 
        # - ban: ban the New Purchase request</br>
        self.new_buy_status = new_buy_status
        # Customer UID
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_buy_status is not None:
            result['NewBuyStatus'] = self.new_buy_status

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewBuyStatus') is not None:
            self.new_buy_status = m.get('NewBuyStatus')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

