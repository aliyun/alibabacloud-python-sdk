# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateImageBuildRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        accessibility: str = None,
        build_config: main_models.CreateImageBuildRequestBuildConfig = None,
        image: main_models.CreateImageBuildRequestImage = None,
        image_build_job_name: str = None,
        overwrite_image_tag: bool = None,
        region_id: str = None,
        resource: main_models.CreateImageBuildRequestResource = None,
        target_registry: main_models.CreateImageBuildRequestTargetRegistry = None,
        user_vpc: main_models.CreateImageBuildRequestUserVpc = None,
        workspace_id: str = None,
    ):
        # The idempotency parameter.
        self.client_token = client_token
        # The visibility. Valid values:
        # - **PUBLIC**: Public.
        # - **PRIVATE**: Private.
        self.accessibility = accessibility
        # **The build configuration, which specifies the content of the Dockerfile to be built.**
        # 
        # This parameter is required.
        self.build_config = build_config
        # The image metadata.
        # 
        # This parameter is required.
        self.image = image
        # The name of the image build task.
        self.image_build_job_name = image_build_job_name
        # Specifies whether to overwrite the existing image version in the image repository.
        self.overwrite_image_tag = overwrite_image_tag
        # The region ID.
        self.region_id = region_id
        # The resources used to run the task.
        # 
        # This parameter is required.
        self.resource = resource
        # **The target registry configuration.**
        # 
        # This parameter is required.
        self.target_registry = target_registry
        # The user VPC information. This parameter is required when you use a public resource group.
        self.user_vpc = user_vpc
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.build_config:
            self.build_config.validate()
        if self.image:
            self.image.validate()
        if self.resource:
            self.resource.validate()
        if self.target_registry:
            self.target_registry.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.build_config is not None:
            result['BuildConfig'] = self.build_config.to_map()

        if self.image is not None:
            result['Image'] = self.image.to_map()

        if self.image_build_job_name is not None:
            result['ImageBuildJobName'] = self.image_build_job_name

        if self.overwrite_image_tag is not None:
            result['OverwriteImageTag'] = self.overwrite_image_tag

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        if self.target_registry is not None:
            result['TargetRegistry'] = self.target_registry.to_map()

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('BuildConfig') is not None:
            temp_model = main_models.CreateImageBuildRequestBuildConfig()
            self.build_config = temp_model.from_map(m.get('BuildConfig'))

        if m.get('Image') is not None:
            temp_model = main_models.CreateImageBuildRequestImage()
            self.image = temp_model.from_map(m.get('Image'))

        if m.get('ImageBuildJobName') is not None:
            self.image_build_job_name = m.get('ImageBuildJobName')

        if m.get('OverwriteImageTag') is not None:
            self.overwrite_image_tag = m.get('OverwriteImageTag')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            temp_model = main_models.CreateImageBuildRequestResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('TargetRegistry') is not None:
            temp_model = main_models.CreateImageBuildRequestTargetRegistry()
            self.target_registry = temp_model.from_map(m.get('TargetRegistry'))

        if m.get('UserVpc') is not None:
            temp_model = main_models.CreateImageBuildRequestUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateImageBuildRequestUserVpc(DaraModel):
    def __init__(
        self,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        security_group_id: str = None,
        switch_id: str = None,
        vpc_id: str = None,
    ):
        # The default routing of the network interface controller (NIC). Valid values:
        # * eth1: Uses the user\\"s elastic network interfaces (ENIs) to access external networks through a private NAT gateway. For the configuration method, refer to [Configure a DSW instance to access the Internet through a private NAT gateway](https://www.alibabacloud.com/help/en/pai/user-guide/configure-a-dsw-instance-to-access-the-internet-through-a-private-nat-gateway).
        self.default_route = default_route
        # The extended CIDR blocks.
        # * If the vSwitch ID is empty, this parameter is optional and the system automatically retrieves all CIDR blocks under the VPC.
        # * If the vSwitch ID is not empty, this parameter is required. We recommend that you specify all CIDR blocks under the VPC.
        self.extended_cidrs = extended_cidrs
        # The security group ID. This parameter is required when you specify the VPC configuration.
        self.security_group_id = security_group_id
        # The vSwitch ID. This parameter is optional.
        self.switch_id = switch_id
        # The VPC ID. When the build task accesses a user\\"s Container Registry Enterprise Edition instance, you must specify a VPC that is added to the access control list of the instance.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route

        if self.extended_cidrs is not None:
            result['ExtendedCidrs'] = self.extended_cidrs

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')

        if m.get('ExtendedCidrs') is not None:
            self.extended_cidrs = m.get('ExtendedCidrs')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateImageBuildRequestTargetRegistry(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        type: str = None,
    ):
        # The registry instance ID. This parameter is required when you use Container Registry (ACR) as the image service.
        self.instance_id = instance_id
        # The registry type. Only Container Registry Enterprise Edition is supported as the target registry.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateImageBuildRequestResource(DaraModel):
    def __init__(
        self,
        ecs_spec: str = None,
        resource_config: main_models.CreateImageBuildRequestResourceResourceConfig = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The pay-as-you-go resource specifications. This parameter is required when you use a public resource group.
        self.ecs_spec = ecs_spec
        # The resource configuration. This parameter is required when you use subscription resources and must be left empty when you use a public resource group.
        self.resource_config = resource_config
        # The resource quota ID. This parameter applies only to subscription resources and must not be specified when you use pay-as-you-go resources.
        self.resource_id = resource_id
        # The subscription resource type. Only Lingjun resources are supported. This parameter is required when you use subscription resources.
        self.resource_type = resource_type

    def validate(self):
        if self.resource_config:
            self.resource_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec

        if self.resource_config is not None:
            result['ResourceConfig'] = self.resource_config.to_map()

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')

        if m.get('ResourceConfig') is not None:
            temp_model = main_models.CreateImageBuildRequestResourceResourceConfig()
            self.resource_config = temp_model.from_map(m.get('ResourceConfig'))

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class CreateImageBuildRequestResourceResourceConfig(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        memory: str = None,
    ):
        # The number of CPU cores.
        self.cpu = cpu
        # The memory capacity.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

class CreateImageBuildRequestImage(DaraModel):
    def __init__(
        self,
        description: str = None,
        labels: List[main_models.CreateImageBuildRequestImageLabels] = None,
        name: str = None,
        uri: str = None,
    ):
        # The image description.
        self.description = description
        # The image labels.
        self.labels = labels
        # The image name. The naming rules are as follows:
        # * The name must be 1 to 50 characters in length.
        # * The name can contain lowercase letters, digits, and hyphens (-), and must start with a letter.
        # * The name must be unique within the same workspace.
        # 
        # This parameter is required.
        self.name = name
        # The image URI.
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.CreateImageBuildRequestImageLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class CreateImageBuildRequestImageLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the image label.
        self.key = key
        # The value of the image label.
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

class CreateImageBuildRequestBuildConfig(DaraModel):
    def __init__(
        self,
        build_type: str = None,
        data_sources: List[main_models.CreateImageBuildRequestBuildConfigDataSources] = None,
        dockerfile: str = None,
        dockerfile_path: str = None,
        registry_auths: Dict[str, Any] = None,
    ):
        # The build type. Valid values:
        # * **PackageInstallation**: Installs software packages based on a specified image.
        # * **CustomDockerfile**: Uses a custom Dockerfile.
        # 
        # This parameter is required.
        self.build_type = build_type
        # The list of data sources.
        self.data_sources = data_sources
        # The content of the Dockerfile to be built.
        self.dockerfile = dockerfile
        # The Dockerfile path, which is a relative path to the mounted context path. Example: docker/Dockerfile. If the mount path is /mnt/data/, the file is located at /mnt/data/docker/Dockerfile.
        self.dockerfile_path = dockerfile_path
        # The authentication information for private image repositories. You can specify the authentication information for an ACR image repository that does not belong to the current user. Format: {"user_registry_domain":{"Auth":"base64 encoded auth"}}.
        self.registry_auths = registry_auths

    def validate(self):
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_type is not None:
            result['BuildType'] = self.build_type

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.dockerfile is not None:
            result['Dockerfile'] = self.dockerfile

        if self.dockerfile_path is not None:
            result['DockerfilePath'] = self.dockerfile_path

        if self.registry_auths is not None:
            result['RegistryAuths'] = self.registry_auths

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildType') is not None:
            self.build_type = m.get('BuildType')

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.CreateImageBuildRequestBuildConfigDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('Dockerfile') is not None:
            self.dockerfile = m.get('Dockerfile')

        if m.get('DockerfilePath') is not None:
            self.dockerfile_path = m.get('DockerfilePath')

        if m.get('RegistryAuths') is not None:
            self.registry_auths = m.get('RegistryAuths')

        return self

class CreateImageBuildRequestBuildConfigDataSources(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_version: str = None,
        mount_access: str = None,
        mount_path: str = None,
        options: str = None,
        uri: str = None,
    ):
        # The ID of the dataset in the workspace. Example: d-************zbs.
        self.data_source_id = data_source_id
        # The dataset version. If you specify this parameter, you must also specify DataSourceId. Example: v1.
        self.data_source_version = data_source_version
        # The read and write permissions. Valid values: RW (default) and RO.
        self.mount_access = mount_access
        # The mount path. Example: /mnt/data/.
        self.mount_path = mount_path
        # The mount property for the custom dataset. Only OSS is supported. Example: {"fs.oss.download.thread.concurrency":"10"}.
        self.options = options
        # The storage path, including the endpoint. This parameter is mutually exclusive with DataSourceId. Example: OSS storage path oss://{bucket-name}.oss-{region}-internal.aliyuncs.com/{subPath}/.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_version is not None:
            result['DataSourceVersion'] = self.data_source_version

        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.options is not None:
            result['Options'] = self.options

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceVersion') is not None:
            self.data_source_version = m.get('DataSourceVersion')

        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

