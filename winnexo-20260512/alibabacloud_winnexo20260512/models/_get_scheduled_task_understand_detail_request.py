# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetScheduledTaskUnderstandDetailRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        digital_employee_name: List[str] = None,
        segments: List[main_models.GetScheduledTaskUnderstandDetailRequestSegments] = None,
        tenant_id: str = None,
        user_input: str = None,
    ):
        # 所属协作群组 ID（如 cg_101）；群任务理解时传入（调用者需为有效群成员），候选技能额外并入群绑定技能
        self.collaboration_group_id = collaboration_group_id
        # 数字员工名称列表，用于过滤可用技能；必传（传空列表表示仅用租户 global 技能）
        # 
        # This parameter is required.
        self.digital_employee_name = digital_employee_name
        self.segments = segments
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 自然语言任务描述
        # 
        # This parameter is required.
        self.user_input = user_input

    def validate(self):
        if self.segments:
            for v1 in self.segments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        result['segments'] = []
        if self.segments is not None:
            for k1 in self.segments:
                result['segments'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_input is not None:
            result['userInput'] = self.user_input

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        self.segments = []
        if m.get('segments') is not None:
            for k1 in m.get('segments'):
                temp_model = main_models.GetScheduledTaskUnderstandDetailRequestSegments()
                self.segments.append(temp_model.from_map(k1))

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userInput') is not None:
            self.user_input = m.get('userInput')

        return self

class GetScheduledTaskUnderstandDetailRequestSegments(DaraModel):
    def __init__(
        self,
        content: str = None,
        enabled: str = None,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
        skill_code: str = None,
        type: str = None,
    ):
        # 文本内容，type=text 时必填
        self.content = content
        # 功能开关，type=web_search 时可选
        self.enabled = enabled
        # 文件名
        self.name = name
        # 对象 ID，type=mention 时有值
        self.object_id = object_id
        # 对象类型如 customer，type=mention 时有值
        self.object_type = object_type
        # 技能编码，type=skill 时有值
        self.skill_code = skill_code
        # 元素类型：text|web_search|mention|skill
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.name is not None:
            result['name'] = self.name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

