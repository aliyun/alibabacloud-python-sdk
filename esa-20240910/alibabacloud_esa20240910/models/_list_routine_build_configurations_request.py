# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRoutineBuildConfigurationsRequest(DaraModel):
    def __init__(
        self,
        routine_names: str = None,
    ):
        # The list of ER routine names, separated by commas.
        # 
        # This parameter is required.
        self.routine_names = routine_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.routine_names is not None:
            result['RoutineNames'] = self.routine_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoutineNames') is not None:
            self.routine_names = m.get('RoutineNames')

        return self

