# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScheduledPlanAppliedInfo(DaraModel):
    def __init__(
        self,
        deployment_id: str = None,
        expected_state: str = None,
        modified_at: str = None,
        modifier: str = None,
        modifier_name: str = None,
        namespace: str = None,
        scheduled_plan_id: str = None,
        scheduled_plan_name: str = None,
        status_state: str = None,
        workspace: str = None,
    ):
        self.deployment_id = deployment_id
        self.expected_state = expected_state
        self.modified_at = modified_at
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.namespace = namespace
        self.scheduled_plan_id = scheduled_plan_id
        self.scheduled_plan_name = scheduled_plan_name
        self.status_state = status_state
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.expected_state is not None:
            result['expectedState'] = self.expected_state

        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.scheduled_plan_id is not None:
            result['scheduledPlanId'] = self.scheduled_plan_id

        if self.scheduled_plan_name is not None:
            result['scheduledPlanName'] = self.scheduled_plan_name

        if self.status_state is not None:
            result['statusState'] = self.status_state

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('expectedState') is not None:
            self.expected_state = m.get('expectedState')

        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('scheduledPlanId') is not None:
            self.scheduled_plan_id = m.get('scheduledPlanId')

        if m.get('scheduledPlanName') is not None:
            self.scheduled_plan_name = m.get('scheduledPlanName')

        if m.get('statusState') is not None:
            self.status_state = m.get('statusState')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

