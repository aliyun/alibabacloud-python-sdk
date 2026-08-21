# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TicketQueryProductRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        product_id: str = None,
    ):
        # This parameter is required.
        self.account_no = account_no
        # This parameter is required.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        return self

