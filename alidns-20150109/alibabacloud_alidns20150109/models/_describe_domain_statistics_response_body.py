# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        statistics: main_models.DescribeDomainStatisticsResponseBodyStatistics = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The statistics on the Domain Name System (DNS) requests.
        self.statistics = statistics

    def validate(self):
        if self.statistics:
            self.statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Statistics') is not None:
            temp_model = main_models.DescribeDomainStatisticsResponseBodyStatistics()
            self.statistics = temp_model.from_map(m.get('Statistics'))

        return self

class DescribeDomainStatisticsResponseBodyStatistics(DaraModel):
    def __init__(
        self,
        statistic: List[main_models.DescribeDomainStatisticsResponseBodyStatisticsStatistic] = None,
    ):
        self.statistic = statistic

    def validate(self):
        if self.statistic:
            for v1 in self.statistic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Statistic'] = []
        if self.statistic is not None:
            for k1 in self.statistic:
                result['Statistic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.statistic = []
        if m.get('Statistic') is not None:
            for k1 in m.get('Statistic'):
                temp_model = main_models.DescribeDomainStatisticsResponseBodyStatisticsStatistic()
                self.statistic.append(temp_model.from_map(k1))

        return self

class DescribeDomainStatisticsResponseBodyStatisticsStatistic(DaraModel):
    def __init__(
        self,
        count: int = None,
        domain_name: str = None,
        timestamp: int = None,
    ):
        # The number of DNS requests.
        self.count = count
        # The domain name.
        self.domain_name = domain_name
        # The statistical timestamp. Unit: milliseconds. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

