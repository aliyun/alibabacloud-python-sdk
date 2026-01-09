# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMetricStoresRequest(DaraModel):
    def __init__(
        self,
        mode: str = None,
        name: str = None,
        offset: int = None,
        size: int = None,
    ):
        # The type of the Metricstore. For example, you can set the parameter to standard to query Standard Metricstores.
        self.mode = mode
        # The name of the Metricstore. Fuzzy search is supported. If you do not specify this parameter, all Metricstores are involved.
        self.name = name
        # The start position of the query.
        self.offset = offset
        # The number of entries per page.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['mode'] = self.mode

        if self.name is not None:
            result['name'] = self.name

        if self.offset is not None:
            result['offset'] = self.offset

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

