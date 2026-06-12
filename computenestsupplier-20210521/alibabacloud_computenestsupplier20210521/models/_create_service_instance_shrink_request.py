# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class CreateServiceInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        end_time: str = None,
        name: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_id: str = None,
        service_version: str = None,
        specification_name: str = None,
        tag: List[main_models.CreateServiceInstanceShrinkRequestTag] = None,
        template_name: str = None,
        user_id: str = None,
    ):
        # A client token to ensure the idempotence of the request. Generate a unique value for this parameter from your client. The token can be up to 64 characters in length and can contain only ASCII characters.
        self.client_token = client_token
        # Specifies whether to perform a dry run. A dry run checks for permissions and instance status. Valid values:
        # 
        # - true: The system checks the request but does not create the service instance.
        # 
        # - false: The system sends the request. If the request passes the check, the service instance is created.
        self.dry_run = dry_run
        # The time when the service instance is released.
        # 
        # > Only service providers can set this parameter for their own service instances in managed scenarios.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.end_time = end_time
        # The name of the service instance. The name must meet the following requirements:
        # 
        # - It can be up to 64 characters in length.
        # 
        # - It must start with a letter or a digit and can contain letters, digits, hyphens (-), and underscores (_).
        self.name = name
        # The parameters used to deploy the service instance.
        # 
        # > If the service instance includes information about the deployment region, specify that information in the deployment parameters.
        self.parameters_shrink = parameters_shrink
        # The ID of the region. Valid values:
        # 
        # - cn-hangzhou: China (Hangzhou)
        # 
        # - ap-southeast-1: Singapore
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the service.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The version of the service.
        self.service_version = service_version
        # The name of the specification package.
        self.specification_name = specification_name
        # The custom tags.
        self.tag = tag
        # The name of the template. Specify this parameter if the service supports multiple templates.
        self.template_name = template_name
        # The ID of the user.
        self.user_id = user_id

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.name is not None:
            result['Name'] = self.name

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateServiceInstanceShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class CreateServiceInstanceShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

