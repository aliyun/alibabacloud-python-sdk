# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetResourceConfigurationSampleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sample: main_models.GetResourceConfigurationSampleResponseBodySample = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The sample.
        self.sample = sample

    def validate(self):
        if self.sample:
            self.sample.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sample is not None:
            result['Sample'] = self.sample.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Sample') is not None:
            temp_model = main_models.GetResourceConfigurationSampleResponseBodySample()
            self.sample = temp_model.from_map(m.get('Sample'))

        return self

class GetResourceConfigurationSampleResponseBodySample(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        availability_zone: str = None,
        configuration: str = None,
        region: str = None,
        resource_creation_time: str = None,
        resource_deleted: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
        resource_type: str = None,
        tags: str = None,
        version: str = None,
    ):
        # The user ID.
        self.account_id = account_id
        # The zone.
        self.availability_zone = availability_zone
        # The complete configuration information of the resource.
        self.configuration = configuration
        # The region ID.
        self.region = region
        # The time when the resource was created.
        self.resource_creation_time = resource_creation_time
        # The deletion status of the resource. Valid values:
        # 
        # - 1: The resource is retained.
        # 
        # - 0: The resource is deleted.
        self.resource_deleted = resource_deleted
        # The resource ID.
        self.resource_id = resource_id
        # The resource name.
        self.resource_name = resource_name
        # The resource status.
        self.resource_status = resource_status
        # The resource type.
        self.resource_type = resource_type
        # The tag.
        self.tags = tags
        # The version information.
        self.version = version

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

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')

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

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

