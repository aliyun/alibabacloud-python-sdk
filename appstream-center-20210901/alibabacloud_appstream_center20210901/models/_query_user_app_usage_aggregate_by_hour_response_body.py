# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class QueryUserAppUsageAggregateByHourResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        index_data: List[main_models.QueryUserAppUsageAggregateByHourResponseBodyIndexData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The business status code. A value of 200 indicates that the request is successful. Other values indicate that the request failed.
        self.code = code
        # The list of hourly aggregated user application usage data. A maximum of five records are returned for each hour.
        self.index_data = index_data
        # The description of the request processing result. A value of success is usually returned when the request is successful.
        self.message = message
        # The unique identifier of the request, which can be used to troubleshoot request issues.
        self.request_id = request_id

    def validate(self):
        if self.index_data:
            for v1 in self.index_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['IndexData'] = []
        if self.index_data is not None:
            for k1 in self.index_data:
                result['IndexData'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.index_data = []
        if m.get('IndexData') is not None:
            for k1 in m.get('IndexData'):
                temp_model = main_models.QueryUserAppUsageAggregateByHourResponseBodyIndexData()
                self.index_data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryUserAppUsageAggregateByHourResponseBodyIndexData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_time_cnt: str = None,
        hh: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The cumulative usage duration of the application within the statistical range. Unit: seconds.
        self.app_time_cnt = app_time_cnt
        # The statistical hour in a two-digit 24-hour format string. Valid values: 00 to 23. Hour boundaries are divided based on the Asia/Shanghai (UTC+8) time zone.
        self.hh = hh

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_time_cnt is not None:
            result['AppTimeCnt'] = self.app_time_cnt

        if self.hh is not None:
            result['Hh'] = self.hh

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppTimeCnt') is not None:
            self.app_time_cnt = m.get('AppTimeCnt')

        if m.get('Hh') is not None:
            self.hh = m.get('Hh')

        return self

