# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WelcomeBlock(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_type: str = None,
        icon: str = None,
        label: str = None,
        type: str = None,
        value: str = None,
    ):
        self.description = description
        self.display_type = display_type
        self.icon = icon
        self.label = label
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_type is not None:
            result['DisplayType'] = self.display_type

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.label is not None:
            result['Label'] = self.label

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayType') is not None:
            self.display_type = m.get('DisplayType')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

