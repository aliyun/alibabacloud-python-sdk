# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryHistoryUsageDurationRankRequest(DaraModel):
    def __init__(
        self,
        biz_type: int = None,
        end_date: str = None,
        limit: int = None,
        next_token: str = None,
        start_date: str = None,
    ):
        # The business type.
        self.biz_type = biz_type
        # The end date of the query in `YYYY-MM-DD` format. You can query data within the last 90 days.
        self.end_date = end_date
        # The number of entries to return. The default value is 5, and the maximum value is 200.
        self.limit = limit
        # The token that is used to retrieve the next page of results. You can obtain this token from the response to the previous request.
        self.next_token = next_token
        # The start date of the query in `YYYY-MM-DD` format. You can query data within the last 90 days.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

