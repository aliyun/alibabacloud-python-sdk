# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateListShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        items_shrink: str = None,
        kind: str = None,
        name: str = None,
    ):
        # The description of the custom list. This parameter provides detailed information about the custom list.
        self.description = description
        # The list items. This parameter provides the specific item data for the list.
        self.items_shrink = items_shrink
        # The kind of the custom list. This parameter specifies the type of the custom list.
        self.kind = kind
        # The name of the custom list.
        # 
        # **Naming rules**: Only letters, digits, and underscores are supported (`^\\w{1,64}$`). The name must be 1 to 64 characters in length.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.items_shrink is not None:
            result['Items'] = self.items_shrink

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Items') is not None:
            self.items_shrink = m.get('Items')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

