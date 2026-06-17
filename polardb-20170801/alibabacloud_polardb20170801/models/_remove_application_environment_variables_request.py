# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveApplicationEnvironmentVariablesRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        restart: bool = None,
        variable_names: List[str] = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Specifies whether to restart the gateway after removing the variables. The default is `true`.
        self.restart = restart
        # A list of the environment variable names to remove.
        # 
        # This parameter is required.
        self.variable_names = variable_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.restart is not None:
            result['Restart'] = self.restart

        if self.variable_names is not None:
            result['VariableNames'] = self.variable_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        if m.get('VariableNames') is not None:
            self.variable_names = m.get('VariableNames')

        return self

