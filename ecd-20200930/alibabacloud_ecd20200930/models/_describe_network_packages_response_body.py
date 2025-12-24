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
        # The premium bandwidth plans.
        self.network_packages = network_packages
        # The token that is used to start the next query. If the value of this parameter is empty, all results are returned.
        self.next_token = next_token
        # The ID of the request.
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
    ):
        # The bandwidth provided by the premium bandwidth plan. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The business status.
        # 
        # Valid values:
        # 
        # *   Expired
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Normal
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.business_status = business_status
        # The time when the premium bandwidth plan was created.
        self.create_time = create_time
        # The public egress IP address of the premium bandwidth plan.
        self.eip_addresses = eip_addresses
        # The time when the premium bandwidth plan expires.
        # 
        # *   If the plan is a subscription one, the time when the plan expires is returned.
        # *   If the plan is a pay-as-you-go one, `2099-12-31T15:59:59Z` is returned.
        self.expired_time = expired_time
        # The charge type of the premium bandwidth plan.
        # 
        # *   Valid value when the `PayType` parameter is set to `PrePaid`:
        # 
        #     *   PayByBandwidth: charges by fixed bandwidth.
        # 
        # *   Valid values when the `PayType` parameter is set to `PostPaid`:
        # 
        #     *   PayByTraffic: charges by data transfer.
        #     *   PayByBandwidth: charges by fixed bandwidth.
        self.internet_charge_type = internet_charge_type
        # The ID of the premium bandwidth plan.
        self.network_package_id = network_package_id
        # The status of the premium bandwidth plan.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Released
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   InUse
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Releasing
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.network_package_status = network_package_status
        # The office network ID.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name
        # The type of the office network.
        # 
        # Valid values:
        # 
        # *   standard: advanced office network
        # *   customized: custom office network
        # *   basic: basic office network
        self.office_site_vpc_type = office_site_vpc_type
        # The billing method of the premium bandwidth plan.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go
        # *   PrePaid: subscription
        self.pay_type = pay_type
        # The time when the reserved network bandwidth took effect.
        self.reservation_active_time = reservation_active_time
        # The peak bandwidth that is reserved for the premium bandwidth plan. Unit: Mbit/s.
        self.reservation_bandwidth = reservation_bandwidth
        # The billing method of the reserved network bandwidth.
        # 
        # Valid values:
        # 
        # *   PayByTraffic: charges by data transfer.
        # 
        # *   PayByBandwidth: charges by fixed bandwidth.
        self.reservation_internet_charge_type = reservation_internet_charge_type

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

        return self

