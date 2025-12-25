# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSubSceneShrinkRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        view_point_shrink: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.name = name
        self.view_point_shrink = view_point_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.view_point_shrink is not None:
            result['ViewPoint'] = self.view_point_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ViewPoint') is not None:
            self.view_point_shrink = m.get('ViewPoint')

        return self

