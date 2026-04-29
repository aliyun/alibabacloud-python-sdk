# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateApplicationEnvironmentVariablesRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        restart: bool = None,
        variables: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.restart = restart
        self.variables = variables

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

        if self.variables is not None:
            result['Variables'] = self.variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        if m.get('Variables') is not None:
            self.variables = m.get('Variables')

        return self

