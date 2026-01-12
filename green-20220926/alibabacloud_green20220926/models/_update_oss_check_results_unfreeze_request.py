# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOssCheckResultsUnfreezeRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        freeze_items: str = None,
        region_id: str = None,
        start_date: str = None,
        task_id: str = None,
    ):
        self.end_date = end_date
        self.freeze_items = freeze_items
        self.region_id = region_id
        self.start_date = start_date
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.freeze_items is not None:
            result['FreezeItems'] = self.freeze_items

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('FreezeItems') is not None:
            self.freeze_items = m.get('FreezeItems')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

