# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOssV2ResultRequest(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        risk_level: str = None,
        start_date: str = None,
        task_name: str = None,
    ):
        self.bucket = bucket
        self.current_page = current_page
        self.end_date = end_date
        self.page_size = page_size
        self.risk_level = risk_level
        self.start_date = start_date
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

