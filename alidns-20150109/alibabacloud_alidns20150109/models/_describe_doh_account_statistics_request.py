# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDohAccountStatisticsRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        lang: str = None,
        start_date: str = None,
    ):
        # The end of the time range to query. Specify the time in the YYYY-MM-DD format.
        # 
        # The default value is the day when you perform the operation.
        self.end_date = end_date
        # The language type.
        self.lang = lang
        # The beginning of the time range to query. Specify the time in the YYYY-MM-DD format.
        # 
        # You can query only the DNS records of the latest 90 days.`The value of StartDate must be greater than or equal to the difference between the current date and 90`.
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

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

