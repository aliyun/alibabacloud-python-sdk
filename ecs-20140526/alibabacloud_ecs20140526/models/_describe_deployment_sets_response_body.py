# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDeploymentSetsResponseBody(DaraModel):
    def __init__(
        self,
        deployment_sets: main_models.DescribeDeploymentSetsResponseBodyDeploymentSets = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the deployment sets.
        self.deployment_sets = deployment_sets
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the region.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The total number of queried deployment sets.
        self.total_count = total_count

    def validate(self):
        if self.deployment_sets:
            self.deployment_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_sets is not None:
            result['DeploymentSets'] = self.deployment_sets.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentSets') is not None:
            temp_model = main_models.DescribeDeploymentSetsResponseBodyDeploymentSets()
            self.deployment_sets = temp_model.from_map(m.get('DeploymentSets'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDeploymentSetsResponseBodyDeploymentSets(DaraModel):
    def __init__(
        self,
        deployment_set: List[main_models.DescribeDeploymentSetsResponseBodyDeploymentSetsDeploymentSet] = None,
    ):
        self.deployment_set = deployment_set

    def validate(self):
        if self.deployment_set:
            for v1 in self.deployment_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeploymentSet'] = []
        if self.deployment_set is not None:
            for k1 in self.deployment_set:
                result['DeploymentSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployment_set = []
        if m.get('DeploymentSet') is not None:
            for k1 in m.get('DeploymentSet'):
                temp_model = main_models.DescribeDeploymentSetsResponseBodyDeploymentSetsDeploymentSet()
                self.deployment_set.append(temp_model.from_map(k1))

        return self

class DescribeDeploymentSetsResponseBodyDeploymentSetsDeploymentSet(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        capacities: main_models.DescribeDeploymentSetsResponseBodyDeploymentSetsDeploymentSetCapacities = None,
        creation_time: str = None,
        deployment_set_description: str = None,
        deployment_set_id: str = None,
        deployment_set_name: str = None,
        deployment_strategy: str = None,
        domain: str = None,
        granularity: str = None,
        group_count: int = None,
        instance_amount: int = None,
        instance_ids: main_models.DescribeDeploymentSetsResponseBodyDeploymentSetsDeploymentSetInstanceIds = None,
        strategy: str = None,
    ):
        self.account_id = account_id
        # Details of the capacities of the deployment set. This parameter is valid only when the deployment set contains ECS instances. The value contains information about the capacities of the deployment set in different zones.
        self.capacities = capacities
        # The time when the deployment set was created.
        self.creation_time = creation_time
        # The description of the deployment set.
        self.deployment_set_description = deployment_set_description
        # The ID of the deployment set.
        self.deployment_set_id = deployment_set_id
        # The name of the deployment set.
        self.deployment_set_name = deployment_set_name
        # The deployment strategy. The return value of this parameter is the value of the `Strategy` request parameter.
        self.deployment_strategy = deployment_strategy
        # The deployment domain.
        self.domain = domain
        # The deployment granularity.
        self.granularity = granularity
        # The number of deployment set groups in the deployment set.
        # 
        # >  This parameter is valid only when the Strategy request parameter is set to AvailabilityGroup.
        self.group_count = group_count
        # The number of instances in the deployment set.
        self.instance_amount = instance_amount
        # The IDs of the Elastic Compute Service (ECS) instances in the deployment set.
        self.instance_ids = instance_ids
        # The deployment strategy.
        self.strategy = strategy

    def validate(self):
        if self.capacities:
            self.capacities.validate()
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.capacities is not None:
            result['Capacities'] = self.capacities.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.deployment_set_description is not None:
            result['DeploymentSetDescription'] = self.deployment_set_description

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.deployment_set_name is not None:
            result['DeploymentSetName'] = self.deployment_set_name

        if self.deployment_strategy is not None:
            result['DeploymentStrategy'] = self.deployment_strategy

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.group_count is not None:
            result['GroupCount'] = self.group_count

        if self.instance_amount is not None:
            result['InstanceAmount'] = self.instance_amount

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('Capacities') is not None:
            temp_model = main_models.DescribeDeploymentSetsResponseBodyDeploymentSetsDeploymentSetCapacities()
            self.capacities = temp_model.from_map(m.get('Capacities'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeploymentSetDescription') is not None:
            self.deployment_set_description = m.get('DeploymentSetDescription')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('DeploymentSetName') is not None:
            self.deployment_set_name = m.get('DeploymentSetName')

        if m.get('DeploymentStrategy') is not None:
            self.deployment_strategy = m.get('DeploymentStrategy')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')

        if m.get('InstanceAmount') is not None:
            self.instance_amount = m.get('InstanceAmount')

        if m.get('InstanceIds') is not None:
            temp_model = main_models.DescribeDeploymentSetsResponseBodyDeploymentSetsDeploymentSetInstanceIds()
            self.instance_ids = temp_model.from_map(m.get('InstanceIds'))

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class DescribeDeploymentSetsResponseBodyDeploymentSetsDeploymentSetInstanceIds(DaraModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class DescribeDeploymentSetsResponseBodyDeploymentSetsDeploymentSetCapacities(DaraModel):
    def __init__(
        self,
        capacity: List[main_models.DescribeDeploymentSetsResponseBodyDeploymentSetsDeploymentSetCapacitiesCapacity] = None,
    ):
        self.capacity = capacity

    def validate(self):
        if self.capacity:
            for v1 in self.capacity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Capacity'] = []
        if self.capacity is not None:
            for k1 in self.capacity:
                result['Capacity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.capacity = []
        if m.get('Capacity') is not None:
            for k1 in m.get('Capacity'):
                temp_model = main_models.DescribeDeploymentSetsResponseBodyDeploymentSetsDeploymentSetCapacitiesCapacity()
                self.capacity.append(temp_model.from_map(k1))

        return self

class DescribeDeploymentSetsResponseBodyDeploymentSetsDeploymentSetCapacitiesCapacity(DaraModel):
    def __init__(
        self,
        available_amount: int = None,
        used_amount: int = None,
        zone_id: str = None,
    ):
        # The number of ECS instances that can be added to the deployment set within the zone.
        self.available_amount = available_amount
        # The number of ECS instances that reside in the zone in the deployment set.
        self.used_amount = used_amount
        # The ID of the zone. Only the zone IDs of existing ECS instances in the deployment set are returned.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount

        if self.used_amount is not None:
            result['UsedAmount'] = self.used_amount

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')

        if m.get('UsedAmount') is not None:
            self.used_amount = m.get('UsedAmount')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

