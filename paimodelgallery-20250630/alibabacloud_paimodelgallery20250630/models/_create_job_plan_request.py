# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_paimodelgallery20250630 import models as main_models
from darabonba.model import DaraModel

class CreateJobPlanRequest(DaraModel):
    def __init__(
        self,
        job_plan_name: str = None,
        job_plan_steps: List[main_models.CreateJobPlanRequestJobPlanSteps] = None,
        job_plan_type: str = None,
        tag: List[main_models.CreateJobPlanRequestTag] = None,
        template_id: str = None,
        workspace_id: str = None,
    ):
        # The name of the job plan.
        self.job_plan_name = job_plan_name
        # The steps of the job plan.
        self.job_plan_steps = job_plan_steps
        # The type of the job plan.
        self.job_plan_type = job_plan_type
        # Note: According to the Alibaba Cloud tag system specification, this parameter name is in singular form.
        self.tag = tag
        # The ID of the scenario-specific distillation template, obtained from ListDistillationTemplates. If this parameter is not specified, a general-purpose job plan is created.
        self.template_id = template_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.job_plan_steps:
            for v1 in self.job_plan_steps:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_plan_name is not None:
            result['JobPlanName'] = self.job_plan_name

        result['JobPlanSteps'] = []
        if self.job_plan_steps is not None:
            for k1 in self.job_plan_steps:
                result['JobPlanSteps'].append(k1.to_map() if k1 else None)

        if self.job_plan_type is not None:
            result['JobPlanType'] = self.job_plan_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobPlanName') is not None:
            self.job_plan_name = m.get('JobPlanName')

        self.job_plan_steps = []
        if m.get('JobPlanSteps') is not None:
            for k1 in m.get('JobPlanSteps'):
                temp_model = main_models.CreateJobPlanRequestJobPlanSteps()
                self.job_plan_steps.append(temp_model.from_map(k1))

        if m.get('JobPlanType') is not None:
            self.job_plan_type = m.get('JobPlanType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateJobPlanRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateJobPlanRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # **Key**
        self.key = key
        # **Value**
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateJobPlanRequestJobPlanSteps(DaraModel):
    def __init__(
        self,
        job_plan_step_name: str = None,
        job_plan_step_spec: Dict[str, Any] = None,
        job_plan_step_type: str = None,
    ):
        # The name of the job plan step.
        self.job_plan_step_name = job_plan_step_name
        # The detailed configuration of the job plan step.
        self.job_plan_step_spec = job_plan_step_spec
        # The type of the job plan step.
        self.job_plan_step_type = job_plan_step_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_plan_step_name is not None:
            result['JobPlanStepName'] = self.job_plan_step_name

        if self.job_plan_step_spec is not None:
            result['JobPlanStepSpec'] = self.job_plan_step_spec

        if self.job_plan_step_type is not None:
            result['JobPlanStepType'] = self.job_plan_step_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobPlanStepName') is not None:
            self.job_plan_step_name = m.get('JobPlanStepName')

        if m.get('JobPlanStepSpec') is not None:
            self.job_plan_step_spec = m.get('JobPlanStepSpec')

        if m.get('JobPlanStepType') is not None:
            self.job_plan_step_type = m.get('JobPlanStepType')

        return self

