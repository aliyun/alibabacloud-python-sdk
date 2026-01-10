# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CustomRuntimeConfig(DaraModel):
    def __init__(
        self,
        args: List[str] = None,
        command: List[str] = None,
        port: int = None,
    ):
        self.args = args
        self.command = command
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['args'] = self.args

        if self.command is not None:
            result['command'] = self.command

        if self.port is not None:
            result['port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')

        if m.get('command') is not None:
            self.command = m.get('command')

        if m.get('port') is not None:
            self.port = m.get('port')

        return self

