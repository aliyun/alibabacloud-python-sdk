# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeMessageVisibilityRequest(DaraModel):
    def __init__(
        self,
        receipt_handle: str = None,
        visibility_timeout: int = None,
    ):
        self.receipt_handle = receipt_handle
        self.visibility_timeout = visibility_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.receipt_handle is not None:
            result['receiptHandle'] = self.receipt_handle

        if self.visibility_timeout is not None:
            result['visibilityTimeout'] = self.visibility_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('receiptHandle') is not None:
            self.receipt_handle = m.get('receiptHandle')

        if m.get('visibilityTimeout') is not None:
            self.visibility_timeout = m.get('visibilityTimeout')

        return self

