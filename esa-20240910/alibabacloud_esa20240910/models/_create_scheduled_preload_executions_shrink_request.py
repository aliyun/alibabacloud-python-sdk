# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScheduledPreloadExecutionsShrinkRequest(DaraModel):
    def __init__(
        self,
        executions_shrink: str = None,
        id: str = None,
    ):
        # This parameter is required.
        self.executions_shrink = executions_shrink
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executions_shrink is not None:
            result['Executions'] = self.executions_shrink

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Executions') is not None:
            self.executions_shrink = m.get('Executions')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

