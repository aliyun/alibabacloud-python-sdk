# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeIpv6AddressesResponseBody(DaraModel):
    def __init__(
        self,
        ipv_6addresses: main_models.DescribeIpv6AddressesResponseBodyIpv6Addresses = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the IPv6 address.
        self.ipv_6addresses = ipv_6addresses
        # The page number of the returned page. Default value: **1**.
        self.page_number = page_number
        # The number of entries returned per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.ipv_6addresses:
            self.ipv_6addresses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6addresses is not None:
            result['Ipv6Addresses'] = self.ipv_6addresses.to_map()

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
        if m.get('Ipv6Addresses') is not None:
            temp_model = main_models.DescribeIpv6AddressesResponseBodyIpv6Addresses()
            self.ipv_6addresses = temp_model.from_map(m.get('Ipv6Addresses'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeIpv6AddressesResponseBodyIpv6Addresses(DaraModel):
    def __init__(
        self,
        ipv_6address: List[main_models.DescribeIpv6AddressesResponseBodyIpv6AddressesIpv6Address] = None,
    ):
        self.ipv_6address = ipv_6address

    def validate(self):
        if self.ipv_6address:
            for v1 in self.ipv_6address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6Address'] = []
        if self.ipv_6address is not None:
            for k1 in self.ipv_6address:
                result['Ipv6Address'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6address = []
        if m.get('Ipv6Address') is not None:
            for k1 in m.get('Ipv6Address'):
                temp_model = main_models.DescribeIpv6AddressesResponseBodyIpv6AddressesIpv6Address()
                self.ipv_6address.append(temp_model.from_map(k1))

        return self

class DescribeIpv6AddressesResponseBodyIpv6AddressesIpv6Address(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        allocation_time: str = None,
        associated_instance_id: str = None,
        associated_instance_type: str = None,
        ipv_6address: str = None,
        ipv_6address_description: str = None,
        ipv_6address_id: str = None,
        ipv_6address_name: str = None,
        ipv_6gateway_id: str = None,
        ipv_6internet_bandwidth: main_models.DescribeIpv6AddressesResponseBodyIpv6AddressesIpv6AddressIpv6InternetBandwidth = None,
        ipv_6isp: str = None,
        network_type: str = None,
        real_bandwidth: int = None,
        resource_group_id: str = None,
        service_managed: int = None,
        status: str = None,
        tags: main_models.DescribeIpv6AddressesResponseBodyIpv6AddressesIpv6AddressTags = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The type of IPv6 address. Valid values:
        # 
        # *   IPv6Address (default): indicates a single IPv6 IP.
        # *   IPv6Prefix: indicates IPv6 CIDR.
        self.address_type = address_type
        # The time when the IPv6 address was created.
        self.allocation_time = allocation_time
        # The ID of the instance associated with the IPv6 address.
        self.associated_instance_id = associated_instance_id
        # The type of instance associated with the IPv6 address.
        self.associated_instance_type = associated_instance_type
        # The IPv6 address.
        self.ipv_6address = ipv_6address
        # The description of the IPv6 address.
        self.ipv_6address_description = ipv_6address_description
        # The ID of the IPv6 address.
        self.ipv_6address_id = ipv_6address_id
        # The name of the IPv6 address.
        self.ipv_6address_name = ipv_6address_name
        # The ID of the IPv6 gateway to which the IPv6 address belongs.
        self.ipv_6gateway_id = ipv_6gateway_id
        # The Internet bandwidth of the IPv6 address.
        self.ipv_6internet_bandwidth = ipv_6internet_bandwidth
        # The ISP of the IPv6 address. Valid values:
        # 
        # *   **BGP** (default)
        # *   **ChinaMobile**
        # *   **ChinaUnicom**
        # *   **ChinaTelecom**
        self.ipv_6isp = ipv_6isp
        # The type of connection supported by the IPv6 address. Valid values:
        # 
        # *   **Private**
        # *   **Public**
        self.network_type = network_type
        # The peak bandwidth of the IPv6 address.
        self.real_bandwidth = real_bandwidth
        # The ID of the resource group to which the IPv6 gateway belongs.
        self.resource_group_id = resource_group_id
        # Indicates whether the instance is managed. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.service_managed = service_managed
        # The status of the IPv6 address.
        # 
        # *   **Pending**
        # *   **Available**
        self.status = status
        # The tag list.
        self.tags = tags
        # The ID of the vSwitch to which the IPv6 address belongs.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the IPv6 address belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.ipv_6internet_bandwidth:
            self.ipv_6internet_bandwidth.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.allocation_time is not None:
            result['AllocationTime'] = self.allocation_time

        if self.associated_instance_id is not None:
            result['AssociatedInstanceId'] = self.associated_instance_id

        if self.associated_instance_type is not None:
            result['AssociatedInstanceType'] = self.associated_instance_type

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.ipv_6address_description is not None:
            result['Ipv6AddressDescription'] = self.ipv_6address_description

        if self.ipv_6address_id is not None:
            result['Ipv6AddressId'] = self.ipv_6address_id

        if self.ipv_6address_name is not None:
            result['Ipv6AddressName'] = self.ipv_6address_name

        if self.ipv_6gateway_id is not None:
            result['Ipv6GatewayId'] = self.ipv_6gateway_id

        if self.ipv_6internet_bandwidth is not None:
            result['Ipv6InternetBandwidth'] = self.ipv_6internet_bandwidth.to_map()

        if self.ipv_6isp is not None:
            result['Ipv6Isp'] = self.ipv_6isp

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.real_bandwidth is not None:
            result['RealBandwidth'] = self.real_bandwidth

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('AllocationTime') is not None:
            self.allocation_time = m.get('AllocationTime')

        if m.get('AssociatedInstanceId') is not None:
            self.associated_instance_id = m.get('AssociatedInstanceId')

        if m.get('AssociatedInstanceType') is not None:
            self.associated_instance_type = m.get('AssociatedInstanceType')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('Ipv6AddressDescription') is not None:
            self.ipv_6address_description = m.get('Ipv6AddressDescription')

        if m.get('Ipv6AddressId') is not None:
            self.ipv_6address_id = m.get('Ipv6AddressId')

        if m.get('Ipv6AddressName') is not None:
            self.ipv_6address_name = m.get('Ipv6AddressName')

        if m.get('Ipv6GatewayId') is not None:
            self.ipv_6gateway_id = m.get('Ipv6GatewayId')

        if m.get('Ipv6InternetBandwidth') is not None:
            temp_model = main_models.DescribeIpv6AddressesResponseBodyIpv6AddressesIpv6AddressIpv6InternetBandwidth()
            self.ipv_6internet_bandwidth = temp_model.from_map(m.get('Ipv6InternetBandwidth'))

        if m.get('Ipv6Isp') is not None:
            self.ipv_6isp = m.get('Ipv6Isp')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RealBandwidth') is not None:
            self.real_bandwidth = m.get('RealBandwidth')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeIpv6AddressesResponseBodyIpv6AddressesIpv6AddressTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeIpv6AddressesResponseBodyIpv6AddressesIpv6AddressTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeIpv6AddressesResponseBodyIpv6AddressesIpv6AddressTagsTag] = None,
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
                temp_model = main_models.DescribeIpv6AddressesResponseBodyIpv6AddressesIpv6AddressTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeIpv6AddressesResponseBodyIpv6AddressesIpv6AddressTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length. The tag key cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value.
        # 
        # The tag value can be up to 128 characters in length. It can be an empty string. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

class DescribeIpv6AddressesResponseBodyIpv6AddressesIpv6AddressIpv6InternetBandwidth(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        business_status: str = None,
        has_reservation_data: bool = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        ipv_6internet_bandwidth_id: str = None,
        reservation_active_time: str = None,
        reservation_bandwidth: int = None,
        reservation_internet_charge_type: str = None,
        reservation_order_type: str = None,
    ):
        # The dedicated Internet bandwidth of the IPv6 address. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The status of the Internet bandwidth of the IPv6 address. Valid values:
        # 
        # *   **Normal**
        # *   **FinancialLocked**
        # *   **SecurityLocked**
        self.business_status = business_status
        # Indicates whether renewal data is included. Valid values:
        # 
        # *   **false**
        # *   **true** **true** is returned only when **IncludeReservationData** is set to **true** and some orders have not taken effect.
        self.has_reservation_data = has_reservation_data
        # The billing method of the Internet bandwidth of the IPv6 address. Valid values:
        # 
        # Only **PostPaid** may be returned, which indicates the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        # The billing method of the Internet bandwidth of the IPv6 address. Valid values:
        # 
        # *   **PayByTraffic**
        # *   **PayByBandwidth**
        self.internet_charge_type = internet_charge_type
        # The Internet bandwidth ID of the IPv6 address.
        self.ipv_6internet_bandwidth_id = ipv_6internet_bandwidth_id
        # The time when the renewal takes effect. The time is displayed in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.reservation_active_time = reservation_active_time
        # The maximum bandwidth after the renewal takes effect. Unit: Mbit/s.
        self.reservation_bandwidth = reservation_bandwidth
        # The metering method that is used after the renewal takes effect.
        # 
        # *   **PayByTraffic**
        # *   **PayByBandwidth**
        self.reservation_internet_charge_type = reservation_internet_charge_type
        # The type of the renewal order. Only **RENEW** may be returned, which indicates that the order is placed for service renewal.
        self.reservation_order_type = reservation_order_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.has_reservation_data is not None:
            result['HasReservationData'] = self.has_reservation_data

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ipv_6internet_bandwidth_id is not None:
            result['Ipv6InternetBandwidthId'] = self.ipv_6internet_bandwidth_id

        if self.reservation_active_time is not None:
            result['ReservationActiveTime'] = self.reservation_active_time

        if self.reservation_bandwidth is not None:
            result['ReservationBandwidth'] = self.reservation_bandwidth

        if self.reservation_internet_charge_type is not None:
            result['ReservationInternetChargeType'] = self.reservation_internet_charge_type

        if self.reservation_order_type is not None:
            result['ReservationOrderType'] = self.reservation_order_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('HasReservationData') is not None:
            self.has_reservation_data = m.get('HasReservationData')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('Ipv6InternetBandwidthId') is not None:
            self.ipv_6internet_bandwidth_id = m.get('Ipv6InternetBandwidthId')

        if m.get('ReservationActiveTime') is not None:
            self.reservation_active_time = m.get('ReservationActiveTime')

        if m.get('ReservationBandwidth') is not None:
            self.reservation_bandwidth = m.get('ReservationBandwidth')

        if m.get('ReservationInternetChargeType') is not None:
            self.reservation_internet_charge_type = m.get('ReservationInternetChargeType')

        if m.get('ReservationOrderType') is not None:
            self.reservation_order_type = m.get('ReservationOrderType')

        return self

