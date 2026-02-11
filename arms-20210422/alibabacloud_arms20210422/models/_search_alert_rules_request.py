# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchAlertRulesRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        current_page: int = None,
        page_size: int = None,
        pid: str = None,
        region_id: str = None,
        title: str = None,
        type: str = None,
    ):
        self.app_type = app_type
        self.current_page = current_page
        self.page_size = page_size
        self.pid = pid
        # This parameter is required.
        self.region_id = region_id
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

