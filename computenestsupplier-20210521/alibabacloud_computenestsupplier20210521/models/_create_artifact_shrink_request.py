# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class CreateArtifactShrinkRequest(DaraModel):
    def __init__(
        self,
        artifact_build_property_shrink: str = None,
        artifact_build_type: str = None,
        artifact_id: str = None,
        artifact_property_shrink: str = None,
        artifact_type: str = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        resource_group_id: str = None,
        support_region_ids: List[str] = None,
        tag: List[main_models.CreateArtifactShrinkRequestTag] = None,
        version_name: str = None,
    ):
        # The build properties of the artifact, utilized for hosting and building the deployment package.
        self.artifact_build_property_shrink = artifact_build_property_shrink
        # The type of the artifact build task. Valid values:
        # 
        # - EcsImage: Build ECS (Elastic Container Service) image.
        # 
        # - Dockerfile: Build container image based on Dockerfile.
        # 
        # - Buildpacks: Build container image based on Buildpacks.
        # 
        # - ContainerImage: Rebuild container image by renaming an existing container image.
        self.artifact_build_type = artifact_build_type
        # The ID of the deployment package.
        self.artifact_id = artifact_id
        # The properties of the deployment object.
        self.artifact_property_shrink = artifact_property_shrink
        # The type of the deployment package. Valid values:
        # 
        # *   EcsImage: Elastic Compute Service (ECS) image.
        # *   AcrImage: container image.
        # *   File: Object Storage Service (OSS) object.
        # *   Script: script.
        # 
        # This parameter is required.
        self.artifact_type = artifact_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The description of the deployment package.
        self.description = description
        # The name of the deployment package.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The supported regions.
        self.support_region_ids = support_region_ids
        # The custom tags.
        self.tag = tag
        # The version name of the deployment package.
        # 
        # This parameter is required.
        self.version_name = version_name

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
        if self.artifact_build_property_shrink is not None:
            result['ArtifactBuildProperty'] = self.artifact_build_property_shrink

        if self.artifact_build_type is not None:
            result['ArtifactBuildType'] = self.artifact_build_type

        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id

        if self.artifact_property_shrink is not None:
            result['ArtifactProperty'] = self.artifact_property_shrink

        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactBuildProperty') is not None:
            self.artifact_build_property_shrink = m.get('ArtifactBuildProperty')

        if m.get('ArtifactBuildType') is not None:
            self.artifact_build_type = m.get('ArtifactBuildType')

        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')

        if m.get('ArtifactProperty') is not None:
            self.artifact_property_shrink = m.get('ArtifactProperty')

        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateArtifactShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class CreateArtifactShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

