# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDohSubDomainStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        statistics: List[main_models.DescribeDohSubDomainStatisticsResponseBodyStatistics] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The statistics list.
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Statistics'] = []
        if self.statistics is not None:
            for k1 in self.statistics:
                result['Statistics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.statistics = []
        if m.get('Statistics') is not None:
            for k1 in m.get('Statistics'):
                temp_model = main_models.DescribeDohSubDomainStatisticsResponseBodyStatistics()
                self.statistics.append(temp_model.from_map(k1))

        return self

class DescribeDohSubDomainStatisticsResponseBodyStatistics(DaraModel):
    def __init__(
        self,
        timestamp: int = None,
        total_count: int = None,
        v_4http_count: int = None,
        v_4https_count: int = None,
        v_6http_count: int = None,
        v_6https_count: int = None,
    ):
        # The timestamp.
        self.timestamp = timestamp
        # The total number of requests.
        self.total_count = total_count
        # The number of IPv4-based HTTP requests.
        self.v_4http_count = v_4http_count
        # The number of IPv4-based HTTPS requests.
        self.v_4https_count = v_4https_count
        # The number of IPv6-based HTTP requests.
        self.v_6http_count = v_6http_count
        # The number of IPv6-based HTTPS requests.
        self.v_6https_count = v_6https_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.v_4http_count is not None:
            result['V4HttpCount'] = self.v_4http_count

        if self.v_4https_count is not None:
            result['V4HttpsCount'] = self.v_4https_count

        if self.v_6http_count is not None:
            result['V6HttpCount'] = self.v_6http_count

        if self.v_6https_count is not None:
            result['V6HttpsCount'] = self.v_6https_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('V4HttpCount') is not None:
            self.v_4http_count = m.get('V4HttpCount')

        if m.get('V4HttpsCount') is not None:
            self.v_4https_count = m.get('V4HttpsCount')

        if m.get('V6HttpCount') is not None:
            self.v_6http_count = m.get('V6HttpCount')

        if m.get('V6HttpsCount') is not None:
            self.v_6https_count = m.get('V6HttpsCount')

        return self

