# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSmartStatisticsPageListRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        end_date: str = None,
        page_size: str = None,
        scene_id: str = None,
        service_code: str = None,
        start_date: str = None,
    ):
        # Current page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # End time, using UTC format, in the form of yyyy-MM-ddTHH:mm:ssZ.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Number of items per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Scene ID.
        # 
        # This parameter is required.
        self.scene_id = scene_id
        # ServiceCode for the real person cloud product, only value: **cloudauthst**.
        self.service_code = service_code
        # Start time, using UTC format, in the form of yyyy-MM-ddTHH:mm:ssZ.
        # 
        # This parameter is required.
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

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

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

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

