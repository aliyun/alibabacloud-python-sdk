# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSnapshotInput(DaraModel):
    def __init__(
        self,
        name: str = None,
        sandbox_id: str = None,
        team_id: str = None,
    ):
        # The snapshot name.
        self.name = name
        # The source sandbox ID.
        # 
        # This parameter is required.
        self.sandbox_id = sandbox_id
        # The team ID.
        # 
        # This parameter is required.
        self.team_id = team_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.sandbox_id is not None:
            result['sandboxID'] = self.sandbox_id

        if self.team_id is not None:
            result['teamID'] = self.team_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        return self

