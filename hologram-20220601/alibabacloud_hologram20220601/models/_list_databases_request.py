# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatabasesRequest(DaraModel):
    def __init__(
        self,
        external: bool = None,
    ):
        self.external = external

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external is not None:
            result['external'] = self.external

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('external') is not None:
            self.external = m.get('external')

        return self

