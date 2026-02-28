# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeRouterInterfacesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        router_interface_set: main_models.DescribeRouterInterfacesResponseBodyRouterInterfaceSet = None,
        total_count: int = None,
    ):
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        self.router_interface_set = router_interface_set
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.router_interface_set:
            self.router_interface_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.router_interface_set is not None:
            result['RouterInterfaceSet'] = self.router_interface_set.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouterInterfaceSet') is not None:
            temp_model = main_models.DescribeRouterInterfacesResponseBodyRouterInterfaceSet()
            self.router_interface_set = temp_model.from_map(m.get('RouterInterfaceSet'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRouterInterfacesResponseBodyRouterInterfaceSet(DaraModel):
    def __init__(
        self,
        router_interface_type: List[main_models.DescribeRouterInterfacesResponseBodyRouterInterfaceSetRouterInterfaceType] = None,
    ):
        self.router_interface_type = router_interface_type

    def validate(self):
        if self.router_interface_type:
            for v1 in self.router_interface_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RouterInterfaceType'] = []
        if self.router_interface_type is not None:
            for k1 in self.router_interface_type:
                result['RouterInterfaceType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.router_interface_type = []
        if m.get('RouterInterfaceType') is not None:
            for k1 in m.get('RouterInterfaceType'):
                temp_model = main_models.DescribeRouterInterfacesResponseBodyRouterInterfaceSetRouterInterfaceType()
                self.router_interface_type.append(temp_model.from_map(k1))

        return self

class DescribeRouterInterfacesResponseBodyRouterInterfaceSetRouterInterfaceType(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        bandwidth: int = None,
        business_status: str = None,
        charge_type: str = None,
        connected_time: str = None,
        creation_time: str = None,
        cross_border: bool = None,
        description: str = None,
        end_time: str = None,
        fast_link_mode: bool = None,
        has_reservation_data: str = None,
        hc_rate: int = None,
        hc_threshold: int = None,
        health_check_source_ip: str = None,
        health_check_target_ip: str = None,
        ipv_6status: str = None,
        name: str = None,
        opposite_access_point_id: str = None,
        opposite_bandwidth: int = None,
        opposite_interface_business_status: str = None,
        opposite_interface_id: str = None,
        opposite_interface_owner_id: str = None,
        opposite_interface_spec: str = None,
        opposite_interface_status: str = None,
        opposite_region_id: str = None,
        opposite_router_id: str = None,
        opposite_router_type: str = None,
        opposite_vpc_instance_id: str = None,
        reservation_active_time: str = None,
        reservation_bandwidth: str = None,
        reservation_internet_charge_type: str = None,
        reservation_order_type: str = None,
        resource_group_id: str = None,
        role: str = None,
        router_id: str = None,
        router_interface_id: str = None,
        router_type: str = None,
        spec: str = None,
        status: str = None,
        tags: main_models.DescribeRouterInterfacesResponseBodyRouterInterfaceSetRouterInterfaceTypeTags = None,
        vpc_instance_id: str = None,
    ):
        self.access_point_id = access_point_id
        self.bandwidth = bandwidth
        self.business_status = business_status
        self.charge_type = charge_type
        self.connected_time = connected_time
        self.creation_time = creation_time
        self.cross_border = cross_border
        self.description = description
        self.end_time = end_time
        self.fast_link_mode = fast_link_mode
        self.has_reservation_data = has_reservation_data
        self.hc_rate = hc_rate
        self.hc_threshold = hc_threshold
        self.health_check_source_ip = health_check_source_ip
        self.health_check_target_ip = health_check_target_ip
        self.ipv_6status = ipv_6status
        self.name = name
        self.opposite_access_point_id = opposite_access_point_id
        self.opposite_bandwidth = opposite_bandwidth
        self.opposite_interface_business_status = opposite_interface_business_status
        self.opposite_interface_id = opposite_interface_id
        self.opposite_interface_owner_id = opposite_interface_owner_id
        self.opposite_interface_spec = opposite_interface_spec
        self.opposite_interface_status = opposite_interface_status
        self.opposite_region_id = opposite_region_id
        self.opposite_router_id = opposite_router_id
        self.opposite_router_type = opposite_router_type
        self.opposite_vpc_instance_id = opposite_vpc_instance_id
        self.reservation_active_time = reservation_active_time
        self.reservation_bandwidth = reservation_bandwidth
        self.reservation_internet_charge_type = reservation_internet_charge_type
        self.reservation_order_type = reservation_order_type
        self.resource_group_id = resource_group_id
        self.role = role
        self.router_id = router_id
        self.router_interface_id = router_interface_id
        self.router_type = router_type
        self.spec = spec
        self.status = status
        self.tags = tags
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.connected_time is not None:
            result['ConnectedTime'] = self.connected_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.cross_border is not None:
            result['CrossBorder'] = self.cross_border

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.fast_link_mode is not None:
            result['FastLinkMode'] = self.fast_link_mode

        if self.has_reservation_data is not None:
            result['HasReservationData'] = self.has_reservation_data

        if self.hc_rate is not None:
            result['HcRate'] = self.hc_rate

        if self.hc_threshold is not None:
            result['HcThreshold'] = self.hc_threshold

        if self.health_check_source_ip is not None:
            result['HealthCheckSourceIp'] = self.health_check_source_ip

        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip

        if self.ipv_6status is not None:
            result['Ipv6Status'] = self.ipv_6status

        if self.name is not None:
            result['Name'] = self.name

        if self.opposite_access_point_id is not None:
            result['OppositeAccessPointId'] = self.opposite_access_point_id

        if self.opposite_bandwidth is not None:
            result['OppositeBandwidth'] = self.opposite_bandwidth

        if self.opposite_interface_business_status is not None:
            result['OppositeInterfaceBusinessStatus'] = self.opposite_interface_business_status

        if self.opposite_interface_id is not None:
            result['OppositeInterfaceId'] = self.opposite_interface_id

        if self.opposite_interface_owner_id is not None:
            result['OppositeInterfaceOwnerId'] = self.opposite_interface_owner_id

        if self.opposite_interface_spec is not None:
            result['OppositeInterfaceSpec'] = self.opposite_interface_spec

        if self.opposite_interface_status is not None:
            result['OppositeInterfaceStatus'] = self.opposite_interface_status

        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id

        if self.opposite_router_id is not None:
            result['OppositeRouterId'] = self.opposite_router_id

        if self.opposite_router_type is not None:
            result['OppositeRouterType'] = self.opposite_router_type

        if self.opposite_vpc_instance_id is not None:
            result['OppositeVpcInstanceId'] = self.opposite_vpc_instance_id

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

        if self.role is not None:
            result['Role'] = self.role

        if self.router_id is not None:
            result['RouterId'] = self.router_id

        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id

        if self.router_type is not None:
            result['RouterType'] = self.router_type

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ConnectedTime') is not None:
            self.connected_time = m.get('ConnectedTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CrossBorder') is not None:
            self.cross_border = m.get('CrossBorder')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FastLinkMode') is not None:
            self.fast_link_mode = m.get('FastLinkMode')

        if m.get('HasReservationData') is not None:
            self.has_reservation_data = m.get('HasReservationData')

        if m.get('HcRate') is not None:
            self.hc_rate = m.get('HcRate')

        if m.get('HcThreshold') is not None:
            self.hc_threshold = m.get('HcThreshold')

        if m.get('HealthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('HealthCheckSourceIp')

        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')

        if m.get('Ipv6Status') is not None:
            self.ipv_6status = m.get('Ipv6Status')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OppositeAccessPointId') is not None:
            self.opposite_access_point_id = m.get('OppositeAccessPointId')

        if m.get('OppositeBandwidth') is not None:
            self.opposite_bandwidth = m.get('OppositeBandwidth')

        if m.get('OppositeInterfaceBusinessStatus') is not None:
            self.opposite_interface_business_status = m.get('OppositeInterfaceBusinessStatus')

        if m.get('OppositeInterfaceId') is not None:
            self.opposite_interface_id = m.get('OppositeInterfaceId')

        if m.get('OppositeInterfaceOwnerId') is not None:
            self.opposite_interface_owner_id = m.get('OppositeInterfaceOwnerId')

        if m.get('OppositeInterfaceSpec') is not None:
            self.opposite_interface_spec = m.get('OppositeInterfaceSpec')

        if m.get('OppositeInterfaceStatus') is not None:
            self.opposite_interface_status = m.get('OppositeInterfaceStatus')

        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')

        if m.get('OppositeRouterId') is not None:
            self.opposite_router_id = m.get('OppositeRouterId')

        if m.get('OppositeRouterType') is not None:
            self.opposite_router_type = m.get('OppositeRouterType')

        if m.get('OppositeVpcInstanceId') is not None:
            self.opposite_vpc_instance_id = m.get('OppositeVpcInstanceId')

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

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')

        if m.get('RouterType') is not None:
            self.router_type = m.get('RouterType')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeRouterInterfacesResponseBodyRouterInterfaceSetRouterInterfaceTypeTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

class DescribeRouterInterfacesResponseBodyRouterInterfaceSetRouterInterfaceTypeTags(DaraModel):
    def __init__(
        self,
        tags: List[main_models.DescribeRouterInterfacesResponseBodyRouterInterfaceSetRouterInterfaceTypeTagsTags] = None,
    ):
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
        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeRouterInterfacesResponseBodyRouterInterfaceSetRouterInterfaceTypeTagsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeRouterInterfacesResponseBodyRouterInterfaceSetRouterInterfaceTypeTagsTags(DaraModel):
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

