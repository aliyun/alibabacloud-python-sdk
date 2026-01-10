# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentRuntimeEndpointsRequest(DaraModel):
    def __init__(
        self,
        endpoint_name: str = None,
        page_number: int = None,
        page_size: int = None,
        search_mode: str = None,
    ):
        # 根据端点名称进行模糊匹配过滤
        self.endpoint_name = endpoint_name
        # 当前页码，从1开始计数
        self.page_number = page_number
        # 每页返回的记录数量
        self.page_size = page_size
        # 查询模式，支持精确查询和模糊查询
        self.search_mode = search_mode

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

        if self.search_mode is not None:
            result['searchMode'] = self.search_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('searchMode') is not None:
            self.search_mode = m.get('searchMode')

        return self

