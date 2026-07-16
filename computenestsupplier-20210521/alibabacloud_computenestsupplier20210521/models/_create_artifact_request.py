# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class CreateArtifactRequest(DaraModel):
    def __init__(
        self,
        artifact_build_property: main_models.CreateArtifactRequestArtifactBuildProperty = None,
        artifact_build_type: str = None,
        artifact_id: str = None,
        artifact_property: main_models.CreateArtifactRequestArtifactProperty = None,
        artifact_type: str = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        resource_group_id: str = None,
        support_region_ids: List[str] = None,
        tag: List[main_models.CreateArtifactRequestTag] = None,
        version_name: str = None,
    ):
        # The content used to build the artifact. This parameter is used for managed artifact builds.
        self.artifact_build_property = artifact_build_property
        # The type of the artifact to be built. Valid values:
        # 
        # - EcsImage: builds an ECS image.
        # 
        # - Dockerfile: builds a container image based on a Dockerfile.
        # 
        # - Buildpacks: builds a container image based on Buildpacks.
        # 
        # - ContainerImage: builds a container image by renaming an existing container image.
        self.artifact_build_type = artifact_build_type
        # The artifact ID.
        # 
        # This parameter is required to create a new version of an existing artifact.
        # 
        # You can call the [ListArtifacts](https://help.aliyun.com/document_detail/469993.html) operation to obtain the artifact ID.
        self.artifact_id = artifact_id
        # The content of the artifact.
        self.artifact_property = artifact_property
        # The artifact type.
        # 
        # Valid values:
        # 
        # - EcsImage: an ECS image artifact.
        # 
        # - AcrImage: a container image artifact.
        # 
        # - File: an Object Storage Service (OSS) file artifact.
        # 
        # - Script: a script artifact.
        # 
        # - HelmChart: a Helm chart artifact.
        # 
        # This parameter is required.
        self.artifact_type = artifact_type
        # Ensures the idempotence of the request.
        self.client_token = client_token
        # The description of the artifact.
        self.description = description
        # The artifact name.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The regions where the image can be distributed.
        self.support_region_ids = support_region_ids
        # The custom tags.
        self.tag = tag
        # The name of the artifact version.
        # 
        # This parameter is required.
        self.version_name = version_name

    def validate(self):
        if self.artifact_build_property:
            self.artifact_build_property.validate()
        if self.artifact_property:
            self.artifact_property.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_build_property is not None:
            result['ArtifactBuildProperty'] = self.artifact_build_property.to_map()

        if self.artifact_build_type is not None:
            result['ArtifactBuildType'] = self.artifact_build_type

        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id

        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property.to_map()

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
            temp_model = main_models.CreateArtifactRequestArtifactBuildProperty()
            self.artifact_build_property = temp_model.from_map(m.get('ArtifactBuildProperty'))

        if m.get('ArtifactBuildType') is not None:
            self.artifact_build_type = m.get('ArtifactBuildType')

        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')

        if m.get('ArtifactProperty') is not None:
            temp_model = main_models.CreateArtifactRequestArtifactProperty()
            self.artifact_property = temp_model.from_map(m.get('ArtifactProperty'))

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
                temp_model = main_models.CreateArtifactRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class CreateArtifactRequestTag(DaraModel):
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

