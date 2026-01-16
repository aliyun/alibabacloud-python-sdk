# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutConcurrencyInput(DaraModel):
    def __init__(
        self,
        reserved_concurrency: int = None,
    ):
        # This parameter is required.
        self.reserved_concurrency = reserved_concurrency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')

        return self

