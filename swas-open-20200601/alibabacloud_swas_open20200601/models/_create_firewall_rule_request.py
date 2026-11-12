# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFirewallRuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        port: str = None,
        region_id: str = None,
        remark: str = None,
        rule_protocol: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The instance ID of the specified simple application server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The port range.
        # - TCP/UDP: Valid values: 1 to 65535. Use a forward slash (/) to separate the start port and the end port. For example, 1024/1055 indicates the port range from 1024 to 1055.
        # - ICMP: -1/-1. This value indicates all ports.
        # 
        # This parameter is required.
        self.port = port
        # The region ID of the specified simple application server.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The remark for the firewall rule.
        self.remark = remark
        # The transport layer protocol. Valid values:
        # 
        # - TCP: TCP
        # - UDP: UDP
        # - TCP+UDP: TCP and UDP
        # - ICMP: ICMP
        # 
        # This parameter is required.
        self.rule_protocol = rule_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_protocol is not None:
            result['RuleProtocol'] = self.rule_protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleProtocol') is not None:
            self.rule_protocol = m.get('RuleProtocol')

        return self

