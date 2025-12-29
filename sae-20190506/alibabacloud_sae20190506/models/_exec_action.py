# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ExecAction(DaraModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['command'] = self.command

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('command') is not None:
            self.command = m.get('command')

        return self

