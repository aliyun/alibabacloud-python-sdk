# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigLayer4RuleBakModeRequest(DaraModel):
    def __init__(
        self,
        bak_mode: str = None,
        listeners: str = None,
    ):
        # The back-to-origin mode. Valid values:
        # - **0**: The default back-to-origin mode. Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the origin server IP address that you specified when you called [CreateNetworkRules](https://help.aliyun.com/document_detail/157482.html) to create the port forwarding rule.
        # - **1**: The origin redundancy mode. Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the primary origin server IP address or secondary origin server IP address that you configured by calling [ConfigLayer4RulePolicy](https://help.aliyun.com/document_detail/312684.html).
        # 
        # This parameter is required.
        self.bak_mode = bak_mode
        # The port forwarding rule to configure.
        # 
        # This parameter is a string converted from a JSON array. Each element in the JSON array represents a created port forwarding rule. You can configure up to one port forwarding rule at a time.
        # 
        # > You can call [DescribeNetworkRules](https://help.aliyun.com/document_detail/157484.html) to query all created port forwarding rules.
        # 
        # Each port forwarding rule contains the following fields:
        # 
        # - **InstanceId**: String type. Required. The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # - **Protocol**: String type. Required. The forwarding protocol type. Valid values: **tcp**, **udp**.
        # - **FrontendPort**: Integer type. Required. The Redirection Port.
        # 
        # This parameter is required.
        self.listeners = listeners

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bak_mode is not None:
            result['BakMode'] = self.bak_mode

        if self.listeners is not None:
            result['Listeners'] = self.listeners

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BakMode') is not None:
            self.bak_mode = m.get('BakMode')

        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')

        return self

