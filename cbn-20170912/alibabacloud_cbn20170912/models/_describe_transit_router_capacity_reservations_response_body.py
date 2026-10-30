# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeTransitRouterCapacityReservationsResponseBody(DaraModel):
    def __init__(
        self,
        deployment_sets: List[main_models.DescribeTransitRouterCapacityReservationsResponseBodyDeploymentSets] = None,
        last_modified_time: str = None,
        minimum_transit_router_capacities: List[main_models.DescribeTransitRouterCapacityReservationsResponseBodyMinimumTransitRouterCapacities] = None,
        request_id: str = None,
    ):
        # The deployment set information specified for the resource reservation.
        self.deployment_sets = deployment_sets
        # The time when the resource reservation was last modified.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.last_modified_time = last_modified_time
        # The list of reserved capacity information for each zone in the resource reservation.
        self.minimum_transit_router_capacities = minimum_transit_router_capacities
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.deployment_sets:
            for v1 in self.deployment_sets:
                 if v1:
                    v1.validate()
        if self.minimum_transit_router_capacities:
            for v1 in self.minimum_transit_router_capacities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeploymentSets'] = []
        if self.deployment_sets is not None:
            for k1 in self.deployment_sets:
                result['DeploymentSets'].append(k1.to_map() if k1 else None)

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        result['MinimumTransitRouterCapacities'] = []
        if self.minimum_transit_router_capacities is not None:
            for k1 in self.minimum_transit_router_capacities:
                result['MinimumTransitRouterCapacities'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployment_sets = []
        if m.get('DeploymentSets') is not None:
            for k1 in m.get('DeploymentSets'):
                temp_model = main_models.DescribeTransitRouterCapacityReservationsResponseBodyDeploymentSets()
                self.deployment_sets.append(temp_model.from_map(k1))

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        self.minimum_transit_router_capacities = []
        if m.get('MinimumTransitRouterCapacities') is not None:
            for k1 in m.get('MinimumTransitRouterCapacities'):
                temp_model = main_models.DescribeTransitRouterCapacityReservationsResponseBodyMinimumTransitRouterCapacities()
                self.minimum_transit_router_capacities.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTransitRouterCapacityReservationsResponseBodyMinimumTransitRouterCapacities(DaraModel):
    def __init__(
        self,
        data_process_gbps: main_models.DescribeTransitRouterCapacityReservationsResponseBodyMinimumTransitRouterCapacitiesDataProcessGbps = None,
        state: main_models.DescribeTransitRouterCapacityReservationsResponseBodyMinimumTransitRouterCapacitiesState = None,
        zone_id: str = None,
    ):
        # The reserved capacity information for the specified zone in the resource reservation.
        self.data_process_gbps = data_process_gbps
        # The status information of the specified zone in the resource reservation.
        self.state = state
        # The ID of the specified zone for the resource reservation.
        self.zone_id = zone_id

    def validate(self):
        if self.data_process_gbps:
            self.data_process_gbps.validate()
        if self.state:
            self.state.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_process_gbps is not None:
            result['DataProcessGbps'] = self.data_process_gbps.to_map()

        if self.state is not None:
            result['State'] = self.state.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataProcessGbps') is not None:
            temp_model = main_models.DescribeTransitRouterCapacityReservationsResponseBodyMinimumTransitRouterCapacitiesDataProcessGbps()
            self.data_process_gbps = temp_model.from_map(m.get('DataProcessGbps'))

        if m.get('State') is not None:
            temp_model = main_models.DescribeTransitRouterCapacityReservationsResponseBodyMinimumTransitRouterCapacitiesState()
            self.state = temp_model.from_map(m.get('State'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeTransitRouterCapacityReservationsResponseBodyMinimumTransitRouterCapacitiesState(DaraModel):
    def __init__(
        self,
        reason: str = None,
        status: str = None,
    ):
        # The reason for failure when the reservation status is ProvisionFailed.
        # 
        # - For example, Reservation.InsufficientCapacity indicates that resources are insufficient to meet the target reserved value.
        self.reason = reason
        # The resource reservation status. Valid values:
        # - Pending: The initial reservation is initiated and is pending processing by Alibaba Cloud.
        # - Provisioning: Alibaba Cloud is processing the reservation request.
        # - Provisioned: The reservation is successful.
        # - ProvisionFailed: The reservation failed. You can refer to the failure reason.
        # - Updating: The reservation is being updated. Operations such as modifying the deployment set or increasing the reserved value require spooling by Alibaba Cloud.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeTransitRouterCapacityReservationsResponseBodyMinimumTransitRouterCapacitiesDataProcessGbps(DaraModel):
    def __init__(
        self,
        effective: int = None,
        target: int = None,
    ):
        # The effective reserved value for the specified zone in the resource reservation.
        # 
        # - The effective reserved value refers to the current billed value for the resource reservation.
        self.effective = effective
        # The target reserved value for the specified active zone in the resource reservation.
        # 
        # - In scenarios where you decrease the quota, the change takes effect in the next month, and the effective reserved value is updated in synchronization.
        # - Upgrade and initial reservation scenarios require spooling by Alibaba Cloud and take effect immediately after the spooling is complete.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective is not None:
            result['Effective'] = self.effective

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

class DescribeTransitRouterCapacityReservationsResponseBodyDeploymentSets(DaraModel):
    def __init__(
        self,
        deployment_set_id: str = None,
        zone_id: str = None,
    ):
        # The instance ID of the deployment set configured in the specified active zone of the transit router, which handles forward and routing tasks.
        self.deployment_set_id = deployment_set_id
        # The zone for which you want to modify the deployment set of the resource reservation.
        # 
        # - To cancel the deployment set, specify the zone and leave the deployment set instance ID empty.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_set_id is not None:
            result['DeploymentSetID'] = self.deployment_set_id

        if self.zone_id is not None:
            result['ZoneID'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentSetID') is not None:
            self.deployment_set_id = m.get('DeploymentSetID')

        if m.get('ZoneID') is not None:
            self.zone_id = m.get('ZoneID')

        return self

