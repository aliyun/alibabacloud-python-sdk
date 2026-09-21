# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class SetRoutineEnvironmentVariablesRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        environment_variables: Dict[str, main_models.EnvironmentVariablesValue] = None,
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
        self.environment_variables = environment_variables
        # The function name.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.environment_variables:
            for v1 in self.environment_variables.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        result['EnvironmentVariables'] = {}
        if self.environment_variables is not None:
            for k1, v1 in self.environment_variables.items():
                result['EnvironmentVariables'][k1] = v1.to_map() if v1 else None

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        self.environment_variables = {}
        if m.get('EnvironmentVariables') is not None:
            for k1, v1 in m.get('EnvironmentVariables').items():
                temp_model = main_models.EnvironmentVariablesValue()
                self.environment_variables[k1] = temp_model.from_map(v1)

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

