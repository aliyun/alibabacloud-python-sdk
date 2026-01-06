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
        self.client_token = client_token
        # 镜像构建的可见性，可能值： - PUBLIC：当前工作空间所有成员都可以操作。 - PRIVATE：只有创建者可以操作。
        self.accessibility = accessibility
        # 构建配置，指定待构建的 Dockerfile 文件内容。
        # 
        # This parameter is required.
        self.build_config = build_config
        # This parameter is required.
        self.image = image
        self.image_build_job_name = image_build_job_name
        # 是否覆盖更新 ACR 镜像仓库中已存在的镜像 tag。
        self.overwrite_image_tag = overwrite_image_tag
        # 代表region的资源属性字段
        self.region_id = region_id
        # 构建任务运行资源
        # 
        # This parameter is required.
        self.resource = resource
        # This parameter is required.
        self.target_registry = target_registry
        # 用户专有网络信息。使用企业版 ACR 实例时，此参数必填，指定在用户 ACR 实例的访问控制里已添加的专有网络。
        self.user_vpc = user_vpc
        # 镜像构建所属的工作空间ID。
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
        # 默认路由网卡出口
        self.default_route = default_route
        # 扩展网段
        self.extended_cidrs = extended_cidrs
        # 安全组 ID
        self.security_group_id = security_group_id
        # 交换机 ID
        self.switch_id = switch_id
        # 专有网络 ID
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
        self.instance_id = instance_id
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
        # 后付费资源规格
        self.ecs_spec = ecs_spec
        self.resource_config = resource_config
        self.resource_id = resource_id
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
        self.cpu = cpu
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
        self.description = description
        self.labels = labels
        # This parameter is required.
        self.name = name
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
        self.key = key
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
        # This parameter is required.
        self.build_type = build_type
        # Dockerfile文件内容
        # 
        # This parameter is required.
        self.dockerfile = dockerfile
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

