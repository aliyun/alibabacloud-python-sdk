# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateParameterShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        owner: str = None,
        properties_shrink: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.id = id
        self.owner = owner
        self.properties_shrink = properties_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.properties_shrink is not None:
            result['Properties'] = self.properties_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Properties') is not None:
            self.properties_shrink = m.get('Properties')

        return self

