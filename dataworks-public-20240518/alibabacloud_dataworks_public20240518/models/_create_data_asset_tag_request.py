# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateDataAssetTagRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        managers: List[str] = None,
        value_type: str = None,
        values: List[str] = None,
    ):
        # The description of the tag.
        self.description = description
        # The tag key.
        # 
        # This parameter is required.
        self.key = key
        # The tag administrators.
        self.managers = managers
        # The type of the tag value. Valid values:
        # 
        # *   Boolean
        # *   Int
        # *   String
        # *   Double
        self.value_type = value_type
        # The tag values.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        if self.managers is not None:
            result['Managers'] = self.managers

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Managers') is not None:
            self.managers = m.get('Managers')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

