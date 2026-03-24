# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainsBySourceResponseBody(DaraModel):
    def __init__(
        self,
        domains_list: main_models.DescribeDomainsBySourceResponseBodyDomainsList = None,
        request_id: str = None,
        sources: str = None,
    ):
        self.domains_list = domains_list
        # The ID of the request.
        self.request_id = request_id
        # The origin servers.
        self.sources = sources

    def validate(self):
        if self.domains_list:
            self.domains_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domains_list is not None:
            result['DomainsList'] = self.domains_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sources is not None:
            result['Sources'] = self.sources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainsList') is not None:
            temp_model = main_models.DescribeDomainsBySourceResponseBodyDomainsList()
            self.domains_list = temp_model.from_map(m.get('DomainsList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Sources') is not None:
            self.sources = m.get('Sources')

        return self

class DescribeDomainsBySourceResponseBodyDomainsList(DaraModel):
    def __init__(
        self,
        domains_data: List[main_models.DescribeDomainsBySourceResponseBodyDomainsListDomainsData] = None,
    ):
        self.domains_data = domains_data

    def validate(self):
        if self.domains_data:
            for v1 in self.domains_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainsData'] = []
        if self.domains_data is not None:
            for k1 in self.domains_data:
                result['DomainsData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains_data = []
        if m.get('DomainsData') is not None:
            for k1 in m.get('DomainsData'):
                temp_model = main_models.DescribeDomainsBySourceResponseBodyDomainsListDomainsData()
                self.domains_data.append(temp_model.from_map(k1))

        return self

class DescribeDomainsBySourceResponseBodyDomainsListDomainsData(DaraModel):
    def __init__(
        self,
        domain_infos: main_models.DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos = None,
        domains: main_models.DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains = None,
        source: str = None,
    ):
        self.domain_infos = domain_infos
        self.domains = domains
        self.source = source

    def validate(self):
        if self.domain_infos:
            self.domain_infos.validate()
        if self.domains:
            self.domains.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_infos is not None:
            result['DomainInfos'] = self.domain_infos.to_map()

        if self.domains is not None:
            result['Domains'] = self.domains.to_map()

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainInfos') is not None:
            temp_model = main_models.DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos()
            self.domain_infos = temp_model.from_map(m.get('DomainInfos'))

        if m.get('Domains') is not None:
            temp_model = main_models.DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains()
            self.domains = temp_model.from_map(m.get('Domains'))

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

class DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains(DaraModel):
    def __init__(
        self,
        domain_names: List[str] = None,
    ):
        self.domain_names = domain_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names is not None:
            result['domainNames'] = self.domain_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainNames') is not None:
            self.domain_names = m.get('domainNames')

        return self

class DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos(DaraModel):
    def __init__(
        self,
        domain_info: List[main_models.DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo] = None,
    ):
        self.domain_info = domain_info

    def validate(self):
        if self.domain_info:
            for v1 in self.domain_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['domainInfo'] = []
        if self.domain_info is not None:
            for k1 in self.domain_info:
                result['domainInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_info = []
        if m.get('domainInfo') is not None:
            for k1 in m.get('domainInfo'):
                temp_model = main_models.DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo()
                self.domain_info.append(temp_model.from_map(k1))

        return self

class DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo(DaraModel):
    def __init__(
        self,
        cdn_type: str = None,
        create_time: str = None,
        domain_cname: str = None,
        domain_name: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.cdn_type = cdn_type
        self.create_time = create_time
        self.domain_cname = domain_cname
        self.domain_name = domain_name
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_cname is not None:
            result['DomainCname'] = self.domain_cname

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainCname') is not None:
            self.domain_cname = m.get('DomainCname')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

