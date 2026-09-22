# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAiAppStatsRequest(DaraModel):
    def __init__(
        self,
        by_month: bool = None,
        end_date: str = None,
        query: str = None,
        region_id: str = None,
        start_date: str = None,
        type: str = None,
    ):
        # Specifies whether to aggregate statistics by month. Default value: false.
        self.by_month = by_month
        # The end date of the query. Format: YYYY-MM-DD HH:mm:ss.
        self.end_date = end_date
        # The query condition.
        self.query = query
        # The region ID.
        self.region_id = region_id
        # The start date of the query. Format: YYYY-MM-DD HH:mm:ss.
        self.start_date = start_date
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.by_month is not None:
            result['ByMonth'] = self.by_month

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.query is not None:
            result['Query'] = self.query

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByMonth') is not None:
            self.by_month = m.get('ByMonth')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

