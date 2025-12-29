# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeJobHistoryRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        page_size: int = None,
        state: str = None,
    ):
        # The ID of the job template.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The number of the page to return.
        self.current_page = current_page
        # The number of entries to return on each page. Valid values: 0 to 10000.
        self.page_size = page_size
        # The status of the job. Valid values:
        # 
        # *   **0**: The job is not executed.
        # *   **1**: The job is executed.
        # *   **2**: The job fails to be executed.
        # *   **3**: The job is being executed.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

