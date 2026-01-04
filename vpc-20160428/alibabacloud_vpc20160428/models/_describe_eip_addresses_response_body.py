# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeEipAddressesResponseBody(DaraModel):
    def __init__(
        self,
        eip_addresses: main_models.DescribeEipAddressesResponseBodyEipAddresses = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of the EIPs.
        self.eip_addresses = eip_addresses
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.eip_addresses:
            self.eip_addresses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses.to_map()

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
        if m.get('EipAddresses') is not None:
            temp_model = main_models.DescribeEipAddressesResponseBodyEipAddresses()
            self.eip_addresses = temp_model.from_map(m.get('EipAddresses'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEipAddressesResponseBodyEipAddresses(DaraModel):
    def __init__(
        self,
        eip_address: List[main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddress] = None,
    ):
        self.eip_address = eip_address

    def validate(self):
        if self.eip_address:
            for v1 in self.eip_address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EipAddress'] = []
        if self.eip_address is not None:
            for k1 in self.eip_address:
                result['EipAddress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_address = []
        if m.get('EipAddress') is not None:
            for k1 in m.get('EipAddress'):
                temp_model = main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddress()
                self.eip_address.append(temp_model.from_map(k1))

        return self

class DescribeEipAddressesResponseBodyEipAddressesEipAddress(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        allocation_time: str = None,
        bandwidth: str = None,
        bandwidth_package_bandwidth: str = None,
        bandwidth_package_id: str = None,
        bandwidth_package_type: str = None,
        biz_type: str = None,
        business_status: str = None,
        charge_type: str = None,
        deletion_protection: bool = None,
        description: str = None,
        eip_bandwidth: str = None,
        expired_time: str = None,
        hdmonitor_status: str = None,
        has_reservation_data: str = None,
        isp: str = None,
        instance_id: str = None,
        instance_region_id: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        ip_address: str = None,
        mode: str = None,
        name: str = None,
        netmode: str = None,
        operation_locks: main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressOperationLocks = None,
        private_ip_address: str = None,
        public_ip_address_pool_id: str = None,
        region_id: str = None,
        reservation_active_time: str = None,
        reservation_bandwidth: str = None,
        reservation_internet_charge_type: str = None,
        reservation_order_type: str = None,
        resource_group_id: str = None,
        second_limited: bool = None,
        security_protection_types: main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressSecurityProtectionTypes = None,
        segment_instance_id: str = None,
        service_id: int = None,
        service_managed: int = None,
        status: str = None,
        tags: main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressTags = None,
        vpc_id: str = None,
        zone: str = None,
    ):
        # The ID of the EIP.
        self.allocation_id = allocation_id
        # The time when the EIP was created. The time follows the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.allocation_time = allocation_time
        # The maximum bandwidth of the EIP. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The maximum bandwidth of the Internet Shared Bandwidth instance with which the EIP is associated. Unit: Mbit/s.
        self.bandwidth_package_bandwidth = bandwidth_package_bandwidth
        # The ID of the Internet Shared Bandwidth instance.
        self.bandwidth_package_id = bandwidth_package_id
        # The type of the bandwidth. Only **CommonBandwidthPackage** may be returned, which indicates Internet Shared Bandwidth.
        self.bandwidth_package_type = bandwidth_package_type
        # The service type. Valid values:
        # 
        # *   **CloudBox** Only cloud box users can select this type.
        # *   **Default** (default)
        self.biz_type = biz_type
        # The service status of the EIP. Valid values:
        # 
        # *   **Normal**
        # *   **OperationLock**
        # *   **Unactivated**
        self.business_status = business_status
        # The billing method of the EIP. Valid values:
        # 
        # *   **PostPaid**: pay-as-you-go.
        # *   **PrePaid**: subscription.
        self.charge_type = charge_type
        # Indicates whether deletion protection is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.deletion_protection = deletion_protection
        # The description of the EIP.
        self.description = description
        # The maximum bandwidth of the EIP when it is not associated with an Internet Shared Bandwidth instance. Unit: Mbit/s.
        self.eip_bandwidth = eip_bandwidth
        # The time when the EIP expires. The time follows the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.expired_time = expired_time
        # Indicates whether fine-grained monitoring is enabled for the EIP. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.hdmonitor_status = hdmonitor_status
        # Indicates whether renewal data is included. Valid values:
        # 
        # *   **false**
        # *   **true** A value of **true** is returned only when **IncludeReservationData** is set to **true** and some orders have not taken effect.
        self.has_reservation_data = has_reservation_data
        # The line type. Valid values:
        # 
        # *   **BGP**: BGP (Multi-ISP). The BGP (Multi-ISP) line is supported in all regions.
        # *   **BGP_PRO**: BGP (Multi-ISP) Pro lines. BGP (Multi-ISP) Pro line is supported only in the China (Hong Kong), Singapore, Japan (Tokyo), Malaysia (Kuala Lumpur), Philippines (Manila), Indonesia (Jakarta), and Thailand (Bangkok) regions.
        # 
        # For more information about BGP (Multi-ISP) and BGP (Multi-ISP) Pro, see the [Line types](https://help.aliyun.com/document_detail/32321.html) section of the "What is EIP?" topic.
        # 
        # If you are allowed to use single-ISP bandwidth, one of the following values may be returned:
        # 
        # *   **ChinaTelecom**
        # *   **ChinaUnicom**
        # *   **ChinaMobile**
        # *   **ChinaTelecom_L2**
        # *   **ChinaUnicom_L2**
        # *   **ChinaMobile_L2**
        # 
        # If your services are deployed in China East 1 Finance, **BGP_FinanceCloud** is returned.
        self.isp = isp
        # The ID of the associated instance.
        self.instance_id = instance_id
        # The region ID of the associated instance.
        self.instance_region_id = instance_region_id
        # The type of the associated instance. Valid values:
        # 
        # *   **EcsInstance**: an ECS instance in a VPC.
        # *   **SlbInstance**: a CLB instance in a VPC.
        # *   **Nat**: a NAT gateway.
        # *   **HaVip**: an HAVIP.
        # *   **NetworkInterface**: a secondary ENI.
        # *   **IpAddress**: an IP address.
        self.instance_type = instance_type
        # The metering method of the EIP. Valid values:
        # 
        # *   **PayByBandwidth**
        # *   **PayByTraffic**
        self.internet_charge_type = internet_charge_type
        # The EIP.
        self.ip_address = ip_address
        # The association mode. Valid values:
        # - **NAT**: NAT mode
        # - **MULTI_BINDED**: multi-EIP-to-ENI mode
        # - **BINDED**: cut-through mode
        self.mode = mode
        # The name of the EIP.
        self.name = name
        # The network type. Only **public** may be returned.
        self.netmode = netmode
        # The details about the locked EIP.
        self.operation_locks = operation_locks
        # The private IP address of the secondary ENI with which the EIP is associated.
        self.private_ip_address = private_ip_address
        # The ID of the IP address pool to which the EIP belongs.
        self.public_ip_address_pool_id = public_ip_address_pool_id
        # The region ID of the EIP.
        self.region_id = region_id
        # The time when the renewal took effect. The time follows the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.reservation_active_time = reservation_active_time
        # The maximum bandwidth after the renewal takes effect. Unit: Mbit/s.
        self.reservation_bandwidth = reservation_bandwidth
        # The metering method that is used after the renewal takes effect. Valid values:
        # 
        # *   **PayByBandwidth**
        # *   **PayByTraffic**
        self.reservation_internet_charge_type = reservation_internet_charge_type
        # The type of the renewal order. Valid values:
        # 
        # *   **RENEWCHANGE**: renewal with an upgrade or a downgrade.
        # *   **TEMP_UPGRADE**: temporary upgrade.
        # *   **UPGRADE**: upgrade.
        self.reservation_order_type = reservation_order_type
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Indicates whether level-2 throttling is configured. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.second_limited = second_limited
        # The edition of Anti-DDoS.
        # 
        # *   If an empty value is returned, it indicates that Anti-DDoS Origin Basic is used.
        # *   If **AntiDDoS_Enhanced** is returned, it indicates that Anti-DDoS Pro/Premium is used.
        self.security_protection_types = security_protection_types
        # The ID of the contiguous EIP group.
        # 
        # This value is returned only when you query contiguous EIPs.
        self.segment_instance_id = segment_instance_id
        # The ID of the service provider to which the managed instance belongs.
        # > This is only valid when the ServiceManaged parameter is set to True.
        self.service_id = service_id
        # Indicates whether the instance is managed. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.service_managed = service_managed
        # The status of the EIP. Valid values:
        # 
        # *   **Associating**
        # *   **Unassociating**
        # *   **InUse**
        # *   **Available**
        # *   **Releasing**
        self.status = status
        # The tags of the EIP.
        self.tags = tags
        # The ID of the VPC in which an IPv4 gateway is created and that is deployed in the same region as the EIP.
        # 
        # When you associate an EIP with an IP address, the system can enable the IP address to access the Internet based on VPC route configurations.
        # 
        # >  This parameter is returned if the value of **InstanceType** is **IpAddress**. In this case, the EIP is associated with an IP address.
        self.vpc_id = vpc_id
        # The zone of the EIP.
        # 
        # This parameter is returned only when the service type is CloudBox.
        self.zone = zone

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()
        if self.security_protection_types:
            self.security_protection_types.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.allocation_time is not None:
            result['AllocationTime'] = self.allocation_time

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_package_bandwidth is not None:
            result['BandwidthPackageBandwidth'] = self.bandwidth_package_bandwidth

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.bandwidth_package_type is not None:
            result['BandwidthPackageType'] = self.bandwidth_package_type

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.description is not None:
            result['Description'] = self.description

        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.hdmonitor_status is not None:
            result['HDMonitorStatus'] = self.hdmonitor_status

        if self.has_reservation_data is not None:
            result['HasReservationData'] = self.has_reservation_data

        if self.isp is not None:
            result['ISP'] = self.isp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.netmode is not None:
            result['Netmode'] = self.netmode

        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.public_ip_address_pool_id is not None:
            result['PublicIpAddressPoolId'] = self.public_ip_address_pool_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reservation_active_time is not None:
            result['ReservationActiveTime'] = self.reservation_active_time

        if self.reservation_bandwidth is not None:
            result['ReservationBandwidth'] = self.reservation_bandwidth

        if self.reservation_internet_charge_type is not None:
            result['ReservationInternetChargeType'] = self.reservation_internet_charge_type

        if self.reservation_order_type is not None:
            result['ReservationOrderType'] = self.reservation_order_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.second_limited is not None:
            result['SecondLimited'] = self.second_limited

        if self.security_protection_types is not None:
            result['SecurityProtectionTypes'] = self.security_protection_types.to_map()

        if self.segment_instance_id is not None:
            result['SegmentInstanceId'] = self.segment_instance_id

        if self.service_id is not None:
            result['ServiceID'] = self.service_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('AllocationTime') is not None:
            self.allocation_time = m.get('AllocationTime')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthPackageBandwidth') is not None:
            self.bandwidth_package_bandwidth = m.get('BandwidthPackageBandwidth')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BandwidthPackageType') is not None:
            self.bandwidth_package_type = m.get('BandwidthPackageType')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('HDMonitorStatus') is not None:
            self.hdmonitor_status = m.get('HDMonitorStatus')

        if m.get('HasReservationData') is not None:
            self.has_reservation_data = m.get('HasReservationData')

        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Netmode') is not None:
            self.netmode = m.get('Netmode')

        if m.get('OperationLocks') is not None:
            temp_model = main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressOperationLocks()
            self.operation_locks = temp_model.from_map(m.get('OperationLocks'))

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('PublicIpAddressPoolId') is not None:
            self.public_ip_address_pool_id = m.get('PublicIpAddressPoolId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReservationActiveTime') is not None:
            self.reservation_active_time = m.get('ReservationActiveTime')

        if m.get('ReservationBandwidth') is not None:
            self.reservation_bandwidth = m.get('ReservationBandwidth')

        if m.get('ReservationInternetChargeType') is not None:
            self.reservation_internet_charge_type = m.get('ReservationInternetChargeType')

        if m.get('ReservationOrderType') is not None:
            self.reservation_order_type = m.get('ReservationOrderType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecondLimited') is not None:
            self.second_limited = m.get('SecondLimited')

        if m.get('SecurityProtectionTypes') is not None:
            temp_model = main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressSecurityProtectionTypes()
            self.security_protection_types = temp_model.from_map(m.get('SecurityProtectionTypes'))

        if m.get('SegmentInstanceId') is not None:
            self.segment_instance_id = m.get('SegmentInstanceId')

        if m.get('ServiceID') is not None:
            self.service_id = m.get('ServiceID')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

class DescribeEipAddressesResponseBodyEipAddressesEipAddressTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressTagsTag] = None,
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
                temp_model = main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeEipAddressesResponseBodyEipAddressesEipAddressTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the EIP.
        self.key = key
        # The tag value of the EIP.
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

class DescribeEipAddressesResponseBodyEipAddressesEipAddressSecurityProtectionTypes(DaraModel):
    def __init__(
        self,
        security_protection_type: List[str] = None,
    ):
        self.security_protection_type = security_protection_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_protection_type is not None:
            result['SecurityProtectionType'] = self.security_protection_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityProtectionType') is not None:
            self.security_protection_type = m.get('SecurityProtectionType')

        return self

class DescribeEipAddressesResponseBodyEipAddressesEipAddressOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: List[main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressOperationLocksLockReason] = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        if self.lock_reason:
            for v1 in self.lock_reason:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LockReason'] = []
        if self.lock_reason is not None:
            for k1 in self.lock_reason:
                result['LockReason'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lock_reason = []
        if m.get('LockReason') is not None:
            for k1 in m.get('LockReason'):
                temp_model = main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k1))

        return self

class DescribeEipAddressesResponseBodyEipAddressesEipAddressOperationLocksLockReason(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        # The reason why the EIP is locked. Valid values:
        # 
        # *   **financial**: The EIP is locked due to overdue payments.
        # *   **security**: The instance is locked for security purposes.
        # *   **sharedPool**: The shared IP address pool is locked due to overdue payments.
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        return self

