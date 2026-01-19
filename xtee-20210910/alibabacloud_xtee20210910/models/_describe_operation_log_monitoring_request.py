# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOperationLogMonitoringRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        end_date: str = None,
        reg_id: str = None,
        start_date: str = None,
        user_name_search: str = None,
    ):
        # Language type of the returned message. Values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # End date (in yyyy-MM-dd format, and the interval from the start date cannot exceed 90 days)
        self.end_date = end_date
        # Region code.
        self.reg_id = reg_id
        # Start date (in yyyy-MM-dd format, and the interval from the current date cannot exceed 90 days)
        self.start_date = start_date
        # Operator.
        self.user_name_search = user_name_search

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.start_date is not None:
            result['startDate'] = self.start_date

        if self.user_name_search is not None:
            result['userNameSearch'] = self.user_name_search

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        if m.get('userNameSearch') is not None:
            self.user_name_search = m.get('userNameSearch')

        return self

