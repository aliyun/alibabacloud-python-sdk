# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryEndUserHistoryUsageRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        is_ad_user: bool = None,
        page_num: int = None,
        page_size: int = None,
        start_date: str = None,
    ):
        # The end date of the query. Format: yyyy-MM-dd. The date cannot be later than yesterday or earlier than StartDate. Default value: yesterday.
        self.end_date = end_date
        # Specifies whether to query Active Directory (AD) domain users. If this parameter is set to true, AD domain users are queried. If this parameter is set to false or not specified, convenience account users are queried.
        self.is_ad_user = is_ad_user
        # The page number. Minimum value: 1. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Valid values: 1 to 100. Default value: 100.
        self.page_size = page_size
        # The start date of the query. Format: yyyy-MM-dd. The date cannot be earlier than 32 days ago. Default value: yesterday.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.is_ad_user is not None:
            result['IsAdUser'] = self.is_ad_user

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('IsAdUser') is not None:
            self.is_ad_user = m.get('IsAdUser')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

