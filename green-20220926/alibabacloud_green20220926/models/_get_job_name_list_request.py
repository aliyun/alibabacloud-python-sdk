# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class GetJobNameListRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        query: str = None,
        region_id: str = None,
        sort: Dict[str, str] = None,
        start_date: str = None,
    ):
        # End date.
        self.end_date = end_date
        # Query condition.
        self.query = query
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
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.query is not None:
            result['Query'] = self.query

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sort is not None:
            result['Sort'] = self.sort

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
            self.sort = m.get('Sort')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

