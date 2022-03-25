# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class Cluster(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        config: str = None,
        name: str = None,
        nas: str = None,
        owner: str = None,
        private_container_path: str = None,
        private_nas_path: str = None,
        public_container_path: str = None,
        public_nas_path: str = None,
        state: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # 集群id
        self.cluster_id = cluster_id
        # 集群类型
        self.cluster_type = cluster_type
        # 集群配置
        self.config = config
        # 集群名称
        self.name = name
        # nas文件id
        self.nas = nas
        # 集群owner
        self.owner = owner
        # 个人nas挂载到容器路径
        self.private_container_path = private_container_path
        # 个人nas挂载路径
        self.private_nas_path = private_nas_path
        # 公共nas挂载到容器的路径
        self.public_container_path = public_container_path
        # 公共nas挂载路径
        self.public_nas_path = public_nas_path
        # 集群状态
        self.state = state
        # 集群vSwitch
        self.v_switch_id = v_switch_id
        # 集群vpc
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.nas is not None:
            result['Nas'] = self.nas
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.private_container_path is not None:
            result['PrivateContainerPath'] = self.private_container_path
        if self.private_nas_path is not None:
            result['PrivateNasPath'] = self.private_nas_path
        if self.public_container_path is not None:
            result['PublicContainerPath'] = self.public_container_path
        if self.public_nas_path is not None:
            result['PublicNasPath'] = self.public_nas_path
        if self.state is not None:
            result['State'] = self.state
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nas') is not None:
            self.nas = m.get('Nas')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PrivateContainerPath') is not None:
            self.private_container_path = m.get('PrivateContainerPath')
        if m.get('PrivateNasPath') is not None:
            self.private_nas_path = m.get('PrivateNasPath')
        if m.get('PublicContainerPath') is not None:
            self.public_container_path = m.get('PublicContainerPath')
        if m.get('PublicNasPath') is not None:
            self.public_nas_path = m.get('PublicNasPath')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class Config(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # 配置名称
        self.name = name
        # 配置数值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class Dataset(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
        default_mount_path: str = None,
        file_system_id: str = None,
        mount_path: str = None,
        name: str = None,
        nas_path: str = None,
    ):
        # 数据集id
        self.dataset_id = dataset_id
        # 默认挂载路径
        self.default_mount_path = default_mount_path
        # 文件系统Id
        self.file_system_id = file_system_id
        # 挂载路径
        self.mount_path = mount_path
        # 数据集名称
        self.name = name
        # 文件系统被挂载路径
        self.nas_path = nas_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.default_mount_path is not None:
            result['DefaultMountPath'] = self.default_mount_path
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.name is not None:
            result['Name'] = self.name
        if self.nas_path is not None:
            result['NasPath'] = self.nas_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DefaultMountPath') is not None:
            self.default_mount_path = m.get('DefaultMountPath')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NasPath') is not None:
            self.nas_path = m.get('NasPath')
        return self


class EcsSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        gpu: int = None,
        gpu_type: str = None,
        instance_type: str = None,
        memory_in_gi_b: int = None,
        system_disk_category: str = None,
        system_disk_size_in_gi_b: int = None,
    ):
        # cpu数量
        self.cpu = cpu
        # gpu卡数
        self.gpu = gpu
        # GPU卡类型
        self.gpu_type = gpu_type
        # 实例类型
        self.instance_type = instance_type
        # 内存(GiB)
        self.memory_in_gi_b = memory_in_gi_b
        # 磁盘类型
        self.system_disk_category = system_disk_category
        # 磁盘大小(GiB)
        self.system_disk_size_in_gi_b = system_disk_size_in_gi_b

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory_in_gi_b is not None:
            result['MemoryInGiB'] = self.memory_in_gi_b
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_size_in_gi_b is not None:
            result['SystemDiskSizeInGiB'] = self.system_disk_size_in_gi_b
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MemoryInGiB') is not None:
            self.memory_in_gi_b = m.get('MemoryInGiB')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskSizeInGiB') is not None:
            self.system_disk_size_in_gi_b = m.get('SystemDiskSizeInGiB')
        return self


class Image(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        author: str = None,
        cuda_version: str = None,
        description: str = None,
        ecs_image_key: str = None,
        framework: str = None,
        framework_version: str = None,
        from_image_id: str = None,
        from_image_name: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        instance_id: str = None,
        namespace: str = None,
        os: str = None,
        osversion: str = None,
        python_version: str = None,
        region: str = None,
        repository: str = None,
        repository_page: str = None,
        resource_type: int = None,
        root_image_id: str = None,
        shared: bool = None,
        short_image_url: str = None,
        short_repository: str = None,
        stage: str = None,
        stage_code: int = None,
        suggested_name: str = None,
        tag: str = None,
        type: str = None,
        workspace_image_id: str = None,
    ):
        # 资源类型
        self.accelerator_type = accelerator_type
        # 镜像作者
        self.author = author
        # Cuda版本
        self.cuda_version = cuda_version
        # 镜像描述
        self.description = description
        # Ecs镜像key
        self.ecs_image_key = ecs_image_key
        # 算法框架
        self.framework = framework
        # 算法框架版本
        self.framework_version = framework_version
        # 镜像父镜像
        self.from_image_id = from_image_id
        # 镜像名称
        self.from_image_name = from_image_name
        # 创建时间
        self.gmt_create_time = gmt_create_time
        # 修改时间
        self.gmt_modified_time = gmt_modified_time
        # 镜像ID
        self.image_id = image_id
        # 镜像名称
        self.image_name = image_name
        # 镜像url
        self.image_url = image_url
        # 实例ID
        self.instance_id = instance_id
        # 镜像命名空间
        self.namespace = namespace
        # 镜像操作系统分发版
        self.os = os
        # 分发版版本
        self.osversion = osversion
        # python版本
        self.python_version = python_version
        # 地区
        self.region = region
        # 镜像仓库
        self.repository = repository
        # 跳转的镜像站点页面
        self.repository_page = repository_page
        # 资源类型
        self.resource_type = resource_type
        # 镜像的根镜像
        self.root_image_id = root_image_id
        # 镜像是否被其他实例共享
        self.shared = shared
        # 镜像短url
        self.short_image_url = short_image_url
        # 镜像仓库短名称
        self.short_repository = short_repository
        # 镜像状态
        self.stage = stage
        # 镜像状态代码
        self.stage_code = stage_code
        # 保存镜像建议的名称
        self.suggested_name = suggested_name
        # Tag
        self.tag = tag
        # 镜像类型
        self.type = type
        # 工作空间镜像id
        self.workspace_image_id = workspace_image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.author is not None:
            result['Author'] = self.author
        if self.cuda_version is not None:
            result['CudaVersion'] = self.cuda_version
        if self.description is not None:
            result['Description'] = self.description
        if self.ecs_image_key is not None:
            result['EcsImageKey'] = self.ecs_image_key
        if self.framework is not None:
            result['Framework'] = self.framework
        if self.framework_version is not None:
            result['FrameworkVersion'] = self.framework_version
        if self.from_image_id is not None:
            result['FromImageId'] = self.from_image_id
        if self.from_image_name is not None:
            result['FromImageName'] = self.from_image_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.os is not None:
            result['OS'] = self.os
        if self.osversion is not None:
            result['OSVersion'] = self.osversion
        if self.python_version is not None:
            result['PythonVersion'] = self.python_version
        if self.region is not None:
            result['Region'] = self.region
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.repository_page is not None:
            result['RepositoryPage'] = self.repository_page
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.root_image_id is not None:
            result['RootImageId'] = self.root_image_id
        if self.shared is not None:
            result['Shared'] = self.shared
        if self.short_image_url is not None:
            result['ShortImageUrl'] = self.short_image_url
        if self.short_repository is not None:
            result['ShortRepository'] = self.short_repository
        if self.stage is not None:
            result['Stage'] = self.stage
        if self.stage_code is not None:
            result['StageCode'] = self.stage_code
        if self.suggested_name is not None:
            result['SuggestedName'] = self.suggested_name
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_image_id is not None:
            result['WorkspaceImageId'] = self.workspace_image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('CudaVersion') is not None:
            self.cuda_version = m.get('CudaVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcsImageKey') is not None:
            self.ecs_image_key = m.get('EcsImageKey')
        if m.get('Framework') is not None:
            self.framework = m.get('Framework')
        if m.get('FrameworkVersion') is not None:
            self.framework_version = m.get('FrameworkVersion')
        if m.get('FromImageId') is not None:
            self.from_image_id = m.get('FromImageId')
        if m.get('FromImageName') is not None:
            self.from_image_name = m.get('FromImageName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OS') is not None:
            self.os = m.get('OS')
        if m.get('OSVersion') is not None:
            self.osversion = m.get('OSVersion')
        if m.get('PythonVersion') is not None:
            self.python_version = m.get('PythonVersion')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('RepositoryPage') is not None:
            self.repository_page = m.get('RepositoryPage')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RootImageId') is not None:
            self.root_image_id = m.get('RootImageId')
        if m.get('Shared') is not None:
            self.shared = m.get('Shared')
        if m.get('ShortImageUrl') is not None:
            self.short_image_url = m.get('ShortImageUrl')
        if m.get('ShortRepository') is not None:
            self.short_repository = m.get('ShortRepository')
        if m.get('Stage') is not None:
            self.stage = m.get('Stage')
        if m.get('StageCode') is not None:
            self.stage_code = m.get('StageCode')
        if m.get('SuggestedName') is not None:
            self.suggested_name = m.get('SuggestedName')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceImageId') is not None:
            self.workspace_image_id = m.get('WorkspaceImageId')
        return self


