# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkPackagesResponseBody(DaraModel):
    def __init__(
        self,
        network_packages: List[main_models.DescribeNetworkPackagesResponseBodyNetworkPackages] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of premium Internet bandwidth plans.
        self.network_packages = network_packages
        # The token for the next query. If NextToken is empty, no more results exist.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.network_packages:
            for v1 in self.network_packages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkPackages'] = []
        if self.network_packages is not None:
            for k1 in self.network_packages:
                result['NetworkPackages'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_packages = []
        if m.get('NetworkPackages') is not None:
            for k1 in m.get('NetworkPackages'):
                temp_model = main_models.DescribeNetworkPackagesResponseBodyNetworkPackages()
                self.network_packages.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNetworkPackagesResponseBodyNetworkPackages(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        business_status: str = None,
        create_time: str = None,
        eip_addresses: List[str] = None,
        expired_time: str = None,
        internet_charge_type: str = None,
        network_package_id: str = None,
        network_package_status: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_vpc_type: str = None,
        pay_type: str = None,
        reservation_active_time: str = None,
        reservation_bandwidth: int = None,
        reservation_internet_charge_type: str = None,
        tags: List[main_models.DescribeNetworkPackagesResponseBodyNetworkPackagesTags] = None,
    ):
        # The bandwidth of the premium Internet bandwidth plan. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The business status.
        self.business_status = business_status
        # The creation time.
        self.create_time = create_time
        # The public egress IP address of the premium Internet bandwidth plan.
        self.eip_addresses = eip_addresses
        # The expiration time of the premium Internet bandwidth plan.
        # 
        # - If the plan uses the subscription billing method, the actual expiration time is returned.
        # - If the plan uses the pay-as-you-go billing method, `2099-12-31T15:59:59Z` is returned.
        self.expired_time = expired_time
        # The billing method of the premium Internet bandwidth plan.
        # 
        # - If the parameter `PayType` is set to `PrePaid`, valid values:
        #     - PayByBandwidth: pay-by-bandwidth.
        # - If the parameter `PayType` is set to `PostPaid`, valid values:
        #     - PayByTraffic: pay-by-data-transfer.
        #     - PayByBandwidth: pay-by-bandwidth.
        self.internet_charge_type = internet_charge_type
        # The ID of the premium Internet bandwidth plan.
        self.network_package_id = network_package_id
        # The status of the premium Internet bandwidth plan.
        self.network_package_status = network_package_status
        # The office network ID.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name
        # The office network type.
        self.office_site_vpc_type = office_site_vpc_type
        # The billing method.
        self.pay_type = pay_type
        # The effective period of the reserved network bandwidth.
        self.reservation_active_time = reservation_active_time
        # The peak reserved network bandwidth. Unit: Mbit/s.
        self.reservation_bandwidth = reservation_bandwidth
        # The billing method of the reserved network bandwidth.
        self.reservation_internet_charge_type = reservation_internet_charge_type
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id

        if self.network_package_status is not None:
            result['NetworkPackageStatus'] = self.network_package_status

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.office_site_vpc_type is not None:
            result['OfficeSiteVpcType'] = self.office_site_vpc_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.reservation_active_time is not None:
            result['ReservationActiveTime'] = self.reservation_active_time

        if self.reservation_bandwidth is not None:
            result['ReservationBandwidth'] = self.reservation_bandwidth

        if self.reservation_internet_charge_type is not None:
            result['ReservationInternetChargeType'] = self.reservation_internet_charge_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EipAddresses') is not None:
            self.eip_addresses = m.get('EipAddresses')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')

        if m.get('NetworkPackageStatus') is not None:
            self.network_package_status = m.get('NetworkPackageStatus')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('OfficeSiteVpcType') is not None:
            self.office_site_vpc_type = m.get('OfficeSiteVpcType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ReservationActiveTime') is not None:
            self.reservation_active_time = m.get('ReservationActiveTime')

        if m.get('ReservationBandwidth') is not None:
            self.reservation_bandwidth = m.get('ReservationBandwidth')

        if m.get('ReservationInternetChargeType') is not None:
            self.reservation_internet_charge_type = m.get('ReservationInternetChargeType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeNetworkPackagesResponseBodyNetworkPackagesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeNetworkPackagesResponseBodyNetworkPackagesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

