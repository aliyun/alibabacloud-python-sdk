# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeIpv6GatewayAttributeResponseBody(DaraModel):
    def __init__(
        self,
        business_status: str = None,
        creation_time: str = None,
        description: str = None,
        expired_time: str = None,
        gateway_route_table_id: str = None,
        instance_charge_type: str = None,
        ipv_6gateway_id: str = None,
        name: str = None,
        owner_id: int = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: main_models.DescribeIpv6GatewayAttributeResponseBodyTags = None,
        vpc_id: str = None,
    ):
        # The status of the IPv6 gateway. Valid values:
        # 
        # *   **Normal**
        # *   **FinancialLocked**
        # *   **SecurityLocked**
        self.business_status = business_status
        # The time when the IPv6 gateway was created.
        self.creation_time = creation_time
        # The description of the IPv6 gateway.
        self.description = description
        # The time when the IPv6 gateway expires.
        self.expired_time = expired_time
        # The ID of the gateway route table associated with the IPv6 gateway.
        # 
        # >  This parameter is available only when the IPv6 gateway is associated with a gateway route table.
        self.gateway_route_table_id = gateway_route_table_id
        # The metering method of the IPv6 gateway.
        self.instance_charge_type = instance_charge_type
        # The ID of the IPv6 gateway.
        self.ipv_6gateway_id = ipv_6gateway_id
        # The name of the IPv6 gateway.
        self.name = name
        # The ID of the Alibaba Cloud account to which the IPv6 gateway belongs.
        # 
        # >  This value is of the Long type. In some languages, the precision may be lost. Use this value with caution.
        self.owner_id = owner_id
        # The ID of the region where the IPv6 gateway is deployed.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the IPv6 gateway. Valid values:
        # 
        # *   **Pending**
        # *   **Available**
        self.status = status
        # The information about the tags.
        self.tags = tags
        # The ID of the virtual private cloud (VPC) to which the IPv6 gateway belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.gateway_route_table_id is not None:
            result['GatewayRouteTableId'] = self.gateway_route_table_id

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.ipv_6gateway_id is not None:
            result['Ipv6GatewayId'] = self.ipv_6gateway_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('GatewayRouteTableId') is not None:
            self.gateway_route_table_id = m.get('GatewayRouteTableId')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('Ipv6GatewayId') is not None:
            self.ipv_6gateway_id = m.get('Ipv6GatewayId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeIpv6GatewayAttributeResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeIpv6GatewayAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeIpv6GatewayAttributeResponseBodyTagsTag] = None,
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
                temp_model = main_models.DescribeIpv6GatewayAttributeResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeIpv6GatewayAttributeResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length. It must start with a letter and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The value of tag N. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length. It must start with a letter and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

