# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainDetailResponseBody(DaraModel):
    def __init__(
        self,
        domain_detail: main_models.DescribeDcdnDomainDetailResponseBodyDomainDetail = None,
        request_id: str = None,
    ):
        # The information about the accelerated domain name.
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
            temp_model = main_models.DescribeDcdnDomainDetailResponseBodyDomainDetail()
            self.domain_detail = temp_model.from_map(m.get('DomainDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnDomainDetailResponseBodyDomainDetail(DaraModel):
    def __init__(
        self,
        cname: str = None,
        description: str = None,
        domain_name: str = None,
        domain_status: str = None,
        function_type: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        resource_group_id: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        scene: str = None,
        scope: str = None,
        sources: main_models.DescribeDcdnDomainDetailResponseBodyDomainDetailSources = None,
    ):
        # The CNAME that is assigned to the accelerated domain name. You must add the CNAME record to the system of your Domain Name System (DNS) provider to map the accelerated domain name to the CNAME.
        self.cname = cname
        # The information about the Internet content provider (ICP) filing of the domain name.
        self.description = description
        # The accelerated domain name.
        self.domain_name = domain_name
        # The status of the accelerated domain name. Valid values:
        # 
        # *   **online**
        # *   **offline**
        # *   **configuring**
        # *   **configure_failed**
        # *   **checking**
        # *   **check_failed**
        self.domain_status = domain_status
        # Computing service type. Valid values:
        # 
        # *   **routine**
        # *   **image**
        # *   **cloudFunction**
        self.function_type = function_type
        # The time when the domain name was added.
        self.gmt_created = gmt_created
        # The time when the domain name was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Indicates whether the Security Socket Layer (SSL) certificate is enabled. Valid values:
        # 
        # *   **on**: **enabled**
        # *   **off**: **disabled**
        self.sslprotocol = sslprotocol
        # The public key of the certificate if HTTPS is enabled.
        self.sslpub = sslpub
        # Acceleration scenario. Valid values:
        # 
        # *   **apiscene**: API acceleration.
        # *   **webservicescene**: website acceleration.
        # *   **staticscene**: video, image, and text acceleration.
        # *   **an empty string**: no acceleration scenario is used.
        self.scene = scene
        # The acceleration region. Default value: domestic. Valid values:
        # 
        # *   **domestic**: Chinese mainland
        # *   **overseas**: global (excluding the Chinese mainland)
        # *   **global**: global
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
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.description is not None:
            result['Description'] = self.description

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

        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.sources is not None:
            result['Sources'] = self.sources.to_map()

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

        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Sources') is not None:
            temp_model = main_models.DescribeDcdnDomainDetailResponseBodyDomainDetailSources()
            self.sources = temp_model.from_map(m.get('Sources'))

        return self

class DescribeDcdnDomainDetailResponseBodyDomainDetailSources(DaraModel):
    def __init__(
        self,
        source: List[main_models.DescribeDcdnDomainDetailResponseBodyDomainDetailSourcesSource] = None,
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
                temp_model = main_models.DescribeDcdnDomainDetailResponseBodyDomainDetailSourcesSource()
                self.source.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainDetailResponseBodyDomainDetailSourcesSource(DaraModel):
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
        # The port over which requests are redirected to the origin server. Ports 443 and 80 are supported.
        self.port = port
        # The priority.
        self.priority = priority
        # The type of the origin server. Valid values:
        # 
        # *   **ipaddr**: an IP address
        # *   **domain**: an origin domain name
        # *   **oss**: the domain name of an Object Storage Service (OSS) bucket
        self.type = type
        # The weight of the origin server if multiple origin servers are specified.
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

