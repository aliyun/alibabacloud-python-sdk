# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CreateTodoRequest(DaraModel):
    def __init__(
        self,
        assignee_user_ids: List[str] = None,
        collaboration_group_id: str = None,
        priority: str = None,
        questions: List[main_models.CreateTodoRequestQuestions] = None,
        source_context: Dict[str, Any] = None,
        source_type: str = None,
        tenant_id: str = None,
        title: str = None,
    ):
        # 处理人平台用户ID列表（1~100，去重后生效）
        # 
        # This parameter is required.
        self.assignee_user_ids = assignee_user_ids
        # 协作空间 ID（可选）
        self.collaboration_group_id = collaboration_group_id
        # 优先级
        self.priority = priority
        # 问题清单（1~N）
        # 
        # This parameter is required.
        self.questions = questions
        # 来源上下文（原样透传落库，不校验）
        # 
        # This parameter is required.
        self.source_context = source_context
        # 待办来源（仅 OPEN_API）
        # 
        # This parameter is required.
        self.source_type = source_type
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 待办标题（≤200 字）
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        if self.questions:
            for v1 in self.questions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assignee_user_ids is not None:
            result['assigneeUserIds'] = self.assignee_user_ids

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.priority is not None:
            result['priority'] = self.priority

        result['questions'] = []
        if self.questions is not None:
            for k1 in self.questions:
                result['questions'].append(k1.to_map() if k1 else None)

        if self.source_context is not None:
            result['sourceContext'] = self.source_context

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assigneeUserIds') is not None:
            self.assignee_user_ids = m.get('assigneeUserIds')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        self.questions = []
        if m.get('questions') is not None:
            for k1 in m.get('questions'):
                temp_model = main_models.CreateTodoRequestQuestions()
                self.questions.append(temp_model.from_map(k1))

        if m.get('sourceContext') is not None:
            self.source_context = m.get('sourceContext')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class CreateTodoRequestQuestions(DaraModel):
    def __init__(
        self,
        allow_custom: bool = None,
        custom_label: str = None,
        custom_max_length: int = None,
        custom_placeholder: str = None,
        max_length: int = None,
        mode: str = None,
        options: List[main_models.CreateTodoRequestQuestionsOptions] = None,
        placeholder: str = None,
        question: str = None,
        required: bool = None,
    ):
        # 是否允许自定义输入
        self.allow_custom = allow_custom
        # 自定义输入项文案
        self.custom_label = custom_label
        # 自定义输入长度上限
        self.custom_max_length = custom_max_length
        # 自定义输入占位符
        self.custom_placeholder = custom_placeholder
        # TEXT 题长度上限
        self.max_length = max_length
        # 作答形态：SINGLE_CHOICE/MULTI_CHOICE/TEXT
        # 
        # This parameter is required.
        self.mode = mode
        # 问题的选项列表；选择题必填，每项含选项文案（label）、补充说明（description）与是否推荐（recommended）
        self.options = options
        # TEXT 题占位符
        self.placeholder = placeholder
        # 问题正文（引用键，清单内唯一）
        # 
        # This parameter is required.
        self.question = question
        # 是否必答
        self.required = required

    def validate(self):
        if self.options:
            for v1 in self.options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_custom is not None:
            result['allowCustom'] = self.allow_custom

        if self.custom_label is not None:
            result['customLabel'] = self.custom_label

        if self.custom_max_length is not None:
            result['customMaxLength'] = self.custom_max_length

        if self.custom_placeholder is not None:
            result['customPlaceholder'] = self.custom_placeholder

        if self.max_length is not None:
            result['maxLength'] = self.max_length

        if self.mode is not None:
            result['mode'] = self.mode

        result['options'] = []
        if self.options is not None:
            for k1 in self.options:
                result['options'].append(k1.to_map() if k1 else None)

        if self.placeholder is not None:
            result['placeholder'] = self.placeholder

        if self.question is not None:
            result['question'] = self.question

        if self.required is not None:
            result['required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowCustom') is not None:
            self.allow_custom = m.get('allowCustom')

        if m.get('customLabel') is not None:
            self.custom_label = m.get('customLabel')

        if m.get('customMaxLength') is not None:
            self.custom_max_length = m.get('customMaxLength')

        if m.get('customPlaceholder') is not None:
            self.custom_placeholder = m.get('customPlaceholder')

        if m.get('maxLength') is not None:
            self.max_length = m.get('maxLength')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        self.options = []
        if m.get('options') is not None:
            for k1 in m.get('options'):
                temp_model = main_models.CreateTodoRequestQuestionsOptions()
                self.options.append(temp_model.from_map(k1))

        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')

        if m.get('question') is not None:
            self.question = m.get('question')

        if m.get('required') is not None:
            self.required = m.get('required')

        return self

class CreateTodoRequestQuestionsOptions(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        recommended: bool = None,
    ):
        # 选项补充说明
        self.description = description
        # 选项文案（引用键）
        # 
        # This parameter is required.
        self.label = label
        # 是否推荐
        self.recommended = recommended

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.label is not None:
            result['label'] = self.label

        if self.recommended is not None:
            result['recommended'] = self.recommended

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('recommended') is not None:
            self.recommended = m.get('recommended')

        return self

