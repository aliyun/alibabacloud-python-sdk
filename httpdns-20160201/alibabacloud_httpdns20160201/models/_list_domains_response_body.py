# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_httpdns20160201 import models as main_models
from darabonba.model import DaraModel

class ListDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domain_infos: main_models.ListDomainsResponseBodyDomainInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.domain_infos = domain_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.domain_infos:
            self.domain_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_infos is not None:
            result['DomainInfos'] = self.domain_infos.to_map()

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
        if m.get('DomainInfos') is not None:
            temp_model = main_models.ListDomainsResponseBodyDomainInfos()
            self.domain_infos = temp_model.from_map(m.get('DomainInfos'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDomainsResponseBodyDomainInfos(DaraModel):
    def __init__(
        self,
        domain_info: List[main_models.ListDomainsResponseBodyDomainInfosDomainInfo] = None,
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
        result['DomainInfo'] = []
        if self.domain_info is not None:
            for k1 in self.domain_info:
                result['DomainInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_info = []
        if m.get('DomainInfo') is not None:
            for k1 in m.get('DomainInfo'):
                temp_model = main_models.ListDomainsResponseBodyDomainInfosDomainInfo()
                self.domain_info.append(temp_model.from_map(k1))

        return self

class ListDomainsResponseBodyDomainInfosDomainInfo(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        resolve_http_aes: int = None,
        resolve_https_aes: int = None,
        resolved: int = None,
        resolved_6: int = None,
        resolved_doh: int = None,
        resolved_https: int = None,
        resolved_https_6: int = None,
        time_modified: int = None,
    ):
        self.domain_name = domain_name
        self.resolve_http_aes = resolve_http_aes
        self.resolve_https_aes = resolve_https_aes
        self.resolved = resolved
        self.resolved_6 = resolved_6
        self.resolved_doh = resolved_doh
        self.resolved_https = resolved_https
        self.resolved_https_6 = resolved_https_6
        self.time_modified = time_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.resolve_http_aes is not None:
            result['ResolveHttpAes'] = self.resolve_http_aes

        if self.resolve_https_aes is not None:
            result['ResolveHttpsAes'] = self.resolve_https_aes

        if self.resolved is not None:
            result['Resolved'] = self.resolved

        if self.resolved_6 is not None:
            result['Resolved6'] = self.resolved_6

        if self.resolved_doh is not None:
            result['ResolvedDoh'] = self.resolved_doh

        if self.resolved_https is not None:
            result['ResolvedHttps'] = self.resolved_https

        if self.resolved_https_6 is not None:
            result['ResolvedHttps6'] = self.resolved_https_6

        if self.time_modified is not None:
            result['TimeModified'] = self.time_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ResolveHttpAes') is not None:
            self.resolve_http_aes = m.get('ResolveHttpAes')

        if m.get('ResolveHttpsAes') is not None:
            self.resolve_https_aes = m.get('ResolveHttpsAes')

        if m.get('Resolved') is not None:
            self.resolved = m.get('Resolved')

        if m.get('Resolved6') is not None:
            self.resolved_6 = m.get('Resolved6')

        if m.get('ResolvedDoh') is not None:
            self.resolved_doh = m.get('ResolvedDoh')

        if m.get('ResolvedHttps') is not None:
            self.resolved_https = m.get('ResolvedHttps')

        if m.get('ResolvedHttps6') is not None:
            self.resolved_https_6 = m.get('ResolvedHttps6')

        if m.get('TimeModified') is not None:
            self.time_modified = m.get('TimeModified')

        return self

