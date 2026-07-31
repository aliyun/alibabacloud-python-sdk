# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
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
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.router_interface_set = router_interface_set
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
        business_status: str = None,
        charge_type: str = None,
        connected_time: str = None,
        creation_time: str = None,
        description: str = None,
        end_time: str = None,
        health_check_source_ip: str = None,
        health_check_target_ip: str = None,
        name: str = None,
        opposite_access_point_id: str = None,
        opposite_interface_business_status: str = None,
        opposite_interface_id: str = None,
        opposite_interface_owner_id: str = None,
        opposite_interface_spec: str = None,
        opposite_interface_status: str = None,
        opposite_region_id: str = None,
        opposite_router_id: str = None,
        opposite_router_type: str = None,
        role: str = None,
        router_id: str = None,
        router_interface_id: str = None,
        router_type: str = None,
        spec: str = None,
        status: str = None,
    ):
        self.access_point_id = access_point_id
        self.business_status = business_status
        self.charge_type = charge_type
        self.connected_time = connected_time
        self.creation_time = creation_time
        self.description = description
        self.end_time = end_time
        self.health_check_source_ip = health_check_source_ip
        self.health_check_target_ip = health_check_target_ip
        self.name = name
        self.opposite_access_point_id = opposite_access_point_id
        self.opposite_interface_business_status = opposite_interface_business_status
        self.opposite_interface_id = opposite_interface_id
        self.opposite_interface_owner_id = opposite_interface_owner_id
        self.opposite_interface_spec = opposite_interface_spec
        self.opposite_interface_status = opposite_interface_status
        self.opposite_region_id = opposite_region_id
        self.opposite_router_id = opposite_router_id
        self.opposite_router_type = opposite_router_type
        self.role = role
        self.router_id = router_id
        self.router_interface_id = router_interface_id
        self.router_type = router_type
        self.spec = spec
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.connected_time is not None:
            result['ConnectedTime'] = self.connected_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.health_check_source_ip is not None:
            result['HealthCheckSourceIp'] = self.health_check_source_ip

        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip

        if self.name is not None:
            result['Name'] = self.name

        if self.opposite_access_point_id is not None:
            result['OppositeAccessPointId'] = self.opposite_access_point_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ConnectedTime') is not None:
            self.connected_time = m.get('ConnectedTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HealthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('HealthCheckSourceIp')

        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OppositeAccessPointId') is not None:
            self.opposite_access_point_id = m.get('OppositeAccessPointId')

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

        return self

