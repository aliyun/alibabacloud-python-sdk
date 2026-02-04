# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRoutineConfEnvsShrinkRequest(DaraModel):
    def __init__(
        self,
        envs_shrink: str = None,
        name: str = None,
    ):
        # The custom canary release environments that you want to delete.
        # 
        # This parameter is required.
        self.envs_shrink = envs_shrink
        # The name of the routine. The name must be unique among the routines that belong to the same Alibaba Cloud account.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.envs_shrink is not None:
            result['Envs'] = self.envs_shrink

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Envs') is not None:
            self.envs_shrink = m.get('Envs')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