class ImageNamespace(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        namespace_status: str = None,
    ):
        # 命名空间名称
        self.namespace = namespace
        # 命名空间状态
        self.namespace_status = namespace_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        return self


class ImageRepository(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_status: str = None,
        repository: str = None,
    ):
        # 创建时间
        self.gmt_create_time = gmt_create_time
        # 修改时间
        self.gmt_modified_time = gmt_modified_time
        # 地区Id
        self.region_id = region_id
        # 仓库名称
        self.repo_name = repo_name
        # 仓库命名空间
        self.repo_namespace = repo_namespace
        # 仓库状态
        self.repo_status = repo_status
        # 仓库地址
        self.repository = repository

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repository is not None:
            result['Repository'] = self.repository
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        return self


class InstanceShutdownTimer(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        schedule_time: str = None,
        ttl_in_millis: int = None,
    ):
        # 定时关机修改时间
        self.gmt_create_time = gmt_create_time
        # 定时关机创建时间
        self.gmt_modified_time = gmt_modified_time
        # 实例ID
        self.instance_id = instance_id
        # 定时关机时间
        self.schedule_time = schedule_time
        # 多少毫秒后定时关机（如果设定可以覆盖ScheduleTime）
        self.ttl_in_millis = ttl_in_millis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.ttl_in_millis is not None:
            result['TtlInMillis'] = self.ttl_in_millis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('TtlInMillis') is not None:
            self.ttl_in_millis = m.get('TtlInMillis')
        return self


