# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOssCheckStatRequest(DaraModel):
    def __init__(
        self,
        by_month: bool = None,
        end_date: str = None,
        parent_task_id: str = None,
        region_id: str = None,
        start_date: str = None,
    ):
        # Whether to query by month.
        self.by_month = by_month
        # End date.
        self.end_date = end_date
        # Parent task ID.
        self.parent_task_id = parent_task_id
        # Region ID.
        self.region_id = region_id
        # Start date.
        self.start_date = start_date

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

        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByMonth') is not None:
            self.by_month = m.get('ByMonth')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

