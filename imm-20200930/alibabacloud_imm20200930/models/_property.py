# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Property(DaraModel):
    def __init__(
        self,
        items_type: str = None,
        name: str = None,
        value: str = None,
        value_type: str = None,
    ):
        # If you set the ValueType field to array, you must specify the type of the elements within the array. The enumerated values include float, integer, and string.
        self.items_type = items_type
        # The property name.
        self.name = name
        # The value.
        self.value = value
        # The type of the property. Supported enumerated values: float, integer, string, and array.
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items_type is not None:
            result['ItemsType'] = self.items_type

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemsType') is not None:
            self.items_type = m.get('ItemsType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

