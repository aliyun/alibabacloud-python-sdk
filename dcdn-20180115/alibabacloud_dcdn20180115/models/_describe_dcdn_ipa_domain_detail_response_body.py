# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnIpaDomainDetailResponseBody(DaraModel):
    def __init__(
        self,
        domain_detail: main_models.DescribeDcdnIpaDomainDetailResponseBodyDomainDetail = None,
        request_id: str = None,
    ):
        # The details about the accelerated domain name.
        self.domain_detail = domain_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain_detail:
            self.domain_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_detail is not None:
            result['DomainDetail'] = self.domain_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainDetail') is not None:
            temp_model = main_models.DescribeDcdnIpaDomainDetailResponseBodyDomainDetail()
            self.domain_detail = temp_model.from_map(m.get('DomainDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnIpaDomainDetailResponseBodyDomainDetail(DaraModel):
    def __init__(
        self,
        cert_name: str = None,
        cname: str = None,
        description: str = None,
        domain_name: str = None,
        domain_status: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        resource_group_id: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        scope: str = None,
        sources: main_models.DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSources = None,
    ):
        # Indicates the name of the certificate if the HTTPS protocol is enabled.
        self.cert_name = cert_name
        # The CNAME assigned to the domain name.
        self.cname = cname
        # The description.
        self.description = description
        # The accelerated domain names.
        self.domain_name = domain_name
        # The status of the accelerated domain name. Valid values:
        # 
        # *   **online**: enabled
        # *   **offline**: disabled
        # *   **configuring**: configuring
        # *   **configure_failed**: configuration failed
        # *   **checking**: reviewing
        # *   **check_failed:** review failed
        self.domain_status = domain_status
        # The creation time.
        self.gmt_created = gmt_created
        # The time when the domain name was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Indicates whether the Security Socket Layer (SSL) certificate is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**.
        self.sslprotocol = sslprotocol
        # The public key of the certificate if HTTPS is enabled.
        self.sslpub = sslpub
        # The acceleration region. Valid values:
        # 
        # *   domestic: Chinese mainland
        # *   overseas: outside the Chinese mainland
        # *   global: global
        self.scope = scope
        # The information about the origin server.
        self.sources = sources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_name is not None:
            result['CertName'] = self.cert_name

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol

        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.sources is not None:
            result['Sources'] = self.sources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')

        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Sources') is not None:
            temp_model = main_models.DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSources()
            self.sources = temp_model.from_map(m.get('Sources'))

        return self

class DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSources(DaraModel):
    def __init__(
        self,
        source: List[main_models.DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSourcesSource] = None,
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
                temp_model = main_models.DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSourcesSource()
                self.source.append(temp_model.from_map(k1))

        return self

class DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSourcesSource(DaraModel):
    def __init__(
        self,
        content: str = None,
        enabled: str = None,
        port: int = None,
        priority: str = None,
        type: str = None,
        weight: str = None,
    ):
        # The address of the origin server.
        self.content = content
        # The status.
        self.enabled = enabled
        # The custom port. Valid values: **0** to **65535**.
        self.port = port
        # The priority.
        self.priority = priority
        # The type of the origin server. Valid values:
        # 
        # *   **ipaddr**: an origin IP address
        # *   **domain**: a domain name.
        # *   **oss**: Object Storage Service (OSS) buckets are not supported.
        self.type = type
        # The weight of the origin server if multiple origin servers have been specified.
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

        if self.enabled is not None:
            result['Enabled'] = self.enabled

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

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

