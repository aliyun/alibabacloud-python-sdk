# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetDailyPlayRegionStatisResponseBody(DaraModel):
    def __init__(
        self,
        daily_play_region_statis_list: List[main_models.GetDailyPlayRegionStatisResponseBodyDailyPlayRegionStatisList] = None,
        empty_dates: List[str] = None,
        fail_dates: List[str] = None,
        request_id: str = None,
    ):
        self.daily_play_region_statis_list = daily_play_region_statis_list
        self.empty_dates = empty_dates
        self.fail_dates = fail_dates
        self.request_id = request_id

    def validate(self):
        if self.daily_play_region_statis_list:
            for v1 in self.daily_play_region_statis_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DailyPlayRegionStatisList'] = []
        if self.daily_play_region_statis_list is not None:
            for k1 in self.daily_play_region_statis_list:
                result['DailyPlayRegionStatisList'].append(k1.to_map() if k1 else None)

        if self.empty_dates is not None:
            result['EmptyDates'] = self.empty_dates

        if self.fail_dates is not None:
            result['FailDates'] = self.fail_dates

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.daily_play_region_statis_list = []
        if m.get('DailyPlayRegionStatisList') is not None:
            for k1 in m.get('DailyPlayRegionStatisList'):
                temp_model = main_models.GetDailyPlayRegionStatisResponseBodyDailyPlayRegionStatisList()
                self.daily_play_region_statis_list.append(temp_model.from_map(k1))

        if m.get('EmptyDates') is not None:
            self.empty_dates = m.get('EmptyDates')

        if m.get('FailDates') is not None:
            self.fail_dates = m.get('FailDates')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDailyPlayRegionStatisResponseBodyDailyPlayRegionStatisList(DaraModel):
    def __init__(
        self,
        date: str = None,
        file_url: str = None,
    ):
        self.date = date
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        return self

