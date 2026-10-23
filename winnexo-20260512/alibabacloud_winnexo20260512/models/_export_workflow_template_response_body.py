# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ExportWorkflowTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        template: main_models.ExportWorkflowTemplateResponseBodyTemplate = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The error description.
        self.message = message
        # The request tracking ID.
        self.request_id = request_id
        # The simplified template definition that can be re-imported.
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.template is not None:
            result['template'] = self.template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('template') is not None:
            temp_model = main_models.ExportWorkflowTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m.get('template'))

        return self

class ExportWorkflowTemplateResponseBodyTemplate(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        steps: List[main_models.ExportWorkflowTemplateResponseBodyTemplateSteps] = None,
    ):
        # The template description.
        self.description = description
        # The template name.
        self.name = name
        # The normalization steps.
        self.steps = steps

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
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        result['steps'] = []
        if self.steps is not None:
            for k1 in self.steps:
                result['steps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.steps = []
        if m.get('steps') is not None:
            for k1 in m.get('steps'):
                temp_model = main_models.ExportWorkflowTemplateResponseBodyTemplateSteps()
                self.steps.append(temp_model.from_map(k1))

        return self

class ExportWorkflowTemplateResponseBodyTemplateSteps(DaraModel):
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
        # The step name.
        self.name = name
        # The name of the responsible agent.
        self.owner_agent_name = owner_agent_name
        # The owner type. Valid values:
        # - MEMBER: Human.
        # - AGENT: Agent.
        self.owner_type = owner_type
        # The user ID of the human owner.
        self.owner_user_id = owner_user_id
        # The list of user IDs of the reviewers.
        self.reviewer_user_ids = reviewer_user_ids
        # The step order.
        self.sort_order = sort_order
        # The step processing instructions.
        self.specification = specification
        # The array of structured segments for the step instructions. Supported types include text, mention, skill, app, files, and web_search. All segment fields and nested attachments are preserved exactly as returned by the backend.
        self.specification_json = specification_json
        # The step ID.
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

