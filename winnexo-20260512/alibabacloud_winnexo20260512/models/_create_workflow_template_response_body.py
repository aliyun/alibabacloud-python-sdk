# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CreateWorkflowTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        created_by_user_id: int = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        steps: List[main_models.CreateWorkflowTemplateResponseBodySteps] = None,
        template_id: str = None,
    ):
        # 业务状态码；成功为200
        self.code = code
        # 创建人用户ID
        self.created_by_user_id = created_by_user_id
        # 模板描述
        self.description = description
        # 创建时间(ISO8601)
        self.gmt_create = gmt_create
        # 修改时间(ISO8601)
        self.gmt_modified = gmt_modified
        # 错误描述
        self.message = message
        # 模板名称
        self.name = name
        # 请求追踪ID
        self.request_id = request_id
        # 有序步骤
        self.steps = steps
        # 模板ID
        self.template_id = template_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('createdByUserId') is not None:
            self.created_by_user_id = m.get('createdByUserId')

        if m.get('description') is not None:
            self.description = m.get('description')

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
                temp_model = main_models.CreateWorkflowTemplateResponseBodySteps()
                self.steps.append(temp_model.from_map(k1))

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

class CreateWorkflowTemplateResponseBodySteps(DaraModel):
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
        step_id: str = None,
    ):
        # 模型档位
        self.model_mode = model_mode
        # 步骤名称
        self.name = name
        # 智能体负责人名称
        self.owner_agent_name = owner_agent_name
        # 负责人类型：MEMBER 人工 / AGENT 智能体
        self.owner_type = owner_type
        # 人工负责人用户ID
        self.owner_user_id = owner_user_id
        # 审核人用户ID列表
        self.reviewer_user_ids = reviewer_user_ids
        # 步骤顺序
        self.sort_order = sort_order
        # 步骤处理说明
        self.specification = specification
        # 步骤ID
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

        if m.get('stepId') is not None:
            self.step_id = m.get('stepId')

        return self

