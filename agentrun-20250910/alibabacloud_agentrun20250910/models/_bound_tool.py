# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BoundTool(DaraModel):
    def __init__(
        self,
        method: str = None,
        path: str = None,
        tool_name: str = None,
    ):
        # 绑定的 HTTP 请求方法，支持：GET、PUT、POST、PATCH、DELETE、OPTIONS
        self.method = method
        # 绑定的 URL 路径，用于路由匹配
        self.path = path
        # 要绑定的工具名称
        self.tool_name = tool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.method is not None:
            result['method'] = self.method

        if self.path is not None:
            result['path'] = self.path

        if self.tool_name is not None:
            result['toolName'] = self.tool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('toolName') is not None:
            self.tool_name = m.get('toolName')

        return self

