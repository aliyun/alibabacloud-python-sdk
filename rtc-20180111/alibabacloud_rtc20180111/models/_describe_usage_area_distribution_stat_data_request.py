# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUsageAreaDistributionStatDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: str = None,
        parent_area: str = None,
        start_date: str = None,
    ):
        # APP ID
        # 
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.end_date = end_date
        self.parent_area = parent_area
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.parent_area is not None:
            result['ParentArea'] = self.parent_area

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ParentArea') is not None:
            self.parent_area = m.get('ParentArea')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

