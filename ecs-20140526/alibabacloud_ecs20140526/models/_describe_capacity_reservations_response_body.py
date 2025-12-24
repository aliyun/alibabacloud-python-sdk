# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeCapacityReservationsResponseBody(DaraModel):
    def __init__(
        self,
        capacity_reservation_set: main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSet = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of the capacity reservations.
        self.capacity_reservation_set = capacity_reservation_set
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.capacity_reservation_set:
            self.capacity_reservation_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_reservation_set is not None:
            result['CapacityReservationSet'] = self.capacity_reservation_set.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityReservationSet') is not None:
            temp_model = main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSet()
            self.capacity_reservation_set = temp_model.from_map(m.get('CapacityReservationSet'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCapacityReservationsResponseBodyCapacityReservationSet(DaraModel):
    def __init__(
        self,
        capacity_reservation_item: List[main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItem] = None,
    ):
        self.capacity_reservation_item = capacity_reservation_item

    def validate(self):
        if self.capacity_reservation_item:
            for v1 in self.capacity_reservation_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CapacityReservationItem'] = []
        if self.capacity_reservation_item is not None:
            for k1 in self.capacity_reservation_item:
                result['CapacityReservationItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.capacity_reservation_item = []
        if m.get('CapacityReservationItem') is not None:
            for k1 in m.get('CapacityReservationItem'):
                temp_model = main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItem()
                self.capacity_reservation_item.append(temp_model.from_map(k1))

        return self

class DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItem(DaraModel):
    def __init__(
        self,
        allocated_resources: main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemAllocatedResources = None,
        capacity_reservation_owner_id: str = None,
        description: str = None,
        end_time: str = None,
        end_time_type: str = None,
        instance_charge_type: str = None,
        platform: str = None,
        private_pool_options_id: str = None,
        private_pool_options_match_criteria: str = None,
        private_pool_options_name: str = None,
        region_id: str = None,
        reserved_instance_id: str = None,
        resource_group_id: str = None,
        saving_plan_id: str = None,
        start_time: str = None,
        start_time_type: str = None,
        status: str = None,
        tags: main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemTags = None,
        time_slot: str = None,
    ):
        # Details of the allocated resources.
        self.allocated_resources = allocated_resources
        # The ID of the capacity reservation owner.
        self.capacity_reservation_owner_id = capacity_reservation_owner_id
        # The description of the capacity reservation.
        self.description = description
        # The time when the capacity reservation expires.
        self.end_time = end_time
        # The release mode of the capacity reservation. Valid values:
        # 
        # *   Limited: The capacity reservation is automatically released at a specified time.
        # *   Unlimited: The capacity reservation is manually released. You can release the capacity reservation anytime.
        self.end_time_type = end_time_type
        # The billing method of the instances created by using the capacity reservation. Valid values:
        # 
        # *   PostPaid: pay-as-you-go.
        # *   PrePaid: subscription.
        self.instance_charge_type = instance_charge_type
        # The operating system type of the instances created by using the capacity reservation. Valid values:
        # 
        # *   windows
        # *   linux
        self.platform = platform
        # The ID of the capacity reservation.
        self.private_pool_options_id = private_pool_options_id
        # The type of the private pool generated after the capacity reservation takes effect. Valid values:
        # 
        # *   Open: open private pool. If you use the capacity reservation to create Elastic Compute Service (ECS) instances, the open private pool that is associated with the capacity reservation is automatically matched. If no capacity is available in the open private pool, resources in the public pool are automatically used to create the instances.
        # *   Target: targeted private pool. If you use the capacity reservation to create ECS instances, the targeted private pool that is associated with the capacity reservation is automatically matched. If no capacity is available in the private pool, the instances fail to be created.
        self.private_pool_options_match_criteria = private_pool_options_match_criteria
        # The name of the capacity reservation.
        self.private_pool_options_name = private_pool_options_name
        # The region ID of the capacity reservation.
        self.region_id = region_id
        # The ID of the reserved instance used with the capacity reservation.
        self.reserved_instance_id = reserved_instance_id
        # The ID of the resource group to which the capacity reservation belongs.
        self.resource_group_id = resource_group_id
        # The ID of the savings plan used with the capacity reservation.
        self.saving_plan_id = saving_plan_id
        # The time when the capacity reservation takes effect.
        self.start_time = start_time
        # The mode in which the capacity reservation takes effect. Valid values:
        # 
        # *   Now: The capacity reservation takes effect immediately after it is created.
        # *   Later: The capacity reservation takes effect at a specified time.
        self.start_time_type = start_time_type
        # The status of the capacity reservation. Valid values:
        # 
        # *   Pending: The capacity reservation is being initialized.
        # *   Preparing: The capacity reservation is being prepared.
        # *   Prepared: The capacity reservation is to take effect.
        # *   Active: The capacity reservation is in effect.
        # *   Released: The capacity reservation has been released manually or automatically when it expired.
        self.status = status
        # The tags that are added to the capacity reservation.
        self.tags = tags
        # >  This parameter is in invitational preview and is not publicly available.
        self.time_slot = time_slot

    def validate(self):
        if self.allocated_resources:
            self.allocated_resources.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocated_resources is not None:
            result['AllocatedResources'] = self.allocated_resources.to_map()

        if self.capacity_reservation_owner_id is not None:
            result['CapacityReservationOwnerId'] = self.capacity_reservation_owner_id

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_time_type is not None:
            result['EndTimeType'] = self.end_time_type

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.private_pool_options_id is not None:
            result['PrivatePoolOptionsId'] = self.private_pool_options_id

        if self.private_pool_options_match_criteria is not None:
            result['PrivatePoolOptionsMatchCriteria'] = self.private_pool_options_match_criteria

        if self.private_pool_options_name is not None:
            result['PrivatePoolOptionsName'] = self.private_pool_options_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserved_instance_id is not None:
            result['ReservedInstanceId'] = self.reserved_instance_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.saving_plan_id is not None:
            result['SavingPlanId'] = self.saving_plan_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.start_time_type is not None:
            result['StartTimeType'] = self.start_time_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.time_slot is not None:
            result['TimeSlot'] = self.time_slot

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatedResources') is not None:
            temp_model = main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemAllocatedResources()
            self.allocated_resources = temp_model.from_map(m.get('AllocatedResources'))

        if m.get('CapacityReservationOwnerId') is not None:
            self.capacity_reservation_owner_id = m.get('CapacityReservationOwnerId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndTimeType') is not None:
            self.end_time_type = m.get('EndTimeType')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('PrivatePoolOptionsId') is not None:
            self.private_pool_options_id = m.get('PrivatePoolOptionsId')

        if m.get('PrivatePoolOptionsMatchCriteria') is not None:
            self.private_pool_options_match_criteria = m.get('PrivatePoolOptionsMatchCriteria')

        if m.get('PrivatePoolOptionsName') is not None:
            self.private_pool_options_name = m.get('PrivatePoolOptionsName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReservedInstanceId') is not None:
            self.reserved_instance_id = m.get('ReservedInstanceId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SavingPlanId') is not None:
            self.saving_plan_id = m.get('SavingPlanId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StartTimeType') is not None:
            self.start_time_type = m.get('StartTimeType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TimeSlot') is not None:
            self.time_slot = m.get('TimeSlot')

        return self

class DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemTagsTag] = None,
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
                temp_model = main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemAllocatedResources(DaraModel):
    def __init__(
        self,
        allocated_resource: List[main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemAllocatedResourcesAllocatedResource] = None,
    ):
        self.allocated_resource = allocated_resource

    def validate(self):
        if self.allocated_resource:
            for v1 in self.allocated_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AllocatedResource'] = []
        if self.allocated_resource is not None:
            for k1 in self.allocated_resource:
                result['AllocatedResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.allocated_resource = []
        if m.get('AllocatedResource') is not None:
            for k1 in m.get('AllocatedResource'):
                temp_model = main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemAllocatedResourcesAllocatedResource()
                self.allocated_resource.append(temp_model.from_map(k1))

        return self

class DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemAllocatedResourcesAllocatedResource(DaraModel):
    def __init__(
        self,
        available_amount: int = None,
        capacity_reservation_usages: main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemAllocatedResourcesAllocatedResourceCapacityReservationUsages = None,
        instance_type: str = None,
        total_amount: int = None,
        used_amount: int = None,
        zone_id: str = None,
    ):
        # The number of available instances.
        self.available_amount = available_amount
        # Details of instance usage.
        self.capacity_reservation_usages = capacity_reservation_usages
        # The instance type of the instances.
        self.instance_type = instance_type
        # The total number of instances for which the capacity of an instance type is reserved.
        self.total_amount = total_amount
        # The number of instances that have used the capacity reservation.
        self.used_amount = used_amount
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.capacity_reservation_usages:
            self.capacity_reservation_usages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount

        if self.capacity_reservation_usages is not None:
            result['CapacityReservationUsages'] = self.capacity_reservation_usages.to_map()

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount

        if self.used_amount is not None:
            result['UsedAmount'] = self.used_amount

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')

        if m.get('CapacityReservationUsages') is not None:
            temp_model = main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemAllocatedResourcesAllocatedResourceCapacityReservationUsages()
            self.capacity_reservation_usages = temp_model.from_map(m.get('CapacityReservationUsages'))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')

        if m.get('UsedAmount') is not None:
            self.used_amount = m.get('UsedAmount')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemAllocatedResourcesAllocatedResourceCapacityReservationUsages(DaraModel):
    def __init__(
        self,
        capacity_reservation_usage: List[main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemAllocatedResourcesAllocatedResourceCapacityReservationUsagesCapacityReservationUsage] = None,
    ):
        self.capacity_reservation_usage = capacity_reservation_usage

    def validate(self):
        if self.capacity_reservation_usage:
            for v1 in self.capacity_reservation_usage:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CapacityReservationUsage'] = []
        if self.capacity_reservation_usage is not None:
            for k1 in self.capacity_reservation_usage:
                result['CapacityReservationUsage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.capacity_reservation_usage = []
        if m.get('CapacityReservationUsage') is not None:
            for k1 in m.get('CapacityReservationUsage'):
                temp_model = main_models.DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemAllocatedResourcesAllocatedResourceCapacityReservationUsagesCapacityReservationUsage()
                self.capacity_reservation_usage.append(temp_model.from_map(k1))

        return self

class DescribeCapacityReservationsResponseBodyCapacityReservationSetCapacityReservationItemAllocatedResourcesAllocatedResourceCapacityReservationUsagesCapacityReservationUsage(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        service_name: str = None,
        used_amount: int = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The name of the Alibaba Cloud service.
        self.service_name = service_name
        # The number of instances that are used by the Alibaba Cloud account or service.
        self.used_amount = used_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.used_amount is not None:
            result['UsedAmount'] = self.used_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('UsedAmount') is not None:
            self.used_amount = m.get('UsedAmount')

        return self

