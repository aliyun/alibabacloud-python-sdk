# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteProvisionedProductPlanRequest(DaraModel):
    def __init__(
        self,
        plan_id: str = None,
    ):
        # The ID of the plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        return self

