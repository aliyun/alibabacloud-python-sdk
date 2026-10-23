# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CreateWorkflowTemplateDraftVersionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        created_by_user_id: int = None,
        description: str = None,
        effective_version: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        steps: List[main_models.CreateWorkflowTemplateDraftVersionResponseBodySteps] = None,
        template_id: str = None,
        version: str = None,
        version_description: str = None,
        version_status: str = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The user ID of the creator.
        self.created_by_user_id = created_by_user_id
        # The description of the template.
        self.description = description
        # The current effective version number of the template. An empty value indicates that only a draft exists and the template cannot be used for work items.
        self.effective_version = effective_version
        # The creation time in ISO 8601 format.
        self.gmt_create = gmt_create
        # The modification time in ISO 8601 format.
        self.gmt_modified = gmt_modified
        # The error description.
        self.message = message
        # The name of the template.
        self.name = name
        # The request tracking ID.
        self.request_id = request_id
        # The ordered steps.
        self.steps = steps
        # The ID of the template.
        self.template_id = template_id
        # The version number to which the returned content belongs.
        self.version = version
        # The change description for this version. An empty value indicates that no description is provided.
        self.version_description = version_description
        # The version status. Valid values: DRAFT (draft) and SUBMITTED (submitted).
        self.version_status = version_status

    def validate(self):
        if self.steps:
            for v1 in self.steps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.created_by_user_id is not None:
            result['createdByUserId'] = self.created_by_user_id

        if self.description is not None:
            result['description'] = self.description

        if self.effective_version is not None:
            result['effectiveVersion'] = self.effective_version

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['steps'] = []
        if self.steps is not None:
            for k1 in self.steps:
                result['steps'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.version is not None:
            result['version'] = self.version

        if self.version_description is not None:
            result['versionDescription'] = self.version_description

        if self.version_status is not None:
            result['versionStatus'] = self.version_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('createdByUserId') is not None:
            self.created_by_user_id = m.get('createdByUserId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('effectiveVersion') is not None:
            self.effective_version = m.get('effectiveVersion')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.steps = []
        if m.get('steps') is not None:
            for k1 in m.get('steps'):
                temp_model = main_models.CreateWorkflowTemplateDraftVersionResponseBodySteps()
                self.steps.append(temp_model.from_map(k1))

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')

        if m.get('versionStatus') is not None:
            self.version_status = m.get('versionStatus')

        return self

class CreateWorkflowTemplateDraftVersionResponseBodySteps(DaraModel):
    def __init__(
        self,
        model_mode: str = None,
        name: str = None,
        owner_agent_name: str = None,
        owner_type: str = None,
        owner_user_id: int = None,
        reviewer_user_ids: List[int] = None,
        sort_order: int = None,
        specification: str = None,
        specification_json: List[Dict[str, Any]] = None,
        step_id: str = None,
    ):
        # The model tier.
        self.model_mode = model_mode
        # The name of the step.
        self.name = name
        # The name of the digital employee executor. This parameter is required when ownerType is set to AGENT.
        self.owner_agent_name = owner_agent_name
        # The type of the executor. Valid values: MEMBER (workspace member) and AGENT (digital employee).
        self.owner_type = owner_type
        # The user ID of the member executor. This parameter is required when ownerType is set to MEMBER.
        self.owner_user_id = owner_user_id
        # The list of user IDs for the owners (formerly reviewers). This parameter is valid only for steps with a digital employee executor and is always empty for steps with a member executor.
        self.reviewer_user_ids = reviewer_user_ids
        # The sort order of the step.
        self.sort_order = sort_order
        # The array of ordered step description segments. Supported types include text, mention, skill, app, files, and web_search. When plain text is entered, a single text segment is returned. The fields and nested attachments of each segment are retained as-is from the backend.
        self.specification = specification
        # The array of structured step description segments. Supported types include text, mention, skill, app, files, and web_search. The fields and nested attachments of each segment are retained as-is from the backend.
        self.specification_json = specification_json
        # The ID of the step.
        self.step_id = step_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_mode is not None:
            result['modelMode'] = self.model_mode

        if self.name is not None:
            result['name'] = self.name

        if self.owner_agent_name is not None:
            result['ownerAgentName'] = self.owner_agent_name

        if self.owner_type is not None:
            result['ownerType'] = self.owner_type

        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id

        if self.reviewer_user_ids is not None:
            result['reviewerUserIds'] = self.reviewer_user_ids

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

        if self.specification is not None:
            result['specification'] = self.specification

        if self.specification_json is not None:
            result['specificationJson'] = self.specification_json

        if self.step_id is not None:
            result['stepId'] = self.step_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelMode') is not None:
            self.model_mode = m.get('modelMode')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ownerAgentName') is not None:
            self.owner_agent_name = m.get('ownerAgentName')

        if m.get('ownerType') is not None:
            self.owner_type = m.get('ownerType')

        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')

        if m.get('reviewerUserIds') is not None:
            self.reviewer_user_ids = m.get('reviewerUserIds')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        if m.get('specification') is not None:
            self.specification = m.get('specification')

        if m.get('specificationJson') is not None:
            self.specification_json = m.get('specificationJson')

        if m.get('stepId') is not None:
            self.step_id = m.get('stepId')

        return self

