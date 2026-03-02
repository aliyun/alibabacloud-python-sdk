# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class CreatePrivilegeCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        role_id: int = None,
        strategy_items: List[main_models.StrategyItem] = None,
        strategys: str = None,
    ):
        self.account_id = account_id
        self.role_id = role_id
        self.strategy_items = strategy_items
        self.strategys = strategys

    def validate(self):
        if self.strategy_items:
            for v1 in self.strategy_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.role_id is not None:
            result['roleId'] = self.role_id

        result['strategyItems'] = []
        if self.strategy_items is not None:
            for k1 in self.strategy_items:
                result['strategyItems'].append(k1.to_map() if k1 else None)

        if self.strategys is not None:
            result['strategys'] = self.strategys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')

        self.strategy_items = []
        if m.get('strategyItems') is not None:
            for k1 in m.get('strategyItems'):
                temp_model = main_models.StrategyItem()
                self.strategy_items.append(temp_model.from_map(k1))

        if m.get('strategys') is not None:
            self.strategys = m.get('strategys')

        return self

