# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetResourceConfigurationTimelineResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_configuration_timeline: main_models.GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The configuration history of the resource.
        self.resource_configuration_timeline = resource_configuration_timeline

    def validate(self):
        if self.resource_configuration_timeline:
            self.resource_configuration_timeline.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_configuration_timeline is not None:
            result['ResourceConfigurationTimeline'] = self.resource_configuration_timeline.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceConfigurationTimeline') is not None:
            temp_model = main_models.GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline()
            self.resource_configuration_timeline = temp_model.from_map(m.get('ResourceConfigurationTimeline'))

        return self

class GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline(DaraModel):
    def __init__(
        self,
        configuration_list: List[main_models.GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # A list of configuration history records for the resource.
        self.configuration_list = configuration_list
        # The maximum number of entries returned for a single request.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token

    def validate(self):
        if self.configuration_list:
            for v1 in self.configuration_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigurationList'] = []
        if self.configuration_list is not None:
            for k1 in self.configuration_list:
                result['ConfigurationList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configuration_list = []
        if m.get('ConfigurationList') is not None:
            for k1 in m.get('ConfigurationList'):
                temp_model = main_models.GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList()
                self.configuration_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        availability_zone: str = None,
        capture_time: str = None,
        configuration_diff: str = None,
        region: str = None,
        relationship: str = None,
        relationship_diff: str = None,
        resource_create_time: str = None,
        resource_event_type: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.account_id = account_id
        # The zone.
        self.availability_zone = availability_zone
        # The timestamp when the resource change snapshot was recorded. The value is a UNIX timestamp in milliseconds.
        self.capture_time = capture_time
        # The details of the resource configuration change.
        self.configuration_diff = configuration_diff
        # The region ID.
        self.region = region
        # Details of related resources, including their region ID, relationship, resource ID, and resource type.
        self.relationship = relationship
        # The changes to the related resources.
        self.relationship_diff = relationship_diff
        # The timestamp when the resource was created. The value is a UNIX timestamp in milliseconds.
        self.resource_create_time = resource_create_time
        # The type of the resource change event. Valid values:
        # 
        # - DISCOVERED: A resource is discovered by Cloud Config.
        # 
        # - DISCOVERED_REVISED: A resource is discovered by Cloud Config through a periodic reconciliation task.
        # 
        # - MODIFY: A resource is modified.
        # 
        # - MODIFY_REVISED: A resource modification is recorded through a periodic reconciliation task.
        # 
        # - REMOVE: A resource is deleted.
        # 
        # > * To ensure data integrity, Cloud Config periodically reconciles resource data. This process can generate resource discovery events, which occur infrequently.
        # >
        # > * The time of an event generated by a reconciliation task is the time when the task discovers the change. This is later than the actual time of the change.
        self.resource_event_type = resource_event_type
        # The resource ID.
        self.resource_id = resource_id
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type
        # The tags of the resource.
        self.tags = tags

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

        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time

        if self.configuration_diff is not None:
            result['ConfigurationDiff'] = self.configuration_diff

        if self.region is not None:
            result['Region'] = self.region

        if self.relationship is not None:
            result['Relationship'] = self.relationship

        if self.relationship_diff is not None:
            result['RelationshipDiff'] = self.relationship_diff

        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time

        if self.resource_event_type is not None:
            result['ResourceEventType'] = self.resource_event_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')

        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')

        if m.get('ConfigurationDiff') is not None:
            self.configuration_diff = m.get('ConfigurationDiff')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Relationship') is not None:
            self.relationship = m.get('Relationship')

        if m.get('RelationshipDiff') is not None:
            self.relationship_diff = m.get('RelationshipDiff')

        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')

        if m.get('ResourceEventType') is not None:
            self.resource_event_type = m.get('ResourceEventType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

