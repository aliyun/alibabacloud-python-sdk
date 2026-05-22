# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateListRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        items: List[str] = None,
        kind: str = None,
        name: str = None,
    ):
        # The description of the list that you want to create.
        self.description = description
        # The items in the list that you want to create.
        self.items = items
        # The type of the list that you want to create.
        self.kind = kind
        # The name of the list that you want to create.
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

        if self.items is not None:
            result['Items'] = self.items

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
            self.items = m.get('Items')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

