# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationEnvironmentVariablesShrinkRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        restart: bool = None,
        variables_shrink: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Specifies whether to restart the gateway after the update. The default value is true.
        self.restart = restart
        # A mapping from environment variable names to values.
        self.variables_shrink = variables_shrink

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

        if self.variables_shrink is not None:
            result['Variables'] = self.variables_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        if m.get('Variables') is not None:
            self.variables_shrink = m.get('Variables')

        return self

