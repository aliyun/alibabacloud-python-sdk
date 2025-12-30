# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeRecordResolveStatisticsSummaryResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        statistics: List[main_models.DescribeRecordResolveStatisticsSummaryResponseBodyStatistics] = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 500**. Default value: **20**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The statistics.
        self.statistics = statistics
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of pages returned.
        self.total_pages = total_pages

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Statistics'] = []
        if self.statistics is not None:
            for k1 in self.statistics:
                result['Statistics'].append(k1.to_map() if k1 else None)

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

        self.statistics = []
        if m.get('Statistics') is not None:
            for k1 in m.get('Statistics'):
                temp_model = main_models.DescribeRecordResolveStatisticsSummaryResponseBodyStatistics()
                self.statistics.append(temp_model.from_map(k1))

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeRecordResolveStatisticsSummaryResponseBodyStatistics(DaraModel):
    def __init__(
        self,
        count: str = None,
        domain_name: str = None,
        domain_type: str = None,
        sub_domain: str = None,
    ):
        # The number of DNS requests.
        self.count = count
        # The subdomain name.
        self.domain_name = domain_name
        # The type of the domain name. The parameter value is not case-sensitive. Valid values:
        # 
        # *   PUBLIC (default): hosted public domain name
        # *   CACHE: cache-accelerated domain name
        self.domain_type = domain_type
        # The subdomain.
        self.sub_domain = sub_domain

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

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        return self

