# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeCommonBandwidthPackagesResponseBody(DaraModel):
    def __init__(
        self,
        common_bandwidth_packages: main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the Internet Shared Bandwidth instance.
        self.common_bandwidth_packages = common_bandwidth_packages
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.common_bandwidth_packages:
            self.common_bandwidth_packages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_bandwidth_packages is not None:
            result['CommonBandwidthPackages'] = self.common_bandwidth_packages.to_map()

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
        if m.get('CommonBandwidthPackages') is not None:
            temp_model = main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackages()
            self.common_bandwidth_packages = temp_model.from_map(m.get('CommonBandwidthPackages'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackages(DaraModel):
    def __init__(
        self,
        common_bandwidth_package: List[main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackage] = None,
    ):
        self.common_bandwidth_package = common_bandwidth_package

    def validate(self):
        if self.common_bandwidth_package:
            for v1 in self.common_bandwidth_package:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommonBandwidthPackage'] = []
        if self.common_bandwidth_package is not None:
            for k1 in self.common_bandwidth_package:
                result['CommonBandwidthPackage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_bandwidth_package = []
        if m.get('CommonBandwidthPackage') is not None:
            for k1 in m.get('CommonBandwidthPackage'):
                temp_model = main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackage()
                self.common_bandwidth_package.append(temp_model.from_map(k1))

        return self

class DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackage(DaraModel):
    def __init__(
        self,
        bandwidth: str = None,
        bandwidth_package_id: str = None,
        biz_type: str = None,
        business_status: str = None,
        creation_time: str = None,
        deletion_protection: bool = None,
        description: str = None,
        expired_time: str = None,
        has_reservation_data: str = None,
        isp: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        name: str = None,
        public_ip_addresses: main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackagePublicIpAddresses = None,
        ratio: int = None,
        region_id: str = None,
        reservation_active_time: str = None,
        reservation_bandwidth: str = None,
        reservation_internet_charge_type: str = None,
        reservation_order_type: str = None,
        resource_group_id: str = None,
        security_protection_types: main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackageSecurityProtectionTypes = None,
        service_managed: int = None,
        status: str = None,
        tags: main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackageTags = None,
        zone: str = None,
    ):
        # The maximum bandwidth of the Internet Shared Bandwidth instance. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The ID of the Internet Shared Bandwidth instance.
        self.bandwidth_package_id = bandwidth_package_id
        # The service type of the Internet Shared Bandwidth instance. Valid values:
        # 
        # *   **CloudBox** The cloud box. Only cloud box users can select this type.
        # *   **Default** (default): The general service type.
        self.biz_type = biz_type
        # The service status of the Internet Shared Bandwidth instance. Valid values:
        # 
        # *   **Normal**: The Internet Shared Bandwidth instance runs as expected.
        # *   **FinancialLocked**: An overdue payment occurs in the Internet Shared Bandwidth instance
        # *   **Unactivated**: The Internet Shared Bandwidth instance is not activated.
        self.business_status = business_status
        # The time when the Internet Shared Bandwidth instance was created. The time is displayed in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.creation_time = creation_time
        # Indicates whether deletion protection is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.deletion_protection = deletion_protection
        # The description of the Internet Shared Bandwidth instance.
        self.description = description
        # The time when the Internet Shared Bandwidth instance expired. The time is displayed in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.expired_time = expired_time
        # Indicates whether the information about pending orders is returned. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.has_reservation_data = has_reservation_data
        # The line type. Valid values:
        # 
        # *   **BGP**: BGP (Multi-ISP) line The BGP (Multi-ISP) line is supported in all regions.
        # *   **BGP_PRO**: BGP (Multi-ISP) Pro line The BGP (Multi-ISP) Pro line is supported in the China (Hong Kong), Singapore (Singapore), Japan (Tokyo), Philippines (Manila), Malaysia (Kuala Lumpur), Indonesia (Jakarta), and Thailand (Bangkok) regions.
        # 
        # If you are allowed to use single-ISP bandwidth, one of the following values is returned:
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
        # The billing method of the Internet Shared Bandwidth instance. Valid value:
        # 
        # **PostPaid**: pay-as-you-go
        self.instance_charge_type = instance_charge_type
        # The metering method of the Internet Shared Bandwidth instance. Valid value:
        # 
        # **PayByTraffic**
        self.internet_charge_type = internet_charge_type
        # The name of the Internet Shared Bandwidth instance.
        self.name = name
        # The elastic IP addresses (EIPs) that are associated with the Internet Shared Bandwidth instance.
        self.public_ip_addresses = public_ip_addresses
        # The percentage of the minimum bandwidth commitment. Only **20** is returned.
        # 
        # >  This parameter is supported only on the Alibaba Cloud China site.
        self.ratio = ratio
        # The ID of the region where the Internet Shared Bandwidth instance resides.
        self.region_id = region_id
        # The time when the renewal took effect. The time is displayed in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.reservation_active_time = reservation_active_time
        # The new maximum bandwidth after the configurations are changed. Unit: Mbit/s.
        self.reservation_bandwidth = reservation_bandwidth
        # The metering method after the configurations are changed. Valid value:
        # 
        # **PayByTraffic**
        self.reservation_internet_charge_type = reservation_internet_charge_type
        # The renewal method. Valid values:
        # 
        # *   **RENEWCHANGE**: renewal with a specification change
        # *   **TEMP_UPGRADE**: renewal with a temporary upgrade
        # *   **UPGRADE**: renewal with an upgrade
        self.reservation_order_type = reservation_order_type
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The editions of Anti-DDoS.
        # 
        # *   If this parameter is empty, Anti-DDoS Origin Basic is enabled.
        # *   If **AntiDDoS_Enhanced** is returned, Anti-DDoS Pro/Premium is enabled.
        self.security_protection_types = security_protection_types
        # Indicates whether the resource is created by the service account. Valid values:
        # 
        # *   **0**: The resource is not created by the service account.
        # *   **1**: The resource is created by the service account.
        self.service_managed = service_managed
        # The status of the Internet Shared Bandwidth instance. Valid values:
        # 
        # *   **Available**: The Internet Shared Bandwidth instance is available.
        # *   **Modifying**: The Internet Shared Bandwidth instance is being modified.
        self.status = status
        # The tag that is added to the Internet Shared Bandwidth instance.
        self.tags = tags
        # The zone of the Internet Shared Bandwidth instance. This parameter is returned only when BizType is set to CloudBox. If BizType is set to Default, an empty value is returned.
        self.zone = zone

    def validate(self):
        if self.public_ip_addresses:
            self.public_ip_addresses.validate()
        if self.security_protection_types:
            self.security_protection_types.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.has_reservation_data is not None:
            result['HasReservationData'] = self.has_reservation_data

        if self.isp is not None:
            result['ISP'] = self.isp

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.name is not None:
            result['Name'] = self.name

        if self.public_ip_addresses is not None:
            result['PublicIpAddresses'] = self.public_ip_addresses.to_map()

        if self.ratio is not None:
            result['Ratio'] = self.ratio

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

        if self.security_protection_types is not None:
            result['SecurityProtectionTypes'] = self.security_protection_types.to_map()

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('HasReservationData') is not None:
            self.has_reservation_data = m.get('HasReservationData')

        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PublicIpAddresses') is not None:
            temp_model = main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackagePublicIpAddresses()
            self.public_ip_addresses = temp_model.from_map(m.get('PublicIpAddresses'))

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

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

        if m.get('SecurityProtectionTypes') is not None:
            temp_model = main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackageSecurityProtectionTypes()
            self.security_protection_types = temp_model.from_map(m.get('SecurityProtectionTypes'))

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackageTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

class DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackageTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackageTagsTag] = None,
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
                temp_model = main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackageTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackageTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key that is added to the Internet Shared Bandwidth instance.
        self.key = key
        # The tag value that is added to the Internet Shared Bandwidth instance.
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

class DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackageSecurityProtectionTypes(DaraModel):
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

class DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackagePublicIpAddresses(DaraModel):
    def __init__(
        self,
        public_ip_addresse: List[main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackagePublicIpAddressesPublicIpAddresse] = None,
    ):
        self.public_ip_addresse = public_ip_addresse

    def validate(self):
        if self.public_ip_addresse:
            for v1 in self.public_ip_addresse:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PublicIpAddresse'] = []
        if self.public_ip_addresse is not None:
            for k1 in self.public_ip_addresse:
                result['PublicIpAddresse'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.public_ip_addresse = []
        if m.get('PublicIpAddresse') is not None:
            for k1 in m.get('PublicIpAddresse'):
                temp_model = main_models.DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackagePublicIpAddressesPublicIpAddresse()
                self.public_ip_addresse.append(temp_model.from_map(k1))

        return self

class DescribeCommonBandwidthPackagesResponseBodyCommonBandwidthPackagesCommonBandwidthPackagePublicIpAddressesPublicIpAddresse(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        bandwidth_package_ip_relation_status: str = None,
        ip_address: str = None,
    ):
        # The ID of the EIP.
        self.allocation_id = allocation_id
        # Indicates whether the EIP is associated with the Internet Shared Bandwidth instance. Valid values:
        # 
        # *   **BINDED**
        # *   **BINDING**
        self.bandwidth_package_ip_relation_status = bandwidth_package_ip_relation_status
        # The public IP address.
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.bandwidth_package_ip_relation_status is not None:
            result['BandwidthPackageIpRelationStatus'] = self.bandwidth_package_ip_relation_status

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('BandwidthPackageIpRelationStatus') is not None:
            self.bandwidth_package_ip_relation_status = m.get('BandwidthPackageIpRelationStatus')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        return self

