# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeUserOnlineClientStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_statistics: main_models.DescribeUserOnlineClientStatisticsResponseBodyUserStatistics = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        self.user_statistics = user_statistics

    def validate(self):
        if self.user_statistics:
            self.user_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_statistics is not None:
            result['UserStatistics'] = self.user_statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserStatistics') is not None:
            temp_model = main_models.DescribeUserOnlineClientStatisticsResponseBodyUserStatistics()
            self.user_statistics = temp_model.from_map(m.get('UserStatistics'))

        return self

class DescribeUserOnlineClientStatisticsResponseBodyUserStatistics(DaraModel):
    def __init__(
        self,
        statistics: List[main_models.DescribeUserOnlineClientStatisticsResponseBodyUserStatisticsStatistics] = None,
    ):
        self.statistics = statistics

    def validate(self):
        if self.statistics:
            for v1 in self.statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Statistics'] = []
        if self.statistics is not None:
            for k1 in self.statistics:
                result['Statistics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.statistics = []
        if m.get('Statistics') is not None:
            for k1 in m.get('Statistics'):
                temp_model = main_models.DescribeUserOnlineClientStatisticsResponseBodyUserStatisticsStatistics()
                self.statistics.append(temp_model.from_map(k1))

        return self

class DescribeUserOnlineClientStatisticsResponseBodyUserStatisticsStatistics(DaraModel):
    def __init__(
        self,
        online_count: str = None,
        user_name: str = None,
    ):
        self.online_count = online_count
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

