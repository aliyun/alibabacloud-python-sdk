# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterConfigureClientBalanceRequest(DaraModel):
    def __init__(
        self,
        balance_type: str = None,
        enable_balance: bool = None,
        initial_balance: float = None,
    ):
        self.balance_type = balance_type
        self.enable_balance = enable_balance
        self.initial_balance = initial_balance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.balance_type is not None:
            result['balanceType'] = self.balance_type

        if self.enable_balance is not None:
            result['enableBalance'] = self.enable_balance

        if self.initial_balance is not None:
            result['initialBalance'] = self.initial_balance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('balanceType') is not None:
            self.balance_type = m.get('balanceType')

        if m.get('enableBalance') is not None:
            self.enable_balance = m.get('enableBalance')

        if m.get('initialBalance') is not None:
            self.initial_balance = m.get('initialBalance')

        return self

