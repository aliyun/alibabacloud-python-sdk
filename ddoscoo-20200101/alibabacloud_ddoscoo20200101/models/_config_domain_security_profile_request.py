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
        # Not in use.
        self.cluster = cluster
        # The Anti-DDoS Global Mitigation Policy for Protection for Website Services. The structure is as follows:
        # - **global_rule_mode**: String type. Optional. The protection level of the DDoS global mitigation feature. Valid values:
        #     - **weak**: Loose.
        #     - **default**: Normal.
        #     - **hard**: Strict.
        # - **global_rule_enable**: Integer type. Optional. The switch of the DDoS global mitigation feature. Valid values:
        #     - **0**: Shutdown.
        #     - **1**: Enabled.
        # 
        # The Blacklist/Whitelist feature of the custom mitigation policies for Protection for Website Services. The structure is as follows:
        # - **bwlist_enable**: Integer type. Optional. The switch of the custom mitigation policy blacklist/whitelist. Valid values:
        #     - **0**: Shutdown.
        #     - **1**: Enabled.
        # 
        # This parameter is required.
        self.config = config
        # The domain name of the website service.
        # > The domain name must have a website forwarding rule configured. You can call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names.
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

