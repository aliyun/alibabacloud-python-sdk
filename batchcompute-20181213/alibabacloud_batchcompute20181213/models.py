# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class UserStage(TeaModel):
    def __init__(
        self,
        description: str = None,
        end_time: int = None,
        start_time: int = None,
        state: str = None,
    ):
        # Description
        self.description = description
        # EndTime
        self.end_time = end_time
        # StartTime
        self.start_time = start_time
        # State
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class Attempt(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        exit_code: int = None,
        output: bytes = None,
        pid: int = None,
        reason: str = None,
        start_time: str = None,
        state: str = None,
        user_stages: List[UserStage] = None,
        worker: str = None,
    ):
        # EndTime
        self.end_time = end_time
        # ExitCode
        self.exit_code = exit_code
        # Output
        self.output = output
        # Pid
        self.pid = pid
        # Reason
        self.reason = reason
        # StartTime
        self.start_time = start_time
        # State
        self.state = state
        # UserStages
        self.user_stages = user_stages
        # Worker
        self.worker = worker

    def validate(self):
        if self.user_stages:
            for k in self.user_stages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.output is not None:
            result['Output'] = self.output
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        result['UserStages'] = []
        if self.user_stages is not None:
            for k in self.user_stages:
                result['UserStages'].append(k.to_map() if k else None)
        if self.worker is not None:
            result['Worker'] = self.worker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.user_stages = []
        if m.get('UserStages') is not None:
            for k in m.get('UserStages'):
                temp_model = UserStage()
                self.user_stages.append(temp_model.from_map(k))
        if m.get('Worker') is not None:
            self.worker = m.get('Worker')
        return self


class Scaling(TeaModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: float = None,
        max_worker_count: int = None,
        metric_type: str = None,
        metric_value: float = None,
        min_worker_count: int = None,
        tolerance_value: float = None,
    ):
        # AdjustmentType
        self.adjustment_type = adjustment_type
        # AdjustmentValue
        self.adjustment_value = adjustment_value
        # MaxWorkerCount
        self.max_worker_count = max_worker_count
        # MetricType
        self.metric_type = metric_type
        # MetricValue
        self.metric_value = metric_value
        # MinWorkerCount
        self.min_worker_count = min_worker_count
        # ToleranceValue
        self.tolerance_value = tolerance_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.max_worker_count is not None:
            result['MaxWorkerCount'] = self.max_worker_count
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.metric_value is not None:
            result['MetricValue'] = self.metric_value
        if self.min_worker_count is not None:
            result['MinWorkerCount'] = self.min_worker_count
        if self.tolerance_value is not None:
            result['ToleranceValue'] = self.tolerance_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('MaxWorkerCount') is not None:
            self.max_worker_count = m.get('MaxWorkerCount')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('MetricValue') is not None:
            self.metric_value = m.get('MetricValue')
        if m.get('MinWorkerCount') is not None:
            self.min_worker_count = m.get('MinWorkerCount')
        if m.get('ToleranceValue') is not None:
            self.tolerance_value = m.get('ToleranceValue')
        return self


class Trigger(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        first_launch_time: str = None,
        repeat_type: str = None,
        repeat_value: str = None,
    ):
        # Enabled
        self.enabled = enabled
        # FirstLaunchTime
        self.first_launch_time = first_launch_time
        # RepeatType
        self.repeat_type = repeat_type
        # RepeatValue
        self.repeat_value = repeat_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.first_launch_time is not None:
            result['FirstLaunchTime'] = self.first_launch_time
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.repeat_value is not None:
            result['RepeatValue'] = self.repeat_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('FirstLaunchTime') is not None:
            self.first_launch_time = m.get('FirstLaunchTime')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('RepeatValue') is not None:
            self.repeat_value = m.get('RepeatValue')
        return self


class AutoScaling(TeaModel):
    def __init__(
        self,
        scaling: Scaling = None,
        trigger: Trigger = None,
    ):
        # Scaling
        self.scaling = scaling
        # Trigger
        self.trigger = trigger

    def validate(self):
        if self.scaling:
            self.scaling.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scaling is not None:
            result['Scaling'] = self.scaling.to_map()
        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scaling') is not None:
            temp_model = Scaling()
            self.scaling = temp_model.from_map(m['Scaling'])
        if m.get('Trigger') is not None:
            temp_model = Trigger()
            self.trigger = temp_model.from_map(m['Trigger'])
        return self


class OSSLogging(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        prefix: str = None,
    ):
        # Bucket
        self.bucket = bucket
        # Prefix
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class SLSLogging(TeaModel):
    def __init__(
        self,
        logtail_config_name: str = None,
        project: str = None,
        store: str = None,
    ):
        # LogtailConfigName
        self.logtail_config_name = logtail_config_name
        # Project
        self.project = project
        # Store
        self.store = store

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logtail_config_name is not None:
            result['LogtailConfigName'] = self.logtail_config_name
        if self.project is not None:
            result['Project'] = self.project
        if self.store is not None:
            result['Store'] = self.store
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogtailConfigName') is not None:
            self.logtail_config_name = m.get('LogtailConfigName')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Store') is not None:
            self.store = m.get('Store')
        return self


class Logging(TeaModel):
    def __init__(
        self,
        name: str = None,
        oss: OSSLogging = None,
        path: str = None,
        sls: SLSLogging = None,
    ):
        # Name
        self.name = name
        # OSS
        self.oss = oss
        # Path
        self.path = path
        # SLS
        self.sls = sls

    def validate(self):
        if self.oss:
            self.oss.validate()
        if self.sls:
            self.sls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.oss is not None:
            result['OSS'] = self.oss.to_map()
        if self.path is not None:
            result['Path'] = self.path
        if self.sls is not None:
            result['SLS'] = self.sls.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OSS') is not None:
            temp_model = OSSLogging()
            self.oss = temp_model.from_map(m['OSS'])
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SLS') is not None:
            temp_model = SLSLogging()
            self.sls = temp_model.from_map(m['SLS'])
        return self


