# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class CreateContainerGroupRequestDnsConfigOption(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateContainerGroupRequestDnsConfig(TeaModel):
    def __init__(
        self,
        name_server: List[str] = None,
        search: List[str] = None,
        option: List[CreateContainerGroupRequestDnsConfigOption] = None,
    ):
        self.name_server = name_server
        self.search = search
        self.option = option

    def validate(self):
        if self.option:
            for k in self.option:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.name_server is not None:
            result['NameServer'] = self.name_server
        if self.search is not None:
            result['Search'] = self.search
        result['Option'] = []
        if self.option is not None:
            for k in self.option:
                result['Option'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameServer') is not None:
            self.name_server = m.get('NameServer')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        self.option = []
        if m.get('Option') is not None:
            for k in m.get('Option'):
                temp_model = CreateContainerGroupRequestDnsConfigOption()
                self.option.append(temp_model.from_map(k))
        return self


class CreateContainerGroupRequestSecurityContextSysctl(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateContainerGroupRequestSecurityContext(TeaModel):
    def __init__(
        self,
        sysctl: List[CreateContainerGroupRequestSecurityContextSysctl] = None,
    ):
        self.sysctl = sysctl

    def validate(self):
        if self.sysctl:
            for k in self.sysctl:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Sysctl'] = []
        if self.sysctl is not None:
            for k in self.sysctl:
                result['Sysctl'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sysctl = []
        if m.get('Sysctl') is not None:
            for k in m.get('Sysctl'):
                temp_model = CreateContainerGroupRequestSecurityContextSysctl()
                self.sysctl.append(temp_model.from_map(k))
        return self


class CreateContainerGroupRequestTag(TeaModel):
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


class CreateContainerGroupRequestImageRegistryCredential(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.server = server
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateContainerGroupRequestContainerReadinessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class CreateContainerGroupRequestContainerReadinessProbeHttpGet(TeaModel):
    def __init__(
        self,
        scheme: str = None,
        path: str = None,
        port: int = None,
    ):
        self.scheme = scheme
        self.path = path
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class CreateContainerGroupRequestContainerReadinessProbeExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class CreateContainerGroupRequestContainerReadinessProbe(TeaModel):
    def __init__(
        self,
        timeout_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: CreateContainerGroupRequestContainerReadinessProbeTcpSocket = None,
        http_get: CreateContainerGroupRequestContainerReadinessProbeHttpGet = None,
        period_seconds: int = None,
        initial_delay_seconds: int = None,
        exec: CreateContainerGroupRequestContainerReadinessProbeExec = None,
        failure_threshold: int = None,
    ):
        self.timeout_seconds = timeout_seconds
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
        self.http_get = http_get
        self.period_seconds = period_seconds
        self.initial_delay_seconds = initial_delay_seconds
        self.exec = exec
        self.failure_threshold = failure_threshold

    def validate(self):
        self.validate_required(self.tcp_socket, 'tcp_socket')
        if self.tcp_socket:
            self.tcp_socket.validate()
        self.validate_required(self.http_get, 'http_get')
        if self.http_get:
            self.http_get.validate()
        self.validate_required(self.exec, 'exec')
        if self.exec:
            self.exec.validate()

    def to_map(self):
        result = dict()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = CreateContainerGroupRequestContainerReadinessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('HttpGet') is not None:
            temp_model = CreateContainerGroupRequestContainerReadinessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('Exec') is not None:
            temp_model = CreateContainerGroupRequestContainerReadinessProbeExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        return self


class CreateContainerGroupRequestContainerSecurityContextCapability(TeaModel):
    def __init__(
        self,
        add: List[str] = None,
    ):
        self.add = add

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class CreateContainerGroupRequestContainerSecurityContext(TeaModel):
    def __init__(
        self,
        capability: CreateContainerGroupRequestContainerSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user

    def validate(self):
        self.validate_required(self.capability, 'capability')
        if self.capability:
            self.capability.validate()

    def to_map(self):
        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = CreateContainerGroupRequestContainerSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class CreateContainerGroupRequestContainerLivenessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class CreateContainerGroupRequestContainerLivenessProbeExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class CreateContainerGroupRequestContainerLivenessProbeHttpGet(TeaModel):
    def __init__(
        self,
        scheme: str = None,
        port: int = None,
        path: str = None,
    ):
        self.scheme = scheme
        self.port = port
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.port is not None:
            result['Port'] = self.port
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateContainerGroupRequestContainerLivenessProbe(TeaModel):
    def __init__(
        self,
        period_seconds: int = None,
        tcp_socket: CreateContainerGroupRequestContainerLivenessProbeTcpSocket = None,
        initial_delay_seconds: int = None,
        success_threshold: int = None,
        exec: CreateContainerGroupRequestContainerLivenessProbeExec = None,
        http_get: CreateContainerGroupRequestContainerLivenessProbeHttpGet = None,
        failure_threshold: int = None,
        timeout_seconds: int = None,
    ):
        self.period_seconds = period_seconds
        self.tcp_socket = tcp_socket
        self.initial_delay_seconds = initial_delay_seconds
        self.success_threshold = success_threshold
        self.exec = exec
        self.http_get = http_get
        self.failure_threshold = failure_threshold
        self.timeout_seconds = timeout_seconds

    def validate(self):
        self.validate_required(self.tcp_socket, 'tcp_socket')
        if self.tcp_socket:
            self.tcp_socket.validate()
        self.validate_required(self.exec, 'exec')
        if self.exec:
            self.exec.validate()
        self.validate_required(self.http_get, 'http_get')
        if self.http_get:
            self.http_get.validate()

    def to_map(self):
        result = dict()
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('TcpSocket') is not None:
            temp_model = CreateContainerGroupRequestContainerLivenessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('Exec') is not None:
            temp_model = CreateContainerGroupRequestContainerLivenessProbeExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('HttpGet') is not None:
            temp_model = CreateContainerGroupRequestContainerLivenessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class CreateContainerGroupRequestContainerEnvironmentVarFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class CreateContainerGroupRequestContainerEnvironmentVar(TeaModel):
    def __init__(
        self,
        field_ref: CreateContainerGroupRequestContainerEnvironmentVarFieldRef = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref = field_ref
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.field_ref, 'field_ref')
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = CreateContainerGroupRequestContainerEnvironmentVarFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateContainerGroupRequestContainerVolumeMount(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        read_only: bool = None,
        sub_path: str = None,
        name: str = None,
    ):
        self.mount_path = mount_path
        self.read_only = read_only
        self.sub_path = sub_path
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateContainerGroupRequestContainerPort(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        port: int = None,
    ):
        self.protocol = protocol
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class CreateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeader(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateContainerGroupRequestContainer(TeaModel):
    def __init__(
        self,
        readiness_probe: CreateContainerGroupRequestContainerReadinessProbe = None,
        security_context: CreateContainerGroupRequestContainerSecurityContext = None,
        liveness_probe: CreateContainerGroupRequestContainerLivenessProbe = None,
        environment_var: List[CreateContainerGroupRequestContainerEnvironmentVar] = None,
        tty: bool = None,
        working_dir: str = None,
        arg: List[str] = None,
        stdin: bool = None,
        volume_mount: List[CreateContainerGroupRequestContainerVolumeMount] = None,
        image_pull_policy: str = None,
        stdin_once: bool = None,
        lifecycle_pre_stop_handler_tcp_socket_port: int = None,
        lifecycle_post_start_handler_http_get_scheme: str = None,
        command: List[str] = None,
        lifecycle_post_start_handler_http_get_host: str = None,
        termination_message_policy: str = None,
        lifecycle_post_start_handler_tcp_socket_port: int = None,
        lifecycle_post_start_handler_http_get_path: str = None,
        lifecycle_post_start_handler_exec: List[str] = None,
        lifecycle_pre_stop_handler_http_get_path: str = None,
        port: List[CreateContainerGroupRequestContainerPort] = None,
        termination_message_path: str = None,
        lifecycle_pre_stop_handler_http_get_scheme: str = None,
        lifecycle_post_start_handler_tcp_socket_host: str = None,
        gpu: int = None,
        lifecycle_pre_stop_handler_exec: List[str] = None,
        memory: float = None,
        name: str = None,
        lifecycle_pre_stop_handler_http_get_host: str = None,
        lifecycle_pre_stop_handler_tcp_socket_host: str = None,
        image: str = None,
        lifecycle_pre_stop_handler_http_get_port: int = None,
        lifecycle_pre_stop_handler_http_get_http_header: List[CreateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader] = None,
        cpu: float = None,
        lifecycle_post_start_handler_http_get_port: int = None,
        lifecycle_post_start_handler_http_get_http_header: List[CreateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeader] = None,
    ):
        self.readiness_probe = readiness_probe
        self.security_context = security_context
        self.liveness_probe = liveness_probe
        self.environment_var = environment_var
        self.tty = tty
        self.working_dir = working_dir
        self.arg = arg
        self.stdin = stdin
        self.volume_mount = volume_mount
        self.image_pull_policy = image_pull_policy
        self.stdin_once = stdin_once
        self.lifecycle_pre_stop_handler_tcp_socket_port = lifecycle_pre_stop_handler_tcp_socket_port
        self.lifecycle_post_start_handler_http_get_scheme = lifecycle_post_start_handler_http_get_scheme
        self.command = command
        self.lifecycle_post_start_handler_http_get_host = lifecycle_post_start_handler_http_get_host
        self.termination_message_policy = termination_message_policy
        self.lifecycle_post_start_handler_tcp_socket_port = lifecycle_post_start_handler_tcp_socket_port
        self.lifecycle_post_start_handler_http_get_path = lifecycle_post_start_handler_http_get_path
        self.lifecycle_post_start_handler_exec = lifecycle_post_start_handler_exec
        self.lifecycle_pre_stop_handler_http_get_path = lifecycle_pre_stop_handler_http_get_path
        self.port = port
        self.termination_message_path = termination_message_path
        self.lifecycle_pre_stop_handler_http_get_scheme = lifecycle_pre_stop_handler_http_get_scheme
        self.lifecycle_post_start_handler_tcp_socket_host = lifecycle_post_start_handler_tcp_socket_host
        self.gpu = gpu
        self.lifecycle_pre_stop_handler_exec = lifecycle_pre_stop_handler_exec
        self.memory = memory
        self.name = name
        self.lifecycle_pre_stop_handler_http_get_host = lifecycle_pre_stop_handler_http_get_host
        self.lifecycle_pre_stop_handler_tcp_socket_host = lifecycle_pre_stop_handler_tcp_socket_host
        self.image = image
        self.lifecycle_pre_stop_handler_http_get_port = lifecycle_pre_stop_handler_http_get_port
        self.lifecycle_pre_stop_handler_http_get_http_header = lifecycle_pre_stop_handler_http_get_http_header
        self.cpu = cpu
        self.lifecycle_post_start_handler_http_get_port = lifecycle_post_start_handler_http_get_port
        self.lifecycle_post_start_handler_http_get_http_header = lifecycle_post_start_handler_http_get_http_header

    def validate(self):
        self.validate_required(self.readiness_probe, 'readiness_probe')
        if self.readiness_probe:
            self.readiness_probe.validate()
        self.validate_required(self.security_context, 'security_context')
        if self.security_context:
            self.security_context.validate()
        self.validate_required(self.liveness_probe, 'liveness_probe')
        if self.liveness_probe:
            self.liveness_probe.validate()
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()
        if self.port:
            for k in self.port:
                if k:
                    k.validate()
        if self.lifecycle_pre_stop_handler_http_get_http_header:
            for k in self.lifecycle_pre_stop_handler_http_get_http_header:
                if k:
                    k.validate()
        if self.lifecycle_post_start_handler_http_get_http_header:
            for k in self.lifecycle_post_start_handler_http_get_http_header:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.readiness_probe is not None:
            result['ReadinessProbe'] = self.readiness_probe.to_map()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.tty is not None:
            result['Tty'] = self.tty
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.lifecycle_pre_stop_handler_tcp_socket_port is not None:
            result['LifecyclePreStopHandlerTcpSocketPort'] = self.lifecycle_pre_stop_handler_tcp_socket_port
        if self.lifecycle_post_start_handler_http_get_scheme is not None:
            result['LifecyclePostStartHandlerHttpGetScheme'] = self.lifecycle_post_start_handler_http_get_scheme
        if self.command is not None:
            result['Command'] = self.command
        if self.lifecycle_post_start_handler_http_get_host is not None:
            result['LifecyclePostStartHandlerHttpGetHost'] = self.lifecycle_post_start_handler_http_get_host
        if self.termination_message_policy is not None:
            result['TerminationMessagePolicy'] = self.termination_message_policy
        if self.lifecycle_post_start_handler_tcp_socket_port is not None:
            result['LifecyclePostStartHandlerTcpSocketPort'] = self.lifecycle_post_start_handler_tcp_socket_port
        if self.lifecycle_post_start_handler_http_get_path is not None:
            result['LifecyclePostStartHandlerHttpGetPath'] = self.lifecycle_post_start_handler_http_get_path
        if self.lifecycle_post_start_handler_exec is not None:
            result['LifecyclePostStartHandlerExec'] = self.lifecycle_post_start_handler_exec
        if self.lifecycle_pre_stop_handler_http_get_path is not None:
            result['LifecyclePreStopHandlerHttpGetPath'] = self.lifecycle_pre_stop_handler_http_get_path
        result['Port'] = []
        if self.port is not None:
            for k in self.port:
                result['Port'].append(k.to_map() if k else None)
        if self.termination_message_path is not None:
            result['TerminationMessagePath'] = self.termination_message_path
        if self.lifecycle_pre_stop_handler_http_get_scheme is not None:
            result['LifecyclePreStopHandlerHttpGetScheme'] = self.lifecycle_pre_stop_handler_http_get_scheme
        if self.lifecycle_post_start_handler_tcp_socket_host is not None:
            result['LifecyclePostStartHandlerTcpSocketHost'] = self.lifecycle_post_start_handler_tcp_socket_host
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.lifecycle_pre_stop_handler_exec is not None:
            result['LifecyclePreStopHandlerExec'] = self.lifecycle_pre_stop_handler_exec
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        if self.lifecycle_pre_stop_handler_http_get_host is not None:
            result['LifecyclePreStopHandlerHttpGetHost'] = self.lifecycle_pre_stop_handler_http_get_host
        if self.lifecycle_pre_stop_handler_tcp_socket_host is not None:
            result['LifecyclePreStopHandlerTcpSocketHost'] = self.lifecycle_pre_stop_handler_tcp_socket_host
        if self.image is not None:
            result['Image'] = self.image
        if self.lifecycle_pre_stop_handler_http_get_port is not None:
            result['LifecyclePreStopHandlerHttpGetPort'] = self.lifecycle_pre_stop_handler_http_get_port
        result['LifecyclePreStopHandlerHttpGetHttpHeader'] = []
        if self.lifecycle_pre_stop_handler_http_get_http_header is not None:
            for k in self.lifecycle_pre_stop_handler_http_get_http_header:
                result['LifecyclePreStopHandlerHttpGetHttpHeader'].append(k.to_map() if k else None)
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.lifecycle_post_start_handler_http_get_port is not None:
            result['LifecyclePostStartHandlerHttpGetPort'] = self.lifecycle_post_start_handler_http_get_port
        result['LifecyclePostStartHandlerHttpGetHttpHeader'] = []
        if self.lifecycle_post_start_handler_http_get_http_header is not None:
            for k in self.lifecycle_post_start_handler_http_get_http_header:
                result['LifecyclePostStartHandlerHttpGetHttpHeader'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReadinessProbe') is not None:
            temp_model = CreateContainerGroupRequestContainerReadinessProbe()
            self.readiness_probe = temp_model.from_map(m['ReadinessProbe'])
        if m.get('SecurityContext') is not None:
            temp_model = CreateContainerGroupRequestContainerSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('LivenessProbe') is not None:
            temp_model = CreateContainerGroupRequestContainerLivenessProbe()
            self.liveness_probe = temp_model.from_map(m['LivenessProbe'])
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = CreateContainerGroupRequestContainerEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = CreateContainerGroupRequestContainerVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('LifecyclePreStopHandlerTcpSocketPort') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_port = m.get('LifecyclePreStopHandlerTcpSocketPort')
        if m.get('LifecyclePostStartHandlerHttpGetScheme') is not None:
            self.lifecycle_post_start_handler_http_get_scheme = m.get('LifecyclePostStartHandlerHttpGetScheme')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('LifecyclePostStartHandlerHttpGetHost') is not None:
            self.lifecycle_post_start_handler_http_get_host = m.get('LifecyclePostStartHandlerHttpGetHost')
        if m.get('TerminationMessagePolicy') is not None:
            self.termination_message_policy = m.get('TerminationMessagePolicy')
        if m.get('LifecyclePostStartHandlerTcpSocketPort') is not None:
            self.lifecycle_post_start_handler_tcp_socket_port = m.get('LifecyclePostStartHandlerTcpSocketPort')
        if m.get('LifecyclePostStartHandlerHttpGetPath') is not None:
            self.lifecycle_post_start_handler_http_get_path = m.get('LifecyclePostStartHandlerHttpGetPath')
        if m.get('LifecyclePostStartHandlerExec') is not None:
            self.lifecycle_post_start_handler_exec = m.get('LifecyclePostStartHandlerExec')
        if m.get('LifecyclePreStopHandlerHttpGetPath') is not None:
            self.lifecycle_pre_stop_handler_http_get_path = m.get('LifecyclePreStopHandlerHttpGetPath')
        self.port = []
        if m.get('Port') is not None:
            for k in m.get('Port'):
                temp_model = CreateContainerGroupRequestContainerPort()
                self.port.append(temp_model.from_map(k))
        if m.get('TerminationMessagePath') is not None:
            self.termination_message_path = m.get('TerminationMessagePath')
        if m.get('LifecyclePreStopHandlerHttpGetScheme') is not None:
            self.lifecycle_pre_stop_handler_http_get_scheme = m.get('LifecyclePreStopHandlerHttpGetScheme')
        if m.get('LifecyclePostStartHandlerTcpSocketHost') is not None:
            self.lifecycle_post_start_handler_tcp_socket_host = m.get('LifecyclePostStartHandlerTcpSocketHost')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('LifecyclePreStopHandlerExec') is not None:
            self.lifecycle_pre_stop_handler_exec = m.get('LifecyclePreStopHandlerExec')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LifecyclePreStopHandlerHttpGetHost') is not None:
            self.lifecycle_pre_stop_handler_http_get_host = m.get('LifecyclePreStopHandlerHttpGetHost')
        if m.get('LifecyclePreStopHandlerTcpSocketHost') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_host = m.get('LifecyclePreStopHandlerTcpSocketHost')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('LifecyclePreStopHandlerHttpGetPort') is not None:
            self.lifecycle_pre_stop_handler_http_get_port = m.get('LifecyclePreStopHandlerHttpGetPort')
        self.lifecycle_pre_stop_handler_http_get_http_header = []
        if m.get('LifecyclePreStopHandlerHttpGetHttpHeader') is not None:
            for k in m.get('LifecyclePreStopHandlerHttpGetHttpHeader'):
                temp_model = CreateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader()
                self.lifecycle_pre_stop_handler_http_get_http_header.append(temp_model.from_map(k))
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('LifecyclePostStartHandlerHttpGetPort') is not None:
            self.lifecycle_post_start_handler_http_get_port = m.get('LifecyclePostStartHandlerHttpGetPort')
        self.lifecycle_post_start_handler_http_get_http_header = []
        if m.get('LifecyclePostStartHandlerHttpGetHttpHeader') is not None:
            for k in m.get('LifecyclePostStartHandlerHttpGetHttpHeader'):
                temp_model = CreateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeader()
                self.lifecycle_post_start_handler_http_get_http_header.append(temp_model.from_map(k))
        return self


class CreateContainerGroupRequestVolumeDiskVolume(TeaModel):
    def __init__(
        self,
        disk_size: int = None,
        fs_type: str = None,
        disk_id: str = None,
    ):
        self.disk_size = disk_size
        self.fs_type = fs_type
        self.disk_id = disk_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.fs_type is not None:
            result['FsType'] = self.fs_type
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        return self


class CreateContainerGroupRequestVolumeNFSVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        read_only: bool = None,
        server: str = None,
    ):
        self.path = path
        self.read_only = read_only
        self.server = server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.server is not None:
            result['Server'] = self.server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        return self


class CreateContainerGroupRequestVolumeFlexVolume(TeaModel):
    def __init__(
        self,
        fs_type: str = None,
        options: str = None,
        driver: str = None,
    ):
        self.fs_type = fs_type
        self.options = options
        self.driver = driver

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.fs_type is not None:
            result['FsType'] = self.fs_type
        if self.options is not None:
            result['Options'] = self.options
        if self.driver is not None:
            result['Driver'] = self.driver
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        return self


class CreateContainerGroupRequestVolumeHostPathVolume(TeaModel):
    def __init__(
        self,
        type: str = None,
        path: str = None,
    ):
        self.type = type
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath(TeaModel):
    def __init__(
        self,
        path: str = None,
        mode: int = None,
        content: str = None,
    ):
        self.path = path
        self.mode = mode
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class CreateContainerGroupRequestVolumeConfigFileVolume(TeaModel):
    def __init__(
        self,
        default_mode: int = None,
        config_file_to_path: List[CreateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath] = None,
    ):
        self.default_mode = default_mode
        self.config_file_to_path = config_file_to_path

    def validate(self):
        if self.config_file_to_path:
            for k in self.config_file_to_path:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.default_mode is not None:
            result['DefaultMode'] = self.default_mode
        result['ConfigFileToPath'] = []
        if self.config_file_to_path is not None:
            for k in self.config_file_to_path:
                result['ConfigFileToPath'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultMode') is not None:
            self.default_mode = m.get('DefaultMode')
        self.config_file_to_path = []
        if m.get('ConfigFileToPath') is not None:
            for k in m.get('ConfigFileToPath'):
                temp_model = CreateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath()
                self.config_file_to_path.append(temp_model.from_map(k))
        return self


class CreateContainerGroupRequestVolumeEmptyDirVolume(TeaModel):
    def __init__(
        self,
        medium: str = None,
    ):
        self.medium = medium

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.medium is not None:
            result['Medium'] = self.medium
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        return self


class CreateContainerGroupRequestVolume(TeaModel):
    def __init__(
        self,
        disk_volume: CreateContainerGroupRequestVolumeDiskVolume = None,
        nfsvolume: CreateContainerGroupRequestVolumeNFSVolume = None,
        flex_volume: CreateContainerGroupRequestVolumeFlexVolume = None,
        host_path_volume: CreateContainerGroupRequestVolumeHostPathVolume = None,
        config_file_volume: CreateContainerGroupRequestVolumeConfigFileVolume = None,
        empty_dir_volume: CreateContainerGroupRequestVolumeEmptyDirVolume = None,
        type: str = None,
        name: str = None,
    ):
        self.disk_volume = disk_volume
        self.nfsvolume = nfsvolume
        self.flex_volume = flex_volume
        self.host_path_volume = host_path_volume
        self.config_file_volume = config_file_volume
        self.empty_dir_volume = empty_dir_volume
        self.type = type
        self.name = name

    def validate(self):
        self.validate_required(self.disk_volume, 'disk_volume')
        if self.disk_volume:
            self.disk_volume.validate()
        self.validate_required(self.nfsvolume, 'nfsvolume')
        if self.nfsvolume:
            self.nfsvolume.validate()
        self.validate_required(self.flex_volume, 'flex_volume')
        if self.flex_volume:
            self.flex_volume.validate()
        self.validate_required(self.host_path_volume, 'host_path_volume')
        if self.host_path_volume:
            self.host_path_volume.validate()
        self.validate_required(self.config_file_volume, 'config_file_volume')
        if self.config_file_volume:
            self.config_file_volume.validate()
        self.validate_required(self.empty_dir_volume, 'empty_dir_volume')
        if self.empty_dir_volume:
            self.empty_dir_volume.validate()

    def to_map(self):
        result = dict()
        if self.disk_volume is not None:
            result['DiskVolume'] = self.disk_volume.to_map()
        if self.nfsvolume is not None:
            result['NFSVolume'] = self.nfsvolume.to_map()
        if self.flex_volume is not None:
            result['FlexVolume'] = self.flex_volume.to_map()
        if self.host_path_volume is not None:
            result['HostPathVolume'] = self.host_path_volume.to_map()
        if self.config_file_volume is not None:
            result['ConfigFileVolume'] = self.config_file_volume.to_map()
        if self.empty_dir_volume is not None:
            result['EmptyDirVolume'] = self.empty_dir_volume.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeDiskVolume()
            self.disk_volume = temp_model.from_map(m['DiskVolume'])
        if m.get('NFSVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeNFSVolume()
            self.nfsvolume = temp_model.from_map(m['NFSVolume'])
        if m.get('FlexVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeFlexVolume()
            self.flex_volume = temp_model.from_map(m['FlexVolume'])
        if m.get('HostPathVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeHostPathVolume()
            self.host_path_volume = temp_model.from_map(m['HostPathVolume'])
        if m.get('ConfigFileVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeConfigFileVolume()
            self.config_file_volume = temp_model.from_map(m['ConfigFileVolume'])
        if m.get('EmptyDirVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeEmptyDirVolume()
            self.empty_dir_volume = temp_model.from_map(m['EmptyDirVolume'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateContainerGroupRequestInitContainerSecurityContextCapability(TeaModel):
    def __init__(
        self,
        add: List[str] = None,
    ):
        self.add = add

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class CreateContainerGroupRequestInitContainerSecurityContext(TeaModel):
    def __init__(
        self,
        capability: CreateContainerGroupRequestInitContainerSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user

    def validate(self):
        self.validate_required(self.capability, 'capability')
        if self.capability:
            self.capability.validate()

    def to_map(self):
        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = CreateContainerGroupRequestInitContainerSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class CreateContainerGroupRequestInitContainerVolumeMount(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        read_only: bool = None,
        sub_path: str = None,
        name: str = None,
    ):
        self.mount_path = mount_path
        self.read_only = read_only
        self.sub_path = sub_path
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateContainerGroupRequestInitContainerPort(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        port: int = None,
    ):
        self.protocol = protocol
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class CreateContainerGroupRequestInitContainerEnvironmentVarFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class CreateContainerGroupRequestInitContainerEnvironmentVar(TeaModel):
    def __init__(
        self,
        field_ref: CreateContainerGroupRequestInitContainerEnvironmentVarFieldRef = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref = field_ref
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.field_ref, 'field_ref')
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = CreateContainerGroupRequestInitContainerEnvironmentVarFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateContainerGroupRequestInitContainer(TeaModel):
    def __init__(
        self,
        security_context: CreateContainerGroupRequestInitContainerSecurityContext = None,
        image: str = None,
        volume_mount: List[CreateContainerGroupRequestInitContainerVolumeMount] = None,
        port: List[CreateContainerGroupRequestInitContainerPort] = None,
        termination_message_path: str = None,
        environment_var: List[CreateContainerGroupRequestInitContainerEnvironmentVar] = None,
        image_pull_policy: str = None,
        working_dir: str = None,
        cpu: float = None,
        arg: List[str] = None,
        command: List[str] = None,
        gpu: int = None,
        memory: float = None,
        termination_message_policy: str = None,
        name: str = None,
    ):
        self.security_context = security_context
        self.image = image
        self.volume_mount = volume_mount
        self.port = port
        self.termination_message_path = termination_message_path
        self.environment_var = environment_var
        self.image_pull_policy = image_pull_policy
        self.working_dir = working_dir
        self.cpu = cpu
        self.arg = arg
        self.command = command
        self.gpu = gpu
        self.memory = memory
        self.termination_message_policy = termination_message_policy
        self.name = name

    def validate(self):
        self.validate_required(self.security_context, 'security_context')
        if self.security_context:
            self.security_context.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()
        if self.port:
            for k in self.port:
                if k:
                    k.validate()
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.image is not None:
            result['Image'] = self.image
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        result['Port'] = []
        if self.port is not None:
            for k in self.port:
                result['Port'].append(k.to_map() if k else None)
        if self.termination_message_path is not None:
            result['TerminationMessagePath'] = self.termination_message_path
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.command is not None:
            result['Command'] = self.command
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.termination_message_policy is not None:
            result['TerminationMessagePolicy'] = self.termination_message_policy
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityContext') is not None:
            temp_model = CreateContainerGroupRequestInitContainerSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Image') is not None:
            self.image = m.get('Image')
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = CreateContainerGroupRequestInitContainerVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        self.port = []
        if m.get('Port') is not None:
            for k in m.get('Port'):
                temp_model = CreateContainerGroupRequestInitContainerPort()
                self.port.append(temp_model.from_map(k))
        if m.get('TerminationMessagePath') is not None:
            self.termination_message_path = m.get('TerminationMessagePath')
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = CreateContainerGroupRequestInitContainerEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('TerminationMessagePolicy') is not None:
            self.termination_message_policy = m.get('TerminationMessagePolicy')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateContainerGroupRequestHostAliase(TeaModel):
    def __init__(
        self,
        ip: str = None,
        hostname: List[str] = None,
    ):
        self.ip = ip
        self.hostname = hostname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        return self


class CreateContainerGroupRequestArn(TeaModel):
    def __init__(
        self,
        role_arn: str = None,
        role_type: str = None,
        assume_role_for: str = None,
    ):
        self.role_arn = role_arn
        self.role_type = role_type
        self.assume_role_for = assume_role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')
        return self


class CreateContainerGroupRequestAcrRegistryInfo(TeaModel):
    def __init__(
        self,
        domain: List[str] = None,
        instance_name: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.domain = domain
        self.instance_name = instance_name
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateContainerGroupRequest(TeaModel):
    def __init__(
        self,
        dns_config: CreateContainerGroupRequestDnsConfig = None,
        security_context: CreateContainerGroupRequestSecurityContext = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        zone_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        container_group_name: str = None,
        restart_policy: str = None,
        eip_instance_id: str = None,
        cpu: float = None,
        memory: float = None,
        resource_group_id: str = None,
        dns_policy: str = None,
        client_token: str = None,
        instance_type: str = None,
        sls_enable: bool = None,
        image_snapshot_id: str = None,
        ram_role_name: str = None,
        termination_grace_period_seconds: int = None,
        auto_match_image_cache: bool = None,
        vk_client_version: str = None,
        ipv_6address_count: int = None,
        active_deadline_seconds: int = None,
        spot_strategy: str = None,
        spot_price_limit: float = None,
        schedule_strategy: str = None,
        tenant_vswitch_id: str = None,
        tenant_security_group_id: str = None,
        core_pattern: str = None,
        share_process_namespace: bool = None,
        product_on_eci_mode: str = None,
        secondary_enipolicy: str = None,
        auto_create_eip: bool = None,
        eip_bandwidth: int = None,
        eip_isp: str = None,
        eip_common_bandwidth_package: str = None,
        host_name: str = None,
        ingress_bandwidth: int = None,
        egress_bandwidth: int = None,
        tag: List[CreateContainerGroupRequestTag] = None,
        image_registry_credential: List[CreateContainerGroupRequestImageRegistryCredential] = None,
        container: List[CreateContainerGroupRequestContainer] = None,
        volume: List[CreateContainerGroupRequestVolume] = None,
        init_container: List[CreateContainerGroupRequestInitContainer] = None,
        host_aliase: List[CreateContainerGroupRequestHostAliase] = None,
        arn: List[CreateContainerGroupRequestArn] = None,
        ntp_server: List[str] = None,
        acr_registry_info: List[CreateContainerGroupRequestAcrRegistryInfo] = None,
    ):
        self.dns_config = dns_config
        self.security_context = security_context
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.zone_id = zone_id
        self.security_group_id = security_group_id
        self.v_switch_id = v_switch_id
        self.container_group_name = container_group_name
        self.restart_policy = restart_policy
        self.eip_instance_id = eip_instance_id
        self.cpu = cpu
        self.memory = memory
        self.resource_group_id = resource_group_id
        self.dns_policy = dns_policy
        self.client_token = client_token
        self.instance_type = instance_type
        self.sls_enable = sls_enable
        self.image_snapshot_id = image_snapshot_id
        self.ram_role_name = ram_role_name
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.auto_match_image_cache = auto_match_image_cache
        self.vk_client_version = vk_client_version
        self.ipv_6address_count = ipv_6address_count
        self.active_deadline_seconds = active_deadline_seconds
        self.spot_strategy = spot_strategy
        self.spot_price_limit = spot_price_limit
        self.schedule_strategy = schedule_strategy
        self.tenant_vswitch_id = tenant_vswitch_id
        self.tenant_security_group_id = tenant_security_group_id
        self.core_pattern = core_pattern
        self.share_process_namespace = share_process_namespace
        self.product_on_eci_mode = product_on_eci_mode
        self.secondary_enipolicy = secondary_enipolicy
        self.auto_create_eip = auto_create_eip
        self.eip_bandwidth = eip_bandwidth
        self.eip_isp = eip_isp
        self.eip_common_bandwidth_package = eip_common_bandwidth_package
        self.host_name = host_name
        self.ingress_bandwidth = ingress_bandwidth
        self.egress_bandwidth = egress_bandwidth
        self.tag = tag
        self.image_registry_credential = image_registry_credential
        self.container = container
        self.volume = volume
        self.init_container = init_container
        self.host_aliase = host_aliase
        self.arn = arn
        self.ntp_server = ntp_server
        self.acr_registry_info = acr_registry_info

    def validate(self):
        if self.dns_config:
            self.dns_config.validate()
        if self.security_context:
            self.security_context.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.image_registry_credential:
            for k in self.image_registry_credential:
                if k:
                    k.validate()
        if self.container:
            for k in self.container:
                if k:
                    k.validate()
        if self.volume:
            for k in self.volume:
                if k:
                    k.validate()
        if self.init_container:
            for k in self.init_container:
                if k:
                    k.validate()
        if self.host_aliase:
            for k in self.host_aliase:
                if k:
                    k.validate()
        if self.arn:
            for k in self.arn:
                if k:
                    k.validate()
        if self.acr_registry_info:
            for k in self.acr_registry_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.dns_config is not None:
            result['DnsConfig'] = self.dns_config.to_map()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name
        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.dns_policy is not None:
            result['DnsPolicy'] = self.dns_policy
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.sls_enable is not None:
            result['SlsEnable'] = self.sls_enable
        if self.image_snapshot_id is not None:
            result['ImageSnapshotId'] = self.image_snapshot_id
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.auto_match_image_cache is not None:
            result['AutoMatchImageCache'] = self.auto_match_image_cache
        if self.vk_client_version is not None:
            result['VkClientVersion'] = self.vk_client_version
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.active_deadline_seconds is not None:
            result['ActiveDeadlineSeconds'] = self.active_deadline_seconds
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.schedule_strategy is not None:
            result['ScheduleStrategy'] = self.schedule_strategy
        if self.tenant_vswitch_id is not None:
            result['TenantVSwitchId'] = self.tenant_vswitch_id
        if self.tenant_security_group_id is not None:
            result['TenantSecurityGroupId'] = self.tenant_security_group_id
        if self.core_pattern is not None:
            result['CorePattern'] = self.core_pattern
        if self.share_process_namespace is not None:
            result['ShareProcessNamespace'] = self.share_process_namespace
        if self.product_on_eci_mode is not None:
            result['ProductOnEciMode'] = self.product_on_eci_mode
        if self.secondary_enipolicy is not None:
            result['SecondaryENIPolicy'] = self.secondary_enipolicy
        if self.auto_create_eip is not None:
            result['AutoCreateEip'] = self.auto_create_eip
        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth
        if self.eip_isp is not None:
            result['EipISP'] = self.eip_isp
        if self.eip_common_bandwidth_package is not None:
            result['EipCommonBandwidthPackage'] = self.eip_common_bandwidth_package
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ingress_bandwidth is not None:
            result['IngressBandwidth'] = self.ingress_bandwidth
        if self.egress_bandwidth is not None:
            result['EgressBandwidth'] = self.egress_bandwidth
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        result['ImageRegistryCredential'] = []
        if self.image_registry_credential is not None:
            for k in self.image_registry_credential:
                result['ImageRegistryCredential'].append(k.to_map() if k else None)
        result['Container'] = []
        if self.container is not None:
            for k in self.container:
                result['Container'].append(k.to_map() if k else None)
        result['Volume'] = []
        if self.volume is not None:
            for k in self.volume:
                result['Volume'].append(k.to_map() if k else None)
        result['InitContainer'] = []
        if self.init_container is not None:
            for k in self.init_container:
                result['InitContainer'].append(k.to_map() if k else None)
        result['HostAliase'] = []
        if self.host_aliase is not None:
            for k in self.host_aliase:
                result['HostAliase'].append(k.to_map() if k else None)
        result['Arn'] = []
        if self.arn is not None:
            for k in self.arn:
                result['Arn'].append(k.to_map() if k else None)
        if self.ntp_server is not None:
            result['NtpServer'] = self.ntp_server
        result['AcrRegistryInfo'] = []
        if self.acr_registry_info is not None:
            for k in self.acr_registry_info:
                result['AcrRegistryInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsConfig') is not None:
            temp_model = CreateContainerGroupRequestDnsConfig()
            self.dns_config = temp_model.from_map(m['DnsConfig'])
        if m.get('SecurityContext') is not None:
            temp_model = CreateContainerGroupRequestSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')
        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('DnsPolicy') is not None:
            self.dns_policy = m.get('DnsPolicy')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SlsEnable') is not None:
            self.sls_enable = m.get('SlsEnable')
        if m.get('ImageSnapshotId') is not None:
            self.image_snapshot_id = m.get('ImageSnapshotId')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('AutoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('AutoMatchImageCache')
        if m.get('VkClientVersion') is not None:
            self.vk_client_version = m.get('VkClientVersion')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('ActiveDeadlineSeconds') is not None:
            self.active_deadline_seconds = m.get('ActiveDeadlineSeconds')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('ScheduleStrategy') is not None:
            self.schedule_strategy = m.get('ScheduleStrategy')
        if m.get('TenantVSwitchId') is not None:
            self.tenant_vswitch_id = m.get('TenantVSwitchId')
        if m.get('TenantSecurityGroupId') is not None:
            self.tenant_security_group_id = m.get('TenantSecurityGroupId')
        if m.get('CorePattern') is not None:
            self.core_pattern = m.get('CorePattern')
        if m.get('ShareProcessNamespace') is not None:
            self.share_process_namespace = m.get('ShareProcessNamespace')
        if m.get('ProductOnEciMode') is not None:
            self.product_on_eci_mode = m.get('ProductOnEciMode')
        if m.get('SecondaryENIPolicy') is not None:
            self.secondary_enipolicy = m.get('SecondaryENIPolicy')
        if m.get('AutoCreateEip') is not None:
            self.auto_create_eip = m.get('AutoCreateEip')
        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')
        if m.get('EipISP') is not None:
            self.eip_isp = m.get('EipISP')
        if m.get('EipCommonBandwidthPackage') is not None:
            self.eip_common_bandwidth_package = m.get('EipCommonBandwidthPackage')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('IngressBandwidth') is not None:
            self.ingress_bandwidth = m.get('IngressBandwidth')
        if m.get('EgressBandwidth') is not None:
            self.egress_bandwidth = m.get('EgressBandwidth')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateContainerGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        self.image_registry_credential = []
        if m.get('ImageRegistryCredential') is not None:
            for k in m.get('ImageRegistryCredential'):
                temp_model = CreateContainerGroupRequestImageRegistryCredential()
                self.image_registry_credential.append(temp_model.from_map(k))
        self.container = []
        if m.get('Container') is not None:
            for k in m.get('Container'):
                temp_model = CreateContainerGroupRequestContainer()
                self.container.append(temp_model.from_map(k))
        self.volume = []
        if m.get('Volume') is not None:
            for k in m.get('Volume'):
                temp_model = CreateContainerGroupRequestVolume()
                self.volume.append(temp_model.from_map(k))
        self.init_container = []
        if m.get('InitContainer') is not None:
            for k in m.get('InitContainer'):
                temp_model = CreateContainerGroupRequestInitContainer()
                self.init_container.append(temp_model.from_map(k))
        self.host_aliase = []
        if m.get('HostAliase') is not None:
            for k in m.get('HostAliase'):
                temp_model = CreateContainerGroupRequestHostAliase()
                self.host_aliase.append(temp_model.from_map(k))
        self.arn = []
        if m.get('Arn') is not None:
            for k in m.get('Arn'):
                temp_model = CreateContainerGroupRequestArn()
                self.arn.append(temp_model.from_map(k))
        if m.get('NtpServer') is not None:
            self.ntp_server = m.get('NtpServer')
        self.acr_registry_info = []
        if m.get('AcrRegistryInfo') is not None:
            for k in m.get('AcrRegistryInfo'):
                temp_model = CreateContainerGroupRequestAcrRegistryInfo()
                self.acr_registry_info.append(temp_model.from_map(k))
        return self


class CreateContainerGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        container_group_id: str = None,
    ):
        self.request_id = request_id
        self.container_group_id = container_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        return self


class CreateContainerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateContainerGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateContainerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageCacheRequestImageRegistryCredential(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.server = server
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateImageCacheRequestTag(TeaModel):
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


class CreateImageCacheRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        zone_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        image_cache_name: str = None,
        eip_instance_id: str = None,
        resource_group_id: str = None,
        client_token: str = None,
        image_cache_size: int = None,
        vk_client_version: str = None,
        retention_days: int = None,
        auto_match_image_cache: bool = None,
        image_registry_credential: List[CreateImageCacheRequestImageRegistryCredential] = None,
        image: List[str] = None,
        tag: List[CreateImageCacheRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.zone_id = zone_id
        self.security_group_id = security_group_id
        self.v_switch_id = v_switch_id
        self.image_cache_name = image_cache_name
        self.eip_instance_id = eip_instance_id
        self.resource_group_id = resource_group_id
        self.client_token = client_token
        self.image_cache_size = image_cache_size
        self.vk_client_version = vk_client_version
        self.retention_days = retention_days
        self.auto_match_image_cache = auto_match_image_cache
        self.image_registry_credential = image_registry_credential
        self.image = image
        self.tag = tag

    def validate(self):
        if self.image_registry_credential:
            for k in self.image_registry_credential:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.image_cache_size is not None:
            result['ImageCacheSize'] = self.image_cache_size
        if self.vk_client_version is not None:
            result['VkClientVersion'] = self.vk_client_version
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.auto_match_image_cache is not None:
            result['AutoMatchImageCache'] = self.auto_match_image_cache
        result['ImageRegistryCredential'] = []
        if self.image_registry_credential is not None:
            for k in self.image_registry_credential:
                result['ImageRegistryCredential'].append(k.to_map() if k else None)
        if self.image is not None:
            result['Image'] = self.image
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ImageCacheSize') is not None:
            self.image_cache_size = m.get('ImageCacheSize')
        if m.get('VkClientVersion') is not None:
            self.vk_client_version = m.get('VkClientVersion')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('AutoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('AutoMatchImageCache')
        self.image_registry_credential = []
        if m.get('ImageRegistryCredential') is not None:
            for k in m.get('ImageRegistryCredential'):
                temp_model = CreateImageCacheRequestImageRegistryCredential()
                self.image_registry_credential.append(temp_model.from_map(k))
        if m.get('Image') is not None:
            self.image = m.get('Image')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateImageCacheRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateImageCacheResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        image_cache_id: str = None,
        container_group_id: str = None,
    ):
        self.request_id = request_id
        self.image_cache_id = image_cache_id
        self.container_group_id = container_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        return self


class CreateImageCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateImageCacheResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateImageCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteContainerGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        container_group_id: str = None,
        client_token: str = None,
        vk_client_version: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.container_group_id = container_group_id
        self.client_token = client_token
        self.vk_client_version = vk_client_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.vk_client_version is not None:
            result['VkClientVersion'] = self.vk_client_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('VkClientVersion') is not None:
            self.vk_client_version = m.get('VkClientVersion')
        return self


class DeleteContainerGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteContainerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteContainerGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteContainerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageCacheRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        image_cache_id: str = None,
        client_token: str = None,
        vk_client_version: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.image_cache_id = image_cache_id
        self.client_token = client_token
        self.vk_client_version = vk_client_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.vk_client_version is not None:
            result['VkClientVersion'] = self.vk_client_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('VkClientVersion') is not None:
            self.vk_client_version = m.get('VkClientVersion')
        return self


class DeleteImageCacheResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImageCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteImageCacheResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteImageCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupMetricRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        container_group_id: str = None,
        start_time: str = None,
        end_time: str = None,
        period: str = None,
        vk_client_version: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.container_group_id = container_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.period = period
        self.vk_client_version = vk_client_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.period is not None:
            result['Period'] = self.period
        if self.vk_client_version is not None:
            result['VkClientVersion'] = self.vk_client_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('VkClientVersion') is not None:
            self.vk_client_version = m.get('VkClientVersion')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsNetworkInterfaces(TeaModel):
    def __init__(
        self,
        rx_errors: int = None,
        tx_bytes: int = None,
        name: str = None,
        tx_errors: int = None,
        rx_bytes: int = None,
    ):
        self.rx_errors = rx_errors
        self.tx_bytes = tx_bytes
        self.name = name
        self.tx_errors = tx_errors
        self.rx_bytes = rx_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rx_errors is not None:
            result['RxErrors'] = self.rx_errors
        if self.tx_bytes is not None:
            result['TxBytes'] = self.tx_bytes
        if self.name is not None:
            result['Name'] = self.name
        if self.tx_errors is not None:
            result['TxErrors'] = self.tx_errors
        if self.rx_bytes is not None:
            result['RxBytes'] = self.rx_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RxErrors') is not None:
            self.rx_errors = m.get('RxErrors')
        if m.get('TxBytes') is not None:
            self.tx_bytes = m.get('TxBytes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TxErrors') is not None:
            self.tx_errors = m.get('TxErrors')
        if m.get('RxBytes') is not None:
            self.rx_bytes = m.get('RxBytes')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsNetwork(TeaModel):
    def __init__(
        self,
        interfaces: List[DescribeContainerGroupMetricResponseBodyRecordsNetworkInterfaces] = None,
    ):
        self.interfaces = interfaces

    def validate(self):
        if self.interfaces:
            for k in self.interfaces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Interfaces'] = []
        if self.interfaces is not None:
            for k in self.interfaces:
                result['Interfaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.interfaces = []
        if m.get('Interfaces') is not None:
            for k in m.get('Interfaces'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecordsNetworkInterfaces()
                self.interfaces.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupMetricResponseBodyRecordsCPU(TeaModel):
    def __init__(
        self,
        usage_nano_cores: int = None,
        limit: int = None,
        usage_core_nano_seconds: int = None,
        load: int = None,
    ):
        self.usage_nano_cores = usage_nano_cores
        self.limit = limit
        self.usage_core_nano_seconds = usage_core_nano_seconds
        self.load = load

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.usage_nano_cores is not None:
            result['UsageNanoCores'] = self.usage_nano_cores
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.usage_core_nano_seconds is not None:
            result['UsageCoreNanoSeconds'] = self.usage_core_nano_seconds
        if self.load is not None:
            result['Load'] = self.load
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsageNanoCores') is not None:
            self.usage_nano_cores = m.get('UsageNanoCores')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('UsageCoreNanoSeconds') is not None:
            self.usage_core_nano_seconds = m.get('UsageCoreNanoSeconds')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsMemory(TeaModel):
    def __init__(
        self,
        rss: int = None,
        usage_bytes: int = None,
        working_set: int = None,
        available_bytes: int = None,
        cache: int = None,
    ):
        self.rss = rss
        self.usage_bytes = usage_bytes
        self.working_set = working_set
        self.available_bytes = available_bytes
        self.cache = cache

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.usage_bytes is not None:
            result['UsageBytes'] = self.usage_bytes
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        if self.available_bytes is not None:
            result['AvailableBytes'] = self.available_bytes
        if self.cache is not None:
            result['Cache'] = self.cache
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('UsageBytes') is not None:
            self.usage_bytes = m.get('UsageBytes')
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        if m.get('AvailableBytes') is not None:
            self.available_bytes = m.get('AvailableBytes')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsContainersCPU(TeaModel):
    def __init__(
        self,
        usage_nano_cores: int = None,
        limit: int = None,
        usage_core_nano_seconds: int = None,
        load: int = None,
    ):
        self.usage_nano_cores = usage_nano_cores
        self.limit = limit
        self.usage_core_nano_seconds = usage_core_nano_seconds
        self.load = load

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.usage_nano_cores is not None:
            result['UsageNanoCores'] = self.usage_nano_cores
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.usage_core_nano_seconds is not None:
            result['UsageCoreNanoSeconds'] = self.usage_core_nano_seconds
        if self.load is not None:
            result['Load'] = self.load
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsageNanoCores') is not None:
            self.usage_nano_cores = m.get('UsageNanoCores')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('UsageCoreNanoSeconds') is not None:
            self.usage_core_nano_seconds = m.get('UsageCoreNanoSeconds')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsContainersMemory(TeaModel):
    def __init__(
        self,
        rss: int = None,
        usage_bytes: int = None,
        working_set: int = None,
        available_bytes: int = None,
        cache: int = None,
    ):
        self.rss = rss
        self.usage_bytes = usage_bytes
        self.working_set = working_set
        self.available_bytes = available_bytes
        self.cache = cache

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.usage_bytes is not None:
            result['UsageBytes'] = self.usage_bytes
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        if self.available_bytes is not None:
            result['AvailableBytes'] = self.available_bytes
        if self.cache is not None:
            result['Cache'] = self.cache
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('UsageBytes') is not None:
            self.usage_bytes = m.get('UsageBytes')
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        if m.get('AvailableBytes') is not None:
            self.available_bytes = m.get('AvailableBytes')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsContainers(TeaModel):
    def __init__(
        self,
        cpu: DescribeContainerGroupMetricResponseBodyRecordsContainersCPU = None,
        memory: DescribeContainerGroupMetricResponseBodyRecordsContainersMemory = None,
        name: str = None,
    ):
        self.cpu = cpu
        self.memory = memory
        self.name = name

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsContainersCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        if m.get('Memory') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsContainersMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeContainerGroupMetricResponseBodyRecords(TeaModel):
    def __init__(
        self,
        network: DescribeContainerGroupMetricResponseBodyRecordsNetwork = None,
        cpu: DescribeContainerGroupMetricResponseBodyRecordsCPU = None,
        timestamp: str = None,
        memory: DescribeContainerGroupMetricResponseBodyRecordsMemory = None,
        containers: List[DescribeContainerGroupMetricResponseBodyRecordsContainers] = None,
    ):
        self.network = network
        self.cpu = cpu
        self.timestamp = timestamp
        self.memory = memory
        self.containers = containers

    def validate(self):
        if self.network:
            self.network.validate()
        if self.cpu:
            self.cpu.validate()
        if self.memory:
            self.memory.validate()
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Network') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('CPU') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Memory') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsMemory()
            self.memory = temp_model.from_map(m['Memory'])
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecordsContainers()
                self.containers.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupMetricResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        container_group_id: str = None,
        records: List[DescribeContainerGroupMetricResponseBodyRecords] = None,
    ):
        self.request_id = request_id
        self.container_group_id = container_group_id
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeContainerGroupMetricResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeContainerGroupMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupPriceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        cpu: float = None,
        memory: float = None,
        instance_type: str = None,
        spot_strategy: str = None,
        zone_id: str = None,
        spot_price_limit: float = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.cpu = cpu
        self.memory = memory
        self.instance_type = instance_type
        self.spot_strategy = spot_strategy
        self.zone_id = zone_id
        self.spot_price_limit = spot_price_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoSpotPricesSpotPrice(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
        spot_price: float = None,
        instance_type: str = None,
        origin_price: float = None,
    ):
        self.zone_id = zone_id
        self.spot_price = spot_price
        self.instance_type = instance_type
        self.origin_price = origin_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.spot_price is not None:
            result['SpotPrice'] = self.spot_price
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('SpotPrice') is not None:
            self.spot_price = m.get('SpotPrice')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoSpotPrices(TeaModel):
    def __init__(
        self,
        spot_price: List[DescribeContainerGroupPriceResponseBodyPriceInfoSpotPricesSpotPrice] = None,
    ):
        self.spot_price = spot_price

    def validate(self):
        if self.spot_price:
            for k in self.spot_price:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SpotPrice'] = []
        if self.spot_price is not None:
            for k in self.spot_price:
                result['SpotPrice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.spot_price = []
        if m.get('SpotPrice') is not None:
            for k in m.get('SpotPrice'):
                temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoSpotPricesSpotPrice()
                self.spot_price.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRulesRule(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRules(TeaModel):
    def __init__(
        self,
        rule: List[DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo(TeaModel):
    def __init__(
        self,
        resource: str = None,
        discount_price: float = None,
        trade_price: float = None,
        original_price: float = None,
        rules: DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRules = None,
    ):
        self.resource = resource
        self.discount_price = discount_price
        self.trade_price = trade_price
        self.original_price = original_price
        self.rules = rules

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('Rules') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfos(TeaModel):
    def __init__(
        self,
        detail_info: List[DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo] = None,
    ):
        self.detail_info = detail_info

    def validate(self):
        if self.detail_info:
            for k in self.detail_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DetailInfo'] = []
        if self.detail_info is not None:
            for k in self.detail_info:
                result['DetailInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_info = []
        if m.get('DetailInfo') is not None:
            for k in m.get('DetailInfo'):
                temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo()
                self.detail_info.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPrice(TeaModel):
    def __init__(
        self,
        discount_price: float = None,
        trade_price: float = None,
        original_price: float = None,
        detail_infos: DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfos = None,
        currency: str = None,
    ):
        self.discount_price = discount_price
        self.trade_price = trade_price
        self.original_price = original_price
        self.detail_infos = detail_infos
        self.currency = currency

    def validate(self):
        if self.detail_infos:
            self.detail_infos.validate()

    def to_map(self):
        result = dict()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.detail_infos is not None:
            result['DetailInfos'] = self.detail_infos.to_map()
        if self.currency is not None:
            result['Currency'] = self.currency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('DetailInfos') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfos()
            self.detail_infos = temp_model.from_map(m['DetailInfos'])
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoRulesRule(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(
        self,
        rule: List[DescribeContainerGroupPriceResponseBodyPriceInfoRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfo(TeaModel):
    def __init__(
        self,
        spot_prices: DescribeContainerGroupPriceResponseBodyPriceInfoSpotPrices = None,
        price: DescribeContainerGroupPriceResponseBodyPriceInfoPrice = None,
        rules: DescribeContainerGroupPriceResponseBodyPriceInfoRules = None,
    ):
        self.spot_prices = spot_prices
        self.price = price
        self.rules = rules

    def validate(self):
        if self.spot_prices:
            self.spot_prices.validate()
        if self.price:
            self.price.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        if self.spot_prices is not None:
            result['SpotPrices'] = self.spot_prices.to_map()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpotPrices') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoSpotPrices()
            self.spot_prices = temp_model.from_map(m['SpotPrices'])
        if m.get('Price') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m['Price'])
        if m.get('Rules') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class DescribeContainerGroupPriceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        price_info: DescribeContainerGroupPriceResponseBodyPriceInfo = None,
    ):
        self.request_id = request_id
        self.price_info = price_info

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PriceInfo') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        return self


class DescribeContainerGroupPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeContainerGroupPriceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeContainerGroupPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupsRequestTag(TeaModel):
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


class DescribeContainerGroupsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        zone_id: str = None,
        v_switch_id: str = None,
        next_token: str = None,
        limit: int = None,
        container_group_ids: str = None,
        container_group_name: str = None,
        status: str = None,
        vk_client_version: str = None,
        resource_group_id: str = None,
        with_event: bool = None,
        tag: List[DescribeContainerGroupsRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.zone_id = zone_id
        self.v_switch_id = v_switch_id
        self.next_token = next_token
        self.limit = limit
        self.container_group_ids = container_group_ids
        self.container_group_name = container_group_name
        self.status = status
        self.vk_client_version = vk_client_version
        self.resource_group_id = resource_group_id
        self.with_event = with_event
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.container_group_ids is not None:
            result['ContainerGroupIds'] = self.container_group_ids
        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name
        if self.status is not None:
            result['Status'] = self.status
        if self.vk_client_version is not None:
            result['VkClientVersion'] = self.vk_client_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.with_event is not None:
            result['WithEvent'] = self.with_event
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('ContainerGroupIds') is not None:
            self.container_group_ids = m.get('ContainerGroupIds')
        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VkClientVersion') is not None:
            self.vk_client_version = m.get('VkClientVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('WithEvent') is not None:
            self.with_event = m.get('WithEvent')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeContainerGroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsHostAliases(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        ip: str = None,
    ):
        self.hostnames = hostnames
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsTags(TeaModel):
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


class DescribeContainerGroupsResponseBodyContainerGroupsEvents(TeaModel):
    def __init__(
        self,
        type: str = None,
        last_timestamp: str = None,
        message: str = None,
        name: str = None,
        reason: str = None,
        count: int = None,
        first_timestamp: str = None,
    ):
        self.type = type
        self.last_timestamp = last_timestamp
        self.message = message
        self.name = name
        self.reason = reason
        self.count = count
        self.first_timestamp = first_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.count is not None:
            result['Count'] = self.count
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeHttpGet(TeaModel):
    def __init__(
        self,
        scheme: str = None,
        path: str = None,
        port: int = None,
    ):
        self.scheme = scheme
        self.path = path
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbe(TeaModel):
    def __init__(
        self,
        success_threshold: int = None,
        initial_delay_seconds: int = None,
        failure_threshold: int = None,
        timeout_seconds: int = None,
        tcp_socket: DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeTcpSocket = None,
        execs: List[str] = None,
        http_get: DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeHttpGet = None,
        period_seconds: int = None,
    ):
        self.success_threshold = success_threshold
        self.initial_delay_seconds = initial_delay_seconds
        self.failure_threshold = failure_threshold
        self.timeout_seconds = timeout_seconds
        self.tcp_socket = tcp_socket
        self.execs = execs
        self.http_get = http_get
        self.period_seconds = period_seconds

    def validate(self):
        if self.tcp_socket:
            self.tcp_socket.validate()
        if self.http_get:
            self.http_get.validate()

    def to_map(self):
        result = dict()
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.execs is not None:
            result['Execs'] = self.execs
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        if m.get('TcpSocket') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('Execs') is not None:
            self.execs = m.get('Execs')
        if m.get('HttpGet') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersVolumeMounts(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        read_only: bool = None,
        name: str = None,
    ):
        self.mount_path = mount_path
        self.read_only = read_only
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersPorts(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        port: int = None,
    ):
        self.protocol = protocol
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersPreviousState(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        finish_time: str = None,
        detail_status: str = None,
        state: str = None,
        message: str = None,
        signal: int = None,
        exit_code: int = None,
        reason: str = None,
    ):
        self.start_time = start_time
        self.finish_time = finish_time
        self.detail_status = detail_status
        self.state = state
        self.message = message
        self.signal = signal
        self.exit_code = exit_code
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status
        if self.state is not None:
            result['State'] = self.state
        if self.message is not None:
            result['Message'] = self.message
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersCurrentState(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        finish_time: str = None,
        detail_status: str = None,
        state: str = None,
        message: str = None,
        signal: int = None,
        exit_code: int = None,
        reason: str = None,
    ):
        self.start_time = start_time
        self.finish_time = finish_time
        self.detail_status = detail_status
        self.state = state
        self.message = message
        self.signal = signal
        self.exit_code = exit_code
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status
        if self.state is not None:
            result['State'] = self.state
        if self.message is not None:
            result['Message'] = self.message
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContextCapability(TeaModel):
    def __init__(
        self,
        adds: List[str] = None,
    ):
        self.adds = adds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.adds is not None:
            result['Adds'] = self.adds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adds') is not None:
            self.adds = m.get('Adds')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContext(TeaModel):
    def __init__(
        self,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
        capability: DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContextCapability = None,
    ):
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user
        self.capability = capability

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        result = dict()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        if m.get('Capability') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFromFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFrom(TeaModel):
    def __init__(
        self,
        field_ref: DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFromFieldRef = None,
    ):
        self.field_ref = field_ref

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFromFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVars(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        value_from: DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFrom = None,
    ):
        self.key = key
        self.value = value
        self.value_from = value_from

    def validate(self):
        if self.value_from:
            self.value_from.validate()

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.value_from is not None:
            result['ValueFrom'] = self.value_from.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueFrom') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFrom()
            self.value_from = temp_model.from_map(m['ValueFrom'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeHttpGet(TeaModel):
    def __init__(
        self,
        scheme: str = None,
        path: str = None,
        port: int = None,
    ):
        self.scheme = scheme
        self.path = path
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbe(TeaModel):
    def __init__(
        self,
        success_threshold: int = None,
        initial_delay_seconds: int = None,
        failure_threshold: int = None,
        timeout_seconds: int = None,
        tcp_socket: DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeTcpSocket = None,
        execs: List[str] = None,
        http_get: DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeHttpGet = None,
        period_seconds: int = None,
    ):
        self.success_threshold = success_threshold
        self.initial_delay_seconds = initial_delay_seconds
        self.failure_threshold = failure_threshold
        self.timeout_seconds = timeout_seconds
        self.tcp_socket = tcp_socket
        self.execs = execs
        self.http_get = http_get
        self.period_seconds = period_seconds

    def validate(self):
        if self.tcp_socket:
            self.tcp_socket.validate()
        if self.http_get:
            self.http_get.validate()

    def to_map(self):
        result = dict()
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.execs is not None:
            result['Execs'] = self.execs
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        if m.get('TcpSocket') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('Execs') is not None:
            self.execs = m.get('Execs')
        if m.get('HttpGet') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainers(TeaModel):
    def __init__(
        self,
        liveness_probe: DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbe = None,
        commands: List[str] = None,
        volume_mounts: List[DescribeContainerGroupsResponseBodyContainerGroupsContainersVolumeMounts] = None,
        args: List[str] = None,
        image: str = None,
        ports: List[DescribeContainerGroupsResponseBodyContainerGroupsContainersPorts] = None,
        restart_count: int = None,
        image_pull_policy: str = None,
        stdin_once: bool = None,
        cpu: float = None,
        previous_state: DescribeContainerGroupsResponseBodyContainerGroupsContainersPreviousState = None,
        tty: bool = None,
        working_dir: str = None,
        current_state: DescribeContainerGroupsResponseBodyContainerGroupsContainersCurrentState = None,
        ready: bool = None,
        gpu: int = None,
        security_context: DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContext = None,
        memory: float = None,
        stdin: bool = None,
        name: str = None,
        environment_vars: List[DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVars] = None,
        readiness_probe: DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbe = None,
    ):
        self.liveness_probe = liveness_probe
        self.commands = commands
        self.volume_mounts = volume_mounts
        self.args = args
        self.image = image
        self.ports = ports
        self.restart_count = restart_count
        self.image_pull_policy = image_pull_policy
        self.stdin_once = stdin_once
        self.cpu = cpu
        self.previous_state = previous_state
        self.tty = tty
        self.working_dir = working_dir
        self.current_state = current_state
        self.ready = ready
        self.gpu = gpu
        self.security_context = security_context
        self.memory = memory
        self.stdin = stdin
        self.name = name
        self.environment_vars = environment_vars
        self.readiness_probe = readiness_probe

    def validate(self):
        if self.liveness_probe:
            self.liveness_probe.validate()
        if self.volume_mounts:
            for k in self.volume_mounts:
                if k:
                    k.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.previous_state:
            self.previous_state.validate()
        if self.current_state:
            self.current_state.validate()
        if self.security_context:
            self.security_context.validate()
        if self.environment_vars:
            for k in self.environment_vars:
                if k:
                    k.validate()
        if self.readiness_probe:
            self.readiness_probe.validate()

    def to_map(self):
        result = dict()
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()
        if self.commands is not None:
            result['Commands'] = self.commands
        result['VolumeMounts'] = []
        if self.volume_mounts is not None:
            for k in self.volume_mounts:
                result['VolumeMounts'].append(k.to_map() if k else None)
        if self.args is not None:
            result['Args'] = self.args
        if self.image is not None:
            result['Image'] = self.image
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.previous_state is not None:
            result['PreviousState'] = self.previous_state.to_map()
        if self.tty is not None:
            result['Tty'] = self.tty
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.current_state is not None:
            result['CurrentState'] = self.current_state.to_map()
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.name is not None:
            result['Name'] = self.name
        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k in self.environment_vars:
                result['EnvironmentVars'].append(k.to_map() if k else None)
        if self.readiness_probe is not None:
            result['ReadinessProbe'] = self.readiness_probe.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LivenessProbe') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbe()
            self.liveness_probe = temp_model.from_map(m['LivenessProbe'])
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        self.volume_mounts = []
        if m.get('VolumeMounts') is not None:
            for k in m.get('VolumeMounts'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersVolumeMounts()
                self.volume_mounts.append(temp_model.from_map(k))
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('PreviousState') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersPreviousState()
            self.previous_state = temp_model.from_map(m['PreviousState'])
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('CurrentState') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersCurrentState()
            self.current_state = temp_model.from_map(m['CurrentState'])
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('SecurityContext') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k in m.get('EnvironmentVars'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k))
        if m.get('ReadinessProbe') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbe()
            self.readiness_probe = temp_model.from_map(m['ReadinessProbe'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersVolumeMounts(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        read_only: bool = None,
        name: str = None,
    ):
        self.mount_path = mount_path
        self.read_only = read_only
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPorts(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        port: int = None,
    ):
        self.protocol = protocol
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPreviousState(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        finish_time: str = None,
        detail_status: str = None,
        state: str = None,
        message: str = None,
        signal: int = None,
        exit_code: int = None,
        reason: str = None,
    ):
        self.start_time = start_time
        self.finish_time = finish_time
        self.detail_status = detail_status
        self.state = state
        self.message = message
        self.signal = signal
        self.exit_code = exit_code
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status
        if self.state is not None:
            result['State'] = self.state
        if self.message is not None:
            result['Message'] = self.message
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersCurrentState(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        finish_time: str = None,
        detail_status: str = None,
        state: str = None,
        message: str = None,
        signal: int = None,
        exit_code: int = None,
        reason: str = None,
    ):
        self.start_time = start_time
        self.finish_time = finish_time
        self.detail_status = detail_status
        self.state = state
        self.message = message
        self.signal = signal
        self.exit_code = exit_code
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status
        if self.state is not None:
            result['State'] = self.state
        if self.message is not None:
            result['Message'] = self.message
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContextCapability(TeaModel):
    def __init__(
        self,
        adds: List[str] = None,
    ):
        self.adds = adds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.adds is not None:
            result['Adds'] = self.adds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adds') is not None:
            self.adds = m.get('Adds')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContext(TeaModel):
    def __init__(
        self,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
        capability: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContextCapability = None,
    ):
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user
        self.capability = capability

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        result = dict()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        if m.get('Capability') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFromFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFrom(TeaModel):
    def __init__(
        self,
        field_ref: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFromFieldRef = None,
    ):
        self.field_ref = field_ref

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFromFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVars(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        value_from: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFrom = None,
    ):
        self.key = key
        self.value = value
        self.value_from = value_from

    def validate(self):
        if self.value_from:
            self.value_from.validate()

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.value_from is not None:
            result['ValueFrom'] = self.value_from.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueFrom') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFrom()
            self.value_from = temp_model.from_map(m['ValueFrom'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainers(TeaModel):
    def __init__(
        self,
        volume_mounts: List[DescribeContainerGroupsResponseBodyContainerGroupsInitContainersVolumeMounts] = None,
        args: List[str] = None,
        image: str = None,
        ports: List[DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPorts] = None,
        restart_count: int = None,
        image_pull_policy: str = None,
        previous_state: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPreviousState = None,
        working_dir: str = None,
        cpu: float = None,
        current_state: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersCurrentState = None,
        command: List[str] = None,
        ready: bool = None,
        gpu: int = None,
        security_context: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContext = None,
        memory: float = None,
        name: str = None,
        environment_vars: List[DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVars] = None,
    ):
        self.volume_mounts = volume_mounts
        self.args = args
        self.image = image
        self.ports = ports
        self.restart_count = restart_count
        self.image_pull_policy = image_pull_policy
        self.previous_state = previous_state
        self.working_dir = working_dir
        self.cpu = cpu
        self.current_state = current_state
        self.command = command
        self.ready = ready
        self.gpu = gpu
        self.security_context = security_context
        self.memory = memory
        self.name = name
        self.environment_vars = environment_vars

    def validate(self):
        if self.volume_mounts:
            for k in self.volume_mounts:
                if k:
                    k.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.previous_state:
            self.previous_state.validate()
        if self.current_state:
            self.current_state.validate()
        if self.security_context:
            self.security_context.validate()
        if self.environment_vars:
            for k in self.environment_vars:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VolumeMounts'] = []
        if self.volume_mounts is not None:
            for k in self.volume_mounts:
                result['VolumeMounts'].append(k.to_map() if k else None)
        if self.args is not None:
            result['Args'] = self.args
        if self.image is not None:
            result['Image'] = self.image
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.previous_state is not None:
            result['PreviousState'] = self.previous_state.to_map()
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.current_state is not None:
            result['CurrentState'] = self.current_state.to_map()
        if self.command is not None:
            result['Command'] = self.command
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k in self.environment_vars:
                result['EnvironmentVars'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.volume_mounts = []
        if m.get('VolumeMounts') is not None:
            for k in m.get('VolumeMounts'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersVolumeMounts()
                self.volume_mounts.append(temp_model.from_map(k))
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('PreviousState') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPreviousState()
            self.previous_state = temp_model.from_map(m['PreviousState'])
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CurrentState') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersCurrentState()
            self.current_state = temp_model.from_map(m['CurrentState'])
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('SecurityContext') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k in m.get('EnvironmentVars'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsDnsConfigOptions(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsDnsConfig(TeaModel):
    def __init__(
        self,
        searches: List[str] = None,
        options: List[DescribeContainerGroupsResponseBodyContainerGroupsDnsConfigOptions] = None,
        name_servers: List[str] = None,
    ):
        self.searches = searches
        self.options = options
        self.name_servers = name_servers

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.searches is not None:
            result['Searches'] = self.searches
        result['Options'] = []
        if self.options is not None:
            for k in self.options:
                result['Options'].append(k.to_map() if k else None)
        if self.name_servers is not None:
            result['NameServers'] = self.name_servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Searches') is not None:
            self.searches = m.get('Searches')
        self.options = []
        if m.get('Options') is not None:
            for k in m.get('Options'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsDnsConfigOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('NameServers') is not None:
            self.name_servers = m.get('NameServers')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsVolumesConfigFileVolumeConfigFileToPaths(TeaModel):
    def __init__(
        self,
        path: str = None,
        content: str = None,
    ):
        self.path = path
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsVolumes(TeaModel):
    def __init__(
        self,
        type: str = None,
        disk_volume_disk_id: str = None,
        nfsvolume_read_only: bool = None,
        config_file_volume_config_file_to_paths: List[DescribeContainerGroupsResponseBodyContainerGroupsVolumesConfigFileVolumeConfigFileToPaths] = None,
        flex_volume_fs_type: str = None,
        flex_volume_driver: str = None,
        disk_volume_fs_type: str = None,
        flex_volume_options: str = None,
        nfsvolume_server: str = None,
        nfsvolume_path: str = None,
        name: str = None,
    ):
        self.type = type
        self.disk_volume_disk_id = disk_volume_disk_id
        self.nfsvolume_read_only = nfsvolume_read_only
        self.config_file_volume_config_file_to_paths = config_file_volume_config_file_to_paths
        self.flex_volume_fs_type = flex_volume_fs_type
        self.flex_volume_driver = flex_volume_driver
        self.disk_volume_fs_type = disk_volume_fs_type
        self.flex_volume_options = flex_volume_options
        self.nfsvolume_server = nfsvolume_server
        self.nfsvolume_path = nfsvolume_path
        self.name = name

    def validate(self):
        if self.config_file_volume_config_file_to_paths:
            for k in self.config_file_volume_config_file_to_paths:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.disk_volume_disk_id is not None:
            result['DiskVolumeDiskId'] = self.disk_volume_disk_id
        if self.nfsvolume_read_only is not None:
            result['NFSVolumeReadOnly'] = self.nfsvolume_read_only
        result['ConfigFileVolumeConfigFileToPaths'] = []
        if self.config_file_volume_config_file_to_paths is not None:
            for k in self.config_file_volume_config_file_to_paths:
                result['ConfigFileVolumeConfigFileToPaths'].append(k.to_map() if k else None)
        if self.flex_volume_fs_type is not None:
            result['FlexVolumeFsType'] = self.flex_volume_fs_type
        if self.flex_volume_driver is not None:
            result['FlexVolumeDriver'] = self.flex_volume_driver
        if self.disk_volume_fs_type is not None:
            result['DiskVolumeFsType'] = self.disk_volume_fs_type
        if self.flex_volume_options is not None:
            result['FlexVolumeOptions'] = self.flex_volume_options
        if self.nfsvolume_server is not None:
            result['NFSVolumeServer'] = self.nfsvolume_server
        if self.nfsvolume_path is not None:
            result['NFSVolumePath'] = self.nfsvolume_path
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DiskVolumeDiskId') is not None:
            self.disk_volume_disk_id = m.get('DiskVolumeDiskId')
        if m.get('NFSVolumeReadOnly') is not None:
            self.nfsvolume_read_only = m.get('NFSVolumeReadOnly')
        self.config_file_volume_config_file_to_paths = []
        if m.get('ConfigFileVolumeConfigFileToPaths') is not None:
            for k in m.get('ConfigFileVolumeConfigFileToPaths'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsVolumesConfigFileVolumeConfigFileToPaths()
                self.config_file_volume_config_file_to_paths.append(temp_model.from_map(k))
        if m.get('FlexVolumeFsType') is not None:
            self.flex_volume_fs_type = m.get('FlexVolumeFsType')
        if m.get('FlexVolumeDriver') is not None:
            self.flex_volume_driver = m.get('FlexVolumeDriver')
        if m.get('DiskVolumeFsType') is not None:
            self.disk_volume_fs_type = m.get('DiskVolumeFsType')
        if m.get('FlexVolumeOptions') is not None:
            self.flex_volume_options = m.get('FlexVolumeOptions')
        if m.get('NFSVolumeServer') is not None:
            self.nfsvolume_server = m.get('NFSVolumeServer')
        if m.get('NFSVolumePath') is not None:
            self.nfsvolume_path = m.get('NFSVolumePath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContextSysctls(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContext(TeaModel):
    def __init__(
        self,
        sysctls: List[DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContextSysctls] = None,
    ):
        self.sysctls = sysctls

    def validate(self):
        if self.sysctls:
            for k in self.sysctls:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Sysctls'] = []
        if self.sysctls is not None:
            for k in self.sysctls:
                result['Sysctls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sysctls = []
        if m.get('Sysctls') is not None:
            for k in m.get('Sysctls'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContextSysctls()
                self.sysctls.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupsResponseBodyContainerGroups(TeaModel):
    def __init__(
        self,
        status: str = None,
        creation_time: str = None,
        vpc_id: str = None,
        internet_ip: str = None,
        tenant_security_group_id: str = None,
        security_group_id: str = None,
        host_aliases: List[DescribeContainerGroupsResponseBodyContainerGroupsHostAliases] = None,
        tags: List[DescribeContainerGroupsResponseBodyContainerGroupsTags] = None,
        events: List[DescribeContainerGroupsResponseBodyContainerGroupsEvents] = None,
        succeeded_time: str = None,
        spot_strategy: str = None,
        tenant_eni_instance_id: str = None,
        discount: int = None,
        restart_policy: str = None,
        memory: float = None,
        tenant_vswitch_id: str = None,
        containers: List[DescribeContainerGroupsResponseBodyContainerGroupsContainers] = None,
        eni_instance_id: str = None,
        init_containers: List[DescribeContainerGroupsResponseBodyContainerGroupsInitContainers] = None,
        container_group_id: str = None,
        instance_type: str = None,
        ipv_6address: str = None,
        intranet_ip: str = None,
        region_id: str = None,
        dns_config: DescribeContainerGroupsResponseBodyContainerGroupsDnsConfig = None,
        volumes: List[DescribeContainerGroupsResponseBodyContainerGroupsVolumes] = None,
        ram_role_name: str = None,
        v_switch_id: str = None,
        cpu: float = None,
        expired_time: str = None,
        resource_group_id: str = None,
        zone_id: str = None,
        container_group_name: str = None,
        eci_security_context: DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContext = None,
        failed_time: str = None,
    ):
        self.status = status
        self.creation_time = creation_time
        self.vpc_id = vpc_id
        self.internet_ip = internet_ip
        self.tenant_security_group_id = tenant_security_group_id
        self.security_group_id = security_group_id
        self.host_aliases = host_aliases
        self.tags = tags
        self.events = events
        self.succeeded_time = succeeded_time
        self.spot_strategy = spot_strategy
        self.tenant_eni_instance_id = tenant_eni_instance_id
        self.discount = discount
        self.restart_policy = restart_policy
        self.memory = memory
        self.tenant_vswitch_id = tenant_vswitch_id
        self.containers = containers
        self.eni_instance_id = eni_instance_id
        self.init_containers = init_containers
        self.container_group_id = container_group_id
        self.instance_type = instance_type
        self.ipv_6address = ipv_6address
        self.intranet_ip = intranet_ip
        self.region_id = region_id
        self.dns_config = dns_config
        self.volumes = volumes
        self.ram_role_name = ram_role_name
        self.v_switch_id = v_switch_id
        self.cpu = cpu
        self.expired_time = expired_time
        self.resource_group_id = resource_group_id
        self.zone_id = zone_id
        self.container_group_name = container_group_name
        self.eci_security_context = eci_security_context
        self.failed_time = failed_time

    def validate(self):
        if self.host_aliases:
            for k in self.host_aliases:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        if self.init_containers:
            for k in self.init_containers:
                if k:
                    k.validate()
        if self.dns_config:
            self.dns_config.validate()
        if self.volumes:
            for k in self.volumes:
                if k:
                    k.validate()
        if self.eci_security_context:
            self.eci_security_context.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.tenant_security_group_id is not None:
            result['TenantSecurityGroupId'] = self.tenant_security_group_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        result['HostAliases'] = []
        if self.host_aliases is not None:
            for k in self.host_aliases:
                result['HostAliases'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.succeeded_time is not None:
            result['SucceededTime'] = self.succeeded_time
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.tenant_eni_instance_id is not None:
            result['TenantEniInstanceId'] = self.tenant_eni_instance_id
        if self.discount is not None:
            result['Discount'] = self.discount
        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.tenant_vswitch_id is not None:
            result['TenantVSwitchId'] = self.tenant_vswitch_id
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        if self.eni_instance_id is not None:
            result['EniInstanceId'] = self.eni_instance_id
        result['InitContainers'] = []
        if self.init_containers is not None:
            for k in self.init_containers:
                result['InitContainers'].append(k.to_map() if k else None)
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dns_config is not None:
            result['DnsConfig'] = self.dns_config.to_map()
        result['Volumes'] = []
        if self.volumes is not None:
            for k in self.volumes:
                result['Volumes'].append(k.to_map() if k else None)
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name
        if self.eci_security_context is not None:
            result['EciSecurityContext'] = self.eci_security_context.to_map()
        if self.failed_time is not None:
            result['FailedTime'] = self.failed_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('TenantSecurityGroupId') is not None:
            self.tenant_security_group_id = m.get('TenantSecurityGroupId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        self.host_aliases = []
        if m.get('HostAliases') is not None:
            for k in m.get('HostAliases'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsHostAliases()
                self.host_aliases.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsTags()
                self.tags.append(temp_model.from_map(k))
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('SucceededTime') is not None:
            self.succeeded_time = m.get('SucceededTime')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('TenantEniInstanceId') is not None:
            self.tenant_eni_instance_id = m.get('TenantEniInstanceId')
        if m.get('Discount') is not None:
            self.discount = m.get('Discount')
        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('TenantVSwitchId') is not None:
            self.tenant_vswitch_id = m.get('TenantVSwitchId')
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainers()
                self.containers.append(temp_model.from_map(k))
        if m.get('EniInstanceId') is not None:
            self.eni_instance_id = m.get('EniInstanceId')
        self.init_containers = []
        if m.get('InitContainers') is not None:
            for k in m.get('InitContainers'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainers()
                self.init_containers.append(temp_model.from_map(k))
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DnsConfig') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsDnsConfig()
            self.dns_config = temp_model.from_map(m['DnsConfig'])
        self.volumes = []
        if m.get('Volumes') is not None:
            for k in m.get('Volumes'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsVolumes()
                self.volumes.append(temp_model.from_map(k))
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')
        if m.get('EciSecurityContext') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContext()
            self.eci_security_context = temp_model.from_map(m['EciSecurityContext'])
        if m.get('FailedTime') is not None:
            self.failed_time = m.get('FailedTime')
        return self


class DescribeContainerGroupsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        next_token: str = None,
        request_id: str = None,
        container_groups: List[DescribeContainerGroupsResponseBodyContainerGroups] = None,
    ):
        self.total_count = total_count
        self.next_token = next_token
        self.request_id = request_id
        self.container_groups = container_groups

    def validate(self):
        if self.container_groups:
            for k in self.container_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ContainerGroups'] = []
        if self.container_groups is not None:
            for k in self.container_groups:
                result['ContainerGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.container_groups = []
        if m.get('ContainerGroups') is not None:
            for k in m.get('ContainerGroups'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroups()
                self.container_groups.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeContainerGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeContainerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerLogRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        container_group_id: str = None,
        container_name: str = None,
        start_time: str = None,
        tail: int = None,
        last_time: bool = None,
        since_seconds: int = None,
        limit_bytes: int = None,
        timestamps: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.container_group_id = container_group_id
        self.container_name = container_name
        self.start_time = start_time
        self.tail = tail
        self.last_time = last_time
        self.since_seconds = since_seconds
        self.limit_bytes = limit_bytes
        self.timestamps = timestamps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tail is not None:
            result['Tail'] = self.tail
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.since_seconds is not None:
            result['SinceSeconds'] = self.since_seconds
        if self.limit_bytes is not None:
            result['LimitBytes'] = self.limit_bytes
        if self.timestamps is not None:
            result['Timestamps'] = self.timestamps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Tail') is not None:
            self.tail = m.get('Tail')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('SinceSeconds') is not None:
            self.since_seconds = m.get('SinceSeconds')
        if m.get('LimitBytes') is not None:
            self.limit_bytes = m.get('LimitBytes')
        if m.get('Timestamps') is not None:
            self.timestamps = m.get('Timestamps')
        return self


class DescribeContainerLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        container_name: str = None,
        content: str = None,
    ):
        self.request_id = request_id
        self.container_name = container_name
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeContainerLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeContainerLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeContainerLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageCachesRequestTag(TeaModel):
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


class DescribeImageCachesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        image_cache_id: str = None,
        image_cache_name: str = None,
        snapshot_id: str = None,
        image: str = None,
        resource_group_id: str = None,
        tag: List[DescribeImageCachesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.image_cache_id = image_cache_id
        self.image_cache_name = image_cache_name
        self.snapshot_id = snapshot_id
        self.image = image
        self.resource_group_id = resource_group_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.image is not None:
            result['Image'] = self.image
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeImageCachesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeImageCachesResponseBodyImageCachesTags(TeaModel):
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


class DescribeImageCachesResponseBodyImageCachesEvents(TeaModel):
    def __init__(
        self,
        type: str = None,
        last_timestamp: str = None,
        message: str = None,
        name: str = None,
        count: int = None,
        first_timestamp: str = None,
    ):
        self.type = type
        self.last_timestamp = last_timestamp
        self.message = message
        self.name = name
        self.count = count
        self.first_timestamp = first_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.count is not None:
            result['Count'] = self.count
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        return self


class DescribeImageCachesResponseBodyImageCaches(TeaModel):
    def __init__(
        self,
        images: List[str] = None,
        creation_time: str = None,
        status: str = None,
        progress: str = None,
        expire_date_time: str = None,
        container_group_id: str = None,
        tags: List[DescribeImageCachesResponseBodyImageCachesTags] = None,
        events: List[DescribeImageCachesResponseBodyImageCachesEvents] = None,
        image_cache_id: str = None,
        region_id: str = None,
        snapshot_id: str = None,
        resource_group_id: str = None,
        image_cache_name: str = None,
    ):
        self.images = images
        self.creation_time = creation_time
        self.status = status
        self.progress = progress
        self.expire_date_time = expire_date_time
        self.container_group_id = container_group_id
        self.tags = tags
        self.events = events
        self.image_cache_id = image_cache_id
        self.region_id = region_id
        self.snapshot_id = snapshot_id
        self.resource_group_id = resource_group_id
        self.image_cache_name = image_cache_name

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.images is not None:
            result['Images'] = self.images
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.expire_date_time is not None:
            result['ExpireDateTime'] = self.expire_date_time
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ExpireDateTime') is not None:
            self.expire_date_time = m.get('ExpireDateTime')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeImageCachesResponseBodyImageCachesTags()
                self.tags.append(temp_model.from_map(k))
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeImageCachesResponseBodyImageCachesEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        return self


class DescribeImageCachesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        image_caches: List[DescribeImageCachesResponseBodyImageCaches] = None,
    ):
        self.request_id = request_id
        self.image_caches = image_caches

    def validate(self):
        if self.image_caches:
            for k in self.image_caches:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ImageCaches'] = []
        if self.image_caches is not None:
            for k in self.image_caches:
                result['ImageCaches'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.image_caches = []
        if m.get('ImageCaches') is not None:
            for k in m.get('ImageCaches'):
                temp_model = DescribeImageCachesResponseBodyImageCaches()
                self.image_caches.append(temp_model.from_map(k))
        return self


class DescribeImageCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImageCachesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeImageCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMultiContainerGroupMetricRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        container_group_ids: str = None,
        resource_group_id: str = None,
        metric_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.container_group_ids = container_group_ids
        self.resource_group_id = resource_group_id
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.container_group_ids is not None:
            result['ContainerGroupIds'] = self.container_group_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ContainerGroupIds') is not None:
            self.container_group_ids = m.get('ContainerGroupIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetworkInterfaces(TeaModel):
    def __init__(
        self,
        rx_errors: int = None,
        tx_bytes: int = None,
        name: str = None,
        tx_errors: int = None,
        rx_bytes: int = None,
    ):
        self.rx_errors = rx_errors
        self.tx_bytes = tx_bytes
        self.name = name
        self.tx_errors = tx_errors
        self.rx_bytes = rx_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rx_errors is not None:
            result['RxErrors'] = self.rx_errors
        if self.tx_bytes is not None:
            result['TxBytes'] = self.tx_bytes
        if self.name is not None:
            result['Name'] = self.name
        if self.tx_errors is not None:
            result['TxErrors'] = self.tx_errors
        if self.rx_bytes is not None:
            result['RxBytes'] = self.rx_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RxErrors') is not None:
            self.rx_errors = m.get('RxErrors')
        if m.get('TxBytes') is not None:
            self.tx_bytes = m.get('TxBytes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TxErrors') is not None:
            self.tx_errors = m.get('TxErrors')
        if m.get('RxBytes') is not None:
            self.rx_bytes = m.get('RxBytes')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetwork(TeaModel):
    def __init__(
        self,
        interfaces: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetworkInterfaces] = None,
    ):
        self.interfaces = interfaces

    def validate(self):
        if self.interfaces:
            for k in self.interfaces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Interfaces'] = []
        if self.interfaces is not None:
            for k in self.interfaces:
                result['Interfaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.interfaces = []
        if m.get('Interfaces') is not None:
            for k in m.get('Interfaces'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetworkInterfaces()
                self.interfaces.append(temp_model.from_map(k))
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsCPU(TeaModel):
    def __init__(
        self,
        usage_nano_cores: int = None,
        limit: int = None,
        usage_core_nano_seconds: int = None,
        load: int = None,
    ):
        self.usage_nano_cores = usage_nano_cores
        self.limit = limit
        self.usage_core_nano_seconds = usage_core_nano_seconds
        self.load = load

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.usage_nano_cores is not None:
            result['UsageNanoCores'] = self.usage_nano_cores
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.usage_core_nano_seconds is not None:
            result['UsageCoreNanoSeconds'] = self.usage_core_nano_seconds
        if self.load is not None:
            result['Load'] = self.load
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsageNanoCores') is not None:
            self.usage_nano_cores = m.get('UsageNanoCores')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('UsageCoreNanoSeconds') is not None:
            self.usage_core_nano_seconds = m.get('UsageCoreNanoSeconds')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsMemory(TeaModel):
    def __init__(
        self,
        rss: int = None,
        usage_bytes: int = None,
        working_set: int = None,
        available_bytes: int = None,
        cache: int = None,
    ):
        self.rss = rss
        self.usage_bytes = usage_bytes
        self.working_set = working_set
        self.available_bytes = available_bytes
        self.cache = cache

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.usage_bytes is not None:
            result['UsageBytes'] = self.usage_bytes
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        if self.available_bytes is not None:
            result['AvailableBytes'] = self.available_bytes
        if self.cache is not None:
            result['Cache'] = self.cache
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('UsageBytes') is not None:
            self.usage_bytes = m.get('UsageBytes')
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        if m.get('AvailableBytes') is not None:
            self.available_bytes = m.get('AvailableBytes')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersCPU(TeaModel):
    def __init__(
        self,
        usage_nano_cores: int = None,
        limit: int = None,
        usage_core_nano_seconds: int = None,
        load: int = None,
    ):
        self.usage_nano_cores = usage_nano_cores
        self.limit = limit
        self.usage_core_nano_seconds = usage_core_nano_seconds
        self.load = load

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.usage_nano_cores is not None:
            result['UsageNanoCores'] = self.usage_nano_cores
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.usage_core_nano_seconds is not None:
            result['UsageCoreNanoSeconds'] = self.usage_core_nano_seconds
        if self.load is not None:
            result['Load'] = self.load
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsageNanoCores') is not None:
            self.usage_nano_cores = m.get('UsageNanoCores')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('UsageCoreNanoSeconds') is not None:
            self.usage_core_nano_seconds = m.get('UsageCoreNanoSeconds')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersMemory(TeaModel):
    def __init__(
        self,
        rss: int = None,
        usage_bytes: int = None,
        working_set: int = None,
        available_bytes: int = None,
        cache: int = None,
    ):
        self.rss = rss
        self.usage_bytes = usage_bytes
        self.working_set = working_set
        self.available_bytes = available_bytes
        self.cache = cache

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.usage_bytes is not None:
            result['UsageBytes'] = self.usage_bytes
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        if self.available_bytes is not None:
            result['AvailableBytes'] = self.available_bytes
        if self.cache is not None:
            result['Cache'] = self.cache
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('UsageBytes') is not None:
            self.usage_bytes = m.get('UsageBytes')
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        if m.get('AvailableBytes') is not None:
            self.available_bytes = m.get('AvailableBytes')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainers(TeaModel):
    def __init__(
        self,
        cpu: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersCPU = None,
        memory: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersMemory = None,
        name: str = None,
    ):
        self.cpu = cpu
        self.memory = memory
        self.name = name

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        if m.get('Memory') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecords(TeaModel):
    def __init__(
        self,
        network: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetwork = None,
        cpu: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsCPU = None,
        timestamp: str = None,
        memory: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsMemory = None,
        containers: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainers] = None,
    ):
        self.network = network
        self.cpu = cpu
        self.timestamp = timestamp
        self.memory = memory
        self.containers = containers

    def validate(self):
        if self.network:
            self.network.validate()
        if self.cpu:
            self.cpu.validate()
        if self.memory:
            self.memory.validate()
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Network') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('CPU') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Memory') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsMemory()
            self.memory = temp_model.from_map(m['Memory'])
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainers()
                self.containers.append(temp_model.from_map(k))
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerSpecContainerMemory(TeaModel):
    def __init__(
        self,
        limit: int = None,
        swap_limit: int = None,
        reservation: int = None,
    ):
        self.limit = limit
        self.swap_limit = swap_limit
        self.reservation = reservation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.swap_limit is not None:
            result['SwapLimit'] = self.swap_limit
        if self.reservation is not None:
            result['Reservation'] = self.reservation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('SwapLimit') is not None:
            self.swap_limit = m.get('SwapLimit')
        if m.get('Reservation') is not None:
            self.reservation = m.get('Reservation')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerSpecContainerCpu(TeaModel):
    def __init__(
        self,
        quota: int = None,
        mask: str = None,
        limit: int = None,
        max_limit: int = None,
        period: int = None,
    ):
        self.quota = quota
        self.mask = mask
        self.limit = limit
        self.max_limit = max_limit
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.max_limit is not None:
            result['MaxLimit'] = self.max_limit
        if self.period is not None:
            result['Period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MaxLimit') is not None:
            self.max_limit = m.get('MaxLimit')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerSpec(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        image: str = None,
        labels: str = None,
        has_custom_metrics: bool = None,
        has_cpu: bool = None,
        envs: str = None,
        has_disk_io: bool = None,
        has_filesystem: bool = None,
        has_network: bool = None,
        container_memory: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerSpecContainerMemory = None,
        has_memory: bool = None,
        container_cpu: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerSpecContainerCpu = None,
    ):
        self.creation_time = creation_time
        self.image = image
        self.labels = labels
        self.has_custom_metrics = has_custom_metrics
        self.has_cpu = has_cpu
        self.envs = envs
        self.has_disk_io = has_disk_io
        self.has_filesystem = has_filesystem
        self.has_network = has_network
        self.container_memory = container_memory
        self.has_memory = has_memory
        self.container_cpu = container_cpu

    def validate(self):
        if self.container_memory:
            self.container_memory.validate()
        if self.container_cpu:
            self.container_cpu.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.image is not None:
            result['Image'] = self.image
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.has_custom_metrics is not None:
            result['HasCustomMetrics'] = self.has_custom_metrics
        if self.has_cpu is not None:
            result['HasCpu'] = self.has_cpu
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.has_disk_io is not None:
            result['HasDiskIo'] = self.has_disk_io
        if self.has_filesystem is not None:
            result['HasFilesystem'] = self.has_filesystem
        if self.has_network is not None:
            result['HasNetwork'] = self.has_network
        if self.container_memory is not None:
            result['ContainerMemory'] = self.container_memory.to_map()
        if self.has_memory is not None:
            result['HasMemory'] = self.has_memory
        if self.container_cpu is not None:
            result['ContainerCpu'] = self.container_cpu.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('HasCustomMetrics') is not None:
            self.has_custom_metrics = m.get('HasCustomMetrics')
        if m.get('HasCpu') is not None:
            self.has_cpu = m.get('HasCpu')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('HasDiskIo') is not None:
            self.has_disk_io = m.get('HasDiskIo')
        if m.get('HasFilesystem') is not None:
            self.has_filesystem = m.get('HasFilesystem')
        if m.get('HasNetwork') is not None:
            self.has_network = m.get('HasNetwork')
        if m.get('ContainerMemory') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerSpecContainerMemory()
            self.container_memory = temp_model.from_map(m['ContainerMemory'])
        if m.get('HasMemory') is not None:
            self.has_memory = m.get('HasMemory')
        if m.get('ContainerCpu') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerSpecContainerCpu()
            self.container_cpu = temp_model.from_map(m['ContainerCpu'])
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsTcp(TeaModel):
    def __init__(
        self,
        close_wait: int = None,
        fin_wait_2: int = None,
        last_ack: int = None,
        closing: int = None,
        listen: int = None,
        time_wait: int = None,
        established: int = None,
        fin_wait_1: int = None,
        close: int = None,
        syn_recv: int = None,
        syn_sent: int = None,
    ):
        self.close_wait = close_wait
        self.fin_wait_2 = fin_wait_2
        self.last_ack = last_ack
        self.closing = closing
        self.listen = listen
        self.time_wait = time_wait
        self.established = established
        self.fin_wait_1 = fin_wait_1
        self.close = close
        self.syn_recv = syn_recv
        self.syn_sent = syn_sent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.close_wait is not None:
            result['CloseWait'] = self.close_wait
        if self.fin_wait_2 is not None:
            result['FinWait2'] = self.fin_wait_2
        if self.last_ack is not None:
            result['LastAck'] = self.last_ack
        if self.closing is not None:
            result['Closing'] = self.closing
        if self.listen is not None:
            result['Listen'] = self.listen
        if self.time_wait is not None:
            result['TimeWait'] = self.time_wait
        if self.established is not None:
            result['Established'] = self.established
        if self.fin_wait_1 is not None:
            result['FinWait1'] = self.fin_wait_1
        if self.close is not None:
            result['Close'] = self.close
        if self.syn_recv is not None:
            result['SynRecv'] = self.syn_recv
        if self.syn_sent is not None:
            result['SynSent'] = self.syn_sent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloseWait') is not None:
            self.close_wait = m.get('CloseWait')
        if m.get('FinWait2') is not None:
            self.fin_wait_2 = m.get('FinWait2')
        if m.get('LastAck') is not None:
            self.last_ack = m.get('LastAck')
        if m.get('Closing') is not None:
            self.closing = m.get('Closing')
        if m.get('Listen') is not None:
            self.listen = m.get('Listen')
        if m.get('TimeWait') is not None:
            self.time_wait = m.get('TimeWait')
        if m.get('Established') is not None:
            self.established = m.get('Established')
        if m.get('FinWait1') is not None:
            self.fin_wait_1 = m.get('FinWait1')
        if m.get('Close') is not None:
            self.close = m.get('Close')
        if m.get('SynRecv') is not None:
            self.syn_recv = m.get('SynRecv')
        if m.get('SynSent') is not None:
            self.syn_sent = m.get('SynSent')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsInterfaceStats(TeaModel):
    def __init__(
        self,
        rx_errors: int = None,
        rx_dropped: int = None,
        tx_dropped: int = None,
        tx_bytes: int = None,
        rx_packets: int = None,
        tx_errors: int = None,
        tx_packets: int = None,
        rx_bytes: int = None,
        name: str = None,
    ):
        self.rx_errors = rx_errors
        self.rx_dropped = rx_dropped
        self.tx_dropped = tx_dropped
        self.tx_bytes = tx_bytes
        self.rx_packets = rx_packets
        self.tx_errors = tx_errors
        self.tx_packets = tx_packets
        self.rx_bytes = rx_bytes
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rx_errors is not None:
            result['RxErrors'] = self.rx_errors
        if self.rx_dropped is not None:
            result['RxDropped'] = self.rx_dropped
        if self.tx_dropped is not None:
            result['TxDropped'] = self.tx_dropped
        if self.tx_bytes is not None:
            result['TxBytes'] = self.tx_bytes
        if self.rx_packets is not None:
            result['RxPackets'] = self.rx_packets
        if self.tx_errors is not None:
            result['TxErrors'] = self.tx_errors
        if self.tx_packets is not None:
            result['TxPackets'] = self.tx_packets
        if self.rx_bytes is not None:
            result['RxBytes'] = self.rx_bytes
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RxErrors') is not None:
            self.rx_errors = m.get('RxErrors')
        if m.get('RxDropped') is not None:
            self.rx_dropped = m.get('RxDropped')
        if m.get('TxDropped') is not None:
            self.tx_dropped = m.get('TxDropped')
        if m.get('TxBytes') is not None:
            self.tx_bytes = m.get('TxBytes')
        if m.get('RxPackets') is not None:
            self.rx_packets = m.get('RxPackets')
        if m.get('TxErrors') is not None:
            self.tx_errors = m.get('TxErrors')
        if m.get('TxPackets') is not None:
            self.tx_packets = m.get('TxPackets')
        if m.get('RxBytes') is not None:
            self.rx_bytes = m.get('RxBytes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsTcp6(TeaModel):
    def __init__(
        self,
        close_wait: int = None,
        fin_wait_2: int = None,
        last_ack: int = None,
        closing: int = None,
        listen: int = None,
        time_wait: int = None,
        established: int = None,
        fin_wait_1: int = None,
        close: int = None,
        syn_recv: int = None,
        syn_sent: int = None,
    ):
        self.close_wait = close_wait
        self.fin_wait_2 = fin_wait_2
        self.last_ack = last_ack
        self.closing = closing
        self.listen = listen
        self.time_wait = time_wait
        self.established = established
        self.fin_wait_1 = fin_wait_1
        self.close = close
        self.syn_recv = syn_recv
        self.syn_sent = syn_sent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.close_wait is not None:
            result['CloseWait'] = self.close_wait
        if self.fin_wait_2 is not None:
            result['FinWait2'] = self.fin_wait_2
        if self.last_ack is not None:
            result['LastAck'] = self.last_ack
        if self.closing is not None:
            result['Closing'] = self.closing
        if self.listen is not None:
            result['Listen'] = self.listen
        if self.time_wait is not None:
            result['TimeWait'] = self.time_wait
        if self.established is not None:
            result['Established'] = self.established
        if self.fin_wait_1 is not None:
            result['FinWait1'] = self.fin_wait_1
        if self.close is not None:
            result['Close'] = self.close
        if self.syn_recv is not None:
            result['SynRecv'] = self.syn_recv
        if self.syn_sent is not None:
            result['SynSent'] = self.syn_sent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloseWait') is not None:
            self.close_wait = m.get('CloseWait')
        if m.get('FinWait2') is not None:
            self.fin_wait_2 = m.get('FinWait2')
        if m.get('LastAck') is not None:
            self.last_ack = m.get('LastAck')
        if m.get('Closing') is not None:
            self.closing = m.get('Closing')
        if m.get('Listen') is not None:
            self.listen = m.get('Listen')
        if m.get('TimeWait') is not None:
            self.time_wait = m.get('TimeWait')
        if m.get('Established') is not None:
            self.established = m.get('Established')
        if m.get('FinWait1') is not None:
            self.fin_wait_1 = m.get('FinWait1')
        if m.get('Close') is not None:
            self.close = m.get('Close')
        if m.get('SynRecv') is not None:
            self.syn_recv = m.get('SynRecv')
        if m.get('SynSent') is not None:
            self.syn_sent = m.get('SynSent')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsUdp(TeaModel):
    def __init__(
        self,
        tx_queued: int = None,
        listen: int = None,
        dropped: int = None,
        rx_queued: int = None,
    ):
        self.tx_queued = tx_queued
        self.listen = listen
        self.dropped = dropped
        self.rx_queued = rx_queued

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tx_queued is not None:
            result['TxQueued'] = self.tx_queued
        if self.listen is not None:
            result['Listen'] = self.listen
        if self.dropped is not None:
            result['Dropped'] = self.dropped
        if self.rx_queued is not None:
            result['RxQueued'] = self.rx_queued
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TxQueued') is not None:
            self.tx_queued = m.get('TxQueued')
        if m.get('Listen') is not None:
            self.listen = m.get('Listen')
        if m.get('Dropped') is not None:
            self.dropped = m.get('Dropped')
        if m.get('RxQueued') is not None:
            self.rx_queued = m.get('RxQueued')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsUdp6(TeaModel):
    def __init__(
        self,
        tx_queued: int = None,
        listen: int = None,
        dropped: int = None,
        rx_queued: int = None,
    ):
        self.tx_queued = tx_queued
        self.listen = listen
        self.dropped = dropped
        self.rx_queued = rx_queued

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tx_queued is not None:
            result['TxQueued'] = self.tx_queued
        if self.listen is not None:
            result['Listen'] = self.listen
        if self.dropped is not None:
            result['Dropped'] = self.dropped
        if self.rx_queued is not None:
            result['RxQueued'] = self.rx_queued
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TxQueued') is not None:
            self.tx_queued = m.get('TxQueued')
        if m.get('Listen') is not None:
            self.listen = m.get('Listen')
        if m.get('Dropped') is not None:
            self.dropped = m.get('Dropped')
        if m.get('RxQueued') is not None:
            self.rx_queued = m.get('RxQueued')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStats(TeaModel):
    def __init__(
        self,
        rx_dropped: int = None,
        tcp: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsTcp = None,
        tx_errors: int = None,
        rx_errors: int = None,
        interface_stats: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsInterfaceStats] = None,
        tcp_6: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsTcp6 = None,
        tx_dropped: int = None,
        udp: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsUdp = None,
        tx_bytes: int = None,
        udp_6: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsUdp6 = None,
        rx_packets: int = None,
        name: str = None,
        rx_bytes: int = None,
        tx_packets: int = None,
    ):
        self.rx_dropped = rx_dropped
        self.tcp = tcp
        self.tx_errors = tx_errors
        self.rx_errors = rx_errors
        self.interface_stats = interface_stats
        self.tcp_6 = tcp_6
        self.tx_dropped = tx_dropped
        self.udp = udp
        self.tx_bytes = tx_bytes
        self.udp_6 = udp_6
        self.rx_packets = rx_packets
        self.name = name
        self.rx_bytes = rx_bytes
        self.tx_packets = tx_packets

    def validate(self):
        if self.tcp:
            self.tcp.validate()
        if self.interface_stats:
            for k in self.interface_stats:
                if k:
                    k.validate()
        if self.tcp_6:
            self.tcp_6.validate()
        if self.udp:
            self.udp.validate()
        if self.udp_6:
            self.udp_6.validate()

    def to_map(self):
        result = dict()
        if self.rx_dropped is not None:
            result['RxDropped'] = self.rx_dropped
        if self.tcp is not None:
            result['Tcp'] = self.tcp.to_map()
        if self.tx_errors is not None:
            result['TxErrors'] = self.tx_errors
        if self.rx_errors is not None:
            result['RxErrors'] = self.rx_errors
        result['InterfaceStats'] = []
        if self.interface_stats is not None:
            for k in self.interface_stats:
                result['InterfaceStats'].append(k.to_map() if k else None)
        if self.tcp_6 is not None:
            result['Tcp6'] = self.tcp_6.to_map()
        if self.tx_dropped is not None:
            result['TxDropped'] = self.tx_dropped
        if self.udp is not None:
            result['Udp'] = self.udp.to_map()
        if self.tx_bytes is not None:
            result['TxBytes'] = self.tx_bytes
        if self.udp_6 is not None:
            result['Udp6'] = self.udp_6.to_map()
        if self.rx_packets is not None:
            result['RxPackets'] = self.rx_packets
        if self.name is not None:
            result['Name'] = self.name
        if self.rx_bytes is not None:
            result['RxBytes'] = self.rx_bytes
        if self.tx_packets is not None:
            result['TxPackets'] = self.tx_packets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RxDropped') is not None:
            self.rx_dropped = m.get('RxDropped')
        if m.get('Tcp') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsTcp()
            self.tcp = temp_model.from_map(m['Tcp'])
        if m.get('TxErrors') is not None:
            self.tx_errors = m.get('TxErrors')
        if m.get('RxErrors') is not None:
            self.rx_errors = m.get('RxErrors')
        self.interface_stats = []
        if m.get('InterfaceStats') is not None:
            for k in m.get('InterfaceStats'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsInterfaceStats()
                self.interface_stats.append(temp_model.from_map(k))
        if m.get('Tcp6') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsTcp6()
            self.tcp_6 = temp_model.from_map(m['Tcp6'])
        if m.get('TxDropped') is not None:
            self.tx_dropped = m.get('TxDropped')
        if m.get('Udp') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsUdp()
            self.udp = temp_model.from_map(m['Udp'])
        if m.get('TxBytes') is not None:
            self.tx_bytes = m.get('TxBytes')
        if m.get('Udp6') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStatsUdp6()
            self.udp_6 = temp_model.from_map(m['Udp6'])
        if m.get('RxPackets') is not None:
            self.rx_packets = m.get('RxPackets')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RxBytes') is not None:
            self.rx_bytes = m.get('RxBytes')
        if m.get('TxPackets') is not None:
            self.tx_packets = m.get('TxPackets')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsFsStats(TeaModel):
    def __init__(
        self,
        type: str = None,
        reads_merged: int = None,
        has_inodes: bool = None,
        reads_completed: int = None,
        writes_merged: int = None,
        inodes_free: int = None,
        available: int = None,
        usage: int = None,
        inodes: int = None,
        base_usage: int = None,
        sectors_read: int = None,
        write_time: int = None,
        sectors_written: int = None,
        read_time: int = None,
        limit: int = None,
        device: str = None,
        writes_completed: int = None,
        io_time: int = None,
        weighted_io_time: int = None,
        io_in_progress: int = None,
    ):
        self.type = type
        self.reads_merged = reads_merged
        self.has_inodes = has_inodes
        self.reads_completed = reads_completed
        self.writes_merged = writes_merged
        self.inodes_free = inodes_free
        self.available = available
        self.usage = usage
        self.inodes = inodes
        self.base_usage = base_usage
        self.sectors_read = sectors_read
        self.write_time = write_time
        self.sectors_written = sectors_written
        self.read_time = read_time
        self.limit = limit
        self.device = device
        self.writes_completed = writes_completed
        self.io_time = io_time
        self.weighted_io_time = weighted_io_time
        self.io_in_progress = io_in_progress

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.reads_merged is not None:
            result['ReadsMerged'] = self.reads_merged
        if self.has_inodes is not None:
            result['HasInodes'] = self.has_inodes
        if self.reads_completed is not None:
            result['ReadsCompleted'] = self.reads_completed
        if self.writes_merged is not None:
            result['WritesMerged'] = self.writes_merged
        if self.inodes_free is not None:
            result['InodesFree'] = self.inodes_free
        if self.available is not None:
            result['Available'] = self.available
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.inodes is not None:
            result['Inodes'] = self.inodes
        if self.base_usage is not None:
            result['BaseUsage'] = self.base_usage
        if self.sectors_read is not None:
            result['SectorsRead'] = self.sectors_read
        if self.write_time is not None:
            result['WriteTime'] = self.write_time
        if self.sectors_written is not None:
            result['SectorsWritten'] = self.sectors_written
        if self.read_time is not None:
            result['ReadTime'] = self.read_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.device is not None:
            result['Device'] = self.device
        if self.writes_completed is not None:
            result['WritesCompleted'] = self.writes_completed
        if self.io_time is not None:
            result['IoTime'] = self.io_time
        if self.weighted_io_time is not None:
            result['WeightedIoTime'] = self.weighted_io_time
        if self.io_in_progress is not None:
            result['IoInProgress'] = self.io_in_progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ReadsMerged') is not None:
            self.reads_merged = m.get('ReadsMerged')
        if m.get('HasInodes') is not None:
            self.has_inodes = m.get('HasInodes')
        if m.get('ReadsCompleted') is not None:
            self.reads_completed = m.get('ReadsCompleted')
        if m.get('WritesMerged') is not None:
            self.writes_merged = m.get('WritesMerged')
        if m.get('InodesFree') is not None:
            self.inodes_free = m.get('InodesFree')
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('Inodes') is not None:
            self.inodes = m.get('Inodes')
        if m.get('BaseUsage') is not None:
            self.base_usage = m.get('BaseUsage')
        if m.get('SectorsRead') is not None:
            self.sectors_read = m.get('SectorsRead')
        if m.get('WriteTime') is not None:
            self.write_time = m.get('WriteTime')
        if m.get('SectorsWritten') is not None:
            self.sectors_written = m.get('SectorsWritten')
        if m.get('ReadTime') is not None:
            self.read_time = m.get('ReadTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('WritesCompleted') is not None:
            self.writes_completed = m.get('WritesCompleted')
        if m.get('IoTime') is not None:
            self.io_time = m.get('IoTime')
        if m.get('WeightedIoTime') is not None:
            self.weighted_io_time = m.get('WeightedIoTime')
        if m.get('IoInProgress') is not None:
            self.io_in_progress = m.get('IoInProgress')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsAcceleratorStats(TeaModel):
    def __init__(
        self,
        model: str = None,
        memory_total: int = None,
        make: str = None,
        duty_cycle: int = None,
        id: str = None,
        memory_used: int = None,
    ):
        self.model = model
        self.memory_total = memory_total
        self.make = make
        self.duty_cycle = duty_cycle
        self.id = id
        self.memory_used = memory_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.model is not None:
            result['Model'] = self.model
        if self.memory_total is not None:
            result['MemoryTotal'] = self.memory_total
        if self.make is not None:
            result['Make'] = self.make
        if self.duty_cycle is not None:
            result['DutyCycle'] = self.duty_cycle
        if self.id is not None:
            result['Id'] = self.id
        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('MemoryTotal') is not None:
            self.memory_total = m.get('MemoryTotal')
        if m.get('Make') is not None:
            self.make = m.get('Make')
        if m.get('DutyCycle') is not None:
            self.duty_cycle = m.get('DutyCycle')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsCpuStatsCpuUsage(TeaModel):
    def __init__(
        self,
        user: int = None,
        per_cpu_usages: List[int] = None,
        total: int = None,
        system: int = None,
    ):
        self.user = user
        self.per_cpu_usages = per_cpu_usages
        self.total = total
        self.system = system

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user
        if self.per_cpu_usages is not None:
            result['PerCpuUsages'] = self.per_cpu_usages
        if self.total is not None:
            result['Total'] = self.total
        if self.system is not None:
            result['System'] = self.system
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('PerCpuUsages') is not None:
            self.per_cpu_usages = m.get('PerCpuUsages')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('System') is not None:
            self.system = m.get('System')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsCpuStatsCpuCFS(TeaModel):
    def __init__(
        self,
        throttled_time: int = None,
        periods: int = None,
        throttled_periods: int = None,
    ):
        self.throttled_time = throttled_time
        self.periods = periods
        self.throttled_periods = throttled_periods

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.throttled_time is not None:
            result['ThrottledTime'] = self.throttled_time
        if self.periods is not None:
            result['Periods'] = self.periods
        if self.throttled_periods is not None:
            result['ThrottledPeriods'] = self.throttled_periods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThrottledTime') is not None:
            self.throttled_time = m.get('ThrottledTime')
        if m.get('Periods') is not None:
            self.periods = m.get('Periods')
        if m.get('ThrottledPeriods') is not None:
            self.throttled_periods = m.get('ThrottledPeriods')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsCpuStats(TeaModel):
    def __init__(
        self,
        cpu_usage: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsCpuStatsCpuUsage = None,
        load_average: int = None,
        cpu_cfs: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsCpuStatsCpuCFS = None,
    ):
        self.cpu_usage = cpu_usage
        self.load_average = load_average
        self.cpu_cfs = cpu_cfs

    def validate(self):
        if self.cpu_usage:
            self.cpu_usage.validate()
        if self.cpu_cfs:
            self.cpu_cfs.validate()

    def to_map(self):
        result = dict()
        if self.cpu_usage is not None:
            result['CpuUsage'] = self.cpu_usage.to_map()
        if self.load_average is not None:
            result['LoadAverage'] = self.load_average
        if self.cpu_cfs is not None:
            result['CpuCFS'] = self.cpu_cfs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuUsage') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsCpuStatsCpuUsage()
            self.cpu_usage = temp_model.from_map(m['CpuUsage'])
        if m.get('LoadAverage') is not None:
            self.load_average = m.get('LoadAverage')
        if m.get('CpuCFS') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsCpuStatsCpuCFS()
            self.cpu_cfs = temp_model.from_map(m['CpuCFS'])
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsMemoryStatsHierarchicalData(TeaModel):
    def __init__(
        self,
        pgmaj_fault: int = None,
        pg_fault: int = None,
    ):
        self.pgmaj_fault = pgmaj_fault
        self.pg_fault = pg_fault

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pgmaj_fault is not None:
            result['PgmajFault'] = self.pgmaj_fault
        if self.pg_fault is not None:
            result['PgFault'] = self.pg_fault
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PgmajFault') is not None:
            self.pgmaj_fault = m.get('PgmajFault')
        if m.get('PgFault') is not None:
            self.pg_fault = m.get('PgFault')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsMemoryStatsContainerData(TeaModel):
    def __init__(
        self,
        pgmaj_fault: int = None,
        pg_fault: int = None,
    ):
        self.pgmaj_fault = pgmaj_fault
        self.pg_fault = pg_fault

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pgmaj_fault is not None:
            result['PgmajFault'] = self.pgmaj_fault
        if self.pg_fault is not None:
            result['PgFault'] = self.pg_fault
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PgmajFault') is not None:
            self.pgmaj_fault = m.get('PgmajFault')
        if m.get('PgFault') is not None:
            self.pg_fault = m.get('PgFault')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsMemoryStats(TeaModel):
    def __init__(
        self,
        fail_cnt: int = None,
        max_usage: int = None,
        hierarchical_data: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsMemoryStatsHierarchicalData = None,
        rss: int = None,
        container_data: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsMemoryStatsContainerData = None,
        working_set: int = None,
        swap: int = None,
        cache: int = None,
        usage: int = None,
    ):
        self.fail_cnt = fail_cnt
        self.max_usage = max_usage
        self.hierarchical_data = hierarchical_data
        self.rss = rss
        self.container_data = container_data
        self.working_set = working_set
        self.swap = swap
        self.cache = cache
        self.usage = usage

    def validate(self):
        if self.hierarchical_data:
            self.hierarchical_data.validate()
        if self.container_data:
            self.container_data.validate()

    def to_map(self):
        result = dict()
        if self.fail_cnt is not None:
            result['FailCnt'] = self.fail_cnt
        if self.max_usage is not None:
            result['MaxUsage'] = self.max_usage
        if self.hierarchical_data is not None:
            result['HierarchicalData'] = self.hierarchical_data.to_map()
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.container_data is not None:
            result['ContainerData'] = self.container_data.to_map()
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        if self.swap is not None:
            result['Swap'] = self.swap
        if self.cache is not None:
            result['Cache'] = self.cache
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCnt') is not None:
            self.fail_cnt = m.get('FailCnt')
        if m.get('MaxUsage') is not None:
            self.max_usage = m.get('MaxUsage')
        if m.get('HierarchicalData') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsMemoryStatsHierarchicalData()
            self.hierarchical_data = temp_model.from_map(m['HierarchicalData'])
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('ContainerData') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsMemoryStatsContainerData()
            self.container_data = temp_model.from_map(m['ContainerData'])
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        if m.get('Swap') is not None:
            self.swap = m.get('Swap')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsTaskStats(TeaModel):
    def __init__(
        self,
        nr_uninterruptible: int = None,
        nr_running: int = None,
        nr_sleeping: int = None,
        nr_io_wait: int = None,
        nr_stopped: int = None,
    ):
        self.nr_uninterruptible = nr_uninterruptible
        self.nr_running = nr_running
        self.nr_sleeping = nr_sleeping
        self.nr_io_wait = nr_io_wait
        self.nr_stopped = nr_stopped

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.nr_uninterruptible is not None:
            result['NrUninterruptible'] = self.nr_uninterruptible
        if self.nr_running is not None:
            result['NrRunning'] = self.nr_running
        if self.nr_sleeping is not None:
            result['NrSleeping'] = self.nr_sleeping
        if self.nr_io_wait is not None:
            result['NrIoWait'] = self.nr_io_wait
        if self.nr_stopped is not None:
            result['NrStopped'] = self.nr_stopped
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NrUninterruptible') is not None:
            self.nr_uninterruptible = m.get('NrUninterruptible')
        if m.get('NrRunning') is not None:
            self.nr_running = m.get('NrRunning')
        if m.get('NrSleeping') is not None:
            self.nr_sleeping = m.get('NrSleeping')
        if m.get('NrIoWait') is not None:
            self.nr_io_wait = m.get('NrIoWait')
        if m.get('NrStopped') is not None:
            self.nr_stopped = m.get('NrStopped')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsDiskIoStatsIoServiced(TeaModel):
    def __init__(
        self,
        stats: str = None,
        minor: int = None,
        major: int = None,
        device: str = None,
    ):
        self.stats = stats
        self.minor = minor
        self.major = major
        self.device = device

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stats is not None:
            result['Stats'] = self.stats
        if self.minor is not None:
            result['Minor'] = self.minor
        if self.major is not None:
            result['Major'] = self.major
        if self.device is not None:
            result['Device'] = self.device
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stats') is not None:
            self.stats = m.get('Stats')
        if m.get('Minor') is not None:
            self.minor = m.get('Minor')
        if m.get('Major') is not None:
            self.major = m.get('Major')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsDiskIoStatsIoServiceTime(TeaModel):
    def __init__(
        self,
        stats: str = None,
        minor: int = None,
        major: int = None,
        device: str = None,
    ):
        self.stats = stats
        self.minor = minor
        self.major = major
        self.device = device

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stats is not None:
            result['Stats'] = self.stats
        if self.minor is not None:
            result['Minor'] = self.minor
        if self.major is not None:
            result['Major'] = self.major
        if self.device is not None:
            result['Device'] = self.device
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stats') is not None:
            self.stats = m.get('Stats')
        if m.get('Minor') is not None:
            self.minor = m.get('Minor')
        if m.get('Major') is not None:
            self.major = m.get('Major')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsDiskIoStats(TeaModel):
    def __init__(
        self,
        io_serviced: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsDiskIoStatsIoServiced] = None,
        io_service_time: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsDiskIoStatsIoServiceTime] = None,
    ):
        self.io_serviced = io_serviced
        self.io_service_time = io_service_time

    def validate(self):
        if self.io_serviced:
            for k in self.io_serviced:
                if k:
                    k.validate()
        if self.io_service_time:
            for k in self.io_service_time:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['IoServiced'] = []
        if self.io_serviced is not None:
            for k in self.io_serviced:
                result['IoServiced'].append(k.to_map() if k else None)
        result['IoServiceTime'] = []
        if self.io_service_time is not None:
            for k in self.io_service_time:
                result['IoServiceTime'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.io_serviced = []
        if m.get('IoServiced') is not None:
            for k in m.get('IoServiced'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsDiskIoStatsIoServiced()
                self.io_serviced.append(temp_model.from_map(k))
        self.io_service_time = []
        if m.get('IoServiceTime') is not None:
            for k in m.get('IoServiceTime'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsDiskIoStatsIoServiceTime()
                self.io_service_time.append(temp_model.from_map(k))
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStats(TeaModel):
    def __init__(
        self,
        network_stats: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStats = None,
        fs_stats: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsFsStats] = None,
        accelerator_stats: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsAcceleratorStats] = None,
        cpu_stats: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsCpuStats = None,
        timestamp: str = None,
        memory_stats: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsMemoryStats = None,
        task_stats: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsTaskStats = None,
        disk_io_stats: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsDiskIoStats = None,
    ):
        self.network_stats = network_stats
        self.fs_stats = fs_stats
        self.accelerator_stats = accelerator_stats
        self.cpu_stats = cpu_stats
        self.timestamp = timestamp
        self.memory_stats = memory_stats
        self.task_stats = task_stats
        self.disk_io_stats = disk_io_stats

    def validate(self):
        if self.network_stats:
            self.network_stats.validate()
        if self.fs_stats:
            for k in self.fs_stats:
                if k:
                    k.validate()
        if self.accelerator_stats:
            for k in self.accelerator_stats:
                if k:
                    k.validate()
        if self.cpu_stats:
            self.cpu_stats.validate()
        if self.memory_stats:
            self.memory_stats.validate()
        if self.task_stats:
            self.task_stats.validate()
        if self.disk_io_stats:
            self.disk_io_stats.validate()

    def to_map(self):
        result = dict()
        if self.network_stats is not None:
            result['NetworkStats'] = self.network_stats.to_map()
        result['FsStats'] = []
        if self.fs_stats is not None:
            for k in self.fs_stats:
                result['FsStats'].append(k.to_map() if k else None)
        result['AcceleratorStats'] = []
        if self.accelerator_stats is not None:
            for k in self.accelerator_stats:
                result['AcceleratorStats'].append(k.to_map() if k else None)
        if self.cpu_stats is not None:
            result['CpuStats'] = self.cpu_stats.to_map()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.memory_stats is not None:
            result['MemoryStats'] = self.memory_stats.to_map()
        if self.task_stats is not None:
            result['TaskStats'] = self.task_stats.to_map()
        if self.disk_io_stats is not None:
            result['DiskIoStats'] = self.disk_io_stats.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkStats') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsNetworkStats()
            self.network_stats = temp_model.from_map(m['NetworkStats'])
        self.fs_stats = []
        if m.get('FsStats') is not None:
            for k in m.get('FsStats'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsFsStats()
                self.fs_stats.append(temp_model.from_map(k))
        self.accelerator_stats = []
        if m.get('AcceleratorStats') is not None:
            for k in m.get('AcceleratorStats'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsAcceleratorStats()
                self.accelerator_stats.append(temp_model.from_map(k))
        if m.get('CpuStats') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsCpuStats()
            self.cpu_stats = temp_model.from_map(m['CpuStats'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('MemoryStats') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsMemoryStats()
            self.memory_stats = temp_model.from_map(m['MemoryStats'])
        if m.get('TaskStats') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsTaskStats()
            self.task_stats = temp_model.from_map(m['TaskStats'])
        if m.get('DiskIoStats') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStatsDiskIoStats()
            self.disk_io_stats = temp_model.from_map(m['DiskIoStats'])
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfos(TeaModel):
    def __init__(
        self,
        aliases: List[str] = None,
        container_spec: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerSpec = None,
        container_stats: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStats] = None,
    ):
        self.aliases = aliases
        self.container_spec = container_spec
        self.container_stats = container_stats

    def validate(self):
        if self.container_spec:
            self.container_spec.validate()
        if self.container_stats:
            for k in self.container_stats:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.aliases is not None:
            result['Aliases'] = self.aliases
        if self.container_spec is not None:
            result['ContainerSpec'] = self.container_spec.to_map()
        result['ContainerStats'] = []
        if self.container_stats is not None:
            for k in self.container_stats:
                result['ContainerStats'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliases') is not None:
            self.aliases = m.get('Aliases')
        if m.get('ContainerSpec') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerSpec()
            self.container_spec = temp_model.from_map(m['ContainerSpec'])
        self.container_stats = []
        if m.get('ContainerStats') is not None:
            for k in m.get('ContainerStats'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfosContainerStats()
                self.container_stats.append(temp_model.from_map(k))
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatas(TeaModel):
    def __init__(
        self,
        records: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecords] = None,
        container_infos: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfos] = None,
    ):
        self.records = records
        self.container_infos = container_infos

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()
        if self.container_infos:
            for k in self.container_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        result['ContainerInfos'] = []
        if self.container_infos is not None:
            for k in self.container_infos:
                result['ContainerInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecords()
                self.records.append(temp_model.from_map(k))
        self.container_infos = []
        if m.get('ContainerInfos') is not None:
            for k in m.get('ContainerInfos'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasContainerInfos()
                self.container_infos.append(temp_model.from_map(k))
        return self


class DescribeMultiContainerGroupMetricResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        monitor_datas: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatas] = None,
    ):
        self.request_id = request_id
        self.monitor_datas = monitor_datas

    def validate(self):
        if self.monitor_datas:
            for k in self.monitor_datas:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MonitorDatas'] = []
        if self.monitor_datas is not None:
            for k in self.monitor_datas:
                result['MonitorDatas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.monitor_datas = []
        if m.get('MonitorDatas') is not None:
            for k in m.get('MonitorDatas'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatas()
                self.monitor_datas.append(temp_model.from_map(k))
        return self


class DescribeMultiContainerGroupMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMultiContainerGroupMetricResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeMultiContainerGroupMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        zones: List[str] = None,
        recommend_zones: List[str] = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.zones = zones
        self.recommend_zones = recommend_zones
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.zones is not None:
            result['Zones'] = self.zones
        if self.recommend_zones is not None:
            result['RecommendZones'] = self.recommend_zones
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        if m.get('RecommendZones') is not None:
            self.recommend_zones = m.get('RecommendZones')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecContainerCommandRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        container_group_id: str = None,
        container_name: str = None,
        command: str = None,
        tty: bool = None,
        stdin: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.container_group_id = container_group_id
        self.container_name = container_name
        self.command = command
        self.tty = tty
        self.stdin = stdin

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.command is not None:
            result['Command'] = self.command
        if self.tty is not None:
            result['TTY'] = self.tty
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('TTY') is not None:
            self.tty = m.get('TTY')
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        return self


class ExecContainerCommandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        web_socket_uri: str = None,
    ):
        self.request_id = request_id
        self.web_socket_uri = web_socket_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.web_socket_uri is not None:
            result['WebSocketUri'] = self.web_socket_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WebSocketUri') is not None:
            self.web_socket_uri = m.get('WebSocketUri')
        return self


class ExecContainerCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecContainerCommandResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ExecContainerCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsageRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListUsageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        attributes: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.attributes = attributes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        return self


class ListUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUsageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartContainerGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        container_group_id: str = None,
        client_token: str = None,
        vk_client_version: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.container_group_id = container_group_id
        self.client_token = client_token
        self.vk_client_version = vk_client_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.vk_client_version is not None:
            result['VkClientVersion'] = self.vk_client_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('VkClientVersion') is not None:
            self.vk_client_version = m.get('VkClientVersion')
        return self


class RestartContainerGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartContainerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartContainerGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RestartContainerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateContainerGroupRequestDnsConfigOption(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateContainerGroupRequestDnsConfig(TeaModel):
    def __init__(
        self,
        name_server: List[str] = None,
        search: List[str] = None,
        option: List[UpdateContainerGroupRequestDnsConfigOption] = None,
    ):
        self.name_server = name_server
        self.search = search
        self.option = option

    def validate(self):
        if self.option:
            for k in self.option:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.name_server is not None:
            result['NameServer'] = self.name_server
        if self.search is not None:
            result['Search'] = self.search
        result['Option'] = []
        if self.option is not None:
            for k in self.option:
                result['Option'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameServer') is not None:
            self.name_server = m.get('NameServer')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        self.option = []
        if m.get('Option') is not None:
            for k in m.get('Option'):
                temp_model = UpdateContainerGroupRequestDnsConfigOption()
                self.option.append(temp_model.from_map(k))
        return self


class UpdateContainerGroupRequestTag(TeaModel):
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


class UpdateContainerGroupRequestVolumeNFSVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        server: str = None,
        read_only: bool = None,
    ):
        self.path = path
        self.server = server
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.server is not None:
            result['Server'] = self.server
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        return self


class UpdateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath(TeaModel):
    def __init__(
        self,
        path: str = None,
        content: str = None,
    ):
        self.path = path
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class UpdateContainerGroupRequestVolumeConfigFileVolume(TeaModel):
    def __init__(
        self,
        config_file_to_path: List[UpdateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath] = None,
    ):
        self.config_file_to_path = config_file_to_path

    def validate(self):
        if self.config_file_to_path:
            for k in self.config_file_to_path:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConfigFileToPath'] = []
        if self.config_file_to_path is not None:
            for k in self.config_file_to_path:
                result['ConfigFileToPath'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_file_to_path = []
        if m.get('ConfigFileToPath') is not None:
            for k in m.get('ConfigFileToPath'):
                temp_model = UpdateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath()
                self.config_file_to_path.append(temp_model.from_map(k))
        return self


class UpdateContainerGroupRequestVolumeEmptyDirVolume(TeaModel):
    def __init__(
        self,
        medium: str = None,
    ):
        self.medium = medium

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.medium is not None:
            result['Medium'] = self.medium
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        return self


class UpdateContainerGroupRequestVolume(TeaModel):
    def __init__(
        self,
        nfsvolume: UpdateContainerGroupRequestVolumeNFSVolume = None,
        config_file_volume: UpdateContainerGroupRequestVolumeConfigFileVolume = None,
        empty_dir_volume: UpdateContainerGroupRequestVolumeEmptyDirVolume = None,
        type: str = None,
        name: str = None,
    ):
        self.nfsvolume = nfsvolume
        self.config_file_volume = config_file_volume
        self.empty_dir_volume = empty_dir_volume
        self.type = type
        self.name = name

    def validate(self):
        self.validate_required(self.nfsvolume, 'nfsvolume')
        if self.nfsvolume:
            self.nfsvolume.validate()
        self.validate_required(self.config_file_volume, 'config_file_volume')
        if self.config_file_volume:
            self.config_file_volume.validate()
        self.validate_required(self.empty_dir_volume, 'empty_dir_volume')
        if self.empty_dir_volume:
            self.empty_dir_volume.validate()

    def to_map(self):
        result = dict()
        if self.nfsvolume is not None:
            result['NFSVolume'] = self.nfsvolume.to_map()
        if self.config_file_volume is not None:
            result['ConfigFileVolume'] = self.config_file_volume.to_map()
        if self.empty_dir_volume is not None:
            result['EmptyDirVolume'] = self.empty_dir_volume.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NFSVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeNFSVolume()
            self.nfsvolume = temp_model.from_map(m['NFSVolume'])
        if m.get('ConfigFileVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeConfigFileVolume()
            self.config_file_volume = temp_model.from_map(m['ConfigFileVolume'])
        if m.get('EmptyDirVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeEmptyDirVolume()
            self.empty_dir_volume = temp_model.from_map(m['EmptyDirVolume'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateContainerGroupRequestContainerReadinessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class UpdateContainerGroupRequestContainerReadinessProbeHttpGet(TeaModel):
    def __init__(
        self,
        scheme: str = None,
        path: str = None,
        port: int = None,
    ):
        self.scheme = scheme
        self.path = path
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class UpdateContainerGroupRequestContainerReadinessProbeExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class UpdateContainerGroupRequestContainerReadinessProbe(TeaModel):
    def __init__(
        self,
        timeout_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: UpdateContainerGroupRequestContainerReadinessProbeTcpSocket = None,
        http_get: UpdateContainerGroupRequestContainerReadinessProbeHttpGet = None,
        period_seconds: int = None,
        initial_delay_seconds: int = None,
        exec: UpdateContainerGroupRequestContainerReadinessProbeExec = None,
        failure_threshold: int = None,
    ):
        self.timeout_seconds = timeout_seconds
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
        self.http_get = http_get
        self.period_seconds = period_seconds
        self.initial_delay_seconds = initial_delay_seconds
        self.exec = exec
        self.failure_threshold = failure_threshold

    def validate(self):
        self.validate_required(self.tcp_socket, 'tcp_socket')
        if self.tcp_socket:
            self.tcp_socket.validate()
        self.validate_required(self.http_get, 'http_get')
        if self.http_get:
            self.http_get.validate()
        self.validate_required(self.exec, 'exec')
        if self.exec:
            self.exec.validate()

    def to_map(self):
        result = dict()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = UpdateContainerGroupRequestContainerReadinessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('HttpGet') is not None:
            temp_model = UpdateContainerGroupRequestContainerReadinessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('Exec') is not None:
            temp_model = UpdateContainerGroupRequestContainerReadinessProbeExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        return self


class UpdateContainerGroupRequestContainerSecurityContextCapability(TeaModel):
    def __init__(
        self,
        add: List[str] = None,
    ):
        self.add = add

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class UpdateContainerGroupRequestContainerSecurityContext(TeaModel):
    def __init__(
        self,
        capability: UpdateContainerGroupRequestContainerSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user

    def validate(self):
        self.validate_required(self.capability, 'capability')
        if self.capability:
            self.capability.validate()

    def to_map(self):
        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = UpdateContainerGroupRequestContainerSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class UpdateContainerGroupRequestContainerLivenessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class UpdateContainerGroupRequestContainerLivenessProbeExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class UpdateContainerGroupRequestContainerLivenessProbeHttpGet(TeaModel):
    def __init__(
        self,
        scheme: str = None,
        port: int = None,
        path: str = None,
    ):
        self.scheme = scheme
        self.port = port
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.port is not None:
            result['Port'] = self.port
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class UpdateContainerGroupRequestContainerLivenessProbe(TeaModel):
    def __init__(
        self,
        period_seconds: int = None,
        tcp_socket: UpdateContainerGroupRequestContainerLivenessProbeTcpSocket = None,
        initial_delay_seconds: int = None,
        success_threshold: int = None,
        exec: UpdateContainerGroupRequestContainerLivenessProbeExec = None,
        http_get: UpdateContainerGroupRequestContainerLivenessProbeHttpGet = None,
        failure_threshold: int = None,
        timeout_seconds: int = None,
    ):
        self.period_seconds = period_seconds
        self.tcp_socket = tcp_socket
        self.initial_delay_seconds = initial_delay_seconds
        self.success_threshold = success_threshold
        self.exec = exec
        self.http_get = http_get
        self.failure_threshold = failure_threshold
        self.timeout_seconds = timeout_seconds

    def validate(self):
        self.validate_required(self.tcp_socket, 'tcp_socket')
        if self.tcp_socket:
            self.tcp_socket.validate()
        self.validate_required(self.exec, 'exec')
        if self.exec:
            self.exec.validate()
        self.validate_required(self.http_get, 'http_get')
        if self.http_get:
            self.http_get.validate()

    def to_map(self):
        result = dict()
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('TcpSocket') is not None:
            temp_model = UpdateContainerGroupRequestContainerLivenessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('Exec') is not None:
            temp_model = UpdateContainerGroupRequestContainerLivenessProbeExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('HttpGet') is not None:
            temp_model = UpdateContainerGroupRequestContainerLivenessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class UpdateContainerGroupRequestContainerEnvironmentVarFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class UpdateContainerGroupRequestContainerEnvironmentVar(TeaModel):
    def __init__(
        self,
        field_ref: UpdateContainerGroupRequestContainerEnvironmentVarFieldRef = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref = field_ref
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.field_ref, 'field_ref')
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = UpdateContainerGroupRequestContainerEnvironmentVarFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateContainerGroupRequestContainerVolumeMount(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        read_only: bool = None,
        sub_path: str = None,
        name: str = None,
    ):
        self.mount_path = mount_path
        self.read_only = read_only
        self.sub_path = sub_path
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateContainerGroupRequestContainerPort(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        port: int = None,
    ):
        self.protocol = protocol
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class UpdateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeaders(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateContainerGroupRequestContainer(TeaModel):
    def __init__(
        self,
        readiness_probe: UpdateContainerGroupRequestContainerReadinessProbe = None,
        security_context: UpdateContainerGroupRequestContainerSecurityContext = None,
        liveness_probe: UpdateContainerGroupRequestContainerLivenessProbe = None,
        environment_var: List[UpdateContainerGroupRequestContainerEnvironmentVar] = None,
        tty: bool = None,
        working_dir: str = None,
        arg: List[str] = None,
        stdin: bool = None,
        volume_mount: List[UpdateContainerGroupRequestContainerVolumeMount] = None,
        image_pull_policy: str = None,
        stdin_once: bool = None,
        lifecycle_pre_stop_handler_tcp_socket_port: int = None,
        lifecycle_post_start_handler_http_get_scheme: str = None,
        command: List[str] = None,
        lifecycle_post_start_handler_http_get_host: str = None,
        lifecycle_post_start_handler_tcp_socket_port: int = None,
        lifecycle_post_start_handler_http_get_path: str = None,
        lifecycle_post_start_handler_exec: List[str] = None,
        lifecycle_pre_stop_handler_http_get_path: str = None,
        port: List[UpdateContainerGroupRequestContainerPort] = None,
        lifecycle_pre_stop_handler_http_get_scheme: str = None,
        lifecycle_post_start_handler_http_get_http_headers: List[UpdateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeaders] = None,
        lifecycle_post_start_handler_tcp_socket_host: str = None,
        gpu: int = None,
        lifecycle_pre_stop_handler_exec: List[str] = None,
        memory: float = None,
        name: str = None,
        lifecycle_pre_stop_handler_http_get_host: str = None,
        lifecycle_pre_stop_handler_tcp_socket_host: str = None,
        image: str = None,
        lifecycle_pre_stop_handler_http_get_port: int = None,
        lifecycle_pre_stop_handler_http_get_http_header: List[UpdateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader] = None,
        cpu: float = None,
        lifecycle_post_start_handler_http_get_port: int = None,
    ):
        self.readiness_probe = readiness_probe
        self.security_context = security_context
        self.liveness_probe = liveness_probe
        self.environment_var = environment_var
        self.tty = tty
        self.working_dir = working_dir
        self.arg = arg
        self.stdin = stdin
        self.volume_mount = volume_mount
        self.image_pull_policy = image_pull_policy
        self.stdin_once = stdin_once
        self.lifecycle_pre_stop_handler_tcp_socket_port = lifecycle_pre_stop_handler_tcp_socket_port
        self.lifecycle_post_start_handler_http_get_scheme = lifecycle_post_start_handler_http_get_scheme
        self.command = command
        self.lifecycle_post_start_handler_http_get_host = lifecycle_post_start_handler_http_get_host
        self.lifecycle_post_start_handler_tcp_socket_port = lifecycle_post_start_handler_tcp_socket_port
        self.lifecycle_post_start_handler_http_get_path = lifecycle_post_start_handler_http_get_path
        self.lifecycle_post_start_handler_exec = lifecycle_post_start_handler_exec
        self.lifecycle_pre_stop_handler_http_get_path = lifecycle_pre_stop_handler_http_get_path
        self.port = port
        self.lifecycle_pre_stop_handler_http_get_scheme = lifecycle_pre_stop_handler_http_get_scheme
        self.lifecycle_post_start_handler_http_get_http_headers = lifecycle_post_start_handler_http_get_http_headers
        self.lifecycle_post_start_handler_tcp_socket_host = lifecycle_post_start_handler_tcp_socket_host
        self.gpu = gpu
        self.lifecycle_pre_stop_handler_exec = lifecycle_pre_stop_handler_exec
        self.memory = memory
        self.name = name
        self.lifecycle_pre_stop_handler_http_get_host = lifecycle_pre_stop_handler_http_get_host
        self.lifecycle_pre_stop_handler_tcp_socket_host = lifecycle_pre_stop_handler_tcp_socket_host
        self.image = image
        self.lifecycle_pre_stop_handler_http_get_port = lifecycle_pre_stop_handler_http_get_port
        self.lifecycle_pre_stop_handler_http_get_http_header = lifecycle_pre_stop_handler_http_get_http_header
        self.cpu = cpu
        self.lifecycle_post_start_handler_http_get_port = lifecycle_post_start_handler_http_get_port

    def validate(self):
        self.validate_required(self.readiness_probe, 'readiness_probe')
        if self.readiness_probe:
            self.readiness_probe.validate()
        self.validate_required(self.security_context, 'security_context')
        if self.security_context:
            self.security_context.validate()
        self.validate_required(self.liveness_probe, 'liveness_probe')
        if self.liveness_probe:
            self.liveness_probe.validate()
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()
        if self.port:
            for k in self.port:
                if k:
                    k.validate()
        if self.lifecycle_post_start_handler_http_get_http_headers:
            for k in self.lifecycle_post_start_handler_http_get_http_headers:
                if k:
                    k.validate()
        if self.lifecycle_pre_stop_handler_http_get_http_header:
            for k in self.lifecycle_pre_stop_handler_http_get_http_header:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.readiness_probe is not None:
            result['ReadinessProbe'] = self.readiness_probe.to_map()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.tty is not None:
            result['Tty'] = self.tty
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.lifecycle_pre_stop_handler_tcp_socket_port is not None:
            result['LifecyclePreStopHandlerTcpSocketPort'] = self.lifecycle_pre_stop_handler_tcp_socket_port
        if self.lifecycle_post_start_handler_http_get_scheme is not None:
            result['LifecyclePostStartHandlerHttpGetScheme'] = self.lifecycle_post_start_handler_http_get_scheme
        if self.command is not None:
            result['Command'] = self.command
        if self.lifecycle_post_start_handler_http_get_host is not None:
            result['LifecyclePostStartHandlerHttpGetHost'] = self.lifecycle_post_start_handler_http_get_host
        if self.lifecycle_post_start_handler_tcp_socket_port is not None:
            result['LifecyclePostStartHandlerTcpSocketPort'] = self.lifecycle_post_start_handler_tcp_socket_port
        if self.lifecycle_post_start_handler_http_get_path is not None:
            result['LifecyclePostStartHandlerHttpGetPath'] = self.lifecycle_post_start_handler_http_get_path
        if self.lifecycle_post_start_handler_exec is not None:
            result['LifecyclePostStartHandlerExec'] = self.lifecycle_post_start_handler_exec
        if self.lifecycle_pre_stop_handler_http_get_path is not None:
            result['LifecyclePreStopHandlerHttpGetPath'] = self.lifecycle_pre_stop_handler_http_get_path
        result['Port'] = []
        if self.port is not None:
            for k in self.port:
                result['Port'].append(k.to_map() if k else None)
        if self.lifecycle_pre_stop_handler_http_get_scheme is not None:
            result['LifecyclePreStopHandlerHttpGetScheme'] = self.lifecycle_pre_stop_handler_http_get_scheme
        result['LifecyclePostStartHandlerHttpGetHttpHeaders'] = []
        if self.lifecycle_post_start_handler_http_get_http_headers is not None:
            for k in self.lifecycle_post_start_handler_http_get_http_headers:
                result['LifecyclePostStartHandlerHttpGetHttpHeaders'].append(k.to_map() if k else None)
        if self.lifecycle_post_start_handler_tcp_socket_host is not None:
            result['LifecyclePostStartHandlerTcpSocketHost'] = self.lifecycle_post_start_handler_tcp_socket_host
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.lifecycle_pre_stop_handler_exec is not None:
            result['LifecyclePreStopHandlerExec'] = self.lifecycle_pre_stop_handler_exec
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        if self.lifecycle_pre_stop_handler_http_get_host is not None:
            result['LifecyclePreStopHandlerHttpGetHost'] = self.lifecycle_pre_stop_handler_http_get_host
        if self.lifecycle_pre_stop_handler_tcp_socket_host is not None:
            result['LifecyclePreStopHandlerTcpSocketHost'] = self.lifecycle_pre_stop_handler_tcp_socket_host
        if self.image is not None:
            result['Image'] = self.image
        if self.lifecycle_pre_stop_handler_http_get_port is not None:
            result['LifecyclePreStopHandlerHttpGetPort'] = self.lifecycle_pre_stop_handler_http_get_port
        result['LifecyclePreStopHandlerHttpGetHttpHeader'] = []
        if self.lifecycle_pre_stop_handler_http_get_http_header is not None:
            for k in self.lifecycle_pre_stop_handler_http_get_http_header:
                result['LifecyclePreStopHandlerHttpGetHttpHeader'].append(k.to_map() if k else None)
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.lifecycle_post_start_handler_http_get_port is not None:
            result['LifecyclePostStartHandlerHttpGetPort'] = self.lifecycle_post_start_handler_http_get_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReadinessProbe') is not None:
            temp_model = UpdateContainerGroupRequestContainerReadinessProbe()
            self.readiness_probe = temp_model.from_map(m['ReadinessProbe'])
        if m.get('SecurityContext') is not None:
            temp_model = UpdateContainerGroupRequestContainerSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('LivenessProbe') is not None:
            temp_model = UpdateContainerGroupRequestContainerLivenessProbe()
            self.liveness_probe = temp_model.from_map(m['LivenessProbe'])
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = UpdateContainerGroupRequestContainerEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = UpdateContainerGroupRequestContainerVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('LifecyclePreStopHandlerTcpSocketPort') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_port = m.get('LifecyclePreStopHandlerTcpSocketPort')
        if m.get('LifecyclePostStartHandlerHttpGetScheme') is not None:
            self.lifecycle_post_start_handler_http_get_scheme = m.get('LifecyclePostStartHandlerHttpGetScheme')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('LifecyclePostStartHandlerHttpGetHost') is not None:
            self.lifecycle_post_start_handler_http_get_host = m.get('LifecyclePostStartHandlerHttpGetHost')
        if m.get('LifecyclePostStartHandlerTcpSocketPort') is not None:
            self.lifecycle_post_start_handler_tcp_socket_port = m.get('LifecyclePostStartHandlerTcpSocketPort')
        if m.get('LifecyclePostStartHandlerHttpGetPath') is not None:
            self.lifecycle_post_start_handler_http_get_path = m.get('LifecyclePostStartHandlerHttpGetPath')
        if m.get('LifecyclePostStartHandlerExec') is not None:
            self.lifecycle_post_start_handler_exec = m.get('LifecyclePostStartHandlerExec')
        if m.get('LifecyclePreStopHandlerHttpGetPath') is not None:
            self.lifecycle_pre_stop_handler_http_get_path = m.get('LifecyclePreStopHandlerHttpGetPath')
        self.port = []
        if m.get('Port') is not None:
            for k in m.get('Port'):
                temp_model = UpdateContainerGroupRequestContainerPort()
                self.port.append(temp_model.from_map(k))
        if m.get('LifecyclePreStopHandlerHttpGetScheme') is not None:
            self.lifecycle_pre_stop_handler_http_get_scheme = m.get('LifecyclePreStopHandlerHttpGetScheme')
        self.lifecycle_post_start_handler_http_get_http_headers = []
        if m.get('LifecyclePostStartHandlerHttpGetHttpHeaders') is not None:
            for k in m.get('LifecyclePostStartHandlerHttpGetHttpHeaders'):
                temp_model = UpdateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeaders()
                self.lifecycle_post_start_handler_http_get_http_headers.append(temp_model.from_map(k))
        if m.get('LifecyclePostStartHandlerTcpSocketHost') is not None:
            self.lifecycle_post_start_handler_tcp_socket_host = m.get('LifecyclePostStartHandlerTcpSocketHost')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('LifecyclePreStopHandlerExec') is not None:
            self.lifecycle_pre_stop_handler_exec = m.get('LifecyclePreStopHandlerExec')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LifecyclePreStopHandlerHttpGetHost') is not None:
            self.lifecycle_pre_stop_handler_http_get_host = m.get('LifecyclePreStopHandlerHttpGetHost')
        if m.get('LifecyclePreStopHandlerTcpSocketHost') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_host = m.get('LifecyclePreStopHandlerTcpSocketHost')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('LifecyclePreStopHandlerHttpGetPort') is not None:
            self.lifecycle_pre_stop_handler_http_get_port = m.get('LifecyclePreStopHandlerHttpGetPort')
        self.lifecycle_pre_stop_handler_http_get_http_header = []
        if m.get('LifecyclePreStopHandlerHttpGetHttpHeader') is not None:
            for k in m.get('LifecyclePreStopHandlerHttpGetHttpHeader'):
                temp_model = UpdateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader()
                self.lifecycle_pre_stop_handler_http_get_http_header.append(temp_model.from_map(k))
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('LifecyclePostStartHandlerHttpGetPort') is not None:
            self.lifecycle_post_start_handler_http_get_port = m.get('LifecyclePostStartHandlerHttpGetPort')
        return self


class UpdateContainerGroupRequestInitContainerSecurityContextCapability(TeaModel):
    def __init__(
        self,
        add: List[str] = None,
    ):
        self.add = add

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class UpdateContainerGroupRequestInitContainerSecurityContext(TeaModel):
    def __init__(
        self,
        capability: UpdateContainerGroupRequestInitContainerSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user

    def validate(self):
        self.validate_required(self.capability, 'capability')
        if self.capability:
            self.capability.validate()

    def to_map(self):
        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = UpdateContainerGroupRequestInitContainerSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class UpdateContainerGroupRequestInitContainerVolumeMount(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        read_only: bool = None,
        sub_path: str = None,
        name: str = None,
    ):
        self.mount_path = mount_path
        self.read_only = read_only
        self.sub_path = sub_path
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateContainerGroupRequestInitContainerPort(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        port: int = None,
    ):
        self.protocol = protocol
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class UpdateContainerGroupRequestInitContainerEnvironmentVarFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class UpdateContainerGroupRequestInitContainerEnvironmentVar(TeaModel):
    def __init__(
        self,
        field_ref: UpdateContainerGroupRequestInitContainerEnvironmentVarFieldRef = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref = field_ref
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.field_ref, 'field_ref')
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = UpdateContainerGroupRequestInitContainerEnvironmentVarFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateContainerGroupRequestInitContainer(TeaModel):
    def __init__(
        self,
        security_context: UpdateContainerGroupRequestInitContainerSecurityContext = None,
        image: str = None,
        volume_mount: List[UpdateContainerGroupRequestInitContainerVolumeMount] = None,
        port: List[UpdateContainerGroupRequestInitContainerPort] = None,
        environment_var: List[UpdateContainerGroupRequestInitContainerEnvironmentVar] = None,
        image_pull_policy: str = None,
        stdin_once: bool = None,
        cpu: float = None,
        tty: bool = None,
        working_dir: str = None,
        command: List[str] = None,
        arg: List[str] = None,
        gpu: int = None,
        memory: float = None,
        stdin: bool = None,
        name: str = None,
    ):
        self.security_context = security_context
        self.image = image
        self.volume_mount = volume_mount
        self.port = port
        self.environment_var = environment_var
        self.image_pull_policy = image_pull_policy
        self.stdin_once = stdin_once
        self.cpu = cpu
        self.tty = tty
        self.working_dir = working_dir
        self.command = command
        self.arg = arg
        self.gpu = gpu
        self.memory = memory
        self.stdin = stdin
        self.name = name

    def validate(self):
        self.validate_required(self.security_context, 'security_context')
        if self.security_context:
            self.security_context.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()
        if self.port:
            for k in self.port:
                if k:
                    k.validate()
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.image is not None:
            result['Image'] = self.image
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        result['Port'] = []
        if self.port is not None:
            for k in self.port:
                result['Port'].append(k.to_map() if k else None)
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.tty is not None:
            result['Tty'] = self.tty
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.command is not None:
            result['Command'] = self.command
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityContext') is not None:
            temp_model = UpdateContainerGroupRequestInitContainerSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Image') is not None:
            self.image = m.get('Image')
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = UpdateContainerGroupRequestInitContainerVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        self.port = []
        if m.get('Port') is not None:
            for k in m.get('Port'):
                temp_model = UpdateContainerGroupRequestInitContainerPort()
                self.port.append(temp_model.from_map(k))
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = UpdateContainerGroupRequestInitContainerEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateContainerGroupRequestImageRegistryCredential(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.server = server
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class UpdateContainerGroupRequest(TeaModel):
    def __init__(
        self,
        dns_config: UpdateContainerGroupRequestDnsConfig = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        container_group_id: str = None,
        restart_policy: str = None,
        client_token: str = None,
        cpu: float = None,
        memory: float = None,
        tag: List[UpdateContainerGroupRequestTag] = None,
        volume: List[UpdateContainerGroupRequestVolume] = None,
        container: List[UpdateContainerGroupRequestContainer] = None,
        init_container: List[UpdateContainerGroupRequestInitContainer] = None,
        image_registry_credential: List[UpdateContainerGroupRequestImageRegistryCredential] = None,
    ):
        self.dns_config = dns_config
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.container_group_id = container_group_id
        self.restart_policy = restart_policy
        self.client_token = client_token
        self.cpu = cpu
        self.memory = memory
        self.tag = tag
        self.volume = volume
        self.container = container
        self.init_container = init_container
        self.image_registry_credential = image_registry_credential

    def validate(self):
        if self.dns_config:
            self.dns_config.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.volume:
            for k in self.volume:
                if k:
                    k.validate()
        if self.container:
            for k in self.container:
                if k:
                    k.validate()
        if self.init_container:
            for k in self.init_container:
                if k:
                    k.validate()
        if self.image_registry_credential:
            for k in self.image_registry_credential:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.dns_config is not None:
            result['DnsConfig'] = self.dns_config.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        result['Volume'] = []
        if self.volume is not None:
            for k in self.volume:
                result['Volume'].append(k.to_map() if k else None)
        result['Container'] = []
        if self.container is not None:
            for k in self.container:
                result['Container'].append(k.to_map() if k else None)
        result['InitContainer'] = []
        if self.init_container is not None:
            for k in self.init_container:
                result['InitContainer'].append(k.to_map() if k else None)
        result['ImageRegistryCredential'] = []
        if self.image_registry_credential is not None:
            for k in self.image_registry_credential:
                result['ImageRegistryCredential'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsConfig') is not None:
            temp_model = UpdateContainerGroupRequestDnsConfig()
            self.dns_config = temp_model.from_map(m['DnsConfig'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = UpdateContainerGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        self.volume = []
        if m.get('Volume') is not None:
            for k in m.get('Volume'):
                temp_model = UpdateContainerGroupRequestVolume()
                self.volume.append(temp_model.from_map(k))
        self.container = []
        if m.get('Container') is not None:
            for k in m.get('Container'):
                temp_model = UpdateContainerGroupRequestContainer()
                self.container.append(temp_model.from_map(k))
        self.init_container = []
        if m.get('InitContainer') is not None:
            for k in m.get('InitContainer'):
                temp_model = UpdateContainerGroupRequestInitContainer()
                self.init_container.append(temp_model.from_map(k))
        self.image_registry_credential = []
        if m.get('ImageRegistryCredential') is not None:
            for k in m.get('ImageRegistryCredential'):
                temp_model = UpdateContainerGroupRequestImageRegistryCredential()
                self.image_registry_credential.append(temp_model.from_map(k))
        return self


class UpdateContainerGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateContainerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateContainerGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateContainerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


