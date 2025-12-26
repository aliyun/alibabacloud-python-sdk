# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SubQuotaPreemptionConfig(DaraModel):
    def __init__(
        self,
        preempted_priority_upper_bound: int = None,
        preempted_products: List[str] = None,
    ):
        self.preempted_priority_upper_bound = preempted_priority_upper_bound
        self.preempted_products = preempted_products

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.preempted_priority_upper_bound is not None:
            result['PreemptedPriorityUpperBound'] = self.preempted_priority_upper_bound

        if self.preempted_products is not None:
            result['PreemptedProducts'] = self.preempted_products

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreemptedPriorityUpperBound') is not None:
            self.preempted_priority_upper_bound = m.get('PreemptedPriorityUpperBound')

        if m.get('PreemptedProducts') is not None:
            self.preempted_products = m.get('PreemptedProducts')

        return self

