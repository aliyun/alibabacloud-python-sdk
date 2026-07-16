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
        # An idempotence token.
        self.client_token = client_token
        # The visibility of the image.
        # 
        # - **PUBLIC**: The image is public.
        # 
        # - **PRIVATE**: The image is private.
        self.accessibility = accessibility
        # **The build configuration. Specify the content of the Dockerfile to be built.**
        # 
        # This parameter is required.
        self.build_config = build_config
        # The metadata of the image.
        # 
        # This parameter is required.
        self.image = image
        # The name of the image build task.
        self.image_build_job_name = image_build_job_name
        # Specifies whether to overwrite an existing image version in the image repository.
        self.overwrite_image_tag = overwrite_image_tag
        # The region ID.
        self.region_id = region_id
        # The resources used to run the task.
        # 
        # This parameter is required.
        self.resource = resource
        # **The configuration of the target image repository.**
        # 
        # This parameter is required.
        self.target_registry = target_registry
        # The information about the user\\"s virtual private cloud (VPC). This parameter is required when you use the public resource group.
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
        # The default route.
        # 
        # - eth1: Indicates that the user\\"s elastic network interface (ENI) is used to access the external network through a private gateway. For more information, see [Configure a Distribution Switch (DSW) instance to access the Internet through a private NAT gateway](https://help.aliyun.com/zh/pai/user-guide/configure-a-dsw-instance-to-access-the-internet-through-a-private-nat-gateway?spm=a2c4g.11186623.0.0.3b3965f6SZWm85).
        self.default_route = default_route
        # The extended CIDR blocks.
        # 
        # - If you do not specify a vSwitch ID, you can leave this parameter empty. The system automatically obtains all CIDR blocks of the VPC.
        # 
        # - If you specify a vSwitch ID, you must specify this parameter. For best results, include all CIDR blocks of the VPC.
        self.extended_cidrs = extended_cidrs
        # The security group ID. This parameter is required when you configure a VPC.
        self.security_group_id = security_group_id
        # The vSwitch ID. This parameter is optional.
        self.switch_id = switch_id
        # The VPC ID. If the build task needs to access your ACR Enterprise Edition instance, specify a VPC that is in the access control list of the instance.
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
        # The ID of the image repository instance. This parameter is required when you use ACR as the image repository.
        self.instance_id = instance_id
        # The type of the target image repository. Only ACR Enterprise Edition is supported.
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
        # The instance type of the pay-as-you-go resource. This parameter is required when you use the public resource group.
        self.ecs_spec = ecs_spec
        # The resource configuration. Specify this parameter when you use subscription resources. Leave it empty when you use the public resource group.
        self.resource_config = resource_config
        # The resource quota ID. This parameter applies only to subscription resources. Do not set this parameter for pay-as-you-go resources.
        self.resource_id = resource_id
        # The type of the subscription resource. Currently, only Lingjun resources are supported. Specify this parameter when you use subscription resources.
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
        # The memory size.
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
        # The description of the image.
        self.description = description
        # The image labels.
        self.labels = labels
        # The name of the image. The name must meet the following requirements:
        # 
        # - The name must be 1 to 50 characters in length.
        # 
        # - The name can contain lowercase letters, digits, and hyphens (-). It must start with a letter.
        # 
        # - The name must be unique within the same workspace.
        # 
        # This parameter is required.
        self.name = name
        # The image URL.
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
        dockerfile: str = None,
        registry_auths: Dict[str, Any] = None,
    ):
        # The build type. The following types are supported:
        # 
        # - **PackageInstallation**: Installs software packages based on a specified image.
        # 
        # - **CustomDockerfile**: Builds an image based on a custom Dockerfile.
        # 
        # This parameter is required.
        self.build_type = build_type
        # The content of the Dockerfile to be built.
        # 
        # This parameter is required.
        self.dockerfile = dockerfile
        # The authentication information for the private image repository. You can specify the authentication information for an ACR image repository that does not belong to you. The format is \\`{"user_registry_domain":{"Auth":"base64 encoded auth"}}\\`.
        self.registry_auths = registry_auths

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_type is not None:
            result['BuildType'] = self.build_type

        if self.dockerfile is not None:
            result['Dockerfile'] = self.dockerfile

        if self.registry_auths is not None:
            result['RegistryAuths'] = self.registry_auths

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildType') is not None:
            self.build_type = m.get('BuildType')

        if m.get('Dockerfile') is not None:
            self.dockerfile = m.get('Dockerfile')

        if m.get('RegistryAuths') is not None:
            self.registry_auths = m.get('RegistryAuths')

        return self

