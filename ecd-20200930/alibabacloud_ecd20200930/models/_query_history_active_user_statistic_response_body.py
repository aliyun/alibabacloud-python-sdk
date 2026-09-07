# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class QueryHistoryActiveUserStatisticResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        user_statistic_list: List[main_models.QueryHistoryActiveUserStatisticResponseBodyUserStatisticList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count
        # The list of daily active user statistics.
        self.user_statistic_list = user_statistic_list

    def validate(self):
        if self.user_statistic_list:
            for v1 in self.user_statistic_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UserStatisticList'] = []
        if self.user_statistic_list is not None:
            for k1 in self.user_statistic_list:
                result['UserStatisticList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.user_statistic_list = []
        if m.get('UserStatisticList') is not None:
            for k1 in m.get('UserStatisticList'):
                temp_model = main_models.QueryHistoryActiveUserStatisticResponseBodyUserStatisticList()
                self.user_statistic_list.append(temp_model.from_map(k1))

        return self

class QueryHistoryActiveUserStatisticResponseBodyUserStatisticList(DaraModel):
    def __init__(
        self,
        active_user_count: int = None,
        format_date: str = None,
        time_stamp: int = None,
    ):
        # The number of deduplicated active users on the day.
        self.active_user_count = active_user_count
        # The date in the standard yyyy-MM-dd format, in the UTC+8 time zone.
        self.format_date = format_date
        # The timestamp of the date, in milliseconds.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_user_count is not None:
            result['ActiveUserCount'] = self.active_user_count

        if self.format_date is not None:
            result['FormatDate'] = self.format_date

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveUserCount') is not None:
            self.active_user_count = m.get('ActiveUserCount')

        if m.get('FormatDate') is not None:
            self.format_date = m.get('FormatDate')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

