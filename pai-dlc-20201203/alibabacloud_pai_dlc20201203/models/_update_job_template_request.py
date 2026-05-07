# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateJobTemplateRequest(DaraModel):
    def __init__(
        self,
        constraints: Dict[str, Any] = None,
        content: str = None,
        description: str = None,
        metadata: Dict[str, Any] = None,
        set_as_default: bool = None,
        template_name: str = None,
        version: int = None,
    ):
        # 字段约束规则。Key 为 JSONPath 表达式，Value 为约束类型：locked（锁定不可覆盖）、overridable（可覆盖）、required（必填）。需与 Content 同时提供，不允许单独更新。
        self.constraints = constraints
        # 任务模板的配置内容，支持 CreateJob 接口的所有参数字段，以 JSON 格式传入。提供时会创建新版本。
        self.content = content
        self.description = description
        # 用户自定义的键值对元数据，用于存储模板的附加信息。
        self.metadata = metadata
        # 当创建了新版本时，是否将新版本设为默认版本。
        self.set_as_default = set_as_default
        self.template_name = template_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.constraints is not None:
            result['Constraints'] = self.constraints

        if self.content is not None:
            result['Content'] = self.content

        if self.description is not None:
            result['Description'] = self.description

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.set_as_default is not None:
            result['SetAsDefault'] = self.set_as_default

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('SetAsDefault') is not None:
            self.set_as_default = m.get('SetAsDefault')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

