# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackUpExportInfoRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        export_type: str = None,
        lang: str = None,
        page_size: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The type of archived information. Valid values:
        # 
        # *   **suspiciousExport**: alert event
        # 
        # This parameter is required.
        self.export_type = export_type
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 20.
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

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

