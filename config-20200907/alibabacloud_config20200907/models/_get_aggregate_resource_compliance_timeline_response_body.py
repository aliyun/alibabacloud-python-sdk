# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetAggregateResourceComplianceTimelineResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_compliance_timeline: main_models.GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimeline = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the compliance timeline.
        self.resource_compliance_timeline = resource_compliance_timeline

    def validate(self):
        if self.resource_compliance_timeline:
            self.resource_compliance_timeline.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_compliance_timeline is not None:
            result['ResourceComplianceTimeline'] = self.resource_compliance_timeline.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceComplianceTimeline') is not None:
            temp_model = main_models.GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimeline()
            self.resource_compliance_timeline = temp_model.from_map(m.get('ResourceComplianceTimeline'))

        return self

class GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimeline(DaraModel):
    def __init__(
        self,
        compliance_list: List[main_models.GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The status of the resource. The parameter value varies based on the resource type and may be left empty. Examples:
        # 
        # *   If the value of the ResourceType parameter is ACS::ECS::Instance, the resource is an Elastic Compute Service (ECS) instance that has a specific state. In this case, the valid values of this parameter are Running and Stopped.
        # *   If the value of the ResourceType parameter is ACS::OSS::Bucket, the resource is an Object Storage Service (OSS) bucket that is not in a specific state. In this case, this parameter is empty.
        self.compliance_list = compliance_list
        # The maximum number of entries returned for a single request.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token

    def validate(self):
        if self.compliance_list:
            for v1 in self.compliance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComplianceList'] = []
        if self.compliance_list is not None:
            for k1 in self.compliance_list:
                result['ComplianceList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_list = []
        if m.get('ComplianceList') is not None:
            for k1 in m.get('ComplianceList'):
                temp_model = main_models.GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList()
                self.compliance_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        availability_zone: str = None,
        capture_time: int = None,
        configuration: str = None,
        configuration_diff: str = None,
        region: str = None,
        resource_create_time: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.account_id = account_id
        # The ID of the zone in which the resource resides.
        self.availability_zone = availability_zone
        # The timestamp when the compliance evaluation was recorded. Unit: milliseconds.
        self.capture_time = capture_time
        # The information about the rules that evaluated the resource and the compliance evaluation result.
        self.configuration = configuration
        # The details of the resource change that triggered the compliance evaluation.
        self.configuration_diff = configuration_diff
        # The ID of the region in which the resource resides.
        self.region = region
        # The timestamp when the resource was created. Unit: milliseconds.
        self.resource_create_time = resource_create_time
        # The ID of the resource.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name
        # The status of the resource. The parameter value varies based on the resource type and may be left empty. Examples:
        # 
        # *   If the ResourceType parameter is set to ACS::ECS::Instance, the resource is an Elastic Compute Service (ECS) instance that has a specific state. In this case, the valid values of this parameter are Running and Stopped.
        # *   If the ResourceType parameter is set to ACS::OSS::Bucket, the resource is an OSS bucket that does not have a specific state. In this case, this parameter is left empty.
        self.resource_status = resource_status
        # The type of the resource.
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

        if self.configuration is not None:
            result['Configuration'] = self.configuration

        if self.configuration_diff is not None:
            result['ConfigurationDiff'] = self.configuration_diff

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')

        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')

        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')

        if m.get('ConfigurationDiff') is not None:
            self.configuration_diff = m.get('ConfigurationDiff')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')

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

        return self

