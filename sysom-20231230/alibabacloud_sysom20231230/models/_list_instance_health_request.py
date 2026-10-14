# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceHealthRequest(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        current: int = None,
        end: float = None,
        instance: str = None,
        page_size: int = None,
        start: float = None,
    ):
        # The cluster ID.
        self.cluster = cluster
        # The current page number.
        self.current = current
        # The end time.
        # 
        # This parameter is required.
        self.end = end
        # The instance ID.
        self.instance = instance
        # The number of entries per page. Default value: 5. Valid values: 1 to 100.
        self.page_size = page_size
        # The start time.
        # 
        # This parameter is required.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.current is not None:
            result['current'] = self.current

        if self.end is not None:
            result['end'] = self.end

        if self.instance is not None:
            result['instance'] = self.instance

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.start is not None:
            result['start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('start') is not None:
            self.start = m.get('start')

        return self

