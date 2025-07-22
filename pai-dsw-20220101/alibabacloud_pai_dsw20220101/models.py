# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class BandwidthLimit(TeaModel):
    def __init__(
        self,
        egress_rate: str = None,
        egress_whitelists: List[str] = None,
        ingress_rate: str = None,
        ingress_whitelists: List[str] = None,
    ):
        self.egress_rate = egress_rate
        self.egress_whitelists = egress_whitelists
        self.ingress_rate = ingress_rate
        self.ingress_whitelists = ingress_whitelists

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.egress_rate is not None:
            result['EgressRate'] = self.egress_rate
        if self.egress_whitelists is not None:
            result['EgressWhitelists'] = self.egress_whitelists
        if self.ingress_rate is not None:
            result['IngressRate'] = self.ingress_rate
        if self.ingress_whitelists is not None:
            result['IngressWhitelists'] = self.ingress_whitelists
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressRate') is not None:
            self.egress_rate = m.get('EgressRate')
        if m.get('EgressWhitelists') is not None:
            self.egress_whitelists = m.get('EgressWhitelists')
        if m.get('IngressRate') is not None:
            self.ingress_rate = m.get('IngressRate')
        if m.get('IngressWhitelists') is not None:
            self.ingress_whitelists = m.get('IngressWhitelists')
        return self


