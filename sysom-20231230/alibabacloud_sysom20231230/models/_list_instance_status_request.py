# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceStatusRequest(DaraModel):
    def __init__(
        self,
        current: int = None,
        instance: str = None,
        page_size: int = None,
        region: str = None,
        status: str = None,
    ):
        self.current = current
        self.instance = instance
        self.page_size = page_size
        self.region = region
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['current'] = self.current

        if self.instance is not None:
            result['instance'] = self.instance

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.region is not None:
            result['region'] = self.region

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