class UserVpc(TeaModel):
    def __init__(
        self,
        role_arn: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # 角色标识码
        self.role_arn = role_arn
        # 安全组ID
        self.security_group_id = security_group_id
        # 虚拟网络ID
        self.vpc_id = vpc_id
        # 虚拟交换机ID
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class Instance(TeaModel):
    def __init__(
        self,
        accumulative_running_time_in_millis: int = None,
        accumulative_running_time_in_minutes: int = None,
        create_user: str = None,
        dataset_list: List[Dataset] = None,
        ecs_spec: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_type: str = None,
        image_url: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_shutdown_timer: InstanceShutdownTimer = None,
        instance_status: str = None,
        instance_url: str = None,
        instance_version: str = None,
        is_public: int = None,
        jupyterlab_url: str = None,
        message: str = None,
        nas_file_system_id: str = None,
        pay_type: int = None,
        pay_type_name: str = None,
        resource: str = None,
        resource_type: int = None,
        shutdown_enabled: bool = None,
        terminal_url: str = None,
        user_id: str = None,
        user_image_list: List[Image] = None,
        user_vpc: UserVpc = None,
        web_ide_url: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # 运行时间，毫秒数
        self.accumulative_running_time_in_millis = accumulative_running_time_in_millis
        # 累计运行时间(分钟)
        self.accumulative_running_time_in_minutes = accumulative_running_time_in_minutes
        # 创建者
        self.create_user = create_user
        # 数据集列表
        self.dataset_list = dataset_list
        # ecs规格
        self.ecs_spec = ecs_spec
        # 创建时间(GMT)
        self.gmt_create_time = gmt_create_time
        # 修改时间(GMT)
        self.gmt_modified_time = gmt_modified_time
        # 镜像ID
        self.image_id = image_id
        # 镜像名称
        self.image_name = image_name
        # 镜像类型
        self.image_type = image_type
        # 镜像链接
        self.image_url = image_url
        # 实例ID
        self.instance_id = instance_id
        # 实例名称
        self.instance_name = instance_name
        # 定时关机任务
        self.instance_shutdown_timer = instance_shutdown_timer
        # 实例状态
        self.instance_status = instance_status
        # dsw实例链接
        self.instance_url = instance_url
        # 实例版本
        self.instance_version = instance_version
        # 是否他人可见
        self.is_public = is_public
        # jupyter链接
        self.jupyterlab_url = jupyterlab_url
        # 错误消息
        self.message = message
        # nas文件系统ID
        self.nas_file_system_id = nas_file_system_id
        # 付费类型代码
        self.pay_type = pay_type
        # 付费类型名称
        self.pay_type_name = pay_type_name
        # 资源类型名称
        self.resource = resource
        # 资源类型代码
        self.resource_type = resource_type
        # 是否支持定时关机
        self.shutdown_enabled = shutdown_enabled
        # 命令行终端链接
        self.terminal_url = terminal_url
        # 用户ID
        self.user_id = user_id
        # 保存用户镜像列表
        self.user_image_list = user_image_list
        # 被打通VPC配置
        self.user_vpc = user_vpc
        # webIde链接
        self.web_ide_url = web_ide_url
        # 工作空间id
        self.workspace_id = workspace_id
        # 工作空间名称
        self.workspace_name = workspace_name

    def validate(self):
        if self.dataset_list:
            for k in self.dataset_list:
                if k:
                    k.validate()
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.user_image_list:
            for k in self.user_image_list:
                if k:
                    k.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accumulative_running_time_in_millis is not None:
            result['AccumulativeRunningTimeInMillis'] = self.accumulative_running_time_in_millis
        if self.accumulative_running_time_in_minutes is not None:
            result['AccumulativeRunningTimeInMinutes'] = self.accumulative_running_time_in_minutes
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        result['DatasetList'] = []
        if self.dataset_list is not None:
            for k in self.dataset_list:
                result['DatasetList'].append(k.to_map() if k else None)
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.instance_version is not None:
            result['InstanceVersion'] = self.instance_version
        if self.is_public is not None:
            result['IsPublic'] = self.is_public
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        if self.message is not None:
            result['Message'] = self.message
        if self.nas_file_system_id is not None:
            result['NasFileSystemId'] = self.nas_file_system_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pay_type_name is not None:
            result['PayTypeName'] = self.pay_type_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.shutdown_enabled is not None:
            result['ShutdownEnabled'] = self.shutdown_enabled
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        result['UserImageList'] = []
        if self.user_image_list is not None:
            for k in self.user_image_list:
                result['UserImageList'].append(k.to_map() if k else None)
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ide_url is not None:
            result['WebIdeUrl'] = self.web_ide_url
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccumulativeRunningTimeInMillis') is not None:
            self.accumulative_running_time_in_millis = m.get('AccumulativeRunningTimeInMillis')
        if m.get('AccumulativeRunningTimeInMinutes') is not None:
            self.accumulative_running_time_in_minutes = m.get('AccumulativeRunningTimeInMinutes')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        self.dataset_list = []
        if m.get('DatasetList') is not None:
            for k in m.get('DatasetList'):
                temp_model = Dataset()
                self.dataset_list.append(temp_model.from_map(k))
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = InstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('InstanceVersion') is not None:
            self.instance_version = m.get('InstanceVersion')
        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NasFileSystemId') is not None:
            self.nas_file_system_id = m.get('NasFileSystemId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PayTypeName') is not None:
            self.pay_type_name = m.get('PayTypeName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ShutdownEnabled') is not None:
            self.shutdown_enabled = m.get('ShutdownEnabled')
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        self.user_image_list = []
        if m.get('UserImageList') is not None:
            for k in m.get('UserImageList'):
                temp_model = Image()
                self.user_image_list.append(temp_model.from_map(k))
        if m.get('UserVpc') is not None:
            temp_model = UserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIdeUrl') is not None:
            self.web_ide_url = m.get('WebIdeUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class InstanceSnapshot(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        instance_snapshot_description: str = None,
        instance_snapshot_id: str = None,
        instance_snapshot_name: str = None,
        instance_snapshot_repo_url: str = None,
        instance_snapshot_status: str = None,
        instance_snapshot_tag: str = None,
    ):
        # 实例快照保存时间（GMT）
        self.gmt_create_time = gmt_create_time
        # 实例快照修改时间（GMT）
        self.gmt_modified_time = gmt_modified_time
        # 实例ID
        self.instance_id = instance_id
        # 实例快照描述
        self.instance_snapshot_description = instance_snapshot_description
        # 实例快照ID
        self.instance_snapshot_id = instance_snapshot_id
        # 实例快照名称
        self.instance_snapshot_name = instance_snapshot_name
        # 实例快照存储地址
        self.instance_snapshot_repo_url = instance_snapshot_repo_url
        # 实例快照状态
        self.instance_snapshot_status = instance_snapshot_status
        # 实例快照标签
        self.instance_snapshot_tag = instance_snapshot_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_snapshot_description is not None:
            result['InstanceSnapshotDescription'] = self.instance_snapshot_description
        if self.instance_snapshot_id is not None:
            result['InstanceSnapshotId'] = self.instance_snapshot_id
        if self.instance_snapshot_name is not None:
            result['InstanceSnapshotName'] = self.instance_snapshot_name
        if self.instance_snapshot_repo_url is not None:
            result['InstanceSnapshotRepoUrl'] = self.instance_snapshot_repo_url
        if self.instance_snapshot_status is not None:
            result['InstanceSnapshotStatus'] = self.instance_snapshot_status
        if self.instance_snapshot_tag is not None:
            result['InstanceSnapshotTag'] = self.instance_snapshot_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSnapshotDescription') is not None:
            self.instance_snapshot_description = m.get('InstanceSnapshotDescription')
        if m.get('InstanceSnapshotId') is not None:
            self.instance_snapshot_id = m.get('InstanceSnapshotId')
        if m.get('InstanceSnapshotName') is not None:
            self.instance_snapshot_name = m.get('InstanceSnapshotName')
        if m.get('InstanceSnapshotRepoUrl') is not None:
            self.instance_snapshot_repo_url = m.get('InstanceSnapshotRepoUrl')
        if m.get('InstanceSnapshotStatus') is not None:
            self.instance_snapshot_status = m.get('InstanceSnapshotStatus')
        if m.get('InstanceSnapshotTag') is not None:
            self.instance_snapshot_tag = m.get('InstanceSnapshotTag')
        return self


class InstanceStatus(TeaModel):
    def __init__(
        self,
        accumulative_running_time_in_minutes: int = None,
        instance_id: str = None,
        instance_shutdown_timer: InstanceShutdownTimer = None,
        instance_status: str = None,
        msg: str = None,
        shutdown_enabled: bool = None,
        type: str = None,
    ):
        # 累计运行时间（分钟）
        self.accumulative_running_time_in_minutes = accumulative_running_time_in_minutes
        # 实例ID
        self.instance_id = instance_id
        self.instance_shutdown_timer = instance_shutdown_timer
        # 实例状态
        self.instance_status = instance_status
        # 实例消息
        self.msg = msg
        # 是否允许使用定时关机
        self.shutdown_enabled = shutdown_enabled
        # 实例类型
        self.type = type

    def validate(self):
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accumulative_running_time_in_minutes is not None:
            result['AccumulativeRunningTimeInMinutes'] = self.accumulative_running_time_in_minutes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.shutdown_enabled is not None:
            result['ShutdownEnabled'] = self.shutdown_enabled
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccumulativeRunningTimeInMinutes') is not None:
            self.accumulative_running_time_in_minutes = m.get('AccumulativeRunningTimeInMinutes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = InstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('ShutdownEnabled') is not None:
            self.shutdown_enabled = m.get('ShutdownEnabled')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class InstanceType(TeaModel):
    def __init__(
        self,
        cpu_core_count: int = None,
        discount: float = None,
        domestic_price: float = None,
        gpuamount: int = None,
        gpuspec: str = None,
        instance_bandwidth_rx: int = None,
        instance_bandwidth_tx: int = None,
        instance_pps_rx: int = None,
        instance_pps_tx: int = None,
        instance_type_family: str = None,
        instance_type_id: str = None,
        international: bool = None,
        local_storage_capacity: int = None,
        memory_size: float = None,
        price: float = None,
        price_cny: float = None,
        price_usd: float = None,
        resource_type: str = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
    ):
        # CPU核数
        self.cpu_core_count = cpu_core_count
        # 折扣
        self.discount = discount
        # 内部价
        self.domestic_price = domestic_price
        # GPU卡数
        self.gpuamount = gpuamount
        # GPU规格
        self.gpuspec = gpuspec
        # 实例接收带宽
        self.instance_bandwidth_rx = instance_bandwidth_rx
        # 实例发送带宽
        self.instance_bandwidth_tx = instance_bandwidth_tx
        # 实例每秒发包数量
        self.instance_pps_rx = instance_pps_rx
        # 实例每秒收包数量
        self.instance_pps_tx = instance_pps_tx
        # 实例规格族
        self.instance_type_family = instance_type_family
        # 实例类型Id
        self.instance_type_id = instance_type_id
        # 是否国际站
        self.international = international
        # 本地磁盘容量
        self.local_storage_capacity = local_storage_capacity
        # 内存容量
        self.memory_size = memory_size
        # 价格
        self.price = price
        # 价格（人民币）
        self.price_cny = price_cny
        # 价格（美元）
        self.price_usd = price_usd
        # 资源类型
        self.resource_type = resource_type
        # 磁盘存储类型
        self.system_disk_category = system_disk_category
        # 磁盘容量
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count
        if self.discount is not None:
            result['Discount'] = self.discount
        if self.domestic_price is not None:
            result['DomesticPrice'] = self.domestic_price
        if self.gpuamount is not None:
            result['GPUAmount'] = self.gpuamount
        if self.gpuspec is not None:
            result['GPUSpec'] = self.gpuspec
        if self.instance_bandwidth_rx is not None:
            result['InstanceBandwidthRx'] = self.instance_bandwidth_rx
        if self.instance_bandwidth_tx is not None:
            result['InstanceBandwidthTx'] = self.instance_bandwidth_tx
        if self.instance_pps_rx is not None:
            result['InstancePpsRx'] = self.instance_pps_rx
        if self.instance_pps_tx is not None:
            result['InstancePpsTx'] = self.instance_pps_tx
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        if self.international is not None:
            result['International'] = self.international
        if self.local_storage_capacity is not None:
            result['LocalStorageCapacity'] = self.local_storage_capacity
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.price is not None:
            result['Price'] = self.price
        if self.price_cny is not None:
            result['PriceCNY'] = self.price_cny
        if self.price_usd is not None:
            result['PriceUSD'] = self.price_usd
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')
        if m.get('Discount') is not None:
            self.discount = m.get('Discount')
        if m.get('DomesticPrice') is not None:
            self.domestic_price = m.get('DomesticPrice')
        if m.get('GPUAmount') is not None:
            self.gpuamount = m.get('GPUAmount')
        if m.get('GPUSpec') is not None:
            self.gpuspec = m.get('GPUSpec')
        if m.get('InstanceBandwidthRx') is not None:
            self.instance_bandwidth_rx = m.get('InstanceBandwidthRx')
        if m.get('InstanceBandwidthTx') is not None:
            self.instance_bandwidth_tx = m.get('InstanceBandwidthTx')
        if m.get('InstancePpsRx') is not None:
            self.instance_pps_rx = m.get('InstancePpsRx')
        if m.get('InstancePpsTx') is not None:
            self.instance_pps_tx = m.get('InstancePpsTx')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        if m.get('International') is not None:
            self.international = m.get('International')
        if m.get('LocalStorageCapacity') is not None:
            self.local_storage_capacity = m.get('LocalStorageCapacity')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('PriceCNY') is not None:
            self.price_cny = m.get('PriceCNY')
        if m.get('PriceUSD') is not None:
            self.price_usd = m.get('PriceUSD')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class Nas(TeaModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        status: str = None,
    ):
        # Nas盘描述
        self.description = description
        # Nas文件系统Id
        self.file_system_id = file_system_id
        # Nas盘状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class Region(TeaModel):
    def __init__(
        self,
        region_city: str = None,
        region_id: str = None,
        region_name: str = None,
        region_state: str = None,
        service_url: str = None,
    ):
        # 城市
        self.region_city = region_city
        # id
        self.region_id = region_id
        # 名称
        self.region_name = region_name
        # 州省
        self.region_state = region_state
        # 服务地址
        self.service_url = service_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_city is not None:
            result['RegionCity'] = self.region_city
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.region_state is not None:
            result['RegionState'] = self.region_state
        if self.service_url is not None:
            result['ServiceUrl'] = self.service_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionCity') is not None:
            self.region_city = m.get('RegionCity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('RegionState') is not None:
            self.region_state = m.get('RegionState')
        if m.get('ServiceUrl') is not None:
            self.service_url = m.get('ServiceUrl')
        return self


class ResourceInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        pay_type: int = None,
        resource_type: int = None,
    ):
        # 显卡类型
        self.name = name
        # 支付类型
        self.pay_type = pay_type
        # 资源类型
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class SecurityGroup(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
        vpc_id: str = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 描述
        self.description = description
        # 安全组id
        self.security_group_id = security_group_id
        # 名称
        self.security_group_name = security_group_name
        # vpc id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class Status(TeaModel):
    def __init__(
        self,
        accumulative_running_time_in_minutes: int = None,
        instance_id: str = None,
        instance_shutdown_timer: InstanceShutdownTimer = None,
        instance_status: str = None,
        msg: str = None,
        type: str = None,
    ):
        # 累计运行时间（分钟）
        self.accumulative_running_time_in_minutes = accumulative_running_time_in_minutes
        # 实例ID
        self.instance_id = instance_id
        self.instance_shutdown_timer = instance_shutdown_timer
        # 实例状态
        self.instance_status = instance_status
        # 实例消息
        self.msg = msg
        # 实例类型
        self.type = type

    def validate(self):
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accumulative_running_time_in_minutes is not None:
            result['AccumulativeRunningTimeInMinutes'] = self.accumulative_running_time_in_minutes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccumulativeRunningTimeInMinutes') is not None:
            self.accumulative_running_time_in_minutes = m.get('AccumulativeRunningTimeInMinutes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = InstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class VSwitch(TeaModel):
    def __init__(
        self,
        available_ip_address_count: int = None,
        cidr_block: str = None,
        create_time: str = None,
        description: str = None,
        is_default: bool = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # 可用ip数量
        self.available_ip_address_count = available_ip_address_count
        # 子网
        self.cidr_block = cidr_block
        # 创建时间
        self.create_time = create_time
        # 描述
        self.description = description
        # 是否默认
        self.is_default = is_default
        # 状态
        self.status = status
        # VSwitch Id
        self.v_switch_id = v_switch_id
        # 名称
        self.v_switch_name = v_switch_name
        # vpc id
        self.vpc_id = vpc_id
        # 可用区
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class Vpc(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        create_time: str = None,
        description: str = None,
        is_default: bool = None,
        status: str = None,
        vrouter_id: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # vpc子网
        self.cidr_block = cidr_block
        # 创建时间
        self.create_time = create_time
        # vpc描述
        self.description = description
        # 是否默认
        self.is_default = is_default
        # vpc状态
        self.status = status
        # 路由id
        self.vrouter_id = vrouter_id
        # vpc id
        self.vpc_id = vpc_id
        # vpc名称
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        dataset_list: List[Dataset] = None,
        ecs_spec: str = None,
        environments: Dict[str, Any] = None,
        image_id: str = None,
        image_url: str = None,
        instance_name: str = None,
        is_public: int = None,
        nas_file_system_id: str = None,
        user_name: str = None,
        user_vpc: UserVpc = None,
        workspace_id: str = None,
    ):
        self.dataset_list = dataset_list
        # 实例规格
        self.ecs_spec = ecs_spec
        # 环境参数
        self.environments = environments
        # 镜像id
        self.image_id = image_id
        # 镜像地址
        self.image_url = image_url
        # 实例名称
        self.instance_name = instance_name
        self.is_public = is_public
        # nas文件系统id
        self.nas_file_system_id = nas_file_system_id
        # 实例的真实用户名称
        self.user_name = user_name
        # 打通的vpc网络配置
        self.user_vpc = user_vpc
        self.workspace_id = workspace_id

    def validate(self):
        if self.dataset_list:
            for k in self.dataset_list:
                if k:
                    k.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatasetList'] = []
        if self.dataset_list is not None:
            for k in self.dataset_list:
                result['DatasetList'].append(k.to_map() if k else None)
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environments is not None:
            result['Environments'] = self.environments
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.is_public is not None:
            result['IsPublic'] = self.is_public
        if self.nas_file_system_id is not None:
            result['NasFileSystemId'] = self.nas_file_system_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_list = []
        if m.get('DatasetList') is not None:
            for k in m.get('DatasetList'):
                temp_model = Dataset()
                self.dataset_list.append(temp_model.from_map(k))
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('Environments') is not None:
            self.environments = m.get('Environments')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')
        if m.get('NasFileSystemId') is not None:
            self.nas_file_system_id = m.get('NasFileSystemId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserVpc') is not None:
            temp_model = UserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceShutdownTimerRequest(TeaModel):
    def __init__(
        self,
        schedule_time: str = None,
        ttl_in_millis: int = None,
    ):
        # 定时关机时间（GMT）
        self.schedule_time = schedule_time
        # 多少毫秒后定时关机（如果设定可以覆盖ScheduleTime）
        self.ttl_in_millis = ttl_in_millis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.ttl_in_millis is not None:
            result['TtlInMillis'] = self.ttl_in_millis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('TtlInMillis') is not None:
            self.ttl_in_millis = m.get('TtlInMillis')
        return self


class CreateInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceShutdownTimerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceShutdownTimerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceShutdownTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceShutdownTimerV2Request(TeaModel):
    def __init__(
        self,
        due_time: str = None,
        remaining_time_in_ms: int = None,
    ):
        # 定时关机设定时间
        self.due_time = due_time
        # 距离定时关机时间段
        self.remaining_time_in_ms = remaining_time_in_ms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.remaining_time_in_ms is not None:
            result['RemainingTimeInMs'] = self.remaining_time_in_ms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('RemainingTimeInMs') is not None:
            self.remaining_time_in_ms = m.get('RemainingTimeInMs')
        return self


class CreateInstanceShutdownTimerV2ResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 实例Id
        self.instance_id = instance_id
        # 请求Id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceShutdownTimerV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceShutdownTimerV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceShutdownTimerV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceSnapshotRequest(TeaModel):
    def __init__(
        self,
        instance_snapshot_description: str = None,
        instance_snapshot_name: str = None,
        instance_snapshot_repo_url: str = None,
    ):
        # 实例快照描述
        self.instance_snapshot_description = instance_snapshot_description
        # 实例快照名称
        self.instance_snapshot_name = instance_snapshot_name
        # 实例快照存储地址（可选）
        self.instance_snapshot_repo_url = instance_snapshot_repo_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_snapshot_description is not None:
            result['InstanceSnapshotDescription'] = self.instance_snapshot_description
        if self.instance_snapshot_name is not None:
            result['InstanceSnapshotName'] = self.instance_snapshot_name
        if self.instance_snapshot_repo_url is not None:
            result['InstanceSnapshotRepoUrl'] = self.instance_snapshot_repo_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceSnapshotDescription') is not None:
            self.instance_snapshot_description = m.get('InstanceSnapshotDescription')
        if m.get('InstanceSnapshotName') is not None:
            self.instance_snapshot_name = m.get('InstanceSnapshotName')
        if m.get('InstanceSnapshotRepoUrl') is not None:
            self.instance_snapshot_repo_url = m.get('InstanceSnapshotRepoUrl')
        return self


class CreateInstanceSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_snapshot_id: str = None,
        request_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 实例快照ID
        self.instance_snapshot_id = instance_snapshot_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_snapshot_id is not None:
            result['InstanceSnapshotId'] = self.instance_snapshot_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSnapshotId') is not None:
            self.instance_snapshot_id = m.get('InstanceSnapshotId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceSnapshotV2Request(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        snapshot_description: str = None,
        snapshot_name: str = None,
    ):
        # 镜像地址
        self.image_url = image_url
        # 实例快照描述
        self.snapshot_description = snapshot_description
        # 实例快照名称
        self.snapshot_name = snapshot_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.snapshot_description is not None:
            result['SnapshotDescription'] = self.snapshot_description
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('SnapshotDescription') is not None:
            self.snapshot_description = m.get('SnapshotDescription')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        return self


class CreateInstanceSnapshotV2ResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
        snapshot_id: str = None,
    ):
        # 实例Id
        self.instance_id = instance_id
        # 请求Id
        self.request_id = request_id
        # 实例快照Id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class CreateInstanceSnapshotV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceSnapshotV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceSnapshotV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceV2RequestDatasets(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
        mount_path: str = None,
    ):
        # 数据集Id
        self.dataset_id = dataset_id
        # 容器内挂载路径
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class CreateInstanceV2RequestUserVpc(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # Security Group Id
        self.security_group_id = security_group_id
        # VSwitch Id
        self.v_switch_id = v_switch_id
        # Vpc Id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateInstanceV2Request(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        datasets: List[CreateInstanceV2RequestDatasets] = None,
        ecs_spec: str = None,
        environment_variables: Dict[str, str] = None,
        image_id: str = None,
        image_url: str = None,
        instance_name: str = None,
        user_vpc: CreateInstanceV2RequestUserVpc = None,
        workspace_id: str = None,
    ):
        # 工作空间内是否他人可见
        self.accessibility = accessibility
        # 数据集集合
        self.datasets = datasets
        # 实例对应的Ecs规格
        self.ecs_spec = ecs_spec
        # 环境变量
        self.environment_variables = environment_variables
        # 镜像Id
        self.image_id = image_id
        # 镜像地址
        self.image_url = image_url
        # 实例名称
        self.instance_name = instance_name
        # user vpc配置
        self.user_vpc = user_vpc
        # 工作空间Id
        self.workspace_id = workspace_id

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = CreateInstanceV2RequestDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('UserVpc') is not None:
            temp_model = CreateInstanceV2RequestUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateInstanceV2ResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 工作空间Id
        self.instance_id = instance_id
        # 请求Id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceShutdownTimerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceShutdownTimerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceShutdownTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceShutdownTimerV2ResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 实例Id
        self.instance_id = instance_id
        # 请求Id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceShutdownTimerV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceShutdownTimerV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceShutdownTimerV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_snapshot_id: str = None,
        request_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 实例快照ID
        self.instance_snapshot_id = instance_snapshot_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_snapshot_id is not None:
            result['InstanceSnapshotId'] = self.instance_snapshot_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSnapshotId') is not None:
            self.instance_snapshot_id = m.get('InstanceSnapshotId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceSnapshotV2ResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
        snapshot_id: str = None,
    ):
        # 实例Id
        self.instance_id = instance_id
        # 请求Id
        self.request_id = request_id
        # 实例快照Id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DeleteInstanceSnapshotV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceSnapshotV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceSnapshotV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceV2ResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 工作空间Id
        self.instance_id = instance_id
        # 请求Id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FoobarResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class FoobarResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FoobarResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FoobarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Foobar1Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: Any = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        authorization_failed_code: str = None,
        authorization_failed_message: str = None,
        authorized: bool = None,
        request_id: str = None,
    ):
        # 授权失败错误代码
        self.authorization_failed_code = authorization_failed_code
        # 授权失败错误消息
        self.authorization_failed_message = authorization_failed_message
        # 是否已经给DSW服务账号授权
        self.authorized = authorized
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_failed_code is not None:
            result['AuthorizationFailedCode'] = self.authorization_failed_code
        if self.authorization_failed_message is not None:
            result['AuthorizationFailedMessage'] = self.authorization_failed_message
        if self.authorized is not None:
            result['Authorized'] = self.authorized
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationFailedCode') is not None:
            self.authorization_failed_code = m.get('AuthorizationFailedCode')
        if m.get('AuthorizationFailedMessage') is not None:
            self.authorization_failed_message = m.get('AuthorizationFailedMessage')
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAuthorizationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDashboardStatisticsRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # 工作空间ID
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDashboardStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        instance_total: int = None,
        instsance_running_total: int = None,
        request_id: str = None,
    ):
        # 实例数
        self.instance_total = instance_total
        # 运行实例数
        self.instsance_running_total = instsance_running_total
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_total is not None:
            result['InstanceTotal'] = self.instance_total
        if self.instsance_running_total is not None:
            result['InstsanceRunningTotal'] = self.instsance_running_total
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTotal') is not None:
            self.instance_total = m.get('InstanceTotal')
        if m.get('InstsanceRunningTotal') is not None:
            self.instsance_running_total = m.get('InstsanceRunningTotal')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDashboardStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDashboardStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDashboardStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        accumulative_running_time_in_minutes: int = None,
        ecs_spec: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_url: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_shutdown_timer: InstanceShutdownTimer = None,
        instance_status: str = None,
        jupyterlab_url: str = None,
        nas_file_system_id: str = None,
        request_id: str = None,
        terminal_url: str = None,
        user_id: str = None,
        user_vpc: UserVpc = None,
        web_ide_url: str = None,
    ):
        # 累计运行时间(分钟)
        self.accumulative_running_time_in_minutes = accumulative_running_time_in_minutes
        # ecs规格
        self.ecs_spec = ecs_spec
        # 实例创建时间(GMT)
        self.gmt_create_time = gmt_create_time
        # 实例修改时间(GMT)
        self.gmt_modified_time = gmt_modified_time
        # 镜像ID
        self.image_id = image_id
        # 镜像链接
        self.image_url = image_url
        # 实例ID
        self.instance_id = instance_id
        # 实例名称
        self.instance_name = instance_name
        # 定时关机任务
        self.instance_shutdown_timer = instance_shutdown_timer
        # 实例状态
        self.instance_status = instance_status
        # jupyter链接
        self.jupyterlab_url = jupyterlab_url
        # nas文件系统ID
        self.nas_file_system_id = nas_file_system_id
        # 请求ID
        self.request_id = request_id
        # 命令行终端链接
        self.terminal_url = terminal_url
        # 用户ID
        self.user_id = user_id
        # 被打通VPC配置
        self.user_vpc = user_vpc
        # web ide链接
        self.web_ide_url = web_ide_url

    def validate(self):
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accumulative_running_time_in_minutes is not None:
            result['AccumulativeRunningTimeInMinutes'] = self.accumulative_running_time_in_minutes
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        if self.nas_file_system_id is not None:
            result['NasFileSystemId'] = self.nas_file_system_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ide_url is not None:
            result['WebIdeUrl'] = self.web_ide_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccumulativeRunningTimeInMinutes') is not None:
            self.accumulative_running_time_in_minutes = m.get('AccumulativeRunningTimeInMinutes')
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = InstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        if m.get('NasFileSystemId') is not None:
            self.nas_file_system_id = m.get('NasFileSystemId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = UserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIdeUrl') is not None:
            self.web_ide_url = m.get('WebIdeUrl')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        request_id: str = None,
        schedule_time: str = None,
    ):
        # 任务创建时间(GMT)
        self.gmt_create_time = gmt_create_time
        # 任务修改时间(GMT)
        self.gmt_modified_time = gmt_modified_time
        # 实例ID
        self.instance_id = instance_id
        # 请求ID
        self.request_id = request_id
        # 定时关机时间(GMT)
        self.schedule_time = schedule_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        return self


class GetInstanceShutdownTimerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceShutdownTimerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceShutdownTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceShutdownTimerV2ResponseBody(TeaModel):
    def __init__(
        self,
        due_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        remaining_time_in_ms: int = None,
        request_id: str = None,
    ):
        # 设定关机时间
        self.due_time = due_time
        # 创建时间
        self.gmt_create_time = gmt_create_time
        # 修改时间
        self.gmt_modified_time = gmt_modified_time
        # 实例Id
        self.instance_id = instance_id
        # 剩余关机时间（ms）
        self.remaining_time_in_ms = remaining_time_in_ms
        # 请求Id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remaining_time_in_ms is not None:
            result['RemainingTimeInMs'] = self.remaining_time_in_ms
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RemainingTimeInMs') is not None:
            self.remaining_time_in_ms = m.get('RemainingTimeInMs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceShutdownTimerV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceShutdownTimerV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceShutdownTimerV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        instance_snapshot_description: str = None,
        instance_snapshot_id: str = None,
        instance_snapshot_name: str = None,
        instance_snapshot_repo_url: str = None,
        instance_snapshot_status: str = None,
        instance_snapshot_tag: str = None,
        request_id: str = None,
    ):
        # 实例快照保存时间（GMT）
        self.gmt_create_time = gmt_create_time
        # 实例快照修改时间（GMT）
        self.gmt_modified_time = gmt_modified_time
        # 实例ID
        self.instance_id = instance_id
        # 实例快照描述
        self.instance_snapshot_description = instance_snapshot_description
        # 实例快照ID
        self.instance_snapshot_id = instance_snapshot_id
        # 实例快照名称
        self.instance_snapshot_name = instance_snapshot_name
        # 实例快照存储地址
        self.instance_snapshot_repo_url = instance_snapshot_repo_url
        # 实例快照状态
        self.instance_snapshot_status = instance_snapshot_status
        # 实例快照标签
        self.instance_snapshot_tag = instance_snapshot_tag
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_snapshot_description is not None:
            result['InstanceSnapshotDescription'] = self.instance_snapshot_description
        if self.instance_snapshot_id is not None:
            result['InstanceSnapshotId'] = self.instance_snapshot_id
        if self.instance_snapshot_name is not None:
            result['InstanceSnapshotName'] = self.instance_snapshot_name
        if self.instance_snapshot_repo_url is not None:
            result['InstanceSnapshotRepoUrl'] = self.instance_snapshot_repo_url
        if self.instance_snapshot_status is not None:
            result['InstanceSnapshotStatus'] = self.instance_snapshot_status
        if self.instance_snapshot_tag is not None:
            result['InstanceSnapshotTag'] = self.instance_snapshot_tag
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSnapshotDescription') is not None:
            self.instance_snapshot_description = m.get('InstanceSnapshotDescription')
        if m.get('InstanceSnapshotId') is not None:
            self.instance_snapshot_id = m.get('InstanceSnapshotId')
        if m.get('InstanceSnapshotName') is not None:
            self.instance_snapshot_name = m.get('InstanceSnapshotName')
        if m.get('InstanceSnapshotRepoUrl') is not None:
            self.instance_snapshot_repo_url = m.get('InstanceSnapshotRepoUrl')
        if m.get('InstanceSnapshotStatus') is not None:
            self.instance_snapshot_status = m.get('InstanceSnapshotStatus')
        if m.get('InstanceSnapshotTag') is not None:
            self.instance_snapshot_tag = m.get('InstanceSnapshotTag')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceSnapshotV2ResponseBody(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_url: str = None,
        instance_id: str = None,
        reason_code: str = None,
        reason_message: str = None,
        request_id: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        status: str = None,
    ):
        # 实例快照创建时间
        self.gmt_create_time = gmt_create_time
        # 实例快照修改时间
        self.gmt_modified_time = gmt_modified_time
        # 实例快照的镜像Id
        self.image_id = image_id
        # 实例快照的镜像地址
        self.image_url = image_url
        # 实例Id
        self.instance_id = instance_id
        # 实例快照错误代码
        self.reason_code = reason_code
        # 实例快照错误消息
        self.reason_message = reason_message
        # 请求Id
        self.request_id = request_id
        # 实例快照Id
        self.snapshot_id = snapshot_id
        # 实例快照名称
        self.snapshot_name = snapshot_name
        # 实例快照状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetInstanceSnapshotV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceSnapshotV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceSnapshotV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceV2ResponseBodyDatasets(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
        mount_path: str = None,
    ):
        # 数据集Id
        self.dataset_id = dataset_id
        # 容器内挂载路径
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class GetInstanceV2ResponseBodyInstanceShutdownTimer(TeaModel):
    def __init__(
        self,
        due_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        remaining_time_in_ms: int = None,
    ):
        # 设定关机时间
        self.due_time = due_time
        # 创建时间
        self.gmt_create_time = gmt_create_time
        # 修改时间
        self.gmt_modified_time = gmt_modified_time
        # 实例Id
        self.instance_id = instance_id
        # 剩余关机时间（ms）
        self.remaining_time_in_ms = remaining_time_in_ms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remaining_time_in_ms is not None:
            result['RemainingTimeInMs'] = self.remaining_time_in_ms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RemainingTimeInMs') is not None:
            self.remaining_time_in_ms = m.get('RemainingTimeInMs')
        return self


