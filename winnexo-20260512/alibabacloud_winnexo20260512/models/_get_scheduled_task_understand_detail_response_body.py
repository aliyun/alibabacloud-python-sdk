# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetScheduledTaskUnderstandDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        related_objects: List[main_models.GetScheduledTaskUnderstandDetailResponseBodyRelatedObjects] = None,
        related_semantics: List[main_models.GetScheduledTaskUnderstandDetailResponseBodyRelatedSemantics] = None,
        related_skills: List[main_models.GetScheduledTaskUnderstandDetailResponseBodyRelatedSkills] = None,
        request_id: str = None,
        task_understand: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 错误描述，成功时为空
        self.message = message
        self.related_objects = related_objects
        self.related_semantics = related_semantics
        self.related_skills = related_skills
        # 请求追踪 ID
        self.request_id = request_id
        # 润色后的任务理解
        self.task_understand = task_understand

    def validate(self):
        if self.related_objects:
            for v1 in self.related_objects:
                 if v1:
                    v1.validate()
        if self.related_semantics:
            for v1 in self.related_semantics:
                 if v1:
                    v1.validate()
        if self.related_skills:
            for v1 in self.related_skills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        result['relatedObjects'] = []
        if self.related_objects is not None:
            for k1 in self.related_objects:
                result['relatedObjects'].append(k1.to_map() if k1 else None)

        result['relatedSemantics'] = []
        if self.related_semantics is not None:
            for k1 in self.related_semantics:
                result['relatedSemantics'].append(k1.to_map() if k1 else None)

        result['relatedSkills'] = []
        if self.related_skills is not None:
            for k1 in self.related_skills:
                result['relatedSkills'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.task_understand is not None:
            result['taskUnderstand'] = self.task_understand

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        self.related_objects = []
        if m.get('relatedObjects') is not None:
            for k1 in m.get('relatedObjects'):
                temp_model = main_models.GetScheduledTaskUnderstandDetailResponseBodyRelatedObjects()
                self.related_objects.append(temp_model.from_map(k1))

        self.related_semantics = []
        if m.get('relatedSemantics') is not None:
            for k1 in m.get('relatedSemantics'):
                temp_model = main_models.GetScheduledTaskUnderstandDetailResponseBodyRelatedSemantics()
                self.related_semantics.append(temp_model.from_map(k1))

        self.related_skills = []
        if m.get('relatedSkills') is not None:
            for k1 in m.get('relatedSkills'):
                temp_model = main_models.GetScheduledTaskUnderstandDetailResponseBodyRelatedSkills()
                self.related_skills.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('taskUnderstand') is not None:
            self.task_understand = m.get('taskUnderstand')

        return self

class GetScheduledTaskUnderstandDetailResponseBodyRelatedSkills(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        name: str = None,
        skill_code: str = None,
        source_ids: List[str] = None,
    ):
        # 技能展示名称
        self.display_name = display_name
        # 文件名
        self.name = name
        # 技能代码
        self.skill_code = skill_code
        # sourceIds
        self.source_ids = source_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.name is not None:
            result['name'] = self.name

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.source_ids is not None:
            result['sourceIds'] = self.source_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('sourceIds') is not None:
            self.source_ids = m.get('sourceIds')

        return self

class GetScheduledTaskUnderstandDetailResponseBodyRelatedSemantics(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        entity: str = None,
    ):
        # 语义属性（JSON 字符串），用于语义检索时过滤
        self.attributes = attributes
        # 语义实体名，如客户/机会
        self.entity = entity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.entity is not None:
            result['entity'] = self.entity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('entity') is not None:
            self.entity = m.get('entity')

        return self

class GetScheduledTaskUnderstandDetailResponseBodyRelatedObjects(DaraModel):
    def __init__(
        self,
        mention_type: str = None,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
    ):
        # 提及类型
        self.mention_type = mention_type
        # 文件名
        self.name = name
        # 对象 ID
        self.object_id = object_id
        # 对象类型
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mention_type is not None:
            result['mentionType'] = self.mention_type

        if self.name is not None:
            result['name'] = self.name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mentionType') is not None:
            self.mention_type = m.get('mentionType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        return self

