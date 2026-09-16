# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInfoCheckExportRecordRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        product_type: str = None,
        start_date: str = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The query end time. Format: YYYY-MM-DD HH:mm:ss, for example, 2025-10-11 21:24:48.
        self.end_date = end_date
        # The number of entries per page.
        self.page_size = page_size
        # The product type. Valid values:
        # - **ID_CARD_2_META**: ID card two-element verification.
        # - **ID_PERIOD**: ID card validity period verification.
        # - **MOBILE_ONLINE_LENGTH**: Mobile number online duration.
        # - **MOBILE_ONLINE_STATUS**: Mobile number online status.
        # - **MOBILE_3_META_SIMPLE**: Mobile number three-element verification (simple edition).
        # - **MOBILE_3_META**: Mobile number three-element verification (detailed edition).
        # - **MOBILE_2_META**: Mobile number two-element verification.
        # - **BANK_CARD_N_META**: Bank card verification (detailed edition).
        # - **MOBILE_DETECT**: Number detection.
        # - **VEHICLE_N_META**: Vehicle element verification (enhanced edition).
        # - **VEHICLE_PENTA_INFO**: Vehicle five-element information recognition.
        # - **VEHICLE_LICENSE_INFO**: Vehicle information recognition.
        # - **VEHICLE_INSURE_DATE**: Vehicle insurance date query.
        # - **VEHICLE_CHECK**: Vehicle element verification.
        self.product_type = product_type
        # The query start time. Format: YYYY-MM-DD HH:mm:ss, for example, 2025-10-11 21:24:48.
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

        if self.product_type is not None:
            result['ProductType'] = self.product_type

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

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

