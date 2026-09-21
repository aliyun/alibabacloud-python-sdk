# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetRoutineEnvironmentVariablesShrinkRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        environment_variables_shrink: str = None,
        name: str = None,
    ):
        # The environment name. Valid values:
        # - `staging`: staging environment.
        # - `production`: production environment.
        # 
        # This parameter is required.
        self.env = env
        # The dictionary of environment variables. The key is the environment variable name, and the value is the environment variable value.
        # 
        # This parameter is required.
        self.environment_variables_shrink = environment_variables_shrink
        # The function name.
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

        if self.environment_variables_shrink is not None:
            result['EnvironmentVariables'] = self.environment_variables_shrink

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('EnvironmentVariables') is not None:
            self.environment_variables_shrink = m.get('EnvironmentVariables')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

