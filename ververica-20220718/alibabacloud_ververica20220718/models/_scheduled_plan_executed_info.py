# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class ScheduledPlanExecutedInfo(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        creator_name: str = None,
        deployment_id: str = None,
        job_resource_upgrading_id: str = None,
        modified_at: str = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        namespace: str = None,
        origin: str = None,
        origin_job_id: str = None,
        status: main_models.ScheduledPlanExecutedStatus = None,
        workspace: str = None,
    ):
        self.created_at = created_at
        self.creator = creator
        self.creator_name = creator_name
        self.deployment_id = deployment_id
        self.job_resource_upgrading_id = job_resource_upgrading_id
        self.modified_at = modified_at
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.name = name
        self.namespace = namespace
        self.origin = origin
        self.origin_job_id = origin_job_id
        self.status = status
        self.workspace = workspace

    def validate(self):
        if self.status:
            self.status.validate()

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

        if self.job_resource_upgrading_id is not None:
            result['jobResourceUpgradingId'] = self.job_resource_upgrading_id

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

        if self.origin_job_id is not None:
            result['originJobId'] = self.origin_job_id

        if self.status is not None:
            result['status'] = self.status.to_map()

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

        if m.get('jobResourceUpgradingId') is not None:
            self.job_resource_upgrading_id = m.get('jobResourceUpgradingId')

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

        if m.get('originJobId') is not None:
            self.origin_job_id = m.get('originJobId')

        if m.get('status') is not None:
            temp_model = main_models.ScheduledPlanExecutedStatus()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

