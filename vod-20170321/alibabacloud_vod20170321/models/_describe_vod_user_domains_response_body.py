# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodUserDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domains: main_models.DescribeVodUserDomainsResponseBodyDomains = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The detailed information about each domain name for CDN. The returned information is displayed in the format that is specified by the PageData parameter.
        self.domains = domains
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
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
            temp_model = main_models.DescribeVodUserDomainsResponseBodyDomains()
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

class DescribeVodUserDomainsResponseBodyDomains(DaraModel):
    def __init__(
        self,
        page_data: List[main_models.DescribeVodUserDomainsResponseBodyDomainsPageData] = None,
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
                temp_model = main_models.DescribeVodUserDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k1))

        return self

class DescribeVodUserDomainsResponseBodyDomainsPageData(DaraModel):
    def __init__(
        self,
        cname: str = None,
        description: str = None,
        domain_name: str = None,
        domain_status: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        sandbox: str = None,
        sources: main_models.DescribeVodUserDomainsResponseBodyDomainsPageDataSources = None,
        ssl_protocol: str = None,
    ):
        # The CNAME that is assigned to the domain name for CDN.
        self.cname = cname
        # The remarks.
        self.description = description
        # The domain name for CDN.
        self.domain_name = domain_name
        # The status of the domain name for CDN. Valid values:
        # 
        # *   **online**: indicates that the domain name is enabled.
        # *   **offline**: indicates that the domain name is disabled.
        # *   **configuring**: indicates that the domain name is being configured.
        # *   **configure_failed**: indicates that the domain name failed to be configured.
        # *   **checking**: indicates that the domain name is under review.
        # *   **check_failed**: indicates that the domain name failed the review.
        self.domain_status = domain_status
        # The time when the domain name for CDN was added. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.gmt_created = gmt_created
        # The last time when the domain name for CDN was modified. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # Indicates whether the accelerated domain name was in a sandbox.
        self.sandbox = sandbox
        # The information about the origin server.
        self.sources = sources
        # Indicates whether HTTPS is enabled.
        # 
        # *   **on**: HTTPS is enabled.
        # *   **off**: HTTPS is not eabled.
        self.ssl_protocol = ssl_protocol

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

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox

        if self.sources is not None:
            result['Sources'] = self.sources.to_map()

        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')

        if m.get('Sources') is not None:
            temp_model = main_models.DescribeVodUserDomainsResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m.get('Sources'))

        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')

        return self

class DescribeVodUserDomainsResponseBodyDomainsPageDataSources(DaraModel):
    def __init__(
        self,
        source: List[main_models.DescribeVodUserDomainsResponseBodyDomainsPageDataSourcesSource] = None,
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
                temp_model = main_models.DescribeVodUserDomainsResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k1))

        return self

class DescribeVodUserDomainsResponseBodyDomainsPageDataSourcesSource(DaraModel):
    def __init__(
        self,
        content: str = None,
        port: int = None,
        priority: str = None,
        type: str = None,
    ):
        # The address of the origin server.
        self.content = content
        # The port number. Valid values: **443** and **80**.
        self.port = port
        # The priority of the origin server.
        self.priority = priority
        # The type of the origin server. Valid values:
        # 
        # *   **ipaddr**: an IP address.
        # *   **domain**: an origin domain name
        # *   **oss**: the OSS domain of an Object Storage Service (OSS) bucket
        self.type = type

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

        return self