class CredentialConfigConfigsRolesUserInfo(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        id: str = None,
        security_token: str = None,
        type: str = None,
    ):
        self.access_key_id = access_key_id
        self.id = id
        self.security_token = security_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.id is not None:
            result['Id'] = self.id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CredentialConfigConfigsRoles(TeaModel):
    def __init__(
        self,
        assume_role_for: str = None,
        policy: str = None,
        role_arn: str = None,
        role_type: str = None,
        user_info: CredentialConfigConfigsRolesUserInfo = None,
    ):
        self.assume_role_for = assume_role_for
        self.policy = policy
        # This parameter is required.
        self.role_arn = role_arn
        # This parameter is required.
        self.role_type = role_type
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('UserInfo') is not None:
            temp_model = CredentialConfigConfigsRolesUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CredentialConfigConfigs(TeaModel):
    def __init__(
        self,
        key: str = None,
        roles: List[CredentialConfigConfigsRoles] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.key = key
        self.roles = roles
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = CredentialConfigConfigsRoles()
                self.roles.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CredentialConfig(TeaModel):
    def __init__(
        self,
        aliyun_env_role_key: str = None,
        configs: List[CredentialConfigConfigs] = None,
        enable: bool = None,
    ):
        self.aliyun_env_role_key = aliyun_env_role_key
        self.configs = configs
        self.enable = enable

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_env_role_key is not None:
            result['AliyunEnvRoleKey'] = self.aliyun_env_role_key
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunEnvRoleKey') is not None:
            self.aliyun_env_role_key = m.get('AliyunEnvRoleKey')
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = CredentialConfigConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DemoCategory(TeaModel):
    def __init__(
        self,
        category_code: str = None,
        category_name: str = None,
        order: int = None,
        sub_categories: List['DemoCategory'] = None,
    ):
        self.category_code = category_code
        self.category_name = category_name
        self.order = order
        self.sub_categories = sub_categories

    def validate(self):
        if self.sub_categories:
            for k in self.sub_categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_code is not None:
            result['CategoryCode'] = self.category_code
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.order is not None:
            result['Order'] = self.order
        result['SubCategories'] = []
        if self.sub_categories is not None:
            for k in self.sub_categories:
                result['SubCategories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        self.sub_categories = []
        if m.get('SubCategories') is not None:
            for k in m.get('SubCategories'):
                temp_model = DemoCategory()
                self.sub_categories.append(temp_model.from_map(k))
        return self


class DynamicMountPoint(TeaModel):
    def __init__(
        self,
        options: str = None,
        root_path: str = None,
    ):
        self.options = options
        # This parameter is required.
        self.root_path = root_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.options is not None:
            result['Options'] = self.options
        if self.root_path is not None:
            result['RootPath'] = self.root_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('RootPath') is not None:
            self.root_path = m.get('RootPath')
        return self


class DynamicMount(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        mount_points: List[DynamicMountPoint] = None,
    ):
        self.enable = enable
        self.mount_points = mount_points

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        result['MountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['MountPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        self.mount_points = []
        if m.get('MountPoints') is not None:
            for k in m.get('MountPoints'):
                temp_model = DynamicMountPoint()
                self.mount_points.append(temp_model.from_map(k))
        return self


class ForwardInfo(TeaModel):
    def __init__(
        self,
        access_type: List[str] = None,
        container_name: str = None,
        eip_allocation_id: str = None,
        enable: bool = None,
        external_port: str = None,
        forward_port: str = None,
        name: str = None,
        nat_gateway_id: str = None,
        sshpublic_key: str = None,
    ):
        self.access_type = access_type
        self.container_name = container_name
        self.eip_allocation_id = eip_allocation_id
        self.enable = enable
        self.external_port = external_port
        self.forward_port = forward_port
        self.name = name
        self.nat_gateway_id = nat_gateway_id
        self.sshpublic_key = sshpublic_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.eip_allocation_id is not None:
            result['EipAllocationId'] = self.eip_allocation_id
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port
        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port
        if self.name is not None:
            result['Name'] = self.name
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.sshpublic_key is not None:
            result['SSHPublicKey'] = self.sshpublic_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('EipAllocationId') is not None:
            self.eip_allocation_id = m.get('EipAllocationId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')
        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('SSHPublicKey') is not None:
            self.sshpublic_key = m.get('SSHPublicKey')
        return self


class ForwardInfoResponseConnectInfoInternet(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        port: str = None,
    ):
        self.endpoint = endpoint
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ForwardInfoResponseConnectInfoIntranet(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        port: str = None,
    ):
        self.endpoint = endpoint
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ForwardInfoResponseConnectInfo(TeaModel):
    def __init__(
        self,
        internet: ForwardInfoResponseConnectInfoInternet = None,
        intranet: ForwardInfoResponseConnectInfoIntranet = None,
        message: str = None,
        phase: str = None,
    ):
        self.internet = internet
        self.intranet = intranet
        self.message = message
        self.phase = phase

    def validate(self):
        if self.internet:
            self.internet.validate()
        if self.intranet:
            self.intranet.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet is not None:
            result['Internet'] = self.internet.to_map()
        if self.intranet is not None:
            result['Intranet'] = self.intranet.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.phase is not None:
            result['Phase'] = self.phase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Internet') is not None:
            temp_model = ForwardInfoResponseConnectInfoInternet()
            self.internet = temp_model.from_map(m['Internet'])
        if m.get('Intranet') is not None:
            temp_model = ForwardInfoResponseConnectInfoIntranet()
            self.intranet = temp_model.from_map(m['Intranet'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        return self


class ForwardInfoResponse(TeaModel):
    def __init__(
        self,
        access_type: List[str] = None,
        connect_info: ForwardInfoResponseConnectInfo = None,
        container_name: str = None,
        eip_allocation_id: str = None,
        enable: bool = None,
        external_port: str = None,
        forward_port: str = None,
        name: str = None,
        nat_gateway_id: str = None,
        sshpublic_key: str = None,
    ):
        self.access_type = access_type
        self.connect_info = connect_info
        self.container_name = container_name
        self.eip_allocation_id = eip_allocation_id
        self.enable = enable
        self.external_port = external_port
        self.forward_port = forward_port
        self.name = name
        self.nat_gateway_id = nat_gateway_id
        self.sshpublic_key = sshpublic_key

    def validate(self):
        if self.connect_info:
            self.connect_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.connect_info is not None:
            result['ConnectInfo'] = self.connect_info.to_map()
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.eip_allocation_id is not None:
            result['EipAllocationId'] = self.eip_allocation_id
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port
        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port
        if self.name is not None:
            result['Name'] = self.name
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.sshpublic_key is not None:
            result['SSHPublicKey'] = self.sshpublic_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('ConnectInfo') is not None:
            temp_model = ForwardInfoResponseConnectInfo()
            self.connect_info = temp_model.from_map(m['ConnectInfo'])
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('EipAllocationId') is not None:
            self.eip_allocation_id = m.get('EipAllocationId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')
        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('SSHPublicKey') is not None:
            self.sshpublic_key = m.get('SSHPublicKey')
        return self


class CreateIdleInstanceCullerRequest(TeaModel):
    def __init__(
        self,
        cpu_percent_threshold: int = None,
        gpu_percent_threshold: int = None,
        max_idle_time_in_minutes: int = None,
    ):
        # The CPU utilization threshold. Unit: percentage. Valid values: 1 to 100. If the CPU utilization of the instance is lower than this threshold, the instance is considered idle.
        self.cpu_percent_threshold = cpu_percent_threshold
        # The GPU utilization threshold. Unit: percentage. Valid values: 1 to 100. This parameter takes effect only if the instance is of the GPU instance type. If both CPU and GPU utilization is lower than the thresholds, the instance is considered idle.
        self.gpu_percent_threshold = gpu_percent_threshold
        # The maximum time duration for which the instance is idle. Unit: minutes. If the time duration for which the instance is idle exceeds this value, the system automatically stops the instance.
        self.max_idle_time_in_minutes = max_idle_time_in_minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_percent_threshold is not None:
            result['CpuPercentThreshold'] = self.cpu_percent_threshold
        if self.gpu_percent_threshold is not None:
            result['GpuPercentThreshold'] = self.gpu_percent_threshold
        if self.max_idle_time_in_minutes is not None:
            result['MaxIdleTimeInMinutes'] = self.max_idle_time_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPercentThreshold') is not None:
            self.cpu_percent_threshold = m.get('CpuPercentThreshold')
        if m.get('GpuPercentThreshold') is not None:
            self.gpu_percent_threshold = m.get('GpuPercentThreshold')
        if m.get('MaxIdleTimeInMinutes') is not None:
            self.max_idle_time_in_minutes = m.get('MaxIdleTimeInMinutes')
        return self


class CreateIdleInstanceCullerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The instance ID.
        self.instance_id = instance_id
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateIdleInstanceCullerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIdleInstanceCullerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateIdleInstanceCullerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestAffinityCPU(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Specifies whether to enable the CPU affinity feature.
        # 
        # *   false
        # *   true
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class CreateInstanceRequestAffinity(TeaModel):
    def __init__(
        self,
        cpu: CreateInstanceRequestAffinityCPU = None,
    ):
        # The CPU affinity configuration. Only subscription instances that use general-purpose computing resources support CPU affinity configuration.
        self.cpu = cpu

    def validate(self):
        if self.cpu:
            self.cpu.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = CreateInstanceRequestAffinityCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        return self


class CreateInstanceRequestCloudDisksStatus(TeaModel):
    def __init__(
        self,
        available: int = None,
        capacity: int = None,
        usage: int = None,
    ):
        # The available capacity. Unit: bytes.
        self.available = available
        # The capacity. Unit: bytes.
        self.capacity = capacity
        # The used capacity. Unit: bytes.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['Available'] = self.available
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class CreateInstanceRequestCloudDisks(TeaModel):
    def __init__(
        self,
        capacity: str = None,
        mount_path: str = None,
        path: str = None,
        status: CreateInstanceRequestCloudDisksStatus = None,
        sub_type: str = None,
    ):
        # If **Resource Type** is **Public Resource** or if **Resource Quota** is subscription-based general-purpose computing resources (CPU cores ≥ 2 and memory ≥ 4 GB, or configured with GPU):
        # 
        # Each instance has a free system disk of 100 GiB for persistent storage. **If the DSW instance is stopped and not launched for more than 15 days, the disk is cleared**. The disk can be expanded. For specific pricing, refer to the console.
        # 
        # **\
        # 
        # **Warning**\
        # 
        # *   After the expansion, you cannot reduce the storage space. Proceed with caution.
        # 
        # *   After the expansion, the disk is not cleared if the instance is stopped for more than 15 days. However, it will continue to incur fees.
        # 
        # *   If you delete the instance, the system disk is also released and the data stored in the disk is deleted. Make sure that you have backed up your data before you delete the instance.
        # 
        # If you need persistent storage, you can **mount a dataset** or add the OSS, NAS, or CPFS path to the **storage path**.
        self.capacity = capacity
        # The mount path of the cloud disk.
        self.mount_path = mount_path
        # The subpath of the cloud disk that is mounted to the instance.
        self.path = path
        # The disk or snapshot usage.
        self.status = status
        # The cloud disk type.
        # 
        # *   rootfs: Mounts the disk as a system disk. The system environment is stored on the disk.
        self.sub_type = sub_type

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.path is not None:
            result['Path'] = self.path
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Status') is not None:
            temp_model = CreateInstanceRequestCloudDisksStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class CreateInstanceRequestDatasets(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
        dataset_version: str = None,
        dynamic: bool = None,
        mount_access: str = None,
        mount_path: str = None,
        option_type: str = None,
        options: str = None,
        uri: str = None,
    ):
        # The dataset ID. If the dataset is read-only, you cannot change the dataset permission from read-only to read and write by using MountAccess.
        # 
        # You can call [ListDatasets](https://help.aliyun.com/document_detail/457222.html) to obtain the dataset ID. If you configure the dataset ID, you cannot configure the dataset URI.
        self.dataset_id = dataset_id
        # The dataset version. You must also configure DatasetId. If you leave this parameter empty, the value v1 is used by default.
        self.dataset_version = dataset_version
        # Specifies whether to enable dynamic mounting. Default value: false.
        # 
        # *   Currently, only instances using general-purpose computing resources are supported.
        # *   Currently, only OSS datasets are supported. The mounted datasets are read-only.
        # *   The mount path of the dynamically mounted dataset must be a subpath of the root path. Example: /mnt/dynamic/data1/\
        # *   A dynamically mounted dataset must be after non-dynamic datasets.
        self.dynamic = dynamic
        # The read and write permissions of the dataset. If the dataset is read-only, it cannot be changed to read and write.
        self.mount_access = mount_access
        # The mount path of the dataset.
        self.mount_path = mount_path
        # The mount type. You cannot specify Options at the same time. This is deprecated, and you can use Options instead.
        self.option_type = option_type
        # The custom dataset mount options. Only OSS is supported. You cannot specify OptionType at the same time. For more information, see [DSW mount configurations](https://www.alibabacloud.com/help/en/pai/user-guide/read-and-write-dataset-data).
        self.options = options
        # The URI of the storage service directory, which can be directly mounted. This parameter is mutually exclusive with DatasetId.
        # 
        # URI formats of different types of storage:
        # 
        # *   OSS: oss://bucket-name.oss-cn-shanghai-internal.aliyuncs.com/data/path/\
        # *   NAS: nas://29\\*\\*d-b12\\*\\*\\*\\*446.cn-hangzhou.nas.aliyuncs.com/data/path/\
        # *   Extreme NAS: nas://29\\*\\*\\*\\*123-y\\*\\*r.cn-hangzhou.extreme.nas.aliyuncs.com/data/path/\
        # *   CPFS: cpfs://cpfs-213\\*\\*\\*\\*87.cn-wulanchabu/ptc-292\\*\\*\\*\\*\\*cbb/exp-290\\*\\*\\*\\*\\*\\*\\*\\*03e/data/path/\
        # *   Lingjun CPFS: bmcpfs://cpfs-290\\*\\*\\*\\*\\*\\*foflh-vpc-x\\*\\*\\*\\*8r.cn-wulanchabu.cpfs.aliyuncs.com/data/path/\
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic
        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.option_type is not None:
            result['OptionType'] = self.option_type
        if self.options is not None:
            result['Options'] = self.options
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')
        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('OptionType') is not None:
            self.option_type = m.get('OptionType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateInstanceRequestLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The custom label key.
        self.key = key
        # The custom label value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateInstanceRequestRequestedResource(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gputype: str = None,
        memory: str = None,
        shared_memory: str = None,
    ):
        # The number of CPU cores.
        self.cpu = cpu
        # The number of GPUs.
        self.gpu = gpu
        # The GPU memory type. Valid values:
        # 
        # *   V100
        # *   A100
        # *   T4
        # *   A10
        # *   P100
        self.gputype = gputype
        # The memory size. Unit: GB.
        self.memory = memory
        # The size of the shared memory. Unit: GB.
        self.shared_memory = shared_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')
        return self


class CreateInstanceRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateInstanceRequestUserCommandOnStart(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class CreateInstanceRequestUserCommand(TeaModel):
    def __init__(
        self,
        on_start: CreateInstanceRequestUserCommandOnStart = None,
    ):
        self.on_start = on_start

    def validate(self):
        if self.on_start:
            self.on_start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.on_start is not None:
            result['OnStart'] = self.on_start.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnStart') is not None:
            temp_model = CreateInstanceRequestUserCommandOnStart()
            self.on_start = temp_model.from_map(m['OnStart'])
        return self


class CreateInstanceRequestUserVpc(TeaModel):
    def __init__(
        self,
        bandwidth_limit: BandwidthLimit = None,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        forward_infos: List[ForwardInfo] = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.bandwidth_limit = bandwidth_limit
        # The default route. Valid values:
        # 
        # *   eth0: The default network interface is used to access the Internet through the public gateway.
        # *   eth1: The user\\"s elastic network interface (ENI) is used to access the Internet through the private gateway. For more information about the configuration method, see [Enable Internet access for a DSW instance by using a private Internet NAT gateway](https://help.aliyun.com/document_detail/2525343.html).
        self.default_route = default_route
        # The extended CIDR blocks.
        # 
        # *   If you leave the SwitchId and ExtendedCIDRs parameters empty, the system automatically obtains all CIDR blocks in a VPC.
        # *   If you configure the SwitchId and ExtendedCIDRs parameters, we recommend that you specify all CIDR blocks in a VPC.
        self.extended_cidrs = extended_cidrs
        # The forward information.
        self.forward_infos = forward_infos
        # The security group ID.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.bandwidth_limit:
            self.bandwidth_limit.validate()
        if self.forward_infos:
            for k in self.forward_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit.to_map()
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        result['ForwardInfos'] = []
        if self.forward_infos is not None:
            for k in self.forward_infos:
                result['ForwardInfos'].append(k.to_map() if k else None)
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            temp_model = BandwidthLimit()
            self.bandwidth_limit = temp_model.from_map(m['BandwidthLimit'])
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        self.forward_infos = []
        if m.get('ForwardInfos') is not None:
            for k in m.get('ForwardInfos'):
                temp_model = ForwardInfo()
                self.forward_infos.append(temp_model.from_map(k))
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        affinity: CreateInstanceRequestAffinity = None,
        cloud_disks: List[CreateInstanceRequestCloudDisks] = None,
        credential_config: CredentialConfig = None,
        datasets: List[CreateInstanceRequestDatasets] = None,
        driver: str = None,
        dynamic_mount: DynamicMount = None,
        ecs_spec: str = None,
        environment_variables: Dict[str, str] = None,
        image_auth: str = None,
        image_id: str = None,
        image_url: str = None,
        instance_name: str = None,
        labels: List[CreateInstanceRequestLabels] = None,
        oversold_type: str = None,
        priority: int = None,
        requested_resource: CreateInstanceRequestRequestedResource = None,
        resource_id: str = None,
        tag: List[CreateInstanceRequestTag] = None,
        user_command: CreateInstanceRequestUserCommand = None,
        user_id: str = None,
        user_vpc: CreateInstanceRequestUserVpc = None,
        workspace_id: str = None,
        workspace_source: str = None,
    ):
        # The instance accessibility.
        # 
        # Valid values:
        # 
        # *   PUBLIC: The instances are accessible to all members in the workspace.
        # *   PRIVATE: The instances are accessible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The affinity configuration.
        self.affinity = affinity
        # The cloud disks.
        self.cloud_disks = cloud_disks
        # The credential configuration.
        self.credential_config = credential_config
        # The datasets.
        self.datasets = datasets
        # The NVIDIA driver configuration.
        self.driver = driver
        # The dynamic mount configuration.
        self.dynamic_mount = dynamic_mount
        # The ECS instance type of the instance. You can call [ListEcsSpecs](https://help.aliyun.com/document_detail/470423.html) to obtain the ECS instance type.
        self.ecs_spec = ecs_spec
        # The environment variables.
        self.environment_variables = environment_variables
        # The Base64-encoded account and password for the user\\"s private image. The password will be hidden.
        self.image_auth = image_auth
        # The image ID. You can call [ListImages](https://help.aliyun.com/document_detail/449118.html) to obtain the image ID.
        self.image_id = image_id
        # The image address. You can call [ListImages](https://help.aliyun.com/document_detail/449118.html) to obtain the image address.
        self.image_url = image_url
        # The instance name. The name must meet the following requirements:
        # 
        # *   The name can contain only letters, digits, and underscores (_).
        # *   The name can be up to 27 characters in length.
        self.instance_name = instance_name
        # The custom labels.
        self.labels = labels
        self.oversold_type = oversold_type
        # The priority based on which resources are allocated to instances. Valid values: 1 to 9.
        # 
        # *   1: the lowest priority.
        # *   9: the highest priority.
        self.priority = priority
        # The resource configurations.
        self.requested_resource = requested_resource
        # The ID of the resource group. This parameter is configured during prepayment. For information about how to create a dedicated resource group, see [Create a dedicated resource group and purchase general computing resources](https://help.aliyun.com/document_detail/202827.html).
        self.resource_id = resource_id
        # The tags.
        self.tag = tag
        self.user_command = user_command
        # The ID of the instance owner. Valid values: Alibaba Cloud account and RAM user.
        self.user_id = user_id
        # The virtual private cloud (VPC) configurations.
        self.user_vpc = user_vpc
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id
        # The storage corresponding to the working directory. You can mount disks or datasets to /mnt/workspace at the same time. OSS datasets and dynamically mounted datasets are not supported.
        # 
        # Valid values:
        # 
        # *   rootfsCloudDisk: Mount the disk to the working directory.
        # *   Mount path of the dataset, such as /mnt/data: Datasets in URI format only support this method.
        # *   Dataset ID, such as d-vsqjvs\\*\\*\\*\\*rp5l206u: If a single dataset is mounted to multiple paths, the first path is selected. We recommend that you do not use this method, use the mount path instead.
        # 
        # If you leave this parameter empty:
        # 
        # *   If the instance uses cloud disks, cloud disks are selected by default.
        # *   if no cloud disks are available, the first NAS or CPFS dataset is selected as the working directory.
        # *   If no cloud disks, and NAS or CPFS datasets are available, the host space is used.
        self.workspace_source = workspace_source

    def validate(self):
        if self.affinity:
            self.affinity.validate()
        if self.cloud_disks:
            for k in self.cloud_disks:
                if k:
                    k.validate()
        if self.credential_config:
            self.credential_config.validate()
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.dynamic_mount:
            self.dynamic_mount.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.requested_resource:
            self.requested_resource.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.user_command:
            self.user_command.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.affinity is not None:
            result['Affinity'] = self.affinity.to_map()
        result['CloudDisks'] = []
        if self.cloud_disks is not None:
            for k in self.cloud_disks:
                result['CloudDisks'].append(k.to_map() if k else None)
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.dynamic_mount is not None:
            result['DynamicMount'] = self.dynamic_mount.to_map()
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.image_auth is not None:
            result['ImageAuth'] = self.image_auth
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.oversold_type is not None:
            result['OversoldType'] = self.oversold_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.requested_resource is not None:
            result['RequestedResource'] = self.requested_resource.to_map()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.user_command is not None:
            result['UserCommand'] = self.user_command.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_source is not None:
            result['WorkspaceSource'] = self.workspace_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Affinity') is not None:
            temp_model = CreateInstanceRequestAffinity()
            self.affinity = temp_model.from_map(m['Affinity'])
        self.cloud_disks = []
        if m.get('CloudDisks') is not None:
            for k in m.get('CloudDisks'):
                temp_model = CreateInstanceRequestCloudDisks()
                self.cloud_disks.append(temp_model.from_map(k))
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = CreateInstanceRequestDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('DynamicMount') is not None:
            temp_model = DynamicMount()
            self.dynamic_mount = temp_model.from_map(m['DynamicMount'])
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('ImageAuth') is not None:
            self.image_auth = m.get('ImageAuth')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = CreateInstanceRequestLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('OversoldType') is not None:
            self.oversold_type = m.get('OversoldType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RequestedResource') is not None:
            temp_model = CreateInstanceRequestRequestedResource()
            self.requested_resource = temp_model.from_map(m['RequestedResource'])
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UserCommand') is not None:
            temp_model = CreateInstanceRequestUserCommand()
            self.user_command = temp_model.from_map(m['UserCommand'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = CreateInstanceRequestUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceSource') is not None:
            self.workspace_source = m.get('WorkspaceSource')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The HTTP status code. Valid values:
        # 
        # *   400
        # *   404
        # *   200
        self.http_status_code = http_status_code
        # The instance ID.
        self.instance_id = instance_id
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceShutdownTimerRequest(TeaModel):
    def __init__(
        self,
        due_time: str = None,
        remaining_time_in_ms: int = None,
    ):
        # The scheduled stop time.
        self.due_time = due_time
        # The time duration before the instance is stopped. Unit: milliseconds.
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


class CreateInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The HTTP status code. Valid values:
        # 
        # *   400
        # *   404
        self.http_status_code = http_status_code
        # The instance ID.
        self.instance_id = instance_id
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateInstanceShutdownTimerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceShutdownTimerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInstanceShutdownTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceSnapshotRequestLabels(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateInstanceSnapshotRequest(TeaModel):
    def __init__(
        self,
        exclude_paths: List[str] = None,
        image_url: str = None,
        labels: List[CreateInstanceSnapshotRequestLabels] = None,
        overwrite: bool = None,
        snapshot_description: str = None,
        snapshot_name: str = None,
    ):
        self.exclude_paths = exclude_paths
        # This parameter is required.
        self.image_url = image_url
        self.labels = labels
        self.overwrite = overwrite
        self.snapshot_description = snapshot_description
        # This parameter is required.
        self.snapshot_name = snapshot_name

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_paths is not None:
            result['ExcludePaths'] = self.exclude_paths
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.snapshot_description is not None:
            result['SnapshotDescription'] = self.snapshot_description
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludePaths') is not None:
            self.exclude_paths = m.get('ExcludePaths')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = CreateInstanceSnapshotRequestLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('SnapshotDescription') is not None:
            self.snapshot_description = m.get('SnapshotDescription')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        return self


class CreateInstanceSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        snapshot_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.message = message
        self.request_id = request_id
        self.snapshot_id = snapshot_id
        self.success = success

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateInstanceSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIdleInstanceCullerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The instance ID.
        self.instance_id = instance_id
        # The response message.
        # 
        # *   If the request is successful, null is returned.
        # *   If the request fails, the failure cause is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteIdleInstanceCullerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIdleInstanceCullerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteIdleInstanceCullerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The HTTP status code. Valid values:
        # 
        # *   400
        # *   404
        # *   200
        self.http_status_code = http_status_code
        # The instance ID.
        self.instance_id = instance_id
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # *   true
        # *   false
        self.success = success

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceLabelsRequest(TeaModel):
    def __init__(
        self,
        label_keys: str = None,
    ):
        # The keys of the tags that you want to delete. Separate multiple tags with commas (,).
        # 
        # This parameter is required.
        self.label_keys = label_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')
        return self


class DeleteInstanceLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceLabelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstanceLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The HTTP status code. Valid values:
        # 
        # *   400
        # *   404
        self.http_status_code = http_status_code
        # The instance ID.
        self.instance_id = instance_id
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteInstanceShutdownTimerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceShutdownTimerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstanceShutdownTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        snapshot_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.message = message
        self.request_id = request_id
        self.snapshot_id = snapshot_id
        self.success = success

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteInstanceSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIdleInstanceCullerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        cpu_percent_threshold: int = None,
        gpu_percent_threshold: int = None,
        idle_time_in_minutes: int = None,
        instance_id: str = None,
        max_idle_time_in_minutes: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The CPU utilization threshold. Unit: percentage. Valid values: 1 to 100. If the CPU utilization of the instance is lower than this threshold, the instance is considered idle.
        self.cpu_percent_threshold = cpu_percent_threshold
        # The GPU utilization threshold. Unit: percentage. Valid values: 1 to 100. This parameter takes effect only if the instance is of the GPU instance type. If both CPU and GPU utilization is lower than the thresholds, the instance is considered idle.
        self.gpu_percent_threshold = gpu_percent_threshold
        # The time duration for which the instance is idle. Unit: minutes.
        self.idle_time_in_minutes = idle_time_in_minutes
        # The instance ID.
        self.instance_id = instance_id
        # The maximum time duration for which the instance is idle. Unit: minutes. If the time duration for which the instance is idle exceeds this value, the system automatically stops the instance.
        self.max_idle_time_in_minutes = max_idle_time_in_minutes
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cpu_percent_threshold is not None:
            result['CpuPercentThreshold'] = self.cpu_percent_threshold
        if self.gpu_percent_threshold is not None:
            result['GpuPercentThreshold'] = self.gpu_percent_threshold
        if self.idle_time_in_minutes is not None:
            result['IdleTimeInMinutes'] = self.idle_time_in_minutes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_idle_time_in_minutes is not None:
            result['MaxIdleTimeInMinutes'] = self.max_idle_time_in_minutes
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CpuPercentThreshold') is not None:
            self.cpu_percent_threshold = m.get('CpuPercentThreshold')
        if m.get('GpuPercentThreshold') is not None:
            self.gpu_percent_threshold = m.get('GpuPercentThreshold')
        if m.get('IdleTimeInMinutes') is not None:
            self.idle_time_in_minutes = m.get('IdleTimeInMinutes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxIdleTimeInMinutes') is not None:
            self.max_idle_time_in_minutes = m.get('MaxIdleTimeInMinutes')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetIdleInstanceCullerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIdleInstanceCullerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetIdleInstanceCullerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceRequest(TeaModel):
    def __init__(
        self,
        token: str = None,
    ):
        # The sharing token information.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetInstanceResponseBodyAffinityCPU(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Indicates whether CPU affinity is enabled.
        # 
        # true false
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class GetInstanceResponseBodyAffinity(TeaModel):
    def __init__(
        self,
        cpu: GetInstanceResponseBodyAffinityCPU = None,
    ):
        # The CPU affinity configuration. Only subscription instances that use general-purpose computing resources support CPU affinity configuration.
        self.cpu = cpu

    def validate(self):
        if self.cpu:
            self.cpu.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = GetInstanceResponseBodyAffinityCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        return self


class GetInstanceResponseBodyCloudDisks(TeaModel):
    def __init__(
        self,
        capacity: str = None,
        mount_path: str = None,
        path: str = None,
        sub_type: str = None,
    ):
        # Disk Capacity
        self.capacity = capacity
        # The mount path of the cloud disk in the container.
        self.mount_path = mount_path
        # The directory on the cloud disk that is mounted to the container.
        self.path = path
        # The usage mode of the cloud disk. The value rootfs indicates that the cloud disk is used as the root file system.
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.path is not None:
            result['Path'] = self.path
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class GetInstanceResponseBodyDatasets(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
        dataset_version: str = None,
        dynamic: bool = None,
        mount_access: str = None,
        mount_path: str = None,
        option_type: str = None,
        options: str = None,
        uri: str = None,
    ):
        # The dataset ID.
        self.dataset_id = dataset_id
        # The dataset version.
        self.dataset_version = dataset_version
        # Indicates whether dynamic mounting is enabled. Default value: false.
        self.dynamic = dynamic
        # The read and write permissions. Valid values: RW and RO.
        self.mount_access = mount_access
        # The mount path in the container.
        self.mount_path = mount_path
        # The mount type of the dataset (deprecated).
        self.option_type = option_type
        # The mount type of the dataset.
        self.options = options
        # The dataset URI.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic
        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.option_type is not None:
            result['OptionType'] = self.option_type
        if self.options is not None:
            result['Options'] = self.options
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')
        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('OptionType') is not None:
            self.option_type = m.get('OptionType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class GetInstanceResponseBodyIdleInstanceCuller(TeaModel):
    def __init__(
        self,
        cpu_percent_threshold: int = None,
        gpu_percent_threshold: int = None,
        idle_time_in_minutes: int = None,
        instance_id: str = None,
        max_idle_time_in_minutes: int = None,
    ):
        # The CPU utilization threshold. Unit: percentage. Valid values: 1 to 100. If the CPU utilization of the instance is lower than this threshold, the instance is considered idle.
        self.cpu_percent_threshold = cpu_percent_threshold
        # The GPU utilization threshold. Unit: percentage. Valid values: 1 to 100. This parameter takes effect only if the instance is of the GPU instance type. If both CPU and GPU utilization is lower than the thresholds, the instance is considered idle.
        self.gpu_percent_threshold = gpu_percent_threshold
        # The current time duration for which the instance is idle. Unit: minutes.
        self.idle_time_in_minutes = idle_time_in_minutes
        # The instance ID.
        self.instance_id = instance_id
        # The maximum time duration for which the instance is idle. Unit: minutes. If the time duration for which the instance is idle exceeds this value, the system automatically stops the instance.
        self.max_idle_time_in_minutes = max_idle_time_in_minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_percent_threshold is not None:
            result['CpuPercentThreshold'] = self.cpu_percent_threshold
        if self.gpu_percent_threshold is not None:
            result['GpuPercentThreshold'] = self.gpu_percent_threshold
        if self.idle_time_in_minutes is not None:
            result['IdleTimeInMinutes'] = self.idle_time_in_minutes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_idle_time_in_minutes is not None:
            result['MaxIdleTimeInMinutes'] = self.max_idle_time_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPercentThreshold') is not None:
            self.cpu_percent_threshold = m.get('CpuPercentThreshold')
        if m.get('GpuPercentThreshold') is not None:
            self.gpu_percent_threshold = m.get('GpuPercentThreshold')
        if m.get('IdleTimeInMinutes') is not None:
            self.idle_time_in_minutes = m.get('IdleTimeInMinutes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxIdleTimeInMinutes') is not None:
            self.max_idle_time_in_minutes = m.get('MaxIdleTimeInMinutes')
        return self


class GetInstanceResponseBodyInstanceShutdownTimer(TeaModel):
    def __init__(
        self,
        due_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        remaining_time_in_ms: int = None,
    ):
        # The scheduled stop time.
        self.due_time = due_time
        # The creation time.
        self.gmt_create_time = gmt_create_time
        # The modified time.
        self.gmt_modified_time = gmt_modified_time
        # The instance ID.
        self.instance_id = instance_id
        # The remaining time before the instance is stopped. Unit: milliseconds.
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


class GetInstanceResponseBodyInstanceSnapshotList(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        reason_code: str = None,
        reason_message: str = None,
        repository_url: str = None,
        status: str = None,
    ):
        # The time when the snapshot was created.
        self.gmt_create_time = gmt_create_time
        # The time when the snapshot was modified.
        self.gmt_modified_time = gmt_modified_time
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image URL.
        self.image_url = image_url
        # The error code of the instance snapshot.
        self.reason_code = reason_code
        # The error message of the instance snapshot.
        self.reason_message = reason_message
        # The image repository URL.
        self.repository_url = repository_url
        # The instance snapshot status.
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
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
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
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetInstanceResponseBodyLabels(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetInstanceResponseBodyLatestSnapshot(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        reason_code: str = None,
        reason_message: str = None,
        repository_url: str = None,
        status: str = None,
    ):
        # The time when the snapshot was created.
        self.gmt_create_time = gmt_create_time
        # The time when the snapshot was modified.
        self.gmt_modified_time = gmt_modified_time
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image URL.
        self.image_url = image_url
        # The error code of the instance snapshot.
        self.reason_code = reason_code
        # The error message of the instance snapshot.
        self.reason_message = reason_message
        # The image repository URL.
        self.repository_url = repository_url
        # The instance snapshot status.
        # 
        # Valid values:
        # 
        # *   Committing
        # *   Pushing
        # *   Failed
        # *   Saved
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
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
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
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetInstanceResponseBodyNodeErrorRecovery(TeaModel):
    def __init__(
        self,
        auto_switch_countdown_seconds: int = None,
        enable_auto_switch_on_node_error: bool = None,
        has_node_error: bool = None,
    ):
        # The number of seconds to wait before automatic switchover.
        self.auto_switch_countdown_seconds = auto_switch_countdown_seconds
        # Indicates whether to enable automatic switchover when a node error occurs.
        self.enable_auto_switch_on_node_error = enable_auto_switch_on_node_error
        # Indicates whether the node has an error.
        self.has_node_error = has_node_error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_switch_countdown_seconds is not None:
            result['autoSwitchCountdownSeconds'] = self.auto_switch_countdown_seconds
        if self.enable_auto_switch_on_node_error is not None:
            result['enableAutoSwitchOnNodeError'] = self.enable_auto_switch_on_node_error
        if self.has_node_error is not None:
            result['hasNodeError'] = self.has_node_error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSwitchCountdownSeconds') is not None:
            self.auto_switch_countdown_seconds = m.get('autoSwitchCountdownSeconds')
        if m.get('enableAutoSwitchOnNodeError') is not None:
            self.enable_auto_switch_on_node_error = m.get('enableAutoSwitchOnNodeError')
        if m.get('hasNodeError') is not None:
            self.has_node_error = m.get('hasNodeError')
        return self


class GetInstanceResponseBodyRequestedResource(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gputype: str = None,
        memory: str = None,
        shared_memory: str = None,
    ):
        # The number of CPU cores.
        self.cpu = cpu
        # The number of GPUs.
        self.gpu = gpu
        # The GPU type. Valid values:
        # 
        # *   V100
        # *   A100
        # *   T4
        # *   A10
        # *   P100
        self.gputype = gputype
        # The memory size. Unit: GB.
        self.memory = memory
        # The shared memory size. Unit: GB.
        self.shared_memory = shared_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')
        return self


class GetInstanceResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetInstanceResponseBodyUserVpc(TeaModel):
    def __init__(
        self,
        bandwidth_limit: BandwidthLimit = None,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        forward_infos: List[ForwardInfoResponse] = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.bandwidth_limit = bandwidth_limit
        # Default Route
        self.default_route = default_route
        # The extended CIDR block.
        # 
        # *   If you leave VSwitchId empty, this parameter is not required and the system automatically obtains all CIDR blocks in the VPC.
        # *   If VSwitchId is not empty, this parameter is required. Specify all CIDR blocks in the VPC.
        self.extended_cidrs = extended_cidrs
        # The forward information.
        self.forward_infos = forward_infos
        # The security group ID.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.bandwidth_limit:
            self.bandwidth_limit.validate()
        if self.forward_infos:
            for k in self.forward_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit.to_map()
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        result['ForwardInfos'] = []
        if self.forward_infos is not None:
            for k in self.forward_infos:
                result['ForwardInfos'].append(k.to_map() if k else None)
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            temp_model = BandwidthLimit()
            self.bandwidth_limit = temp_model.from_map(m['BandwidthLimit'])
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        self.forward_infos = []
        if m.get('ForwardInfos') is not None:
            for k in m.get('ForwardInfos'):
                temp_model = ForwardInfoResponse()
                self.forward_infos.append(temp_model.from_map(k))
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        accessibility: str = None,
        accumulated_running_time_in_ms: int = None,
        affinity: GetInstanceResponseBodyAffinity = None,
        cloud_disks: List[GetInstanceResponseBodyCloudDisks] = None,
        code: str = None,
        credential_config: CredentialConfig = None,
        datasets: List[GetInstanceResponseBodyDatasets] = None,
        driver: str = None,
        dynamic_mount: DynamicMount = None,
        ecs_spec: str = None,
        environment_variables: Dict[str, str] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        http_status_code: int = None,
        idle_instance_culler: GetInstanceResponseBodyIdleInstanceCuller = None,
        image_auth: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_shutdown_timer: GetInstanceResponseBodyInstanceShutdownTimer = None,
        instance_snapshot_list: List[GetInstanceResponseBodyInstanceSnapshotList] = None,
        instance_url: str = None,
        jupyterlab_url: str = None,
        labels: List[GetInstanceResponseBodyLabels] = None,
        latest_snapshot: GetInstanceResponseBodyLatestSnapshot = None,
        message: str = None,
        node_error_recovery: GetInstanceResponseBodyNodeErrorRecovery = None,
        payment_type: str = None,
        priority: int = None,
        proxy_path: str = None,
        reason_code: str = None,
        reason_message: str = None,
        request_id: str = None,
        requested_resource: GetInstanceResponseBodyRequestedResource = None,
        resource_id: str = None,
        resource_name: str = None,
        status: str = None,
        success: bool = None,
        tags: List[GetInstanceResponseBodyTags] = None,
        terminal_url: str = None,
        user_command_id: str = None,
        user_id: str = None,
        user_name: str = None,
        user_vpc: GetInstanceResponseBodyUserVpc = None,
        web_ideurl: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
        workspace_source: str = None,
    ):
        # The accelerator type of the instance.
        # 
        # Valid values:
        # 
        # *   CPU
        # *   GPU
        self.accelerator_type = accelerator_type
        # The accessibility. Valid values:
        # 
        # *   PRIVATE: Accessible only to you and the administrator of the workspace.
        # *   PUBLIC: Accessible to all members in the workspace.
        self.accessibility = accessibility
        # The accumulated running duration. Unit: milliseconds.
        self.accumulated_running_time_in_ms = accumulated_running_time_in_ms
        # The affinity configuration.
        self.affinity = affinity
        # The cloud disks of the instance.
        self.cloud_disks = cloud_disks
        # The status code. Valid values:
        # 
        # *   InternalError: All errors, except for parameter validation errors, are internal errors.
        # *   ValidationError: A parameter validation error.
        self.code = code
        # The credential injection configuration.
        self.credential_config = credential_config
        # The datasets.
        self.datasets = datasets
        # The NVIDIA driver configuration.
        self.driver = driver
        # The dynamic mount configuration.
        self.dynamic_mount = dynamic_mount
        # The ECS instance type of the instance.
        self.ecs_spec = ecs_spec
        # The environment variables.
        self.environment_variables = environment_variables
        # The creation time of the instance.
        self.gmt_create_time = gmt_create_time
        # The last modified time of the instance.
        self.gmt_modified_time = gmt_modified_time
        # The HTTP status code. Valid values:
        # 
        # *   400
        # *   404
        self.http_status_code = http_status_code
        # The automatic shutdown settings.
        self.idle_instance_culler = idle_instance_culler
        # The Base64-encoded account and password for the user‘s private image. The password will be hidden.
        self.image_auth = image_auth
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image address.
        self.image_url = image_url
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The scheduled stop tasks.
        self.instance_shutdown_timer = instance_shutdown_timer
        # The instance snapshots.
        self.instance_snapshot_list = instance_snapshot_list
        # The instance URL.
        self.instance_url = instance_url
        # The JupyterLab URL.
        self.jupyterlab_url = jupyterlab_url
        # The custom tags.
        self.labels = labels
        # The latest user image saved.
        self.latest_snapshot = latest_snapshot
        # The error message. Valid values:
        # 
        # *   If the request is successful, null is returned.
        # *   If the request fails, the cause for the failure is returned.
        self.message = message
        # The error recovery configuration of the node.
        self.node_error_recovery = node_error_recovery
        # The billing method. Valid values:
        # 
        # *   PayAsYouGo
        # *   Subscription
        self.payment_type = payment_type
        # The priority based on which resources are allocated to instances.
        self.priority = priority
        # The proxy path.
        self.proxy_path = proxy_path
        # The error code of the instance.
        self.reason_code = reason_code
        # The cause of the instance error.
        self.reason_message = reason_message
        # The request ID.
        self.request_id = request_id
        # The resource configurations in subscription scenarios.
        self.requested_resource = requested_resource
        # The resource ID. This parameter is available if the billing method is subscription.
        self.resource_id = resource_id
        # The specification type.
        # 
        # *   For subscription, this is the requested CPU and memory size.
        # *   For pay-as-you-go, this is the selected ECS instance type.
        self.resource_name = resource_name
        # The instance status.
        # 
        # Valid values:
        # 
        # *   Creating
        # *   SaveFailed
        # *   Stopped
        # *   Failed
        # *   ResourceAllocating
        # *   Stopping
        # *   Updating
        # *   Saving
        # *   Queuing
        # *   Recovering
        # *   Starting
        # *   Running
        # *   Saved
        # *   Deleting
        # *   EnvPreparing
        self.status = status
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The tags.
        self.tags = tags
        # The terminal URL.
        self.terminal_url = terminal_url
        self.user_command_id = user_command_id
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name
        # The virtual private cloud (VPC) configurations.
        self.user_vpc = user_vpc
        # The Web IDE URL.
        self.web_ideurl = web_ideurl
        # The workspace ID.
        self.workspace_id = workspace_id
        # The workspace name.
        self.workspace_name = workspace_name
        # The storage for the workspace. If you leave this parameter empty, the workspace uses File Storage NAS (NAS) storage, cloud disks, or local disks in sequence.
        self.workspace_source = workspace_source

    def validate(self):
        if self.affinity:
            self.affinity.validate()
        if self.cloud_disks:
            for k in self.cloud_disks:
                if k:
                    k.validate()
        if self.credential_config:
            self.credential_config.validate()
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.dynamic_mount:
            self.dynamic_mount.validate()
        if self.idle_instance_culler:
            self.idle_instance_culler.validate()
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.instance_snapshot_list:
            for k in self.instance_snapshot_list:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.latest_snapshot:
            self.latest_snapshot.validate()
        if self.node_error_recovery:
            self.node_error_recovery.validate()
        if self.requested_resource:
            self.requested_resource.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
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
        if self.affinity is not None:
            result['Affinity'] = self.affinity.to_map()
        result['CloudDisks'] = []
        if self.cloud_disks is not None:
            for k in self.cloud_disks:
                result['CloudDisks'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.dynamic_mount is not None:
            result['DynamicMount'] = self.dynamic_mount.to_map()
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.idle_instance_culler is not None:
            result['IdleInstanceCuller'] = self.idle_instance_culler.to_map()
        if self.image_auth is not None:
            result['ImageAuth'] = self.image_auth
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
        result['InstanceSnapshotList'] = []
        if self.instance_snapshot_list is not None:
            for k in self.instance_snapshot_list:
                result['InstanceSnapshotList'].append(k.to_map() if k else None)
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.latest_snapshot is not None:
            result['LatestSnapshot'] = self.latest_snapshot.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.node_error_recovery is not None:
            result['NodeErrorRecovery'] = self.node_error_recovery.to_map()
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.proxy_path is not None:
            result['ProxyPath'] = self.proxy_path
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.requested_resource is not None:
            result['RequestedResource'] = self.requested_resource.to_map()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_command_id is not None:
            result['UserCommandId'] = self.user_command_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ideurl is not None:
            result['WebIDEUrl'] = self.web_ideurl
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        if self.workspace_source is not None:
            result['WorkspaceSource'] = self.workspace_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('AccumulatedRunningTimeInMs') is not None:
            self.accumulated_running_time_in_ms = m.get('AccumulatedRunningTimeInMs')
        if m.get('Affinity') is not None:
            temp_model = GetInstanceResponseBodyAffinity()
            self.affinity = temp_model.from_map(m['Affinity'])
        self.cloud_disks = []
        if m.get('CloudDisks') is not None:
            for k in m.get('CloudDisks'):
                temp_model = GetInstanceResponseBodyCloudDisks()
                self.cloud_disks.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = GetInstanceResponseBodyDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('DynamicMount') is not None:
            temp_model = DynamicMount()
            self.dynamic_mount = temp_model.from_map(m['DynamicMount'])
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('IdleInstanceCuller') is not None:
            temp_model = GetInstanceResponseBodyIdleInstanceCuller()
            self.idle_instance_culler = temp_model.from_map(m['IdleInstanceCuller'])
        if m.get('ImageAuth') is not None:
            self.image_auth = m.get('ImageAuth')
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
            temp_model = GetInstanceResponseBodyInstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        self.instance_snapshot_list = []
        if m.get('InstanceSnapshotList') is not None:
            for k in m.get('InstanceSnapshotList'):
                temp_model = GetInstanceResponseBodyInstanceSnapshotList()
                self.instance_snapshot_list.append(temp_model.from_map(k))
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetInstanceResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatestSnapshot') is not None:
            temp_model = GetInstanceResponseBodyLatestSnapshot()
            self.latest_snapshot = temp_model.from_map(m['LatestSnapshot'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeErrorRecovery') is not None:
            temp_model = GetInstanceResponseBodyNodeErrorRecovery()
            self.node_error_recovery = temp_model.from_map(m['NodeErrorRecovery'])
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ProxyPath') is not None:
            self.proxy_path = m.get('ProxyPath')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestedResource') is not None:
            temp_model = GetInstanceResponseBodyRequestedResource()
            self.requested_resource = temp_model.from_map(m['RequestedResource'])
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetInstanceResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserCommandId') is not None:
            self.user_command_id = m.get('UserCommandId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserVpc') is not None:
            temp_model = GetInstanceResponseBodyUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIDEUrl') is not None:
            self.web_ideurl = m.get('WebIDEUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        if m.get('WorkspaceSource') is not None:
            self.workspace_source = m.get('WorkspaceSource')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceEventsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        max_events_num: int = None,
        start_time: str = None,
        token: str = None,
    ):
        # The end of the time range to query.
        self.end_time = end_time
        # The maximum number of events. Default value: 2000.
        self.max_events_num = max_events_num
        # The beginning of the time range to query.
        self.start_time = start_time
        # The token used to share the URL.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_events_num is not None:
            result['MaxEventsNum'] = self.max_events_num
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxEventsNum') is not None:
            self.max_events_num = m.get('MaxEventsNum')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetInstanceEventsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        events: List[str] = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The events.
        self.events = events
        # The HTTP status code. Valid values:
        # 
        # *   400: One or more parameters are invalid.
        # *   404: The instance does not exist.
        # *   200: The request is normal.
        self.http_status_code = http_status_code
        # The instance ID.
        self.instance_id = instance_id
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.events is not None:
            result['Events'] = self.events
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstanceEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceMetricsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        metric_type: str = None,
        start_time: str = None,
        time_step: str = None,
    ):
        # The end of the time range to query.
        self.end_time = end_time
        # The metric type. Valid values:
        # 
        # *   GpuCoreUsage: the GPU utilization.
        # *   GpuMemoryUsage: the GPU memory utilization.
        # *   CpuCoreUsage: the CPU utilization.
        # *   MemoryUsage: the memory utilization.
        # *   NetworkInputRate: the network ingress rate.
        # *   NetworkOutputRate: the network egress rate.
        # *   DiskReadRate: the disk read rate.
        # *   DiskWriteRate: the disk write rate.
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # The beginning of the time range to query.
        self.start_time = start_time
        # The interval at which metrics are returned. Unit: minutes.
        self.time_step = time_step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_step is not None:
            result['TimeStep'] = self.time_step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')
        return self


class GetInstanceMetricsResponseBodyPodMetricsMetrics(TeaModel):
    def __init__(
        self,
        time: int = None,
        value: float = None,
    ):
        # The timestamp corresponding to the metric.
        self.time = time
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetInstanceMetricsResponseBodyPodMetrics(TeaModel):
    def __init__(
        self,
        metrics: List[GetInstanceMetricsResponseBodyPodMetricsMetrics] = None,
        pod_id: str = None,
    ):
        # The metrics of the pod that corresponds to the instance.
        self.metrics = metrics
        # The ID of the pod that corresponds to the instance.
        self.pod_id = pod_id

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = GetInstanceMetricsResponseBodyPodMetricsMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        return self


class GetInstanceMetricsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        pod_metrics: List[GetInstanceMetricsResponseBodyPodMetrics] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The HTTP status code. Valid values:
        # 
        # *   400
        # *   404
        self.http_status_code = http_status_code
        # The instance ID.
        self.instance_id = instance_id
        # The response message.
        self.message = message
        # The information about the metrics of the pod that corresponds to the instance.
        self.pod_metrics = pod_metrics
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.pod_metrics:
            for k in self.pod_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        result['PodMetrics'] = []
        if self.pod_metrics is not None:
            for k in self.pod_metrics:
                result['PodMetrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.pod_metrics = []
        if m.get('PodMetrics') is not None:
            for k in m.get('PodMetrics'):
                temp_model = GetInstanceMetricsResponseBodyPodMetrics()
                self.pod_metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceMetricsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstanceMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        due_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        remaining_time_in_ms: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.due_time = due_time
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.message = message
        self.remaining_time_in_ms = remaining_time_in_ms
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.remaining_time_in_ms is not None:
            result['RemainingTimeInMs'] = self.remaining_time_in_ms
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RemainingTimeInMs') is not None:
            self.remaining_time_in_ms = m.get('RemainingTimeInMs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceShutdownTimerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceShutdownTimerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstanceShutdownTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceSnapshotResponseBodyLabels(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetInstanceSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        exclude_paths: List[str] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        http_status_code: int = None,
        image_id: str = None,
        image_url: str = None,
        instance_id: str = None,
        labels: List[GetInstanceSnapshotResponseBodyLabels] = None,
        message: str = None,
        reason_code: str = None,
        reason_message: str = None,
        request_id: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.exclude_paths = exclude_paths
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.http_status_code = http_status_code
        self.image_id = image_id
        self.image_url = image_url
        self.instance_id = instance_id
        self.labels = labels
        self.message = message
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.request_id = request_id
        self.snapshot_id = snapshot_id
        self.snapshot_name = snapshot_name
        self.status = status
        self.success = success

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.exclude_paths is not None:
            result['ExcludePaths'] = self.exclude_paths
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ExcludePaths') is not None:
            self.exclude_paths = m.get('ExcludePaths')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetInstanceSnapshotResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLifecycleRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        limit: int = None,
        order: str = None,
        session_number: int = None,
        start_time: str = None,
        token: str = None,
    ):
        # The end of the time range to query.
        self.end_time = end_time
        # The number of sessions to query.
        self.limit = limit
        # The sorting order of the results. Valid values:
        # 
        # *   ASC: sorted by time in ascending order.
        # *   DESC: sorted by time in descending order.
        self.order = order
        # A session refers to the process of an instance from startup to failure or shutdown. The sessionNumber indicates the offset value for the instance\\"s session sequence.
        self.session_number = session_number
        # The beginning of the time range to query.
        self.start_time = start_time
        # The token used to share the URL.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order is not None:
            result['Order'] = self.order
        if self.session_number is not None:
            result['SessionNumber'] = self.session_number
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('SessionNumber') is not None:
            self.session_number = m.get('SessionNumber')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetLifecycleResponseBodyLifecycle(TeaModel):
    def __init__(
        self,
        status: str = None,
        reason_code: str = None,
        reason_message: str = None,
        gmt_create_time: str = None,
    ):
        # The status of the instance. Valid values:
        # 
        # *   Creating
        # *   SaveFailed: The instance image failed to be saved.
        # *   Stopped
        # *   Failed
        # *   ResourceAllocating
        # *   Stopping
        # *   Updating
        # *   Saving
        # *   Starting
        # *   Running
        # *   Saved
        # *   EnvPreparing: Preparing environment.
        # *   ArrearStopping: The service is being stopped due to overdue payments.
        # *   Arrearge: The service is stopped due to overdue payments.
        # *   Queuing
        # *   Recovering
        self.status = status
        # The reason code that corresponds to an event.
        self.reason_code = reason_code
        # The reason message that corresponds to an event.
        self.reason_message = reason_message
        # The time the status was created, specifically the time the instance transitioned to this status (in GMT).
        self.gmt_create_time = gmt_create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        return self


class GetLifecycleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        lifecycle: List[List[GetLifecycleResponseBodyLifecycle]] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: All errors, except for parameter validation errors, are internal errors.
        # *   ValidationError: A parameter validation error.
        self.code = code
        # The lifecycle details.
        self.lifecycle = lifecycle
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of queried sessions.
        self.total_count = total_count

    def validate(self):
        if self.lifecycle:
            for k in self.lifecycle:
                for k1 in k:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Lifecycle'] = []
        if self.lifecycle is not None:
            for k in self.lifecycle:
                l1 = []
                for k1 in k:
                    l1.append(k1.to_map() if k1 else None)
                result['Lifecycle'].append(l1)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.lifecycle = []
        if m.get('Lifecycle') is not None:
            for k in m.get('Lifecycle'):
                l1 = []
                for k1 in k:
                    temp_model = GetLifecycleResponseBodyLifecycle()
                    l1.append(temp_model.from_map(k1))
                self.lifecycle.append(l1)
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetLifecycleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLifecycleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLifecycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMetricsRequest(TeaModel):
    def __init__(
        self,
        dimensions: str = None,
        end_time: str = None,
        length: str = None,
        metric_name: str = None,
        namespace: str = None,
        next_token: str = None,
        period: str = None,
        start_time: str = None,
    ):
        self.dimensions = dimensions
        self.end_time = end_time
        self.length = length
        self.metric_name = metric_name
        self.namespace = namespace
        self.next_token = next_token
        self.period = period
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.length is not None:
            result['Length'] = self.length
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.period is not None:
            result['Period'] = self.period
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetMetricsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        datapoints: str = None,
        message: str = None,
        next_token: str = None,
        period: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.datapoints = datapoints
        self.message = message
        self.next_token = next_token
        self.period = period
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.period is not None:
            result['Period'] = self.period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Datapoints') is not None:
            self.datapoints = m.get('Datapoints')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMetricsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceGroupStatisticsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        resource_id: str = None,
        start_time: str = None,
        workspace_ids: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.workspace_ids = workspace_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')
        return self


class GetResourceGroupStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        statistics: Dict[str, dict] = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.statistics = statistics
        self.success = success

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetResourceGroupStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceGroupStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceGroupStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        instance_id: str = None,
    ):
        # The validity period. Unit: seconds.
        self.expire_time = expire_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        token: str = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: All errors, except for parameter validation errors, are internal errors.
        # *   ValidationError: A parameter validation error.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The temporary authentication information of the DSW instance.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserCommandRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        token: str = None,
    ):
        self.instance_id = instance_id
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetUserCommandResponseBodyOnStart(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetUserCommandResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        on_start: GetUserCommandResponseBodyOnStart = None,
        request_id: str = None,
        success: bool = None,
        user_command_id: str = None,
        access_denied_detail: Dict[str, Any] = None,
    ):
        self.code = code
        self.message = message
        self.on_start = on_start
        self.request_id = request_id
        self.success = success
        self.user_command_id = user_command_id
        self.access_denied_detail = access_denied_detail

    def validate(self):
        if self.on_start:
            self.on_start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.on_start is not None:
            result['OnStart'] = self.on_start.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user_command_id is not None:
            result['UserCommandId'] = self.user_command_id
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OnStart') is not None:
            temp_model = GetUserCommandResponseBodyOnStart()
            self.on_start = temp_model.from_map(m['OnStart'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UserCommandId') is not None:
            self.user_command_id = m.get('UserCommandId')
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        return self


class GetUserCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserCommandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserConfigResponseBodyFreeTier(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        init_base_unit: str = None,
        init_base_value: float = None,
        init_show_unit: str = None,
        init_show_value: str = None,
        is_free_tier_user: bool = None,
        period_base_unit: str = None,
        period_base_value: float = None,
        period_show_unit: str = None,
        period_show_value: str = None,
        start_time: str = None,
        status: str = None,
    ):
        self.end_time = end_time
        self.init_base_unit = init_base_unit
        self.init_base_value = init_base_value
        self.init_show_unit = init_show_unit
        self.init_show_value = init_show_value
        self.is_free_tier_user = is_free_tier_user
        self.period_base_unit = period_base_unit
        self.period_base_value = period_base_value
        self.period_show_unit = period_show_unit
        self.period_show_value = period_show_value
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.init_base_unit is not None:
            result['InitBaseUnit'] = self.init_base_unit
        if self.init_base_value is not None:
            result['InitBaseValue'] = self.init_base_value
        if self.init_show_unit is not None:
            result['InitShowUnit'] = self.init_show_unit
        if self.init_show_value is not None:
            result['InitShowValue'] = self.init_show_value
        if self.is_free_tier_user is not None:
            result['IsFreeTierUser'] = self.is_free_tier_user
        if self.period_base_unit is not None:
            result['PeriodBaseUnit'] = self.period_base_unit
        if self.period_base_value is not None:
            result['PeriodBaseValue'] = self.period_base_value
        if self.period_show_unit is not None:
            result['PeriodShowUnit'] = self.period_show_unit
        if self.period_show_value is not None:
            result['PeriodShowValue'] = self.period_show_value
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InitBaseUnit') is not None:
            self.init_base_unit = m.get('InitBaseUnit')
        if m.get('InitBaseValue') is not None:
            self.init_base_value = m.get('InitBaseValue')
        if m.get('InitShowUnit') is not None:
            self.init_show_unit = m.get('InitShowUnit')
        if m.get('InitShowValue') is not None:
            self.init_show_value = m.get('InitShowValue')
        if m.get('IsFreeTierUser') is not None:
            self.is_free_tier_user = m.get('IsFreeTierUser')
        if m.get('PeriodBaseUnit') is not None:
            self.period_base_unit = m.get('PeriodBaseUnit')
        if m.get('PeriodBaseValue') is not None:
            self.period_base_value = m.get('PeriodBaseValue')
        if m.get('PeriodShowUnit') is not None:
            self.period_show_unit = m.get('PeriodShowUnit')
        if m.get('PeriodShowValue') is not None:
            self.period_show_value = m.get('PeriodShowValue')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetUserConfigResponseBody(TeaModel):
    def __init__(
        self,
        account_sufficient: bool = None,
        code: str = None,
        enable_eci_disk: bool = None,
        free_tier: GetUserConfigResponseBodyFreeTier = None,
        free_tier_spec_available: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.account_sufficient = account_sufficient
        self.code = code
        self.enable_eci_disk = enable_eci_disk
        self.free_tier = free_tier
        self.free_tier_spec_available = free_tier_spec_available
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.free_tier:
            self.free_tier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_sufficient is not None:
            result['AccountSufficient'] = self.account_sufficient
        if self.code is not None:
            result['Code'] = self.code
        if self.enable_eci_disk is not None:
            result['EnableEciDisk'] = self.enable_eci_disk
        if self.free_tier is not None:
            result['FreeTier'] = self.free_tier.to_map()
        if self.free_tier_spec_available is not None:
            result['FreeTierSpecAvailable'] = self.free_tier_spec_available
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountSufficient') is not None:
            self.account_sufficient = m.get('AccountSufficient')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnableEciDisk') is not None:
            self.enable_eci_disk = m.get('EnableEciDisk')
        if m.get('FreeTier') is not None:
            temp_model = GetUserConfigResponseBodyFreeTier()
            self.free_tier = temp_model.from_map(m['FreeTier'])
        if m.get('FreeTierSpecAvailable') is not None:
            self.free_tier_spec_available = m.get('FreeTierSpecAvailable')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEcsSpecsRequest(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_type: str = None,
        sort_by: str = None,
    ):
        # The accelerator type.
        # 
        # *   CPU: Only CPU computing is used.
        # *   GPU: GPUs are used to accelerate computing.
        # 
        # This parameter is required.
        self.accelerator_type = accelerator_type
        # The sorting order. Valid values:
        # 
        # *   ASC
        # *   DESC
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        self.resource_type = resource_type
        # The field by which the query results are sorted. Set the value to gmtCreate.
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
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
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
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListEcsSpecsResponseBodyEcsSpecsLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The label key added to the ECS specification.
        self.key = key
        # The label value added to the ECS specification.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListEcsSpecsResponseBodyEcsSpecs(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        cpu: int = None,
        currency: str = None,
        gpu: int = None,
        gpumemory_size: float = None,
        gputype: str = None,
        instance_bandwidth_rx: int = None,
        instance_type: str = None,
        is_available: bool = None,
        labels: List[ListEcsSpecsResponseBodyEcsSpecsLabels] = None,
        memory: float = None,
        price: float = None,
        spot_stock_status: str = None,
        system_disk_capacity: int = None,
    ):
        # The accelerator type.
        self.accelerator_type = accelerator_type
        # The number of vCPUs.
        self.cpu = cpu
        # The currency unit.
        self.currency = currency
        # The number of GPUs.
        self.gpu = gpu
        self.gpumemory_size = gpumemory_size
        # The GPU type. Valid values:
        # 
        # *   V100
        # *   A100
        # *   A10
        # *   T4
        # *   P100
        self.gputype = gputype
        # The inbound bandwidth of the instance.
        self.instance_bandwidth_rx = instance_bandwidth_rx
        # The instance type.
        self.instance_type = instance_type
        # Indicates whether the resource was available.
        self.is_available = is_available
        # The labels of the ECS specification.
        self.labels = labels
        # The memory size. Unit: GB.
        self.memory = memory
        # The price.
        self.price = price
        self.spot_stock_status = spot_stock_status
        # The size of the system disk. Unit: GB.
        self.system_disk_capacity = system_disk_capacity

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

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
        if self.gpumemory_size is not None:
            result['GPUMemorySize'] = self.gpumemory_size
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.instance_bandwidth_rx is not None:
            result['InstanceBandwidthRx'] = self.instance_bandwidth_rx
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.is_available is not None:
            result['IsAvailable'] = self.is_available
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.price is not None:
            result['Price'] = self.price
        if self.spot_stock_status is not None:
            result['SpotStockStatus'] = self.spot_stock_status
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
        if m.get('GPUMemorySize') is not None:
            self.gpumemory_size = m.get('GPUMemorySize')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('InstanceBandwidthRx') is not None:
            self.instance_bandwidth_rx = m.get('InstanceBandwidthRx')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListEcsSpecsResponseBodyEcsSpecsLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('SpotStockStatus') is not None:
            self.spot_stock_status = m.get('SpotStockStatus')
        if m.get('SystemDiskCapacity') is not None:
            self.system_disk_capacity = m.get('SystemDiskCapacity')
        return self


class ListEcsSpecsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        ecs_specs: List[ListEcsSpecsResponseBodyEcsSpecs] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The specifications of the ECS instances returned on this page.
        self.ecs_specs = ecs_specs
        # The HTTP status code. Valid values:
        # 
        # *   400
        # *   404
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of ECS instances.
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
        if self.code is not None:
            result['Code'] = self.code
        result['EcsSpecs'] = []
        if self.ecs_specs is not None:
            for k in self.ecs_specs:
                result['EcsSpecs'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.ecs_specs = []
        if m.get('EcsSpecs') is not None:
            for k in m.get('EcsSpecs'):
                temp_model = ListEcsSpecsResponseBodyEcsSpecs()
                self.ecs_specs.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEcsSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEcsSpecsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEcsSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceSnapshotRequest(TeaModel):
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


class ListInstanceSnapshotResponseBodySnapshotsLabels(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListInstanceSnapshotResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        exclude_paths: List[str] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_url: str = None,
        instance_id: str = None,
        labels: List[ListInstanceSnapshotResponseBodySnapshotsLabels] = None,
        reason_code: str = None,
        reason_message: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        status: str = None,
    ):
        self.exclude_paths = exclude_paths
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.image_id = image_id
        self.image_url = image_url
        self.instance_id = instance_id
        self.labels = labels
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.snapshot_id = snapshot_id
        self.snapshot_name = snapshot_name
        self.status = status

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_paths is not None:
            result['ExcludePaths'] = self.exclude_paths
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
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
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
        if m.get('ExcludePaths') is not None:
            self.exclude_paths = m.get('ExcludePaths')
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
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListInstanceSnapshotResponseBodySnapshotsLabels()
                self.labels.append(temp_model.from_map(k))
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


class ListInstanceSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        snapshots: List[ListInstanceSnapshotResponseBodySnapshots] = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.snapshots = snapshots
        self.success = success
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = ListInstanceSnapshotResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceStatisticsRequest(TeaModel):
    def __init__(
        self,
        workspace_ids: str = None,
    ):
        # This parameter is required.
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


class ListInstanceStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        statistics: Dict[str, dict] = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.statistics = statistics
        self.success = success

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInstanceStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstanceStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        accessibility: str = None,
        create_user_id: str = None,
        gpu_type: str = None,
        image_name: str = None,
        instance_id: str = None,
        instance_name: str = None,
        labels: Dict[str, Any] = None,
        max_cpu: str = None,
        max_gpu: str = None,
        max_gpu_memory: str = None,
        max_memory: str = None,
        min_cpu: str = None,
        min_gpu: str = None,
        min_gpu_memory: str = None,
        min_memory: str = None,
        order: str = None,
        oversold_info: str = None,
        oversold_type: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_type: str = None,
        resource_id: str = None,
        sort_by: str = None,
        status: str = None,
        tag: List[ListInstancesRequestTag] = None,
        workspace_id: str = None,
    ):
        # The accelerator type.
        # 
        # *   CPU: Only CPU computing is used.
        # *   GPU: GPUs are used to accelerate computing.
        self.accelerator_type = accelerator_type
        # The accessibility. Valid values:
        # 
        # *   PRIVATE (default): The instances are accessible only to you and the administrator of the workspace.
        # *   PUBLIC: The instances are accessible only to all members in the workspace.
        self.accessibility = accessibility
        # The UID of the creator.
        self.create_user_id = create_user_id
        # The GPU type.
        self.gpu_type = gpu_type
        # The image name.
        self.image_name = image_name
        # The instance ID. You can call [ListInstances](https://help.aliyun.com/document_detail/470439.html) to obtain the instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The labels. A maximum of four labels are supported.
        self.labels = labels
        # The maximum number of CPUs. Unit: 0.001 CPU. The value 1000 indicates one CPU.
        self.max_cpu = max_cpu
        # The maximum number of GPUs. Unit: 0.001 GPU. The value 1000 indicates one GPU.
        self.max_gpu = max_gpu
        # The maximum memory size per GPU card. Unit: GB.
        self.max_gpu_memory = max_gpu_memory
        # The maximum memory size. Unit: GB.
        self.max_memory = max_memory
        # The minimum number of CPUs. Unit: 0.001 CPU. The value 1000 indicates one CPU.
        self.min_cpu = min_cpu
        # The minimum number of GPUs. Unit: 0.001 GPU. The value 1000 indicates one GPU.
        self.min_gpu = min_gpu
        # The minimum memory size per GPU card. Unit: GB.
        self.min_gpu_memory = min_gpu_memory
        # The minimum memory size. Unit: GB.
        self.min_memory = min_memory
        # The order that you use to sort the query results.
        # 
        # Valid values:
        # 
        # *   ASC
        # *   DESC
        self.order = order
        self.oversold_info = oversold_info
        self.oversold_type = oversold_type
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo
        # *   Subscription
        self.payment_type = payment_type
        # The resource group ID. If you leave this parameter empty, the instances in the pay-as-you-go resource group are queried. If you set this parameter to ALL, all instances are queried.
        self.resource_id = resource_id
        # The field that you use to sort the query results.
        # 
        # Valid values:
        # 
        # *   Priority
        # *   GmtCreateTime
        # *   GmtModifiedTime
        self.sort_by = sort_by
        # The instance status.
        # 
        # Valid values:
        # 
        # *   Creating
        # *   SaveFailed
        # *   Stopped
        # *   Failed
        # *   ResourceAllocating
        # *   Stopping
        # *   Updating
        # *   Saving
        # *   Queuing
        # *   Recovering
        # *   Starting
        # *   Running
        # *   Saved
        # *   Deleting
        # *   EnvPreparing
        self.status = status
        # The tags.
        self.tag = tag
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.max_cpu is not None:
            result['MaxCpu'] = self.max_cpu
        if self.max_gpu is not None:
            result['MaxGpu'] = self.max_gpu
        if self.max_gpu_memory is not None:
            result['MaxGpuMemory'] = self.max_gpu_memory
        if self.max_memory is not None:
            result['MaxMemory'] = self.max_memory
        if self.min_cpu is not None:
            result['MinCpu'] = self.min_cpu
        if self.min_gpu is not None:
            result['MinGpu'] = self.min_gpu
        if self.min_gpu_memory is not None:
            result['MinGpuMemory'] = self.min_gpu_memory
        if self.min_memory is not None:
            result['MinMemory'] = self.min_memory
        if self.order is not None:
            result['Order'] = self.order
        if self.oversold_info is not None:
            result['OversoldInfo'] = self.oversold_info
        if self.oversold_type is not None:
            result['OversoldType'] = self.oversold_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('MaxCpu') is not None:
            self.max_cpu = m.get('MaxCpu')
        if m.get('MaxGpu') is not None:
            self.max_gpu = m.get('MaxGpu')
        if m.get('MaxGpuMemory') is not None:
            self.max_gpu_memory = m.get('MaxGpuMemory')
        if m.get('MaxMemory') is not None:
            self.max_memory = m.get('MaxMemory')
        if m.get('MinCpu') is not None:
            self.min_cpu = m.get('MinCpu')
        if m.get('MinGpu') is not None:
            self.min_gpu = m.get('MinGpu')
        if m.get('MinGpuMemory') is not None:
            self.min_gpu_memory = m.get('MinGpuMemory')
        if m.get('MinMemory') is not None:
            self.min_memory = m.get('MinMemory')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OversoldInfo') is not None:
            self.oversold_info = m.get('OversoldInfo')
        if m.get('OversoldType') is not None:
            self.oversold_type = m.get('OversoldType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        accessibility: str = None,
        create_user_id: str = None,
        gpu_type: str = None,
        image_name: str = None,
        instance_id: str = None,
        instance_name: str = None,
        labels_shrink: str = None,
        max_cpu: str = None,
        max_gpu: str = None,
        max_gpu_memory: str = None,
        max_memory: str = None,
        min_cpu: str = None,
        min_gpu: str = None,
        min_gpu_memory: str = None,
        min_memory: str = None,
        order: str = None,
        oversold_info: str = None,
        oversold_type: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_type: str = None,
        resource_id: str = None,
        sort_by: str = None,
        status: str = None,
        tag_shrink: str = None,
        workspace_id: str = None,
    ):
        # The accelerator type.
        # 
        # *   CPU: Only CPU computing is used.
        # *   GPU: GPUs are used to accelerate computing.
        self.accelerator_type = accelerator_type
        # The accessibility. Valid values:
        # 
        # *   PRIVATE (default): The instances are accessible only to you and the administrator of the workspace.
        # *   PUBLIC: The instances are accessible only to all members in the workspace.
        self.accessibility = accessibility
        # The UID of the creator.
        self.create_user_id = create_user_id
        # The GPU type.
        self.gpu_type = gpu_type
        # The image name.
        self.image_name = image_name
        # The instance ID. You can call [ListInstances](https://help.aliyun.com/document_detail/470439.html) to obtain the instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The labels. A maximum of four labels are supported.
        self.labels_shrink = labels_shrink
        # The maximum number of CPUs. Unit: 0.001 CPU. The value 1000 indicates one CPU.
        self.max_cpu = max_cpu
        # The maximum number of GPUs. Unit: 0.001 GPU. The value 1000 indicates one GPU.
        self.max_gpu = max_gpu
        # The maximum memory size per GPU card. Unit: GB.
        self.max_gpu_memory = max_gpu_memory
        # The maximum memory size. Unit: GB.
        self.max_memory = max_memory
        # The minimum number of CPUs. Unit: 0.001 CPU. The value 1000 indicates one CPU.
        self.min_cpu = min_cpu
        # The minimum number of GPUs. Unit: 0.001 GPU. The value 1000 indicates one GPU.
        self.min_gpu = min_gpu
        # The minimum memory size per GPU card. Unit: GB.
        self.min_gpu_memory = min_gpu_memory
        # The minimum memory size. Unit: GB.
        self.min_memory = min_memory
        # The order that you use to sort the query results.
        # 
        # Valid values:
        # 
        # *   ASC
        # *   DESC
        self.order = order
        self.oversold_info = oversold_info
        self.oversold_type = oversold_type
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo
        # *   Subscription
        self.payment_type = payment_type
        # The resource group ID. If you leave this parameter empty, the instances in the pay-as-you-go resource group are queried. If you set this parameter to ALL, all instances are queried.
        self.resource_id = resource_id
        # The field that you use to sort the query results.
        # 
        # Valid values:
        # 
        # *   Priority
        # *   GmtCreateTime
        # *   GmtModifiedTime
        self.sort_by = sort_by
        # The instance status.
        # 
        # Valid values:
        # 
        # *   Creating
        # *   SaveFailed
        # *   Stopped
        # *   Failed
        # *   ResourceAllocating
        # *   Stopping
        # *   Updating
        # *   Saving
        # *   Queuing
        # *   Recovering
        # *   Starting
        # *   Running
        # *   Saved
        # *   Deleting
        # *   EnvPreparing
        self.status = status
        # The tags.
        self.tag_shrink = tag_shrink
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.labels_shrink is not None:
            result['Labels'] = self.labels_shrink
        if self.max_cpu is not None:
            result['MaxCpu'] = self.max_cpu
        if self.max_gpu is not None:
            result['MaxGpu'] = self.max_gpu
        if self.max_gpu_memory is not None:
            result['MaxGpuMemory'] = self.max_gpu_memory
        if self.max_memory is not None:
            result['MaxMemory'] = self.max_memory
        if self.min_cpu is not None:
            result['MinCpu'] = self.min_cpu
        if self.min_gpu is not None:
            result['MinGpu'] = self.min_gpu
        if self.min_gpu_memory is not None:
            result['MinGpuMemory'] = self.min_gpu_memory
        if self.min_memory is not None:
            result['MinMemory'] = self.min_memory
        if self.order is not None:
            result['Order'] = self.order
        if self.oversold_info is not None:
            result['OversoldInfo'] = self.oversold_info
        if self.oversold_type is not None:
            result['OversoldType'] = self.oversold_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Labels') is not None:
            self.labels_shrink = m.get('Labels')
        if m.get('MaxCpu') is not None:
            self.max_cpu = m.get('MaxCpu')
        if m.get('MaxGpu') is not None:
            self.max_gpu = m.get('MaxGpu')
        if m.get('MaxGpuMemory') is not None:
            self.max_gpu_memory = m.get('MaxGpuMemory')
        if m.get('MaxMemory') is not None:
            self.max_memory = m.get('MaxMemory')
        if m.get('MinCpu') is not None:
            self.min_cpu = m.get('MinCpu')
        if m.get('MinGpu') is not None:
            self.min_gpu = m.get('MinGpu')
        if m.get('MinGpuMemory') is not None:
            self.min_gpu_memory = m.get('MinGpuMemory')
        if m.get('MinMemory') is not None:
            self.min_memory = m.get('MinMemory')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OversoldInfo') is not None:
            self.oversold_info = m.get('OversoldInfo')
        if m.get('OversoldType') is not None:
            self.oversold_type = m.get('OversoldType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListInstancesResponseBodyInstancesAffinityCPU(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Indicates whether the CPU affinity feature was enabled.
        # 
        # true false
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ListInstancesResponseBodyInstancesAffinity(TeaModel):
    def __init__(
        self,
        cpu: ListInstancesResponseBodyInstancesAffinityCPU = None,
    ):
        # The CPU affinity configuration. Only subscription instances that use general-purpose computing resources support CPU affinity configuration.
        self.cpu = cpu

    def validate(self):
        if self.cpu:
            self.cpu.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = ListInstancesResponseBodyInstancesAffinityCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        return self


class ListInstancesResponseBodyInstancesCloudDisks(TeaModel):
    def __init__(
        self,
        capacity: str = None,
        mount_path: str = None,
        path: str = None,
        sub_type: str = None,
    ):
        # The cloud disk capacity.
        self.capacity = capacity
        # The mount path of the cloud disk in the container.
        self.mount_path = mount_path
        # The directory on the cloud disk that is mounted to the container.
        self.path = path
        # The cloud disk type. The value rootfs indicates that the cloud disk is used as the root file system (rootfs).
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.path is not None:
            result['Path'] = self.path
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class ListInstancesResponseBodyInstancesDatasets(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
        dataset_version: str = None,
        dynamic: bool = None,
        mount_access: str = None,
        mount_path: str = None,
        option_type: str = None,
        options: str = None,
        uri: str = None,
    ):
        # The dataset ID.
        self.dataset_id = dataset_id
        # The dataset version.
        self.dataset_version = dataset_version
        # Indicates whether dynamic mounting was enabled. Default value: false.
        self.dynamic = dynamic
        # The read and write permissions. Valid values: RW and RO.
        self.mount_access = mount_access
        # The mount path in the container.
        self.mount_path = mount_path
        # The type of the mount option.
        self.option_type = option_type
        # The mount type of the dataset.
        self.options = options
        # The dataset URI.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic
        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.option_type is not None:
            result['OptionType'] = self.option_type
        if self.options is not None:
            result['Options'] = self.options
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')
        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('OptionType') is not None:
            self.option_type = m.get('OptionType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class ListInstancesResponseBodyInstancesIdleInstanceCuller(TeaModel):
    def __init__(
        self,
        cpu_percent_threshold: int = None,
        gpu_percent_threshold: int = None,
        idle_time_in_minutes: int = None,
        instance_id: str = None,
        max_idle_time_in_minutes: int = None,
    ):
        # The CPU utilization threshold. Unit: percentage. Valid values: 1 to 100. If the CPU utilization of the instance is lower than this threshold, the instance is considered idle.
        self.cpu_percent_threshold = cpu_percent_threshold
        # The GPU utilization threshold. Unit: percentage. Valid values: 1 to 100. This parameter takes effect only if the instance is of the GPU instance type. If both CPU and GPU utilization is lower than the thresholds, the instance is considered idle.
        self.gpu_percent_threshold = gpu_percent_threshold
        # The time duration for which the instance is idle. Unit: minutes.
        self.idle_time_in_minutes = idle_time_in_minutes
        # The instance ID.
        self.instance_id = instance_id
        # The maximum time duration for which the instance is idle. Unit: minutes. If the time duration for which the instance is idle exceeds this value, the system automatically stops the instance.
        self.max_idle_time_in_minutes = max_idle_time_in_minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_percent_threshold is not None:
            result['CpuPercentThreshold'] = self.cpu_percent_threshold
        if self.gpu_percent_threshold is not None:
            result['GpuPercentThreshold'] = self.gpu_percent_threshold
        if self.idle_time_in_minutes is not None:
            result['IdleTimeInMinutes'] = self.idle_time_in_minutes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_idle_time_in_minutes is not None:
            result['MaxIdleTimeInMinutes'] = self.max_idle_time_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPercentThreshold') is not None:
            self.cpu_percent_threshold = m.get('CpuPercentThreshold')
        if m.get('GpuPercentThreshold') is not None:
            self.gpu_percent_threshold = m.get('GpuPercentThreshold')
        if m.get('IdleTimeInMinutes') is not None:
            self.idle_time_in_minutes = m.get('IdleTimeInMinutes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxIdleTimeInMinutes') is not None:
            self.max_idle_time_in_minutes = m.get('MaxIdleTimeInMinutes')
        return self


class ListInstancesResponseBodyInstancesInstanceShutdownTimer(TeaModel):
    def __init__(
        self,
        due_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        remaining_time_in_ms: int = None,
    ):
        # The scheduled stop time.
        self.due_time = due_time
        # The time when the instance was created.
        self.gmt_create_time = gmt_create_time
        # The time when the instance was modified.
        self.gmt_modified_time = gmt_modified_time
        # The instance ID.
        self.instance_id = instance_id
        # The remaining time before the instance is stopped.
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


class ListInstancesResponseBodyInstancesInstanceSnapshotList(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        reason_code: str = None,
        reason_message: str = None,
        repository_url: str = None,
        status: str = None,
    ):
        # The time when the snapshot was created.
        self.gmt_create_time = gmt_create_time
        # The time when the snapshot was modified.
        self.gmt_modified_time = gmt_modified_time
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image URL.
        self.image_url = image_url
        # The error code of the instance snapshot.
        self.reason_code = reason_code
        # The error message of the instance snapshot.
        self.reason_message = reason_message
        # The URL of the image repository.
        self.repository_url = repository_url
        # The status of the instance snapshot.
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
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
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
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyInstancesLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The custom label key.
        self.key = key
        # The custom label value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListInstancesResponseBodyInstancesLatestSnapshot(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        reason_code: str = None,
        reason_message: str = None,
        repository_url: str = None,
        status: str = None,
    ):
        # The time when the snapshot was created.
        self.gmt_create_time = gmt_create_time
        # The time when the snapshot was modified.
        self.gmt_modified_time = gmt_modified_time
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image URL.
        self.image_url = image_url
        # The error code of the instance snapshot.
        self.reason_code = reason_code
        # The error message of the instance snapshot.
        self.reason_message = reason_message
        # The URL of the image repository.
        self.repository_url = repository_url
        # The status of the instance snapshot.
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
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
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
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyInstancesRequestedResource(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gputype: str = None,
        memory: str = None,
        shared_memory: str = None,
    ):
        # The number of CPU cores.
        self.cpu = cpu
        # The number of GPUs.
        self.gpu = gpu
        # The GPU memory type.
        self.gputype = gputype
        # The memory size.
        self.memory = memory
        # The size of the shared memory.
        self.shared_memory = shared_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')
        return self


class ListInstancesResponseBodyInstancesTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListInstancesResponseBodyInstancesUserVpc(TeaModel):
    def __init__(
        self,
        bandwidth_limit: BandwidthLimit = None,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        forward_infos: List[ForwardInfoResponse] = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.bandwidth_limit = bandwidth_limit
        # The default route.
        self.default_route = default_route
        # The extended CIDR blocks.
        self.extended_cidrs = extended_cidrs
        # The forward information.
        self.forward_infos = forward_infos
        # The security group ID.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.bandwidth_limit:
            self.bandwidth_limit.validate()
        if self.forward_infos:
            for k in self.forward_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit.to_map()
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        result['ForwardInfos'] = []
        if self.forward_infos is not None:
            for k in self.forward_infos:
                result['ForwardInfos'].append(k.to_map() if k else None)
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            temp_model = BandwidthLimit()
            self.bandwidth_limit = temp_model.from_map(m['BandwidthLimit'])
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        self.forward_infos = []
        if m.get('ForwardInfos') is not None:
            for k in m.get('ForwardInfos'):
                temp_model = ForwardInfoResponse()
                self.forward_infos.append(temp_model.from_map(k))
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        accessibility: str = None,
        accumulated_running_time_in_ms: int = None,
        affinity: ListInstancesResponseBodyInstancesAffinity = None,
        cloud_disks: List[ListInstancesResponseBodyInstancesCloudDisks] = None,
        credential_config: CredentialConfig = None,
        datasets: List[ListInstancesResponseBodyInstancesDatasets] = None,
        driver: str = None,
        dynamic_mount: DynamicMount = None,
        ecs_spec: str = None,
        environment_variables: Dict[str, str] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        idle_instance_culler: ListInstancesResponseBodyInstancesIdleInstanceCuller = None,
        image_auth: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_shutdown_timer: ListInstancesResponseBodyInstancesInstanceShutdownTimer = None,
        instance_snapshot_list: List[ListInstancesResponseBodyInstancesInstanceSnapshotList] = None,
        instance_url: str = None,
        jupyterlab_url: str = None,
        labels: List[ListInstancesResponseBodyInstancesLabels] = None,
        latest_snapshot: ListInstancesResponseBodyInstancesLatestSnapshot = None,
        oversold_info: str = None,
        oversold_type: str = None,
        payment_type: str = None,
        priority: int = None,
        reason_code: str = None,
        reason_message: str = None,
        requested_resource: ListInstancesResponseBodyInstancesRequestedResource = None,
        resource_id: str = None,
        resource_name: str = None,
        status: str = None,
        tags: List[ListInstancesResponseBodyInstancesTags] = None,
        terminal_url: str = None,
        user_id: str = None,
        user_name: str = None,
        user_vpc: ListInstancesResponseBodyInstancesUserVpc = None,
        web_ideurl: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
        workspace_source: str = None,
    ):
        # The accelerator type of the instance. Valid values:
        # 
        # *   CPU
        # *   GPU
        self.accelerator_type = accelerator_type
        # The accessibility. Valid values:
        # 
        # *   PRIVATE (default): The instances are accessible only to you and the administrator of the workspace.
        # *   PUBLIC: The instances are accessible only to all members in the workspace.
        self.accessibility = accessibility
        # The accumulated running duration. Unit: milliseconds.
        self.accumulated_running_time_in_ms = accumulated_running_time_in_ms
        # The affinity configuration.
        self.affinity = affinity
        # The cloud disks of the instance.
        self.cloud_disks = cloud_disks
        # The credential configuration.
        self.credential_config = credential_config
        # The datasets.
        self.datasets = datasets
        # The NVIDIA driver configuration.
        self.driver = driver
        # The dynamic mount configurations.
        self.dynamic_mount = dynamic_mount
        # The ECS instance type of the instance.
        self.ecs_spec = ecs_spec
        # The environment variables.
        self.environment_variables = environment_variables
        # The time when the instance was created.
        self.gmt_create_time = gmt_create_time
        # The time when the instance was modified.
        self.gmt_modified_time = gmt_modified_time
        # The rule for stopping idle instances.
        self.idle_instance_culler = idle_instance_culler
        # The Base64-encoded account and password for the user\\"s private image. The password will be hidden.
        self.image_auth = image_auth
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image address.
        self.image_url = image_url
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The scheduled stop task.
        self.instance_shutdown_timer = instance_shutdown_timer
        # The instance snapshots.
        self.instance_snapshot_list = instance_snapshot_list
        # The instance URL.
        self.instance_url = instance_url
        # The JupyterLab URL.
        self.jupyterlab_url = jupyterlab_url
        # The custom labels.
        self.labels = labels
        # The user image that was latest saved.
        self.latest_snapshot = latest_snapshot
        self.oversold_info = oversold_info
        self.oversold_type = oversold_type
        # The billing method. Valid values:
        # 
        # *   PayAsYouGo
        # *   Subscription
        self.payment_type = payment_type
        # The priority based on which resources are allocated to instances. Resources are preferentially allocated to instances with higher priorities.
        self.priority = priority
        # The error code of the instance.
        self.reason_code = reason_code
        # The cause of the instance error.
        self.reason_message = reason_message
        # The resource configurations.
        self.requested_resource = requested_resource
        # The resource ID. This parameter is valid only if you set PaymentType to Subscription.
        self.resource_id = resource_id
        # The specifications.
        # 
        # *   In pay-as-you-go scenarios, the value is the specifications of the purchased ECS instance type.
        # *   In subscription scenarios, the value is the requested number of CPU cores and memory size.
        self.resource_name = resource_name
        # The instance status.
        self.status = status
        # The tags.
        self.tags = tags
        # The terminal URL.
        self.terminal_url = terminal_url
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name
        # The virtual private cloud (VPC) configurations.
        self.user_vpc = user_vpc
        # The Web IDE URL.
        self.web_ideurl = web_ideurl
        # The workspace ID.
        self.workspace_id = workspace_id
        # The workspace name.
        self.workspace_name = workspace_name
        # The storage for the workspace. If you leave this parameter empty, the workspace uses File Storage NAS (NAS) storage, cloud disks, or local disks in sequence.
        self.workspace_source = workspace_source

    def validate(self):
        if self.affinity:
            self.affinity.validate()
        if self.cloud_disks:
            for k in self.cloud_disks:
                if k:
                    k.validate()
        if self.credential_config:
            self.credential_config.validate()
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.dynamic_mount:
            self.dynamic_mount.validate()
        if self.idle_instance_culler:
            self.idle_instance_culler.validate()
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.instance_snapshot_list:
            for k in self.instance_snapshot_list:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.latest_snapshot:
            self.latest_snapshot.validate()
        if self.requested_resource:
            self.requested_resource.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
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
        if self.affinity is not None:
            result['Affinity'] = self.affinity.to_map()
        result['CloudDisks'] = []
        if self.cloud_disks is not None:
            for k in self.cloud_disks:
                result['CloudDisks'].append(k.to_map() if k else None)
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.dynamic_mount is not None:
            result['DynamicMount'] = self.dynamic_mount.to_map()
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.idle_instance_culler is not None:
            result['IdleInstanceCuller'] = self.idle_instance_culler.to_map()
        if self.image_auth is not None:
            result['ImageAuth'] = self.image_auth
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
        result['InstanceSnapshotList'] = []
        if self.instance_snapshot_list is not None:
            for k in self.instance_snapshot_list:
                result['InstanceSnapshotList'].append(k.to_map() if k else None)
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.latest_snapshot is not None:
            result['LatestSnapshot'] = self.latest_snapshot.to_map()
        if self.oversold_info is not None:
            result['OversoldInfo'] = self.oversold_info
        if self.oversold_type is not None:
            result['OversoldType'] = self.oversold_type
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.requested_resource is not None:
            result['RequestedResource'] = self.requested_resource.to_map()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ideurl is not None:
            result['WebIDEUrl'] = self.web_ideurl
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        if self.workspace_source is not None:
            result['WorkspaceSource'] = self.workspace_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('AccumulatedRunningTimeInMs') is not None:
            self.accumulated_running_time_in_ms = m.get('AccumulatedRunningTimeInMs')
        if m.get('Affinity') is not None:
            temp_model = ListInstancesResponseBodyInstancesAffinity()
            self.affinity = temp_model.from_map(m['Affinity'])
        self.cloud_disks = []
        if m.get('CloudDisks') is not None:
            for k in m.get('CloudDisks'):
                temp_model = ListInstancesResponseBodyInstancesCloudDisks()
                self.cloud_disks.append(temp_model.from_map(k))
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = ListInstancesResponseBodyInstancesDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('DynamicMount') is not None:
            temp_model = DynamicMount()
            self.dynamic_mount = temp_model.from_map(m['DynamicMount'])
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('IdleInstanceCuller') is not None:
            temp_model = ListInstancesResponseBodyInstancesIdleInstanceCuller()
            self.idle_instance_culler = temp_model.from_map(m['IdleInstanceCuller'])
        if m.get('ImageAuth') is not None:
            self.image_auth = m.get('ImageAuth')
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
            temp_model = ListInstancesResponseBodyInstancesInstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        self.instance_snapshot_list = []
        if m.get('InstanceSnapshotList') is not None:
            for k in m.get('InstanceSnapshotList'):
                temp_model = ListInstancesResponseBodyInstancesInstanceSnapshotList()
                self.instance_snapshot_list.append(temp_model.from_map(k))
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListInstancesResponseBodyInstancesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatestSnapshot') is not None:
            temp_model = ListInstancesResponseBodyInstancesLatestSnapshot()
            self.latest_snapshot = temp_model.from_map(m['LatestSnapshot'])
        if m.get('OversoldInfo') is not None:
            self.oversold_info = m.get('OversoldInfo')
        if m.get('OversoldType') is not None:
            self.oversold_type = m.get('OversoldType')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestedResource') is not None:
            temp_model = ListInstancesResponseBodyInstancesRequestedResource()
            self.requested_resource = temp_model.from_map(m['RequestedResource'])
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListInstancesResponseBodyInstancesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserVpc') is not None:
            temp_model = ListInstancesResponseBodyInstancesUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIDEUrl') is not None:
            self.web_ideurl = m.get('WebIDEUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        if m.get('WorkspaceSource') is not None:
            self.workspace_source = m.get('WorkspaceSource')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instances: List[ListInstancesResponseBodyInstances] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The HTTP status code. Valid values:
        # 
        # *   400
        # *   404
        self.http_status_code = http_status_code
        # The instances returned on this page.
        self.instances = instances
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of instances.
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSystemLogsRequest(TeaModel):
    def __init__(
        self,
        gmt_end_time: str = None,
        gmt_start_time: str = None,
        instance_id: str = None,
        log_level: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        problem_category: str = None,
        sort_by: str = None,
        source_request_id: str = None,
        source_type: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_end_time = gmt_end_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_start_time = gmt_start_time
        self.instance_id = instance_id
        self.log_level = log_level
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.problem_category = problem_category
        self.sort_by = sort_by
        self.source_request_id = source_request_id
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.problem_category is not None:
            result['ProblemCategory'] = self.problem_category
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source_request_id is not None:
            result['SourceRequestId'] = self.source_request_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProblemCategory') is not None:
            self.problem_category = m.get('ProblemCategory')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SourceRequestId') is not None:
            self.source_request_id = m.get('SourceRequestId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class ListSystemLogsResponseBodySystemLogs(TeaModel):
    def __init__(
        self,
        content: str = None,
        gmt_create_time: str = None,
        level: str = None,
    ):
        self.content = content
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create_time = gmt_create_time
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class ListSystemLogsResponseBody(TeaModel):
    def __init__(
        self,
        system_logs: List[ListSystemLogsResponseBodySystemLogs] = None,
        total_count: int = None,
    ):
        self.system_logs = system_logs
        self.total_count = total_count

    def validate(self):
        if self.system_logs:
            for k in self.system_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemLogs'] = []
        if self.system_logs is not None:
            for k in self.system_logs:
                result['SystemLogs'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_logs = []
        if m.get('SystemLogs') is not None:
            for k in m.get('SystemLogs'):
                temp_model = ListSystemLogsResponseBodySystemLogs()
                self.system_logs.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSystemLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSystemLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSystemLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
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


class StopInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequestAffinityCPU(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Specifies whether CPU affinity is enabled.
        # 
        # *   true
        # *   false
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class UpdateInstanceRequestAffinity(TeaModel):
    def __init__(
        self,
        cpu: UpdateInstanceRequestAffinityCPU = None,
    ):
        # The CPU affinity configuration. Only subscription instances that use general-purpose computing resources support CPU affinity configuration.
        self.cpu = cpu

    def validate(self):
        if self.cpu:
            self.cpu.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = UpdateInstanceRequestAffinityCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        return self


class UpdateInstanceRequestCloudDisks(TeaModel):
    def __init__(
        self,
        capacity: str = None,
        sub_type: str = None,
    ):
        # If **Resource Type** is **Public Resource** or if **Resource Quota** is subscription-based general-purpose computing resources (CPU cores ≥ 2 and memory ≥ 4 GB, or configured with GPU):
        # 
        # Each instance has a free system disk quota of 100 GiB for persistent storage. **If the DSW instance is stopped and not launched for more than 15 days, the disk is cleared**. The disk can be expanded. For specific pricing, refer to the console.
        # 
        # **\
        # 
        # **Warning**\
        # 
        # *   After the expansion, you cannot reduce the storage space. Proceed with caution.
        # 
        # *   After the expansion, the disk is not cleared if the instance is stopped for more than 15 days. However, it will continue to incur fees.
        # 
        # *   If you delete the instance, the system disk is also released and the data stored in the disk is deleted. Make sure that you have backed up your data before you delete the instance.
        # 
        # If you need persistent storage, you can **mount a dataset** or add the OSS, NAS, or CPFS path to the **storage path**.
        self.capacity = capacity
        # Disk type:
        # 
        # *   rootfs: Mounts the disk as a system disk. The system environment is stored on the disk.
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class UpdateInstanceRequestDatasets(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
        dataset_version: str = None,
        dynamic: bool = None,
        mount_access: str = None,
        mount_path: str = None,
        option_type: str = None,
        options: str = None,
        uri: str = None,
    ):
        # The dataset ID. If the dataset is read-only, you cannot change the dataset pemission from read-only to read and write by using MountAccess.
        # 
        # You can call [ListDatasets](https://help.aliyun.com/document_detail/457222.html) to obtain the dataset ID. If you configure the dataset ID, you cannot configure the dataset URI.
        self.dataset_id = dataset_id
        # The dataset version. You must also configure DatasetId. If you leave this parameter empty, the value v1 is used by default.
        self.dataset_version = dataset_version
        # Specifies whether dynamic mounting is enabled. Default value: false.
        # 
        # *   Currently, only instances using general-purpose computing resources are supported.
        # *   Currently, only OSS datasets are supported. The mounted datasets are read-only.
        # *   The MountPath of the dynamically mounted dataset must be a subpath of the root path. Example: /mnt/dynamic/data1/\
        # *   A dynamically mounted dataset must be after non-dynamic datasets.
        self.dynamic = dynamic
        # The read and write permissions of the dataset. If the dataset is read-only, it cannot be changed to read and write.
        self.mount_access = mount_access
        # The mount path of the dataset.
        self.mount_path = mount_path
        # The mount type. You cannot specify Options at the same time. This is deprecated, you can use Options instead.
        self.option_type = option_type
        # The custom dataset mount options. Only OSS is supported. You cannot specify OptionType at the same time. For more information, see [DSW mount configurations](https://www.alibabacloud.com/help/en/pai/user-guide/read-and-write-dataset-data).
        self.options = options
        # The URI of the storage service directory, which can be directly mounted. This parameter is mutually exclusive with DatasetId.
        # 
        # URI formats of different types of storage:
        # 
        # *   OSS: oss://bucket-name.oss-cn-shanghai-internal.aliyuncs.com/data/path/\
        # *   NAS: nas://29\\*\\*d-b12\\*\\*\\*\\*446.cn-hangzhou.nas.aliyuncs.com/data/path/\
        # *   Extreme NAS: nas://29\\*\\*\\*\\*123-y\\*\\*r.cn-hangzhou.extreme.nas.aliyuncs.com/data/path/\
        # *   CPFS: cpfs://cpfs-213\\*\\*\\*\\*87.cn-wulanchabu/ptc-292\\*\\*\\*\\*\\*cbb/exp-290\\*\\*\\*\\*\\*\\*\\*\\*03e/data/path/\
        # *   Lingjun CPFS: bmcpfs://cpfs-290\\*\\*\\*\\*\\*\\*foflh-vpc-x\\*\\*\\*\\*8r.cn-wulanchabu.cpfs.aliyuncs.com/data/path/\
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic
        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.option_type is not None:
            result['OptionType'] = self.option_type
        if self.options is not None:
            result['Options'] = self.options
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')
        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('OptionType') is not None:
            self.option_type = m.get('OptionType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class UpdateInstanceRequestRequestedResource(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gputype: str = None,
        memory: str = None,
        shared_memory: str = None,
    ):
        # The number of vCPU cores.
        self.cpu = cpu
        # The number of GPUs.
        self.gpu = gpu
        # The GPU type.
        self.gputype = gputype
        # The memory size. Unit: GB.
        self.memory = memory
        # The shared memory size. Unit: GB.
        self.shared_memory = shared_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')
        return self


class UpdateInstanceRequestUserCommandOnStart(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class UpdateInstanceRequestUserCommand(TeaModel):
    def __init__(
        self,
        on_start: UpdateInstanceRequestUserCommandOnStart = None,
    ):
        self.on_start = on_start

    def validate(self):
        if self.on_start:
            self.on_start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.on_start is not None:
            result['OnStart'] = self.on_start.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnStart') is not None:
            temp_model = UpdateInstanceRequestUserCommandOnStart()
            self.on_start = temp_model.from_map(m['OnStart'])
        return self


class UpdateInstanceRequestUserVpc(TeaModel):
    def __init__(
        self,
        bandwidth_limit: BandwidthLimit = None,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        forward_infos: List[ForwardInfo] = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.bandwidth_limit = bandwidth_limit
        # The default route. Valid values:
        # 
        # *   eth0: The default network interface is used to access the Internet through the public gateway.
        # *   eth1: The user\\"s Elastic Network Interface is used to access the Internet through the private gateway.
        self.default_route = default_route
        # The extended CIDR blocks.
        # 
        # *   If you leave VSwitchId empty, this parameter is not required and the system automatically obtains all CIDR blocks in the VPC.
        # *   If VSwitchId is not empty, this parameter is required. Specify all CIDR blocks in the VPC.
        self.extended_cidrs = extended_cidrs
        # The forward configuration of the instance.
        self.forward_infos = forward_infos
        # The security group ID.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.bandwidth_limit:
            self.bandwidth_limit.validate()
        if self.forward_infos:
            for k in self.forward_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit.to_map()
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        result['ForwardInfos'] = []
        if self.forward_infos is not None:
            for k in self.forward_infos:
                result['ForwardInfos'].append(k.to_map() if k else None)
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            temp_model = BandwidthLimit()
            self.bandwidth_limit = temp_model.from_map(m['BandwidthLimit'])
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        self.forward_infos = []
        if m.get('ForwardInfos') is not None:
            for k in m.get('ForwardInfos'):
                temp_model = ForwardInfo()
                self.forward_infos.append(temp_model.from_map(k))
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        affinity: UpdateInstanceRequestAffinity = None,
        cloud_disks: List[UpdateInstanceRequestCloudDisks] = None,
        credential_config: CredentialConfig = None,
        datasets: List[UpdateInstanceRequestDatasets] = None,
        disassociate_credential: bool = None,
        disassociate_datasets: bool = None,
        disassociate_driver: bool = None,
        disassociate_environment_variables: bool = None,
        disassociate_forward_infos: bool = None,
        disassociate_user_command: bool = None,
        disassociate_vpc: bool = None,
        driver: str = None,
        dynamic_mount: DynamicMount = None,
        ecs_spec: str = None,
        environment_variables: Dict[str, Any] = None,
        image_auth: str = None,
        image_id: str = None,
        image_url: str = None,
        instance_name: str = None,
        oversold_type: str = None,
        priority: int = None,
        requested_resource: UpdateInstanceRequestRequestedResource = None,
        user_command: UpdateInstanceRequestUserCommand = None,
        user_id: str = None,
        user_vpc: UpdateInstanceRequestUserVpc = None,
        workspace_source: str = None,
    ):
        # The visibility of the instance.
        # 
        # Valid values:
        # 
        # *   PUBLIC: Accessible to all members in the workspace.
        # *   PRIVATE: Accessible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The affinity configuration.
        self.affinity = affinity
        # The cloud disks.
        self.cloud_disks = cloud_disks
        # The credential configuration.
        self.credential_config = credential_config
        # The datasets.
        self.datasets = datasets
        # Specifies whether to delete the credential injection information.
        self.disassociate_credential = disassociate_credential
        # Specifies whether to delete the associated datasets.
        # 
        # *   true
        # *   false
        self.disassociate_datasets = disassociate_datasets
        # Specifies whether to delete the NVIDIA driver configuration.
        self.disassociate_driver = disassociate_driver
        self.disassociate_environment_variables = disassociate_environment_variables
        # Specifies whether to delete the associated forward information.
        self.disassociate_forward_infos = disassociate_forward_infos
        self.disassociate_user_command = disassociate_user_command
        # Specifies whether to delete the associated user VPC.
        self.disassociate_vpc = disassociate_vpc
        # The NVIDIA driver configuration.
        self.driver = driver
        # The dynamic mount configuration.
        self.dynamic_mount = dynamic_mount
        # The ECS instance type of the instance. You can call [ListEcsSpecs](https://help.aliyun.com/document_detail/470423.html) to obtain the ECS instance type.
        self.ecs_spec = ecs_spec
        self.environment_variables = environment_variables
        # The Base64-encoded account and password for the user‘s private image. The password will be hidden.
        self.image_auth = image_auth
        # The image ID. You can call [ListImages](https://help.aliyun.com/document_detail/449118.html) to obtain the image ID.
        self.image_id = image_id
        # The image address. You can call [ListImages](https://help.aliyun.com/document_detail/449118.html) to obtain the image address.
        self.image_url = image_url
        # The instance name. Format requirements:
        # 
        # *   The name can contain only letters, digits, and underscores (_).
        # *   The name can be up to 27 characters in length.
        self.instance_name = instance_name
        self.oversold_type = oversold_type
        # The priority based on which resources are allocated to instances. Valid values: 1 to 9.
        # 
        # *   1: the lowest priority.
        # *   9 is the highest priority.
        self.priority = priority
        # The resource configurations.
        self.requested_resource = requested_resource
        self.user_command = user_command
        # the User ID of the instance.
        self.user_id = user_id
        # The virtual private cloud (VPC) configurations.
        self.user_vpc = user_vpc
        # Specifies the storage corresponding to the working directory. You can mount disks or datasets to /mnt/workspace at the same time. OSS datasets and dynamically mounted datasets are not supported.
        # 
        # Valid values:
        # 
        # *   rootfsCloudDisk: Mount disk to the working directory.
        # *   Mount path of the dataset, such as /mnt/data: Datasets in URI format only support this method.
        # *   Dataset ID, such as d-vsqjvs\\*\\*\\*\\*rp5l206u: If a single dataset is mounted to multiple paths, the first path is selected. We recommend that you do not use this method, use the mount path instead.
        # 
        # If you leave this parameter empty:
        # 
        # *   If the instance uses cloud disks, cloud disks are selected by default.
        # *   if no disks are available, the first NAS or CPFS dataset is selected as the working directory.
        # *   If no disk, NAS, or CPFS datasets is available, the host space is used.
        self.workspace_source = workspace_source

    def validate(self):
        if self.affinity:
            self.affinity.validate()
        if self.cloud_disks:
            for k in self.cloud_disks:
                if k:
                    k.validate()
        if self.credential_config:
            self.credential_config.validate()
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.dynamic_mount:
            self.dynamic_mount.validate()
        if self.requested_resource:
            self.requested_resource.validate()
        if self.user_command:
            self.user_command.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.affinity is not None:
            result['Affinity'] = self.affinity.to_map()
        result['CloudDisks'] = []
        if self.cloud_disks is not None:
            for k in self.cloud_disks:
                result['CloudDisks'].append(k.to_map() if k else None)
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.disassociate_credential is not None:
            result['DisassociateCredential'] = self.disassociate_credential
        if self.disassociate_datasets is not None:
            result['DisassociateDatasets'] = self.disassociate_datasets
        if self.disassociate_driver is not None:
            result['DisassociateDriver'] = self.disassociate_driver
        if self.disassociate_environment_variables is not None:
            result['DisassociateEnvironmentVariables'] = self.disassociate_environment_variables
        if self.disassociate_forward_infos is not None:
            result['DisassociateForwardInfos'] = self.disassociate_forward_infos
        if self.disassociate_user_command is not None:
            result['DisassociateUserCommand'] = self.disassociate_user_command
        if self.disassociate_vpc is not None:
            result['DisassociateVpc'] = self.disassociate_vpc
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.dynamic_mount is not None:
            result['DynamicMount'] = self.dynamic_mount.to_map()
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.image_auth is not None:
            result['ImageAuth'] = self.image_auth
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.oversold_type is not None:
            result['OversoldType'] = self.oversold_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.requested_resource is not None:
            result['RequestedResource'] = self.requested_resource.to_map()
        if self.user_command is not None:
            result['UserCommand'] = self.user_command.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_source is not None:
            result['WorkspaceSource'] = self.workspace_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Affinity') is not None:
            temp_model = UpdateInstanceRequestAffinity()
            self.affinity = temp_model.from_map(m['Affinity'])
        self.cloud_disks = []
        if m.get('CloudDisks') is not None:
            for k in m.get('CloudDisks'):
                temp_model = UpdateInstanceRequestCloudDisks()
                self.cloud_disks.append(temp_model.from_map(k))
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = UpdateInstanceRequestDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('DisassociateCredential') is not None:
            self.disassociate_credential = m.get('DisassociateCredential')
        if m.get('DisassociateDatasets') is not None:
            self.disassociate_datasets = m.get('DisassociateDatasets')
        if m.get('DisassociateDriver') is not None:
            self.disassociate_driver = m.get('DisassociateDriver')
        if m.get('DisassociateEnvironmentVariables') is not None:
            self.disassociate_environment_variables = m.get('DisassociateEnvironmentVariables')
        if m.get('DisassociateForwardInfos') is not None:
            self.disassociate_forward_infos = m.get('DisassociateForwardInfos')
        if m.get('DisassociateUserCommand') is not None:
            self.disassociate_user_command = m.get('DisassociateUserCommand')
        if m.get('DisassociateVpc') is not None:
            self.disassociate_vpc = m.get('DisassociateVpc')
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('DynamicMount') is not None:
            temp_model = DynamicMount()
            self.dynamic_mount = temp_model.from_map(m['DynamicMount'])
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('ImageAuth') is not None:
            self.image_auth = m.get('ImageAuth')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('OversoldType') is not None:
            self.oversold_type = m.get('OversoldType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RequestedResource') is not None:
            temp_model = UpdateInstanceRequestRequestedResource()
            self.requested_resource = temp_model.from_map(m['RequestedResource'])
        if m.get('UserCommand') is not None:
            temp_model = UpdateInstanceRequestUserCommand()
            self.user_command = temp_model.from_map(m['UserCommand'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = UpdateInstanceRequestUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceSource') is not None:
            self.workspace_source = m.get('WorkspaceSource')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The HTTP status code. Valid values:
        # 
        # *   400
        # *   404
        self.http_status_code = http_status_code
        # The instance ID.
        self.instance_id = instance_id
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceLabelsRequestLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the custom tag.
        # 
        # This parameter is required.
        self.key = key
        # The value of the custom tag.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateInstanceLabelsRequest(TeaModel):
    def __init__(
        self,
        labels: List[UpdateInstanceLabelsRequestLabels] = None,
    ):
        # The tags that you want to update.
        # 
        # This parameter is required.
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = UpdateInstanceLabelsRequestLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class UpdateInstanceLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceLabelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateInstanceLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


