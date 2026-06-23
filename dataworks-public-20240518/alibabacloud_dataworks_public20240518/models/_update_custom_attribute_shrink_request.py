# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCustomAttributeShrinkRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        display_enabled: bool = None,
        display_name: str = None,
        entity_types_shrink: str = None,
        id: str = None,
        search_filter_enabled: bool = None,
        value_enums_shrink: str = None,
    ):
        # The new description for the custom attribute. It must be 256 characters or less.
        self.comment = comment
        # Whether to display the custom attribute in the UI.
        self.display_enabled = display_enabled
        # The new display name for the custom attribute. It must be 128 characters or less.
        self.display_name = display_name
        # The applicable entity types. This parameter supports specific types and wildcard formats, such as `*-table` and `*-column`. For example:
        # 
        # - `dataworks-project`: A DataWorks workspace
        # 
        # - `dataworks-dataset`: A DataWorks dataset
        # 
        # - `maxcompute-table`: A MaxCompute table
        # 
        # - `*-column`: All column types
        self.entity_types_shrink = entity_types_shrink
        # The custom attribute ID.
        # 
        # This parameter is required.
        self.id = id
        # Whether the custom attribute can be used as a filter condition.
        self.search_filter_enabled = search_filter_enabled
        # The enumerated values. This applies only to custom attributes of the `enum` type. You can only append new values during an update.
        self.value_enums_shrink = value_enums_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.display_enabled is not None:
            result['DisplayEnabled'] = self.display_enabled

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.entity_types_shrink is not None:
            result['EntityTypes'] = self.entity_types_shrink

        if self.id is not None:
            result['Id'] = self.id

        if self.search_filter_enabled is not None:
            result['SearchFilterEnabled'] = self.search_filter_enabled

        if self.value_enums_shrink is not None:
            result['ValueEnums'] = self.value_enums_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DisplayEnabled') is not None:
            self.display_enabled = m.get('DisplayEnabled')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EntityTypes') is not None:
            self.entity_types_shrink = m.get('EntityTypes')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SearchFilterEnabled') is not None:
            self.search_filter_enabled = m.get('SearchFilterEnabled')

        if m.get('ValueEnums') is not None:
            self.value_enums_shrink = m.get('ValueEnums')

        return self

