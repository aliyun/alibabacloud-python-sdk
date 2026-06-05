# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHiveAttributeRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        hive_id: str = None,
        name: str = None,
    ):
        self.description = description
        # ID
        # 
        # This parameter is required.
        self.hive_id = hive_id
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

        if self.hive_id is not None:
            result['HiveId'] = self.hive_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HiveId') is not None:
            self.hive_id = m.get('HiveId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

