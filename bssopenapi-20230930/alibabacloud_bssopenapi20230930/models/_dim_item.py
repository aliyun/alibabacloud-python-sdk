# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class DimItem(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        page_info: main_models.DimItemPageInfo = None,
        values: List[main_models.ItemValues] = None,
    ):
        self.code = code
        self.name = name
        self.page_info = page_info
        self.values = values

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.values:
            for v1 in self.values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageInfo') is not None:
            temp_model = main_models.DimItemPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.ItemValues()
                self.values.append(temp_model.from_map(k1))

        return self



class DimItemPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

