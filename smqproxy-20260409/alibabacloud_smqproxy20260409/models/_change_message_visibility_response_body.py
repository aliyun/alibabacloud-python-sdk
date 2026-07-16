# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeMessageVisibilityResponseBody(DaraModel):
    def __init__(
        self,
        next_visible_time: int = None,
        receipt_handle: str = None,
    ):
        self.next_visible_time = next_visible_time
        self.receipt_handle = receipt_handle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_visible_time is not None:
            result['NextVisibleTime'] = self.next_visible_time

        if self.receipt_handle is not None:
            result['ReceiptHandle'] = self.receipt_handle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextVisibleTime') is not None:
            self.next_visible_time = m.get('NextVisibleTime')

        if m.get('ReceiptHandle') is not None:
            self.receipt_handle = m.get('ReceiptHandle')

        return self

