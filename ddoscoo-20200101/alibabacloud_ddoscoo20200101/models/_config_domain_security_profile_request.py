# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigDomainSecurityProfileRequest(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        config: str = None,
        domain: str = None,
    ):
        # This parameter is unavailable.
        self.cluster = cluster
        # The configurations for the global mitigation policy feature. The configurations include the following fields:
        # 
        # *   **global_rule_mode**: optional. The mode for the global mitigation policy feature. Data type: string. Valid values:
        # 
        #     *   **weak**: loose.
        #     *   **default**: normal.
        #     *   **hard**: strict.
        # 
        # *   **global_rule_enable**: optional. Specifies whether to enable the global mitigation policy feature. Data type: string. Valid values:
        # 
        #     *   **0**: disabled.
        #     *   **1**: enabled.
        # 
        # This parameter is required.
        self.config = config
        # The domain name of the website.
        # 
        # >  A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['Cluster'] = self.cluster

        if self.config is not None:
            result['Config'] = self.config

        if self.domain is not None:
            result['Domain'] = self.domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cluster') is not None:
            self.cluster = m.get('Cluster')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        return self

