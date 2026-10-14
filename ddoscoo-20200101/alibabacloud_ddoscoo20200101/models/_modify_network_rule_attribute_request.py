# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNetworkRuleAttributeRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        forward_protocol: str = None,
        frontend_port: int = None,
        instance_id: str = None,
        module: str = None,
    ):
        # The advanced settings for the port forwarding rule. Specify the settings as a JSON string. The structure is described below.
        # The structure of \\`TcpConfig\\` is as follows:
        # 
        # - **PersistenceTimeout**: An integer. This parameter is required. The timeout period for session persistence. Unit: seconds. Valid values: **30** to **3600**. The default value is **0**, which disables session persistence.
        # 
        # - **Synproxy**: A string. This parameter is required. The status of the False Source setting for the DDoS mitigation policy. Valid values: \\`off\\` and \\`on\\`.
        # 
        # - **NodataConn**: A string. This parameter is required. The status of the Empty Connection setting for the DDoS mitigation policy. Valid values: \\`off\\` and \\`on\\`.
        # 
        # - **Sla**: A struct. This parameter is required. The configuration for destination rate limiting. For more information, see the \\`Sla\\` section below.
        # 
        # - **Slimit**: A struct. This parameter is required. The configuration for source rate limiting. For more information, see the \\`Slimit\\` section below.
        # 
        # - **PayloadLen**: A struct. This parameter is required. The packet length filter configuration. For more information, see the \\`PayloadLen\\` section below.
        # 
        # The structure of \\`Sla\\` is as follows:
        # 
        # - **Cps**: An integer. This parameter is required. The maximum number of new connections per second to a destination IP address. Valid values: 100 to 100,000.
        # 
        # - **Maxconn**: An integer. This parameter is required. The maximum number of concurrent connections to a destination IP address. Valid values: 1,000 to 1,000,000.
        # 
        # - **CpsEnable**: An integer. This parameter is required. Specifies whether to enable the limit on new connections. Valid values: 0 (disabled) and 1 (enabled). The default value is 1.
        # 
        # - **MaxconnEnable**: An integer. This parameter is required. Specifies whether to enable the limit on concurrent connections. Valid values: 0 (disabled) and 1 (enabled). The default value is 1.
        # 
        # The structure of \\`Slimit\\` is as follows:
        # 
        # - **Cps**: An integer. This parameter is required. The maximum number of new connections per second from a source IP address. Valid values: 1 to 50,000.
        # 
        # - **Maxconn**: An integer. This parameter is required. The maximum number of concurrent connections from a source IP address. Valid values: 1 to 50,000.
        # 
        # - **CpsEnable**: An integer. This parameter is required. Specifies whether to enable the limit on new connections. Valid values: 0 (disabled) and 1 (enabled). The default value is 1.
        # 
        # - **MaxconnEnable**: An integer. This parameter is required. Specifies whether to enable the limit on concurrent connections. Valid values: 0 (disabled) and 1 (enabled). The default value is 1.
        # 
        # - **CpsMode**: An integer. This parameter is required. The mode for the new connection rate limit from a source IP address. Valid values: 1 (off) and 2 (auto).
        # 
        # The structure of \\`PayloadLen\\` is as follows:
        # 
        # - **Min**: An integer. This parameter is required. The minimum packet length. Valid values: 0 to 1,500.
        # 
        # - **Max**: An integer. This parameter is required. The maximum packet length. Valid values: 0 to 1,500.
        # 
        # This parameter is required.
        self.config = config
        # The forwarding protocol. Valid values:
        # 
        # - **tcp**
        # 
        # - **udp**
        # 
        # This parameter is required.
        self.forward_protocol = forward_protocol
        # The forwarding port.
        # 
        # This parameter is required.
        self.frontend_port = frontend_port
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # 
        # > Call [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) to query the IDs of all Anti-DDoS Pro and Anti-DDoS Premium instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The module for Layer 7 port support. The default value is sla. Valid value:
        # 
        # **sla**: Speed Limit for Destination
        self.module = module

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol

        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.module is not None:
            result['Module'] = self.module

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')

        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        return self

