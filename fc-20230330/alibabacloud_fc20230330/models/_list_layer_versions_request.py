# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLayerVersionsRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        start_version: str = None,
    ):
        # The number of versions to be returned.
        self.limit = limit
        # The initial version of the layer.
        self.start_version = start_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.start_version is not None:
            result['startVersion'] = self.start_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('startVersion') is not None:
            self.start_version = m.get('startVersion')

        return self

