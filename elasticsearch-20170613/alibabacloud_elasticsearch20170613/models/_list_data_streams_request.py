# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataStreamsRequest(DaraModel):
    def __init__(
        self,
        is_managed: bool = None,
        name: str = None,
    ):
        self.is_managed = is_managed
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_managed is not None:
            result['isManaged'] = self.is_managed

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

