# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDiagnosisRequest(DaraModel):
    def __init__(
        self,
        current: int = None,
        page_size: int = None,
        params: str = None,
        service_name: str = None,
        status: str = None,
    ):
        self.current = current
        self.page_size = page_size
        self.params = params
        self.service_name = service_name
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

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.params is not None:
            result['params'] = self.params

        if self.service_name is not None:
            result['service_name'] = self.service_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

