# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetActionPlanRequest(DaraModel):
    def __init__(
        self,
        action_plan_id: str = None,
    ):
        # The ID of the execution plan.
        self.action_plan_id = action_plan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_plan_id is not None:
            result['ActionPlanId'] = self.action_plan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPlanId') is not None:
            self.action_plan_id = m.get('ActionPlanId')

        return self