class CreateArtifactRequestArtifactProperty(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_version: str = None,
        image_id: str = None,
        region_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_type: str = None,
        tag: str = None,
        url: str = None,
    ):
        # The commodity code of the product in Alibaba Cloud Marketplace.
        # 
        # Obtain the commodity code in the [Alibaba Cloud Marketplace console](https://market.console.aliyun.com/?spm=a2c4g.11186623.0.0.599d6787eMBBxu#/apiTools?_k=d7j8gk).
        # 
        # > This parameter can be set only when the artifact is an image artifact.
        self.commodity_code = commodity_code
        # The version of the product in Alibaba Cloud Marketplace.
        # 
        # View the product version on the [Alibaba Cloud Marketplace](https://market.aliyun.com/?spm=5176.24779694.0.0.b2144d22sksKM5) page.
        # 
        # > This parameter can be set only when the artifact is an image artifact.
        self.commodity_version = commodity_version
        # The image ID.
        # 
        # After you specify a region ID, call the [DescribeImages](https://help.aliyun.com/document_detail/2679797.html) operation to view the available image IDs in the specified region.
        # 
        # > This parameter can be set only when the artifact is an image artifact.
        self.image_id = image_id
        # The region of the image.
        # 
        # > This parameter can be set only when the artifact is an image artifact.
        self.region_id = region_id
        # The ID of the image repository.
        # 
        # Call the [ListAcrImageRepositories](https://help.aliyun.com/document_detail/2539919.html) operation to obtain the image repository ID.
        # 
        # > This parameter can be set only when the artifact is a container image artifact or a Helm chart artifact.
        self.repo_id = repo_id
        # The name of the image repository.
        # 
        # > This parameter can be set only when the artifact is a container image artifact or a Helm chart artifact.
        self.repo_name = repo_name
        # The type of the repository. Valid values: Public and Private.
        self.repo_type = repo_type
        # The version of the image in the image repository.
        # 
        # Call the [ListAcrImageTags](https://help.aliyun.com/document_detail/2539920.html) operation to obtain the version of the image in the image repository.
        # 
        # > This parameter can be set only when the artifact is a container image artifact or a Helm chart artifact.
        self.tag = tag
        # The URL of the file artifact.
        # 
        # Upload a file and obtain its URL in the [Object Storage Service console](https://oss.console.aliyun.com/bucket).
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_version is not None:
            result['CommodityVersion'] = self.commodity_version

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_type is not None:
            result['RepoType'] = self.repo_type

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityVersion') is not None:
            self.commodity_version = m.get('CommodityVersion')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class CreateArtifactRequestArtifactBuildProperty(DaraModel):
    def __init__(
        self,
        build_args: List[main_models.CreateArtifactRequestArtifactBuildPropertyBuildArgs] = None,
        code_repo: main_models.CreateArtifactRequestArtifactBuildPropertyCodeRepo = None,
        command_content: str = None,
        command_type: str = None,
        dockerfile_path: str = None,
        enable_gpu: bool = None,
        region_id: str = None,
        source_container_image: str = None,
        source_image_id: str = None,
        system_disk_size: int = None,
    ):
        # The build arguments.
        # 
        # > This parameter can be set only when ArtifactBuildType is set to Dockerfile.
        self.build_args = build_args
        # The code repository address.
        # 
        # > This parameter can be set only when ArtifactBuildType is set to Dockerfile or Buildpacks.
        self.code_repo = code_repo
        # The content of the command.
        # 
        # > This parameter can be set only when the artifact is an ECS image artifact.
        self.command_content = command_content
        # The command type. Valid values:
        # 
        # - RunBatScript: The command is a BAT script that runs on a Windows instance.
        # 
        # - RunPowerShellScript: The command is a PowerShell script that runs on a Windows instance.
        # 
        # - RunShellScript: The command is a shell script that runs on a Linux instance.
        # 
        # > This parameter can be set only when the artifact is an ECS image artifact.
        self.command_type = command_type
        # The relative address of the Dockerfile file in the code repository.
        # 
        # Default value: Dockerfile.
        # 
        # > This parameter can be set only when ArtifactBuildType is set to Dockerfile.
        self.dockerfile_path = dockerfile_path
        # Specifies whether to use a GPU-accelerated instance. By default, a CPU-powered instance is used.
        self.enable_gpu = enable_gpu
        # The ID of the region where the source image is located.
        # 
        # > This parameter can be set only when the artifact is an ECS image artifact.
        self.region_id = region_id
        # The pull address of the source container image.
        # 
        # Used for docker pull ${SourceContainerImage}.
        # 
        # > This parameter can be set only when ArtifactBuildType is set to ContainerImage.
        self.source_container_image = source_container_image
        # The source image ID. The following types are supported:
        # 
        # - Image ID: The ID of the ECS image.
        # 
        # - OOS public parameter name: The image ID is automatically obtained based on the name of the Operation Orchestration Service (OOS) public parameter.
        # 
        # > This parameter can be set only when the artifact is an ECS image artifact.
        self.source_image_id = source_image_id
        # The size of the system disk. Unit: GiB.
        self.system_disk_size = system_disk_size

    def validate(self):
        if self.build_args:
            for v1 in self.build_args:
                 if v1:
                    v1.validate()
        if self.code_repo:
            self.code_repo.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BuildArgs'] = []
        if self.build_args is not None:
            for k1 in self.build_args:
                result['BuildArgs'].append(k1.to_map() if k1 else None)

        if self.code_repo is not None:
            result['CodeRepo'] = self.code_repo.to_map()

        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.command_type is not None:
            result['CommandType'] = self.command_type

        if self.dockerfile_path is not None:
            result['DockerfilePath'] = self.dockerfile_path

        if self.enable_gpu is not None:
            result['EnableGpu'] = self.enable_gpu

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_container_image is not None:
            result['SourceContainerImage'] = self.source_container_image

        if self.source_image_id is not None:
            result['SourceImageId'] = self.source_image_id

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_args = []
        if m.get('BuildArgs') is not None:
            for k1 in m.get('BuildArgs'):
                temp_model = main_models.CreateArtifactRequestArtifactBuildPropertyBuildArgs()
                self.build_args.append(temp_model.from_map(k1))

        if m.get('CodeRepo') is not None:
            temp_model = main_models.CreateArtifactRequestArtifactBuildPropertyCodeRepo()
            self.code_repo = temp_model.from_map(m.get('CodeRepo'))

        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')

        if m.get('DockerfilePath') is not None:
            self.dockerfile_path = m.get('DockerfilePath')

        if m.get('EnableGpu') is not None:
            self.enable_gpu = m.get('EnableGpu')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceContainerImage') is not None:
            self.source_container_image = m.get('SourceContainerImage')

        if m.get('SourceImageId') is not None:
            self.source_image_id = m.get('SourceImageId')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

