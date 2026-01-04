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
        # The detailed settings of the port forwarding rule. This parameter is a JSON string and contains the following fields. The detailed settings of a TCP port forwarding rule contain the following fields.
        # 
        # *   **PersistenceTimeout**: the timeout period of session persistence. This field is required and of the integer type. Valid values: **30** to **3600**. Unit: seconds. Default value: **0**, which indicates that session persistence is disabled.
        # *   **Synproxy**: specifies whether to enable the false source feature in the DDoS mitigation policy. This field is required and of the string type. Valid values: off and on.
        # *   **NodataConn**: specifies whether to enable the empty connection feature in the DDoS mitigation policy. This field is required and of the string type. Valid values: off and on.
        # *   **Sla**: the settings of the speed limit for destination feature. This field is required and of the struct type. For more information, see the following description about Sla.
        # *   **Slimit**: the settings of the rate limit for source feature. This field is required and of the struct type. For more information, see the following description about Slimit.
        # *   **PayloadLen**: the settings of the packet length limit feature. This field is required and of the struct type. For more information, see the following description about PayloadLen.
        # 
        # Sla contains the following fields:
        # 
        # *   **Cps**: the destination rate limit on new connections in the DDoS mitigation policy. This field is required and of the integer type. Valid values: 100 to 100000.
        # *   **Maxconn**: the destination rate limit on concurrent connections in the DDoS mitigation policy. This field is required and of the integer type. Valid values: 1000 to 1000000.
        # *   **CpsEnable**: specifies whether to enable Cps. This field is required and of the integer type. Valid values: 0 and 1. Default value: 1. The value 0 indicates that Cps is disabled, and the value 1 indicates that Cps is enabled.
        # *   **MaxconnEnable**: specifies whether to enable Maxconn. This field is required and of the integer type. Valid values: 0 and 1. Default value: 1. The value 0 indicates that Maxconn is disabled, and the value 1 indicates that Maxconn is enabled.
        # 
        # Slimit contains the following fields:
        # 
        # *   **Cps**: the source rate limit on new connections in the DDoS mitigation policy. This field is required and of the integer type. Valid values: 1 to 50000.
        # *   **Maxconn**: the source rate limit on concurrent connections in the DDoS mitigation policy. This field is required and of the integer type. Valid values: 1 to 50000.
        # *   **CpsEnable**: specifies whether to enable Cps. This field is required and of the integer type. Valid values: 0 and 1. Default value: 1. The value 0 indicates that Cps is disabled, and the value 1 indicates that Cps is enabled.
        # *   **MaxconnEnable**: specifies whether to enable Maxconn. This field is required and of the integer type. Valid values: 0 and 1. Default value: 1. The value 0 indicates that Maxconn is disabled, and the value 1 indicates that Maxconn is enabled.
        # *   **CpsMode**: specifies whether to enable the source rate limit on new connections. This field is required and of the integer type. Valid values: 1 and 2. The value 1 indicates that the source rate limit is disabled. The value 2 indicates that the system determines whether to enable the source rate limit.
        # 
        # PayloadLen contains the following fields:
        # 
        # *   **Min**: the minimum packet length in the DDoS mitigation policy. This field is required and of the integer type. Valid values: 0 to 1500.
        # *   **Max**: the maximum packet length in the DDoS mitigation policy. This field is required and of the integer type. Valid values: 0 to 1500.
        # 
        # This parameter is required.
        self.config = config
        # The forwarding protocol. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        # 
        # This parameter is required.
        self.forward_protocol = forward_protocol
        # The forwarding port.
        # 
        # This parameter is required.
        self.frontend_port = frontend_port
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
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

