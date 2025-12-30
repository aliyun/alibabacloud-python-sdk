# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDohSubDomainStatisticsSummaryResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        statistics: List[main_models.DescribeDohSubDomainStatisticsSummaryResponseBodyStatistics] = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The statistics list.
        self.statistics = statistics
        # Total number of entries returned.
        self.total_items = total_items
        # Total number of pages returned.
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
                temp_model = main_models.DescribeDohSubDomainStatisticsSummaryResponseBodyStatistics()
                self.statistics.append(temp_model.from_map(k1))

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeDohSubDomainStatisticsSummaryResponseBodyStatistics(DaraModel):
    def __init__(
        self,
        http_count: int = None,
        https_count: int = None,
        ip_count: int = None,
        sub_domain: str = None,
        total_count: int = None,
        v_4http_count: int = None,
        v_4https_count: int = None,
        v_6http_count: int = None,
        v_6https_count: int = None,
    ):
        # The number of HTTP requests.
        self.http_count = http_count
        # The number of HTTPS requests.
        self.https_count = https_count
        # The number of IP addresses.
        self.ip_count = ip_count
        # The subdomain.
        self.sub_domain = sub_domain
        # Total number of requests.
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
        if self.http_count is not None:
            result['HttpCount'] = self.http_count

        if self.https_count is not None:
            result['HttpsCount'] = self.https_count

        if self.ip_count is not None:
            result['IpCount'] = self.ip_count

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

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
        if m.get('HttpCount') is not None:
            self.http_count = m.get('HttpCount')

        if m.get('HttpsCount') is not None:
            self.https_count = m.get('HttpsCount')

        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

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

