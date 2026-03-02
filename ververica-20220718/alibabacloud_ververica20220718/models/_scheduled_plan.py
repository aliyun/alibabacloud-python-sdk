# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class ScheduledPlan(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        creator_name: str = None,
        deployment_id: str = None,
        modified_at: str = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        namespace: str = None,
        origin: str = None,
        periodic_scheduling_policies: List[main_models.PeriodicSchedulingPolicy] = None,
        scheduled_plan_id: str = None,
        status: str = None,
        updated_by_user: bool = None,
        workspace: str = None,
    ):
        self.created_at = created_at
        self.creator = creator
        self.creator_name = creator_name
        self.deployment_id = deployment_id
        self.modified_at = modified_at
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.name = name
        self.namespace = namespace
        self.origin = origin
        self.periodic_scheduling_policies = periodic_scheduling_policies
        self.scheduled_plan_id = scheduled_plan_id
        self.status = status
        self.updated_by_user = updated_by_user
        self.workspace = workspace

    def validate(self):
        if self.periodic_scheduling_policies:
            for v1 in self.periodic_scheduling_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.origin is not None:
            result['origin'] = self.origin

        result['periodicSchedulingPolicies'] = []
        if self.periodic_scheduling_policies is not None:
            for k1 in self.periodic_scheduling_policies:
                result['periodicSchedulingPolicies'].append(k1.to_map() if k1 else None)

        if self.scheduled_plan_id is not None:
            result['scheduledPlanId'] = self.scheduled_plan_id

        if self.status is not None:
            result['status'] = self.status

        if self.updated_by_user is not None:
            result['updatedByUser'] = self.updated_by_user

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('origin') is not None:
            self.origin = m.get('origin')

        self.periodic_scheduling_policies = []
        if m.get('periodicSchedulingPolicies') is not None:
            for k1 in m.get('periodicSchedulingPolicies'):
                temp_model = main_models.PeriodicSchedulingPolicy()
                self.periodic_scheduling_policies.append(temp_model.from_map(k1))

        if m.get('scheduledPlanId') is not None:
            self.scheduled_plan_id = m.get('scheduledPlanId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedByUser') is not None:
            self.updated_by_user = m.get('updatedByUser')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

