# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class CreateNetworkPathRequest(DaraModel):
    def __init__(
        self,
        network_path_description: str = None,
        network_path_name: str = None,
        protocol: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_id: str = None,
        source_ip_address: str = None,
        source_port: int = None,
        source_type: str = None,
        tag: List[main_models.CreateNetworkPathRequestTag] = None,
        target_id: str = None,
        target_ip_address: str = None,
        target_port: int = None,
        target_type: str = None,
    ):
        # The description of the network path.
        self.network_path_description = network_path_description
        # The name of the network path.
        # 
        # This parameter is required.
        self.network_path_name = network_path_name
        # The protocol type. Valid values:
        # 
        # *   **tcp**: Transmission Control Protocol (TCP)
        # *   **udp**: User Datagram Protocol (UDP)
        # *   **icmp**: Internet Control Message Protocol (ICMP)
        self.protocol = protocol
        # The region ID of the network path that you want to create.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the source resource.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The source IP address.
        self.source_ip_address = source_ip_address
        # The source port.
        self.source_port = source_port
        # The type of the source resource. Valid values:
        # 
        # *   **ecs**: the Elastic Compute Service (ECS) instance
        # *   **internetIp**: the public IP address
        # *   **vsw**: the vSwitch
        # *   **vpn**: the VPN gateway
        # *   **vbr**: the virtual border router (VBR)
        # 
        # This parameter is required.
        self.source_type = source_type
        # The tags to add to the resource.
        self.tag = tag
        # The ID of the destination resource.
        self.target_id = target_id
        # The destination IP address.
        self.target_ip_address = target_ip_address
        # The destination port.
        self.target_port = target_port
        # The type of the destination resource. Valid values:
        # 
        # *   **ecs**: the ECS instance
        # *   **internetIp**: the public IP address
        # *   **vsw**: the vSwitch
        # *   **vpn**: the VPN gateway
        # *   **vbr**: the VBR
        # *   **clb**: the Classic Load Balancer (CLB) instance
        self.target_type = target_type

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_path_description is not None:
            result['NetworkPathDescription'] = self.network_path_description

        if self.network_path_name is not None:
            result['NetworkPathName'] = self.network_path_name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_ip_address is not None:
            result['SourceIpAddress'] = self.source_ip_address

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_ip_address is not None:
            result['TargetIpAddress'] = self.target_ip_address

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPathDescription') is not None:
            self.network_path_description = m.get('NetworkPathDescription')

        if m.get('NetworkPathName') is not None:
            self.network_path_name = m.get('NetworkPathName')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceIpAddress') is not None:
            self.source_ip_address = m.get('SourceIpAddress')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateNetworkPathRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetIpAddress') is not None:
            self.target_ip_address = m.get('TargetIpAddress')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self



class CreateNetworkPathRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the resource. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        # 
        # You can add up to 20 tags in each call.
        self.key = key
        # The value of tag N to add to the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `aliyun` or `acs:`.
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

