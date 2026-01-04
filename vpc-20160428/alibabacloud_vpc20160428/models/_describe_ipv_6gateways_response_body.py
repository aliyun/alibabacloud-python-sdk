# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeIpv6GatewaysResponseBody(DaraModel):
    def __init__(
        self,
        ipv_6gateways: main_models.DescribeIpv6GatewaysResponseBodyIpv6Gateways = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the IPv6 gateway.
        self.ipv_6gateways = ipv_6gateways
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipv_6gateways:
            self.ipv_6gateways.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6gateways is not None:
            result['Ipv6Gateways'] = self.ipv_6gateways.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Gateways') is not None:
            temp_model = main_models.DescribeIpv6GatewaysResponseBodyIpv6Gateways()
            self.ipv_6gateways = temp_model.from_map(m.get('Ipv6Gateways'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeIpv6GatewaysResponseBodyIpv6Gateways(DaraModel):
    def __init__(
        self,
        ipv_6gateway: List[main_models.DescribeIpv6GatewaysResponseBodyIpv6GatewaysIpv6Gateway] = None,
    ):
        self.ipv_6gateway = ipv_6gateway

    def validate(self):
        if self.ipv_6gateway:
            for v1 in self.ipv_6gateway:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6Gateway'] = []
        if self.ipv_6gateway is not None:
            for k1 in self.ipv_6gateway:
                result['Ipv6Gateway'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6gateway = []
        if m.get('Ipv6Gateway') is not None:
            for k1 in m.get('Ipv6Gateway'):
                temp_model = main_models.DescribeIpv6GatewaysResponseBodyIpv6GatewaysIpv6Gateway()
                self.ipv_6gateway.append(temp_model.from_map(k1))

        return self

class DescribeIpv6GatewaysResponseBodyIpv6GatewaysIpv6Gateway(DaraModel):
    def __init__(
        self,
        business_status: str = None,
        creation_time: str = None,
        description: str = None,
        expired_time: str = None,
        instance_charge_type: str = None,
        ipv_6gateway_id: str = None,
        name: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: main_models.DescribeIpv6GatewaysResponseBodyIpv6GatewaysIpv6GatewayTags = None,
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
        # The billing method of the IPv6 gateway.
        # 
        # Only **PostPaid** may be returned, which indicates that the IPv6 gateway uses the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        # The ID of the IPv6 gateway.
        self.ipv_6gateway_id = ipv_6gateway_id
        # The name of the IPv6 gateway.
        self.name = name
        self.owner_id = owner_id
        # The ID of the region in which the IPv6 gateway is deployed.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The status of the IPv6 gateway. Valid values:
        # 
        # *   **Pending**
        # *   **Available**
        self.status = status
        # The information about the tags.
        self.tags = tags
        # The ID of the VPC to which the IPv6 gateway belongs.
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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeIpv6GatewaysResponseBodyIpv6GatewaysIpv6GatewayTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeIpv6GatewaysResponseBodyIpv6GatewaysIpv6GatewayTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeIpv6GatewaysResponseBodyIpv6GatewaysIpv6GatewayTagsTag] = None,
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
                temp_model = main_models.DescribeIpv6GatewaysResponseBodyIpv6GatewaysIpv6GatewayTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeIpv6GatewaysResponseBodyIpv6GatewaysIpv6GatewayTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

