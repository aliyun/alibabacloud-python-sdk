# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRoutineBuildRequest(DaraModel):
    def __init__(
        self,
        routine_build_id: int = None,
    ):
        # The ID of the ER build task.
        # 
        # This parameter is required.
        self.routine_build_id = routine_build_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.routine_build_id is not None:
            result['RoutineBuildId'] = self.routine_build_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoutineBuildId') is not None:
            self.routine_build_id = m.get('RoutineBuildId')

        return self

