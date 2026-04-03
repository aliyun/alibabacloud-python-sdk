# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class BoundConfiguration(DaraModel):
    def __init__(
        self,
        bound_tools: List[main_models.BoundTool] = None,
    ):
        # 绑定的工具配置列表，每个配置项定义一个工具与特定 HTTP 路径和方法的绑定关系
        self.bound_tools = bound_tools

    def validate(self):
        if self.bound_tools:
            for v1 in self.bound_tools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['boundTools'] = []
        if self.bound_tools is not None:
            for k1 in self.bound_tools:
                result['boundTools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bound_tools = []
        if m.get('boundTools') is not None:
            for k1 in m.get('boundTools'):
                temp_model = main_models.BoundTool()
                self.bound_tools.append(temp_model.from_map(k1))

        return self

