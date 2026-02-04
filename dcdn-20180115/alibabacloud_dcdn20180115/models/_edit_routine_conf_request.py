# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class EditRoutineConfRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        env_conf: Dict[str, Any] = None,
        name: str = None,
    ):
        # The description of the routine.
        self.description = description
        # The configurations of the specified environment.
        self.env_conf = env_conf
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
        if self.description is not None:
            result['Description'] = self.description

        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

