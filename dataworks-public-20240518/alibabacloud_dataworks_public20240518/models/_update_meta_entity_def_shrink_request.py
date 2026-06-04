# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMetaEntityDefShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        entity_type: str = None,
        new_attribute_defs_shrink: str = None,
        update_attribute_defs_shrink: str = None,
    ):
        self.description = description
        self.display_name = display_name
        # This parameter is required.
        self.entity_type = entity_type
        self.new_attribute_defs_shrink = new_attribute_defs_shrink
        self.update_attribute_defs_shrink = update_attribute_defs_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.new_attribute_defs_shrink is not None:
            result['NewAttributeDefs'] = self.new_attribute_defs_shrink

        if self.update_attribute_defs_shrink is not None:
            result['UpdateAttributeDefs'] = self.update_attribute_defs_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('NewAttributeDefs') is not None:
            self.new_attribute_defs_shrink = m.get('NewAttributeDefs')

        if m.get('UpdateAttributeDefs') is not None:
            self.update_attribute_defs_shrink = m.get('UpdateAttributeDefs')

        return self

