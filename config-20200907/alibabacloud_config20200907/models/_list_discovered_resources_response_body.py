# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListDiscoveredResourcesResponseBody(DaraModel):
    def __init__(
        self,
        discovered_resource_profiles: main_models.ListDiscoveredResourcesResponseBodyDiscoveredResourceProfiles = None,
        request_id: str = None,
    ):
        # The information about the resources.
        self.discovered_resource_profiles = discovered_resource_profiles
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_profiles:
            self.discovered_resource_profiles.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discovered_resource_profiles is not None:
            result['DiscoveredResourceProfiles'] = self.discovered_resource_profiles.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscoveredResourceProfiles') is not None:
            temp_model = main_models.ListDiscoveredResourcesResponseBodyDiscoveredResourceProfiles()
            self.discovered_resource_profiles = temp_model.from_map(m.get('DiscoveredResourceProfiles'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDiscoveredResourcesResponseBodyDiscoveredResourceProfiles(DaraModel):
    def __init__(
        self,
        discovered_resource_profile_list: List[main_models.ListDiscoveredResourcesResponseBodyDiscoveredResourceProfilesDiscoveredResourceProfileList] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The details of the resources.
        self.discovered_resource_profile_list = discovered_resource_profile_list
        # The maximum number of entries returned on each page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The total number of resources.
        self.total_count = total_count

    def validate(self):
        if self.discovered_resource_profile_list:
            for v1 in self.discovered_resource_profile_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DiscoveredResourceProfileList'] = []
        if self.discovered_resource_profile_list is not None:
            for k1 in self.discovered_resource_profile_list:
                result['DiscoveredResourceProfileList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.discovered_resource_profile_list = []
        if m.get('DiscoveredResourceProfileList') is not None:
            for k1 in m.get('DiscoveredResourceProfileList'):
                temp_model = main_models.ListDiscoveredResourcesResponseBodyDiscoveredResourceProfilesDiscoveredResourceProfileList()
                self.discovered_resource_profile_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDiscoveredResourcesResponseBodyDiscoveredResourceProfilesDiscoveredResourceProfileList(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        availability_zone: str = None,
        region: str = None,
        resource_creation_time: int = None,
        resource_deleted: int = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
        resource_type: str = None,
        tags: str = None,
        update_time: int = None,
        v_switch_id: str = None,
        version: int = None,
        vpc_id: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.account_id = account_id
        # The zone ID.
        self.availability_zone = availability_zone
        # The region ID.
        self.region = region
        # The timestamp when the resource was created. Unit: milliseconds.
        self.resource_creation_time = resource_creation_time
        # The status of the resource. Valid values:
        # 
        # *   0: The resource is deleted.
        # *   1: The resource is retained.
        self.resource_deleted = resource_deleted
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The resource ID.
        self.resource_id = resource_id
        # The resource name.
        self.resource_name = resource_name
        # The status of the resource. The value of this parameter varies based on the resource type and may be empty. Examples:
        # 
        # *   If the ResourceType parameter is set to ACS::ECS::Instance, the resource is an Elastic Compute Service (ECS) instance that has a specific state. In this case, the valid values of this parameter are Running and Stopped.
        # *   If the ResourceType parameter is ACS::OSS::Bucket, the resource is an Object Storage Service (OSS) bucket that is not in a specific state. In this case, this parameter is left empty.
        self.resource_status = resource_status
        # The type of the resource.
        self.resource_type = resource_type
        # The tags of the resource.
        self.tags = tags
        # The time when the resource was last updated. The value must be a timestamp in milliseconds.
        self.update_time = update_time
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The version of the resource change.
        self.version = version
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_creation_time is not None:
            result['ResourceCreationTime'] = self.resource_creation_time

        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceCreationTime') is not None:
            self.resource_creation_time = m.get('ResourceCreationTime')

        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

