# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_paimodelgallery20250630 import models as main_models
from darabonba.model import DaraModel

class GetJobPlanResponseBody(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        job_plan_current_step: str = None,
        job_plan_id: str = None,
        job_plan_name: str = None,
        job_plan_steps: List[main_models.GetJobPlanResponseBodyJobPlanSteps] = None,
        job_plan_type: str = None,
        owner_id: str = None,
        request_id: str = None,
        tags: List[main_models.GetJobPlanResponseBodyTags] = None,
        template_id: str = None,
        template_name: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The creation time of the job plan.
        self.gmt_create_time = gmt_create_time
        # The last modified time of the job plan.
        self.gmt_modified_time = gmt_modified_time
        # The current step.
        self.job_plan_current_step = job_plan_current_step
        # The job plan ID.
        self.job_plan_id = job_plan_id
        # The job plan name, which is unique within the workspace.
        self.job_plan_name = job_plan_name
        # The job plan steps.
        self.job_plan_steps = job_plan_steps
        # The job plan type.
        self.job_plan_type = job_plan_type
        # The Alibaba Cloud account ID that owns the job plan.
        self.owner_id = owner_id
        # The request ID.
        self.request_id = request_id
        # The list of tags.
        self.tags = tags
        # The distillation template ID used to create the job plan. An empty value indicates that this is not a scenario-based distillation task.
        self.template_id = template_id
        # The display name of the distillation template, localized based on the requested language.
        self.template_name = template_name
        # The Alibaba Cloud account ID that created the job plan.
        self.user_id = user_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.job_plan_steps:
            for v1 in self.job_plan_steps:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.job_plan_current_step is not None:
            result['JobPlanCurrentStep'] = self.job_plan_current_step

        if self.job_plan_id is not None:
            result['JobPlanId'] = self.job_plan_id

        if self.job_plan_name is not None:
            result['JobPlanName'] = self.job_plan_name

        result['JobPlanSteps'] = []
        if self.job_plan_steps is not None:
            for k1 in self.job_plan_steps:
                result['JobPlanSteps'].append(k1.to_map() if k1 else None)

        if self.job_plan_type is not None:
            result['JobPlanType'] = self.job_plan_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('JobPlanCurrentStep') is not None:
            self.job_plan_current_step = m.get('JobPlanCurrentStep')

        if m.get('JobPlanId') is not None:
            self.job_plan_id = m.get('JobPlanId')

        if m.get('JobPlanName') is not None:
            self.job_plan_name = m.get('JobPlanName')

        self.job_plan_steps = []
        if m.get('JobPlanSteps') is not None:
            for k1 in m.get('JobPlanSteps'):
                temp_model = main_models.GetJobPlanResponseBodyJobPlanSteps()
                self.job_plan_steps.append(temp_model.from_map(k1))

        if m.get('JobPlanType') is not None:
            self.job_plan_type = m.get('JobPlanType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetJobPlanResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetJobPlanResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class GetJobPlanResponseBodyJobPlanSteps(DaraModel):
    def __init__(
        self,
        job_plan_step_id: str = None,
        job_plan_step_name: str = None,
        job_plan_step_spec: Dict[str, Any] = None,
        job_plan_step_type: str = None,
    ):
        # The generated PAIFlow PipelineRunId.
        self.job_plan_step_id = job_plan_step_id
        # The job plan step name.
        self.job_plan_step_name = job_plan_step_name
        # The job plan step configuration.
        self.job_plan_step_spec = job_plan_step_spec
        # The job plan step type.
        self.job_plan_step_type = job_plan_step_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_plan_step_id is not None:
            result['JobPlanStepId'] = self.job_plan_step_id

        if self.job_plan_step_name is not None:
            result['JobPlanStepName'] = self.job_plan_step_name

        if self.job_plan_step_spec is not None:
            result['JobPlanStepSpec'] = self.job_plan_step_spec

        if self.job_plan_step_type is not None:
            result['JobPlanStepType'] = self.job_plan_step_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobPlanStepId') is not None:
            self.job_plan_step_id = m.get('JobPlanStepId')

        if m.get('JobPlanStepName') is not None:
            self.job_plan_step_name = m.get('JobPlanStepName')

        if m.get('JobPlanStepSpec') is not None:
            self.job_plan_step_spec = m.get('JobPlanStepSpec')

        if m.get('JobPlanStepType') is not None:
            self.job_plan_step_type = m.get('JobPlanStepType')

        return self

