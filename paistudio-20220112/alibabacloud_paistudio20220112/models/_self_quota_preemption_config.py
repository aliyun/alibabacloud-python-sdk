# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SelfQuotaPreemptionConfig(DaraModel):
    def __init__(
        self,
        preempted_priorities: List[int] = None,
        preempted_products: List[str] = None,
        preemptor_priorities: List[int] = None,
    ):
        self.preempted_priorities = preempted_priorities
        self.preempted_products = preempted_products
        self.preemptor_priorities = preemptor_priorities

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.preempted_priorities is not None:
            result['PreemptedPriorities'] = self.preempted_priorities

        if self.preempted_products is not None:
            result['PreemptedProducts'] = self.preempted_products

        if self.preemptor_priorities is not None:
            result['PreemptorPriorities'] = self.preemptor_priorities

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreemptedPriorities') is not None:
            self.preempted_priorities = m.get('PreemptedPriorities')

        if m.get('PreemptedProducts') is not None:
            self.preempted_products = m.get('PreemptedProducts')

        if m.get('PreemptorPriorities') is not None:
            self.preemptor_priorities = m.get('PreemptorPriorities')

        return self

