# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveApplicationEnvironmentVariablesShrinkRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        restart: bool = None,
        variable_names_shrink: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.restart = restart
        # This parameter is required.
        self.variable_names_shrink = variable_names_shrink

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

        if self.variable_names_shrink is not None:
            result['VariableNames'] = self.variable_names_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        if m.get('VariableNames') is not None:
            self.variable_names_shrink = m.get('VariableNames')

        return self

