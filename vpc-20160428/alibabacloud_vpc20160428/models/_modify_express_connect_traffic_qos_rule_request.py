# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyExpressConnectTrafficQosRuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dst_cidr: str = None,
        dst_ipv_6cidr: str = None,
        dst_port_range: str = None,
        match_dscp: int = None,
        owner_account: str = None,
        owner_id: int = None,
        priority: int = None,
        protocol: str = None,
        qos_id: str = None,
        queue_id: str = None,
        region_id: str = None,
        remarking_dscp: int = None,
        resource_owner_account: str = None,
        rule_description: str = None,
        rule_id: str = None,
        rule_name: str = None,
        src_cidr: str = None,
        src_ipv_6cidr: str = None,
        src_port_range: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The destination IPv4 CIDR block that matches the QoS rule traffic.
        # 
        # > When this parameter is unavailable, specify **SrcIPv6Cidr** or **DstIPv6Cidr**.
        self.dst_cidr = dst_cidr
        # The destination IPv6 CIDR block that matches the QoS rule traffic.
        # 
        # > When this parameter is unavailable, specify **SrcCidr** or **DstCidr**.
        self.dst_ipv_6cidr = dst_ipv_6cidr
        # The range of destination ports that match the QoS rule traffic. Valid values: **0** to **65535**. If the traffic does not match, the value is -1. You can specify only one port. The start port number must be the same as the end port number. Different protocols correspond to different ports. Valid values:
        # 
        # *   **ALL** (uneditable): -1/-1.
        # *   **ICMP(IPv4)** (uneditable): -1/-1.
        # *   **ICMPv6(IPv6)** (uneditable): -1/-1.
        # *   **TCP** (editable): -1/-1.
        # *   **UDP** (editable): -1/-1.
        # *   **GRE** (uneditable): -1/-1.
        # *   **SSH** (uneditable): 22/22.
        # *   **Telnet** (uneditable): 23/23.
        # *   **HTTP** (uneditable): 80/80.
        # *   **HTTPS** (uneditable): 443/443.
        # *   **MS SQL** (uneditable): 1443/1443.
        # *   **Oracle** (uneditable): 1521/1521.
        # *   **MySql** (uneditable): 3306/3306.
        # *   **RDP** (uneditable): 3389/3389.
        # *   **PostgreSQL** (uneditable): 5432/5432.
        # *   **Redis** (uneditable): 6379/6379.
        self.dst_port_range = dst_port_range
        # The DSCP value that matches the QoS rule traffic. Valid values: **0** to **63**. If no value is matched, the value is -1.
        self.match_dscp = match_dscp
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The priority of the QoS rule. Valid values: **1** to **9000**. A larger value indicates a higher priority. The priority of each QoS rule must be unique in the same QoS policy.
        self.priority = priority
        # The protocol of the QoS rule. Valid values:
        # 
        # *   **ALL**
        # *   **ICMP(IPv4)**
        # *   **ICMPv6(IPv6)**
        # *   **TCP**
        # *   **UDP**
        # *   **GRE**
        # *   **SSH**
        # *   **Telnet**
        # *   **HTTP**
        # *   **HTTPS**
        # *   **MS SQL**
        # *   **Oracle**
        # *   **MySql**
        # *   **RDP**
        # *   **PostgreSQL**
        # *   **Redis**
        self.protocol = protocol
        # The ID of the QoS policy.
        # 
        # This parameter is required.
        self.qos_id = qos_id
        # The ID of the QoS queue.
        # 
        # This parameter is required.
        self.queue_id = queue_id
        # The region ID of the QoS policy.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The new DSCP value. Valid values: **0** to **63**. If you do not change the value, set the value to -1.
        self.remarking_dscp = remarking_dscp
        self.resource_owner_account = resource_owner_account
        # The description of the QoS rule.
        # 
        # The description must be 0 to 256 characters in length and cannot start with `http://` or `https://`.
        self.rule_description = rule_description
        # The ID of the QoS rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the QoS rule.
        # 
        # The name must be 0 to 128 characters in length and cannot start with `http://` or `https://`.
        self.rule_name = rule_name
        # The source IPv4 CIDR block that matches the QoS rule traffic.
        # 
        # > When this parameter is unavailable, specify **SrcIPv6Cidr** or **DstIPv6Cidr**.
        self.src_cidr = src_cidr
        # The source IPv6 CIDR block that matches the QoS rule traffic.
        # 
        # > When this parameter is unavailable, specify **SrcCidr** or **DstCidr**.
        self.src_ipv_6cidr = src_ipv_6cidr
        # The range of source ports that match the QoS rule traffic. Valid values: **0** to **65535**. If the traffic does not match, the value is -1. You can specify only one port. The start port number must be the same as the end port number.
        self.src_port_range = src_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dst_cidr is not None:
            result['DstCidr'] = self.dst_cidr

        if self.dst_ipv_6cidr is not None:
            result['DstIPv6Cidr'] = self.dst_ipv_6cidr

        if self.dst_port_range is not None:
            result['DstPortRange'] = self.dst_port_range

        if self.match_dscp is not None:
            result['MatchDscp'] = self.match_dscp

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.queue_id is not None:
            result['QueueId'] = self.queue_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remarking_dscp is not None:
            result['RemarkingDscp'] = self.remarking_dscp

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.rule_description is not None:
            result['RuleDescription'] = self.rule_description

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.src_cidr is not None:
            result['SrcCidr'] = self.src_cidr

        if self.src_ipv_6cidr is not None:
            result['SrcIPv6Cidr'] = self.src_ipv_6cidr

        if self.src_port_range is not None:
            result['SrcPortRange'] = self.src_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DstCidr') is not None:
            self.dst_cidr = m.get('DstCidr')

        if m.get('DstIPv6Cidr') is not None:
            self.dst_ipv_6cidr = m.get('DstIPv6Cidr')

        if m.get('DstPortRange') is not None:
            self.dst_port_range = m.get('DstPortRange')

        if m.get('MatchDscp') is not None:
            self.match_dscp = m.get('MatchDscp')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemarkingDscp') is not None:
            self.remarking_dscp = m.get('RemarkingDscp')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('RuleDescription') is not None:
            self.rule_description = m.get('RuleDescription')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SrcCidr') is not None:
            self.src_cidr = m.get('SrcCidr')

        if m.get('SrcIPv6Cidr') is not None:
            self.src_ipv_6cidr = m.get('SrcIPv6Cidr')

        if m.get('SrcPortRange') is not None:
            self.src_port_range = m.get('SrcPortRange')

        return self

