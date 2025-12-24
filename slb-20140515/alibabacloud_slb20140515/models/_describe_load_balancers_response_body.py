# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancersResponseBody(DaraModel):
    def __init__(
        self,
        load_balancers: main_models.DescribeLoadBalancersResponseBodyLoadBalancers = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array of CLB instances.
        self.load_balancers = load_balancers
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of instances returned.
        self.total_count = total_count

    def validate(self):
        if self.load_balancers:
            self.load_balancers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancers is not None:
            result['LoadBalancers'] = self.load_balancers.to_map()

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
        if m.get('LoadBalancers') is not None:
            temp_model = main_models.DescribeLoadBalancersResponseBodyLoadBalancers()
            self.load_balancers = temp_model.from_map(m.get('LoadBalancers'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLoadBalancersResponseBodyLoadBalancers(DaraModel):
    def __init__(
        self,
        load_balancer: List[main_models.DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancer] = None,
    ):
        self.load_balancer = load_balancer

    def validate(self):
        if self.load_balancer:
            for v1 in self.load_balancer:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LoadBalancer'] = []
        if self.load_balancer is not None:
            for k1 in self.load_balancer:
                result['LoadBalancer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancer = []
        if m.get('LoadBalancer') is not None:
            for k1 in m.get('LoadBalancer'):
                temp_model = main_models.DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancer()
                self.load_balancer.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancer(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_ipversion: str = None,
        address_type: str = None,
        bandwidth: int = None,
        create_time: str = None,
        create_time_stamp: int = None,
        delete_protection: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        internet_charge_type_alias: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_spec: str = None,
        load_balancer_status: str = None,
        master_zone_id: str = None,
        modification_protection_reason: str = None,
        modification_protection_status: str = None,
        network_type: str = None,
        pay_type: str = None,
        region_id: str = None,
        region_id_alias: str = None,
        resource_group_id: str = None,
        slave_zone_id: str = None,
        tags: main_models.DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancerTags = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The endpoint of the CLB instance.
        self.address = address
        # The IP version that is used by the CLB instance. Valid values: **ipv4** and **ipv6**.
        self.address_ipversion = address_ipversion
        # The network type of the CLB instance. Valid values:
        # 
        # *   **internet:** After an Internet-facing CLB instance is created, the system assigns a public IP address to the CLB instance. Then, the CLB instance can forward requests over the Internet.
        # *   **intranet:** After an internal-facing CLB instance is created, the system assigns a private IP address to the CLB instance. Then, the CLB instance can forward requests only over internal networks.
        self.address_type = address_type
        # The maximum bandwidth of the listener. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The time when the CLB instance was created. The time follows the `YYYY-MM-DDThh:mm:ssZ` format.
        self.create_time = create_time
        # The timestamp when the instance was created.
        self.create_time_stamp = create_time_stamp
        # Indicates whether deletion protection is enabled for the CLB instance. Valid values:
        # 
        # *   **on:** Deletion protection is enabled.
        # *   **off:** Deletion protection is disabled.
        self.delete_protection = delete_protection
        # The metering method of the CLB instance. Valid values:
        # 
        # *   **PayBySpec:** pay-by-specification.
        # *   **PayByCLCU:** pay-by-LCU.
        # 
        # >  This parameter takes effect only for accounts registered on the China site (aliyun.com) and when the **PayType** parameter is set to **PayOnDemand**.
        self.instance_charge_type = instance_charge_type
        # The metering method of the Internet-facing CLB instance. Valid values:
        # 
        # *   **3:** pay-by-bandwidth (**paybybandwidth**).
        # *   **4:** pay-by-data-transfer (**paybytraffic**).
        self.internet_charge_type = internet_charge_type
        # The metering method of Internet data transfer. Valid values:
        # 
        # *   **paybybandwidth:** pay-by-bandwidth.
        # *   **paybytraffic:** pay-by-data-transfer.
        self.internet_charge_type_alias = internet_charge_type_alias
        # The ID of the CLB instance.
        self.load_balancer_id = load_balancer_id
        # The name of the CLB instance.
        self.load_balancer_name = load_balancer_name
        # The specification of the CLB instance.
        # 
        # >  Pay-as-you-go CLB instances are not subject to specifications. **slb.lcu.elastic** is returned by default.
        self.load_balancer_spec = load_balancer_spec
        # The status of the CLB instance. Valid values:
        # 
        # *   **inactive:** The CLB instance is disabled. CLB instances in the inactive state do not forward traffic.
        # *   **active:** The CLB instance runs as expected. By default, newly created CLB instances are in the **active** state.
        # *   **locked:** The CLB instance is locked.
        self.load_balancer_status = load_balancer_status
        # The ID of the primary zone to which the CLB instance belongs.
        self.master_zone_id = master_zone_id
        # The reason why the configuration read-only mode was enabled. The reason must be 1 to 80 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The reason must start with a letter.
        # 
        # > This parameter takes effect only when you set the `ModificationProtectionStatus` parameter to **ConsoleProtection**.
        self.modification_protection_reason = modification_protection_reason
        # Indicates whether the configuration read-only mode is enabled for the CLB instance. Valid values:
        # 
        # *   **NonProtection:** The configuration read-only mode is disabled. In this case, you cannot specify the ModificationProtectionReason parameter. If you specify the `ModificationProtectionReason` parameter, the value is cleared.
        # *   **ConsoleProtection:** The configuration read-only mode is enabled.
        # 
        # >  If you set this parameter to **ConsoleProtection**, you cannot modify the configurations of the CLB instance in the CLB console. However, you can call API operations to modify the configurations of the CLB instance.
        self.modification_protection_status = modification_protection_status
        # The network type of the internal-facing CLB instance. Valid values:
        # 
        # *   **vpc**: VPC
        # *   **Classic**: classic network
        self.network_type = network_type
        # The billing method of the CLB instance.
        # 
        # *   **PayOnDemand** is returned, which indicates the pay-as-you-go billing method.
        self.pay_type = pay_type
        # The ID of the region where the CLB instance was deployed.
        self.region_id = region_id
        # The region where the CLB instance was deployed.
        self.region_id_alias = region_id_alias
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the secondary zone to which the CLB instance belongs.
        self.slave_zone_id = slave_zone_id
        # The tags.
        self.tags = tags
        # The ID of the vSwitch to which the internal-facing CLB instance belongs.
        self.v_switch_id = v_switch_id
        # The ID of the VPC in which the internal-facing CLB instance was deployed.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tags:
            self.tags.validate()

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

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp

        if self.delete_protection is not None:
            result['DeleteProtection'] = self.delete_protection

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.internet_charge_type_alias is not None:
            result['InternetChargeTypeAlias'] = self.internet_charge_type_alias

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id

        if self.modification_protection_reason is not None:
            result['ModificationProtectionReason'] = self.modification_protection_reason

        if self.modification_protection_status is not None:
            result['ModificationProtectionStatus'] = self.modification_protection_status

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_id_alias is not None:
            result['RegionIdAlias'] = self.region_id_alias

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.slave_zone_id is not None:
            result['SlaveZoneId'] = self.slave_zone_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

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

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')

        if m.get('DeleteProtection') is not None:
            self.delete_protection = m.get('DeleteProtection')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('InternetChargeTypeAlias') is not None:
            self.internet_charge_type_alias = m.get('InternetChargeTypeAlias')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')

        if m.get('ModificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('ModificationProtectionReason')

        if m.get('ModificationProtectionStatus') is not None:
            self.modification_protection_status = m.get('ModificationProtectionStatus')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionIdAlias') is not None:
            self.region_id_alias = m.get('RegionIdAlias')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SlaveZoneId') is not None:
            self.slave_zone_id = m.get('SlaveZoneId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancerTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancerTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancerTagsTag] = None,
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
                temp_model = main_models.DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancerTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancerTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

