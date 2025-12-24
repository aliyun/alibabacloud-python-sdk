# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainDetailResponseBody(DaraModel):
    def __init__(
        self,
        domain_detail: main_models.DescribeLiveDomainDetailResponseBodyDomainDetail = None,
        request_id: str = None,
    ):
        # The configuration details of the domain name.
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
            temp_model = main_models.DescribeLiveDomainDetailResponseBodyDomainDetail()
            self.domain_detail = temp_model.from_map(m.get('DomainDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveDomainDetailResponseBodyDomainDetail(DaraModel):
    def __init__(
        self,
        cert_name: str = None,
        cname: str = None,
        description: str = None,
        domain_name: str = None,
        domain_status: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        live_domain_type: str = None,
        region: str = None,
        resource_group_id: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        scope: str = None,
    ):
        # The name of the certificate.
        self.cert_name = cert_name
        # The CNAME that is assigned to the domain name. You must add a CNAME record in the system of your Domain Name System (DNS) service provider to map the domain name to the CNAME.
        # 
        # >  A time-to-live (TTL) value is specified in the CNAME record of a domain name to indicate how long the CNAME record can be cached on the DNS resolver. If you modify the CNAME record of the domain name, the new settings take effect after the cache expires, which takes about 10 minutes. For more information, see [CNAME resolution](https://help.aliyun.com/document_detail/362010.html).
        self.cname = cname
        # The description of the domain name.
        self.description = description
        # The streaming domain or ingest domain.
        self.domain_name = domain_name
        # The status of the domain name. Valid values:
        # 
        # *   **online**: The domain name is enabled.
        # *   **offline**: The domain name is disabled.
        # *   **configuring**: The domain is being configured.
        self.domain_status = domain_status
        # The time when the domain name was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.gmt_created = gmt_created
        # The time when the domain name was last modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The type of the domain name. Valid values:
        # 
        # *   **liveVideo**: streaming domain
        # *   **liveEdge**: ingest domain
        self.live_domain_type = live_domain_type
        # The ID of the region where the domain name resides.
        self.region = region
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Indicates whether the SSL certificate is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.sslprotocol = sslprotocol
        # The public key of the certificate.
        self.sslpub = sslpub
        # The acceleration region. Valid values:
        # 
        # *   **domestic**: regions in the Chinese mainland.
        # *   **overseas**: regions outside the Chinese mainland.
        # *   **global**: regions in and outside the Chinese mainland.
        self.scope = scope

    def validate(self):
        pass

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

        if self.live_domain_type is not None:
            result['LiveDomainType'] = self.live_domain_type

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol

        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub

        if self.scope is not None:
            result['Scope'] = self.scope

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

        if m.get('LiveDomainType') is not None:
            self.live_domain_type = m.get('LiveDomainType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')

        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