class CreateArtifactRequestArtifactBuildPropertyCodeRepo(DaraModel):
    def __init__(
        self,
        branch: str = None,
        endpoint: str = None,
        org_id: str = None,
        owner: str = None,
        platform: str = None,
        repo_id: int = None,
        repo_name: str = None,
    ):
        # The name of the code repository branch.
        self.branch = branch
        # The endpoint. This parameter is required for a private GitLab deployment.
        self.endpoint = endpoint
        # The organization ID.
        self.org_id = org_id
        # The owner of the code repository.
        # 
        # > This parameter is required only when the code repository is a private repository.
        self.owner = owner
        # The platform where the code repository is located. Valid values:
        # 
        # - github
        # 
        # - gitee
        # 
        # - gitlab
        # 
        # - codeup
        self.platform = platform
        # The repository ID.
        self.repo_id = repo_id
        # The repository name.
        self.repo_name = repo_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch is not None:
            result['Branch'] = self.branch

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        return self

class CreateArtifactRequestArtifactBuildPropertyBuildArgs(DaraModel):
    def __init__(
        self,
        argument_name: str = None,
        argument_value: str = None,
    ):
        # The name of the build argument.
        self.argument_name = argument_name
        # The value of the build argument.
        self.argument_value = argument_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.argument_name is not None:
            result['ArgumentName'] = self.argument_name

        if self.argument_value is not None:
            result['ArgumentValue'] = self.argument_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgumentName') is not None:
            self.argument_name = m.get('ArgumentName')

        if m.get('ArgumentValue') is not None:
            self.argument_value = m.get('ArgumentValue')

        return self

