# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetSkillResponseBody(DaraModel):
    def __init__(
        self,
        arguments: List[main_models.GetSkillResponseBodyArguments] = None,
        code: str = None,
        created_time: str = None,
        description: str = None,
        detail_logic: str = None,
        display_name: str = None,
        execute_mode: str = None,
        global_access: bool = None,
        has_draft_changes: bool = None,
        input_config: str = None,
        input_config_formatted: List[Dict[str, Any]] = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        skill_code: str = None,
        skill_files: List[Dict[str, Any]] = None,
        skill_hub_definition_id: int = None,
        skill_md_summary: str = None,
        source_type: str = None,
        status: str = None,
        tags: List[str] = None,
        updated_time: str = None,
        version_count: int = None,
        version_number: str = None,
    ):
        self.arguments = arguments
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 创建时间，ISO8601 格式
        self.created_time = created_time
        # 技能描述（已 i18n 解析）
        self.description = description
        # 技能详细逻辑
        self.detail_logic = detail_logic
        # 展示名称
        self.display_name = display_name
        # 执行模式
        self.execute_mode = execute_mode
        # 是否全局可访问
        self.global_access = global_access
        # 是否存在未发布的草稿修改
        self.has_draft_changes = has_draft_changes
        # 入参配置原文
        self.input_config = input_config
        self.input_config_formatted = input_config_formatted
        # 错误描述，成功时为空
        self.message = message
        # 文件名
        self.name = name
        # 请求追踪 ID
        self.request_id = request_id
        # 技能编码（全局唯一）
        self.skill_code = skill_code
        self.skill_files = skill_files
        # 技能定义 ID
        self.skill_hub_definition_id = skill_hub_definition_id
        # SKILL.md 简介（由 LLM 生成）
        self.skill_md_summary = skill_md_summary
        # 来源类型: BUILTIN / CUSTOM
        self.source_type = source_type
        # 技能状态: ACTIVE / DRAFT
        self.status = status
        # tags
        self.tags = tags
        # 修改时间，ISO8601 格式
        self.updated_time = updated_time
        # 版本总数
        self.version_count = version_count
        # 版本号
        self.version_number = version_number

    def validate(self):
        if self.arguments:
            for v1 in self.arguments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['arguments'] = []
        if self.arguments is not None:
            for k1 in self.arguments:
                result['arguments'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['code'] = self.code

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.description is not None:
            result['description'] = self.description

        if self.detail_logic is not None:
            result['detailLogic'] = self.detail_logic

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.execute_mode is not None:
            result['executeMode'] = self.execute_mode

        if self.global_access is not None:
            result['globalAccess'] = self.global_access

        if self.has_draft_changes is not None:
            result['hasDraftChanges'] = self.has_draft_changes

        if self.input_config is not None:
            result['inputConfig'] = self.input_config

        if self.input_config_formatted is not None:
            result['inputConfigFormatted'] = self.input_config_formatted

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.skill_files is not None:
            result['skillFiles'] = self.skill_files

        if self.skill_hub_definition_id is not None:
            result['skillHubDefinitionId'] = self.skill_hub_definition_id

        if self.skill_md_summary is not None:
            result['skillMdSummary'] = self.skill_md_summary

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.status is not None:
            result['status'] = self.status

        if self.tags is not None:
            result['tags'] = self.tags

        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time

        if self.version_count is not None:
            result['versionCount'] = self.version_count

        if self.version_number is not None:
            result['versionNumber'] = self.version_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.arguments = []
        if m.get('arguments') is not None:
            for k1 in m.get('arguments'):
                temp_model = main_models.GetSkillResponseBodyArguments()
                self.arguments.append(temp_model.from_map(k1))

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('detailLogic') is not None:
            self.detail_logic = m.get('detailLogic')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('executeMode') is not None:
            self.execute_mode = m.get('executeMode')

        if m.get('globalAccess') is not None:
            self.global_access = m.get('globalAccess')

        if m.get('hasDraftChanges') is not None:
            self.has_draft_changes = m.get('hasDraftChanges')

        if m.get('inputConfig') is not None:
            self.input_config = m.get('inputConfig')

        if m.get('inputConfigFormatted') is not None:
            self.input_config_formatted = m.get('inputConfigFormatted')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('skillFiles') is not None:
            self.skill_files = m.get('skillFiles')

        if m.get('skillHubDefinitionId') is not None:
            self.skill_hub_definition_id = m.get('skillHubDefinitionId')

        if m.get('skillMdSummary') is not None:
            self.skill_md_summary = m.get('skillMdSummary')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')

        if m.get('versionCount') is not None:
            self.version_count = m.get('versionCount')

        if m.get('versionNumber') is not None:
            self.version_number = m.get('versionNumber')

        return self

class GetSkillResponseBodyArguments(DaraModel):
    def __init__(
        self,
        default: str = None,
        description: str = None,
        enum: List[str] = None,
        name: str = None,
        required: bool = None,
        type: str = None,
    ):
        # 默认值
        self.default = default
        # 参数说明
        self.description = description
        # enum
        self.enum = enum
        # 文件名
        self.name = name
        # 是否必填
        self.required = required
        # 参数类型: string / number / boolean / array
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['default'] = self.default

        if self.description is not None:
            result['description'] = self.description

        if self.enum is not None:
            result['enum'] = self.enum

        if self.name is not None:
            result['name'] = self.name

        if self.required is not None:
            result['required'] = self.required

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('default') is not None:
            self.default = m.get('default')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enum') is not None:
            self.enum = m.get('enum')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

