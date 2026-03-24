# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domains: List[main_models.DescribeDomainsResponseBodyDomains] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of domain names.
        self.domains = domains
        # The request ID.
        self.request_id = request_id
        # The total number of domain name configurations returned.
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
                temp_model = main_models.DescribeDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDomainsResponseBodyDomains(DaraModel):
    def __init__(
        self,
        backeds: main_models.DescribeDomainsResponseBodyDomainsBackeds = None,
        cname: str = None,
        domain: str = None,
        domain_id: str = None,
        listen_ports: main_models.DescribeDomainsResponseBodyDomainsListenPorts = None,
        resource_manager_resource_group_id: str = None,
        status: int = None,
    ):
        # The back-to-origin configuration.
        self.backeds = backeds
        # The canonical name (CNAME) that is assigned to the domain name by WAF.
        self.cname = cname
        # The domain name that is added to WAF.
        self.domain = domain
        # The ID of the domain name.
        self.domain_id = domain_id
        # The listener configuration.
        self.listen_ports = listen_ports
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The status of the domain name. Valid values:
        # 
        # - **1**: The domain name is in a normal state.
        # 
        # - **2**: The domain name is being created.
        # 
        # - **3**: The domain name is being modified.
        # 
        # - **4**: The domain name is being released.
        # 
        # - **5**: Forwarding is disabled for the domain name.
        self.status = status

    def validate(self):
        if self.backeds:
            self.backeds.validate()
        if self.listen_ports:
            self.listen_ports.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backeds is not None:
            result['Backeds'] = self.backeds.to_map()

        if self.cname is not None:
            result['Cname'] = self.cname

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.listen_ports is not None:
            result['ListenPorts'] = self.listen_ports.to_map()

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Backeds') is not None:
            temp_model = main_models.DescribeDomainsResponseBodyDomainsBackeds()
            self.backeds = temp_model.from_map(m.get('Backeds'))

        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('ListenPorts') is not None:
            temp_model = main_models.DescribeDomainsResponseBodyDomainsListenPorts()
            self.listen_ports = temp_model.from_map(m.get('ListenPorts'))

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDomainsResponseBodyDomainsListenPorts(DaraModel):
    def __init__(
        self,
        http: List[int] = None,
        https: List[int] = None,
    ):
        # The list of listening ports for the HTTP protocol.
        self.http = http
        # The list of listening ports for the HTTPS protocol.
        self.https = https

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http is not None:
            result['Http'] = self.http

        if self.https is not None:
            result['Https'] = self.https

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Http') is not None:
            self.http = m.get('Http')

        if m.get('Https') is not None:
            self.https = m.get('Https')

        return self

class DescribeDomainsResponseBodyDomainsBackeds(DaraModel):
    def __init__(
        self,
        http: List[main_models.DescribeDomainsResponseBodyDomainsBackedsHttp] = None,
        https: List[main_models.DescribeDomainsResponseBodyDomainsBackedsHttps] = None,
    ):
        # The list of origin addresses for the HTTP protocol.
        self.http = http
        # The list of origin addresses for the HTTPS protocol.
        self.https = https

    def validate(self):
        if self.http:
            for v1 in self.http:
                 if v1:
                    v1.validate()
        if self.https:
            for v1 in self.https:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Http'] = []
        if self.http is not None:
            for k1 in self.http:
                result['Http'].append(k1.to_map() if k1 else None)

        result['Https'] = []
        if self.https is not None:
            for k1 in self.https:
                result['Https'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.http = []
        if m.get('Http') is not None:
            for k1 in m.get('Http'):
                temp_model = main_models.DescribeDomainsResponseBodyDomainsBackedsHttp()
                self.http.append(temp_model.from_map(k1))

        self.https = []
        if m.get('Https') is not None:
            for k1 in m.get('Https'):
                temp_model = main_models.DescribeDomainsResponseBodyDomainsBackedsHttps()
                self.https.append(temp_model.from_map(k1))

        return self

class DescribeDomainsResponseBodyDomainsBackedsHttps(DaraModel):
    def __init__(
        self,
        backend: str = None,
    ):
        # The origin address for the HTTPS protocol.
        self.backend = backend

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend is not None:
            result['Backend'] = self.backend

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Backend') is not None:
            self.backend = m.get('Backend')

        return self

class DescribeDomainsResponseBodyDomainsBackedsHttp(DaraModel):
    def __init__(
        self,
        backend: str = None,
    ):
        # The origin address for the HTTP protocol.
        self.backend = backend

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend is not None:
            result['Backend'] = self.backend

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Backend') is not None:
            self.backend = m.get('Backend')

        return self

