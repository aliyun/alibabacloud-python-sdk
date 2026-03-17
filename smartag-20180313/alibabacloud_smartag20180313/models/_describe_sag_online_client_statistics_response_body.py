# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagOnlineClientStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sag_statistics: main_models.DescribeSagOnlineClientStatisticsResponseBodySagStatistics = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        self.sag_statistics = sag_statistics

    def validate(self):
        if self.sag_statistics:
            self.sag_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sag_statistics is not None:
            result['SagStatistics'] = self.sag_statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SagStatistics') is not None:
            temp_model = main_models.DescribeSagOnlineClientStatisticsResponseBodySagStatistics()
            self.sag_statistics = temp_model.from_map(m.get('SagStatistics'))

        return self

class DescribeSagOnlineClientStatisticsResponseBodySagStatistics(DaraModel):
    def __init__(
        self,
        statistics: List[main_models.DescribeSagOnlineClientStatisticsResponseBodySagStatisticsStatistics] = None,
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
                temp_model = main_models.DescribeSagOnlineClientStatisticsResponseBodySagStatisticsStatistics()
                self.statistics.append(temp_model.from_map(k1))

        return self

class DescribeSagOnlineClientStatisticsResponseBodySagStatisticsStatistics(DaraModel):
    def __init__(
        self,
        online_count: str = None,
        smart_agid: str = None,
    ):
        self.online_count = online_count
        self.smart_agid = smart_agid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        return self

