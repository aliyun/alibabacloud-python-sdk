# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeQualityAreaDistributionStatDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        parent_area: str = None,
        start_date: int = None,
    ):
        # The app ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The end time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The name of the parent region. For example, the parent region of Hangzhou is Zhejiang Province, and the parameter is set to China_Zhejiang Province. If this parameter is left empty, the statistics are collected at the country level worldwide, such as China and the United Kingdom.
        self.parent_area = parent_area
        # The start time of the query. The value is a UNIX timestamp in seconds.
        # 
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

