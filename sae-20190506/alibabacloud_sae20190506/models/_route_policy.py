# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class RoutePolicy(DaraModel):
    def __init__(
        self,
        condition: str = None,
        policy_items: List[main_models.PolicyItem] = None,
    ):
        self.condition = condition
        self.policy_items = policy_items

    def validate(self):
        if self.policy_items:
            for v1 in self.policy_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['condition'] = self.condition

        result['policyItems'] = []
        if self.policy_items is not None:
            for k1 in self.policy_items:
                result['policyItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        self.policy_items = []
        if m.get('policyItems') is not None:
            for k1 in m.get('policyItems'):
                temp_model = main_models.PolicyItem()
                self.policy_items.append(temp_model.from_map(k1))

        return self

