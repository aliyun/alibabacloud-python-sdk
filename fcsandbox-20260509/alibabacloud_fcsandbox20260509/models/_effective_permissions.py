# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class EffectivePermissions(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        capabilities: List[str] = None,
    ):
        # The actions.
        self.actions = actions
        # The capabilities.
        self.capabilities = capabilities

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.capabilities is not None:
            result['capabilities'] = self.capabilities

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('capabilities') is not None:
            self.capabilities = m.get('capabilities')

        return self

