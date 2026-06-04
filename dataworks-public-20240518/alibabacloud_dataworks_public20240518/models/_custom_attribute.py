# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CustomAttribute(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: int = None,
        display_enabled: bool = None,
        display_name: str = None,
        entity_types: List[str] = None,
        id: str = None,
        modify_time: int = None,
        search_filter_enabled: bool = None,
        type: str = None,
        value_enums: List[str] = None,
    ):
        self.comment = comment
        self.create_time = create_time
        self.display_enabled = display_enabled
        self.display_name = display_name
        self.entity_types = entity_types
        self.id = id
        self.modify_time = modify_time
        self.search_filter_enabled = search_filter_enabled
        self.type = type
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.display_enabled is not None:
            result['DisplayEnabled'] = self.display_enabled

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.entity_types is not None:
            result['EntityTypes'] = self.entity_types

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

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

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DisplayEnabled') is not None:
            self.display_enabled = m.get('DisplayEnabled')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EntityTypes') is not None:
            self.entity_types = m.get('EntityTypes')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('SearchFilterEnabled') is not None:
            self.search_filter_enabled = m.get('SearchFilterEnabled')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValueEnums') is not None:
            self.value_enums = m.get('ValueEnums')

        return self

