# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class PreviewNotifyTemplateRequest(DaraModel):
    def __init__(
        self,
        data: Any = None,
        templates: List[main_models.PreviewNotifyTemplateRequestTemplates] = None,
    ):
        self.data = data
        # 待渲染的模板列表，每项包含模板标识和模板内容
        # 
        # This parameter is required.
        self.templates = templates

    def validate(self):
        if self.templates:
            for v1 in self.templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        result['templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['templates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        self.templates = []
        if m.get('templates') is not None:
            for k1 in m.get('templates'):
                temp_model = main_models.PreviewNotifyTemplateRequestTemplates()
                self.templates.append(temp_model.from_map(k1))

        return self

class PreviewNotifyTemplateRequestTemplates(DaraModel):
    def __init__(
        self,
        key: str = None,
        template: str = None,
    ):
        # 模板标识，前端自定义，原样返回。建议使用 title / content 等语义名称
        # 
        # This parameter is required.
        self.key = key
        # Go template 语法的模板内容字符串
        # 
        # This parameter is required.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.template is not None:
            result['template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('template') is not None:
            self.template = m.get('template')

        return self

