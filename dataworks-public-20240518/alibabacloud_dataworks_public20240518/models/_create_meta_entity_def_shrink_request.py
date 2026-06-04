# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMetaEntityDefShrinkRequest(DaraModel):
    def __init__(
        self,
        attribute_defs_shrink: str = None,
        description: str = None,
        display_name: str = None,
        extend: str = None,
        name: str = None,
    ):
        self.attribute_defs_shrink = attribute_defs_shrink
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        self.extend = extend
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_defs_shrink is not None:
            result['AttributeDefs'] = self.attribute_defs_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeDefs') is not None:
            self.attribute_defs_shrink = m.get('AttributeDefs')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

