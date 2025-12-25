# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCDeploymentSetsResponseBody(DaraModel):
    def __init__(
        self,
        deployment_sets: main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSets = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the deployment set.
        self.deployment_sets = deployment_sets
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
            temp_model = main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSets()
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

class DescribeRCDeploymentSetsResponseBodyDeploymentSets(DaraModel):
    def __init__(
        self,
        deployment_set: List[main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSet] = None,
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
                temp_model = main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSet()
                self.deployment_set.append(temp_model.from_map(k1))

        return self

class DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSet(DaraModel):
    def __init__(
        self,
        capacities: main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetCapacities = None,
        create_time: str = None,
        deployment_set_description: str = None,
        deployment_set_id: str = None,
        deployment_set_name: str = None,
        deployment_strategy: str = None,
        domain: str = None,
        granularity: str = None,
        group_count: int = None,
        instance_amount: int = None,
        instance_ids: main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetInstanceIds = None,
        strategy: str = None,
        tags: main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetTags = None,
    ):
        # The details of the capacities of the deployment set. This parameter is valid only when the deployment set contains existing RDS Custom instances. The value contains the details of the capacities of the deployment set in different zones.
        self.capacities = capacities
        # The time when the deployment set was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The deployment set description.
        self.deployment_set_description = deployment_set_description
        # The deployment set ID.
        self.deployment_set_id = deployment_set_id
        # The deployment set name.
        self.deployment_set_name = deployment_set_name
        # The deployment strategy. The return value of this parameter is the value of the `Strategy` request parameter.
        self.deployment_strategy = deployment_strategy
        # The deployment domain.
        self.domain = domain
        # The deployment granularity.
        self.granularity = granularity
        # The number of groups in the deployment set.
        # 
        # >  This parameter is valid only when the Strategy request parameter is set to AvailabilityGroup.
        self.group_count = group_count
        # The number of RDS Custom instances in the deployment set.
        self.instance_amount = instance_amount
        # The ID of the RDS Custom instance in the deployment set.
        self.instance_ids = instance_ids
        # The deployment strategy.
        self.strategy = strategy
        self.tags = tags

    def validate(self):
        if self.capacities:
            self.capacities.validate()
        if self.instance_ids:
            self.instance_ids.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacities is not None:
            result['Capacities'] = self.capacities.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacities') is not None:
            temp_model = main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetCapacities()
            self.capacities = temp_model.from_map(m.get('Capacities'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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
            temp_model = main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetInstanceIds()
            self.instance_ids = temp_model.from_map(m.get('InstanceIds'))

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetTagsTag] = None,
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
                temp_model = main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetTagsTag(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetInstanceIds(DaraModel):
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

class DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetCapacities(DaraModel):
    def __init__(
        self,
        capacity: List[main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetCapacitiesCapacity] = None,
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
                temp_model = main_models.DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetCapacitiesCapacity()
                self.capacity.append(temp_model.from_map(k1))

        return self

class DescribeRCDeploymentSetsResponseBodyDeploymentSetsDeploymentSetCapacitiesCapacity(DaraModel):
    def __init__(
        self,
        available_amount: int = None,
        used_amount: int = None,
        zone_id: str = None,
    ):
        # The number of RDS Custom instances that reside in the zone and can be added to the deployment set.
        self.available_amount = available_amount
        # The number of RDS Custom instances that reside in the zone in the deployment set.
        self.used_amount = used_amount
        # The zone ID. Only the IDs of the zones to which the existing RDS Custom instances in the deployment set belong are returned.
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

