# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTlsConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        domain: str = None,
        resource_group_id: str = None,
    ):
        # The details of the TLS policy. The value is a JSON string that contains the following fields:
        # 
        # *   **ssl_protocols**: the version of TLS. This field is required. Data type: string. Valid values:
        # 
        #     *   **tls1.0**: TLS 1.0 and later
        #     *   **tls1.1**: TLS 1.1 and later
        #     *   **tls1.2**: TLS 1.2 and later
        # 
        # *   **ssl_ciphers**: the type of the cipher suite. This field is required. Data type: string. Valid values:
        # 
        #     *   **all**: all cipher suites, which include strong and weak cipher suites
        #     *   **improved**: enhanced cipher suites
        #     *   **strong**: strong cipher suites
        #     *   **default**: default cipher suites, which include only strong cipher suites
        # 
        # This parameter is required.
        self.config = config
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

