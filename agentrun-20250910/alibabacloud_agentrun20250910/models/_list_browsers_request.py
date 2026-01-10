# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBrowsersRequest(DaraModel):
    def __init__(
        self,
        browser_name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # 根据浏览器实例名称进行模糊匹配过滤
        self.browser_name = browser_name
        # 当前页码，从1开始计数
        self.page_number = page_number
        # 每页返回的记录数量
        self.page_size = page_size
        # 根据浏览器实例的运行状态进行过滤，可选值：CREATING、READY、DELETING等
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_name is not None:
            result['browserName'] = self.browser_name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browserName') is not None:
            self.browser_name = m.get('browserName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

