# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainStatisticsSummaryResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        statistics: main_models.DescribeDomainStatisticsSummaryResponseBodyStatistics = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The statistics on the Domain Name System (DNS) requests.
        self.statistics = statistics
        # The total number of data records.
        self.total_items = total_items
        # The total number of returned pages.
        self.total_pages = total_pages

    def validate(self):
        if self.statistics:
            self.statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Statistics') is not None:
            temp_model = main_models.DescribeDomainStatisticsSummaryResponseBodyStatistics()
            self.statistics = temp_model.from_map(m.get('Statistics'))

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeDomainStatisticsSummaryResponseBodyStatistics(DaraModel):
    def __init__(
        self,
        statistic: List[main_models.DescribeDomainStatisticsSummaryResponseBodyStatisticsStatistic] = None,
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
                temp_model = main_models.DescribeDomainStatisticsSummaryResponseBodyStatisticsStatistic()
                self.statistic.append(temp_model.from_map(k1))

        return self

class DescribeDomainStatisticsSummaryResponseBodyStatisticsStatistic(DaraModel):
    def __init__(
        self,
        count: int = None,
        domain_name: str = None,
        domain_type: str = None,
        resolve_analysis_status: str = None,
    ):
        # The number of DNS requests.
        self.count = count
        # The domain name.
        self.domain_name = domain_name
        # The type of the domain name. The parameter value is not case-sensitive. Valid values:
        # 
        # PUBLIC (default): hosted public domain name
        # 
        # CACHE: cache-accelerated domain name
        self.domain_type = domain_type
        # Indicates whether the DNS traffic analysis feature is enabled for the domain name. Valid values:
        # 
        # *   OPEN
        # *   CLOSE
        self.resolve_analysis_status = resolve_analysis_status

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

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.resolve_analysis_status is not None:
            result['resolveAnalysisStatus'] = self.resolve_analysis_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('resolveAnalysisStatus') is not None:
            self.resolve_analysis_status = m.get('resolveAnalysisStatus')

        return self

