# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteProvisionedProductPlanResponseBody(DaraModel):
    def __init__(
        self,
        plan_id: str = None,
        request_id: str = None,
    ):
        # The ID of the plan.
        self.plan_id = plan_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

