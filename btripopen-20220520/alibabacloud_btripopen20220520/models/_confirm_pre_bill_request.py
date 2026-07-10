# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfirmPreBillRequest(DaraModel):
    def __init__(
        self,
        bill_batch: str = None,
    ):
        # The bill batch date in the format of yyyy-MM-dd, such as 2026-06-21.
        # 
        # This parameter is required.
        self.bill_batch = bill_batch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_batch is not None:
            result['bill_batch'] = self.bill_batch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bill_batch') is not None:
            self.bill_batch = m.get('bill_batch')

        return self

