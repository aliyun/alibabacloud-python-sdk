# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


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
        cuda_version: str = None,
        framework: str = None,
        framework_version: str = None,
        image_id: str = None,
        image_name: str = None,
        instance_id: str = None,
        os: str = None,
        osversion: str = None,
        type: str = None,
    ):
        # 资源类型
        self.accelerator_type = accelerator_type
        # Cuda版本
        self.cuda_version = cuda_version
        # 算法框架
        self.framework = framework
        # 算法框架版本
        self.framework_version = framework_version
        # 镜像ID
        self.image_id = image_id
        # 镜像名称
        self.image_name = image_name
        # 实例ID
        self.instance_id = instance_id
        # 镜像操作系统分发版
        self.os = os
        # 分发版版本
        self.osversion = osversion
        # 镜像类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.cuda_version is not None:
            result['CudaVersion'] = self.cuda_version
        if self.framework is not None:
            result['Framework'] = self.framework
        if self.framework_version is not None:
            result['FrameworkVersion'] = self.framework_version
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.os is not None:
            result['OS'] = self.os
        if self.osversion is not None:
            result['OSVersion'] = self.osversion
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('CudaVersion') is not None:
            self.cuda_version = m.get('CudaVersion')
        if m.get('Framework') is not None:
            self.framework = m.get('Framework')
        if m.get('FrameworkVersion') is not None:
            self.framework_version = m.get('FrameworkVersion')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OS') is not None:
            self.os = m.get('OS')
        if m.get('OSVersion') is not None:
            self.osversion = m.get('OSVersion')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class InstanceShutdownTimer(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        schedule_time: str = None,
    ):
        # 定时关机修改时间
        self.gmt_create_time = gmt_create_time
        # 定时关机创建时间
        self.gmt_modified_time = gmt_modified_time
        # 实例ID
        self.instance_id = instance_id
        # 定时关机时间
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
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
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
        instance_url: str = None,
        jupyterlab_url: str = None,
        nas_file_system_id: str = None,
        terminal_url: str = None,
        user_id: str = None,
        user_vpc: UserVpc = None,
        web_ide_url: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # 累计运行时间(分钟)
        self.accumulative_running_time_in_minutes = accumulative_running_time_in_minutes
        # ecs规格
        self.ecs_spec = ecs_spec
        # 创建时间(GMT)
        self.gmt_create_time = gmt_create_time
        # 修改时间(GMT)
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
        # dsw实例链接
        self.instance_url = instance_url
        # jupyter链接
        self.jupyterlab_url = jupyterlab_url
        # nas文件系统ID
        self.nas_file_system_id = nas_file_system_id
        # 命令行终端链接
        self.terminal_url = terminal_url
        # 用户ID
        self.user_id = user_id
        # 被打通VPC配置
        self.user_vpc = user_vpc
        # webIde链接
        self.web_ide_url = web_ide_url
        # 工作空间id
        self.workspace_id = workspace_id
        # 工作空间名称
        self.workspace_name = workspace_name

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
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        if self.nas_file_system_id is not None:
            result['NasFileSystemId'] = self.nas_file_system_id
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
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
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        if m.get('NasFileSystemId') is not None:
            self.nas_file_system_id = m.get('NasFileSystemId')
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        ecs_spec: str = None,
        image_id: str = None,
        image_url: str = None,
        instance_name: str = None,
        nas_file_system_id: str = None,
        user_vpc: UserVpc = None,
    ):
        # 实例规格
        self.ecs_spec = ecs_spec
        # 镜像id
        self.image_id = image_id
        # 镜像地址
        self.image_url = image_url
        # 实例名称
        self.instance_name = instance_name
        # nas文件系统id
        self.nas_file_system_id = nas_file_system_id
        # 打通的vpc网络配置
        self.user_vpc = user_vpc

    def validate(self):
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.nas_file_system_id is not None:
            result['NasFileSystemId'] = self.nas_file_system_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('NasFileSystemId') is not None:
            self.nas_file_system_id = m.get('NasFileSystemId')
        if m.get('UserVpc') is not None:
            temp_model = UserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
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
    ):
        # 定时关机时间(GMT)
        self.schedule_time = schedule_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
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


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        accelerator_type_equals: str = None,
        image_name_contains: str = None,
        image_type_equals: str = None,
    ):
        # 资源类型
        self.accelerator_type_equals = accelerator_type_equals
        # 容器名称关键字
        self.image_name_contains = image_name_contains
        # 镜像类型
        self.image_type_equals = image_type_equals

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorTypeEquals') is not None:
            self.accelerator_type_equals = m.get('AcceleratorTypeEquals')
        if m.get('ImageNameContains') is not None:
            self.image_name_contains = m.get('ImageNameContains')
        if m.get('ImageTypeEquals') is not None:
            self.image_type_equals = m.get('ImageTypeEquals')
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


