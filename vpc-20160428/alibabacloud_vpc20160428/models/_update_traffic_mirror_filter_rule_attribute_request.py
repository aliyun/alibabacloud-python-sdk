# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTrafficMirrorFilterRuleAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        destination_cidr_block: str = None,
        destination_port_range: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        priority: int = None,
        protocol: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rule_action: str = None,
        source_cidr_block: str = None,
        source_port_range: str = None,
        traffic_mirror_filter_rule_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** as the **ClientToken**. The **RequestId** may be different for each request.
        self.client_token = client_token
        # The destination CIDR block of the network traffic for the inbound or outbound rule to be modified.
        self.destination_cidr_block = destination_cidr_block
        # The destination port range of the network traffic for the inbound or outbound rule to be modified.
        # 
        # > If **Protocol** is set to **ICMP**, the port range cannot be modified.
        self.destination_port_range = destination_port_range
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # - **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the configuration of the inbound or outbound rule is modified.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The priority of the inbound or outbound rule to be modified. A smaller value indicates a higher priority.
        self.priority = priority
        # The Protocol Type of the network traffic to be mirrored by the inbound or outbound rule. Valid values:
        # 
        # - **ALL**: all protocols.
        # 
        # - **ICMP**: Internet Control Message Protocol.
        # 
        # - **TCP**: Transmission Control Protocol.
        # 
        # - **UDP**: User Datagram Protocol.
        self.protocol = protocol
        # The region ID of the traffic mirror.
        # 
        # You can call [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) to query the most recent region list. For more information about regions that support traffic mirroring, see [Traffic mirroring overview](https://help.aliyun.com/document_detail/207513.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The collection policy of the inbound or outbound rule to be modified. Valid values:
        # 
        # - **accept**: collects network traffic.
        # 
        # - **drop**: does not collect network traffic.
        self.rule_action = rule_action
        # The source CIDR block of the network traffic for the inbound or outbound rule to be modified.
        self.source_cidr_block = source_cidr_block
        # The source port range of the network traffic for the inbound or outbound rule to be modified.
        # > If **Protocol** is set to **ICMP**, the port range cannot be modified.
        self.source_port_range = source_port_range
        # The instance ID of the inbound or outbound rule of the traffic mirroring filter.
        # 
        # This parameter is required.
        self.traffic_mirror_filter_rule_id = traffic_mirror_filter_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.destination_port_range is not None:
            result['DestinationPortRange'] = self.destination_port_range

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.source_cidr_block is not None:
            result['SourceCidrBlock'] = self.source_cidr_block

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        if self.traffic_mirror_filter_rule_id is not None:
            result['TrafficMirrorFilterRuleId'] = self.traffic_mirror_filter_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('DestinationPortRange') is not None:
            self.destination_port_range = m.get('DestinationPortRange')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('SourceCidrBlock') is not None:
            self.source_cidr_block = m.get('SourceCidrBlock')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('TrafficMirrorFilterRuleId') is not None:
            self.traffic_mirror_filter_rule_id = m.get('TrafficMirrorFilterRuleId')

        return self

