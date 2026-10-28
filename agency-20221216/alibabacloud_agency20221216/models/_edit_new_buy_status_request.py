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
        # The new purchase status. Valid values:
        # 
        # - cancelBan: allows new purchases
        # - ban: prohibits new purchases.
        self.new_buy_status = new_buy_status
        # The UID of the customer.
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

