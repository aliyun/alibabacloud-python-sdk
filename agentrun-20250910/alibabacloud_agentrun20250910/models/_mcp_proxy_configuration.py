# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class McpProxyConfiguration(DaraModel):
    def __init__(
        self,
        hooks: List[main_models.Hook] = None,
    ):
        # MCP 代理的钩子函数配置列表，每个钩子可以在请求处理的不同阶段执行自定义逻辑
        self.hooks = hooks

    def validate(self):
        if self.hooks:
            for v1 in self.hooks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['hooks'] = []
        if self.hooks is not None:
            for k1 in self.hooks:
                result['hooks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hooks = []
        if m.get('hooks') is not None:
            for k1 in m.get('hooks'):
                temp_model = main_models.Hook()
                self.hooks.append(temp_model.from_map(k1))

        return self

