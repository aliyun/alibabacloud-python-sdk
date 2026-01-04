# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVSwitchAttributesResponseBody(DaraModel):
    def __init__(
        self,
        available_ip_address_count: int = None,
        cidr_block: str = None,
        creation_time: str = None,
        description: str = None,
        enabled_ipv_6: bool = None,
        ipv_6cidr_block: str = None,
        is_default: bool = None,
        network_acl_id: str = None,
        owner_id: int = None,
        request_id: str = None,
        resource_group_id: str = None,
        route_table: main_models.DescribeVSwitchAttributesResponseBodyRouteTable = None,
        share_type: str = None,
        status: str = None,
        tags: main_models.DescribeVSwitchAttributesResponseBodyTags = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The number of available IP addresses.
        self.available_ip_address_count = available_ip_address_count
        # The CIDR block of the vSwitch.
        self.cidr_block = cidr_block
        # The time when the vSwitch was created.
        self.creation_time = creation_time
        # The description of the vSwitch.
        self.description = description
        # Indicates whether IPv6 is enabled for the vSwitch. If you enable IPv6, you must configure the IPv6 CIDR block of the vSwitch. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enabled_ipv_6 = enabled_ipv_6
        # The IPv6 CIDR block of the vSwitch.
        self.ipv_6cidr_block = ipv_6cidr_block
        # Indicates whether the vSwitch is the default vSwitch. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_default = is_default
        # The network access control list (ACL) rules.
        self.network_acl_id = network_acl_id
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.owner_id = owner_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the ACL belongs.
        self.resource_group_id = resource_group_id
        # The information about the route table that is associated with the vSwitch.
        self.route_table = route_table
        # Indicates whether the vSwitch is shared.
        # 
        # *   If no value is returned, the vSwitch is a regular vSwitch.
        # *   If **Shared** is returned, the vSwitch is shared.
        # *   If **Sharing** is returned, the vSwitch is being shared.
        self.share_type = share_type
        # The status of the vSwitch. Valid values:
        # 
        # *   **Pending**
        # *   **Available**
        self.status = status
        # The information about the tags.
        self.tags = tags
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The vSwitch name.
        self.v_switch_name = v_switch_name
        # The ID of the VPC to which the vSwitch belongs.
        self.vpc_id = vpc_id
        # The ID of the zone to which the vSwitch belongs.
        self.zone_id = zone_id

    def validate(self):
        if self.route_table:
            self.route_table.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled_ipv_6 is not None:
            result['EnabledIpv6'] = self.enabled_ipv_6

        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.network_acl_id is not None:
            result['NetworkAclId'] = self.network_acl_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_table is not None:
            result['RouteTable'] = self.route_table.to_map()

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnabledIpv6') is not None:
            self.enabled_ipv_6 = m.get('EnabledIpv6')

        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('NetworkAclId') is not None:
            self.network_acl_id = m.get('NetworkAclId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouteTable') is not None:
            temp_model = main_models.DescribeVSwitchAttributesResponseBodyRouteTable()
            self.route_table = temp_model.from_map(m.get('RouteTable'))

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeVSwitchAttributesResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeVSwitchAttributesResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeVSwitchAttributesResponseBodyTagsTag] = None,
    ):
        self.tag = tag

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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeVSwitchAttributesResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeVSwitchAttributesResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N added to the resource.
        self.key = key
        # The value of tag N added to the resource.
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

class DescribeVSwitchAttributesResponseBodyRouteTable(DaraModel):
    def __init__(
        self,
        route_table_id: str = None,
        route_table_type: str = None,
    ):
        # The ID of the route table that is associated with the vSwitch.
        self.route_table_id = route_table_id
        # The type of the route table. Valid values:
        # 
        # *   **System**
        # *   **Custom**
        self.route_table_type = route_table_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.route_table_type is not None:
            result['RouteTableType'] = self.route_table_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('RouteTableType') is not None:
            self.route_table_type = m.get('RouteTableType')

        return self

