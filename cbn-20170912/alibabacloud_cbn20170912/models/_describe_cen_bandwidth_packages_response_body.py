# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeCenBandwidthPackagesResponseBody(DaraModel):
    def __init__(
        self,
        cen_bandwidth_packages: main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details about the bandwidth plan.
        self.cen_bandwidth_packages = cen_bandwidth_packages
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cen_bandwidth_packages:
            self.cen_bandwidth_packages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_bandwidth_packages is not None:
            result['CenBandwidthPackages'] = self.cen_bandwidth_packages.to_map()

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
        if m.get('CenBandwidthPackages') is not None:
            temp_model = main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages()
            self.cen_bandwidth_packages = temp_model.from_map(m.get('CenBandwidthPackages'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages(DaraModel):
    def __init__(
        self,
        cen_bandwidth_package: List[main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackage] = None,
    ):
        self.cen_bandwidth_package = cen_bandwidth_package

    def validate(self):
        if self.cen_bandwidth_package:
            for v1 in self.cen_bandwidth_package:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CenBandwidthPackage'] = []
        if self.cen_bandwidth_package is not None:
            for k1 in self.cen_bandwidth_package:
                result['CenBandwidthPackage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_bandwidth_package = []
        if m.get('CenBandwidthPackage') is not None:
            for k1 in m.get('CenBandwidthPackage'):
                temp_model = main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackage()
                self.cen_bandwidth_package.append(temp_model.from_map(k1))

        return self

class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackage(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        bandwidth_package_charge_type: str = None,
        business_status: str = None,
        cen_bandwidth_package_id: str = None,
        cen_ids: main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageCenIds = None,
        creation_time: str = None,
        description: str = None,
        expired_time: str = None,
        geographic_region_aid: str = None,
        geographic_region_bid: str = None,
        geographic_span_id: str = None,
        has_reservation_data: str = None,
        is_cross_border: bool = None,
        name: str = None,
        orgin_inter_region_bandwidth_limits: main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimits = None,
        reservation_active_time: str = None,
        reservation_bandwidth: str = None,
        reservation_internet_charge_type: str = None,
        reservation_order_type: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageTags = None,
    ):
        # The maximum bandwidth of the bandwidth plan.
        self.bandwidth = bandwidth
        # The billing method of the bandwidth plan.
        self.bandwidth_package_charge_type = bandwidth_package_charge_type
        # The status of the bandwidth plan. Valid values:
        # 
        # *   **Normal**: running as expected.
        # *   **FinancialLocked**: locked due to overdue payments.
        # *   **SecurityLocked**: locked due to security reasons
        self.business_status = business_status
        # The ID of the bandwidth plan.
        self.cen_bandwidth_package_id = cen_bandwidth_package_id
        # A list of CEN instances that are associated with the bandwidth plan.
        self.cen_ids = cen_ids
        # The time when the bandwidth plan was created. The time is displayed in the ISO8601 standard in the YYYY-MM-DDThh:mmZ format.
        self.creation_time = creation_time
        # The description of the bandwidth plan.
        self.description = description
        # The time when the bandwidth plan expires.
        self.expired_time = expired_time
        # The ID of the area that you want to query. Valid values:
        # 
        # *   **china**: Chinese mainland.
        # *   **asia-pacific**: Asia Pacific
        # *   **europe**: Europe
        # *   **north-america**: North America
        self.geographic_region_aid = geographic_region_aid
        # The ID of the other area connected by the bandwidth plan. Valid values:
        # 
        # *   **china**: Chinese mainland.
        # *   **asia-pacific**: Asia Pacific
        # *   **europe**: Europe
        # *   **north-america**: North America
        self.geographic_region_bid = geographic_region_bid
        # The ID of the connected area.
        self.geographic_span_id = geographic_span_id
        # Indicates whether renewal data is included.
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter returns **true** only when the **IncludeReservationData** parameter is set to **true** and a pending order exists.
        self.has_reservation_data = has_reservation_data
        # Indicates whether the bandwidth plan supports cross-border communication.
        # 
        # *   **false**
        # *   **true**
        self.is_cross_border = is_cross_border
        # The name of the bandwidth plan.
        self.name = name
        # The details about the connected regions.
        self.orgin_inter_region_bandwidth_limits = orgin_inter_region_bandwidth_limits
        # The expiration time of the temporary upgrade.
        self.reservation_active_time = reservation_active_time
        # The bandwidth value to which the bandwidth plan is restored when the temporary upgrade ends.
        self.reservation_bandwidth = reservation_bandwidth
        # The new billing method.
        self.reservation_internet_charge_type = reservation_internet_charge_type
        # The renewal method.
        # 
        # *   **TEMP_UPGRADE**: temporary upgrade
        # *   **UPGRADE**: upgrade
        self.reservation_order_type = reservation_order_type
        # The ID of the resource group to which the ACL belongs.
        self.resource_group_id = resource_group_id
        # Indicates whether the bandwidth plan is associated with a CEN instance.
        # 
        # *   **Idle**
        # *   **InUse**
        self.status = status
        # The tags of the bandwidth plan.
        self.tags = tags

    def validate(self):
        if self.cen_ids:
            self.cen_ids.validate()
        if self.orgin_inter_region_bandwidth_limits:
            self.orgin_inter_region_bandwidth_limits.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_package_charge_type is not None:
            result['BandwidthPackageChargeType'] = self.bandwidth_package_charge_type

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id

        if self.cen_ids is not None:
            result['CenIds'] = self.cen_ids.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.geographic_region_aid is not None:
            result['GeographicRegionAId'] = self.geographic_region_aid

        if self.geographic_region_bid is not None:
            result['GeographicRegionBId'] = self.geographic_region_bid

        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id

        if self.has_reservation_data is not None:
            result['HasReservationData'] = self.has_reservation_data

        if self.is_cross_border is not None:
            result['IsCrossBorder'] = self.is_cross_border

        if self.name is not None:
            result['Name'] = self.name

        if self.orgin_inter_region_bandwidth_limits is not None:
            result['OrginInterRegionBandwidthLimits'] = self.orgin_inter_region_bandwidth_limits.to_map()

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

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthPackageChargeType') is not None:
            self.bandwidth_package_charge_type = m.get('BandwidthPackageChargeType')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')

        if m.get('CenIds') is not None:
            temp_model = main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageCenIds()
            self.cen_ids = temp_model.from_map(m.get('CenIds'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('GeographicRegionAId') is not None:
            self.geographic_region_aid = m.get('GeographicRegionAId')

        if m.get('GeographicRegionBId') is not None:
            self.geographic_region_bid = m.get('GeographicRegionBId')

        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')

        if m.get('HasReservationData') is not None:
            self.has_reservation_data = m.get('HasReservationData')

        if m.get('IsCrossBorder') is not None:
            self.is_cross_border = m.get('IsCrossBorder')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrginInterRegionBandwidthLimits') is not None:
            temp_model = main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimits()
            self.orgin_inter_region_bandwidth_limits = temp_model.from_map(m.get('OrginInterRegionBandwidthLimits'))

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageTagsTag] = None,
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
                temp_model = main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageTagsTag(DaraModel):
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

class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimits(DaraModel):
    def __init__(
        self,
        orgin_inter_region_bandwidth_limit: List[main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimitsOrginInterRegionBandwidthLimit] = None,
    ):
        self.orgin_inter_region_bandwidth_limit = orgin_inter_region_bandwidth_limit

    def validate(self):
        if self.orgin_inter_region_bandwidth_limit:
            for v1 in self.orgin_inter_region_bandwidth_limit:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OrginInterRegionBandwidthLimit'] = []
        if self.orgin_inter_region_bandwidth_limit is not None:
            for k1 in self.orgin_inter_region_bandwidth_limit:
                result['OrginInterRegionBandwidthLimit'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.orgin_inter_region_bandwidth_limit = []
        if m.get('OrginInterRegionBandwidthLimit') is not None:
            for k1 in m.get('OrginInterRegionBandwidthLimit'):
                temp_model = main_models.DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimitsOrginInterRegionBandwidthLimit()
                self.orgin_inter_region_bandwidth_limit.append(temp_model.from_map(k1))

        return self

class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimitsOrginInterRegionBandwidthLimit(DaraModel):
    def __init__(
        self,
        bandwidth_limit: str = None,
        geographic_span_id: str = None,
        local_region_id: str = None,
        opposite_region_id: str = None,
    ):
        # The maximum bandwidth value for the inter-region connection.
        self.bandwidth_limit = bandwidth_limit
        # The connected regions.
        self.geographic_span_id = geographic_span_id
        # The ID of the local region.
        self.local_region_id = local_region_id
        # The ID of the peer region.
        self.opposite_region_id = opposite_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit

        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id

        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id

        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')

        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')

        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')

        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')

        return self

class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageCenIds(DaraModel):
    def __init__(
        self,
        cen_id: List[str] = None,
    ):
        self.cen_id = cen_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        return self

