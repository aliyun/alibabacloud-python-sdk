# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateCustomAttributeRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        display_enabled: bool = None,
        display_name: str = None,
        entity_types: List[str] = None,
        id: str = None,
        search_filter_enabled: bool = None,
        type: str = None,
        value_enums: List[str] = None,
    ):
        # The description of the custom attribute. The description must be less than 256 characters in length.
        self.comment = comment
        # Specifies whether to display the attribute on the product page. The default value is true.
        self.display_enabled = display_enabled
        # The display name of the custom attribute. The name must be less than 128 characters in length.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The list of applicable entity types. You can specify precise entity types or use wildcards such as `*-table` and `*-column`. Examples:
        # 
        # - dataworks-project: a DataWorks workspace.
        # 
        # - dataworks-dataset: a DataWorks dataset.
        # 
        # - maxcompute-table: a MaxCompute table.
        # 
        # - \\*-column: all field types.
        # 
        # This parameter is required.
        self.entity_types = entity_types
        # The ID of the custom attribute. The ID must match the regular expression `^custom-attribute:[A-Za-z][A-Za-z0-9_]{0,98}$`. The part after \\`custom-attribute:\\` must be less than 100 characters in length.
        # 
        # This parameter is required.
        self.id = id
        # Specifies whether the attribute can be used as a filter on the Data Map search page. The default value is false. Currently, you can set this parameter to true only for attributes of the ENUM type.
        self.search_filter_enabled = search_filter_enabled
        # The type of the custom attribute. Valid values are ENUM, TEXT, and HYPERLINK.
        # 
        # This parameter is required.
        self.type = type
        # The enumeration values. This parameter is required when \\`Type\\` is set to \\`ENUM\\`. It is not supported for the TEXT and HYPERLINK types.
        self.value_enums = value_enums

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

        if self.entity_types is not None:
            result['EntityTypes'] = self.entity_types

        if self.id is not None:
            result['Id'] = self.id

        if self.search_filter_enabled is not None:
            result['SearchFilterEnabled'] = self.search_filter_enabled

        if self.type is not None:
            result['Type'] = self.type

        if self.value_enums is not None:
            result['ValueEnums'] = self.value_enums

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
            self.entity_types = m.get('EntityTypes')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SearchFilterEnabled') is not None:
            self.search_filter_enabled = m.get('SearchFilterEnabled')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValueEnums') is not None:
            self.value_enums = m.get('ValueEnums')

        return self

