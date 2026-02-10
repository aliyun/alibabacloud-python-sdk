# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRestorePlansRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        instance_name: str = None,
        page_size: int = None,
        status: str = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The name of the server.
        self.instance_name = instance_name
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The status of the restoration task. Valid values:
        # 
        # *   **init**: initializing
        # *   **created**: creating
        # *   **running**: running
        # *   **completed**: complete
        # *   **error**: failed
        # *   **restoring**: restoring
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

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

