# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainListResponseBody(DaraModel):
    def __init__(
        self,
        domain_list_response_list: List[main_models.DescribeDomainListResponseBodyDomainListResponseList] = None,
        page_info: main_models.DescribeDomainListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The list of domain name asset information.
        self.domain_list_response_list = domain_list_response_list
        # The pagination information of the query result.
        self.page_info = page_info
        # The ID of the request. The ID is a unique identifier that Alibaba Cloud generates for the request and can be used to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.domain_list_response_list:
            for v1 in self.domain_list_response_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainListResponseList'] = []
        if self.domain_list_response_list is not None:
            for k1 in self.domain_list_response_list:
                result['DomainListResponseList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_list_response_list = []
        if m.get('DomainListResponseList') is not None:
            for k1 in m.get('DomainListResponseList'):
                temp_model = main_models.DescribeDomainListResponseBodyDomainListResponseList()
                self.domain_list_response_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeDomainListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainListResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of domain names displayed on the current page in a paged query.
        self.count = count
        # The page number of the current page in a paged query.
        self.current_page = current_page
        # The number of domain names displayed on each page in a paged query. Default value: **10**, which indicates that 10 domain names are displayed on each page.
        self.page_size = page_size
        # The total number of domain names returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDomainListResponseBodyDomainListResponseList(DaraModel):
    def __init__(
        self,
        domain: str = None,
        ip_list: str = None,
    ):
        # The domain name or website name.
        self.domain = domain
        # The IP address information associated with the domain name.
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        return self

