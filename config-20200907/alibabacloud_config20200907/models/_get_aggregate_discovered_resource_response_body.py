# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetAggregateDiscoveredResourceResponseBody(DaraModel):
    def __init__(
        self,
        discovered_resource_detail: main_models.GetAggregateDiscoveredResourceResponseBodyDiscoveredResourceDetail = None,
        request_id: str = None,
    ):
        # The details of the resource.
        self.discovered_resource_detail = discovered_resource_detail
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_detail:
            self.discovered_resource_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discovered_resource_detail is not None:
            result['DiscoveredResourceDetail'] = self.discovered_resource_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscoveredResourceDetail') is not None:
            temp_model = main_models.GetAggregateDiscoveredResourceResponseBodyDiscoveredResourceDetail()
            self.discovered_resource_detail = temp_model.from_map(m.get('DiscoveredResourceDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAggregateDiscoveredResourceResponseBodyDiscoveredResourceDetail(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        availability_zone: str = None,
        compliance_type: str = None,
        configuration: str = None,
        region: str = None,
        resource_creation_time: int = None,
        resource_deleted: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
        resource_type: str = None,
        tags: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.account_id = account_id
        # The ID of the zone in which the resource resides.
        self.availability_zone = availability_zone
        # The compliance evaluation result of the resource. Valid values:
        # 
        # *   COMPLIANT: The resource is evaluated as compliant.
        # *   NON_COMPLIANT: The resource is evaluated as non-compliant.
        # *   NOT_APPLICABLE: The rule does not apply to the resource.
        # *   INSUFFICIENT_DATA: No data is available.
        # *   IGNORED: The resource is ignored during compliance evaluation.
        self.compliance_type = compliance_type
        # The configuration of the resource.
        self.configuration = configuration
        # The region ID.
        self.region = region
        # The timestamp when the resource was created.
        self.resource_creation_time = resource_creation_time
        # Indicates whether the resource was deleted. Valid values:
        # 
        # *   1: The resource was not deleted.
        # *   0: The resource was deleted.
        self.resource_deleted = resource_deleted
        # The resource ID.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name
        # The status of the resource. The value of this parameter varies based on the resource type and may be empty.
        # 
        # *   If the ResourceType parameter is set to ACS::ECS::Instance, the resource is an ECS instance that has a specific state. In this case, the valid values of this parameter are Running and Stopped.
        # *   If the ResourceType parameter is ACS::OSS::Bucket, the resource is an Object Storage Service (OSS) bucket that is not in a specific state. In this case, this parameter is left empty.
        self.resource_status = resource_status
        # The type of the resource.
        self.resource_type = resource_type
        # The tags of the resource.
        self.tags = tags
        # This parameter is required.
        self.v_switch_id = v_switch_id
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

        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.configuration is not None:
            result['Configuration'] = self.configuration

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_creation_time is not None:
            result['ResourceCreationTime'] = self.resource_creation_time

        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted

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

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')

        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceCreationTime') is not None:
            self.resource_creation_time = m.get('ResourceCreationTime')

        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')

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

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

