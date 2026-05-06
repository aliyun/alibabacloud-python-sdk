# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRatePlanPriceRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        period: int = None,
        plan_name: str = None,
    ):
        self.amount = amount
        self.period = period
        self.plan_name = plan_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.period is not None:
            result['Period'] = self.period

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        return self

