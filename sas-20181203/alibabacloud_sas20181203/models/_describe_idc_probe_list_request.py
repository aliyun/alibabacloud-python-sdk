# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIdcProbeListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        idc_name: str = None,
        page_size: int = None,
        status: int = None,
    ):
        # The page number of the page to return. Default value: 1, which indicates that the first page is returned.
        self.current_page = current_page
        # The name of the IDC.
        self.idc_name = idc_name
        # The maximum number of entries per page when paging. Default value: 20. If you leave this parameter empty, 20 entries are returned per page.
        # > Do not leave PageSize empty.
        self.page_size = page_size
        # The usage status of the probe. Valid values:
        # 
        # - **0**: enabled
        # - **1**: disabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.idc_name is not None:
            result['IdcName'] = self.idc_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('IdcName') is not None:
            self.idc_name = m.get('IdcName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

