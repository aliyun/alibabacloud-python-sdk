# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceResourceRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        group: str = None,
        type: str = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.category = category
        # This parameter is required.
        self.group = group
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.group is not None:
            result['Group'] = self.group

        if self.type is not None:
            result['Type'] = self.type

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

