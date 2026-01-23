# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuotaListExportPagedRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        language: str = None,
        page_size: int = None,
    ):
        # Pagination, current page number, starting from 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Multilingual Parameters, the default language is English.</br>
        # en: English</br>
        # zh: Chinese</br>
        # ja: Japanese </br>
        self.language = language
        # Pagination, record number on each page, maximum 100.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.language is not None:
            result['Language'] = self.language

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

