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
        # Sets the page number from which to start displaying the query results. The default value is 1, indicating that the display starts from the first page.
        self.current_page = current_page
        # The name of the IDC.
        self.idc_name = idc_name
        # Specifies the maximum number of data entries to display per page in a paginated query. The default number of data entries per page is 20, and if the PageSize parameter is empty, it will default to returning 20 data entries.
        # > It is recommended that the PageSize value is not empty.
        self.page_size = page_size
        # Probe status. Values:
        # 
        # - **0**: Enabled
        # - **1**: Disabled
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

