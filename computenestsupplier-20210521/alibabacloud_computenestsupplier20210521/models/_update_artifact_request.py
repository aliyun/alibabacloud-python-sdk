# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class UpdateArtifactRequest(DaraModel):
    def __init__(
        self,
        artifact_build_property: main_models.UpdateArtifactRequestArtifactBuildProperty = None,
        artifact_id: str = None,
        artifact_property: main_models.UpdateArtifactRequestArtifactProperty = None,
        client_token: str = None,
        description: str = None,
        permission_type: str = None,
        support_region_ids: List[str] = None,
        version_name: str = None,
    ):
        # The properties for building the artifact. This is used for managed artifact builds.
        self.artifact_build_property = artifact_build_property
        # The ID of the artifact.
        # 
        # To obtain the artifact ID, call the [ListArtifacts](https://help.aliyun.com/document_detail/469993.html) operation.
        # 
        # This parameter is required.
        self.artifact_id = artifact_id
        # The properties of the artifact.
        self.artifact_property = artifact_property
        # A client token to ensure the idempotence of the request. Generate a unique token for each request from your client. The **ClientToken** can contain only ASCII characters and must be no more than 64 characters long.
        self.client_token = client_token
        # The description of the artifact.
        self.description = description
        # The permission type. This parameter is valid for container image artifacts and Helm Chart artifacts. The value can be changed only from \\`Automatic\\` to \\`Public\\`. Valid values:
        # 
        # - Public
        # 
        # - Automatic
        self.permission_type = permission_type
        # The IDs of regions to which the image can be distributed.
        self.support_region_ids = support_region_ids
        # The name of the artifact version.
        self.version_name = version_name

    def validate(self):
        if self.artifact_build_property:
            self.artifact_build_property.validate()
        if self.artifact_property:
            self.artifact_property.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_build_property is not None:
            result['ArtifactBuildProperty'] = self.artifact_build_property.to_map()

        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id

        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property.to_map()

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type

        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactBuildProperty') is not None:
            temp_model = main_models.UpdateArtifactRequestArtifactBuildProperty()
            self.artifact_build_property = temp_model.from_map(m.get('ArtifactBuildProperty'))

        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')

        if m.get('ArtifactProperty') is not None:
            temp_model = main_models.UpdateArtifactRequestArtifactProperty()
            self.artifact_property = temp_model.from_map(m.get('ArtifactProperty'))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')

        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class UpdateArtifactRequestArtifactProperty(DaraModel):
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
        # The code of the Alibaba Cloud Marketplace product.
        # 
        # You can obtain the product code in the [Alibaba Cloud Marketplace console](https://market.console.aliyun.com/?spm=a2c4g.11186623.0.0.599d6787eMBBxu#/apiTools?_k=d7j8gk).
        # 
        # > This parameter is available only for image artifacts.
        self.commodity_code = commodity_code
        # The version of the Alibaba Cloud Marketplace product.
        # 
        # You can view the product version on the [Alibaba Cloud Marketplace page](https://market.aliyun.com/?spm=5176.24779694.0.0.b2144d22sksKM5).
        # 
        # > This parameter is available only for image artifacts.
        self.commodity_version = commodity_version
        # The ID of the image.
        # 
        # After you specify a region ID, call the [DescribeImages](https://help.aliyun.com/document_detail/2679797.html) operation to query available image IDs in that region.
        # 
        # > This parameter is available only for image artifacts.
        self.image_id = image_id
        # The region of the image.
        # 
        # > This parameter is available only for image artifacts.
        self.region_id = region_id
        # The ID of the image repository.
        # 
        # To obtain the image repository ID, call the [ListAcrImageRepositories](https://help.aliyun.com/document_detail/2539919.html) operation.
        # 
        # > This parameter is available only for container image artifacts and Helm Chart artifacts.
        self.repo_id = repo_id
        # The name of the image repository.
        # 
        # > This parameter is available only for container image artifacts and Helm Chart artifacts.
        self.repo_name = repo_name
        # The permission type of the repository. Valid values:
        # 
        # - `Public`: public repository
        # 
        # - `Private`: private repository
        # 
        # > This parameter is available only for container image artifacts and Helm Chart artifacts.
        self.repo_type = repo_type
        # The version tag of the image in the repository.
        # 
        # To obtain the version tag, call the [ListAcrImageTags](https://help.aliyun.com/document_detail/2539920.html) operation.
        # 
        # > This parameter is available only for container image artifacts and Helm Chart artifacts.
        self.tag = tag
        # The URL of the file artifact.
        # 
        # You can upload the file and obtain its URL in the [Object Storage Service console](https://oss.console.aliyun.com/bucket).
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