class GetInstanceV2ResponseBodyLatestSnapshot(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        repository_url: str = None,
    ):
        # 快照创建时间
        self.gmt_create_time = gmt_create_time
        # 快照修改时间
        self.gmt_modified_time = gmt_modified_time
        # 镜像Id
        self.image_id = image_id
        # 镜像名称
        self.image_name = image_name
        # 镜像Url
        self.image_url = image_url
        # 镜像仓库Url
        self.repository_url = repository_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        return self


class GetInstanceV2ResponseBodyUserVpc(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # Security Group Id
        self.security_group_id = security_group_id
        # VSwitch Id
        self.v_switch_id = v_switch_id
        # Vpc Id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetInstanceV2ResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        accessibility: str = None,
        accumulated_running_time_in_ms: int = None,
        datasets: List[GetInstanceV2ResponseBodyDatasets] = None,
        ecs_spec: str = None,
        environment_variables: Dict[str, str] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_shutdown_timer: GetInstanceV2ResponseBodyInstanceShutdownTimer = None,
        instance_url: str = None,
        jupyterlab_url: str = None,
        latest_snapshot: GetInstanceV2ResponseBodyLatestSnapshot = None,
        payment_type: str = None,
        reason_code: str = None,
        reason_message: str = None,
        request_id: str = None,
        status: str = None,
        terminal_url: str = None,
        user_id: str = None,
        user_vpc: GetInstanceV2ResponseBodyUserVpc = None,
        web_ideurl: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # 实例计算类型
        self.accelerator_type = accelerator_type
        # 工作空间内是否他人可见
        self.accessibility = accessibility
        # 累计运行时间（ms）
        self.accumulated_running_time_in_ms = accumulated_running_time_in_ms
        # 数据集集合
        self.datasets = datasets
        # 实例对应的Ecs规格
        self.ecs_spec = ecs_spec
        # 环境变量
        self.environment_variables = environment_variables
        # 实例创建时间
        self.gmt_create_time = gmt_create_time
        # 实例修改时间
        self.gmt_modified_time = gmt_modified_time
        # 镜像Id
        self.image_id = image_id
        # 镜像名称
        self.image_name = image_name
        # 镜像地址
        self.image_url = image_url
        # 实例Id
        self.instance_id = instance_id
        # 实例名称
        self.instance_name = instance_name
        # 定时关机任务
        self.instance_shutdown_timer = instance_shutdown_timer
        # 实例Url
        self.instance_url = instance_url
        # Jupyterlab Url
        self.jupyterlab_url = jupyterlab_url
        # 最新保存的用户镜像
        self.latest_snapshot = latest_snapshot
        # 支付类型
        self.payment_type = payment_type
        # 实例错误代码
        self.reason_code = reason_code
        # 实例错误原因
        self.reason_message = reason_message
        # 请求Id
        self.request_id = request_id
        # 实例状态
        self.status = status
        # terminal url
        self.terminal_url = terminal_url
        # 用户Id
        self.user_id = user_id
        # user vpc配置
        self.user_vpc = user_vpc
        # web ide url
        self.web_ideurl = web_ideurl
        # 工作空间Id
        self.workspace_id = workspace_id
        # 工作空间名称
        self.workspace_name = workspace_name

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.latest_snapshot:
            self.latest_snapshot.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.accumulated_running_time_in_ms is not None:
            result['AccumulatedRunningTimeInMs'] = self.accumulated_running_time_in_ms
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        if self.latest_snapshot is not None:
            result['LatestSnapshot'] = self.latest_snapshot.to_map()
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ideurl is not None:
            result['WebIDEUrl'] = self.web_ideurl
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('AccumulatedRunningTimeInMs') is not None:
            self.accumulated_running_time_in_ms = m.get('AccumulatedRunningTimeInMs')
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = GetInstanceV2ResponseBodyDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = GetInstanceV2ResponseBodyInstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        if m.get('LatestSnapshot') is not None:
            temp_model = GetInstanceV2ResponseBodyLatestSnapshot()
            self.latest_snapshot = temp_model.from_map(m['LatestSnapshot'])
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = GetInstanceV2ResponseBodyUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIDEUrl') is not None:
            self.web_ideurl = m.get('WebIDEUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class GetInstanceV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstancesStatisticsRequest(TeaModel):
    def __init__(
        self,
        workspace_ids: str = None,
    ):
        # 工作空间id列表
        self.workspace_ids = workspace_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')
        return self


class GetInstancesStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistics: Dict[str, Any] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 统计数据
        self.statistics = statistics

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        return self


class GetInstancesStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstancesStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstancesStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserConfigV2ResponseBody(TeaModel):
    def __init__(
        self,
        account_sufficient: bool = None,
        request_id: str = None,
    ):
        # 用户账号金额是否充足
        self.account_sufficient = account_sufficient
        # 请求Id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_sufficient is not None:
            result['AccountSufficient'] = self.account_sufficient
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountSufficient') is not None:
            self.account_sufficient = m.get('AccountSufficient')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserConfigV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserConfigV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserConfigV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEcsSpecsRequest(TeaModel):
    def __init__(
        self,
        accelerator_type_equals: str = None,
    ):
        # 每页返回的实例数
        self.accelerator_type_equals = accelerator_type_equals

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type_equals is not None:
            result['AcceleratorTypeEquals'] = self.accelerator_type_equals
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorTypeEquals') is not None:
            self.accelerator_type_equals = m.get('AcceleratorTypeEquals')
        return self


class ListEcsSpecsResponseBody(TeaModel):
    def __init__(
        self,
        ecs_specs: List[EcsSpec] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 请求ecs规格列表
        self.ecs_specs = ecs_specs
        # 请求ID
        self.request_id = request_id
        # 符合要求的ecs规格数量
        self.total_count = total_count

    def validate(self):
        if self.ecs_specs:
            for k in self.ecs_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsSpecs'] = []
        if self.ecs_specs is not None:
            for k in self.ecs_specs:
                result['EcsSpecs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_specs = []
        if m.get('EcsSpecs') is not None:
            for k in m.get('EcsSpecs'):
                temp_model = EcsSpec()
                self.ecs_specs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEcsSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEcsSpecsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEcsSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEcsSpecsV2Request(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
    ):
        # 加速类型
        self.accelerator_type = accelerator_type
        # 排序顺序
        self.order = order
        # 页数
        self.page_number = page_number
        # 每页大小
        self.page_size = page_size
        # 排序字段
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListEcsSpecsV2ResponseBodyEcsSpecs(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        cpu: int = None,
        currency: str = None,
        gpu: int = None,
        gputype: str = None,
        instance_bandwidth_rx: int = None,
        instance_type: str = None,
        memory: float = None,
        price: float = None,
        system_disk_capacity: int = None,
    ):
        # 资源类型
        self.accelerator_type = accelerator_type
        # CPU核数
        self.cpu = cpu
        # 货币单位
        self.currency = currency
        # GPU卡数
        self.gpu = gpu
        # 显卡类型
        self.gputype = gputype
        # 实例接收带宽
        self.instance_bandwidth_rx = instance_bandwidth_rx
        # 实例规格
        self.instance_type = instance_type
        # 内存大小(GB)
        self.memory = memory
        # 价格
        self.price = price
        # 系统盘大小(GB)
        self.system_disk_capacity = system_disk_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.instance_bandwidth_rx is not None:
            result['InstanceBandwidthRx'] = self.instance_bandwidth_rx
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.price is not None:
            result['Price'] = self.price
        if self.system_disk_capacity is not None:
            result['SystemDiskCapacity'] = self.system_disk_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('InstanceBandwidthRx') is not None:
            self.instance_bandwidth_rx = m.get('InstanceBandwidthRx')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('SystemDiskCapacity') is not None:
            self.system_disk_capacity = m.get('SystemDiskCapacity')
        return self


class ListEcsSpecsV2ResponseBody(TeaModel):
    def __init__(
        self,
        ecs_specs: List[ListEcsSpecsV2ResponseBodyEcsSpecs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 本分页中请求的实例列表
        self.ecs_specs = ecs_specs
        # 请求Id
        self.request_id = request_id
        # 实例总数
        self.total_count = total_count

    def validate(self):
        if self.ecs_specs:
            for k in self.ecs_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsSpecs'] = []
        if self.ecs_specs is not None:
            for k in self.ecs_specs:
                result['EcsSpecs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_specs = []
        if m.get('EcsSpecs') is not None:
            for k in m.get('EcsSpecs'):
                temp_model = ListEcsSpecsV2ResponseBodyEcsSpecs()
                self.ecs_specs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEcsSpecsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEcsSpecsV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEcsSpecsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        accelerator_type_equals: str = None,
        image_name_contains: str = None,
        image_type_equals: str = None,
        product: str = None,
        workspace_id: str = None,
    ):
        # 资源类型
        self.accelerator_type_equals = accelerator_type_equals
        # 容器名称关键字
        self.image_name_contains = image_name_contains
        # 镜像类型
        self.image_type_equals = image_type_equals
        # 产品
        self.product = product
        # 工作空间Id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type_equals is not None:
            result['AcceleratorTypeEquals'] = self.accelerator_type_equals
        if self.image_name_contains is not None:
            result['ImageNameContains'] = self.image_name_contains
        if self.image_type_equals is not None:
            result['ImageTypeEquals'] = self.image_type_equals
        if self.product is not None:
            result['Product'] = self.product
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorTypeEquals') is not None:
            self.accelerator_type_equals = m.get('AcceleratorTypeEquals')
        if m.get('ImageNameContains') is not None:
            self.image_name_contains = m.get('ImageNameContains')
        if m.get('ImageTypeEquals') is not None:
            self.image_type_equals = m.get('ImageTypeEquals')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(
        self,
        images: List[Image] = None,
        request_id: str = None,
    ):
        # 镜像列表
        self.images = images
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = Image()
                self.images.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListImagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceSnapshotV2Request(TeaModel):
    def __init__(
        self,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
    ):
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListInstanceSnapshotV2ResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_url: str = None,
        instance_id: str = None,
        reason_code: str = None,
        reason_message: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        status: str = None,
    ):
        # 实例快照创建时间
        self.gmt_create_time = gmt_create_time
        # 实例快照修改时间
        self.gmt_modified_time = gmt_modified_time
        # 实例快照的镜像Id
        self.image_id = image_id
        # 实例快照的镜像地址
        self.image_url = image_url
        # 实例Id
        self.instance_id = instance_id
        # 实例快照错误代码
        self.reason_code = reason_code
        # 实例快照错误消息
        self.reason_message = reason_message
        # 实例快照Id
        self.snapshot_id = snapshot_id
        # 实例快照名称
        self.snapshot_name = snapshot_name
        # 实例快照状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstanceSnapshotV2ResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        snapshots: List[ListInstanceSnapshotV2ResponseBodySnapshots] = None,
        total_count: int = None,
    ):
        # 请求Id
        self.request_id = request_id
        # 本分页中请求的实例镜像列表
        self.snapshots = snapshots
        # 实例总数
        self.total_count = total_count

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = ListInstanceSnapshotV2ResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceSnapshotV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceSnapshotV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstanceSnapshotV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        instance_snapshots: List[InstanceSnapshot] = None,
        request_id: str = None,
    ):
        # 镜像快照列表
        self.instance_snapshots = instance_snapshots
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.instance_snapshots:
            for k in self.instance_snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceSnapshots'] = []
        if self.instance_snapshots is not None:
            for k in self.instance_snapshots:
                result['InstanceSnapshots'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_snapshots = []
        if m.get('InstanceSnapshots') is not None:
            for k in m.get('InstanceSnapshots'):
                temp_model = InstanceSnapshot()
                self.instance_snapshots.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstanceSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceSnapshotsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstanceSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceStatisticsV2Request(TeaModel):
    def __init__(
        self,
        workspace_ids: str = None,
    ):
        # 工作空间列表
        self.workspace_ids = workspace_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')
        return self


class ListInstanceStatisticsV2ResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistics: Dict[str, dict] = None,
    ):
        # 请求Id
        self.request_id = request_id
        # 统计信息
        self.statistics = statistics

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        return self


class ListInstanceStatisticsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceStatisticsV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstanceStatisticsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        in_workspace: bool = None,
        instance_name_contains: str = None,
        instance_status_equals: str = None,
        page_number: str = None,
        page_size: str = None,
        sort_by: str = None,
        sort_order: str = None,
        workspace_id_equals: str = None,
    ):
        # 是否在工作空间内查询
        self.in_workspace = in_workspace
        # 实例名称关键字
        self.instance_name_contains = instance_name_contains
        # 实例状态
        self.instance_status_equals = instance_status_equals
        # 当前页
        self.page_number = page_number
        # 每页返回的实例数
        self.page_size = page_size
        # 排序字段
        self.sort_by = sort_by
        # 升序降序
        self.sort_order = sort_order
        # 工作空间Id
        self.workspace_id_equals = workspace_id_equals

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_workspace is not None:
            result['InWorkspace'] = self.in_workspace
        if self.instance_name_contains is not None:
            result['InstanceNameContains'] = self.instance_name_contains
        if self.instance_status_equals is not None:
            result['InstanceStatusEquals'] = self.instance_status_equals
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.workspace_id_equals is not None:
            result['WorkspaceIdEquals'] = self.workspace_id_equals
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InWorkspace') is not None:
            self.in_workspace = m.get('InWorkspace')
        if m.get('InstanceNameContains') is not None:
            self.instance_name_contains = m.get('InstanceNameContains')
        if m.get('InstanceStatusEquals') is not None:
            self.instance_status_equals = m.get('InstanceStatusEquals')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('WorkspaceIdEquals') is not None:
            self.workspace_id_equals = m.get('WorkspaceIdEquals')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[Instance] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 实例列表
        self.instances = instances
        # 当前页
        self.page_number = page_number
        # 每页返回的实例数
        self.page_size = page_size
        # 请求ID
        self.request_id = request_id
        # 符合条件的实例数
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = Instance()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesStatusRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
    ):
        # 实例Id列表
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class ListInstancesStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statuses: List[InstanceStatus] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.statuses = statuses

    def validate(self):
        if self.statuses:
            for k in self.statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statuses'] = []
        if self.statuses is not None:
            for k in self.statuses:
                result['Statuses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statuses = []
        if m.get('Statuses') is not None:
            for k in m.get('Statuses'):
                temp_model = InstanceStatus()
                self.statuses.append(temp_model.from_map(k))
        return self


class ListInstancesStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstancesStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstancesStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesV2Request(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        # 实例名称
        self.instance_name = instance_name
        # 排列顺序
        self.order = order
        # 页码
        self.page_number = page_number
        # 分页数量大小
        self.page_size = page_size
        # 排序字段
        self.sort_by = sort_by
        # 实例状态
        self.status = status
        # 工作空间Id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListInstancesV2ResponseBodyInstancesDatasets(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
        mount_path: str = None,
    ):
        # 数据集Id
        self.dataset_id = dataset_id
        # 容器内挂载路径
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class ListInstancesV2ResponseBodyInstancesInstanceShutdownTimer(TeaModel):
    def __init__(
        self,
        due_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        remaining_time_in_ms: int = None,
    ):
        # 设定关机时间
        self.due_time = due_time
        # 创建时间
        self.gmt_create_time = gmt_create_time
        # 修改时间
        self.gmt_modified_time = gmt_modified_time
        # 实例Id
        self.instance_id = instance_id
        # 剩余关机时间（ms）
        self.remaining_time_in_ms = remaining_time_in_ms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remaining_time_in_ms is not None:
            result['RemainingTimeInMs'] = self.remaining_time_in_ms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RemainingTimeInMs') is not None:
            self.remaining_time_in_ms = m.get('RemainingTimeInMs')
        return self


class ListInstancesV2ResponseBodyInstancesLatestSnapshot(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        repository_url: str = None,
    ):
        # 快照创建时间
        self.gmt_create_time = gmt_create_time
        # 快照修改时间
        self.gmt_modified_time = gmt_modified_time
        # 镜像Id
        self.image_id = image_id
        # 镜像名称
        self.image_name = image_name
        # 镜像Url
        self.image_url = image_url
        # 镜像仓库Url
        self.repository_url = repository_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        return self


class ListInstancesV2ResponseBodyInstancesUserVpc(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # Security Group Id
        self.security_group_id = security_group_id
        # VSwitch Id
        self.v_switch_id = v_switch_id
        # Vpc Id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListInstancesV2ResponseBodyInstances(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        accessibility: str = None,
        accumulated_running_time_in_ms: int = None,
        datasets: List[ListInstancesV2ResponseBodyInstancesDatasets] = None,
        ecs_spec: str = None,
        environment_variables: Dict[str, str] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_shutdown_timer: ListInstancesV2ResponseBodyInstancesInstanceShutdownTimer = None,
        instance_url: str = None,
        jupyterlab_url: str = None,
        latest_snapshot: ListInstancesV2ResponseBodyInstancesLatestSnapshot = None,
        payment_type: str = None,
        reason_code: str = None,
        reason_message: str = None,
        status: str = None,
        terminal_url: str = None,
        user_id: str = None,
        user_vpc: ListInstancesV2ResponseBodyInstancesUserVpc = None,
        web_ideurl: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # 实例计算类型
        self.accelerator_type = accelerator_type
        # 工作空间内是否他人可见
        self.accessibility = accessibility
        # 累计运行时间（ms）
        self.accumulated_running_time_in_ms = accumulated_running_time_in_ms
        # 数据集集合
        self.datasets = datasets
        # 实例对应的Ecs规格
        self.ecs_spec = ecs_spec
        # 环境变量
        self.environment_variables = environment_variables
        # 实例创建时间
        self.gmt_create_time = gmt_create_time
        # 实例修改时间
        self.gmt_modified_time = gmt_modified_time
        # 镜像Id
        self.image_id = image_id
        # 镜像名称
        self.image_name = image_name
        # 镜像地址
        self.image_url = image_url
        # 实例Id
        self.instance_id = instance_id
        # 实例名称
        self.instance_name = instance_name
        # 定时关机任务
        self.instance_shutdown_timer = instance_shutdown_timer
        # 实例Url
        self.instance_url = instance_url
        # Jupyterlab Url
        self.jupyterlab_url = jupyterlab_url
        # 最新保存的用户镜像
        self.latest_snapshot = latest_snapshot
        # 支付类型
        self.payment_type = payment_type
        # 实例错误代码
        self.reason_code = reason_code
        # 实例错误原因
        self.reason_message = reason_message
        # 实例状态
        self.status = status
        # terminal url
        self.terminal_url = terminal_url
        # 用户Id
        self.user_id = user_id
        # user vpc配置
        self.user_vpc = user_vpc
        # web ide url
        self.web_ideurl = web_ideurl
        # 工作空间Id
        self.workspace_id = workspace_id
        # 工作空间名称
        self.workspace_name = workspace_name

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.latest_snapshot:
            self.latest_snapshot.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.accumulated_running_time_in_ms is not None:
            result['AccumulatedRunningTimeInMs'] = self.accumulated_running_time_in_ms
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        if self.latest_snapshot is not None:
            result['LatestSnapshot'] = self.latest_snapshot.to_map()
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.status is not None:
            result['Status'] = self.status
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ideurl is not None:
            result['WebIDEUrl'] = self.web_ideurl
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('AccumulatedRunningTimeInMs') is not None:
            self.accumulated_running_time_in_ms = m.get('AccumulatedRunningTimeInMs')
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = ListInstancesV2ResponseBodyInstancesDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = ListInstancesV2ResponseBodyInstancesInstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        if m.get('LatestSnapshot') is not None:
            temp_model = ListInstancesV2ResponseBodyInstancesLatestSnapshot()
            self.latest_snapshot = temp_model.from_map(m['LatestSnapshot'])
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = ListInstancesV2ResponseBodyInstancesUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIDEUrl') is not None:
            self.web_ideurl = m.get('WebIDEUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListInstancesV2ResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ListInstancesV2ResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 本分页中请求的实例列表
        self.instances = instances
        # 请求Id
        self.request_id = request_id
        # 实例总数
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesV2ResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstancesV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstancesV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceV2ResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 工作空间Id
        self.instance_id = instance_id
        # 请求Id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartInstanceV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartInstanceV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartInstanceV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(
        self,
        save_image: bool = None,
    ):
        # 是否保存镜像后停止
        self.save_image = save_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.save_image is not None:
            result['SaveImage'] = self.save_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SaveImage') is not None:
            self.save_image = m.get('SaveImage')
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceV2Request(TeaModel):
    def __init__(
        self,
        save_image: bool = None,
    ):
        self.save_image = save_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.save_image is not None:
            result['SaveImage'] = self.save_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SaveImage') is not None:
            self.save_image = m.get('SaveImage')
        return self


class StopInstanceV2ResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 工作空间Id
        self.instance_id = instance_id
        # 请求Id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInstanceV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopInstanceV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopInstanceV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
    ):
        # 修改后实例名称
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceSnapshotRequest(TeaModel):
    def __init__(
        self,
        instance_snapshot_name: str = None,
    ):
        # 实例快照名称
        self.instance_snapshot_name = instance_snapshot_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_snapshot_name is not None:
            result['InstanceSnapshotName'] = self.instance_snapshot_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceSnapshotName') is not None:
            self.instance_snapshot_name = m.get('InstanceSnapshotName')
        return self


class UpdateInstanceSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_snapshot_id: str = None,
        request_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 实例镜像ID
        self.instance_snapshot_id = instance_snapshot_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_snapshot_id is not None:
            result['InstanceSnapshotId'] = self.instance_snapshot_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSnapshotId') is not None:
            self.instance_snapshot_id = m.get('InstanceSnapshotId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateInstanceSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceV2RequestDatasets(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
        mount_path: str = None,
    ):
        # 数据集Id
        self.dataset_id = dataset_id
        # 容器内挂载路径
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class UpdateInstanceV2RequestInstanceShutdownTimer(TeaModel):
    def __init__(
        self,
        due_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        remaining_time_in_ms: int = None,
    ):
        # 设定关机时间
        self.due_time = due_time
        # 创建时间
        self.gmt_create_time = gmt_create_time
        # 修改时间
        self.gmt_modified_time = gmt_modified_time
        # 实例Id
        self.instance_id = instance_id
        # 剩余关机时间（ms）
        self.remaining_time_in_ms = remaining_time_in_ms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remaining_time_in_ms is not None:
            result['RemainingTimeInMs'] = self.remaining_time_in_ms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RemainingTimeInMs') is not None:
            self.remaining_time_in_ms = m.get('RemainingTimeInMs')
        return self


class UpdateInstanceV2RequestLatestSnapshot(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        repository_url: str = None,
    ):
        # 快照创建时间
        self.gmt_create_time = gmt_create_time
        # 快照修改时间
        self.gmt_modified_time = gmt_modified_time
        # 镜像Id
        self.image_id = image_id
        # 镜像名称
        self.image_name = image_name
        # 镜像Url
        self.image_url = image_url
        # 镜像仓库Url
        self.repository_url = repository_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        return self


class UpdateInstanceV2RequestUserVpc(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # Security Group Id
        self.security_group_id = security_group_id
        # VSwitch Id
        self.v_switch_id = v_switch_id
        # Vpc Id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateInstanceV2Request(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        accessibility: str = None,
        accumulated_running_time_in_ms: int = None,
        datasets: List[UpdateInstanceV2RequestDatasets] = None,
        ecs_spec: str = None,
        environment_variables: Dict[str, str] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_shutdown_timer: UpdateInstanceV2RequestInstanceShutdownTimer = None,
        instance_url: str = None,
        jupyterlab_url: str = None,
        latest_snapshot: UpdateInstanceV2RequestLatestSnapshot = None,
        payment_type: str = None,
        reason_code: str = None,
        reason_message: str = None,
        status: str = None,
        terminal_url: str = None,
        user_id: str = None,
        user_vpc: UpdateInstanceV2RequestUserVpc = None,
        web_ideurl: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # 实例计算类型
        self.accelerator_type = accelerator_type
        # 工作空间内是否他人可见
        self.accessibility = accessibility
        # 累计运行时间（ms）
        self.accumulated_running_time_in_ms = accumulated_running_time_in_ms
        # 数据集集合
        self.datasets = datasets
        # 实例对应的Ecs规格
        self.ecs_spec = ecs_spec
        # 环境变量
        self.environment_variables = environment_variables
        # 实例创建时间
        self.gmt_create_time = gmt_create_time
        # 实例修改时间
        self.gmt_modified_time = gmt_modified_time
        # 镜像Id
        self.image_id = image_id
        # 镜像名称
        self.image_name = image_name
        # 镜像地址
        self.image_url = image_url
        # 实例Id
        self.instance_id = instance_id
        # 实例名称
        self.instance_name = instance_name
        # 定时关机任务
        self.instance_shutdown_timer = instance_shutdown_timer
        # 实例Url
        self.instance_url = instance_url
        # Jupyterlab Url
        self.jupyterlab_url = jupyterlab_url
        # 最新保存的用户镜像
        self.latest_snapshot = latest_snapshot
        # 支付类型
        self.payment_type = payment_type
        # 实例错误代码
        self.reason_code = reason_code
        # 实例错误原因
        self.reason_message = reason_message
        # 实例状态
        self.status = status
        # terminal url
        self.terminal_url = terminal_url
        # 用户Id
        self.user_id = user_id
        # user vpc配置
        self.user_vpc = user_vpc
        # web ide url
        self.web_ideurl = web_ideurl
        # 工作空间Id
        self.workspace_id = workspace_id
        # 工作空间名称
        self.workspace_name = workspace_name

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.latest_snapshot:
            self.latest_snapshot.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.accumulated_running_time_in_ms is not None:
            result['AccumulatedRunningTimeInMs'] = self.accumulated_running_time_in_ms
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        if self.latest_snapshot is not None:
            result['LatestSnapshot'] = self.latest_snapshot.to_map()
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.status is not None:
            result['Status'] = self.status
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ideurl is not None:
            result['WebIDEUrl'] = self.web_ideurl
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('AccumulatedRunningTimeInMs') is not None:
            self.accumulated_running_time_in_ms = m.get('AccumulatedRunningTimeInMs')
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = UpdateInstanceV2RequestDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = UpdateInstanceV2RequestInstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        if m.get('LatestSnapshot') is not None:
            temp_model = UpdateInstanceV2RequestLatestSnapshot()
            self.latest_snapshot = temp_model.from_map(m['LatestSnapshot'])
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = UpdateInstanceV2RequestUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIDEUrl') is not None:
            self.web_ideurl = m.get('WebIDEUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class UpdateInstanceV2ResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 工作空间Id
        self.instance_id = instance_id
        # 请求Id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateInstanceV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateInstanceV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateV3InstanceByUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateV3InstanceByUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        id_list: List[int] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_set: List[str] = None,
        workspace_id: str = None,
    ):
        # 状态码
        self.code = code
        # http状态码
        self.http_status_code = http_status_code
        self.id_list = id_list
        # 说明
        self.message = message
        # 请求Id
        self.request_id = request_id
        # 成功标志
        self.success = success
        self.user_set = user_set
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.id_list is not None:
            result['IdList'] = self.id_list
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user_set is not None:
            result['UserSet'] = self.user_set
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UserSet') is not None:
            self.user_set = m.get('UserSet')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateV3InstanceByUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateV3InstanceByUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateV3InstanceByUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


