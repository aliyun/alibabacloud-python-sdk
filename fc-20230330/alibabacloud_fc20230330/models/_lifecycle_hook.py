# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class LifecycleHook(DaraModel):
    def __init__(
        self,
        command: List[str] = None,
        handler: str = None,
        timeout: int = None,
    ):
        # 函数生命周期初始化阶段回调指令，生命周期回调方法的执行入口 handler 和 command 不允许同时配置，只能有一个生效，同时配置会产生错误提示
        self.command = command
        # The handler of the hook. The definition is similar to that of a request handler.
        self.handler = handler
        # The timeout period of the hook. Unit: seconds.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['command'] = self.command

        if self.handler is not None:
            result['handler'] = self.handler

        if self.timeout is not None:
            result['timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('command') is not None:
            self.command = m.get('command')

        if m.get('handler') is not None:
            self.handler = m.get('handler')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        return self

