# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsDomainDetailResponseBody(DaraModel):
    def __init__(
        self,
        domain_config: main_models.DescribeVsDomainDetailResponseBodyDomainConfig = None,
        request_id: str = None,
    ):
        # Domain configuration details.
        self.domain_config = domain_config
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_config:
            self.domain_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_config is not None:
            result['DomainConfig'] = self.domain_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainConfig') is not None:
            temp_model = main_models.DescribeVsDomainDetailResponseBodyDomainConfig()
            self.domain_config = temp_model.from_map(m.get('DomainConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVsDomainDetailResponseBodyDomainConfig(DaraModel):
    def __init__(
        self,
        cname: str = None,
        description: str = None,
        domain_name: str = None,
        domain_status: str = None,
        domain_type: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        region: str = None,
        sslprotocol: str = None,
        scope: str = None,
    ):
        # The CNAME assigned to the Visual Edge Computing Service domain. You must configure your DNS provider to point your domain to this CNAME.
        self.cname = cname
        # The domain description.
        self.description = description
        # The Visual Edge Computing Service domain name.
        self.domain_name = domain_name
        # The status of the Visual Edge Computing Service accelerated domain. Valid values:
        # 
        # - **online**: Enabled.
        # 
        # - **offline**: Disabled.
        # 
        # - **configuring**: Being configured.
        self.domain_status = domain_status
        # The domain type.
        # 
        # > Static value: vs
        self.domain_type = domain_type
        # The creation time.
        self.gmt_created = gmt_created
        # The most recent modification time.
        self.gmt_modified = gmt_modified
        # The region where the domain is located.
        self.region = region
        # Indicates whether HTTPS is enabled. Valid values:
        # 
        # - **on**: Enabled.
        # 
        # - **off** (default): Disabled.
        self.sslprotocol = sslprotocol
        # The acceleration region. Valid values:
        # 
        # - **domestic**
        # 
        # - **overseas**
        # 
        # - **global**
        self.scope = scope

    def validate(self):
        pass

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

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.region is not None:
            result['Region'] = self.region

        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol

        if self.scope is not None:
            result['Scope'] = self.scope

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

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

