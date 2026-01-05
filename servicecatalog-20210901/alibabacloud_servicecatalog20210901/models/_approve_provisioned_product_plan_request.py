# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApproveProvisionedProductPlanRequest(DaraModel):
    def __init__(
        self,
        approval_action: str = None,
        comment: str = None,
        plan_id: str = None,
    ):
        # The review action. Valid values:
        # 
        # *   Approve
        # *   Reject
        # 
        # This parameter is required.
        self.approval_action = approval_action
        # The review description.
        self.comment = comment
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
        if self.approval_action is not None:
            result['ApprovalAction'] = self.approval_action

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalAction') is not None:
            self.approval_action = m.get('ApprovalAction')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        return self

