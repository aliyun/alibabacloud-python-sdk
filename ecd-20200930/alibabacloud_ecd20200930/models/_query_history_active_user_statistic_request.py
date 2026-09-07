# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryHistoryActiveUserStatisticRequest(DaraModel):
    def __init__(
        self,
        biz_type: int = None,
        end_date: str = None,
        office_site_id: str = None,
        period: str = None,
        start_date: str = None,
        user_group_id: str = None,
    ):
        # The business channel type code.
        self.biz_type = biz_type
        # The end date of the query. The date is in the yyyy-MM-dd format. The maximum value is yesterday (N-1 data).
        self.end_date = end_date
        # The workspace ID. If specified, only active users within the specified workspace are counted.
        self.office_site_id = office_site_id
        # The statistical period.
        self.period = period
        # The start date of the query. The date is in the yyyy-MM-dd format. The value cannot be earlier than 6 months ago or later than EndDate.
        self.start_date = start_date
        # The user group ID. If specified, only active users within the specified user group are counted.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.period is not None:
            result['Period'] = self.period

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

