# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetaStatisticsPageListRequest(DaraModel):
    def __init__(
        self,
        api: str = None,
        current_page: int = None,
        end_date: int = None,
        page_size: int = None,
        start_date: int = None,
    ):
        # Product API:
        # - **ID_CARD_2_META**: ID Card Two-Element Verification
        # - **ID_PERIOD**: ID Card Validity Verification Period
        # - **MOBILE_ONLINE_LENGTH**: Mobile Online Duration
        # - **MOBILE_ONLINE_STATUS**: Mobile Online Status
        # - **MOBILE_3_META_SIMPLE**: Mobile Number Three-Element Verification (Simple)
        # - **MOBILE_3_META**: Mobile Number Three-Element Verification (Detailed)
        # - **MOBILE_2_META**: Mobile Number Two-Element Verification
        # - **BANK_CARD_N_META**: Bank Card Verification (Detailed)
        # - **MOBILE_DETECT**: Number Detection
        # - **VEHICLE_N_META**: Vehicle Element Verification (Enhanced)
        # - **VEHICLE_PENTA_INFO**: Vehicle Five-Element Information Recognition
        # - **VEHICLE_LICENSE_INFO**: Vehicle Information Recognition
        # - **VEHICLE_INSURE_DATE**: Vehicle Insurance Date Query
        # - **VEHICLE_CHECK**: Vehicle Element Verification
        # 
        # This parameter is required.
        self.api = api
        # Current page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Query end time. Unix timestamp.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Number of data entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Query start time. The timestamp is in milliseconds.
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
        if self.api is not None:
            result['Api'] = self.api

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

