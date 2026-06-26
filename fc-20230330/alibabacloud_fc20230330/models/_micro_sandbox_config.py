# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MicroSandboxConfig(DaraModel):
    def __init__(
        self,
        os_type: str = None,
        ready_command: str = None,
        start_command: str = None,
    ):
        self.os_type = os_type
        self.ready_command = ready_command
        self.start_command = start_command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.os_type is not None:
            result['osType'] = self.os_type

        if self.ready_command is not None:
            result['readyCommand'] = self.ready_command

        if self.start_command is not None:
            result['startCommand'] = self.start_command

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('osType') is not None:
            self.os_type = m.get('osType')

        if m.get('readyCommand') is not None:
            self.ready_command = m.get('readyCommand')

        if m.get('startCommand') is not None:
            self.start_command = m.get('startCommand')

        return self

