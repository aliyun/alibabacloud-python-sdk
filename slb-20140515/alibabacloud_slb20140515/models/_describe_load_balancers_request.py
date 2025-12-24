# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancersRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_ipversion: str = None,
        address_type: str = None,
        internet_charge_type: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_status: str = None,
        master_zone_id: str = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        pay_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        server_id: str = None,
        server_intranet_address: str = None,
        slave_zone_id: str = None,
        tag: List[main_models.DescribeLoadBalancersRequestTag] = None,
        tags: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The IP address that the CLB instance uses to provide services.
        self.address = address
        # The IP version that is used by the CLB instance. Valid values: **ipv4** and **ipv6**.
        self.address_ipversion = address_ipversion
        # The network type of the CLB instance. Valid values:
        # 
        # *   **internet:** After an Internet-facing CLB instance is created, the system assigns a public IP address to the CLB instance. Then, the CLB instance can forward requests over the Internet.
        # *   **intranet:** After an internal-facing CLB instance is created, the system assigns a private IP address to the CLB instance. Then, the CLB instance can forward requests only over internal networks.
        self.address_type = address_type
        # The metering method of Internet data transfer. Valid values:
        # 
        # *   **paybybandwidth:** pay-by-bandwidth.
        # *   **paybytraffic:** pay-by-data-transfer.
        self.internet_charge_type = internet_charge_type
        # The ID of the CLB instance.
        # 
        # You can specify up to 10 IDs. Separate multiple IDs with commas (,).
        self.load_balancer_id = load_balancer_id
        # The name of the CLB instance.
        # 
        # The name must be 1 to 80 characters in length, and can contain digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        # 
        # You can specify up to 10 names. Separate multiple names with commas (,).
        self.load_balancer_name = load_balancer_name
        # The status of the CLB instance. Valid values:
        # 
        # *   **inactive:** The CLB instance is disabled. CLB instances in the inactive state do not forward traffic.
        # *   **active:** The CLB instance runs as expected. By default, newly created CLB instances are in the **active** state.
        # *   **locked:** The CLB instance is locked. After a CLB instance expires, it is locked for seven days. A locked CLB instance cannot forward traffic and you cannot perform operations on the locked CLB instance. However, other settings such as the IP address are retained.
        self.load_balancer_status = load_balancer_status
        # The ID of the primary zone to which the CLB instance belongs.
        self.master_zone_id = master_zone_id
        # The network type of the internal-facing CLB instance. Valid values:
        # 
        # *   **vpc**: VPC
        # *   **Classic**: classic network
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: **1** to **100**.
        # 
        # >  If you specify the **PageSize** parameter, you must also specify the **PageNumber** parameter.
        self.page_size = page_size
        # The billing method of the CLB instance. Valid values:
        # 
        # *   Set the value to **PayOnDemand**.
        self.pay_type = pay_type
        # The ID of the region where the CLB instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/2401682.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the backend server that is added to the CLB instance.
        self.server_id = server_id
        # The private IP address of the backend server that is added to the CLB instance.
        # 
        # You can specify multiple IP addresses. Separate multiple IP addresses with commas (,).
        self.server_intranet_address = server_intranet_address
        # The ID of the secondary zone to which the CLB instance belongs.
        # 
        # CLB instances on Alibaba Finance Cloud do not support cross-zone deployment.
        self.slave_zone_id = slave_zone_id
        # The tags.
        self.tag = tag
        # The tags that are added to the CLB instance. The tags must be key-value pairs that are contained in a JSON dictionary.
        # 
        # You can specify up to 10 tags in each call.
        self.tags = tags
        # The ID of the vSwitch to which the CLB instance belongs.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC) to which the CLB instance belongs.
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
        if self.address is not None:
            result['Address'] = self.address

        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id

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

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.server_intranet_address is not None:
            result['ServerIntranetAddress'] = self.server_intranet_address

        if self.slave_zone_id is not None:
            result['SlaveZoneId'] = self.slave_zone_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')

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

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('ServerIntranetAddress') is not None:
            self.server_intranet_address = m.get('ServerIntranetAddress')

        if m.get('SlaveZoneId') is not None:
            self.slave_zone_id = m.get('SlaveZoneId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeLoadBalancersRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeLoadBalancersRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key must be 1 to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be at most 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
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

