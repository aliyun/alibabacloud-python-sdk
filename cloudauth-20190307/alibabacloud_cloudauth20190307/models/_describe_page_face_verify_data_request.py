# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePageFaceVerifyDataRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        product_code: str = None,
        scene_id: int = None,
        start_date: str = None,
    ):
        # Current page number, default is 1.
        self.current_page = current_page
        # Required, end time, format is yyyy-MM-dd, default is yyyy-MM-dd 00:00:00, the query interval cannot exceed 90 days.
        self.end_date = end_date
        # Number of items per page, default is 10.
        self.page_size = page_size
        # Product code.
        self.product_code = product_code
        # Scene ID.
        self.scene_id = scene_id
        # Required, start time, format is yyyy-MM-dd, default is yyyy-MM-dd 00:00:00, the query interval cannot exceed 90 days.
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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

