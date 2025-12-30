# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDNSSLBSubDomainsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        slb_sub_domains: main_models.DescribeDNSSLBSubDomainsResponseBodySlbSubDomains = None,
        total_count: int = None,
    ):
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **20**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The subdomains for which weighted round-robin is enabled.
        self.slb_sub_domains = slb_sub_domains
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.slb_sub_domains:
            self.slb_sub_domains.validate()

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

        if self.slb_sub_domains is not None:
            result['SlbSubDomains'] = self.slb_sub_domains.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlbSubDomains') is not None:
            temp_model = main_models.DescribeDNSSLBSubDomainsResponseBodySlbSubDomains()
            self.slb_sub_domains = temp_model.from_map(m.get('SlbSubDomains'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDNSSLBSubDomainsResponseBodySlbSubDomains(DaraModel):
    def __init__(
        self,
        slb_sub_domain: List[main_models.DescribeDNSSLBSubDomainsResponseBodySlbSubDomainsSlbSubDomain] = None,
    ):
        self.slb_sub_domain = slb_sub_domain

    def validate(self):
        if self.slb_sub_domain:
            for v1 in self.slb_sub_domain:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlbSubDomain'] = []
        if self.slb_sub_domain is not None:
            for k1 in self.slb_sub_domain:
                result['SlbSubDomain'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slb_sub_domain = []
        if m.get('SlbSubDomain') is not None:
            for k1 in m.get('SlbSubDomain'):
                temp_model = main_models.DescribeDNSSLBSubDomainsResponseBodySlbSubDomainsSlbSubDomain()
                self.slb_sub_domain.append(temp_model.from_map(k1))

        return self

class DescribeDNSSLBSubDomainsResponseBodySlbSubDomainsSlbSubDomain(DaraModel):
    def __init__(
        self,
        line_algorithms: main_models.DescribeDNSSLBSubDomainsResponseBodySlbSubDomainsSlbSubDomainLineAlgorithms = None,
        open: bool = None,
        record_count: int = None,
        sub_domain: str = None,
        type: str = None,
    ):
        # The lines for which weighted round-robin is enabled.
        self.line_algorithms = line_algorithms
        # Indicates whether weighted round-robin is enabled for the subdomain.
        self.open = open
        # The number of DNS records added for the subdomain.
        self.record_count = record_count
        # The name of the subdomain.
        self.sub_domain = sub_domain
        # The type of the Domain Name System (DNS) record that supports weighted round-robin. Valid values: A, AAAA, and CNAME.
        self.type = type

    def validate(self):
        if self.line_algorithms:
            self.line_algorithms.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line_algorithms is not None:
            result['LineAlgorithms'] = self.line_algorithms.to_map()

        if self.open is not None:
            result['Open'] = self.open

        if self.record_count is not None:
            result['RecordCount'] = self.record_count

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineAlgorithms') is not None:
            temp_model = main_models.DescribeDNSSLBSubDomainsResponseBodySlbSubDomainsSlbSubDomainLineAlgorithms()
            self.line_algorithms = temp_model.from_map(m.get('LineAlgorithms'))

        if m.get('Open') is not None:
            self.open = m.get('Open')

        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeDNSSLBSubDomainsResponseBodySlbSubDomainsSlbSubDomainLineAlgorithms(DaraModel):
    def __init__(
        self,
        line_algorithm: List[main_models.DescribeDNSSLBSubDomainsResponseBodySlbSubDomainsSlbSubDomainLineAlgorithmsLineAlgorithm] = None,
    ):
        self.line_algorithm = line_algorithm

    def validate(self):
        if self.line_algorithm:
            for v1 in self.line_algorithm:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LineAlgorithm'] = []
        if self.line_algorithm is not None:
            for k1 in self.line_algorithm:
                result['LineAlgorithm'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.line_algorithm = []
        if m.get('LineAlgorithm') is not None:
            for k1 in m.get('LineAlgorithm'):
                temp_model = main_models.DescribeDNSSLBSubDomainsResponseBodySlbSubDomainsSlbSubDomainLineAlgorithmsLineAlgorithm()
                self.line_algorithm.append(temp_model.from_map(k1))

        return self

class DescribeDNSSLBSubDomainsResponseBodySlbSubDomainsSlbSubDomainLineAlgorithmsLineAlgorithm(DaraModel):
    def __init__(
        self,
        line: str = None,
        open: bool = None,
    ):
        # The DNS resolution line. The line can be China Telecom, China Mobile, and China Unicom.
        self.line = line
        # Indicates whether weighted round-robin is enabled for the line. Valid values:
        # 
        # *   **true** (default): Weighted round-robin is enabled.
        # *   **false**: Weighted round-robin is disabled.
        self.open = open

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['Line'] = self.line

        if self.open is not None:
            result['Open'] = self.open

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Open') is not None:
            self.open = m.get('Open')

        return self

