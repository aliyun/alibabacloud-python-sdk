# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MetaEntityAttributeDef(DaraModel):
    def __init__(
        self,
        allowed_values: List[str] = None,
        description: str = None,
        display_enabled: bool = None,
        display_name: str = None,
        is_optional: bool = None,
        name: str = None,
        search_filter_enabled: bool = None,
        type: str = None,
    ):
        self.allowed_values = allowed_values
        self.description = description
        self.display_enabled = display_enabled
        self.display_name = display_name
        self.is_optional = is_optional
        self.name = name
        self.search_filter_enabled = search_filter_enabled
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values

        if self.description is not None:
            result['Description'] = self.description

        if self.display_enabled is not None:
            result['DisplayEnabled'] = self.display_enabled

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.is_optional is not None:
            result['IsOptional'] = self.is_optional

        if self.name is not None:
            result['Name'] = self.name

        if self.search_filter_enabled is not None:
            result['SearchFilterEnabled'] = self.search_filter_enabled

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayEnabled') is not None:
            self.display_enabled = m.get('DisplayEnabled')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('IsOptional') is not None:
            self.is_optional = m.get('IsOptional')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SearchFilterEnabled') is not None:
            self.search_filter_enabled = m.get('SearchFilterEnabled')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

