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
        # The callback command for the function lifecycle initialization phase. The handler and command parameters for the lifecycle hook execution entry point cannot be configured at the same time. Only one can take effect. Configuring both produces an error.
        self.command = command
        # The execution entry point of the hook, similar in meaning to the handler.
        self.handler = handler
        # The timeout period of the hook, in seconds.
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

