# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateTrafficMirrorFilterRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        egress_rules: List[main_models.CreateTrafficMirrorFilterRequestEgressRules] = None,
        ingress_rules: List[main_models.CreateTrafficMirrorFilterRequestIngressRules] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateTrafficMirrorFilterRequestTag] = None,
        traffic_mirror_filter_description: str = None,
        traffic_mirror_filter_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a parameter value on your client to ensure that the value is unique across different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether to only perform a dry run for the request. Valid values:
        # 
        # - **true**: performs a dry run for the request without creating the traffic mirror filter. The system checks whether required parameters are specified, the request format, and service limits. If the dry run fails, the corresponding error is returned. If the dry run succeeds, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): sends a normal request. If the request passes the check, a 2xx HTTP status code is returned and the filter is created.
        self.dry_run = dry_run
        # The information about the outbound rules.
        self.egress_rules = egress_rules
        # The information about the inbound rules.
        self.ingress_rules = ingress_rules
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the traffic mirror.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs. For more information about the regions that support traffic mirroring, see [Traffic mirroring overview](https://help.aliyun.com/document_detail/207513.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the traffic mirroring belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags of the resource.
        self.tag = tag
        # The description of the traffic mirror filter.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.traffic_mirror_filter_description = traffic_mirror_filter_description
        # The name of the traffic mirror filter.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.traffic_mirror_filter_name = traffic_mirror_filter_name

    def validate(self):
        if self.egress_rules:
            for v1 in self.egress_rules:
                 if v1:
                    v1.validate()
        if self.ingress_rules:
            for v1 in self.ingress_rules:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.traffic_mirror_filter_description is not None:
            result['TrafficMirrorFilterDescription'] = self.traffic_mirror_filter_description

        if self.traffic_mirror_filter_name is not None:
            result['TrafficMirrorFilterName'] = self.traffic_mirror_filter_name

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
                temp_model = main_models.CreateTrafficMirrorFilterRequestEgressRules()
                self.egress_rules.append(temp_model.from_map(k1))

        self.ingress_rules = []
        if m.get('IngressRules') is not None:
            for k1 in m.get('IngressRules'):
                temp_model = main_models.CreateTrafficMirrorFilterRequestIngressRules()
                self.ingress_rules.append(temp_model.from_map(k1))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateTrafficMirrorFilterRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TrafficMirrorFilterDescription') is not None:
            self.traffic_mirror_filter_description = m.get('TrafficMirrorFilterDescription')

        if m.get('TrafficMirrorFilterName') is not None:
            self.traffic_mirror_filter_name = m.get('TrafficMirrorFilterName')

        return self

class CreateTrafficMirrorFilterRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. If you specify this parameter, you cannot specify an empty string.
        # 
        # A tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. If you specify this parameter, you can specify an empty string.
        # 
        # A tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateTrafficMirrorFilterRequestIngressRules(DaraModel):
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
        # The collection policy of the inbound rule. Valid values:
        # 
        # - **accept**: collects network traffic.
        # - **drop**: does not collect network traffic.
        self.action = action
        # The destination CIDR block of the network traffic for the inbound rule.
        self.destination_cidr_block = destination_cidr_block
        # The destination port range of the network traffic for the inbound rule. Valid values are **1** to **65535**. Separate the start port and the end port with a forward slash (/). Examples: **1/200** and **80/80**.
        # 
        # > If **IngressRules.N.Protocol** is set to **ALL** or **ICMP**, you do not need to specify this parameter, which indicates that all ports are allowed.
        self.destination_port_range = destination_port_range
        # The IP version of the instance. Valid values:
        # 
        # - **IPv4**: IPv4.
        # - **IPv6**: IPv6.
        self.ip_version = ip_version
        # The priority of the inbound rule. A smaller value indicates a higher priority.
        # The maximum value of **N** is **10**, which indicates that you can configure up to 10 inbound rules for a filter.
        self.priority = priority
        # The protocol type of the network traffic to be mirrored for the inbound rule. Valid values:
        # 
        # - **ALL**: all protocols.
        # - **ICMP**: Internet Control Message Protocol (ICMP).
        # - **TCP**: Transmission Control Protocol (TCP).
        # - **UDP**: User Datagram Protocol (UDP).
        self.protocol = protocol
        # The source CIDR block of the network traffic for the inbound rule.
        self.source_cidr_block = source_cidr_block
        # The source port range of the network traffic for the inbound rule. Valid values are **1** to **65535**. Separate the start port and the end port with a forward slash (/). Examples: **1/200** and **80/80**.
        # 
        # > If **IngressRules.N.Protocol** is set to **ALL** or **ICMP**, you do not need to specify this parameter, which indicates that all ports are allowed.
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

class CreateTrafficMirrorFilterRequestEgressRules(DaraModel):
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
        # - **accept**: collects network traffic.
        # - **drop**: does not collect network traffic.
        self.action = action
        # The destination CIDR block of the network traffic for the outbound rule.
        self.destination_cidr_block = destination_cidr_block
        # The destination port range of the network traffic for the outbound rule. Valid values are **1** to **65535**. Separate the start port and the end port with a forward slash (/). Examples: **1/200** and **80/80**. You cannot set this parameter only to **-1/-1**, which indicates that all ports are allowed.
        # 
        # > If **EgressRules.N.Protocol** is set to **ALL** or **ICMP**, you do not need to specify this parameter, which indicates that all ports are allowed.
        self.destination_port_range = destination_port_range
        # The IP version of the instance. Valid values:
        # 
        # - **IPv4**: IPv4.
        # - **IPv6**: IPv6.
        self.ip_version = ip_version
        # The priority of the outbound rule. A smaller value indicates a higher priority.
        # The maximum value of **N** is **10**, which indicates that you can configure up to 10 outbound rules for a filter.
        self.priority = priority
        # The protocol type of the network traffic to be mirrored for the outbound rule. Valid values:
        # 
        # - **ALL**: all protocols.
        # - **ICMP**: Internet Control Message Protocol (ICMP).
        # - **TCP**: Transmission Control Protocol (TCP).
        # - **UDP**: User Datagram Protocol (UDP).
        self.protocol = protocol
        # The source CIDR block of the network traffic for the outbound rule.
        self.source_cidr_block = source_cidr_block
        # The source port range of the network traffic for the outbound rule. Valid values are **1** to **65535**. Separate the start port and the end port with a forward slash (/). Examples: **1/200** and **80/80**. You cannot set this parameter only to **-1/-1**, which indicates that all ports are allowed.
        # 
        # > If **EgressRules.N.Protocol** is set to **ALL** or **ICMP**, you do not need to specify this parameter, which indicates that all ports are allowed.
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

