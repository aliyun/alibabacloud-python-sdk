# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAssetCountRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: int = None,
        show_size: int = None,
        start_date: int = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.show_size = show_size
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

