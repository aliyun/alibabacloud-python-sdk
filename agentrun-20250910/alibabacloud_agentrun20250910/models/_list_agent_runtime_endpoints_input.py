# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAgentRuntimeEndpointsInput(DaraModel):
    def __init__(
        self,
        endpoint_name: str = None,
        page_number: int = None,
        page_size: int = None,
        statuses: List[str] = None,
    ):
        # 按端点名称过滤
        self.endpoint_name = endpoint_name
        # 页码
        self.page_number = page_number
        # 每页记录数
        self.page_size = page_size
        # 按状态过滤
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_name is not None:
            result['endpointName'] = self.endpoint_name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.statuses is not None:
            result['statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('statuses') is not None:
            self.statuses = m.get('statuses')

        return self

