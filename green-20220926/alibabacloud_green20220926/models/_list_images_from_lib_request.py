# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ListImagesFromLibRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        img_id: str = None,
        lib_id: str = None,
        page_size: int = None,
        region_id: str = None,
        sort: Dict[str, str] = None,
        start_date: str = None,
    ):
        # Current page number.
        self.current_page = current_page
        # End date.
        self.end_date = end_date
        # Image ID.
        self.img_id = img_id
        # Gallery ID.
        self.lib_id = lib_id
        # Page size.
        self.page_size = page_size
        # Region ID.
        self.region_id = region_id
        # Sort field.
        self.sort = sort
        # Start date.
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

        if self.img_id is not None:
            result['ImgId'] = self.img_id

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ImgId') is not None:
            self.img_id = m.get('ImgId')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

