# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AutoPassPolicy(DaraModel):
    def __init__(
        self,
        command_prefix: List[str] = None,
        full_command: str = None,
        version: str = None,
    ):
        # The selected command prefix. The array must contain exactly one prefix. You must specify either this parameter or fullCommand.
        self.command_prefix = command_prefix
        # The full command for exact matching. The command must not be empty. You must specify either this parameter or commandPrefix.
        self.full_command = full_command
        # The version required for a valid rule. The current version is v1.0.0.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_prefix is not None:
            result['commandPrefix'] = self.command_prefix

        if self.full_command is not None:
            result['fullCommand'] = self.full_command

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commandPrefix') is not None:
            self.command_prefix = m.get('commandPrefix')

        if m.get('fullCommand') is not None:
            self.full_command = m.get('fullCommand')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

