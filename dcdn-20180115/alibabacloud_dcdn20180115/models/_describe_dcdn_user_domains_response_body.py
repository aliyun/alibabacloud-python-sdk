# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnUserDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domains: main_models.DescribeDcdnUserDomainsResponseBodyDomains = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the queried domains.
        self.domains = domains
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()

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
        if m.get('Domains') is not None:
            temp_model = main_models.DescribeDcdnUserDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m.get('Domains'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDcdnUserDomainsResponseBodyDomains(DaraModel):
    def __init__(
        self,
        page_data: List[main_models.DescribeDcdnUserDomainsResponseBodyDomainsPageData] = None,
    ):
        self.page_data = page_data

    def validate(self):
        if self.page_data:
            for v1 in self.page_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PageData'] = []
        if self.page_data is not None:
            for k1 in self.page_data:
                result['PageData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k1 in m.get('PageData'):
                temp_model = main_models.DescribeDcdnUserDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k1))

        return self

class DescribeDcdnUserDomainsResponseBodyDomainsPageData(DaraModel):
    def __init__(
        self,
        cname: str = None,
        description: str = None,
        domain_id: int = None,
        domain_name: str = None,
        domain_status: str = None,
        function_type: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        resource_group_id: str = None,
        sslprotocol: str = None,
        sandbox: str = None,
        scene: str = None,
        sources: main_models.DescribeDcdnUserDomainsResponseBodyDomainsPageDataSources = None,
    ):
        # The CNAME of the domain.
        self.cname = cname
        # The reason why the domain failed the review.
        self.description = description
        # The domain ID.
        self.domain_id = domain_id
        # The domain name.
        self.domain_name = domain_name
        # The domain status.
        # 
        # *   **online**: The domain is active.
        # *   **offline**: The domain is suspended.
        # *   **configuring**: The domain is being configured.
        # *   **configure_failed**: The domain failed to be configured.
        # *   **checking**: The domain is under review.
        # *   **check_failed**: The domain failed the review.
        self.domain_status = domain_status
        # The computing service type. Valid values:
        # 
        # *   **routine**
        # *   **image**
        # *   **cloudFunction**
        self.function_type = function_type
        # The time when the domain was added to DCDN.
        self.gmt_created = gmt_created
        # The time when the domain was modified.
        self.gmt_modified = gmt_modified
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Indicates whether HTTPS was enabled.
        # 
        # *   **on**: enabled.
        # *   **off**: disabled.
        self.sslprotocol = sslprotocol
        # The sandbox status.
        self.sandbox = sandbox
        # The acceleration scenario. Valid values:
        # 
        # *   **apiscene**: accelerates response to API calls.
        # *   **webservicescene**: accelerates content delivery for websites.
        # *   **staticscene**: accelerates the delivery of videos, images, and text.
        # *   **If you leave this parameter empty, no scenarios are supported.
        self.scene = scene
        # The information about the origin servers.
        self.sources = sources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.function_type is not None:
            result['FunctionType'] = self.function_type

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol

        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.sources is not None:
            result['Sources'] = self.sources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')

        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Sources') is not None:
            temp_model = main_models.DescribeDcdnUserDomainsResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m.get('Sources'))

        return self

class DescribeDcdnUserDomainsResponseBodyDomainsPageDataSources(DaraModel):
    def __init__(
        self,
        source: List[main_models.DescribeDcdnUserDomainsResponseBodyDomainsPageDataSourcesSource] = None,
    ):
        self.source = source

    def validate(self):
        if self.source:
            for v1 in self.source:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Source'] = []
        if self.source is not None:
            for k1 in self.source:
                result['Source'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k1 in m.get('Source'):
                temp_model = main_models.DescribeDcdnUserDomainsResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k1))

        return self

class DescribeDcdnUserDomainsResponseBodyDomainsPageDataSourcesSource(DaraModel):
    def __init__(
        self,
        content: str = None,
        port: int = None,
        priority: str = None,
        type: str = None,
        weight: str = None,
    ):
        # The address of the origin server.
        self.content = content
        # The port of the origin server.
        self.port = port
        # The priority of the origin server.
        self.priority = priority
        # The type of the origin server.
        self.type = type
        # The weight of the origin server.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.port is not None:
            result['Port'] = self.port

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.type is not None:
            result['Type'] = self.type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

