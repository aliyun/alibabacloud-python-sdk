# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSensitiveSwitchRequest(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        parent_category: str = None,
        sensitive_category: str = None,
        sensitive_level: str = None,
        switch_status: str = None,
    ):
        self.category_name = category_name
        self.current_page = current_page
        self.lang = lang
        self.page_size = page_size
        self.parent_category = parent_category
        self.sensitive_category = sensitive_category
        self.sensitive_level = sensitive_level
        self.switch_status = switch_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_category is not None:
            result['ParentCategory'] = self.parent_category

        if self.sensitive_category is not None:
            result['SensitiveCategory'] = self.sensitive_category

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentCategory') is not None:
            self.parent_category = m.get('ParentCategory')

        if m.get('SensitiveCategory') is not None:
            self.sensitive_category = m.get('SensitiveCategory')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        return self

