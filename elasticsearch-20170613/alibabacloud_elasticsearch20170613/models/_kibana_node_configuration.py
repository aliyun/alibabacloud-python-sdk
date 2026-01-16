# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KibanaNodeConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.disk is not None:
            result['disk'] = self.disk

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

