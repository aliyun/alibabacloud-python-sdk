# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DLCatalog(DaraModel):
    def __init__(
        self,
        description: str = None,
        location: str = None,
        name: str = None,
    ):
        self.description = description
        self.location = location
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

        if self.location is not None:
            result['Location'] = self.location

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

