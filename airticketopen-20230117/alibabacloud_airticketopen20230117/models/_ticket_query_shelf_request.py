# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TicketQueryShelfRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        scenic_id: int = None,
    ):
        # This parameter is required.
        self.account_no = account_no
        # This parameter is required.
        self.scenic_id = scenic_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.scenic_id is not None:
            result['ScenicId'] = self.scenic_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('ScenicId') is not None:
            self.scenic_id = m.get('ScenicId')

        return self

