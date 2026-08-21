# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodDomainDetailResponseBody(DaraModel):
    def __init__(
        self,
        domain_detail: main_models.DescribeVodDomainDetailResponseBodyDomainDetail = None,
        request_id: str = None,
    ):
        # The basic configuration information of the domain name.
        self.domain_detail = domain_detail
        # The request ID.
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
            temp_model = main_models.DescribeVodDomainDetailResponseBodyDomainDetail()
            self.domain_detail = temp_model.from_map(m.get('DomainDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVodDomainDetailResponseBodyDomainDetail(DaraModel):
    def __init__(
        self,
        cert_name: str = None,
        cname: str = None,
        description: str = None,
        domain_name: str = None,
        domain_status: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        scope: str = None,
        sources: main_models.DescribeVodDomainDetailResponseBodyDomainDetailSources = None,
        weight: str = None,
    ):
        # The name of the HTTPS certificate. This parameter is returned only if HTTPS secure acceleration is enabled.
        self.cert_name = cert_name
        # The CNAME assigned to the accelerated domain name. You must add a CNAME record with your DNS provider to map the accelerated domain name to this CNAME. For more information, see [Configure a CNAME record](https://help.aliyun.com/document_detail/86075.html).
        self.cname = cname
        # The description of the VOD acceleration domain name.
        self.description = description
        # The VOD acceleration domain name.
        self.domain_name = domain_name
        # The status of the accelerated domain name. Valid values:
        # 
        # - **online**: enabled.
        # - **offline**: disabled.
        # - **configuring**: being configured.
        # - **configure_failed**: configuration failed.
        # - **checking**: being reviewed.
        # - **check_failed**: review failed.
        self.domain_status = domain_status
        # The time when the domain name was created. The time follows the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is displayed in UTC.
        self.gmt_created = gmt_created
        # The time when the domain name was last modified. The time follows the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # Indicates whether the SSL certificate is enabled. Valid values:
        # 
        # - **on**: Enabled.
        # - **off**: Disabled.
        self.sslprotocol = sslprotocol
        # The public key of the HTTPS certificate. This parameter is returned only if HTTPS secure acceleration is enabled.
        self.sslpub = sslpub
        # The acceleration region. Valid values:
        # 
        # - **domestic** (default): the Chinese mainland only.
        # - **overseas**: global (excluding the Chinese mainland).
        # - **global**: global.
        self.scope = scope
        self.sources = sources
        # The back-to-origin weight.
        self.weight = weight

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

        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol

        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.sources is not None:
            result['Sources'] = self.sources.to_map()

        if self.weight is not None:
            result['Weight'] = self.weight

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

        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')

        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Sources') is not None:
            temp_model = main_models.DescribeVodDomainDetailResponseBodyDomainDetailSources()
            self.sources = temp_model.from_map(m.get('Sources'))

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class DescribeVodDomainDetailResponseBodyDomainDetailSources(DaraModel):
    def __init__(
        self,
        source: List[main_models.DescribeVodDomainDetailResponseBodyDomainDetailSourcesSource] = None,
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
                temp_model = main_models.DescribeVodDomainDetailResponseBodyDomainDetailSourcesSource()
                self.source.append(temp_model.from_map(k1))

        return self

class DescribeVodDomainDetailResponseBodyDomainDetailSourcesSource(DaraModel):
    def __init__(
        self,
        content: str = None,
        enabled: str = None,
        port: int = None,
        priority: str = None,
        type: str = None,
        weight: str = None,
    ):
        self.content = content
        self.enabled = enabled
        self.port = port
        self.priority = priority
        self.type = type
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

