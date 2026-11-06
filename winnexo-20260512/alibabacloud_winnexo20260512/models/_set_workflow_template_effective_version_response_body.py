# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class SetWorkflowTemplateEffectiveVersionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        created_by_user_id: int = None,
        description: str = None,
        edges: List[Dict[str, Any]] = None,
        effective_version: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        layout: Dict[str, Any] = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        schema_version: int = None,
        steps: List[main_models.SetWorkflowTemplateEffectiveVersionResponseBodySteps] = None,
        template_id: str = None,
        version: str = None,
        version_description: str = None,
        version_status: str = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The user ID of the creator.
        self.created_by_user_id = created_by_user_id
        # The template description.
        self.description = description
        # 节点依赖边；每项包含from/to，引用稳定stepId
        self.edges = edges
        # The current effective version number of the template. An empty value indicates that only a draft exists and it cannot be used for work items.
        self.effective_version = effective_version
        # The creation time in ISO 8601 format.
        self.gmt_create = gmt_create
        # The modification time in ISO 8601 format.
        self.gmt_modified = gmt_modified
        # 可选画布布局，按stepId索引；只影响展示，不决定依赖
        self.layout = layout
        # The error description.
        self.message = message
        # The step name. This field can be empty for drafts but is required upon submission.
        self.name = name
        # The request tracking ID.
        self.request_id = request_id
        # 模板结构版本，当前为2，与业务版本vN独立
        self.schema_version = schema_version
        # The ordered steps.
        self.steps = steps
        # The template ID.
        self.template_id = template_id
        # The version number of the returned content.
        self.version = version
        # The change description for this version. An empty value indicates that no description is provided.
        self.version_description = version_description
        # The version status. Valid values:
        # - DRAFT: Draft.
        # - SUBMITTED: Submitted.
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

        if self.edges is not None:
            result['edges'] = self.edges

        if self.effective_version is not None:
            result['effectiveVersion'] = self.effective_version

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.layout is not None:
            result['layout'] = self.layout

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

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

        if m.get('edges') is not None:
            self.edges = m.get('edges')

        if m.get('effectiveVersion') is not None:
            self.effective_version = m.get('effectiveVersion')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('layout') is not None:
            self.layout = m.get('layout')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        self.steps = []
        if m.get('steps') is not None:
            for k1 in m.get('steps'):
                temp_model = main_models.SetWorkflowTemplateEffectiveVersionResponseBodySteps()
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

class SetWorkflowTemplateEffectiveVersionResponseBodySteps(DaraModel):
    def __init__(
        self,
        model_mode: str = None,
        name: str = None,
        owner_agent_name: str = None,
        owner_type: str = None,
        owner_user_id: int = None,
        review_output: bool = None,
        reviewer_user_ids: List[int] = None,
        sort_order: int = None,
        specification: str = None,
        specification_json: List[Dict[str, Any]] = None,
        step_id: str = None,
    ):
        # The model tier.
        self.model_mode = model_mode
        # The step name. This field can be empty for drafts but is required upon submission.
        self.name = name
        # The name of the agent owner.
        self.owner_agent_name = owner_agent_name
        # The owner type. Valid values:
        # - MEMBER: Human.
        # - AGENT: Agent.
        self.owner_type = owner_type
        # The user ID of the human owner.
        self.owner_user_id = owner_user_id
        # 是否人工审核产出物，默认关闭；仅数字员工可开启，审核待办自动发负责人
        self.review_output = review_output
        # The list of user IDs of the reviewers.
        self.reviewer_user_ids = reviewer_user_ids
        # The step order.
        self.sort_order = sort_order
        # The display text derived from ordered segments. Fixed titles are not added, and the text is not stored independently.
        self.specification = specification
        # The array of ordered segments. Supports text, mention, skill, app, files, and web_search. Retains reference identities and order.
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

        if self.review_output is not None:
            result['reviewOutput'] = self.review_output

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

        if m.get('reviewOutput') is not None:
            self.review_output = m.get('reviewOutput')

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

