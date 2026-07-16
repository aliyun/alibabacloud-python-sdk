# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchDeleteMessageRequest(DaraModel):
    def __init__(
        self,
        receipt_handles: List[str] = None,
    ):
        self.receipt_handles = receipt_handles

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.receipt_handles is not None:
            result['ReceiptHandles'] = self.receipt_handles

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiptHandles') is not None:
            self.receipt_handles = m.get('ReceiptHandles')

        return self

