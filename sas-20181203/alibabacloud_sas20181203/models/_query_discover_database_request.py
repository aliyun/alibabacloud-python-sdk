# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDiscoverDatabaseRequest(DaraModel):
    def __init__(
        self,
        create_mark: str = None,
    ):
        # The ID of the scan task.
        # 
        # > You can call the [StartDiscoverDatabaseTask](~~StartDiscoverDatabaseTask~~) operation to query the ID of the task.
        self.create_mark = create_mark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_mark is not None:
            result['CreateMark'] = self.create_mark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateMark') is not None:
            self.create_mark = m.get('CreateMark')

        return self

