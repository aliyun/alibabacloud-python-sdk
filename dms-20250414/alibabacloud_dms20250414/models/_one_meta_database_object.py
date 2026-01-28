# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OneMetaDatabaseObject(DaraModel):
    def __init__(
        self,
        object_name: str = None,
        object_qualified_name: str = None,
        object_type: str = None,
    ):
        self.object_name = object_name
        self.object_qualified_name = object_qualified_name
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.object_qualified_name is not None:
            result['ObjectQualifiedName'] = self.object_qualified_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ObjectQualifiedName') is not None:
            self.object_qualified_name = m.get('ObjectQualifiedName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        return self

