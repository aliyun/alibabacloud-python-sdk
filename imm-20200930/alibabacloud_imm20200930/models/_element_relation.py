# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ElementRelation(DaraModel):
    def __init__(
        self,
        object_id: str = None,
        type: str = None,
    ):
        # The ID of the element.
        self.object_id = object_id
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

