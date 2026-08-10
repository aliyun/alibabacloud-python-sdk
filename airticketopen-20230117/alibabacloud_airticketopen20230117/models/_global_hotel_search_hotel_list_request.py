# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GlobalHotelSearchHotelListRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        city_code: str = None,
        page_no: int = None,
        page_size: int = None,
        tracer_id: str = None,
    ):
        # The distributor account ID.
        # 
        # This parameter is required.
        self.account_no = account_no
        # The city code.
        # 
        # This parameter is required.
        self.city_code = city_code
        # The page number. Pages start from 1.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # traceId
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.city_code is not None:
            result['CityCode'] = self.city_code

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

