# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVirusScanMachineRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        remark: str = None,
        uuid: str = None,
    ):
        # The page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The information about the server that you want to query. The value can be the name or the IP address of the server.
        self.remark = remark
        # The UUID of the server.
        self.uuid = uuid

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

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

