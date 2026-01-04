# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeIpv6AddressesRequest(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        associated_instance_id: str = None,
        associated_instance_type: str = None,
        include_reservation_data: bool = None,
        ipv_6address: str = None,
        ipv_6address_id: str = None,
        ipv_6internet_bandwidth_id: str = None,
        name: str = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        service_managed: bool = None,
        tag: List[main_models.DescribeIpv6AddressesRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The type of IP address. Valid values:
        # 
        # - IPv6Address (default): indicates an IPv6 instance used to query a single IPv6 address.
        # 
        # - IPv6Prefix: indicates an IPv6 instance used to query prefix CIDR blocks.
        self.address_type = address_type
        # The ID of the instance that is assigned the IPv6 address.
        self.associated_instance_id = associated_instance_id
        # The type of instance associated with the IPv6 address. Valid values:
        # 
        # *   **EcsInstance**: Elastic Compute Service (ECS) instance in a virtual private cloud (VPC)
        # *   **NetworkInterface**: secondary elastic network interface (ENI)
        self.associated_instance_type = associated_instance_type
        # Specifies whether to return information about pending orders. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        self.include_reservation_data = include_reservation_data
        # The IPv6 address that you want to query.
        self.ipv_6address = ipv_6address
        # The ID of the IPv6 address that you want to query. You can enter at most 20 IPv6 address IDs in each API request. Separate IPv6 address IDs with commas (,).
        self.ipv_6address_id = ipv_6address_id
        # The ID of the Internet bandwidth that you purchased for the IPv6 address.
        self.ipv_6internet_bandwidth_id = ipv_6internet_bandwidth_id
        # The name of the IPv6 address that you want to query.
        # 
        # The name must be 0 to 128 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        # The type of communication supported by the IPv6 address. Valid values:
        # 
        # *   **Private**
        # *   **Public**
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the region in which you want to query IPv6 addresses. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the IPv6 gateway belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Indicates whether the instance is managed. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # If you do not specify this parameter, all instances are queried.
        self.service_managed = service_managed
        # The tag list.
        self.tag = tag
        # The ID of the vSwitch to which the IPv6 address belongs.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the IPv6 address belongs.
        self.vpc_id = vpc_id

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
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.associated_instance_id is not None:
            result['AssociatedInstanceId'] = self.associated_instance_id

        if self.associated_instance_type is not None:
            result['AssociatedInstanceType'] = self.associated_instance_type

        if self.include_reservation_data is not None:
            result['IncludeReservationData'] = self.include_reservation_data

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.ipv_6address_id is not None:
            result['Ipv6AddressId'] = self.ipv_6address_id

        if self.ipv_6internet_bandwidth_id is not None:
            result['Ipv6InternetBandwidthId'] = self.ipv_6internet_bandwidth_id

        if self.name is not None:
            result['Name'] = self.name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('AssociatedInstanceId') is not None:
            self.associated_instance_id = m.get('AssociatedInstanceId')

        if m.get('AssociatedInstanceType') is not None:
            self.associated_instance_type = m.get('AssociatedInstanceType')

        if m.get('IncludeReservationData') is not None:
            self.include_reservation_data = m.get('IncludeReservationData')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('Ipv6AddressId') is not None:
            self.ipv_6address_id = m.get('Ipv6AddressId')

        if m.get('Ipv6InternetBandwidthId') is not None:
            self.ipv_6internet_bandwidth_id = m.get('Ipv6InternetBandwidthId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeIpv6AddressesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeIpv6AddressesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        self.key = key
        # The value of tag N.
        # 
        # The tag value can be up to 128 characters in length. It can be an empty string. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        # 
        # Each tag key corresponds to one tag value. You can specify at most 20 tag values at a time.
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

