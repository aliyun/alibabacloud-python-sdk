# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRoutineEnvironmentVariablesShrinkRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        environment_variable_keys_shrink: str = None,
        name: str = None,
    ):
        # The environment name.
        # 
        # Valid values:
        # - `staging`: staging environment
        # - `production`: production environment
        # 
        # This parameter is required.
        self.env = env
        # The list of environment variable keys to delete.
        # 
        # This parameter is required.
        self.environment_variable_keys_shrink = environment_variable_keys_shrink
        # The name of the Routine function.
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
        if self.env is not None:
            result['Env'] = self.env

        if self.environment_variable_keys_shrink is not None:
            result['EnvironmentVariableKeys'] = self.environment_variable_keys_shrink

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('EnvironmentVariableKeys') is not None:
            self.environment_variable_keys_shrink = m.get('EnvironmentVariableKeys')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

