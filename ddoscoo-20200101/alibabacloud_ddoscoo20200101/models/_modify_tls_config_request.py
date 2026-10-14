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
        # The details of the TLS security policy, expressed as a JSON-formatted string with the following structure.
        # - **ssl_protocols**: String type, required. The TLS version. Valid values:
        #     - **tls1.0**: TLS 1.0 and later are supported.
        #     - **tls1.1**: TLS 1.1 and later are supported.
        #     - **tls1.2**: TLS 1.2 and later are supported.
        # - **ssl_ciphers**: String type, required. The cipher suite type. Valid values:
        #     - **all**: all cipher suites, including strong and weak cipher suites
        #     - **improved**: enhanced cipher suites
        #     - **strong**: strong cipher suites only
        #     - **default**: default cipher suites, which include only strong cipher suites
        # - **ssl_13_enabled**: Boolean type, optional. Specifies whether to enable TLS 1.3. Valid values:
        #     - **true**: Enables TLS 1.3.
        #     - **false**: Disables TLS 1.3.
        # - **custom_ciphers**: Array type, optional. The list of custom cipher suites for TLS versions earlier than 1.3.
        # - **tls_13_custom_ciphers**: Array type, optional. The list of custom cipher suites for TLS 1.3. If TLS 1.3 is enabled, select at least one cipher suite for TLS versions earlier than 1.3.
        # 
        # This parameter is required.
        self.config = config
        # The domain name of the website.
        # > The domain name must have a website forwarding rule configured. You can call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the resource group to which the Anti-DDoS Pro or Anti-DDoS Premium instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
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

