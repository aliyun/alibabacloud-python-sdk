# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InstanceExecAuthorizationInputOptions(DaraModel):
    def __init__(
        self,
        command: List[str] = None,
        stderr: bool = None,
        stdin: bool = None,
        stdout: bool = None,
        tty: bool = None,
    ):
        self.command = command
        self.stderr = stderr
        self.stdin = stdin
        self.stdout = stdout
        self.tty = tty

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['command'] = self.command

        if self.stderr is not None:
            result['stderr'] = self.stderr

        if self.stdin is not None:
            result['stdin'] = self.stdin

        if self.stdout is not None:
            result['stdout'] = self.stdout

        if self.tty is not None:
            result['tty'] = self.tty

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('command') is not None:
            self.command = m.get('command')

        if m.get('stderr') is not None:
            self.stderr = m.get('stderr')

        if m.get('stdin') is not None:
            self.stdin = m.get('stdin')

        if m.get('stdout') is not None:
            self.stdout = m.get('stdout')

        if m.get('tty') is not None:
            self.tty = m.get('tty')

        return self

