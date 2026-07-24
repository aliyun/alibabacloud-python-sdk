# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobNameListShrinkRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        query: str = None,
        region_id: str = None,
        sort_shrink: str = None,
        start_date: str = None,
    ):
        # The end time. Format: `YYYY-MM-DD HH:mm:ss`.
        self.end_date = end_date
        # The query condition.
        self.query = query
        # The region ID.
        self.region_id = region_id
        # The sort field.
        self.sort_shrink = sort_shrink
        # The start time. Format: `YYYY-MM-DD HH:mm:ss`.
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

        if self.query is not None:
            result['Query'] = self.query

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

