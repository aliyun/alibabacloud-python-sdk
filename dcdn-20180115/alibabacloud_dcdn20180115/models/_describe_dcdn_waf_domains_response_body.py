# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domains: List[main_models.DescribeDcdnWafDomainsResponseBodyDomains] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The protected domain name.
        self.domains = domains
        # The page number of the returned page, which is the same as the PageNumber parameter in request parameters.
        self.page_number = page_number
        # The number of domain names returned per page, which is the same as the PageSize parameter in request parameters.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of protected domain names.
        self.total_count = total_count

    def validate(self):
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['Domains'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.DescribeDcdnWafDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDcdnWafDomainsResponseBodyDomains(DaraModel):
    def __init__(
        self,
        client_ip_tag: str = None,
        domain_name: str = None,
        policy_count: int = None,
    ):
        # The header of IP address of the client that is connected to the point of presence (POP).
        self.client_ip_tag = client_ip_tag
        # The protected domain name.
        self.domain_name = domain_name
        # The number of protection policies that were configured for the protected domain name.
        self.policy_count = policy_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip_tag is not None:
            result['ClientIpTag'] = self.client_ip_tag

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.policy_count is not None:
            result['PolicyCount'] = self.policy_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIpTag') is not None:
            self.client_ip_tag = m.get('ClientIpTag')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PolicyCount') is not None:
            self.policy_count = m.get('PolicyCount')

        return self