class UpdateArtifactRequestArtifactBuildProperty(DaraModel):
    def __init__(
        self,
        build_args: List[main_models.UpdateArtifactRequestArtifactBuildPropertyBuildArgs] = None,
        code_repo: main_models.UpdateArtifactRequestArtifactBuildPropertyCodeRepo = None,
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
        # > This parameter is available only when \\`ArtifactBuildType\\` is set to \\`Dockerfile\\`.
        self.build_args = build_args
        # The code repository address.
        # 
        # > This parameter is available only when \\`ArtifactBuildType\\` is set to \\`Dockerfile\\` or \\`Buildpacks\\`.
        self.code_repo = code_repo
        # The content of the command.
        # 
        # > This parameter is available only for ECS image artifacts.
        self.command_content = command_content
        # The command type. Valid values:
        # 
        # - RunBatScript: The command is a batch script that runs on a Windows instance.
        # 
        # - RunPowerShellScript: The command is a PowerShell script that runs on a Windows instance.
        # 
        # - RunShellScript: The command is a shell script that runs on a Linux instance.
        # 
        # > This parameter is available only for ECS image artifacts.
        self.command_type = command_type
        # The relative path of the Dockerfile in the code repository.
        # 
        # Default value: Dockerfile
        # 
        # > This parameter is available only when \\`ArtifactBuildType\\` is set to \\`Dockerfile\\`.
        self.dockerfile_path = dockerfile_path
        # Specifies whether to use a GPU-accelerated instance for the build. By default, a CPU instance is used.
        self.enable_gpu = enable_gpu
        # The ID of the region where the source image is located.
        # 
        # > This parameter is available only for ECS image artifacts.
        self.region_id = region_id
        # The pull URL of the source container image.
        # 
        # Used for \\`docker pull ${SourceContainerImage}\\`.
        # 
        # > This parameter is available only when \\`ArtifactBuildType\\` is set to \\`ContainerImage\\`.
        self.source_container_image = source_container_image
        # The source image ID. The following types are supported:
        # 
        # - Image ID: The ID of the ECS image.
        # 
        # - OOS common parameter name: The system automatically obtains the corresponding image ID based on the OOS common parameter name.
        # 
        # > This parameter is available only for ECS image artifacts.
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
                temp_model = main_models.UpdateArtifactRequestArtifactBuildPropertyBuildArgs()
                self.build_args.append(temp_model.from_map(k1))

        if m.get('CodeRepo') is not None:
            temp_model = main_models.UpdateArtifactRequestArtifactBuildPropertyCodeRepo()
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

class UpdateArtifactRequestArtifactBuildPropertyCodeRepo(DaraModel):
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
        # The branch name of the code repository.
        self.branch = branch
        # The endpoint. This parameter is required for a private GitLab deployment.
        self.endpoint = endpoint
        # The organization ID.
        self.org_id = org_id
        # The owner of the code repository.
        # 
        # > This parameter is required only if the code repository is private.
        self.owner = owner
        # The platform of the code repository. Valid values:
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

class UpdateArtifactRequestArtifactBuildPropertyBuildArgs(DaraModel):
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