class MountPoint(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        # MountPath
        self.mount_path = mount_path
        # Name
        self.name = name
        # ReadOnly
        self.read_only = read_only
        # SubPath
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class ExposedPort(TeaModel):
    def __init__(
        self,
        container_port: int = None,
        host_ports: List[int] = None,
        proto: str = None,
    ):
        # ContainerPort
        self.container_port = container_port
        # HostPorts
        self.host_ports = host_ports
        # Proto
        self.proto = proto

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_port is not None:
            result['ContainerPort'] = self.container_port
        if self.host_ports is not None:
            result['HostPorts'] = self.host_ports
        if self.proto is not None:
            result['Proto'] = self.proto
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerPort') is not None:
            self.container_port = m.get('ContainerPort')
        if m.get('HostPorts') is not None:
            self.host_ports = m.get('HostPorts')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        return self


class Docker(TeaModel):
    def __init__(
        self,
        exposed_ports: List[ExposedPort] = None,
        image: str = None,
    ):
        # ExposedPorts
        self.exposed_ports = exposed_ports
        # Image
        self.image = image

    def validate(self):
        if self.exposed_ports:
            for k in self.exposed_ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExposedPorts'] = []
        if self.exposed_ports is not None:
            for k in self.exposed_ports:
                result['ExposedPorts'].append(k.to_map() if k else None)
        if self.image is not None:
            result['Image'] = self.image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exposed_ports = []
        if m.get('ExposedPorts') is not None:
            for k in m.get('ExposedPorts'):
                temp_model = ExposedPort()
                self.exposed_ports.append(temp_model.from_map(k))
        if m.get('Image') is not None:
            self.image = m.get('Image')
        return self


class BootstrapRuntime(TeaModel):
    def __init__(
        self,
        docker: Docker = None,
    ):
        # Docker
        self.docker = docker

    def validate(self):
        if self.docker:
            self.docker.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docker is not None:
            result['Docker'] = self.docker.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Docker') is not None:
            temp_model = Docker()
            self.docker = temp_model.from_map(m['Docker'])
        return self


class NFSVolumeSource(TeaModel):
    def __init__(
        self,
        path: str = None,
        read_only: bool = None,
        server: str = None,
        version: str = None,
    ):
        # Path
        self.path = path
        # ReadOnly
        self.read_only = read_only
        # Server
        self.server = server
        # Version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.server is not None:
            result['Server'] = self.server
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class OSSVolumeSource(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        object: str = None,
        prefix: str = None,
        read_only: bool = None,
    ):
        # Bucket
        self.bucket = bucket
        # Object
        self.object = object
        # Prefix
        self.prefix = prefix
        # ReadOnly
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.object is not None:
            result['Object'] = self.object
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        return self


class PDSVolumeSource(TeaModel):
    def __init__(
        self,
        domain: str = None,
        drive: str = None,
        object: str = None,
        prefix: str = None,
        read_only: bool = None,
    ):
        # Domain
        self.domain = domain
        # Drive
        self.drive = drive
        # Object
        self.object = object
        # Prefix
        self.prefix = prefix
        # ReadOnly
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.drive is not None:
            result['Drive'] = self.drive
        if self.object is not None:
            result['Object'] = self.object
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Drive') is not None:
            self.drive = m.get('Drive')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        return self


class Volume(TeaModel):
    def __init__(
        self,
        nfs: NFSVolumeSource = None,
        name: str = None,
        oss: OSSVolumeSource = None,
        pds: PDSVolumeSource = None,
    ):
        # NFS
        self.nfs = nfs
        # Name
        self.name = name
        # OSS
        self.oss = oss
        # PDS
        self.pds = pds

    def validate(self):
        if self.nfs:
            self.nfs.validate()
        if self.oss:
            self.oss.validate()
        if self.pds:
            self.pds.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nfs is not None:
            result['NFS'] = self.nfs.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.oss is not None:
            result['OSS'] = self.oss.to_map()
        if self.pds is not None:
            result['PDS'] = self.pds.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NFS') is not None:
            temp_model = NFSVolumeSource()
            self.nfs = temp_model.from_map(m['NFS'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OSS') is not None:
            temp_model = OSSVolumeSource()
            self.oss = temp_model.from_map(m['OSS'])
        if m.get('PDS') is not None:
            temp_model = PDSVolumeSource()
            self.pds = temp_model.from_map(m['PDS'])
        return self


class Bootstrap(TeaModel):
    def __init__(
        self,
        background: bool = None,
        command: List[str] = None,
        envs: Dict[str, str] = None,
        loggings: Logging = None,
        mount_points: List[MountPoint] = None,
        package_uri: str = None,
        running_timeout: int = None,
        runtimes: BootstrapRuntime = None,
        volumes: List[Volume] = None,
    ):
        # Background
        self.background = background
        # Command
        self.command = command
        # Envs
        self.envs = envs
        # Loggings
        self.loggings = loggings
        # MountPoints
        self.mount_points = mount_points
        # PackageUri
        self.package_uri = package_uri
        # RunningTimeout
        self.running_timeout = running_timeout
        # Runtimes
        self.runtimes = runtimes
        # Volumes
        self.volumes = volumes

    def validate(self):
        if self.loggings:
            self.loggings.validate()
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()
        if self.runtimes:
            self.runtimes.validate()
        if self.volumes:
            for k in self.volumes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background is not None:
            result['Background'] = self.background
        if self.command is not None:
            result['Command'] = self.command
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.loggings is not None:
            result['Loggings'] = self.loggings.to_map()
        result['MountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['MountPoints'].append(k.to_map() if k else None)
        if self.package_uri is not None:
            result['PackageUri'] = self.package_uri
        if self.running_timeout is not None:
            result['RunningTimeout'] = self.running_timeout
        if self.runtimes is not None:
            result['Runtimes'] = self.runtimes.to_map()
        result['Volumes'] = []
        if self.volumes is not None:
            for k in self.volumes:
                result['Volumes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Background') is not None:
            self.background = m.get('Background')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('Loggings') is not None:
            temp_model = Logging()
            self.loggings = temp_model.from_map(m['Loggings'])
        self.mount_points = []
        if m.get('MountPoints') is not None:
            for k in m.get('MountPoints'):
                temp_model = MountPoint()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('PackageUri') is not None:
            self.package_uri = m.get('PackageUri')
        if m.get('RunningTimeout') is not None:
            self.running_timeout = m.get('RunningTimeout')
        if m.get('Runtimes') is not None:
            temp_model = BootstrapRuntime()
            self.runtimes = temp_model.from_map(m['Runtimes'])
        self.volumes = []
        if m.get('Volumes') is not None:
            for k in m.get('Volumes'):
                temp_model = Volume()
                self.volumes.append(temp_model.from_map(k))
        return self


class ServiceRoleNode(TeaModel):
    def __init__(
        self,
        assume_role_for: str = None,
        role: str = None,
        role_type: str = None,
    ):
        # AssumeRoleFor
        self.assume_role_for = assume_role_for
        # Role
        self.role = role
        # RoleType
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for
        if self.role is not None:
            result['Role'] = self.role
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class CredentialConfig(TeaModel):
    def __init__(
        self,
        chain: List[ServiceRoleNode] = None,
        policy: str = None,
        service_role: str = None,
    ):
        # Chain
        self.chain = chain
        # Policy
        self.policy = policy
        # ServiceRole
        self.service_role = service_role

    def validate(self):
        if self.chain:
            for k in self.chain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Chain'] = []
        if self.chain is not None:
            for k in self.chain:
                result['Chain'].append(k.to_map() if k else None)
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chain = []
        if m.get('Chain') is not None:
            for k in m.get('Chain'):
                temp_model = ServiceRoleNode()
                self.chain.append(temp_model.from_map(k))
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        return self


class ECS(TeaModel):
    def __init__(
        self,
        hostname_prefix: str = None,
        instance_type: str = None,
        password_inherit: bool = None,
        resource_type: str = None,
        spot_price_limit: str = None,
        spot_strategy: str = None,
        system_disk_size: int = None,
        system_disk_type: str = None,
        vmimage: str = None,
    ):
        # HostnamePrefix
        self.hostname_prefix = hostname_prefix
        # InstanceType
        self.instance_type = instance_type
        # PasswordInherit
        self.password_inherit = password_inherit
        # ResourceType
        self.resource_type = resource_type
        # SpotPriceLimit
        self.spot_price_limit = spot_price_limit
        # SpotStrategy
        self.spot_strategy = spot_strategy
        # SystemDiskSize
        self.system_disk_size = system_disk_size
        # SystemDiskType
        self.system_disk_type = system_disk_type
        # VMImage
        self.vmimage = vmimage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname_prefix is not None:
            result['HostnamePrefix'] = self.hostname_prefix
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        if self.vmimage is not None:
            result['VMImage'] = self.vmimage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostnamePrefix') is not None:
            self.hostname_prefix = m.get('HostnamePrefix')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        if m.get('VMImage') is not None:
            self.vmimage = m.get('VMImage')
        return self


class ExecAction(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        # Command
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class HTTPHeader(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # Name
        self.name = name
        # Value
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


class HTTPGetAction(TeaModel):
    def __init__(
        self,
        httpheaders: List[HTTPHeader] = None,
        host: str = None,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        # HTTPHeaders
        self.httpheaders = httpheaders
        # Host
        self.host = host
        # Path
        self.path = path
        # Port
        self.port = port
        # Scheme
        self.scheme = scheme

    def validate(self):
        if self.httpheaders:
            for k in self.httpheaders:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HTTPHeaders'] = []
        if self.httpheaders is not None:
            for k in self.httpheaders:
                result['HTTPHeaders'].append(k.to_map() if k else None)
        if self.host is not None:
            result['Host'] = self.host
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.httpheaders = []
        if m.get('HTTPHeaders') is not None:
            for k in m.get('HTTPHeaders'):
                temp_model = HTTPHeader()
                self.httpheaders.append(temp_model.from_map(k))
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class Handler(TeaModel):
    def __init__(
        self,
        exec: ExecAction = None,
        httpget: HTTPGetAction = None,
    ):
        # Exec
        self.exec = exec
        # HTTPGet
        self.httpget = httpget

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.httpget:
            self.httpget.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.httpget is not None:
            result['HTTPGet'] = self.httpget.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = ExecAction()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('HTTPGet') is not None:
            temp_model = HTTPGetAction()
            self.httpget = temp_model.from_map(m['HTTPGet'])
        return self


class Probe(TeaModel):
    def __init__(
        self,
        failure_threshold: int = None,
        handler: Handler = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        timeout_seconds: int = None,
    ):
        # FailureThreshold
        self.failure_threshold = failure_threshold
        # Handler
        self.handler = handler
        # InitialDelaySeconds
        self.initial_delay_seconds = initial_delay_seconds
        # PeriodSeconds
        self.period_seconds = period_seconds
        # SuccessThreshold
        self.success_threshold = success_threshold
        # TimeoutSeconds
        self.timeout_seconds = timeout_seconds

    def validate(self):
        if self.handler:
            self.handler.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.handler is not None:
            result['Handler'] = self.handler.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('Handler') is not None:
            temp_model = Handler()
            self.handler = temp_model.from_map(m['Handler'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class SLB(TeaModel):
    def __init__(
        self,
        slbid: str = None,
    ):
        # SLBId
        self.slbid = slbid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slbid is not None:
            result['SLBId'] = self.slbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SLBId') is not None:
            self.slbid = m.get('SLBId')
        return self


class UpgradePolicy(TeaModel):
    def __init__(
        self,
        upgrade_ratio: float = None,
    ):
        # UpgradeRatio
        self.upgrade_ratio = upgrade_ratio

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.upgrade_ratio is not None:
            result['UpgradeRatio'] = self.upgrade_ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpgradeRatio') is not None:
            self.upgrade_ratio = m.get('UpgradeRatio')
        return self


class VPC(TeaModel):
    def __init__(
        self,
        security_groups: List[str] = None,
        vpcid: str = None,
        v_switches: List[str] = None,
    ):
        # SecurityGroups
        self.security_groups = security_groups
        # VPCId
        self.vpcid = vpcid
        # VSwitches
        self.v_switches = v_switches

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroups') is not None:
            self.security_groups = m.get('SecurityGroups')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        return self


class ClusterDefinition(TeaModel):
    def __init__(
        self,
        auto_scaling: List[AutoScaling] = None,
        bootstrap: Bootstrap = None,
        credential_configs: CredentialConfig = None,
        docker: Docker = None,
        ecs: ECS = None,
        liveness_probe: Probe = None,
        managed_job_queue: bool = None,
        mount_points: List[MountPoint] = None,
        provider_type: str = None,
        resources: Dict[str, str] = None,
        slb: SLB = None,
        scaling: Scaling = None,
        startup_probe: Probe = None,
        upgrade_policy: UpgradePolicy = None,
        vpc: VPC = None,
        volumes: List[Volume] = None,
        worker_type: str = None,
    ):
        # AutoScaling
        self.auto_scaling = auto_scaling
        # Bootstrap
        self.bootstrap = bootstrap
        # CredentialConfigs
        self.credential_configs = credential_configs
        # Docker
        self.docker = docker
        # ECS
        self.ecs = ecs
        # LivenessProbe
        self.liveness_probe = liveness_probe
        # ManagedJobQueue
        self.managed_job_queue = managed_job_queue
        # MountPoints
        self.mount_points = mount_points
        # ProviderType
        self.provider_type = provider_type
        # Resources
        self.resources = resources
        # SLB
        self.slb = slb
        # Scaling
        self.scaling = scaling
        # StartupProbe
        self.startup_probe = startup_probe
        # UpgradePolicy
        self.upgrade_policy = upgrade_policy
        # VPC
        self.vpc = vpc
        # Volumes
        self.volumes = volumes
        # WorkerType
        self.worker_type = worker_type

    def validate(self):
        if self.auto_scaling:
            for k in self.auto_scaling:
                if k:
                    k.validate()
        if self.bootstrap:
            self.bootstrap.validate()
        if self.credential_configs:
            self.credential_configs.validate()
        if self.docker:
            self.docker.validate()
        if self.ecs:
            self.ecs.validate()
        if self.liveness_probe:
            self.liveness_probe.validate()
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()
        if self.slb:
            self.slb.validate()
        if self.scaling:
            self.scaling.validate()
        if self.startup_probe:
            self.startup_probe.validate()
        if self.upgrade_policy:
            self.upgrade_policy.validate()
        if self.vpc:
            self.vpc.validate()
        if self.volumes:
            for k in self.volumes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoScaling'] = []
        if self.auto_scaling is not None:
            for k in self.auto_scaling:
                result['AutoScaling'].append(k.to_map() if k else None)
        if self.bootstrap is not None:
            result['Bootstrap'] = self.bootstrap.to_map()
        if self.credential_configs is not None:
            result['CredentialConfigs'] = self.credential_configs.to_map()
        if self.docker is not None:
            result['Docker'] = self.docker.to_map()
        if self.ecs is not None:
            result['ECS'] = self.ecs.to_map()
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()
        if self.managed_job_queue is not None:
            result['ManagedJobQueue'] = self.managed_job_queue
        result['MountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['MountPoints'].append(k.to_map() if k else None)
        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.slb is not None:
            result['SLB'] = self.slb.to_map()
        if self.scaling is not None:
            result['Scaling'] = self.scaling.to_map()
        if self.startup_probe is not None:
            result['StartupProbe'] = self.startup_probe.to_map()
        if self.upgrade_policy is not None:
            result['UpgradePolicy'] = self.upgrade_policy.to_map()
        if self.vpc is not None:
            result['VPC'] = self.vpc.to_map()
        result['Volumes'] = []
        if self.volumes is not None:
            for k in self.volumes:
                result['Volumes'].append(k.to_map() if k else None)
        if self.worker_type is not None:
            result['WorkerType'] = self.worker_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_scaling = []
        if m.get('AutoScaling') is not None:
            for k in m.get('AutoScaling'):
                temp_model = AutoScaling()
                self.auto_scaling.append(temp_model.from_map(k))
        if m.get('Bootstrap') is not None:
            temp_model = Bootstrap()
            self.bootstrap = temp_model.from_map(m['Bootstrap'])
        if m.get('CredentialConfigs') is not None:
            temp_model = CredentialConfig()
            self.credential_configs = temp_model.from_map(m['CredentialConfigs'])
        if m.get('Docker') is not None:
            temp_model = Docker()
            self.docker = temp_model.from_map(m['Docker'])
        if m.get('ECS') is not None:
            temp_model = ECS()
            self.ecs = temp_model.from_map(m['ECS'])
        if m.get('LivenessProbe') is not None:
            temp_model = Probe()
            self.liveness_probe = temp_model.from_map(m['LivenessProbe'])
        if m.get('ManagedJobQueue') is not None:
            self.managed_job_queue = m.get('ManagedJobQueue')
        self.mount_points = []
        if m.get('MountPoints') is not None:
            for k in m.get('MountPoints'):
                temp_model = MountPoint()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('SLB') is not None:
            temp_model = SLB()
            self.slb = temp_model.from_map(m['SLB'])
        if m.get('Scaling') is not None:
            temp_model = Scaling()
            self.scaling = temp_model.from_map(m['Scaling'])
        if m.get('StartupProbe') is not None:
            temp_model = Probe()
            self.startup_probe = temp_model.from_map(m['StartupProbe'])
        if m.get('UpgradePolicy') is not None:
            temp_model = UpgradePolicy()
            self.upgrade_policy = temp_model.from_map(m['UpgradePolicy'])
        if m.get('VPC') is not None:
            temp_model = VPC()
            self.vpc = temp_model.from_map(m['VPC'])
        self.volumes = []
        if m.get('Volumes') is not None:
            for k in m.get('Volumes'):
                temp_model = Volume()
                self.volumes.append(temp_model.from_map(k))
        if m.get('WorkerType') is not None:
            self.worker_type = m.get('WorkerType')
        return self


class Errors(TeaModel):
    def __init__(
        self,
        action: str = None,
        code: str = None,
        message: str = None,
        repeat: int = None,
    ):
        # Action
        self.action = action
        # Code
        self.code = code
        # Message
        self.message = message
        # Repeat
        self.repeat = repeat

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.repeat is not None:
            result['Repeat'] = self.repeat
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Repeat') is not None:
            self.repeat = m.get('Repeat')
        return self


class Conditions(TeaModel):
    def __init__(
        self,
        condition: str = None,
        errors: List[Errors] = None,
        last_probe_time: str = None,
        last_transition_time: str = None,
        status: str = None,
    ):
        # Condition
        self.condition = condition
        # Errors
        self.errors = errors
        # LastProbeTime
        self.last_probe_time = last_probe_time
        # LastTransitionTime
        self.last_transition_time = last_transition_time
        # Status
        self.status = status

    def validate(self):
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.last_probe_time is not None:
            result['LastProbeTime'] = self.last_probe_time
        if self.last_transition_time is not None:
            result['LastTransitionTime'] = self.last_transition_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = Errors()
                self.errors.append(temp_model.from_map(k))
        if m.get('LastProbeTime') is not None:
            self.last_probe_time = m.get('LastProbeTime')
        if m.get('LastTransitionTime') is not None:
            self.last_transition_time = m.get('LastTransitionTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class OSSDescription(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        object: str = None,
        prefix: str = None,
    ):
        # Bucket
        self.bucket = bucket
        # Object
        self.object = object
        # Prefix
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.object is not None:
            result['Object'] = self.object
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class PDSDescription(TeaModel):
    def __init__(
        self,
        domain: str = None,
        drive: str = None,
        object: str = None,
        prefix: str = None,
    ):
        # Domain
        self.domain = domain
        # Drive
        self.drive = drive
        # Object
        self.object = object
        # Prefix
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.drive is not None:
            result['Drive'] = self.drive
        if self.object is not None:
            result['Object'] = self.object
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Drive') is not None:
            self.drive = m.get('Drive')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class Destination(TeaModel):
    def __init__(
        self,
        oss: OSSDescription = None,
        pds: PDSDescription = None,
    ):
        self.oss = oss
        self.pds = pds

    def validate(self):
        if self.oss:
            self.oss.validate()
        if self.pds:
            self.pds.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss is not None:
            result['OSS'] = self.oss.to_map()
        if self.pds is not None:
            result['PDS'] = self.pds.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSS') is not None:
            temp_model = OSSDescription()
            self.oss = temp_model.from_map(m['OSS'])
        if m.get('PDS') is not None:
            temp_model = PDSDescription()
            self.pds = temp_model.from_map(m['PDS'])
        return self


class Exec(TeaModel):
    def __init__(
        self,
        exec: ExecAction = None,
    ):
        # Exec
        self.exec = exec

    def validate(self):
        if self.exec:
            self.exec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = ExecAction()
            self.exec = temp_model.from_map(m['Exec'])
        return self


class FailStrategy(TeaModel):
    def __init__(
        self,
        max_retries: int = None,
        running_timeout: int = None,
        success_code: List[int] = None,
        waiting_timeout: int = None,
    ):
        # MaxRetries
        self.max_retries = max_retries
        # RunningTimeout
        self.running_timeout = running_timeout
        # SuccessCode
        self.success_code = success_code
        # WaitingTimeout
        self.waiting_timeout = waiting_timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_retries is not None:
            result['MaxRetries'] = self.max_retries
        if self.running_timeout is not None:
            result['RunningTimeout'] = self.running_timeout
        if self.success_code is not None:
            result['SuccessCode'] = self.success_code
        if self.waiting_timeout is not None:
            result['WaitingTimeout'] = self.waiting_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxRetries') is not None:
            self.max_retries = m.get('MaxRetries')
        if m.get('RunningTimeout') is not None:
            self.running_timeout = m.get('RunningTimeout')
        if m.get('SuccessCode') is not None:
            self.success_code = m.get('SuccessCode')
        if m.get('WaitingTimeout') is not None:
            self.waiting_timeout = m.get('WaitingTimeout')
        return self


class HTTPGet(TeaModel):
    def __init__(
        self,
        httpget: HTTPGetAction = None,
    ):
        # HTTPGet
        self.httpget = httpget

    def validate(self):
        if self.httpget:
            self.httpget.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.httpget is not None:
            result['HTTPGet'] = self.httpget.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HTTPGet') is not None:
            temp_model = HTTPGetAction()
            self.httpget = temp_model.from_map(m['HTTPGet'])
        return self


class Source(TeaModel):
    def __init__(
        self,
        oss: OSSDescription = None,
        pds: PDSDescription = None,
    ):
        self.oss = oss
        self.pds = pds

    def validate(self):
        if self.oss:
            self.oss.validate()
        if self.pds:
            self.pds.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss is not None:
            result['OSS'] = self.oss.to_map()
        if self.pds is not None:
            result['PDS'] = self.pds.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSS') is not None:
            temp_model = OSSDescription()
            self.oss = temp_model.from_map(m['OSS'])
        if m.get('PDS') is not None:
            temp_model = PDSDescription()
            self.pds = temp_model.from_map(m['PDS'])
        return self


class Input(TeaModel):
    def __init__(
        self,
        file_mode: str = None,
        file_path: str = None,
        source: Source = None,
    ):
        # FileMode
        self.file_mode = file_mode
        # FilePath
        self.file_path = file_path
        self.source = source

    def validate(self):
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_mode is not None:
            result['FileMode'] = self.file_mode
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.source is not None:
            result['Source'] = self.source.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileMode') is not None:
            self.file_mode = m.get('FileMode')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Source') is not None:
            temp_model = Source()
            self.source = temp_model.from_map(m['Source'])
        return self


class MNSNotification(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        filters: List[str] = None,
        topic: str = None,
    ):
        # Endpoint
        self.endpoint = endpoint
        # Filters
        self.filters = filters
        # Topic
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class Notification(TeaModel):
    def __init__(
        self,
        mns: MNSNotification = None,
    ):
        # MNS
        self.mns = mns

    def validate(self):
        if self.mns:
            self.mns.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mns is not None:
            result['MNS'] = self.mns.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MNS') is not None:
            temp_model = MNSNotification()
            self.mns = temp_model.from_map(m['MNS'])
        return self


class Output(TeaModel):
    def __init__(
        self,
        destination: Destination = None,
        file_pattern: str = None,
        upload_conditions: List[str] = None,
        upload_mode: str = None,
    ):
        # Destination
        self.destination = destination
        # FilePattern
        self.file_pattern = file_pattern
        # UploadConditions
        self.upload_conditions = upload_conditions
        # UploadMode
        self.upload_mode = upload_mode

    def validate(self):
        if self.destination:
            self.destination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['Destination'] = self.destination.to_map()
        if self.file_pattern is not None:
            result['FilePattern'] = self.file_pattern
        if self.upload_conditions is not None:
            result['UploadConditions'] = self.upload_conditions
        if self.upload_mode is not None:
            result['UploadMode'] = self.upload_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Destination') is not None:
            temp_model = Destination()
            self.destination = temp_model.from_map(m['Destination'])
        if m.get('FilePattern') is not None:
            self.file_pattern = m.get('FilePattern')
        if m.get('UploadConditions') is not None:
            self.upload_conditions = m.get('UploadConditions')
        if m.get('UploadMode') is not None:
            self.upload_mode = m.get('UploadMode')
        return self


class ReleaseCondition(TeaModel):
    def __init__(
        self,
        state: str = None,
        ttlseconds: int = None,
    ):
        # State
        self.state = state
        # TTLSeconds
        self.ttlseconds = ttlseconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.ttlseconds is not None:
            result['TTLSeconds'] = self.ttlseconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TTLSeconds') is not None:
            self.ttlseconds = m.get('TTLSeconds')
        return self


class ReleaseStrategy(TeaModel):
    def __init__(
        self,
        release_conditions: List[ReleaseCondition] = None,
    ):
        # ReleaseConditions
        self.release_conditions = release_conditions

    def validate(self):
        if self.release_conditions:
            for k in self.release_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReleaseConditions'] = []
        if self.release_conditions is not None:
            for k in self.release_conditions:
                result['ReleaseConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.release_conditions = []
        if m.get('ReleaseConditions') is not None:
            for k in m.get('ReleaseConditions'):
                temp_model = ReleaseCondition()
                self.release_conditions.append(temp_model.from_map(k))
        return self


class Runtimes(TeaModel):
    def __init__(
        self,
        docker: Docker = None,
        ecs: ECS = None,
        job_queue: str = None,
        vpc: VPC = None,
    ):
        # Docker
        self.docker = docker
        # ECS
        self.ecs = ecs
        # JobQueue
        self.job_queue = job_queue
        # VPC
        self.vpc = vpc

    def validate(self):
        if self.docker:
            self.docker.validate()
        if self.ecs:
            self.ecs.validate()
        if self.vpc:
            self.vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docker is not None:
            result['Docker'] = self.docker.to_map()
        if self.ecs is not None:
            result['ECS'] = self.ecs.to_map()
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.vpc is not None:
            result['VPC'] = self.vpc.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Docker') is not None:
            temp_model = Docker()
            self.docker = temp_model.from_map(m['Docker'])
        if m.get('ECS') is not None:
            temp_model = ECS()
            self.ecs = temp_model.from_map(m['ECS'])
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('VPC') is not None:
            temp_model = VPC()
            self.vpc = temp_model.from_map(m['VPC'])
        return self


class JobDefinition(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
        credential_config: CredentialConfig = None,
        envs: Dict[str, str] = None,
        fail_strategy: FailStrategy = None,
        inputs: List[Input] = None,
        labels: Dict[str, str] = None,
        loggings: Logging = None,
        mount_points: List[MountPoint] = None,
        notification: Notification = None,
        outputs: List[Output] = None,
        package_uri: str = None,
        release_strategy: ReleaseStrategy = None,
        resources: Dict[str, str] = None,
        runtimes: Runtimes = None,
        user_data: Dict[str, str] = None,
        volumes: List[Volume] = None,
    ):
        # Command
        self.command = command
        # CredentialConfig
        self.credential_config = credential_config
        # Envs
        self.envs = envs
        # FailStrategy
        self.fail_strategy = fail_strategy
        # Inputs
        self.inputs = inputs
        # Labels
        self.labels = labels
        # Loggings
        self.loggings = loggings
        # MountPoints
        self.mount_points = mount_points
        # Notification
        self.notification = notification
        # Outputs
        self.outputs = outputs
        # PackageUri
        self.package_uri = package_uri
        # ReleaseStrategy
        self.release_strategy = release_strategy
        # Resources
        self.resources = resources
        # Runtimes
        self.runtimes = runtimes
        # UserData
        self.user_data = user_data
        # Volumes
        self.volumes = volumes

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.fail_strategy:
            self.fail_strategy.validate()
        if self.inputs:
            for k in self.inputs:
                if k:
                    k.validate()
        if self.loggings:
            self.loggings.validate()
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()
        if self.notification:
            self.notification.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        if self.release_strategy:
            self.release_strategy.validate()
        if self.runtimes:
            self.runtimes.validate()
        if self.volumes:
            for k in self.volumes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.fail_strategy is not None:
            result['FailStrategy'] = self.fail_strategy.to_map()
        result['Inputs'] = []
        if self.inputs is not None:
            for k in self.inputs:
                result['Inputs'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.loggings is not None:
            result['Loggings'] = self.loggings.to_map()
        result['MountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['MountPoints'].append(k.to_map() if k else None)
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        if self.package_uri is not None:
            result['PackageUri'] = self.package_uri
        if self.release_strategy is not None:
            result['ReleaseStrategy'] = self.release_strategy.to_map()
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.runtimes is not None:
            result['Runtimes'] = self.runtimes.to_map()
        if self.user_data is not None:
            result['UserData'] = self.user_data
        result['Volumes'] = []
        if self.volumes is not None:
            for k in self.volumes:
                result['Volumes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('FailStrategy') is not None:
            temp_model = FailStrategy()
            self.fail_strategy = temp_model.from_map(m['FailStrategy'])
        self.inputs = []
        if m.get('Inputs') is not None:
            for k in m.get('Inputs'):
                temp_model = Input()
                self.inputs.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Loggings') is not None:
            temp_model = Logging()
            self.loggings = temp_model.from_map(m['Loggings'])
        self.mount_points = []
        if m.get('MountPoints') is not None:
            for k in m.get('MountPoints'):
                temp_model = MountPoint()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = Output()
                self.outputs.append(temp_model.from_map(k))
        if m.get('PackageUri') is not None:
            self.package_uri = m.get('PackageUri')
        if m.get('ReleaseStrategy') is not None:
            temp_model = ReleaseStrategy()
            self.release_strategy = temp_model.from_map(m['ReleaseStrategy'])
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Runtimes') is not None:
            temp_model = Runtimes()
            self.runtimes = temp_model.from_map(m['Runtimes'])
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        self.volumes = []
        if m.get('Volumes') is not None:
            for k in m.get('Volumes'):
                temp_model = Volume()
                self.volumes.append(temp_model.from_map(k))
        return self


class JobQueueDefinitionSchedulerConfig(TeaModel):
    def __init__(
        self,
        state: str = None,
    ):
        # State
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ProviderConfig(TeaModel):
    def __init__(
        self,
        max_worker_count: int = None,
        min_worker_count: int = None,
        provider_id: str = None,
        provider_type: str = None,
        worker_type: str = None,
    ):
        # MaxWorkerCount
        self.max_worker_count = max_worker_count
        # MinWorkerCount
        self.min_worker_count = min_worker_count
        # ProviderId
        self.provider_id = provider_id
        # ProviderType
        self.provider_type = provider_type
        # WorkerType
        self.worker_type = worker_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_worker_count is not None:
            result['MaxWorkerCount'] = self.max_worker_count
        if self.min_worker_count is not None:
            result['MinWorkerCount'] = self.min_worker_count
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type
        if self.worker_type is not None:
            result['WorkerType'] = self.worker_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxWorkerCount') is not None:
            self.max_worker_count = m.get('MaxWorkerCount')
        if m.get('MinWorkerCount') is not None:
            self.min_worker_count = m.get('MinWorkerCount')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')
        if m.get('WorkerType') is not None:
            self.worker_type = m.get('WorkerType')
        return self


class JobQueueDefinition(TeaModel):
    def __init__(
        self,
        labels: Dict[str, str] = None,
        priority: int = None,
        provider_configs: List[ProviderConfig] = None,
        scheduler_config: JobQueueDefinitionSchedulerConfig = None,
    ):
        # Labels
        self.labels = labels
        # Priority
        self.priority = priority
        # ProviderConfigs
        self.provider_configs = provider_configs
        # SchedulerConfig
        self.scheduler_config = scheduler_config

    def validate(self):
        if self.provider_configs:
            for k in self.provider_configs:
                if k:
                    k.validate()
        if self.scheduler_config:
            self.scheduler_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.priority is not None:
            result['Priority'] = self.priority
        result['ProviderConfigs'] = []
        if self.provider_configs is not None:
            for k in self.provider_configs:
                result['ProviderConfigs'].append(k.to_map() if k else None)
        if self.scheduler_config is not None:
            result['SchedulerConfig'] = self.scheduler_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.provider_configs = []
        if m.get('ProviderConfigs') is not None:
            for k in m.get('ProviderConfigs'):
                temp_model = ProviderConfig()
                self.provider_configs.append(temp_model.from_map(k))
        if m.get('SchedulerConfig') is not None:
            temp_model = JobQueueDefinitionSchedulerConfig()
            self.scheduler_config = temp_model.from_map(m['SchedulerConfig'])
        return self


class ProviderStatus(TeaModel):
    def __init__(
        self,
        allocatable_resources: Dict[str, str] = None,
        allocated_resources: Dict[str, str] = None,
        provider_id: str = None,
    ):
        # AllocatableResources
        self.allocatable_resources = allocatable_resources
        # AllocatedResources
        self.allocated_resources = allocated_resources
        # ProviderId
        self.provider_id = provider_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocatable_resources is not None:
            result['AllocatableResources'] = self.allocatable_resources
        if self.allocated_resources is not None:
            result['AllocatedResources'] = self.allocated_resources
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatableResources') is not None:
            self.allocatable_resources = m.get('AllocatableResources')
        if m.get('AllocatedResources') is not None:
            self.allocated_resources = m.get('AllocatedResources')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        return self


class SchedulerStatus(TeaModel):
    def __init__(
        self,
        canceled_job_count: int = None,
        failed_job_count: int = None,
        running_job_count: int = None,
        succeeded_job_count: int = None,
        waiting_job_count: int = None,
    ):
        # CanceledJobCount
        self.canceled_job_count = canceled_job_count
        # FailedJobCount
        self.failed_job_count = failed_job_count
        # RunningJobCount
        self.running_job_count = running_job_count
        # SucceededJobCount
        self.succeeded_job_count = succeeded_job_count
        # WaitingJobCount
        self.waiting_job_count = waiting_job_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.canceled_job_count is not None:
            result['CanceledJobCount'] = self.canceled_job_count
        if self.failed_job_count is not None:
            result['FailedJobCount'] = self.failed_job_count
        if self.running_job_count is not None:
            result['RunningJobCount'] = self.running_job_count
        if self.succeeded_job_count is not None:
            result['SucceededJobCount'] = self.succeeded_job_count
        if self.waiting_job_count is not None:
            result['WaitingJobCount'] = self.waiting_job_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanceledJobCount') is not None:
            self.canceled_job_count = m.get('CanceledJobCount')
        if m.get('FailedJobCount') is not None:
            self.failed_job_count = m.get('FailedJobCount')
        if m.get('RunningJobCount') is not None:
            self.running_job_count = m.get('RunningJobCount')
        if m.get('SucceededJobCount') is not None:
            self.succeeded_job_count = m.get('SucceededJobCount')
        if m.get('WaitingJobCount') is not None:
            self.waiting_job_count = m.get('WaitingJobCount')
        return self


class JobQueueStatus(TeaModel):
    def __init__(
        self,
        allocatable_resources: Dict[str, str] = None,
        allocated_resources: Dict[str, str] = None,
        create_time: str = None,
        last_update_time: str = None,
        managed: bool = None,
        provider_statuses: List[ProviderStatus] = None,
        reason: str = None,
        scheduler_status: SchedulerStatus = None,
        state: str = None,
    ):
        # AllocatableResources
        self.allocatable_resources = allocatable_resources
        # AllocatedResources
        self.allocated_resources = allocated_resources
        # CreateTime
        self.create_time = create_time
        # LastUpdateTime
        self.last_update_time = last_update_time
        # Managed
        self.managed = managed
        # ProviderStatuses
        self.provider_statuses = provider_statuses
        # Reason
        self.reason = reason
        self.scheduler_status = scheduler_status
        # State
        self.state = state

    def validate(self):
        if self.provider_statuses:
            for k in self.provider_statuses:
                if k:
                    k.validate()
        if self.scheduler_status:
            self.scheduler_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocatable_resources is not None:
            result['AllocatableResources'] = self.allocatable_resources
        if self.allocated_resources is not None:
            result['AllocatedResources'] = self.allocated_resources
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.managed is not None:
            result['Managed'] = self.managed
        result['ProviderStatuses'] = []
        if self.provider_statuses is not None:
            for k in self.provider_statuses:
                result['ProviderStatuses'].append(k.to_map() if k else None)
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.scheduler_status is not None:
            result['SchedulerStatus'] = self.scheduler_status.to_map()
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatableResources') is not None:
            self.allocatable_resources = m.get('AllocatableResources')
        if m.get('AllocatedResources') is not None:
            self.allocated_resources = m.get('AllocatedResources')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Managed') is not None:
            self.managed = m.get('Managed')
        self.provider_statuses = []
        if m.get('ProviderStatuses') is not None:
            for k in m.get('ProviderStatuses'):
                temp_model = ProviderStatus()
                self.provider_statuses.append(temp_model.from_map(k))
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SchedulerStatus') is not None:
            temp_model = SchedulerStatus()
            self.scheduler_status = temp_model.from_map(m['SchedulerStatus'])
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ProjectDefinition(TeaModel):
    def __init__(
        self,
        job_lifecycle: int = None,
        labels: Dict[str, str] = None,
        role: str = None,
    ):
        # JobLifecycle
        self.job_lifecycle = job_lifecycle
        # Labels
        self.labels = labels
        # Role
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_lifecycle is not None:
            result['JobLifecycle'] = self.job_lifecycle
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class WorkerStatusContainer(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory: int = None,
    ):
        # Cpu
        self.cpu = cpu
        # Memory
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class WorkerStatusECS(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        endpoint: str = None,
        hostname: str = None,
        instance_id: str = None,
        instance_type: str = None,
        memory: int = None,
        password: str = None,
        resource_type: str = None,
        spot_price_limit: str = None,
        spot_strategy: str = None,
        system_disk_size: int = None,
        system_disk_type: str = None,
        vmimage: str = None,
        zone_id: str = None,
    ):
        # Cpu
        self.cpu = cpu
        # Endpoint
        self.endpoint = endpoint
        # Hostname
        self.hostname = hostname
        # InstanceId
        self.instance_id = instance_id
        # InstanceType
        self.instance_type = instance_type
        # Memory
        self.memory = memory
        # Password
        self.password = password
        # ResourceType
        self.resource_type = resource_type
        # SpotPriceLimit
        self.spot_price_limit = spot_price_limit
        # SpotStrategy
        self.spot_strategy = spot_strategy
        # SystemDiskSize
        self.system_disk_size = system_disk_size
        # SystemDiskType
        self.system_disk_type = system_disk_type
        # VMImage
        self.vmimage = vmimage
        # ZoneId
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.password is not None:
            result['Password'] = self.password
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        if self.vmimage is not None:
            result['VMImage'] = self.vmimage
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        if m.get('VMImage') is not None:
            self.vmimage = m.get('VMImage')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class WorkerStatus(TeaModel):
    def __init__(
        self,
        conditions: List[Conditions] = None,
        container: WorkerStatusContainer = None,
        create_time: str = None,
        ecs: WorkerStatusECS = None,
        job_queue: str = None,
        network_interface_id: str = None,
        pool_worker_id: str = None,
        security_group_id: str = None,
        state: str = None,
        v_switch_id: str = None,
        worker_type: int = None,
    ):
        # Conditions
        self.conditions = conditions
        # Container
        self.container = container
        # CreateTime
        self.create_time = create_time
        # ECS
        self.ecs = ecs
        # JobQueue
        self.job_queue = job_queue
        # NetworkInterfaceId
        self.network_interface_id = network_interface_id
        # PoolWorkerId
        self.pool_worker_id = pool_worker_id
        # SecurityGroupId
        self.security_group_id = security_group_id
        # State
        self.state = state
        # VSwitchId
        self.v_switch_id = v_switch_id
        # WorkerType
        self.worker_type = worker_type

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.container:
            self.container.validate()
        if self.ecs:
            self.ecs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.container is not None:
            result['Container'] = self.container.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ecs is not None:
            result['ECS'] = self.ecs.to_map()
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.pool_worker_id is not None:
            result['PoolWorkerId'] = self.pool_worker_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.state is not None:
            result['State'] = self.state
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.worker_type is not None:
            result['WorkerType'] = self.worker_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = Conditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Container') is not None:
            temp_model = WorkerStatusContainer()
            self.container = temp_model.from_map(m['Container'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ECS') is not None:
            temp_model = WorkerStatusECS()
            self.ecs = temp_model.from_map(m['ECS'])
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PoolWorkerId') is not None:
            self.pool_worker_id = m.get('PoolWorkerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('WorkerType') is not None:
            self.worker_type = m.get('WorkerType')
        return self


class CancelJobRequest(TeaModel):
    def __init__(
        self,
        exit_code: str = None,
        job_id: str = None,
        project: str = None,
        reason: str = None,
    ):
        self.exit_code = exit_code
        self.job_id = job_id
        self.project = project
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.project is not None:
            result['Project'] = self.project
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class CancelJobResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelJobResponseBody = None,
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
            temp_model = CancelJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        definition: ClusterDefinition = None,
        description: str = None,
        name: str = None,
        project: str = None,
    ):
        self.client_token = client_token
        # Definition
        self.definition = definition
        # Description
        self.description = description
        # Name
        self.name = name
        # Project
        self.project = project

    def validate(self):
        if self.definition:
            self.definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Definition') is not None:
            temp_model = ClusterDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class CreateClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        definition_shrink: str = None,
        description: str = None,
        name: str = None,
        project: str = None,
    ):
        self.client_token = client_token
        # Definition
        self.definition_shrink = definition_shrink
        # Description
        self.description = description
        # Name
        self.name = name
        # Project
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.definition_shrink is not None:
            result['Definition'] = self.definition_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Definition') is not None:
            self.definition_shrink = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        host_id: str = None,
        request_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateClusterResponseBody = None,
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        definition: JobDefinition = None,
        description: str = None,
        name: str = None,
        project: str = None,
    ):
        self.client_token = client_token
        self.definition = definition
        self.description = description
        self.name = name
        self.project = project

    def validate(self):
        if self.definition:
            self.definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Definition') is not None:
            temp_model = JobDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class CreateJobShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        definition_shrink: str = None,
        description: str = None,
        name: str = None,
        project: str = None,
    ):
        self.client_token = client_token
        self.definition_shrink = definition_shrink
        self.description = description
        self.name = name
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.definition_shrink is not None:
            result['Definition'] = self.definition_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Definition') is not None:
            self.definition_shrink = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        job_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.job_id = job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateJobResponseBody = None,
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
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobQueueRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        definition: JobQueueDefinition = None,
        description: str = None,
        name: str = None,
        project: str = None,
    ):
        self.client_token = client_token
        self.definition = definition
        self.description = description
        self.name = name
        self.project = project

    def validate(self):
        if self.definition:
            self.definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Definition') is not None:
            temp_model = JobQueueDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class CreateJobQueueShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        definition_shrink: str = None,
        description: str = None,
        name: str = None,
        project: str = None,
    ):
        self.client_token = client_token
        self.definition_shrink = definition_shrink
        self.description = description
        self.name = name
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.definition_shrink is not None:
            result['Definition'] = self.definition_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Definition') is not None:
            self.definition_shrink = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class CreateJobQueueResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        name: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.name = name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateJobQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateJobQueueResponseBody = None,
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
            temp_model = CreateJobQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        definition: ProjectDefinition = None,
        description: str = None,
        project: str = None,
    ):
        self.client_token = client_token
        self.definition = definition
        self.description = description
        self.project = project

    def validate(self):
        if self.definition:
            self.definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Definition') is not None:
            temp_model = ProjectDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class CreateProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        definition_shrink: str = None,
        description: str = None,
        project: str = None,
    ):
        self.client_token = client_token
        self.definition_shrink = definition_shrink
        self.description = description
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.definition_shrink is not None:
            result['Definition'] = self.definition_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Definition') is not None:
            self.definition_shrink = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        project: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.project = project
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.project is not None:
            result['Project'] = self.project
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProjectResponseBody = None,
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        project: str = None,
    ):
        # ClusterId
        self.cluster_id = cluster_id
        # Project
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteClusterResponseBody = None,
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
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        project: str = None,
    ):
        self.job_id = job_id
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DeleteJobResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteJobResponseBody = None,
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
            temp_model = DeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobQueueRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        project: str = None,
    ):
        self.name = name
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DeleteJobQueueResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteJobQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteJobQueueResponseBody = None,
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
            temp_model = DeleteJobQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
    ):
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProjectResponseBody = None,
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        project: str = None,
    ):
        self.cluster_id = cluster_id
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class GetClusterResponseBodyStatus(TeaModel):
    def __init__(
        self,
        allocatable_resources: Dict[str, str] = None,
        allocated_resources: Dict[str, str] = None,
        conditions: List[Conditions] = None,
        create_time: str = None,
        current_worker_count: int = None,
        desired_worker_count: int = None,
        state: str = None,
    ):
        self.allocatable_resources = allocatable_resources
        self.allocated_resources = allocated_resources
        self.conditions = conditions
        self.create_time = create_time
        self.current_worker_count = current_worker_count
        self.desired_worker_count = desired_worker_count
        self.state = state

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocatable_resources is not None:
            result['AllocatableResources'] = self.allocatable_resources
        if self.allocated_resources is not None:
            result['AllocatedResources'] = self.allocated_resources
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_worker_count is not None:
            result['CurrentWorkerCount'] = self.current_worker_count
        if self.desired_worker_count is not None:
            result['DesiredWorkerCount'] = self.desired_worker_count
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatableResources') is not None:
            self.allocatable_resources = m.get('AllocatableResources')
        if m.get('AllocatedResources') is not None:
            self.allocated_resources = m.get('AllocatedResources')
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = Conditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentWorkerCount') is not None:
            self.current_worker_count = m.get('CurrentWorkerCount')
        if m.get('DesiredWorkerCount') is not None:
            self.desired_worker_count = m.get('DesiredWorkerCount')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        definition: ClusterDefinition = None,
        description: str = None,
        host_id: str = None,
        name: str = None,
        owner_id: str = None,
        project: str = None,
        request_id: str = None,
        status: GetClusterResponseBodyStatus = None,
    ):
        self.cluster_id = cluster_id
        self.definition = definition
        self.description = description
        self.host_id = host_id
        self.name = name
        self.owner_id = owner_id
        self.project = project
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.definition:
            self.definition.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Definition') is not None:
            temp_model = ClusterDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = GetClusterResponseBodyStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class GetClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetClusterResponseBody = None,
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
            temp_model = GetClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        project: str = None,
    ):
        self.job_id = job_id
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class GetJobResponseBodyStatus(TeaModel):
    def __init__(
        self,
        attempts: List[Attempt] = None,
        create_time: str = None,
        end_time: str = None,
        exit_code: int = None,
        pid: int = None,
        reason: str = None,
        start_time: str = None,
        state: str = None,
        worker: str = None,
    ):
        self.attempts = attempts
        self.create_time = create_time
        self.end_time = end_time
        self.exit_code = exit_code
        self.pid = pid
        self.reason = reason
        self.start_time = start_time
        self.state = state
        self.worker = worker

    def validate(self):
        if self.attempts:
            for k in self.attempts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attempts'] = []
        if self.attempts is not None:
            for k in self.attempts:
                result['Attempts'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.worker is not None:
            result['Worker'] = self.worker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attempts = []
        if m.get('Attempts') is not None:
            for k in m.get('Attempts'):
                temp_model = Attempt()
                self.attempts.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Worker') is not None:
            self.worker = m.get('Worker')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(
        self,
        definition: JobDefinition = None,
        description: str = None,
        host_id: str = None,
        job_id: str = None,
        name: str = None,
        owner_id: str = None,
        project: str = None,
        request_id: str = None,
        status: GetJobResponseBodyStatus = None,
    ):
        self.definition = definition
        self.description = description
        self.host_id = host_id
        self.job_id = job_id
        self.name = name
        self.owner_id = owner_id
        self.project = project
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.definition:
            self.definition.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            temp_model = JobDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = GetJobResponseBodyStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class GetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJobResponseBody = None,
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
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobQueueRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        project: str = None,
    ):
        self.name = name
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class GetJobQueueResponseBody(TeaModel):
    def __init__(
        self,
        definition: JobQueueDefinition = None,
        description: str = None,
        host_id: str = None,
        name: str = None,
        owner_id: str = None,
        project: str = None,
        request_id: str = None,
        status: JobQueueStatus = None,
    ):
        self.definition = definition
        self.description = description
        self.host_id = host_id
        self.name = name
        self.owner_id = owner_id
        self.project = project
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.definition:
            self.definition.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            temp_model = JobQueueDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = JobQueueStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class GetJobQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJobQueueResponseBody = None,
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
            temp_model = GetJobQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
    ):
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class GetProjectResponseBodyStatus(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        last_modified_time: str = None,
    ):
        self.create_time = create_time
        self.last_modified_time = last_modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(
        self,
        definition: ProjectDefinition = None,
        description: str = None,
        host_id: str = None,
        project: str = None,
        request_id: str = None,
        status: GetProjectResponseBodyStatus = None,
    ):
        self.definition = definition
        self.description = description
        self.host_id = host_id
        self.project = project
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.definition:
            self.definition.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.project is not None:
            result['Project'] = self.project
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            temp_model = ProjectDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = GetProjectResponseBodyStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProjectResponseBody = None,
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
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkerRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        project: str = None,
        worker_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.project = project
        self.worker_id = worker_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.project is not None:
            result['Project'] = self.project
        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')
        return self


class GetWorkerResponseBodyStatusContainer(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory: int = None,
    ):
        self.cpu = cpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class GetWorkerResponseBodyStatusECS(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        endpoint: str = None,
        hostname: str = None,
        instance_id: str = None,
        instance_type: str = None,
        memory: int = None,
        password: str = None,
        resource_type: str = None,
        spot_price_limit: str = None,
        spot_strategy: str = None,
        system_disk_size: int = None,
        system_disk_type: str = None,
        vmimage: str = None,
        zone_id: str = None,
    ):
        self.cpu = cpu
        self.endpoint = endpoint
        self.hostname = hostname
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.memory = memory
        self.password = password
        self.resource_type = resource_type
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk_size = system_disk_size
        self.system_disk_type = system_disk_type
        self.vmimage = vmimage
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.password is not None:
            result['Password'] = self.password
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        if self.vmimage is not None:
            result['VMImage'] = self.vmimage
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        if m.get('VMImage') is not None:
            self.vmimage = m.get('VMImage')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetWorkerResponseBodyStatus(TeaModel):
    def __init__(
        self,
        active_time: str = None,
        allocate_time: str = None,
        conditions: List[Conditions] = None,
        container: GetWorkerResponseBodyStatusContainer = None,
        create_time: str = None,
        ecs: GetWorkerResponseBodyStatusECS = None,
        job_queue: str = None,
        network_interface_id: str = None,
        pool_worker_id: str = None,
        security_group_id: str = None,
        state: str = None,
        v_switch_id: str = None,
        worker_type: int = None,
    ):
        self.active_time = active_time
        self.allocate_time = allocate_time
        self.conditions = conditions
        self.container = container
        self.create_time = create_time
        self.ecs = ecs
        self.job_queue = job_queue
        self.network_interface_id = network_interface_id
        self.pool_worker_id = pool_worker_id
        self.security_group_id = security_group_id
        self.state = state
        self.v_switch_id = v_switch_id
        self.worker_type = worker_type

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.container:
            self.container.validate()
        if self.ecs:
            self.ecs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.allocate_time is not None:
            result['AllocateTime'] = self.allocate_time
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.container is not None:
            result['Container'] = self.container.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ecs is not None:
            result['ECS'] = self.ecs.to_map()
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.pool_worker_id is not None:
            result['PoolWorkerId'] = self.pool_worker_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.state is not None:
            result['State'] = self.state
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.worker_type is not None:
            result['WorkerType'] = self.worker_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('AllocateTime') is not None:
            self.allocate_time = m.get('AllocateTime')
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = Conditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Container') is not None:
            temp_model = GetWorkerResponseBodyStatusContainer()
            self.container = temp_model.from_map(m['Container'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ECS') is not None:
            temp_model = GetWorkerResponseBodyStatusECS()
            self.ecs = temp_model.from_map(m['ECS'])
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PoolWorkerId') is not None:
            self.pool_worker_id = m.get('PoolWorkerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('WorkerType') is not None:
            self.worker_type = m.get('WorkerType')
        return self


class GetWorkerResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        status: GetWorkerResponseBodyStatus = None,
        worker_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id
        self.status = status
        self.worker_id = worker_id

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = GetWorkerResponseBodyStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')
        return self


class GetWorkerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWorkerResponseBody = None,
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
            temp_model = GetWorkerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillWorkerRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        project: str = None,
        worker_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.project = project
        self.worker_id = worker_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.project is not None:
            result['Project'] = self.project
        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')
        return self


class KillWorkerResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KillWorkerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: KillWorkerResponseBody = None,
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
            temp_model = KillWorkerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        project: str = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class ListClustersResponseBodyClustersStatus(TeaModel):
    def __init__(
        self,
        allocatable_resources: Dict[str, str] = None,
        allocated_resources: Dict[str, str] = None,
        conditions: List[Conditions] = None,
        create_time: str = None,
        current_worker_count: int = None,
        desired_worker_count: int = None,
        state: str = None,
    ):
        self.allocatable_resources = allocatable_resources
        self.allocated_resources = allocated_resources
        self.conditions = conditions
        self.create_time = create_time
        self.current_worker_count = current_worker_count
        self.desired_worker_count = desired_worker_count
        self.state = state

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocatable_resources is not None:
            result['AllocatableResources'] = self.allocatable_resources
        if self.allocated_resources is not None:
            result['AllocatedResources'] = self.allocated_resources
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_worker_count is not None:
            result['CurrentWorkerCount'] = self.current_worker_count
        if self.desired_worker_count is not None:
            result['DesiredWorkerCount'] = self.desired_worker_count
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatableResources') is not None:
            self.allocatable_resources = m.get('AllocatableResources')
        if m.get('AllocatedResources') is not None:
            self.allocated_resources = m.get('AllocatedResources')
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = Conditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentWorkerCount') is not None:
            self.current_worker_count = m.get('CurrentWorkerCount')
        if m.get('DesiredWorkerCount') is not None:
            self.desired_worker_count = m.get('DesiredWorkerCount')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        definition: ClusterDefinition = None,
        description: str = None,
        name: str = None,
        owner_id: str = None,
        project: str = None,
        status: ListClustersResponseBodyClustersStatus = None,
    ):
        self.cluster_id = cluster_id
        self.definition = definition
        self.description = description
        self.name = name
        self.owner_id = owner_id
        self.project = project
        self.status = status

    def validate(self):
        if self.definition:
            self.definition.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Definition') is not None:
            temp_model = ClusterDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Status') is not None:
            temp_model = ListClustersResponseBodyClustersStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[ListClustersResponseBodyClusters] = None,
        host_id: str = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.clusters = clusters
        self.host_id = host_id
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = ListClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClustersResponseBody = None,
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
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobQueuesRequest(TeaModel):
    def __init__(
        self,
        label_selector: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        order_reverse: bool = None,
        project: str = None,
        state: str = None,
    ):
        self.label_selector = label_selector
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
        self.order_reverse = order_reverse
        self.project = project
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_reverse is not None:
            result['OrderReverse'] = self.order_reverse
        if self.project is not None:
            result['Project'] = self.project
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderReverse') is not None:
            self.order_reverse = m.get('OrderReverse')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListJobQueuesResponseBodyJobQueues(TeaModel):
    def __init__(
        self,
        definition: JobQueueDefinition = None,
        description: str = None,
        name: str = None,
        next_token: str = None,
        owner_id: str = None,
        project: str = None,
        status: JobQueueStatus = None,
        total_count: int = None,
    ):
        self.definition = definition
        self.description = description
        self.name = name
        self.next_token = next_token
        self.owner_id = owner_id
        self.project = project
        self.status = status
        self.total_count = total_count

    def validate(self):
        if self.definition:
            self.definition.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            temp_model = JobQueueDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Status') is not None:
            temp_model = JobQueueStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobQueuesResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        job_queues: List[ListJobQueuesResponseBodyJobQueues] = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.job_queues = job_queues
        self.request_id = request_id

    def validate(self):
        if self.job_queues:
            for k in self.job_queues:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        result['JobQueues'] = []
        if self.job_queues is not None:
            for k in self.job_queues:
                result['JobQueues'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        self.job_queues = []
        if m.get('JobQueues') is not None:
            for k in m.get('JobQueues'):
                temp_model = ListJobQueuesResponseBodyJobQueues()
                self.job_queues.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListJobQueuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListJobQueuesResponseBody = None,
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
            temp_model = ListJobQueuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        label_selector: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        order_by: str = None,
        order_reverse: bool = None,
        project: str = None,
        state: str = None,
    ):
        self.cluster_id = cluster_id
        self.label_selector = label_selector
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.order_by = order_by
        self.order_reverse = order_reverse
        self.project = project
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_reverse is not None:
            result['OrderReverse'] = self.order_reverse
        if self.project is not None:
            result['Project'] = self.project
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderReverse') is not None:
            self.order_reverse = m.get('OrderReverse')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListJobsResponseBodyJobsStatus(TeaModel):
    def __init__(
        self,
        attempts: List[Attempt] = None,
        create_time: str = None,
        end_time: str = None,
        exit_code: int = None,
        pid: int = None,
        reason: str = None,
        start_time: str = None,
        state: str = None,
        worker: str = None,
    ):
        self.attempts = attempts
        self.create_time = create_time
        self.end_time = end_time
        self.exit_code = exit_code
        self.pid = pid
        self.reason = reason
        self.start_time = start_time
        self.state = state
        self.worker = worker

    def validate(self):
        if self.attempts:
            for k in self.attempts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attempts'] = []
        if self.attempts is not None:
            for k in self.attempts:
                result['Attempts'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.worker is not None:
            result['Worker'] = self.worker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attempts = []
        if m.get('Attempts') is not None:
            for k in m.get('Attempts'):
                temp_model = Attempt()
                self.attempts.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Worker') is not None:
            self.worker = m.get('Worker')
        return self


class ListJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        definition: JobDefinition = None,
        description: str = None,
        job_id: str = None,
        name: str = None,
        owner_id: str = None,
        project: str = None,
        status: ListJobsResponseBodyJobsStatus = None,
    ):
        self.definition = definition
        self.description = description
        self.job_id = job_id
        self.name = name
        self.owner_id = owner_id
        self.project = project
        self.status = status

    def validate(self):
        if self.definition:
            self.definition.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            temp_model = JobDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Status') is not None:
            temp_model = ListJobsResponseBodyJobsStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        jobs: List[ListJobsResponseBodyJobs] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.host_id = host_id
        self.jobs = jobs
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListJobsResponseBody = None,
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
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        label_selector: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        order_reverse: bool = None,
    ):
        self.label_selector = label_selector
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
        self.order_reverse = order_reverse

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_reverse is not None:
            result['OrderReverse'] = self.order_reverse
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderReverse') is not None:
            self.order_reverse = m.get('OrderReverse')
        return self


class ListProjectsResponseBodyProjectsStatus(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        last_modified_time: str = None,
    ):
        self.create_time = create_time
        self.last_modified_time = last_modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        return self


class ListProjectsResponseBodyProjects(TeaModel):
    def __init__(
        self,
        definition: ProjectDefinition = None,
        description: str = None,
        project: str = None,
        status: ListProjectsResponseBodyProjectsStatus = None,
    ):
        self.definition = definition
        self.description = description
        self.project = project
        self.status = status

    def validate(self):
        if self.definition:
            self.definition.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.project is not None:
            result['Project'] = self.project
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            temp_model = ProjectDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Status') is not None:
            temp_model = ListProjectsResponseBodyProjectsStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        projects: List[ListProjectsResponseBodyProjects] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.projects = projects
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = ListProjectsResponseBodyProjects()
                self.projects.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectsResponseBody = None,
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class ListRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        regions: List[ListRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRegionsResponseBody = None,
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkersRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        project: str = None,
    ):
        self.cluster_id = cluster_id
        self.max_results = max_results
        self.next_token = next_token
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class ListWorkersResponseBodyWorkersStatusContainer(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory: int = None,
    ):
        self.cpu = cpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListWorkersResponseBodyWorkersStatusECS(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        endpoint: str = None,
        hostname: str = None,
        instance_id: str = None,
        instance_type: str = None,
        memory: int = None,
        password: str = None,
        resource_type: str = None,
        spot_price_limit: str = None,
        spot_strategy: str = None,
        system_disk_size: int = None,
        system_disk_type: str = None,
        vmimage: str = None,
        zone_id: str = None,
    ):
        self.cpu = cpu
        self.endpoint = endpoint
        self.hostname = hostname
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.memory = memory
        self.password = password
        self.resource_type = resource_type
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk_size = system_disk_size
        self.system_disk_type = system_disk_type
        self.vmimage = vmimage
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.password is not None:
            result['Password'] = self.password
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        if self.vmimage is not None:
            result['VMImage'] = self.vmimage
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        if m.get('VMImage') is not None:
            self.vmimage = m.get('VMImage')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListWorkersResponseBodyWorkersStatus(TeaModel):
    def __init__(
        self,
        active_time: str = None,
        allocate_time: str = None,
        conditions: List[Conditions] = None,
        container: ListWorkersResponseBodyWorkersStatusContainer = None,
        create_time: str = None,
        ecs: ListWorkersResponseBodyWorkersStatusECS = None,
        job_queue: str = None,
        network_interface_id: str = None,
        pool_worker_id: str = None,
        security_group_id: str = None,
        state: str = None,
        v_switch_id: str = None,
        worker_type: int = None,
    ):
        self.active_time = active_time
        self.allocate_time = allocate_time
        self.conditions = conditions
        self.container = container
        self.create_time = create_time
        self.ecs = ecs
        self.job_queue = job_queue
        self.network_interface_id = network_interface_id
        self.pool_worker_id = pool_worker_id
        self.security_group_id = security_group_id
        self.state = state
        self.v_switch_id = v_switch_id
        self.worker_type = worker_type

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.container:
            self.container.validate()
        if self.ecs:
            self.ecs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.allocate_time is not None:
            result['AllocateTime'] = self.allocate_time
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.container is not None:
            result['Container'] = self.container.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ecs is not None:
            result['ECS'] = self.ecs.to_map()
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.pool_worker_id is not None:
            result['PoolWorkerId'] = self.pool_worker_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.state is not None:
            result['State'] = self.state
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.worker_type is not None:
            result['WorkerType'] = self.worker_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('AllocateTime') is not None:
            self.allocate_time = m.get('AllocateTime')
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = Conditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Container') is not None:
            temp_model = ListWorkersResponseBodyWorkersStatusContainer()
            self.container = temp_model.from_map(m['Container'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ECS') is not None:
            temp_model = ListWorkersResponseBodyWorkersStatusECS()
            self.ecs = temp_model.from_map(m['ECS'])
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PoolWorkerId') is not None:
            self.pool_worker_id = m.get('PoolWorkerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('WorkerType') is not None:
            self.worker_type = m.get('WorkerType')
        return self


class ListWorkersResponseBodyWorkers(TeaModel):
    def __init__(
        self,
        status: ListWorkersResponseBodyWorkersStatus = None,
        worker_id: str = None,
    ):
        self.status = status
        self.worker_id = worker_id

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            temp_model = ListWorkersResponseBodyWorkersStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')
        return self


class ListWorkersResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        workers: List[ListWorkersResponseBodyWorkers] = None,
    ):
        self.host_id = host_id
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.workers = workers

    def validate(self):
        if self.workers:
            for k in self.workers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Workers'] = []
        if self.workers is not None:
            for k in self.workers:
                result['Workers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.workers = []
        if m.get('Workers') is not None:
            for k in m.get('Workers'):
                temp_model = ListWorkersResponseBodyWorkers()
                self.workers.append(temp_model.from_map(k))
        return self


class ListWorkersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListWorkersResponseBody = None,
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
            temp_model = ListWorkersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenBatchComputeServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenBatchComputeServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenBatchComputeServiceResponseBody = None,
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
            temp_model = OpenBatchComputeServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PollCmdRequest(TeaModel):
    def __init__(
        self,
        queue: str = None,
        wait_seconds: str = None,
        worker_id: str = None,
    ):
        self.queue = queue
        self.wait_seconds = wait_seconds
        self.worker_id = worker_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.wait_seconds is not None:
            result['WaitSeconds'] = self.wait_seconds
        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('WaitSeconds') is not None:
            self.wait_seconds = m.get('WaitSeconds')
        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')
        return self


class PollCmdResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PollCmdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PollCmdResponseBody = None,
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
            temp_model = PollCmdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecreateWorkerRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        project: str = None,
        worker_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.project = project
        self.worker_id = worker_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.project is not None:
            result['Project'] = self.project
        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')
        return self


class RecreateWorkerResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecreateWorkerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecreateWorkerResponseBody = None,
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
            temp_model = RecreateWorkerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        definition: JobDefinition = None,
        description: str = None,
        name: str = None,
        project: str = None,
    ):
        self.client_token = client_token
        self.definition = definition
        self.description = description
        self.name = name
        self.project = project

    def validate(self):
        if self.definition:
            self.definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Definition') is not None:
            temp_model = JobDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class RunJobShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        definition_shrink: str = None,
        description: str = None,
        name: str = None,
        project: str = None,
    ):
        self.client_token = client_token
        self.definition_shrink = definition_shrink
        self.description = description
        self.name = name
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.definition_shrink is not None:
            result['Definition'] = self.definition_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Definition') is not None:
            self.definition_shrink = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class RunJobResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        end_time: str = None,
        exit_code: int = None,
        host_id: str = None,
        pid: int = None,
        reason: str = None,
        request_id: str = None,
        start_time: str = None,
        state: str = None,
        worker: str = None,
    ):
        self.create_time = create_time
        self.end_time = end_time
        self.exit_code = exit_code
        self.host_id = host_id
        self.pid = pid
        self.reason = reason
        self.request_id = request_id
        self.start_time = start_time
        self.state = state
        self.worker = worker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.worker is not None:
            result['Worker'] = self.worker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Worker') is not None:
            self.worker = m.get('Worker')
        return self


class RunJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunJobResponseBody = None,
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
            temp_model = RunJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        definition: ClusterDefinition = None,
        project: str = None,
    ):
        self.cluster_id = cluster_id
        self.definition = definition
        self.project = project

    def validate(self):
        if self.definition:
            self.definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Definition') is not None:
            temp_model = ClusterDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class UpdateClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        definition_shrink: str = None,
        project: str = None,
    ):
        self.cluster_id = cluster_id
        self.definition_shrink = definition_shrink
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.definition_shrink is not None:
            result['Definition'] = self.definition_shrink
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Definition') is not None:
            self.definition_shrink = m.get('Definition')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class UpdateClusterResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateClusterResponseBody = None,
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
            temp_model = UpdateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateJobQueueRequest(TeaModel):
    def __init__(
        self,
        definition: JobQueueDefinition = None,
        name: str = None,
        project: str = None,
    ):
        self.definition = definition
        self.name = name
        self.project = project

    def validate(self):
        if self.definition:
            self.definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            temp_model = JobQueueDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class UpdateJobQueueShrinkRequest(TeaModel):
    def __init__(
        self,
        definition_shrink: str = None,
        name: str = None,
        project: str = None,
    ):
        self.definition_shrink = definition_shrink
        self.name = name
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition_shrink is not None:
            result['Definition'] = self.definition_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition_shrink = m.get('Definition')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class UpdateJobQueueResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateJobQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateJobQueueResponseBody = None,
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
            temp_model = UpdateJobQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        definition: ProjectDefinition = None,
        description: str = None,
        project: str = None,
    ):
        self.definition = definition
        self.description = description
        self.project = project

    def validate(self):
        if self.definition:
            self.definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            temp_model = ProjectDefinition()
            self.definition = temp_model.from_map(m['Definition'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class UpdateProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        definition_shrink: str = None,
        description: str = None,
        project: str = None,
    ):
        self.definition_shrink = definition_shrink
        self.description = description
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition_shrink is not None:
            result['Definition'] = self.definition_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition_shrink = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProjectResponseBody = None,
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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkerStatusRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        status: str = None,
        worker_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.status = status
        self.worker_id = worker_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.status is not None:
            result['Status'] = self.status
        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')
        return self


class UpdateWorkerStatusResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWorkerStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateWorkerStatusResponseBody = None,
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
            temp_model = UpdateWorkerStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


