# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ActionIntegrationConfig(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        enabled: bool = None,
    ):
        # 行动集成 ID 列表
        self.actions = actions
        # 是否启用行动集成
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

