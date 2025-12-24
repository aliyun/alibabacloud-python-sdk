# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeBandwidthPackagesResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth_packages: main_models.DescribeBandwidthPackagesResponseBodyBandwidthPackages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.bandwidth_packages = bandwidth_packages
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.bandwidth_packages:
            self.bandwidth_packages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_packages is not None:
            result['BandwidthPackages'] = self.bandwidth_packages.to_map()

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
        if m.get('BandwidthPackages') is not None:
            temp_model = main_models.DescribeBandwidthPackagesResponseBodyBandwidthPackages()
            self.bandwidth_packages = temp_model.from_map(m.get('BandwidthPackages'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBandwidthPackagesResponseBodyBandwidthPackages(DaraModel):
    def __init__(
        self,
        bandwidth_package: List[main_models.DescribeBandwidthPackagesResponseBodyBandwidthPackagesBandwidthPackage] = None,
    ):
        self.bandwidth_package = bandwidth_package

    def validate(self):
        if self.bandwidth_package:
            for v1 in self.bandwidth_package:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BandwidthPackage'] = []
        if self.bandwidth_package is not None:
            for k1 in self.bandwidth_package:
                result['BandwidthPackage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bandwidth_package = []
        if m.get('BandwidthPackage') is not None:
            for k1 in m.get('BandwidthPackage'):
                temp_model = main_models.DescribeBandwidthPackagesResponseBodyBandwidthPackagesBandwidthPackage()
                self.bandwidth_package.append(temp_model.from_map(k1))

        return self

class DescribeBandwidthPackagesResponseBodyBandwidthPackagesBandwidthPackage(DaraModel):
    def __init__(
        self,
        bandwidth: str = None,
        bandwidth_package_id: str = None,
        business_status: str = None,
        creation_time: str = None,
        description: str = None,
        isp: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        ip_count: str = None,
        name: str = None,
        nat_gateway_id: str = None,
        public_ip_addresses: main_models.DescribeBandwidthPackagesResponseBodyBandwidthPackagesBandwidthPackagePublicIpAddresses = None,
        region_id: str = None,
        status: str = None,
        zone_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.bandwidth_package_id = bandwidth_package_id
        self.business_status = business_status
        self.creation_time = creation_time
        self.description = description
        self.isp = isp
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type
        self.ip_count = ip_count
        self.name = name
        self.nat_gateway_id = nat_gateway_id
        self.public_ip_addresses = public_ip_addresses
        self.region_id = region_id
        self.status = status
        self.zone_id = zone_id

    def validate(self):
        if self.public_ip_addresses:
            self.public_ip_addresses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.isp is not None:
            result['ISP'] = self.isp

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ip_count is not None:
            result['IpCount'] = self.ip_count

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.public_ip_addresses is not None:
            result['PublicIpAddresses'] = self.public_ip_addresses.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('PublicIpAddresses') is not None:
            temp_model = main_models.DescribeBandwidthPackagesResponseBodyBandwidthPackagesBandwidthPackagePublicIpAddresses()
            self.public_ip_addresses = temp_model.from_map(m.get('PublicIpAddresses'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeBandwidthPackagesResponseBodyBandwidthPackagesBandwidthPackagePublicIpAddresses(DaraModel):
    def __init__(
        self,
        public_ip_addresse: List[main_models.DescribeBandwidthPackagesResponseBodyBandwidthPackagesBandwidthPackagePublicIpAddressesPublicIpAddresse] = None,
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
                temp_model = main_models.DescribeBandwidthPackagesResponseBodyBandwidthPackagesBandwidthPackagePublicIpAddressesPublicIpAddresse()
                self.public_ip_addresse.append(temp_model.from_map(k1))

        return self

class DescribeBandwidthPackagesResponseBodyBandwidthPackagesBandwidthPackagePublicIpAddressesPublicIpAddresse(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        ip_address: str = None,
    ):
        self.allocation_id = allocation_id
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

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        return self

