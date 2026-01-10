# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTemplatesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # 当前页码，从1开始计数
        self.page_number = page_number
        # 每页返回的记录数量
        self.page_size = page_size
        self.status = status
        self.template_name = template_name
        # 按模板类型过滤
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.template_type is not None:
            result['templateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')

        return self

