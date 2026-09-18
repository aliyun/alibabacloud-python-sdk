# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateMmsDataSourceRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        config: Dict[str, Any] = None,
        name: str = None,
        test: bool = None,
    ):
        # The type of the update operation:
        # 
        # 1. UPDATE_CONFIG: updates the data source configuration.
        # 2. START: starts the data source instance.
        # 3. STOP: shuts down the data source instance.
        # 4. RENAME: renames the data source.
        self.action = action
        # The data source configuration. The configuration items vary based on the data source.
        self.config = config
        # The new name of the data source.
        self.name = name
        # Tests the data source configuration.
        self.test = test

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.config is not None:
            result['config'] = self.config

        if self.name is not None:
            result['name'] = self.name

        if self.test is not None:
            result['test'] = self.test

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('test') is not None:
            self.test = m.get('test')

        return self

