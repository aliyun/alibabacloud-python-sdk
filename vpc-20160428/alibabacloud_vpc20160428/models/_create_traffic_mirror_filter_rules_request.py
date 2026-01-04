# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateTrafficMirrorFilterRulesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        egress_rules: List[main_models.CreateTrafficMirrorFilterRulesRequestEgressRules] = None,
        ingress_rules: List[main_models.CreateTrafficMirrorFilterRulesRequestIngressRules] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        traffic_mirror_filter_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to check the request without performing the operation. Valid values:
        # 
        # *   **true**: checks the request without performing the operation. The system checks the required parameters, request format, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. After the request passes the check, the operation is performed.
        self.dry_run = dry_run
        # The information about the outbound rule.
        self.egress_rules = egress_rules
        # The information about the inbound rules.
        self.ingress_rules = ingress_rules
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region to which the mirrored traffic belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list. For more information about regions that support traffic mirror, see [Overview of traffic mirror](https://help.aliyun.com/document_detail/207513.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the filter.
        # 
        # This parameter is required.
        self.traffic_mirror_filter_id = traffic_mirror_filter_id

    def validate(self):
        if self.egress_rules:
            for v1 in self.egress_rules:
                 if v1:
                    v1.validate()
        if self.ingress_rules:
            for v1 in self.ingress_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        result['EgressRules'] = []
        if self.egress_rules is not None:
            for k1 in self.egress_rules:
                result['EgressRules'].append(k1.to_map() if k1 else None)

        result['IngressRules'] = []
        if self.ingress_rules is not None:
            for k1 in self.ingress_rules:
                result['IngressRules'].append(k1.to_map() if k1 else None)

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.traffic_mirror_filter_id is not None:
            result['TrafficMirrorFilterId'] = self.traffic_mirror_filter_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        self.egress_rules = []
        if m.get('EgressRules') is not None:
            for k1 in m.get('EgressRules'):
                temp_model = main_models.CreateTrafficMirrorFilterRulesRequestEgressRules()
                self.egress_rules.append(temp_model.from_map(k1))

        self.ingress_rules = []
        if m.get('IngressRules') is not None:
            for k1 in m.get('IngressRules'):
                temp_model = main_models.CreateTrafficMirrorFilterRulesRequestIngressRules()
                self.ingress_rules.append(temp_model.from_map(k1))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TrafficMirrorFilterId') is not None:
            self.traffic_mirror_filter_id = m.get('TrafficMirrorFilterId')

        return self

class CreateTrafficMirrorFilterRulesRequestIngressRules(DaraModel):
    def __init__(
        self,
        action: str = None,
        destination_cidr_block: str = None,
        destination_port_range: str = None,
        ip_version: str = None,
        priority: int = None,
        protocol: str = None,
        source_cidr_block: str = None,
        source_port_range: str = None,
    ):
        # The policy of the inbound rule. Valid values:
        # 
        # *   **accept**: collects network traffic.
        # *   **drop**: drops network traffic.
        self.action = action
        # The destination CIDR block of the inbound traffic.
        self.destination_cidr_block = destination_cidr_block
        # The destination port range of the inbound traffic. Valid value: **1** to **65535**. Separate the first and the last port with a forward slash (/). For example, **1/200** or **80/80**.
        # 
        # >  If the **IngressRules.N.Protocol** parameter is set to **ALL** or **ICMP**, you do not need to set this parameter. In this case, all ports are available.
        self.destination_port_range = destination_port_range
        # The IP version of the instance. The following value may be returned:
        # 
        # *   **IPv4**: IPv4
        # *   **IPv6**: IPv6
        self.ip_version = ip_version
        # The priority of the inbound rule. A smaller value indicates a higher priority. The maximum value of **N** is **10**. You can configure up to 10 inbound rules for a filter.
        self.priority = priority
        # The protocol that is used by the inbound traffic to be mirrored. Valid values:
        # 
        # *   **ALL**: all protocols
        # *   **ICMP**: Internet Control Message Protocol.
        # *   **TCP**: Transmission Control Protocol.
        # *   **UDP**: User Datagram Protocol.
        self.protocol = protocol
        # The source CIDR block of the inbound traffic.
        self.source_cidr_block = source_cidr_block
        # The source port range of the inbound traffic. Valid value: **1** to **65535**. Separate the first and last port with a forward slash (/). For example **1/200** and **80/80**. You cannot set this parameter to \\*\\*-1/-1\\*\\*, which indicates all ports.
        # 
        # >  If the **IngressRules.N.Protocol** parameter is set to **ALL** or **ICMP**, you do not need to set this parameter. In this case, all ports are available.
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.destination_port_range is not None:
            result['DestinationPortRange'] = self.destination_port_range

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.source_cidr_block is not None:
            result['SourceCidrBlock'] = self.source_cidr_block

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('DestinationPortRange') is not None:
            self.destination_port_range = m.get('DestinationPortRange')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SourceCidrBlock') is not None:
            self.source_cidr_block = m.get('SourceCidrBlock')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

class CreateTrafficMirrorFilterRulesRequestEgressRules(DaraModel):
    def __init__(
        self,
        action: str = None,
        destination_cidr_block: str = None,
        destination_port_range: str = None,
        ip_version: str = None,
        priority: int = None,
        protocol: str = None,
        source_cidr_block: str = None,
        source_port_range: str = None,
    ):
        # The collection policy of the outbound rule. Valid values:
        # 
        # *   **accept**: accepts network traffic.
        # *   **drop**: drops network traffic.
        self.action = action
        # The destination CIDR block of the outbound traffic.
        self.destination_cidr_block = destination_cidr_block
        # The destination port range of the outbound traffic. Valid value: **1** to **65535**. Separate the first and last port with a forward slash (/). For example **1/200** and **80/80**. You cannot set this parameter to \\*\\*-1/-1\\*\\*, which indicates all ports.
        # 
        # >  If **EgressRules.N.Protocol** is set to **ALL** or **ICMP**, you do not need to set this parameter. In this case, all ports are available.
        self.destination_port_range = destination_port_range
        # The IP version of the instance. Valid values:
        # 
        # *   **IPv4**: IPv4
        # *   **IPv6**: IPv6
        self.ip_version = ip_version
        # The priority of the outbound rule. A smaller value indicates a higher priority. The maximum value of **N** is **10**. You can configure up to 10 outbound rules for a filter.
        self.priority = priority
        # The protocol that is used by the outbound traffic to be mirrored. Valid values:
        # 
        # *   **ALL**: all protocols
        # *   **ICMP**: Internet Control Message Protocol.
        # *   **TCP**: Transmission Control Protocol.
        # *   **UDP**: User Datagram Protocol.
        self.protocol = protocol
        # The source CIDR block of the outbound traffic.
        self.source_cidr_block = source_cidr_block
        # The source port range of the outbound traffic. Valid value: **1** to **65535**. Separate the first and last port with a forward slash (/). For example **1/200** and **80/80**. You cannot set this parameter to \\*\\*-1/-1\\*\\*, which indicates all ports.
        # 
        # >  If **EgressRules.N.Protocol** is set to **ALL** or **ICMP**, you do not need to set this parameter. In this case, all ports are available.
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.destination_port_range is not None:
            result['DestinationPortRange'] = self.destination_port_range

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.source_cidr_block is not None:
            result['SourceCidrBlock'] = self.source_cidr_block

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('DestinationPortRange') is not None:
            self.destination_port_range = m.get('DestinationPortRange')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SourceCidrBlock') is not None:
            self.source_cidr_block = m.get('SourceCidrBlock')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

