# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCodeInterpretersRequest(DaraModel):
    def __init__(
        self,
        code_interpreter_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 根据代码解释器实例名称进行模糊匹配过滤
        self.code_interpreter_name = code_interpreter_name
        # 当前页码，从1开始计数
        self.page_number = page_number
        # 每页返回的记录数量
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_interpreter_name is not None:
            result['codeInterpreterName'] = self.code_interpreter_name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeInterpreterName') is not None:
            self.code_interpreter_name = m.get('codeInterpreterName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

