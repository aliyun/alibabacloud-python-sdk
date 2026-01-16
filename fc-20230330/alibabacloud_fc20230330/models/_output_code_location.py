# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OutputCodeLocation(DaraModel):
    def __init__(
        self,
        location: str = None,
        repository_type: str = None,
    ):
        self.location = location
        self.repository_type = repository_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.location is not None:
            result['location'] = self.location

        if self.repository_type is not None:
            result['repositoryType'] = self.repository_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('repositoryType') is not None:
            self.repository_type = m.get('repositoryType')

        return self

