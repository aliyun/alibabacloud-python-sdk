# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class QueryHistoryActiveUserCountResponseBody(DaraModel):
    def __init__(
        self,
        active_user_count: main_models.QueryHistoryActiveUserCountResponseBodyActiveUserCount = None,
        request_id: str = None,
    ):
        self.active_user_count = active_user_count
        self.request_id = request_id

    def validate(self):
        if self.active_user_count:
            self.active_user_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_user_count is not None:
            result['ActiveUserCount'] = self.active_user_count.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveUserCount') is not None:
            temp_model = main_models.QueryHistoryActiveUserCountResponseBodyActiveUserCount()
            self.active_user_count = temp_model.from_map(m.get('ActiveUserCount'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryHistoryActiveUserCountResponseBodyActiveUserCount(DaraModel):
    def __init__(
        self,
        daily_active_user_count: int = None,
        monthly_active_user_count: int = None,
    ):
        self.daily_active_user_count = daily_active_user_count
        self.monthly_active_user_count = monthly_active_user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.daily_active_user_count is not None:
            result['DailyActiveUserCount'] = self.daily_active_user_count

        if self.monthly_active_user_count is not None:
            result['MonthlyActiveUserCount'] = self.monthly_active_user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DailyActiveUserCount') is not None:
            self.daily_active_user_count = m.get('DailyActiveUserCount')

        if m.get('MonthlyActiveUserCount') is not None:
            self.monthly_active_user_count = m.get('MonthlyActiveUserCount')

        return self

