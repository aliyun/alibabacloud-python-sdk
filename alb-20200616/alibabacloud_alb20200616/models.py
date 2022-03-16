# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddEntriesToAclRequestAclEntries(TeaModel):
    def __init__(
        self,
        description: str = None,
        entry: str = None,
    ):
        # 描述信息
        self.description = description
        # 条目
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.entry is not None:
            result['Entry'] = self.entry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        return self


class AddEntriesToAclRequest(TeaModel):
    def __init__(
        self,
        acl_entries: List[AddEntriesToAclRequestAclEntries] = None,
        acl_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
    ):
        # 条目信息列表
        self.acl_entries = acl_entries
        # AclId
        self.acl_id = acl_id
        # 幂等Token
        self.client_token = client_token
        # dryRun
        self.dry_run = dry_run

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = AddEntriesToAclRequestAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class AddEntriesToAclResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # job
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddEntriesToAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddEntriesToAclResponseBody = None,
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
            temp_model = AddEntriesToAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddServersToServerGroupRequestServers(TeaModel):
    def __init__(
        self,
        description: str = None,
        port: int = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        weight: int = None,
    ):
        # 描述信息
        self.description = description
        # 后端端口号
        self.port = port
        # 后端服务器id
        self.server_id = server_id
        # 后端服务器ip
        self.server_ip = server_ip
        # 后端服务器类型
        self.server_type = server_type
        # 后端服务器权重
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class AddServersToServerGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        server_group_id: str = None,
        servers: List[AddServersToServerGroupRequestServers] = None,
    ):
        # 幂等Token
        self.client_token = client_token
        # dryRun
        self.dry_run = dry_run
        # 后端服务器Id
        self.server_group_id = server_group_id
        # 后端服务器
        self.servers = servers

    def validate(self):
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = AddServersToServerGroupRequestServers()
                self.servers.append(temp_model.from_map(k))
        return self


class AddServersToServerGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddServersToServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddServersToServerGroupResponseBody = None,
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
            temp_model = AddServersToServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyHealthCheckTemplateToServerGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        health_check_template_id: str = None,
        server_group_id: str = None,
    ):
        # 幂等Token
        self.client_token = client_token
        # dryRun
        self.dry_run = dry_run
        # 健康检查模板Id
        self.health_check_template_id = health_check_template_id
        # 服务器组Id
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.health_check_template_id is not None:
            result['HealthCheckTemplateId'] = self.health_check_template_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('HealthCheckTemplateId') is not None:
            self.health_check_template_id = m.get('HealthCheckTemplateId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class ApplyHealthCheckTemplateToServerGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApplyHealthCheckTemplateToServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApplyHealthCheckTemplateToServerGroupResponseBody = None,
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
            temp_model = ApplyHealthCheckTemplateToServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAclsWithListenerRequest(TeaModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
        acl_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
    ):
        # 访问控制策略Id
        self.acl_ids = acl_ids
        # 绑定类型
        self.acl_type = acl_type
        # 幂等标识
        self.client_token = client_token
        # 预检此次请求
        self.dry_run = dry_run
        # 监听Id
        self.listener_id = listener_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class AssociateAclsWithListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateAclsWithListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateAclsWithListenerResponseBody = None,
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
            temp_model = AssociateAclsWithListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAdditionalCertificatesWithListenerRequestCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # 证书Id
        self.certificate_id = certificate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class AssociateAdditionalCertificatesWithListenerRequest(TeaModel):
    def __init__(
        self,
        certificates: List[AssociateAdditionalCertificatesWithListenerRequestCertificates] = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
    ):
        # 证书列表
        self.certificates = certificates
        # 幂等Token
        self.client_token = client_token
        # dryRun
        self.dry_run = dry_run
        # 监听Id
        self.listener_id = listener_id

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = AssociateAdditionalCertificatesWithListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class AssociateAdditionalCertificatesWithListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateAdditionalCertificatesWithListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateAdditionalCertificatesWithListenerResponseBody = None,
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
            temp_model = AssociateAdditionalCertificatesWithListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachCommonBandwidthPackageToLoadBalancerRequest(TeaModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
    ):
        # 带宽包ID
        self.bandwidth_package_id = bandwidth_package_id
        # 幂等参数
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 实例ID
        self.load_balancer_id = load_balancer_id
        # 地域ID
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AttachCommonBandwidthPackageToLoadBalancerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachCommonBandwidthPackageToLoadBalancerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachCommonBandwidthPackageToLoadBalancerResponseBody = None,
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
            temp_model = AttachCommonBandwidthPackageToLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAclRequest(TeaModel):
    def __init__(
        self,
        acl_name: str = None,
        client_token: str = None,
        dry_run: bool = None,
        resource_group_id: str = None,
    ):
        # Acl名称
        self.acl_name = acl_name
        # 幂等Token
        self.client_token = client_token
        # dryRun
        self.dry_run = dry_run
        # 资源组Id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateAclResponseBody(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        job_id: str = None,
        request_id: str = None,
    ):
        # AclId
        self.acl_id = acl_id
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAclResponseBody = None,
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
            temp_model = CreateAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHealthCheckTemplateRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        health_check_codes: List[str] = None,
        health_check_connect_port: int = None,
        health_check_host: str = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_path: str = None,
        health_check_protocol: str = None,
        health_check_template_name: str = None,
        health_check_timeout: int = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
    ):
        # 幂等参数
        self.client_token = client_token
        # dryRun
        self.dry_run = dry_run
        # 状态码
        self.health_check_codes = health_check_codes
        # 端口号
        self.health_check_connect_port = health_check_connect_port
        # 域名
        self.health_check_host = health_check_host
        # 版本
        self.health_check_http_version = health_check_http_version
        # 时间间隔
        self.health_check_interval = health_check_interval
        # 方法
        self.health_check_method = health_check_method
        # uri
        self.health_check_path = health_check_path
        # 协议
        self.health_check_protocol = health_check_protocol
        # 名称
        self.health_check_template_name = health_check_template_name
        # 超时时间
        self.health_check_timeout = health_check_timeout
        # 健康阈值
        self.healthy_threshold = healthy_threshold
        # 不健康阈值
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.health_check_codes is not None:
            result['HealthCheckCodes'] = self.health_check_codes
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_host is not None:
            result['HealthCheckHost'] = self.health_check_host
        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.health_check_template_name is not None:
            result['HealthCheckTemplateName'] = self.health_check_template_name
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('HealthCheckCodes') is not None:
            self.health_check_codes = m.get('HealthCheckCodes')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckHost') is not None:
            self.health_check_host = m.get('HealthCheckHost')
        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('HealthCheckTemplateName') is not None:
            self.health_check_template_name = m.get('HealthCheckTemplateName')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class CreateHealthCheckTemplateResponseBody(TeaModel):
    def __init__(
        self,
        health_check_template_id: str = None,
        request_id: str = None,
    ):
        # 健康检查模板ID
        self.health_check_template_id = health_check_template_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_template_id is not None:
            result['HealthCheckTemplateId'] = self.health_check_template_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckTemplateId') is not None:
            self.health_check_template_id = m.get('HealthCheckTemplateId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateHealthCheckTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateHealthCheckTemplateResponseBody = None,
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
            temp_model = CreateHealthCheckTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateListenerRequestCaCertificates(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateListenerRequestCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # 正式标识
        self.certificate_id = certificate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class CreateListenerRequestDefaultActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        # 服务器组ID
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class CreateListenerRequestDefaultActionsForwardGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[CreateListenerRequestDefaultActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # 服务器组列表
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = CreateListenerRequestDefaultActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class CreateListenerRequestDefaultActions(TeaModel):
    def __init__(
        self,
        forward_group_config: CreateListenerRequestDefaultActionsForwardGroupConfig = None,
        type: str = None,
    ):
        # 转发组
        self.forward_group_config = forward_group_config
        # 动作类型
        self.type = type

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = CreateListenerRequestDefaultActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateListenerRequestQuicConfig(TeaModel):
    def __init__(
        self,
        quic_listener_id: str = None,
        quic_upgrade_enabled: bool = None,
    ):
        # 需要关联的QUIC监听ID，HTTPS监听时有效，QuicUpgradeEnabled为true时必选
        self.quic_listener_id = quic_listener_id
        # 是否开启quic升级，HTTPS监听时有效
        self.quic_upgrade_enabled = quic_upgrade_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quic_listener_id is not None:
            result['QuicListenerId'] = self.quic_listener_id
        if self.quic_upgrade_enabled is not None:
            result['QuicUpgradeEnabled'] = self.quic_upgrade_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuicListenerId') is not None:
            self.quic_listener_id = m.get('QuicListenerId')
        if m.get('QuicUpgradeEnabled') is not None:
            self.quic_upgrade_enabled = m.get('QuicUpgradeEnabled')
        return self


class CreateListenerRequestXForwardedForConfig(TeaModel):
    def __init__(
        self,
        xforwarded_for_client_cert_client_verify_alias: str = None,
        xforwarded_for_client_cert_client_verify_enabled: bool = None,
        xforwarded_for_client_cert_fingerprint_alias: str = None,
        xforwarded_for_client_cert_fingerprint_enabled: bool = None,
        xforwarded_for_client_cert_issuer_dnalias: str = None,
        xforwarded_for_client_cert_issuer_dnenabled: bool = None,
        xforwarded_for_client_cert_subject_dnalias: str = None,
        xforwarded_for_client_cert_subject_dnenabled: bool = None,
        xforwarded_for_client_src_port_enabled: bool = None,
        xforwarded_for_enabled: bool = None,
        xforwarded_for_proto_enabled: bool = None,
        xforwarded_for_slbid_enabled: bool = None,
        xforwarded_for_slbport_enabled: bool = None,
    ):
        # 自定义HEADER头名称，只有当XForwardedForClientCertClientVerifyEnabled的值为true的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_client_verify_alias = xforwarded_for_client_cert_client_verify_alias
        # 是否通过X-Forwarded-Clientcert-clientverify  头字段获取对访问负载均衡实例客户端证书的校验结果。HTTPS监听有效。
        self.xforwarded_for_client_cert_client_verify_enabled = xforwarded_for_client_cert_client_verify_enabled
        # 自定义HEADER头名称，只有当XForwardedForClientCertFingerprintEnabled的值为true的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_fingerprint_alias = xforwarded_for_client_cert_fingerprint_alias
        # 是否通过X-Forwarded-Clientcert-fingerprint 头字段获取访问负载均衡实例客户端证书的指纹取值，HTTPS监听有效。
        self.xforwarded_for_client_cert_fingerprint_enabled = xforwarded_for_client_cert_fingerprint_enabled
        # 自定义HEADER头名称，只有当XForwardedForClientCertIssuerDNEnabled的值为‘On’的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_issuer_dnalias = xforwarded_for_client_cert_issuer_dnalias
        # 是否通过 X-Forwarded-Clientcert-issuerdn 头字段获取访问负载均衡实例客户端证书的发行者信息。HTTPS监听有效。
        self.xforwarded_for_client_cert_issuer_dnenabled = xforwarded_for_client_cert_issuer_dnenabled
        # 自定义HEADER头名称，只有当XForwardedForClientCertSubjectDNEnabled的值为true的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_subject_dnalias = xforwarded_for_client_cert_subject_dnalias
        # 是否通过X-Forwarded-Clientcert-subjectdn  头字段获取访问负载均衡实例客户端证书的所有者信息。HTTPS监听有效。
        self.xforwarded_for_client_cert_subject_dnenabled = xforwarded_for_client_cert_subject_dnenabled
        # 是否通过X-Forwarded-Client-Port 头字段获取访问负载均衡实例客户端的端口。HTTPS监听有效。
        self.xforwarded_for_client_src_port_enabled = xforwarded_for_client_src_port_enabled
        # 是否开启通过X-Forwarded-For头字段获取来访者真实 IP
        self.xforwarded_for_enabled = xforwarded_for_enabled
        # 是否通过X-Forwarded-Proto头字段获取负载均衡实例的监听协议。
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        # 是否通过SLB-ID头字段获取负载均衡实例ID。
        self.xforwarded_for_slbid_enabled = xforwarded_for_slbid_enabled
        # 是否通过X-Forwarded-Port 头字段获取负载均衡实例的监听端口。HTTPS监听有效。
        self.xforwarded_for_slbport_enabled = xforwarded_for_slbport_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.xforwarded_for_client_cert_client_verify_alias is not None:
            result['XForwardedForClientCertClientVerifyAlias'] = self.xforwarded_for_client_cert_client_verify_alias
        if self.xforwarded_for_client_cert_client_verify_enabled is not None:
            result['XForwardedForClientCertClientVerifyEnabled'] = self.xforwarded_for_client_cert_client_verify_enabled
        if self.xforwarded_for_client_cert_fingerprint_alias is not None:
            result['XForwardedForClientCertFingerprintAlias'] = self.xforwarded_for_client_cert_fingerprint_alias
        if self.xforwarded_for_client_cert_fingerprint_enabled is not None:
            result['XForwardedForClientCertFingerprintEnabled'] = self.xforwarded_for_client_cert_fingerprint_enabled
        if self.xforwarded_for_client_cert_issuer_dnalias is not None:
            result['XForwardedForClientCertIssuerDNAlias'] = self.xforwarded_for_client_cert_issuer_dnalias
        if self.xforwarded_for_client_cert_issuer_dnenabled is not None:
            result['XForwardedForClientCertIssuerDNEnabled'] = self.xforwarded_for_client_cert_issuer_dnenabled
        if self.xforwarded_for_client_cert_subject_dnalias is not None:
            result['XForwardedForClientCertSubjectDNAlias'] = self.xforwarded_for_client_cert_subject_dnalias
        if self.xforwarded_for_client_cert_subject_dnenabled is not None:
            result['XForwardedForClientCertSubjectDNEnabled'] = self.xforwarded_for_client_cert_subject_dnenabled
        if self.xforwarded_for_client_src_port_enabled is not None:
            result['XForwardedForClientSrcPortEnabled'] = self.xforwarded_for_client_src_port_enabled
        if self.xforwarded_for_enabled is not None:
            result['XForwardedForEnabled'] = self.xforwarded_for_enabled
        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled
        if self.xforwarded_for_slbid_enabled is not None:
            result['XForwardedForSLBIdEnabled'] = self.xforwarded_for_slbid_enabled
        if self.xforwarded_for_slbport_enabled is not None:
            result['XForwardedForSLBPortEnabled'] = self.xforwarded_for_slbport_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('XForwardedForClientCertClientVerifyAlias') is not None:
            self.xforwarded_for_client_cert_client_verify_alias = m.get('XForwardedForClientCertClientVerifyAlias')
        if m.get('XForwardedForClientCertClientVerifyEnabled') is not None:
            self.xforwarded_for_client_cert_client_verify_enabled = m.get('XForwardedForClientCertClientVerifyEnabled')
        if m.get('XForwardedForClientCertFingerprintAlias') is not None:
            self.xforwarded_for_client_cert_fingerprint_alias = m.get('XForwardedForClientCertFingerprintAlias')
        if m.get('XForwardedForClientCertFingerprintEnabled') is not None:
            self.xforwarded_for_client_cert_fingerprint_enabled = m.get('XForwardedForClientCertFingerprintEnabled')
        if m.get('XForwardedForClientCertIssuerDNAlias') is not None:
            self.xforwarded_for_client_cert_issuer_dnalias = m.get('XForwardedForClientCertIssuerDNAlias')
        if m.get('XForwardedForClientCertIssuerDNEnabled') is not None:
            self.xforwarded_for_client_cert_issuer_dnenabled = m.get('XForwardedForClientCertIssuerDNEnabled')
        if m.get('XForwardedForClientCertSubjectDNAlias') is not None:
            self.xforwarded_for_client_cert_subject_dnalias = m.get('XForwardedForClientCertSubjectDNAlias')
        if m.get('XForwardedForClientCertSubjectDNEnabled') is not None:
            self.xforwarded_for_client_cert_subject_dnenabled = m.get('XForwardedForClientCertSubjectDNEnabled')
        if m.get('XForwardedForClientSrcPortEnabled') is not None:
            self.xforwarded_for_client_src_port_enabled = m.get('XForwardedForClientSrcPortEnabled')
        if m.get('XForwardedForEnabled') is not None:
            self.xforwarded_for_enabled = m.get('XForwardedForEnabled')
        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')
        if m.get('XForwardedForSLBIdEnabled') is not None:
            self.xforwarded_for_slbid_enabled = m.get('XForwardedForSLBIdEnabled')
        if m.get('XForwardedForSLBPortEnabled') is not None:
            self.xforwarded_for_slbport_enabled = m.get('XForwardedForSLBPortEnabled')
        return self


class CreateListenerRequest(TeaModel):
    def __init__(
        self,
        ca_certificates: List[CreateListenerRequestCaCertificates] = None,
        ca_enabled: bool = None,
        certificates: List[CreateListenerRequestCertificates] = None,
        client_token: str = None,
        default_actions: List[CreateListenerRequestDefaultActions] = None,
        dry_run: bool = None,
        gzip_enabled: bool = None,
        http_2enabled: bool = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balancer_id: str = None,
        quic_config: CreateListenerRequestQuicConfig = None,
        request_timeout: int = None,
        security_policy_id: str = None,
        xforwarded_for_config: CreateListenerRequestXForwardedForConfig = None,
    ):
        # 监听默认CA证书列表，N当前取值范围为1
        self.ca_certificates = ca_certificates
        # 是否开启双向认证
        self.ca_enabled = ca_enabled
        # 监听默认服务器证书列表，N当前取值范围为1
        self.certificates = certificates
        # 幂等标识
        self.client_token = client_token
        # 监听默认动作
        self.default_actions = default_actions
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 是否开启Gzip压缩
        self.gzip_enabled = gzip_enabled
        # 是否开启HTTP/2特性
        self.http_2enabled = http_2enabled
        # 连接空闲超时时间
        self.idle_timeout = idle_timeout
        # 监听描述
        self.listener_description = listener_description
        # 监听端口
        self.listener_port = listener_port
        # 监听协议
        self.listener_protocol = listener_protocol
        # 负载均衡标识
        self.load_balancer_id = load_balancer_id
        # HTTPS启用QUIC时相关属性
        self.quic_config = quic_config
        # 请求超时时间
        self.request_timeout = request_timeout
        # 安全策略
        self.security_policy_id = security_policy_id
        # XForward字段相关的配置
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
        if self.ca_certificates:
            for k in self.ca_certificates:
                if k:
                    k.validate()
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.default_actions:
            for k in self.default_actions:
                if k:
                    k.validate()
        if self.quic_config:
            self.quic_config.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CaCertificates'] = []
        if self.ca_certificates is not None:
            for k in self.ca_certificates:
                result['CaCertificates'].append(k.to_map() if k else None)
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['DefaultActions'] = []
        if self.default_actions is not None:
            for k in self.default_actions:
                result['DefaultActions'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.gzip_enabled is not None:
            result['GzipEnabled'] = self.gzip_enabled
        if self.http_2enabled is not None:
            result['Http2Enabled'] = self.http_2enabled
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.quic_config is not None:
            result['QuicConfig'] = self.quic_config.to_map()
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ca_certificates = []
        if m.get('CaCertificates') is not None:
            for k in m.get('CaCertificates'):
                temp_model = CreateListenerRequestCaCertificates()
                self.ca_certificates.append(temp_model.from_map(k))
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = CreateListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.default_actions = []
        if m.get('DefaultActions') is not None:
            for k in m.get('DefaultActions'):
                temp_model = CreateListenerRequestDefaultActions()
                self.default_actions.append(temp_model.from_map(k))
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('GzipEnabled') is not None:
            self.gzip_enabled = m.get('GzipEnabled')
        if m.get('Http2Enabled') is not None:
            self.http_2enabled = m.get('Http2Enabled')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('QuicConfig') is not None:
            temp_model = CreateListenerRequestQuicConfig()
            self.quic_config = temp_model.from_map(m['QuicConfig'])
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('XForwardedForConfig') is not None:
            temp_model = CreateListenerRequestXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m['XForwardedForConfig'])
        return self


class CreateListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        listener_id: str = None,
        request_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # 监听标识
        self.listener_id = listener_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateListenerResponseBody = None,
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
            temp_model = CreateListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerRequestLoadBalancerBillingConfig(TeaModel):
    def __init__(
        self,
        pay_type: str = None,
    ):
        # 实例的计费类型
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class CreateLoadBalancerRequestModificationProtectionConfig(TeaModel):
    def __init__(
        self,
        reason: str = None,
        status: str = None,
    ):
        # 设置修改保护状态的原因
        self.reason = reason
        # 负载均衡修改保护状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateLoadBalancerRequestZoneMappings(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # 交换机标识
        self.v_switch_id = v_switch_id
        # 可用区
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateLoadBalancerRequest(TeaModel):
    def __init__(
        self,
        address_allocated_mode: str = None,
        address_type: str = None,
        client_token: str = None,
        deletion_protection_enabled: bool = None,
        dry_run: bool = None,
        load_balancer_billing_config: CreateLoadBalancerRequestLoadBalancerBillingConfig = None,
        load_balancer_edition: str = None,
        load_balancer_name: str = None,
        modification_protection_config: CreateLoadBalancerRequestModificationProtectionConfig = None,
        resource_group_id: str = None,
        vpc_id: str = None,
        zone_mappings: List[CreateLoadBalancerRequestZoneMappings] = None,
    ):
        # 地址模式
        self.address_allocated_mode = address_allocated_mode
        # 负载均衡的地址类型
        self.address_type = address_type
        # 幂等标识
        self.client_token = client_token
        # 是否开启删除保护
        self.deletion_protection_enabled = deletion_protection_enabled
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 计费相关配置信息
        self.load_balancer_billing_config = load_balancer_billing_config
        # 负载均衡的版本
        self.load_balancer_edition = load_balancer_edition
        # 名称
        self.load_balancer_name = load_balancer_name
        # 负载均衡修改保护相关信息
        self.modification_protection_config = modification_protection_config
        # 资源组
        self.resource_group_id = resource_group_id
        # 负载均衡实例的专有网络ID。
        self.vpc_id = vpc_id
        # 可用区及交换机映射列表
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.load_balancer_billing_config:
            self.load_balancer_billing_config.validate()
        if self.modification_protection_config:
            self.modification_protection_config.validate()
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_allocated_mode is not None:
            result['AddressAllocatedMode'] = self.address_allocated_mode
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deletion_protection_enabled is not None:
            result['DeletionProtectionEnabled'] = self.deletion_protection_enabled
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()
        if self.load_balancer_edition is not None:
            result['LoadBalancerEdition'] = self.load_balancer_edition
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressAllocatedMode') is not None:
            self.address_allocated_mode = m.get('AddressAllocatedMode')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeletionProtectionEnabled') is not None:
            self.deletion_protection_enabled = m.get('DeletionProtectionEnabled')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = CreateLoadBalancerRequestLoadBalancerBillingConfig()
            self.load_balancer_billing_config = temp_model.from_map(m['LoadBalancerBillingConfig'])
        if m.get('LoadBalancerEdition') is not None:
            self.load_balancer_edition = m.get('LoadBalancerEdition')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('ModificationProtectionConfig') is not None:
            temp_model = CreateLoadBalancerRequestModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m['ModificationProtectionConfig'])
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = CreateLoadBalancerRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class CreateLoadBalancerResponseBody(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        request_id: str = None,
    ):
        # 负载均衡实例标识
        self.load_balancer_id = load_balancer_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLoadBalancerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoadBalancerResponseBody = None,
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
            temp_model = CreateLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleRequestRuleActionsFixedResponseConfig(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        http_code: str = None,
    ):
        # 内容
        self.content = content
        # 内容类型
        self.content_type = content_type
        # HTTP响应码
        self.http_code = http_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        return self


class CreateRuleRequestRuleActionsForwardGroupConfigServerGroupStickySession(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        timeout: int = None,
    ):
        # 是否开启会话保持
        self.enabled = enabled
        # 超时时间
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateRuleRequestRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        # 服务器组标识
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class CreateRuleRequestRuleActionsForwardGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_sticky_session: CreateRuleRequestRuleActionsForwardGroupConfigServerGroupStickySession = None,
        server_group_tuples: List[CreateRuleRequestRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # 服务器组之间会话保持
        self.server_group_sticky_session = server_group_sticky_session
        # 转发到的目的服务器组列表
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_sticky_session:
            self.server_group_sticky_session.validate()
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_sticky_session is not None:
            result['ServerGroupStickySession'] = self.server_group_sticky_session.to_map()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupStickySession') is not None:
            temp_model = CreateRuleRequestRuleActionsForwardGroupConfigServerGroupStickySession()
            self.server_group_sticky_session = temp_model.from_map(m['ServerGroupStickySession'])
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = CreateRuleRequestRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class CreateRuleRequestRuleActionsInsertHeaderConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        value_type: str = None,
    ):
        # HTTP标头
        self.key = key
        # HTTP标头内容
        self.value = value
        # 取值类型
        self.value_type = value_type

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
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class CreateRuleRequestRuleActionsRedirectConfig(TeaModel):
    def __init__(
        self,
        host: str = None,
        http_code: str = None,
        path: str = None,
        port: str = None,
        protocol: str = None,
        query: str = None,
    ):
        # 要跳转的主机地址
        self.host = host
        # 跳转方式
        self.http_code = http_code
        # 要跳转的路径
        self.path = path
        # 要跳转的端口
        self.port = port
        # 要跳转的协议
        self.protocol = protocol
        # 要跳转的查询字符串
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class CreateRuleRequestRuleActionsRewriteConfig(TeaModel):
    def __init__(
        self,
        host: str = None,
        path: str = None,
        query: str = None,
    ):
        # 主机名
        self.host = host
        # 路径
        self.path = path
        # 查询
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.path is not None:
            result['Path'] = self.path
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class CreateRuleRequestRuleActionsTrafficLimitConfig(TeaModel):
    def __init__(
        self,
        qps: int = None,
    ):
        self.qps = qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['QPS'] = self.qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        return self


class CreateRuleRequestRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class CreateRuleRequestRuleActionsTrafficMirrorConfigMirrorGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[CreateRuleRequestRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples] = None,
    ):
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = CreateRuleRequestRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class CreateRuleRequestRuleActionsTrafficMirrorConfig(TeaModel):
    def __init__(
        self,
        mirror_group_config: CreateRuleRequestRuleActionsTrafficMirrorConfigMirrorGroupConfig = None,
        target_type: str = None,
    ):
        # 镜像至服务器组
        self.mirror_group_config = mirror_group_config
        # 镜像目标类型
        self.target_type = target_type

    def validate(self):
        if self.mirror_group_config:
            self.mirror_group_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mirror_group_config is not None:
            result['MirrorGroupConfig'] = self.mirror_group_config.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MirrorGroupConfig') is not None:
            temp_model = CreateRuleRequestRuleActionsTrafficMirrorConfigMirrorGroupConfig()
            self.mirror_group_config = temp_model.from_map(m['MirrorGroupConfig'])
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateRuleRequestRuleActions(TeaModel):
    def __init__(
        self,
        fixed_response_config: CreateRuleRequestRuleActionsFixedResponseConfig = None,
        forward_group_config: CreateRuleRequestRuleActionsForwardGroupConfig = None,
        insert_header_config: CreateRuleRequestRuleActionsInsertHeaderConfig = None,
        order: int = None,
        redirect_config: CreateRuleRequestRuleActionsRedirectConfig = None,
        rewrite_config: CreateRuleRequestRuleActionsRewriteConfig = None,
        traffic_limit_config: CreateRuleRequestRuleActionsTrafficLimitConfig = None,
        traffic_mirror_config: CreateRuleRequestRuleActionsTrafficMirrorConfig = None,
        type: str = None,
    ):
        # 返回固定内容动作配置
        self.fixed_response_config = fixed_response_config
        # 转发组动作配置
        self.forward_group_config = forward_group_config
        # 插入头部动作配置
        self.insert_header_config = insert_header_config
        # 优先级
        self.order = order
        # 重定向动作配置
        self.redirect_config = redirect_config
        # 内部重定向动作配置
        self.rewrite_config = rewrite_config
        # 流量限速
        self.traffic_limit_config = traffic_limit_config
        # 流量镜像
        self.traffic_mirror_config = traffic_mirror_config
        # 转发规则动作类型
        self.type = type

    def validate(self):
        if self.fixed_response_config:
            self.fixed_response_config.validate()
        if self.forward_group_config:
            self.forward_group_config.validate()
        if self.insert_header_config:
            self.insert_header_config.validate()
        if self.redirect_config:
            self.redirect_config.validate()
        if self.rewrite_config:
            self.rewrite_config.validate()
        if self.traffic_limit_config:
            self.traffic_limit_config.validate()
        if self.traffic_mirror_config:
            self.traffic_mirror_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fixed_response_config is not None:
            result['FixedResponseConfig'] = self.fixed_response_config.to_map()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.insert_header_config is not None:
            result['InsertHeaderConfig'] = self.insert_header_config.to_map()
        if self.order is not None:
            result['Order'] = self.order
        if self.redirect_config is not None:
            result['RedirectConfig'] = self.redirect_config.to_map()
        if self.rewrite_config is not None:
            result['RewriteConfig'] = self.rewrite_config.to_map()
        if self.traffic_limit_config is not None:
            result['TrafficLimitConfig'] = self.traffic_limit_config.to_map()
        if self.traffic_mirror_config is not None:
            result['TrafficMirrorConfig'] = self.traffic_mirror_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedResponseConfig') is not None:
            temp_model = CreateRuleRequestRuleActionsFixedResponseConfig()
            self.fixed_response_config = temp_model.from_map(m['FixedResponseConfig'])
        if m.get('ForwardGroupConfig') is not None:
            temp_model = CreateRuleRequestRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('InsertHeaderConfig') is not None:
            temp_model = CreateRuleRequestRuleActionsInsertHeaderConfig()
            self.insert_header_config = temp_model.from_map(m['InsertHeaderConfig'])
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RedirectConfig') is not None:
            temp_model = CreateRuleRequestRuleActionsRedirectConfig()
            self.redirect_config = temp_model.from_map(m['RedirectConfig'])
        if m.get('RewriteConfig') is not None:
            temp_model = CreateRuleRequestRuleActionsRewriteConfig()
            self.rewrite_config = temp_model.from_map(m['RewriteConfig'])
        if m.get('TrafficLimitConfig') is not None:
            temp_model = CreateRuleRequestRuleActionsTrafficLimitConfig()
            self.traffic_limit_config = temp_model.from_map(m['TrafficLimitConfig'])
        if m.get('TrafficMirrorConfig') is not None:
            temp_model = CreateRuleRequestRuleActionsTrafficMirrorConfig()
            self.traffic_mirror_config = temp_model.from_map(m['TrafficMirrorConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateRuleRequestRuleConditionsCookieConfigValues(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Cookie条件键
        self.key = key
        # Cookie条件值
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


class CreateRuleRequestRuleConditionsCookieConfig(TeaModel):
    def __init__(
        self,
        values: List[CreateRuleRequestRuleConditionsCookieConfigValues] = None,
    ):
        # Cookie键值对列表
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = CreateRuleRequestRuleConditionsCookieConfigValues()
                self.values.append(temp_model.from_map(k))
        return self


class CreateRuleRequestRuleConditionsHeaderConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # HTTP标头键
        self.key = key
        # HTTP标头值列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateRuleRequestRuleConditionsHostConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 主机名列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateRuleRequestRuleConditionsMethodConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # HTTP请求方法列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateRuleRequestRuleConditionsPathConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 路径条件列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateRuleRequestRuleConditionsQueryStringConfigValues(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 查询字符串条件键
        self.key = key
        # 查询字符串条件值
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


class CreateRuleRequestRuleConditionsQueryStringConfig(TeaModel):
    def __init__(
        self,
        values: List[CreateRuleRequestRuleConditionsQueryStringConfigValues] = None,
    ):
        # 查询字符串条件键值对列表
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = CreateRuleRequestRuleConditionsQueryStringConfigValues()
                self.values.append(temp_model.from_map(k))
        return self


class CreateRuleRequestRuleConditionsSourceIpConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 基于源IP业务流量匹配
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateRuleRequestRuleConditions(TeaModel):
    def __init__(
        self,
        cookie_config: CreateRuleRequestRuleConditionsCookieConfig = None,
        header_config: CreateRuleRequestRuleConditionsHeaderConfig = None,
        host_config: CreateRuleRequestRuleConditionsHostConfig = None,
        method_config: CreateRuleRequestRuleConditionsMethodConfig = None,
        path_config: CreateRuleRequestRuleConditionsPathConfig = None,
        query_string_config: CreateRuleRequestRuleConditionsQueryStringConfig = None,
        source_ip_config: CreateRuleRequestRuleConditionsSourceIpConfig = None,
        type: str = None,
    ):
        # Cookie条件配置
        self.cookie_config = cookie_config
        # HTTP标头条件配置
        self.header_config = header_config
        # 主机名条件配置
        self.host_config = host_config
        # HTTP请求方法条件配置
        self.method_config = method_config
        # 路径条件配置
        self.path_config = path_config
        # 查询字符串条件配置
        self.query_string_config = query_string_config
        # 基于源IP业务流量匹配
        self.source_ip_config = source_ip_config
        # 条件类型
        self.type = type

    def validate(self):
        if self.cookie_config:
            self.cookie_config.validate()
        if self.header_config:
            self.header_config.validate()
        if self.host_config:
            self.host_config.validate()
        if self.method_config:
            self.method_config.validate()
        if self.path_config:
            self.path_config.validate()
        if self.query_string_config:
            self.query_string_config.validate()
        if self.source_ip_config:
            self.source_ip_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie_config is not None:
            result['CookieConfig'] = self.cookie_config.to_map()
        if self.header_config is not None:
            result['HeaderConfig'] = self.header_config.to_map()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        if self.method_config is not None:
            result['MethodConfig'] = self.method_config.to_map()
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.query_string_config is not None:
            result['QueryStringConfig'] = self.query_string_config.to_map()
        if self.source_ip_config is not None:
            result['SourceIpConfig'] = self.source_ip_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieConfig') is not None:
            temp_model = CreateRuleRequestRuleConditionsCookieConfig()
            self.cookie_config = temp_model.from_map(m['CookieConfig'])
        if m.get('HeaderConfig') is not None:
            temp_model = CreateRuleRequestRuleConditionsHeaderConfig()
            self.header_config = temp_model.from_map(m['HeaderConfig'])
        if m.get('HostConfig') is not None:
            temp_model = CreateRuleRequestRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        if m.get('MethodConfig') is not None:
            temp_model = CreateRuleRequestRuleConditionsMethodConfig()
            self.method_config = temp_model.from_map(m['MethodConfig'])
        if m.get('PathConfig') is not None:
            temp_model = CreateRuleRequestRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('QueryStringConfig') is not None:
            temp_model = CreateRuleRequestRuleConditionsQueryStringConfig()
            self.query_string_config = temp_model.from_map(m['QueryStringConfig'])
        if m.get('SourceIpConfig') is not None:
            temp_model = CreateRuleRequestRuleConditionsSourceIpConfig()
            self.source_ip_config = temp_model.from_map(m['SourceIpConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        priority: int = None,
        rule_actions: List[CreateRuleRequestRuleActions] = None,
        rule_conditions: List[CreateRuleRequestRuleConditions] = None,
        rule_name: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 监听标识
        self.listener_id = listener_id
        # 转发规则优先级
        self.priority = priority
        # 转发规则动作
        self.rule_actions = rule_actions
        # 转发规则条件
        self.rule_conditions = rule_conditions
        # 转发规则名称
        self.rule_name = rule_name

    def validate(self):
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = CreateRuleRequestRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = CreateRuleRequestRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        rule_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id
        # 转发规则标识
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRuleResponseBody = None,
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
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRulesRequestRulesRuleActionsFixedResponseConfig(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        http_code: str = None,
    ):
        # 内容
        self.content = content
        # 内容类型
        self.content_type = content_type
        # HTTP响应码
        self.http_code = http_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        return self


class CreateRulesRequestRulesRuleActionsForwardGroupConfigServerGroupStickySession(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        timeout: int = None,
    ):
        # 是否开启会话保持
        self.enabled = enabled
        # 超时时间
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateRulesRequestRulesRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        # 服务器组标识
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class CreateRulesRequestRulesRuleActionsForwardGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_sticky_session: CreateRulesRequestRulesRuleActionsForwardGroupConfigServerGroupStickySession = None,
        server_group_tuples: List[CreateRulesRequestRulesRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # 服务器组之间会话保持
        self.server_group_sticky_session = server_group_sticky_session
        # 转发到的目的服务器组列表
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_sticky_session:
            self.server_group_sticky_session.validate()
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_sticky_session is not None:
            result['ServerGroupStickySession'] = self.server_group_sticky_session.to_map()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupStickySession') is not None:
            temp_model = CreateRulesRequestRulesRuleActionsForwardGroupConfigServerGroupStickySession()
            self.server_group_sticky_session = temp_model.from_map(m['ServerGroupStickySession'])
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = CreateRulesRequestRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class CreateRulesRequestRulesRuleActionsInsertHeaderConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        value_type: str = None,
    ):
        # HTTP标头
        self.key = key
        # HTTP标头内容
        self.value = value
        # 取值类型
        self.value_type = value_type

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
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class CreateRulesRequestRulesRuleActionsRedirectConfig(TeaModel):
    def __init__(
        self,
        host: str = None,
        http_code: str = None,
        path: str = None,
        port: str = None,
        protocol: str = None,
        query: str = None,
    ):
        # 要跳转的主机地址
        self.host = host
        # 跳转方式
        self.http_code = http_code
        # 要跳转的路径
        self.path = path
        # 要跳转的端口
        self.port = port
        # 要跳转的协议
        self.protocol = protocol
        # 要跳转的查询字符串
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class CreateRulesRequestRulesRuleActionsRewriteConfig(TeaModel):
    def __init__(
        self,
        host: str = None,
        path: str = None,
        query: str = None,
    ):
        # 主机名
        self.host = host
        # 路径
        self.path = path
        # 查询
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.path is not None:
            result['Path'] = self.path
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class CreateRulesRequestRulesRuleActionsTrafficLimitConfig(TeaModel):
    def __init__(
        self,
        qps: int = None,
    ):
        self.qps = qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['QPS'] = self.qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        return self


class CreateRulesRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class CreateRulesRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[CreateRulesRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples] = None,
    ):
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = CreateRulesRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class CreateRulesRequestRulesRuleActionsTrafficMirrorConfig(TeaModel):
    def __init__(
        self,
        mirror_group_config: CreateRulesRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfig = None,
        target_type: str = None,
    ):
        # 镜像至服务器组
        self.mirror_group_config = mirror_group_config
        # 镜像目标类型
        self.target_type = target_type

    def validate(self):
        if self.mirror_group_config:
            self.mirror_group_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mirror_group_config is not None:
            result['MirrorGroupConfig'] = self.mirror_group_config.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MirrorGroupConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfig()
            self.mirror_group_config = temp_model.from_map(m['MirrorGroupConfig'])
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateRulesRequestRulesRuleActions(TeaModel):
    def __init__(
        self,
        fixed_response_config: CreateRulesRequestRulesRuleActionsFixedResponseConfig = None,
        forward_group_config: CreateRulesRequestRulesRuleActionsForwardGroupConfig = None,
        insert_header_config: CreateRulesRequestRulesRuleActionsInsertHeaderConfig = None,
        order: int = None,
        redirect_config: CreateRulesRequestRulesRuleActionsRedirectConfig = None,
        rewrite_config: CreateRulesRequestRulesRuleActionsRewriteConfig = None,
        traffic_limit_config: CreateRulesRequestRulesRuleActionsTrafficLimitConfig = None,
        traffic_mirror_config: CreateRulesRequestRulesRuleActionsTrafficMirrorConfig = None,
        type: str = None,
    ):
        # 返回固定内容动作配置
        self.fixed_response_config = fixed_response_config
        # 转发组动作配置
        self.forward_group_config = forward_group_config
        # 插入头部动作配置
        self.insert_header_config = insert_header_config
        # 优先级
        self.order = order
        # 重定向动作配置
        self.redirect_config = redirect_config
        # 内部重定向动作配置
        self.rewrite_config = rewrite_config
        # 流量限速
        self.traffic_limit_config = traffic_limit_config
        # 流量镜像
        self.traffic_mirror_config = traffic_mirror_config
        # 转发规则动作类型
        self.type = type

    def validate(self):
        if self.fixed_response_config:
            self.fixed_response_config.validate()
        if self.forward_group_config:
            self.forward_group_config.validate()
        if self.insert_header_config:
            self.insert_header_config.validate()
        if self.redirect_config:
            self.redirect_config.validate()
        if self.rewrite_config:
            self.rewrite_config.validate()
        if self.traffic_limit_config:
            self.traffic_limit_config.validate()
        if self.traffic_mirror_config:
            self.traffic_mirror_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fixed_response_config is not None:
            result['FixedResponseConfig'] = self.fixed_response_config.to_map()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.insert_header_config is not None:
            result['InsertHeaderConfig'] = self.insert_header_config.to_map()
        if self.order is not None:
            result['Order'] = self.order
        if self.redirect_config is not None:
            result['RedirectConfig'] = self.redirect_config.to_map()
        if self.rewrite_config is not None:
            result['RewriteConfig'] = self.rewrite_config.to_map()
        if self.traffic_limit_config is not None:
            result['TrafficLimitConfig'] = self.traffic_limit_config.to_map()
        if self.traffic_mirror_config is not None:
            result['TrafficMirrorConfig'] = self.traffic_mirror_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedResponseConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleActionsFixedResponseConfig()
            self.fixed_response_config = temp_model.from_map(m['FixedResponseConfig'])
        if m.get('ForwardGroupConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('InsertHeaderConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleActionsInsertHeaderConfig()
            self.insert_header_config = temp_model.from_map(m['InsertHeaderConfig'])
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RedirectConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleActionsRedirectConfig()
            self.redirect_config = temp_model.from_map(m['RedirectConfig'])
        if m.get('RewriteConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleActionsRewriteConfig()
            self.rewrite_config = temp_model.from_map(m['RewriteConfig'])
        if m.get('TrafficLimitConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleActionsTrafficLimitConfig()
            self.traffic_limit_config = temp_model.from_map(m['TrafficLimitConfig'])
        if m.get('TrafficMirrorConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleActionsTrafficMirrorConfig()
            self.traffic_mirror_config = temp_model.from_map(m['TrafficMirrorConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateRulesRequestRulesRuleConditionsCookieConfigValues(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Cookie条件键
        self.key = key
        # Cookie条件值
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


class CreateRulesRequestRulesRuleConditionsCookieConfig(TeaModel):
    def __init__(
        self,
        values: List[CreateRulesRequestRulesRuleConditionsCookieConfigValues] = None,
    ):
        # Cookie键值对列表
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = CreateRulesRequestRulesRuleConditionsCookieConfigValues()
                self.values.append(temp_model.from_map(k))
        return self


class CreateRulesRequestRulesRuleConditionsHeaderConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # HTTP标头键
        self.key = key
        # HTTP标头值列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateRulesRequestRulesRuleConditionsHostConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 主机名列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateRulesRequestRulesRuleConditionsMethodConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # HTTP请求方法列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateRulesRequestRulesRuleConditionsPathConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 路径条件列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateRulesRequestRulesRuleConditionsQueryStringConfigValues(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 查询字符串条件键
        self.key = key
        # 查询字符串条件值
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


class CreateRulesRequestRulesRuleConditionsQueryStringConfig(TeaModel):
    def __init__(
        self,
        values: List[CreateRulesRequestRulesRuleConditionsQueryStringConfigValues] = None,
    ):
        # 查询字符串条件键值对列表
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = CreateRulesRequestRulesRuleConditionsQueryStringConfigValues()
                self.values.append(temp_model.from_map(k))
        return self


class CreateRulesRequestRulesRuleConditionsResponseHeaderConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # 返回HTTP标头键
        self.key = key
        # 返回HTTP标头值
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateRulesRequestRulesRuleConditionsSourceIpConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 基于源IP业务流量匹配
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateRulesRequestRulesRuleConditions(TeaModel):
    def __init__(
        self,
        cookie_config: CreateRulesRequestRulesRuleConditionsCookieConfig = None,
        header_config: CreateRulesRequestRulesRuleConditionsHeaderConfig = None,
        host_config: CreateRulesRequestRulesRuleConditionsHostConfig = None,
        method_config: CreateRulesRequestRulesRuleConditionsMethodConfig = None,
        path_config: CreateRulesRequestRulesRuleConditionsPathConfig = None,
        query_string_config: CreateRulesRequestRulesRuleConditionsQueryStringConfig = None,
        response_header_config: CreateRulesRequestRulesRuleConditionsResponseHeaderConfig = None,
        source_ip_config: CreateRulesRequestRulesRuleConditionsSourceIpConfig = None,
        type: str = None,
    ):
        # Cookie条件配置
        self.cookie_config = cookie_config
        # HTTP标头条件配置
        self.header_config = header_config
        # 主机名条件配置
        self.host_config = host_config
        # HTTP请求方法条件配置
        self.method_config = method_config
        # 路径条件配置
        self.path_config = path_config
        # 查询字符串条件配置
        self.query_string_config = query_string_config
        # 返回HTTP标头
        self.response_header_config = response_header_config
        # 基于源IP业务流量匹配
        self.source_ip_config = source_ip_config
        # 条件类型
        self.type = type

    def validate(self):
        if self.cookie_config:
            self.cookie_config.validate()
        if self.header_config:
            self.header_config.validate()
        if self.host_config:
            self.host_config.validate()
        if self.method_config:
            self.method_config.validate()
        if self.path_config:
            self.path_config.validate()
        if self.query_string_config:
            self.query_string_config.validate()
        if self.response_header_config:
            self.response_header_config.validate()
        if self.source_ip_config:
            self.source_ip_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie_config is not None:
            result['CookieConfig'] = self.cookie_config.to_map()
        if self.header_config is not None:
            result['HeaderConfig'] = self.header_config.to_map()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        if self.method_config is not None:
            result['MethodConfig'] = self.method_config.to_map()
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.query_string_config is not None:
            result['QueryStringConfig'] = self.query_string_config.to_map()
        if self.response_header_config is not None:
            result['ResponseHeaderConfig'] = self.response_header_config.to_map()
        if self.source_ip_config is not None:
            result['SourceIpConfig'] = self.source_ip_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleConditionsCookieConfig()
            self.cookie_config = temp_model.from_map(m['CookieConfig'])
        if m.get('HeaderConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleConditionsHeaderConfig()
            self.header_config = temp_model.from_map(m['HeaderConfig'])
        if m.get('HostConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        if m.get('MethodConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleConditionsMethodConfig()
            self.method_config = temp_model.from_map(m['MethodConfig'])
        if m.get('PathConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('QueryStringConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleConditionsQueryStringConfig()
            self.query_string_config = temp_model.from_map(m['QueryStringConfig'])
        if m.get('ResponseHeaderConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleConditionsResponseHeaderConfig()
            self.response_header_config = temp_model.from_map(m['ResponseHeaderConfig'])
        if m.get('SourceIpConfig') is not None:
            temp_model = CreateRulesRequestRulesRuleConditionsSourceIpConfig()
            self.source_ip_config = temp_model.from_map(m['SourceIpConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateRulesRequestRules(TeaModel):
    def __init__(
        self,
        direction: str = None,
        priority: int = None,
        rule_actions: List[CreateRulesRequestRulesRuleActions] = None,
        rule_conditions: List[CreateRulesRequestRulesRuleConditions] = None,
        rule_name: str = None,
    ):
        # 转发规则方向
        self.direction = direction
        # 转发规则优先级
        self.priority = priority
        # 转发规则动作
        self.rule_actions = rule_actions
        # 转发规则条件
        self.rule_conditions = rule_conditions
        # 转发规则名称
        self.rule_name = rule_name

    def validate(self):
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = CreateRulesRequestRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = CreateRulesRequestRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class CreateRulesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        rules: List[CreateRulesRequestRules] = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 监听标识
        self.listener_id = listener_id
        # 转发规则列表
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = CreateRulesRequestRules()
                self.rules.append(temp_model.from_map(k))
        return self


class CreateRulesResponseBodyRuleIds(TeaModel):
    def __init__(
        self,
        priority: int = None,
        rule_id: str = None,
    ):
        # 转发规则优先级
        self.priority = priority
        # 转发规则标识
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateRulesResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        rule_ids: List[CreateRulesResponseBodyRuleIds] = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id
        # 转发规则标识列表
        self.rule_ids = rule_ids

    def validate(self):
        if self.rule_ids:
            for k in self.rule_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleIds'] = []
        if self.rule_ids is not None:
            for k in self.rule_ids:
                result['RuleIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_ids = []
        if m.get('RuleIds') is not None:
            for k in m.get('RuleIds'):
                temp_model = CreateRulesResponseBodyRuleIds()
                self.rule_ids.append(temp_model.from_map(k))
        return self


class CreateRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRulesResponseBody = None,
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
            temp_model = CreateRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecurityPolicyRequest(TeaModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        resource_group_id: str = None,
        security_policy_name: str = None,
        tlsversions: List[str] = None,
    ):
        # 加密套件
        self.ciphers = ciphers
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 资源组id
        self.resource_group_id = resource_group_id
        # 安全策略名称
        self.security_policy_name = security_policy_name
        # tls版本
        self.tlsversions = tlsversions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name
        if self.tlsversions is not None:
            result['TLSVersions'] = self.tlsversions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')
        if m.get('TLSVersions') is not None:
            self.tlsversions = m.get('TLSVersions')
        return self


class CreateSecurityPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_policy_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 安全策略id
        self.security_policy_id = security_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        return self


class CreateSecurityPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSecurityPolicyResponseBody = None,
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
            temp_model = CreateSecurityPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServerGroupRequestHealthCheckConfig(TeaModel):
    def __init__(
        self,
        health_check_codes: List[str] = None,
        health_check_connect_port: int = None,
        health_check_enabled: bool = None,
        health_check_host: str = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_path: str = None,
        health_check_protocol: str = None,
        health_check_timeout: int = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
    ):
        # 健康检查正常的状态码
        self.health_check_codes = health_check_codes
        # 健康检查端口
        self.health_check_connect_port = health_check_connect_port
        # 是否启用健康检查
        self.health_check_enabled = health_check_enabled
        # 健康检查域名
        self.health_check_host = health_check_host
        # 健康检查HTTP协议版本
        self.health_check_http_version = health_check_http_version
        # 健康检查间隔
        self.health_check_interval = health_check_interval
        # 健康检查方法
        self.health_check_method = health_check_method
        # 健康检查Path
        self.health_check_path = health_check_path
        # 健康检查协议类型
        self.health_check_protocol = health_check_protocol
        # 健康检查超时时间
        self.health_check_timeout = health_check_timeout
        # 健康检查成功判定阈值
        self.healthy_threshold = healthy_threshold
        # 健康检查不成功判定阈值
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_codes is not None:
            result['HealthCheckCodes'] = self.health_check_codes
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_host is not None:
            result['HealthCheckHost'] = self.health_check_host
        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckCodes') is not None:
            self.health_check_codes = m.get('HealthCheckCodes')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckHost') is not None:
            self.health_check_host = m.get('HealthCheckHost')
        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class CreateServerGroupRequestStickySessionConfig(TeaModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        sticky_session_enabled: bool = None,
        sticky_session_type: str = None,
    ):
        # 服务器上配置的Cookie
        self.cookie = cookie
        # 服务器上配置的Cookie
        self.cookie_timeout = cookie_timeout
        # 是否启用会话保持
        self.sticky_session_enabled = sticky_session_enabled
        # 会话保持类型
        self.sticky_session_type = sticky_session_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.sticky_session_enabled is not None:
            result['StickySessionEnabled'] = self.sticky_session_enabled
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('StickySessionEnabled') is not None:
            self.sticky_session_enabled = m.get('StickySessionEnabled')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        return self


class CreateServerGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        health_check_config: CreateServerGroupRequestHealthCheckConfig = None,
        protocol: str = None,
        resource_group_id: str = None,
        scheduler: str = None,
        server_group_name: str = None,
        server_group_type: str = None,
        service_name: str = None,
        sticky_session_config: CreateServerGroupRequestStickySessionConfig = None,
        vpc_id: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 健康检查配置
        self.health_check_config = health_check_config
        # 后端协议类型
        self.protocol = protocol
        # 资源组id
        self.resource_group_id = resource_group_id
        # 调度策略
        self.scheduler = scheduler
        # 服务器组名称
        self.server_group_name = server_group_name
        # 服务器组类型
        self.server_group_type = server_group_type
        # 服务器名称
        self.service_name = service_name
        # 会话保持配置
        self.sticky_session_config = sticky_session_config
        # VpcId
        self.vpc_id = vpc_id

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()
        if self.sticky_session_config:
            self.sticky_session_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name
        if self.server_group_type is not None:
            result['ServerGroupType'] = self.server_group_type
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.sticky_session_config is not None:
            result['StickySessionConfig'] = self.sticky_session_config.to_map()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('HealthCheckConfig') is not None:
            temp_model = CreateServerGroupRequestHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m['HealthCheckConfig'])
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')
        if m.get('ServerGroupType') is not None:
            self.server_group_type = m.get('ServerGroupType')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StickySessionConfig') is not None:
            temp_model = CreateServerGroupRequestStickySessionConfig()
            self.sticky_session_config = temp_model.from_map(m['StickySessionConfig'])
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateServerGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        server_group_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id
        # 服务器组id
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class CreateServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServerGroupResponseBody = None,
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
            temp_model = CreateServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAclRequest(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
    ):
        # 访问控制策略id
        self.acl_id = acl_id
        # 幂等Token
        self.client_token = client_token
        # DryRun
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class DeleteAclResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAclResponseBody = None,
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
            temp_model = DeleteAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHealthCheckTemplatesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        health_check_template_ids: List[str] = None,
    ):
        # 幂等token
        self.client_token = client_token
        # dryRun
        self.dry_run = dry_run
        # 健康检查模板Id列表
        self.health_check_template_ids = health_check_template_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.health_check_template_ids is not None:
            result['HealthCheckTemplateIds'] = self.health_check_template_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('HealthCheckTemplateIds') is not None:
            self.health_check_template_ids = m.get('HealthCheckTemplateIds')
        return self


class DeleteHealthCheckTemplatesResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteHealthCheckTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteHealthCheckTemplatesResponseBody = None,
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
            temp_model = DeleteHealthCheckTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteListenerRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 监听id
        self.listener_id = listener_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class DeleteListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteListenerResponseBody = None,
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
            temp_model = DeleteListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLoadBalancerRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 实例id
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DeleteLoadBalancerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLoadBalancerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLoadBalancerResponseBody = None,
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
            temp_model = DeleteLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        rule_id: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 转发规则标识
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteRuleResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRuleResponseBody = None,
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
            temp_model = DeleteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRulesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        rule_ids: List[str] = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 同一个监听下的转发规则标识列表
        self.rule_ids = rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        return self


class DeleteRulesResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRulesResponseBody = None,
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
            temp_model = DeleteRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecurityPolicyRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        security_policy_id: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 安全策略Id
        self.security_policy_id = security_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        return self


class DeleteSecurityPolicyResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSecurityPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSecurityPolicyResponseBody = None,
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
            temp_model = DeleteSecurityPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServerGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        server_group_id: str = None,
    ):
        # 幂等参数
        self.client_token = client_token
        # 是否DryRun
        self.dry_run = dry_run
        # 服务器组id
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class DeleteServerGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # job
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteServerGroupResponseBody = None,
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
            temp_model = DeleteServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        # 语言
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


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # 名称
        self.local_name = local_name
        # endpoint
        self.region_endpoint = region_endpoint
        # RegionId
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
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # Region列表
        self.regions = regions
        # Id of the request
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
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        # 可用区名称
        self.local_name = local_name
        # 可用区id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: List[DescribeZonesResponseBodyZones] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 可用区列表
        self.zones = zones

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeZonesResponseBody = None,
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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachCommonBandwidthPackageFromLoadBalancerRequest(TeaModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
    ):
        # 带宽包ID
        self.bandwidth_package_id = bandwidth_package_id
        # 幂等参数
        self.client_token = client_token
        # 预校验
        self.dry_run = dry_run
        # 实例ID
        self.load_balancer_id = load_balancer_id
        # 地域ID
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachCommonBandwidthPackageFromLoadBalancerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务ID
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachCommonBandwidthPackageFromLoadBalancerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachCommonBandwidthPackageFromLoadBalancerResponseBody = None,
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
            temp_model = DetachCommonBandwidthPackageFromLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDeletionProtectionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        resource_id: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 实例id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DisableDeletionProtectionResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableDeletionProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableDeletionProtectionResponseBody = None,
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
            temp_model = DisableDeletionProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableLoadBalancerAccessLogRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 实例id
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DisableLoadBalancerAccessLogResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableLoadBalancerAccessLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableLoadBalancerAccessLogResponseBody = None,
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
            temp_model = DisableLoadBalancerAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateAclsFromListenerRequest(TeaModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
    ):
        # 访问控制策略Id
        self.acl_ids = acl_ids
        # 幂等标识
        self.client_token = client_token
        # 预检此次请求
        self.dry_run = dry_run
        # 监听Id
        self.listener_id = listener_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class DissociateAclsFromListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DissociateAclsFromListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DissociateAclsFromListenerResponseBody = None,
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
            temp_model = DissociateAclsFromListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateAdditionalCertificatesFromListenerRequestCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # 证书Id
        self.certificate_id = certificate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class DissociateAdditionalCertificatesFromListenerRequest(TeaModel):
    def __init__(
        self,
        certificates: List[DissociateAdditionalCertificatesFromListenerRequestCertificates] = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
    ):
        # 证书列表
        self.certificates = certificates
        # 幂等Token
        self.client_token = client_token
        # dryRun
        self.dry_run = dry_run
        # 监听Id
        self.listener_id = listener_id

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = DissociateAdditionalCertificatesFromListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class DissociateAdditionalCertificatesFromListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DissociateAdditionalCertificatesFromListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DissociateAdditionalCertificatesFromListenerResponseBody = None,
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
            temp_model = DissociateAdditionalCertificatesFromListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableDeletionProtectionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        resource_id: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 实例id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class EnableDeletionProtectionResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableDeletionProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableDeletionProtectionResponseBody = None,
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
            temp_model = EnableDeletionProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableLoadBalancerAccessLogRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        log_project: str = None,
        log_store: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 实例id
        self.load_balancer_id = load_balancer_id
        # 日志Project
        self.log_project = log_project
        # 日志Store
        self.log_store = log_store

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.log_project is not None:
            result['LogProject'] = self.log_project
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        return self


class EnableLoadBalancerAccessLogResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableLoadBalancerAccessLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableLoadBalancerAccessLogResponseBody = None,
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
            temp_model = EnableLoadBalancerAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHealthCheckTemplateAttributeRequest(TeaModel):
    def __init__(
        self,
        health_check_template_id: str = None,
    ):
        # 健康检查模板Id
        self.health_check_template_id = health_check_template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_template_id is not None:
            result['HealthCheckTemplateId'] = self.health_check_template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckTemplateId') is not None:
            self.health_check_template_id = m.get('HealthCheckTemplateId')
        return self


class GetHealthCheckTemplateAttributeResponseBody(TeaModel):
    def __init__(
        self,
        health_check_codes: List[str] = None,
        health_check_connect_port: int = None,
        health_check_host: str = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_path: str = None,
        health_check_protocol: str = None,
        health_check_template_id: str = None,
        health_check_template_name: str = None,
        health_check_timeout: int = None,
        healthy_threshold: int = None,
        request_id: str = None,
        unhealthy_threshold: int = None,
    ):
        # 状态码
        self.health_check_codes = health_check_codes
        # 端口
        self.health_check_connect_port = health_check_connect_port
        # 域名
        self.health_check_host = health_check_host
        # 版本
        self.health_check_http_version = health_check_http_version
        # 间隔时间
        self.health_check_interval = health_check_interval
        # 方法
        self.health_check_method = health_check_method
        # uri
        self.health_check_path = health_check_path
        # 协议
        self.health_check_protocol = health_check_protocol
        # 健康检查模板Id
        self.health_check_template_id = health_check_template_id
        # 名称
        self.health_check_template_name = health_check_template_name
        # 超时时间
        self.health_check_timeout = health_check_timeout
        # 健康阈值
        self.healthy_threshold = healthy_threshold
        # Id of the request
        self.request_id = request_id
        # 不健康阈值
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_codes is not None:
            result['HealthCheckCodes'] = self.health_check_codes
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_host is not None:
            result['HealthCheckHost'] = self.health_check_host
        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.health_check_template_id is not None:
            result['HealthCheckTemplateId'] = self.health_check_template_id
        if self.health_check_template_name is not None:
            result['HealthCheckTemplateName'] = self.health_check_template_name
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckCodes') is not None:
            self.health_check_codes = m.get('HealthCheckCodes')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckHost') is not None:
            self.health_check_host = m.get('HealthCheckHost')
        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('HealthCheckTemplateId') is not None:
            self.health_check_template_id = m.get('HealthCheckTemplateId')
        if m.get('HealthCheckTemplateName') is not None:
            self.health_check_template_name = m.get('HealthCheckTemplateName')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class GetHealthCheckTemplateAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHealthCheckTemplateAttributeResponseBody = None,
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
            temp_model = GetHealthCheckTemplateAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        listener_id: str = None,
    ):
        # 监听标识
        self.listener_id = listener_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class GetListenerAttributeResponseBodyAclConfigAclRelations(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        status: str = None,
    ):
        # ACL标识
        self.acl_id = acl_id
        # ACL与监听关联的状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetListenerAttributeResponseBodyAclConfig(TeaModel):
    def __init__(
        self,
        acl_relations: List[GetListenerAttributeResponseBodyAclConfigAclRelations] = None,
        acl_type: str = None,
    ):
        # 监听绑定的访问策略组
        self.acl_relations = acl_relations
        # 访问控制类型
        self.acl_type = acl_type

    def validate(self):
        if self.acl_relations:
            for k in self.acl_relations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclRelations'] = []
        if self.acl_relations is not None:
            for k in self.acl_relations:
                result['AclRelations'].append(k.to_map() if k else None)
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_relations = []
        if m.get('AclRelations') is not None:
            for k in m.get('AclRelations'):
                temp_model = GetListenerAttributeResponseBodyAclConfigAclRelations()
                self.acl_relations.append(temp_model.from_map(k))
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        return self


class GetListenerAttributeResponseBodyCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # 正式标识
        self.certificate_id = certificate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class GetListenerAttributeResponseBodyDefaultActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        # 服务器组ID
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class GetListenerAttributeResponseBodyDefaultActionsForwardGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[GetListenerAttributeResponseBodyDefaultActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # 服务器组列表
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = GetListenerAttributeResponseBodyDefaultActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class GetListenerAttributeResponseBodyDefaultActions(TeaModel):
    def __init__(
        self,
        forward_group_config: GetListenerAttributeResponseBodyDefaultActionsForwardGroupConfig = None,
        type: str = None,
    ):
        # 转发到服务器组
        self.forward_group_config = forward_group_config
        # 类型
        self.type = type

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = GetListenerAttributeResponseBodyDefaultActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetListenerAttributeResponseBodyLogConfigAccessLogTracingConfig(TeaModel):
    def __init__(
        self,
        tracing_enabled: bool = None,
        tracing_sample: int = None,
        tracing_type: str = None,
    ):
        # Xtrace功能状态
        self.tracing_enabled = tracing_enabled
        # Xtrace功能状态
        self.tracing_sample = tracing_sample
        # xtrace的类型
        self.tracing_type = tracing_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tracing_enabled is not None:
            result['TracingEnabled'] = self.tracing_enabled
        if self.tracing_sample is not None:
            result['TracingSample'] = self.tracing_sample
        if self.tracing_type is not None:
            result['TracingType'] = self.tracing_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TracingEnabled') is not None:
            self.tracing_enabled = m.get('TracingEnabled')
        if m.get('TracingSample') is not None:
            self.tracing_sample = m.get('TracingSample')
        if m.get('TracingType') is not None:
            self.tracing_type = m.get('TracingType')
        return self


class GetListenerAttributeResponseBodyLogConfig(TeaModel):
    def __init__(
        self,
        access_log_record_customized_headers_enabled: bool = None,
        access_log_tracing_config: GetListenerAttributeResponseBodyLogConfigAccessLogTracingConfig = None,
    ):
        # 访问日志是否开启携带自定义Header
        self.access_log_record_customized_headers_enabled = access_log_record_customized_headers_enabled
        # 访问日志Xtrace相关的配置
        self.access_log_tracing_config = access_log_tracing_config

    def validate(self):
        if self.access_log_tracing_config:
            self.access_log_tracing_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_record_customized_headers_enabled is not None:
            result['AccessLogRecordCustomizedHeadersEnabled'] = self.access_log_record_customized_headers_enabled
        if self.access_log_tracing_config is not None:
            result['AccessLogTracingConfig'] = self.access_log_tracing_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogRecordCustomizedHeadersEnabled') is not None:
            self.access_log_record_customized_headers_enabled = m.get('AccessLogRecordCustomizedHeadersEnabled')
        if m.get('AccessLogTracingConfig') is not None:
            temp_model = GetListenerAttributeResponseBodyLogConfigAccessLogTracingConfig()
            self.access_log_tracing_config = temp_model.from_map(m['AccessLogTracingConfig'])
        return self


class GetListenerAttributeResponseBodyQuicConfig(TeaModel):
    def __init__(
        self,
        quic_listener_id: str = None,
        quic_upgrade_enabled: bool = None,
    ):
        # 需要关联的QUIC监听ID，HTTPS监听时有效，QuicUpgradeEnabled为true时必选
        self.quic_listener_id = quic_listener_id
        # 是否开启quic升级，HTTPS监听时有效
        self.quic_upgrade_enabled = quic_upgrade_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quic_listener_id is not None:
            result['QuicListenerId'] = self.quic_listener_id
        if self.quic_upgrade_enabled is not None:
            result['QuicUpgradeEnabled'] = self.quic_upgrade_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuicListenerId') is not None:
            self.quic_listener_id = m.get('QuicListenerId')
        if m.get('QuicUpgradeEnabled') is not None:
            self.quic_upgrade_enabled = m.get('QuicUpgradeEnabled')
        return self


class GetListenerAttributeResponseBodyXForwardedForConfig(TeaModel):
    def __init__(
        self,
        xforwarded_for_client_cert_client_verify_alias: str = None,
        xforwarded_for_client_cert_client_verify_enabled: bool = None,
        xforwarded_for_client_cert_fingerprint_alias: str = None,
        xforwarded_for_client_cert_fingerprint_enabled: bool = None,
        xforwarded_for_client_cert_issuer_dnalias: str = None,
        xforwarded_for_client_cert_issuer_dnenabled: bool = None,
        xforwarded_for_client_cert_subject_dnalias: str = None,
        xforwarded_for_client_cert_subject_dnenabled: bool = None,
        xforwarded_for_client_src_port_enabled: bool = None,
        xforwarded_for_enabled: bool = None,
        xforwarded_for_proto_enabled: bool = None,
        xforwarded_for_slbid_enabled: bool = None,
        xforwarded_for_slbport_enabled: bool = None,
    ):
        # 自定义HEADER头名称，只有当XForwardedForClientCertClientVerifyEnabled的值为true的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_client_verify_alias = xforwarded_for_client_cert_client_verify_alias
        # 是否通过X-Forwarded-Clientcert-clientverify  头字段获取对访问负载均衡实例客户端证书的校验结果。HTTPS监听有效。
        self.xforwarded_for_client_cert_client_verify_enabled = xforwarded_for_client_cert_client_verify_enabled
        # 自定义HEADER头名称，只有当XForwardedForClientCertFingerprintEnabled的值为true的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_fingerprint_alias = xforwarded_for_client_cert_fingerprint_alias
        # 是否通过X-Forwarded-Clientcert-fingerprint 头字段获取访问负载均衡实例客户端证书的指纹取值，HTTPS监听有效。
        self.xforwarded_for_client_cert_fingerprint_enabled = xforwarded_for_client_cert_fingerprint_enabled
        # 自定义HEADER头名称，只有当XForwardedForClientCertIssuerDNEnabled的值为‘On’的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_issuer_dnalias = xforwarded_for_client_cert_issuer_dnalias
        # 是否通过 X-Forwarded-Clientcert-issuerdn 头字段获取访问负载均衡实例客户端证书的发行者信息。HTTPS监听有效。
        self.xforwarded_for_client_cert_issuer_dnenabled = xforwarded_for_client_cert_issuer_dnenabled
        # 自定义HEADER头名称，只有当XForwardedForClientCertSubjectDNEnabled的值为true的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_subject_dnalias = xforwarded_for_client_cert_subject_dnalias
        # 是否通过X-Forwarded-Clientcert-subjectdn  头字段获取访问负载均衡实例客户端证书的所有者信息。HTTPS监听有效。
        self.xforwarded_for_client_cert_subject_dnenabled = xforwarded_for_client_cert_subject_dnenabled
        # 是否通过X-Forwarded-Client-Port 头字段获取访问负载均衡实例客户端的端口。HTTPS监听有效。
        self.xforwarded_for_client_src_port_enabled = xforwarded_for_client_src_port_enabled
        # 是否开启通过X-Forwarded-For头字段获取来访者真实 IP
        self.xforwarded_for_enabled = xforwarded_for_enabled
        # 是否通过X-Forwarded-Proto头字段获取负载均衡实例的监听协议。
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        # 是否通过SLB-ID头字段获取负载均衡实例ID。
        self.xforwarded_for_slbid_enabled = xforwarded_for_slbid_enabled
        # 是否通过X-Forwarded-Port 头字段获取负载均衡实例的监听端口。HTTPS监听有效。
        self.xforwarded_for_slbport_enabled = xforwarded_for_slbport_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.xforwarded_for_client_cert_client_verify_alias is not None:
            result['XForwardedForClientCertClientVerifyAlias'] = self.xforwarded_for_client_cert_client_verify_alias
        if self.xforwarded_for_client_cert_client_verify_enabled is not None:
            result['XForwardedForClientCertClientVerifyEnabled'] = self.xforwarded_for_client_cert_client_verify_enabled
        if self.xforwarded_for_client_cert_fingerprint_alias is not None:
            result['XForwardedForClientCertFingerprintAlias'] = self.xforwarded_for_client_cert_fingerprint_alias
        if self.xforwarded_for_client_cert_fingerprint_enabled is not None:
            result['XForwardedForClientCertFingerprintEnabled'] = self.xforwarded_for_client_cert_fingerprint_enabled
        if self.xforwarded_for_client_cert_issuer_dnalias is not None:
            result['XForwardedForClientCertIssuerDNAlias'] = self.xforwarded_for_client_cert_issuer_dnalias
        if self.xforwarded_for_client_cert_issuer_dnenabled is not None:
            result['XForwardedForClientCertIssuerDNEnabled'] = self.xforwarded_for_client_cert_issuer_dnenabled
        if self.xforwarded_for_client_cert_subject_dnalias is not None:
            result['XForwardedForClientCertSubjectDNAlias'] = self.xforwarded_for_client_cert_subject_dnalias
        if self.xforwarded_for_client_cert_subject_dnenabled is not None:
            result['XForwardedForClientCertSubjectDNEnabled'] = self.xforwarded_for_client_cert_subject_dnenabled
        if self.xforwarded_for_client_src_port_enabled is not None:
            result['XForwardedForClientSrcPortEnabled'] = self.xforwarded_for_client_src_port_enabled
        if self.xforwarded_for_enabled is not None:
            result['XForwardedForEnabled'] = self.xforwarded_for_enabled
        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled
        if self.xforwarded_for_slbid_enabled is not None:
            result['XForwardedForSLBIdEnabled'] = self.xforwarded_for_slbid_enabled
        if self.xforwarded_for_slbport_enabled is not None:
            result['XForwardedForSLBPortEnabled'] = self.xforwarded_for_slbport_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('XForwardedForClientCertClientVerifyAlias') is not None:
            self.xforwarded_for_client_cert_client_verify_alias = m.get('XForwardedForClientCertClientVerifyAlias')
        if m.get('XForwardedForClientCertClientVerifyEnabled') is not None:
            self.xforwarded_for_client_cert_client_verify_enabled = m.get('XForwardedForClientCertClientVerifyEnabled')
        if m.get('XForwardedForClientCertFingerprintAlias') is not None:
            self.xforwarded_for_client_cert_fingerprint_alias = m.get('XForwardedForClientCertFingerprintAlias')
        if m.get('XForwardedForClientCertFingerprintEnabled') is not None:
            self.xforwarded_for_client_cert_fingerprint_enabled = m.get('XForwardedForClientCertFingerprintEnabled')
        if m.get('XForwardedForClientCertIssuerDNAlias') is not None:
            self.xforwarded_for_client_cert_issuer_dnalias = m.get('XForwardedForClientCertIssuerDNAlias')
        if m.get('XForwardedForClientCertIssuerDNEnabled') is not None:
            self.xforwarded_for_client_cert_issuer_dnenabled = m.get('XForwardedForClientCertIssuerDNEnabled')
        if m.get('XForwardedForClientCertSubjectDNAlias') is not None:
            self.xforwarded_for_client_cert_subject_dnalias = m.get('XForwardedForClientCertSubjectDNAlias')
        if m.get('XForwardedForClientCertSubjectDNEnabled') is not None:
            self.xforwarded_for_client_cert_subject_dnenabled = m.get('XForwardedForClientCertSubjectDNEnabled')
        if m.get('XForwardedForClientSrcPortEnabled') is not None:
            self.xforwarded_for_client_src_port_enabled = m.get('XForwardedForClientSrcPortEnabled')
        if m.get('XForwardedForEnabled') is not None:
            self.xforwarded_for_enabled = m.get('XForwardedForEnabled')
        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')
        if m.get('XForwardedForSLBIdEnabled') is not None:
            self.xforwarded_for_slbid_enabled = m.get('XForwardedForSLBIdEnabled')
        if m.get('XForwardedForSLBPortEnabled') is not None:
            self.xforwarded_for_slbport_enabled = m.get('XForwardedForSLBPortEnabled')
        return self


class GetListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        acl_config: GetListenerAttributeResponseBodyAclConfig = None,
        ca_enabled: bool = None,
        certificates: List[GetListenerAttributeResponseBodyCertificates] = None,
        default_actions: List[GetListenerAttributeResponseBodyDefaultActions] = None,
        gzip_enabled: bool = None,
        http_2enabled: bool = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        listener_status: str = None,
        load_balancer_id: str = None,
        log_config: GetListenerAttributeResponseBodyLogConfig = None,
        quic_config: GetListenerAttributeResponseBodyQuicConfig = None,
        request_id: str = None,
        request_timeout: int = None,
        security_policy_id: str = None,
        xforwarded_for_config: GetListenerAttributeResponseBodyXForwardedForConfig = None,
    ):
        # ACL相关配置信息
        self.acl_config = acl_config
        # 是否开启双向认证
        self.ca_enabled = ca_enabled
        # 监听默认服务器证书列表，N当前取值范围为1
        self.certificates = certificates
        # 默认动作
        self.default_actions = default_actions
        # 是否开启Gzip压缩
        self.gzip_enabled = gzip_enabled
        # 是否开启HTTP/2特性
        self.http_2enabled = http_2enabled
        # 连接空闲超时时间
        self.idle_timeout = idle_timeout
        # 监听描述
        self.listener_description = listener_description
        # 监听标识
        self.listener_id = listener_id
        # 监听端口
        self.listener_port = listener_port
        # 监听协议
        self.listener_protocol = listener_protocol
        # 监听状态
        self.listener_status = listener_status
        # 负载均衡标识
        self.load_balancer_id = load_balancer_id
        # 监听访问日志相关配置
        self.log_config = log_config
        # HTTPS启用QUIC时相关属性
        self.quic_config = quic_config
        # Id of the request
        self.request_id = request_id
        # 请求超时时间
        self.request_timeout = request_timeout
        # 安全策略
        self.security_policy_id = security_policy_id
        # XForward字段相关的配置
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
        if self.acl_config:
            self.acl_config.validate()
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.default_actions:
            for k in self.default_actions:
                if k:
                    k.validate()
        if self.log_config:
            self.log_config.validate()
        if self.quic_config:
            self.quic_config.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_config is not None:
            result['AclConfig'] = self.acl_config.to_map()
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        result['DefaultActions'] = []
        if self.default_actions is not None:
            for k in self.default_actions:
                result['DefaultActions'].append(k.to_map() if k else None)
        if self.gzip_enabled is not None:
            result['GzipEnabled'] = self.gzip_enabled
        if self.http_2enabled is not None:
            result['Http2Enabled'] = self.http_2enabled
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.listener_status is not None:
            result['ListenerStatus'] = self.listener_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.log_config is not None:
            result['LogConfig'] = self.log_config.to_map()
        if self.quic_config is not None:
            result['QuicConfig'] = self.quic_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclConfig') is not None:
            temp_model = GetListenerAttributeResponseBodyAclConfig()
            self.acl_config = temp_model.from_map(m['AclConfig'])
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = GetListenerAttributeResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k))
        self.default_actions = []
        if m.get('DefaultActions') is not None:
            for k in m.get('DefaultActions'):
                temp_model = GetListenerAttributeResponseBodyDefaultActions()
                self.default_actions.append(temp_model.from_map(k))
        if m.get('GzipEnabled') is not None:
            self.gzip_enabled = m.get('GzipEnabled')
        if m.get('Http2Enabled') is not None:
            self.http_2enabled = m.get('Http2Enabled')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('ListenerStatus') is not None:
            self.listener_status = m.get('ListenerStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LogConfig') is not None:
            temp_model = GetListenerAttributeResponseBodyLogConfig()
            self.log_config = temp_model.from_map(m['LogConfig'])
        if m.get('QuicConfig') is not None:
            temp_model = GetListenerAttributeResponseBodyQuicConfig()
            self.quic_config = temp_model.from_map(m['QuicConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('XForwardedForConfig') is not None:
            temp_model = GetListenerAttributeResponseBodyXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m['XForwardedForConfig'])
        return self


class GetListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetListenerAttributeResponseBody = None,
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
            temp_model = GetListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetListenerHealthStatusRequest(TeaModel):
    def __init__(
        self,
        include_rule: bool = None,
        listener_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # 是否包含转发规则健康检查结果
        self.include_rule = include_rule
        # 监听Id
        self.listener_id = listener_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_rule is not None:
            result['IncludeRule'] = self.include_rule
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeRule') is not None:
            self.include_rule = m.get('IncludeRule')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason(TeaModel):
    def __init__(
        self,
        actual_response: str = None,
        expected_response: str = None,
        reason_code: str = None,
    ):
        # 后端实际的返回码信息
        self.actual_response = actual_response
        # 用户预期的后端返回码信息
        self.expected_response = expected_response
        # 失败reasonCode
        self.reason_code = reason_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_response is not None:
            result['ActualResponse'] = self.actual_response
        if self.expected_response is not None:
            result['ExpectedResponse'] = self.expected_response
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualResponse') is not None:
            self.actual_response = m.get('ActualResponse')
        if m.get('ExpectedResponse') is not None:
            self.expected_response = m.get('ExpectedResponse')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        return self


class GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers(TeaModel):
    def __init__(
        self,
        port: int = None,
        reason: GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason = None,
        server_id: str = None,
        server_ip: str = None,
        status: str = None,
    ):
        # 后端服务器端口
        self.port = port
        # status为非正常状态时的详细异常原因
        self.reason = reason
        # 后端服务器id
        self.server_id = server_id
        # 后端服务器Ip
        self.server_ip = server_ip
        # 健康检查状态
        self.status = status

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Reason') is not None:
            temp_model = GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason()
            self.reason = temp_model.from_map(m['Reason'])
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        health_check_enabled: str = None,
        non_normal_servers: List[GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers] = None,
        server_group_id: str = None,
    ):
        # 服务器组使用类型
        self.action_type = action_type
        # 健康检查开启/关闭
        self.health_check_enabled = health_check_enabled
        # 处于非正常状态的后端服务器
        self.non_normal_servers = non_normal_servers
        # 服务器组ID
        self.server_group_id = server_group_id

    def validate(self):
        if self.non_normal_servers:
            for k in self.non_normal_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        result['NonNormalServers'] = []
        if self.non_normal_servers is not None:
            for k in self.non_normal_servers:
                result['NonNormalServers'].append(k.to_map() if k else None)
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        self.non_normal_servers = []
        if m.get('NonNormalServers') is not None:
            for k in m.get('NonNormalServers'):
                temp_model = GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers()
                self.non_normal_servers.append(temp_model.from_map(k))
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class GetListenerHealthStatusResponseBodyListenerHealthStatus(TeaModel):
    def __init__(
        self,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        server_group_infos: List[GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos] = None,
    ):
        # 监听Id
        self.listener_id = listener_id
        # 监听的端口号
        self.listener_port = listener_port
        # 监听的协议
        self.listener_protocol = listener_protocol
        # 服务器组健康检查结果
        self.server_group_infos = server_group_infos

    def validate(self):
        if self.server_group_infos:
            for k in self.server_group_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        result['ServerGroupInfos'] = []
        if self.server_group_infos is not None:
            for k in self.server_group_infos:
                result['ServerGroupInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        self.server_group_infos = []
        if m.get('ServerGroupInfos') is not None:
            for k in m.get('ServerGroupInfos'):
                temp_model = GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos()
                self.server_group_infos.append(temp_model.from_map(k))
        return self


class GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfosNonNormalServersReason(TeaModel):
    def __init__(
        self,
        actual_response: str = None,
        expected_response: str = None,
        reason_code: str = None,
    ):
        # 后端实际的返回码信息
        self.actual_response = actual_response
        # 用户预期的后端返回码信息
        self.expected_response = expected_response
        # 失败reasonCode
        self.reason_code = reason_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_response is not None:
            result['ActualResponse'] = self.actual_response
        if self.expected_response is not None:
            result['ExpectedResponse'] = self.expected_response
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualResponse') is not None:
            self.actual_response = m.get('ActualResponse')
        if m.get('ExpectedResponse') is not None:
            self.expected_response = m.get('ExpectedResponse')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        return self


class GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfosNonNormalServers(TeaModel):
    def __init__(
        self,
        port: int = None,
        reason: GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfosNonNormalServersReason = None,
        server_id: str = None,
        server_ip: str = None,
        status: str = None,
    ):
        # 后端服务器端口
        self.port = port
        # status为非正常状态时的详细异常原因
        self.reason = reason
        # 后端服务器Id
        self.server_id = server_id
        # 后端服务器ID
        self.server_ip = server_ip
        # 健康检查状态
        self.status = status

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Reason') is not None:
            temp_model = GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfosNonNormalServersReason()
            self.reason = temp_model.from_map(m['Reason'])
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfos(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        health_check_enabled: str = None,
        non_normal_servers: List[GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfosNonNormalServers] = None,
        server_group_id: str = None,
    ):
        # 服务器组使用类型
        self.action_type = action_type
        # 健康检查开启/关闭
        self.health_check_enabled = health_check_enabled
        # 处于非正常状态的后端服务器
        self.non_normal_servers = non_normal_servers
        # 服务器组ID
        self.server_group_id = server_group_id

    def validate(self):
        if self.non_normal_servers:
            for k in self.non_normal_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        result['NonNormalServers'] = []
        if self.non_normal_servers is not None:
            for k in self.non_normal_servers:
                result['NonNormalServers'].append(k.to_map() if k else None)
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        self.non_normal_servers = []
        if m.get('NonNormalServers') is not None:
            for k in m.get('NonNormalServers'):
                temp_model = GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfosNonNormalServers()
                self.non_normal_servers.append(temp_model.from_map(k))
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class GetListenerHealthStatusResponseBodyRuleHealthStatus(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        server_group_infos: List[GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfos] = None,
    ):
        # 转发规则ID
        self.rule_id = rule_id
        # 服务器组健康检查结果
        self.server_group_infos = server_group_infos

    def validate(self):
        if self.server_group_infos:
            for k in self.server_group_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        result['ServerGroupInfos'] = []
        if self.server_group_infos is not None:
            for k in self.server_group_infos:
                result['ServerGroupInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        self.server_group_infos = []
        if m.get('ServerGroupInfos') is not None:
            for k in m.get('ServerGroupInfos'):
                temp_model = GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfos()
                self.server_group_infos.append(temp_model.from_map(k))
        return self


class GetListenerHealthStatusResponseBody(TeaModel):
    def __init__(
        self,
        listener_health_status: List[GetListenerHealthStatusResponseBodyListenerHealthStatus] = None,
        next_token: str = None,
        request_id: str = None,
        rule_health_status: List[GetListenerHealthStatusResponseBodyRuleHealthStatus] = None,
    ):
        # 监听健康检查结果
        self.listener_health_status = listener_health_status
        # 下一页标识
        self.next_token = next_token
        # 请求Id
        self.request_id = request_id
        # 转发规则健康检查结果
        self.rule_health_status = rule_health_status

    def validate(self):
        if self.listener_health_status:
            for k in self.listener_health_status:
                if k:
                    k.validate()
        if self.rule_health_status:
            for k in self.rule_health_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListenerHealthStatus'] = []
        if self.listener_health_status is not None:
            for k in self.listener_health_status:
                result['ListenerHealthStatus'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleHealthStatus'] = []
        if self.rule_health_status is not None:
            for k in self.rule_health_status:
                result['RuleHealthStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener_health_status = []
        if m.get('ListenerHealthStatus') is not None:
            for k in m.get('ListenerHealthStatus'):
                temp_model = GetListenerHealthStatusResponseBodyListenerHealthStatus()
                self.listener_health_status.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_health_status = []
        if m.get('RuleHealthStatus') is not None:
            for k in m.get('RuleHealthStatus'):
                temp_model = GetListenerHealthStatusResponseBodyRuleHealthStatus()
                self.rule_health_status.append(temp_model.from_map(k))
        return self


class GetListenerHealthStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetListenerHealthStatusResponseBody = None,
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
            temp_model = GetListenerHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoadBalancerAttributeRequest(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
    ):
        # 实例标识
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class GetLoadBalancerAttributeResponseBodyAccessLogConfig(TeaModel):
    def __init__(
        self,
        log_project: str = None,
        log_store: str = None,
    ):
        # 访问日志投递的logProject
        self.log_project = log_project
        # 删除保护开启时间
        self.log_store = log_store

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_project is not None:
            result['LogProject'] = self.log_project
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        return self


class GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        enabled_time: str = None,
    ):
        # 删除保护状态
        self.enabled = enabled
        # 删除保护开启时间
        self.enabled_time = enabled_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')
        return self


class GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig(TeaModel):
    def __init__(
        self,
        pay_type: str = None,
    ):
        # 实例的计费类型
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class GetLoadBalancerAttributeResponseBodyLoadBalancerOperationLocks(TeaModel):
    def __init__(
        self,
        lock_reason: str = None,
        lock_type: str = None,
    ):
        # 锁定原因
        self.lock_reason = lock_reason
        # 锁定类型
        self.lock_type = lock_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.lock_type is not None:
            result['LockType'] = self.lock_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('LockType') is not None:
            self.lock_type = m.get('LockType')
        return self


class GetLoadBalancerAttributeResponseBodyModificationProtectionConfig(TeaModel):
    def __init__(
        self,
        reason: str = None,
        status: str = None,
    ):
        # 设置修改保护状态的原因
        self.reason = reason
        # 负载均衡修改保护状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetLoadBalancerAttributeResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 实例的标签键
        self.key = key
        # 实例的标签值
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


class GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses(TeaModel):
    def __init__(
        self,
        address: str = None,
        ipv_6address: str = None,
    ):
        # IP地址
        self.address = address
        # Ipv6地址
        self.ipv_6address = ipv_6address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')
        return self


class GetLoadBalancerAttributeResponseBodyZoneMappings(TeaModel):
    def __init__(
        self,
        load_balancer_addresses: List[GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses] = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # 固定VIP模式下，负载均衡在此可用区中的地址列表
        self.load_balancer_addresses = load_balancer_addresses
        # 交换机标识
        self.v_switch_id = v_switch_id
        # 可用区标识
        self.zone_id = zone_id

    def validate(self):
        if self.load_balancer_addresses:
            for k in self.load_balancer_addresses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LoadBalancerAddresses'] = []
        if self.load_balancer_addresses is not None:
            for k in self.load_balancer_addresses:
                result['LoadBalancerAddresses'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancer_addresses = []
        if m.get('LoadBalancerAddresses') is not None:
            for k in m.get('LoadBalancerAddresses'):
                temp_model = GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses()
                self.load_balancer_addresses.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetLoadBalancerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        access_log_config: GetLoadBalancerAttributeResponseBodyAccessLogConfig = None,
        address_allocated_mode: str = None,
        address_ip_version: str = None,
        address_type: str = None,
        bandwidth_package_id: str = None,
        create_time: str = None,
        dnsname: str = None,
        deletion_protection_config: GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig = None,
        ipv_6address_type: str = None,
        load_balancer_billing_config: GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig = None,
        load_balancer_bussiness_status: str = None,
        load_balancer_edition: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_operation_locks: List[GetLoadBalancerAttributeResponseBodyLoadBalancerOperationLocks] = None,
        load_balancer_status: str = None,
        modification_protection_config: GetLoadBalancerAttributeResponseBodyModificationProtectionConfig = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        tags: List[GetLoadBalancerAttributeResponseBodyTags] = None,
        vpc_id: str = None,
        zone_mappings: List[GetLoadBalancerAttributeResponseBodyZoneMappings] = None,
    ):
        # 访问日志属性
        self.access_log_config = access_log_config
        # 地址分配方式
        self.address_allocated_mode = address_allocated_mode
        # 协议版本
        self.address_ip_version = address_ip_version
        # 地址类型
        self.address_type = address_type
        # 带宽包ID
        self.bandwidth_package_id = bandwidth_package_id
        # 资源创建时间
        self.create_time = create_time
        # DNS域名
        self.dnsname = dnsname
        # 负载均衡删除保护相关信息
        self.deletion_protection_config = deletion_protection_config
        # IPV6地址类型
        self.ipv_6address_type = ipv_6address_type
        # 计费相关属性
        self.load_balancer_billing_config = load_balancer_billing_config
        # 实例业务状态
        self.load_balancer_bussiness_status = load_balancer_bussiness_status
        # 负载均衡的版本
        self.load_balancer_edition = load_balancer_edition
        # 负载均衡标识
        self.load_balancer_id = load_balancer_id
        # 实例名称
        self.load_balancer_name = load_balancer_name
        # 锁定原因
        self.load_balancer_operation_locks = load_balancer_operation_locks
        # 实例状态
        self.load_balancer_status = load_balancer_status
        # 负载均衡修改保护相关信息
        self.modification_protection_config = modification_protection_config
        # 地域
        self.region_id = region_id
        # Id of the request
        self.request_id = request_id
        # 企业资源组ID
        self.resource_group_id = resource_group_id
        # 标签列表
        self.tags = tags
        # Vpc网络ID
        self.vpc_id = vpc_id
        # 负载均衡的可用区资源
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.access_log_config:
            self.access_log_config.validate()
        if self.deletion_protection_config:
            self.deletion_protection_config.validate()
        if self.load_balancer_billing_config:
            self.load_balancer_billing_config.validate()
        if self.load_balancer_operation_locks:
            for k in self.load_balancer_operation_locks:
                if k:
                    k.validate()
        if self.modification_protection_config:
            self.modification_protection_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_config is not None:
            result['AccessLogConfig'] = self.access_log_config.to_map()
        if self.address_allocated_mode is not None:
            result['AddressAllocatedMode'] = self.address_allocated_mode
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dnsname is not None:
            result['DNSName'] = self.dnsname
        if self.deletion_protection_config is not None:
            result['DeletionProtectionConfig'] = self.deletion_protection_config.to_map()
        if self.ipv_6address_type is not None:
            result['Ipv6AddressType'] = self.ipv_6address_type
        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()
        if self.load_balancer_bussiness_status is not None:
            result['LoadBalancerBussinessStatus'] = self.load_balancer_bussiness_status
        if self.load_balancer_edition is not None:
            result['LoadBalancerEdition'] = self.load_balancer_edition
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        result['LoadBalancerOperationLocks'] = []
        if self.load_balancer_operation_locks is not None:
            for k in self.load_balancer_operation_locks:
                result['LoadBalancerOperationLocks'].append(k.to_map() if k else None)
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogConfig') is not None:
            temp_model = GetLoadBalancerAttributeResponseBodyAccessLogConfig()
            self.access_log_config = temp_model.from_map(m['AccessLogConfig'])
        if m.get('AddressAllocatedMode') is not None:
            self.address_allocated_mode = m.get('AddressAllocatedMode')
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DNSName') is not None:
            self.dnsname = m.get('DNSName')
        if m.get('DeletionProtectionConfig') is not None:
            temp_model = GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig()
            self.deletion_protection_config = temp_model.from_map(m['DeletionProtectionConfig'])
        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')
        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig()
            self.load_balancer_billing_config = temp_model.from_map(m['LoadBalancerBillingConfig'])
        if m.get('LoadBalancerBussinessStatus') is not None:
            self.load_balancer_bussiness_status = m.get('LoadBalancerBussinessStatus')
        if m.get('LoadBalancerEdition') is not None:
            self.load_balancer_edition = m.get('LoadBalancerEdition')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        self.load_balancer_operation_locks = []
        if m.get('LoadBalancerOperationLocks') is not None:
            for k in m.get('LoadBalancerOperationLocks'):
                temp_model = GetLoadBalancerAttributeResponseBodyLoadBalancerOperationLocks()
                self.load_balancer_operation_locks.append(temp_model.from_map(k))
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('ModificationProtectionConfig') is not None:
            temp_model = GetLoadBalancerAttributeResponseBodyModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m['ModificationProtectionConfig'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetLoadBalancerAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = GetLoadBalancerAttributeResponseBodyZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class GetLoadBalancerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLoadBalancerAttributeResponseBody = None,
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
            temp_model = GetLoadBalancerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAclEntriesRequest(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # 访问控制策略Id
        self.acl_id = acl_id
        # 查询数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListAclEntriesResponseBodyAclEntries(TeaModel):
    def __init__(
        self,
        description: str = None,
        entry: str = None,
        status: str = None,
    ):
        # 描述信息
        self.description = description
        # IP条目
        self.entry = entry
        # 状态
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
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAclEntriesResponseBody(TeaModel):
    def __init__(
        self,
        acl_entries: List[ListAclEntriesResponseBodyAclEntries] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 访问控制列表
        self.acl_entries = acl_entries
        # 本次查询返回记录数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = ListAclEntriesResponseBodyAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAclEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAclEntriesResponseBody = None,
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
            temp_model = ListAclEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAclRelationsRequest(TeaModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
    ):
        # 访问控制策略Id
        self.acl_ids = acl_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        return self


class ListAclRelationsResponseBodyAclRelationsRelatedListeners(TeaModel):
    def __init__(
        self,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balancer_id: str = None,
        status: str = None,
    ):
        # 监听ID
        self.listener_id = listener_id
        # 监听端口
        self.listener_port = listener_port
        # 监听协议
        self.listener_protocol = listener_protocol
        # 实例ID
        self.load_balancer_id = load_balancer_id
        # 关联状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAclRelationsResponseBodyAclRelations(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        related_listeners: List[ListAclRelationsResponseBodyAclRelationsRelatedListeners] = None,
    ):
        # 访问控制策略id
        self.acl_id = acl_id
        # 关联的监听
        self.related_listeners = related_listeners

    def validate(self):
        if self.related_listeners:
            for k in self.related_listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        result['RelatedListeners'] = []
        if self.related_listeners is not None:
            for k in self.related_listeners:
                result['RelatedListeners'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        self.related_listeners = []
        if m.get('RelatedListeners') is not None:
            for k in m.get('RelatedListeners'):
                temp_model = ListAclRelationsResponseBodyAclRelationsRelatedListeners()
                self.related_listeners.append(temp_model.from_map(k))
        return self


class ListAclRelationsResponseBody(TeaModel):
    def __init__(
        self,
        acl_relations: List[ListAclRelationsResponseBodyAclRelations] = None,
        request_id: str = None,
    ):
        # 访问控制列表
        self.acl_relations = acl_relations
        # 请求id
        self.request_id = request_id

    def validate(self):
        if self.acl_relations:
            for k in self.acl_relations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclRelations'] = []
        if self.acl_relations is not None:
            for k in self.acl_relations:
                result['AclRelations'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_relations = []
        if m.get('AclRelations') is not None:
            for k in m.get('AclRelations'):
                temp_model = ListAclRelationsResponseBodyAclRelations()
                self.acl_relations.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAclRelationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAclRelationsResponseBody = None,
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
            temp_model = ListAclRelationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAclsRequest(TeaModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
        acl_names: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
    ):
        # 访问控制策略Id
        self.acl_ids = acl_ids
        # 访问控制策略名称
        self.acl_names = acl_names
        # 查询数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # 资源组ID
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.acl_names is not None:
            result['AclNames'] = self.acl_names
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('AclNames') is not None:
            self.acl_names = m.get('AclNames')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListAclsResponseBodyAcls(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_name: str = None,
        acl_status: str = None,
        address_ipversion: str = None,
        config_managed_enabled: bool = None,
        resource_group_id: str = None,
    ):
        # 访问控制策略id
        self.acl_id = acl_id
        # 访问控制策略名称
        self.acl_name = acl_name
        # 状态
        self.acl_status = acl_status
        # IP版本
        self.address_ipversion = address_ipversion
        # 配置管理
        self.config_managed_enabled = config_managed_enabled
        # 资源组ID
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.config_managed_enabled is not None:
            result['ConfigManagedEnabled'] = self.config_managed_enabled
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('ConfigManagedEnabled') is not None:
            self.config_managed_enabled = m.get('ConfigManagedEnabled')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListAclsResponseBody(TeaModel):
    def __init__(
        self,
        acls: List[ListAclsResponseBodyAcls] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 访问控制列表
        self.acls = acls
        # 本次查询返回记录数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.acls:
            for k in self.acls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Acls'] = []
        if self.acls is not None:
            for k in self.acls:
                result['Acls'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acls = []
        if m.get('Acls') is not None:
            for k in m.get('Acls'):
                temp_model = ListAclsResponseBodyAcls()
                self.acls.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAclsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAclsResponseBody = None,
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
            temp_model = ListAclsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAsynJobsRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        begin_time: int = None,
        end_time: int = None,
        job_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # 操作接口名
        self.api_name = api_name
        # 任务过滤时间范围-开始时间
        self.begin_time = begin_time
        # 任务过滤时间范围-结束时间
        self.end_time = end_time
        # 任务ID列表
        self.job_ids = job_ids
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 下一个查询开始Token
        self.next_token = next_token
        # 资源实例ID列表
        self.resource_ids = resource_ids
        # 资源类型类型
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListAsynJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        create_time: int = None,
        error_code: str = None,
        error_message: str = None,
        id: str = None,
        modify_time: int = None,
        operate_type: str = None,
        resource_id: str = None,
        resource_type: str = None,
        status: str = None,
    ):
        # openapi名称
        self.api_name = api_name
        # 任务开始时间戳
        self.create_time = create_time
        # 如果Status为失败，则为错误码
        self.error_code = error_code
        # 如果Status为失败，则为错误信息
        self.error_message = error_message
        # 任务ID
        self.id = id
        # 任务结束时间戳
        self.modify_time = modify_time
        # 操作类型
        self.operate_type = operate_type
        # 关联的资源实例ID
        self.resource_id = resource_id
        # 关联的资源类型
        self.resource_type = resource_type
        # 任务状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAsynJobsResponseBody(TeaModel):
    def __init__(
        self,
        jobs: List[ListAsynJobsResponseBodyJobs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 任务列表
        self.jobs = jobs
        # 本次查询返回记录数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 总记录数
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
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListAsynJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAsynJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAsynJobsResponseBody = None,
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
            temp_model = ListAsynJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHealthCheckTemplatesRequest(TeaModel):
    def __init__(
        self,
        health_check_template_ids: List[str] = None,
        health_check_template_names: List[str] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # 健康检查模板ID列表
        self.health_check_template_ids = health_check_template_ids
        # 健康检查模板名称列表
        self.health_check_template_names = health_check_template_names
        # 查询数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_template_ids is not None:
            result['HealthCheckTemplateIds'] = self.health_check_template_ids
        if self.health_check_template_names is not None:
            result['HealthCheckTemplateNames'] = self.health_check_template_names
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckTemplateIds') is not None:
            self.health_check_template_ids = m.get('HealthCheckTemplateIds')
        if m.get('HealthCheckTemplateNames') is not None:
            self.health_check_template_names = m.get('HealthCheckTemplateNames')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListHealthCheckTemplatesResponseBodyHealthCheckTemplates(TeaModel):
    def __init__(
        self,
        health_check_codes: List[str] = None,
        health_check_connect_port: int = None,
        health_check_host: str = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_path: str = None,
        health_check_protocol: str = None,
        health_check_template_id: str = None,
        health_check_template_name: str = None,
        health_check_timeout: int = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
    ):
        # 状态码
        self.health_check_codes = health_check_codes
        # 端口
        self.health_check_connect_port = health_check_connect_port
        # 域名
        self.health_check_host = health_check_host
        # 版本
        self.health_check_http_version = health_check_http_version
        # 间隔时间
        self.health_check_interval = health_check_interval
        # 方法
        self.health_check_method = health_check_method
        # uri
        self.health_check_path = health_check_path
        # 协议
        self.health_check_protocol = health_check_protocol
        # 健康检查模板Id
        self.health_check_template_id = health_check_template_id
        # 名称
        self.health_check_template_name = health_check_template_name
        # 超时时间
        self.health_check_timeout = health_check_timeout
        # 健康阈值
        self.healthy_threshold = healthy_threshold
        # 不健康阈值
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_codes is not None:
            result['HealthCheckCodes'] = self.health_check_codes
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_host is not None:
            result['HealthCheckHost'] = self.health_check_host
        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.health_check_template_id is not None:
            result['HealthCheckTemplateId'] = self.health_check_template_id
        if self.health_check_template_name is not None:
            result['HealthCheckTemplateName'] = self.health_check_template_name
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckCodes') is not None:
            self.health_check_codes = m.get('HealthCheckCodes')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckHost') is not None:
            self.health_check_host = m.get('HealthCheckHost')
        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('HealthCheckTemplateId') is not None:
            self.health_check_template_id = m.get('HealthCheckTemplateId')
        if m.get('HealthCheckTemplateName') is not None:
            self.health_check_template_name = m.get('HealthCheckTemplateName')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class ListHealthCheckTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        health_check_templates: List[ListHealthCheckTemplatesResponseBodyHealthCheckTemplates] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 健康检查模板
        self.health_check_templates = health_check_templates
        # 本次查询返回记录数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.health_check_templates:
            for k in self.health_check_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HealthCheckTemplates'] = []
        if self.health_check_templates is not None:
            for k in self.health_check_templates:
                result['HealthCheckTemplates'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.health_check_templates = []
        if m.get('HealthCheckTemplates') is not None:
            for k in m.get('HealthCheckTemplates'):
                temp_model = ListHealthCheckTemplatesResponseBodyHealthCheckTemplates()
                self.health_check_templates.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHealthCheckTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHealthCheckTemplatesResponseBody = None,
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
            temp_model = ListHealthCheckTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenerCertificatesRequest(TeaModel):
    def __init__(
        self,
        certificate_type: str = None,
        listener_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # 证书类型
        self.certificate_type = certificate_type
        # 监听Id
        self.listener_id = listener_id
        # 查询数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListListenerCertificatesResponseBodyCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        certificate_type: str = None,
        is_default: bool = None,
        status: str = None,
    ):
        # 证书Id
        self.certificate_id = certificate_id
        # 证书类型
        self.certificate_type = certificate_type
        # 是否为默认证书
        self.is_default = is_default
        # 证书状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListListenerCertificatesResponseBody(TeaModel):
    def __init__(
        self,
        certificates: List[ListListenerCertificatesResponseBodyCertificates] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 监听SSL证书列表
        self.certificates = certificates
        # 本次查询返回记录数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = ListListenerCertificatesResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenerCertificatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListListenerCertificatesResponseBody = None,
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
            temp_model = ListListenerCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersRequest(TeaModel):
    def __init__(
        self,
        listener_ids: List[str] = None,
        listener_protocol: str = None,
        load_balancer_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # 监听ID列表，N最大支持20
        self.listener_ids = listener_ids
        # 监听协议
        self.listener_protocol = listener_protocol
        # 实例ID列表，N最大支持20
        self.load_balancer_ids = load_balancer_ids
        # 本次读取的最大数据记录数量，此参数为可选参数，取值1-100，用户传入为空时，默认为20。
        self.max_results = max_results
        # 用来标记当前开始读取的位置，置空表示从头开始。
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_ids is not None:
            result['ListenerIds'] = self.listener_ids
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerIds') is not None:
            self.listener_ids = m.get('ListenerIds')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListListenersResponseBodyListenersDefaultActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        # 服务器组ID
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class ListListenersResponseBodyListenersDefaultActionsForwardGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[ListListenersResponseBodyListenersDefaultActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # 服务器组列表
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = ListListenersResponseBodyListenersDefaultActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class ListListenersResponseBodyListenersDefaultActions(TeaModel):
    def __init__(
        self,
        forward_group_config: ListListenersResponseBodyListenersDefaultActionsForwardGroupConfig = None,
        type: str = None,
    ):
        # 转发到服务器组
        self.forward_group_config = forward_group_config
        # 类型
        self.type = type

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = ListListenersResponseBodyListenersDefaultActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListListenersResponseBodyListenersLogConfigAccessLogTracingConfig(TeaModel):
    def __init__(
        self,
        tracing_enabled: bool = None,
        tracing_sample: int = None,
        tracing_type: str = None,
    ):
        # Xtrace功能状态
        self.tracing_enabled = tracing_enabled
        # Xtrace功能状态
        self.tracing_sample = tracing_sample
        # xtrace的类型
        self.tracing_type = tracing_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tracing_enabled is not None:
            result['TracingEnabled'] = self.tracing_enabled
        if self.tracing_sample is not None:
            result['TracingSample'] = self.tracing_sample
        if self.tracing_type is not None:
            result['TracingType'] = self.tracing_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TracingEnabled') is not None:
            self.tracing_enabled = m.get('TracingEnabled')
        if m.get('TracingSample') is not None:
            self.tracing_sample = m.get('TracingSample')
        if m.get('TracingType') is not None:
            self.tracing_type = m.get('TracingType')
        return self


class ListListenersResponseBodyListenersLogConfig(TeaModel):
    def __init__(
        self,
        access_log_record_customized_headers_enabled: bool = None,
        access_log_tracing_config: ListListenersResponseBodyListenersLogConfigAccessLogTracingConfig = None,
    ):
        # 访问日志是否开启携带自定义Header
        self.access_log_record_customized_headers_enabled = access_log_record_customized_headers_enabled
        # 访问日志Xtrace相关的配置
        self.access_log_tracing_config = access_log_tracing_config

    def validate(self):
        if self.access_log_tracing_config:
            self.access_log_tracing_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_record_customized_headers_enabled is not None:
            result['AccessLogRecordCustomizedHeadersEnabled'] = self.access_log_record_customized_headers_enabled
        if self.access_log_tracing_config is not None:
            result['AccessLogTracingConfig'] = self.access_log_tracing_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogRecordCustomizedHeadersEnabled') is not None:
            self.access_log_record_customized_headers_enabled = m.get('AccessLogRecordCustomizedHeadersEnabled')
        if m.get('AccessLogTracingConfig') is not None:
            temp_model = ListListenersResponseBodyListenersLogConfigAccessLogTracingConfig()
            self.access_log_tracing_config = temp_model.from_map(m['AccessLogTracingConfig'])
        return self


class ListListenersResponseBodyListenersQuicConfig(TeaModel):
    def __init__(
        self,
        quic_listener_id: str = None,
        quic_upgrade_enabled: bool = None,
    ):
        # 需要关联的QUIC监听ID，HTTPS监听时有效，QuicUpgradeEnabled为true时必选
        self.quic_listener_id = quic_listener_id
        # 是否开启quic升级，HTTPS监听时有效
        self.quic_upgrade_enabled = quic_upgrade_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quic_listener_id is not None:
            result['QuicListenerId'] = self.quic_listener_id
        if self.quic_upgrade_enabled is not None:
            result['QuicUpgradeEnabled'] = self.quic_upgrade_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuicListenerId') is not None:
            self.quic_listener_id = m.get('QuicListenerId')
        if m.get('QuicUpgradeEnabled') is not None:
            self.quic_upgrade_enabled = m.get('QuicUpgradeEnabled')
        return self


class ListListenersResponseBodyListenersXForwardedForConfig(TeaModel):
    def __init__(
        self,
        xforwarded_for_client_cert_client_verify_alias: str = None,
        xforwarded_for_client_cert_client_verify_enabled: bool = None,
        xforwarded_for_client_cert_fingerprint_alias: str = None,
        xforwarded_for_client_cert_fingerprint_enabled: bool = None,
        xforwarded_for_client_cert_issuer_dnalias: str = None,
        xforwarded_for_client_cert_issuer_dnenabled: bool = None,
        xforwarded_for_client_cert_subject_dnalias: str = None,
        xforwarded_for_client_cert_subject_dnenabled: bool = None,
        xforwarded_for_client_src_port_enabled: bool = None,
        xforwarded_for_enabled: bool = None,
        xforwarded_for_proto_enabled: bool = None,
        xforwarded_for_slbid_enabled: bool = None,
        xforwarded_for_slbport_enabled: bool = None,
    ):
        # 自定义HEADER头名称，只有当XForwardedForClientCertClientVerifyEnabled的值为true的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_client_verify_alias = xforwarded_for_client_cert_client_verify_alias
        # 是否通过X-Forwarded-Clientcert-clientverify  头字段获取对访问负载均衡实例客户端证书的校验结果。HTTPS监听有效。
        self.xforwarded_for_client_cert_client_verify_enabled = xforwarded_for_client_cert_client_verify_enabled
        # 自定义HEADER头名称，只有当XForwardedForClientCertFingerprintEnabled的值为true的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_fingerprint_alias = xforwarded_for_client_cert_fingerprint_alias
        # 是否通过X-Forwarded-Clientcert-fingerprint 头字段获取访问负载均衡实例客户端证书的指纹取值，HTTPS监听有效。
        self.xforwarded_for_client_cert_fingerprint_enabled = xforwarded_for_client_cert_fingerprint_enabled
        # 自定义HEADER头名称，只有当XForwardedForClientCertIssuerDNEnabled的值为‘On’的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_issuer_dnalias = xforwarded_for_client_cert_issuer_dnalias
        # 是否通过 X-Forwarded-Clientcert-issuerdn 头字段获取访问负载均衡实例客户端证书的发行者信息。HTTPS监听有效。
        self.xforwarded_for_client_cert_issuer_dnenabled = xforwarded_for_client_cert_issuer_dnenabled
        # 自定义HEADER头名称，只有当XForwardedForClientCertSubjectDNEnabled的值为true的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_subject_dnalias = xforwarded_for_client_cert_subject_dnalias
        # 是否通过X-Forwarded-Clientcert-subjectdn  头字段获取访问负载均衡实例客户端证书的所有者信息。HTTPS监听有效。
        self.xforwarded_for_client_cert_subject_dnenabled = xforwarded_for_client_cert_subject_dnenabled
        # 是否通过X-Forwarded-Client-Port 头字段获取访问负载均衡实例客户端的端口。HTTPS监听有效。
        self.xforwarded_for_client_src_port_enabled = xforwarded_for_client_src_port_enabled
        # 是否开启通过X-Forwarded-For头字段获取来访者真实 IP
        self.xforwarded_for_enabled = xforwarded_for_enabled
        # 是否通过X-Forwarded-Proto头字段获取负载均衡实例的监听协议。
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        # 是否通过SLB-ID头字段获取负载均衡实例ID。
        self.xforwarded_for_slbid_enabled = xforwarded_for_slbid_enabled
        # 是否通过X-Forwarded-Port 头字段获取负载均衡实例的监听端口。HTTPS监听有效。
        self.xforwarded_for_slbport_enabled = xforwarded_for_slbport_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.xforwarded_for_client_cert_client_verify_alias is not None:
            result['XForwardedForClientCertClientVerifyAlias'] = self.xforwarded_for_client_cert_client_verify_alias
        if self.xforwarded_for_client_cert_client_verify_enabled is not None:
            result['XForwardedForClientCertClientVerifyEnabled'] = self.xforwarded_for_client_cert_client_verify_enabled
        if self.xforwarded_for_client_cert_fingerprint_alias is not None:
            result['XForwardedForClientCertFingerprintAlias'] = self.xforwarded_for_client_cert_fingerprint_alias
        if self.xforwarded_for_client_cert_fingerprint_enabled is not None:
            result['XForwardedForClientCertFingerprintEnabled'] = self.xforwarded_for_client_cert_fingerprint_enabled
        if self.xforwarded_for_client_cert_issuer_dnalias is not None:
            result['XForwardedForClientCertIssuerDNAlias'] = self.xforwarded_for_client_cert_issuer_dnalias
        if self.xforwarded_for_client_cert_issuer_dnenabled is not None:
            result['XForwardedForClientCertIssuerDNEnabled'] = self.xforwarded_for_client_cert_issuer_dnenabled
        if self.xforwarded_for_client_cert_subject_dnalias is not None:
            result['XForwardedForClientCertSubjectDNAlias'] = self.xforwarded_for_client_cert_subject_dnalias
        if self.xforwarded_for_client_cert_subject_dnenabled is not None:
            result['XForwardedForClientCertSubjectDNEnabled'] = self.xforwarded_for_client_cert_subject_dnenabled
        if self.xforwarded_for_client_src_port_enabled is not None:
            result['XForwardedForClientSrcPortEnabled'] = self.xforwarded_for_client_src_port_enabled
        if self.xforwarded_for_enabled is not None:
            result['XForwardedForEnabled'] = self.xforwarded_for_enabled
        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled
        if self.xforwarded_for_slbid_enabled is not None:
            result['XForwardedForSLBIdEnabled'] = self.xforwarded_for_slbid_enabled
        if self.xforwarded_for_slbport_enabled is not None:
            result['XForwardedForSLBPortEnabled'] = self.xforwarded_for_slbport_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('XForwardedForClientCertClientVerifyAlias') is not None:
            self.xforwarded_for_client_cert_client_verify_alias = m.get('XForwardedForClientCertClientVerifyAlias')
        if m.get('XForwardedForClientCertClientVerifyEnabled') is not None:
            self.xforwarded_for_client_cert_client_verify_enabled = m.get('XForwardedForClientCertClientVerifyEnabled')
        if m.get('XForwardedForClientCertFingerprintAlias') is not None:
            self.xforwarded_for_client_cert_fingerprint_alias = m.get('XForwardedForClientCertFingerprintAlias')
        if m.get('XForwardedForClientCertFingerprintEnabled') is not None:
            self.xforwarded_for_client_cert_fingerprint_enabled = m.get('XForwardedForClientCertFingerprintEnabled')
        if m.get('XForwardedForClientCertIssuerDNAlias') is not None:
            self.xforwarded_for_client_cert_issuer_dnalias = m.get('XForwardedForClientCertIssuerDNAlias')
        if m.get('XForwardedForClientCertIssuerDNEnabled') is not None:
            self.xforwarded_for_client_cert_issuer_dnenabled = m.get('XForwardedForClientCertIssuerDNEnabled')
        if m.get('XForwardedForClientCertSubjectDNAlias') is not None:
            self.xforwarded_for_client_cert_subject_dnalias = m.get('XForwardedForClientCertSubjectDNAlias')
        if m.get('XForwardedForClientCertSubjectDNEnabled') is not None:
            self.xforwarded_for_client_cert_subject_dnenabled = m.get('XForwardedForClientCertSubjectDNEnabled')
        if m.get('XForwardedForClientSrcPortEnabled') is not None:
            self.xforwarded_for_client_src_port_enabled = m.get('XForwardedForClientSrcPortEnabled')
        if m.get('XForwardedForEnabled') is not None:
            self.xforwarded_for_enabled = m.get('XForwardedForEnabled')
        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')
        if m.get('XForwardedForSLBIdEnabled') is not None:
            self.xforwarded_for_slbid_enabled = m.get('XForwardedForSLBIdEnabled')
        if m.get('XForwardedForSLBPortEnabled') is not None:
            self.xforwarded_for_slbport_enabled = m.get('XForwardedForSLBPortEnabled')
        return self


class ListListenersResponseBodyListeners(TeaModel):
    def __init__(
        self,
        ca_enabled: str = None,
        default_actions: List[ListListenersResponseBodyListenersDefaultActions] = None,
        gzip_enabled: bool = None,
        http_2enabled: bool = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        listener_status: str = None,
        load_balancer_id: str = None,
        log_config: ListListenersResponseBodyListenersLogConfig = None,
        quic_config: ListListenersResponseBodyListenersQuicConfig = None,
        request_timeout: int = None,
        security_policy_id: str = None,
        xforwarded_for_config: ListListenersResponseBodyListenersXForwardedForConfig = None,
    ):
        # 是否开启双向认证
        self.ca_enabled = ca_enabled
        # 默认动作
        self.default_actions = default_actions
        # 是否开启Gzip压缩
        self.gzip_enabled = gzip_enabled
        # 是否开启HTTP/2特性
        self.http_2enabled = http_2enabled
        # 连接空闲超时时间
        self.idle_timeout = idle_timeout
        # 监听描述
        self.listener_description = listener_description
        # 监听标识
        self.listener_id = listener_id
        # 监听端口
        self.listener_port = listener_port
        # 监听协议
        self.listener_protocol = listener_protocol
        # 监听状态
        self.listener_status = listener_status
        # 负载均衡标识
        self.load_balancer_id = load_balancer_id
        # 监听访问日志相关配置
        self.log_config = log_config
        # HTTPS启用QUIC时相关属性
        self.quic_config = quic_config
        # 请求超时时间
        self.request_timeout = request_timeout
        # 安全策略
        self.security_policy_id = security_policy_id
        # XForward字段相关的配置
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
        if self.default_actions:
            for k in self.default_actions:
                if k:
                    k.validate()
        if self.log_config:
            self.log_config.validate()
        if self.quic_config:
            self.quic_config.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        result['DefaultActions'] = []
        if self.default_actions is not None:
            for k in self.default_actions:
                result['DefaultActions'].append(k.to_map() if k else None)
        if self.gzip_enabled is not None:
            result['GzipEnabled'] = self.gzip_enabled
        if self.http_2enabled is not None:
            result['Http2Enabled'] = self.http_2enabled
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.listener_status is not None:
            result['ListenerStatus'] = self.listener_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.log_config is not None:
            result['LogConfig'] = self.log_config.to_map()
        if self.quic_config is not None:
            result['QuicConfig'] = self.quic_config.to_map()
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        self.default_actions = []
        if m.get('DefaultActions') is not None:
            for k in m.get('DefaultActions'):
                temp_model = ListListenersResponseBodyListenersDefaultActions()
                self.default_actions.append(temp_model.from_map(k))
        if m.get('GzipEnabled') is not None:
            self.gzip_enabled = m.get('GzipEnabled')
        if m.get('Http2Enabled') is not None:
            self.http_2enabled = m.get('Http2Enabled')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('ListenerStatus') is not None:
            self.listener_status = m.get('ListenerStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LogConfig') is not None:
            temp_model = ListListenersResponseBodyListenersLogConfig()
            self.log_config = temp_model.from_map(m['LogConfig'])
        if m.get('QuicConfig') is not None:
            temp_model = ListListenersResponseBodyListenersQuicConfig()
            self.quic_config = temp_model.from_map(m['QuicConfig'])
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('XForwardedForConfig') is not None:
            temp_model = ListListenersResponseBodyListenersXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m['XForwardedForConfig'])
        return self


class ListListenersResponseBody(TeaModel):
    def __init__(
        self,
        listeners: List[ListListenersResponseBodyListeners] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 监听列表
        self.listeners = listeners
        # 本次请求所返回的最大记录条数。
        self.max_results = max_results
        # 用来表示当前调用返回读取到的位置，空代表数据已经读取完毕。
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 本次请求条件下的数据总量。
        self.total_count = total_count

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListListenersResponseBody = None,
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
            temp_model = ListListenersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLoadBalancersRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 实例的标签键
        self.key = key
        # 实例的标签值
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


class ListLoadBalancersRequest(TeaModel):
    def __init__(
        self,
        address_type: str = None,
        load_balancer_bussiness_status: str = None,
        load_balancer_ids: List[str] = None,
        load_balancer_names: List[str] = None,
        load_balancer_status: str = None,
        max_results: int = None,
        next_token: str = None,
        pay_type: str = None,
        resource_group_id: str = None,
        tag: List[ListLoadBalancersRequestTag] = None,
        vpc_ids: List[str] = None,
        zone_id: str = None,
    ):
        # 负载均衡的地址类型
        self.address_type = address_type
        # 实例业务状态
        self.load_balancer_bussiness_status = load_balancer_bussiness_status
        # 实例ID列表，N最大支持20
        self.load_balancer_ids = load_balancer_ids
        # 实例Name列表，N最大支持10
        self.load_balancer_names = load_balancer_names
        # 实例状态
        self.load_balancer_status = load_balancer_status
        # 本次读取的最大数据记录数量，此参数为可选参数，取值1-100，用户传入为空时，默认为20。
        self.max_results = max_results
        # 用来标记当前开始读取的位置，置空表示从头开始。
        self.next_token = next_token
        # 付费类型
        self.pay_type = pay_type
        # 资源组ID
        self.resource_group_id = resource_group_id
        # tag列表
        self.tag = tag
        # vpcId列表
        self.vpc_ids = vpc_ids
        # 可用区ID
        self.zone_id = zone_id

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
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.load_balancer_bussiness_status is not None:
            result['LoadBalancerBussinessStatus'] = self.load_balancer_bussiness_status
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids
        if self.load_balancer_names is not None:
            result['LoadBalancerNames'] = self.load_balancer_names
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('LoadBalancerBussinessStatus') is not None:
            self.load_balancer_bussiness_status = m.get('LoadBalancerBussinessStatus')
        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')
        if m.get('LoadBalancerNames') is not None:
            self.load_balancer_names = m.get('LoadBalancerNames')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListLoadBalancersRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListLoadBalancersResponseBodyLoadBalancersAccessLogConfig(TeaModel):
    def __init__(
        self,
        log_project: str = None,
        log_store: str = None,
    ):
        # 访问日志投递的logProject
        self.log_project = log_project
        # 删除保护开启时间
        self.log_store = log_store

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_project is not None:
            result['LogProject'] = self.log_project
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        return self


class ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        enabled_time: str = None,
    ):
        # 删除保护状态
        self.enabled = enabled
        # 删除保护开启时间
        self.enabled_time = enabled_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')
        return self


class ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig(TeaModel):
    def __init__(
        self,
        pay_type: str = None,
    ):
        # 实例的计费类型
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class ListLoadBalancersResponseBodyLoadBalancersLoadBalancerOperationLocks(TeaModel):
    def __init__(
        self,
        lock_reason: str = None,
        lock_type: str = None,
    ):
        # 锁定的原因
        self.lock_reason = lock_reason
        # 锁定的类型
        self.lock_type = lock_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.lock_type is not None:
            result['LockType'] = self.lock_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('LockType') is not None:
            self.lock_type = m.get('LockType')
        return self


class ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig(TeaModel):
    def __init__(
        self,
        reason: str = None,
        status: str = None,
    ):
        # 设置修改保护状态的原因
        self.reason = reason
        # 负载均衡修改保护状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLoadBalancersResponseBodyLoadBalancersTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 实例的标签键
        self.key = key
        # 实例的标签值
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


class ListLoadBalancersResponseBodyLoadBalancers(TeaModel):
    def __init__(
        self,
        access_log_config: ListLoadBalancersResponseBodyLoadBalancersAccessLogConfig = None,
        address_allocated_mode: str = None,
        address_ip_version: str = None,
        address_type: str = None,
        bandwidth_package_id: str = None,
        create_time: str = None,
        dnsname: str = None,
        deletion_protection_config: ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig = None,
        ipv_6address_type: str = None,
        load_balancer_billing_config: ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig = None,
        load_balancer_bussiness_status: str = None,
        load_balancer_edition: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_operation_locks: List[ListLoadBalancersResponseBodyLoadBalancersLoadBalancerOperationLocks] = None,
        load_balancer_status: str = None,
        modification_protection_config: ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig = None,
        resource_group_id: str = None,
        tags: List[ListLoadBalancersResponseBodyLoadBalancersTags] = None,
        vpc_id: str = None,
    ):
        # 访问日志属性
        self.access_log_config = access_log_config
        # 地址模式
        self.address_allocated_mode = address_allocated_mode
        # 协议版本
        self.address_ip_version = address_ip_version
        # 地址类型
        self.address_type = address_type
        # 带宽包ID
        self.bandwidth_package_id = bandwidth_package_id
        # 资源创建时间
        self.create_time = create_time
        # DNS域名
        self.dnsname = dnsname
        # 负载均衡删除保护相关信息
        self.deletion_protection_config = deletion_protection_config
        # IPV6地址类型
        self.ipv_6address_type = ipv_6address_type
        # 计费相关属性
        self.load_balancer_billing_config = load_balancer_billing_config
        # 实例业务状态
        self.load_balancer_bussiness_status = load_balancer_bussiness_status
        # 负载均衡的版本
        self.load_balancer_edition = load_balancer_edition
        # 负载均衡标识
        self.load_balancer_id = load_balancer_id
        # 实例名称
        self.load_balancer_name = load_balancer_name
        # 锁定的原因
        self.load_balancer_operation_locks = load_balancer_operation_locks
        # 实例状态
        self.load_balancer_status = load_balancer_status
        # 负载均衡修改保护相关信息
        self.modification_protection_config = modification_protection_config
        # 企业资源组ID
        self.resource_group_id = resource_group_id
        # 标签列表
        self.tags = tags
        # Vpc网络ID
        self.vpc_id = vpc_id

    def validate(self):
        if self.access_log_config:
            self.access_log_config.validate()
        if self.deletion_protection_config:
            self.deletion_protection_config.validate()
        if self.load_balancer_billing_config:
            self.load_balancer_billing_config.validate()
        if self.load_balancer_operation_locks:
            for k in self.load_balancer_operation_locks:
                if k:
                    k.validate()
        if self.modification_protection_config:
            self.modification_protection_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_config is not None:
            result['AccessLogConfig'] = self.access_log_config.to_map()
        if self.address_allocated_mode is not None:
            result['AddressAllocatedMode'] = self.address_allocated_mode
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dnsname is not None:
            result['DNSName'] = self.dnsname
        if self.deletion_protection_config is not None:
            result['DeletionProtectionConfig'] = self.deletion_protection_config.to_map()
        if self.ipv_6address_type is not None:
            result['Ipv6AddressType'] = self.ipv_6address_type
        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()
        if self.load_balancer_bussiness_status is not None:
            result['LoadBalancerBussinessStatus'] = self.load_balancer_bussiness_status
        if self.load_balancer_edition is not None:
            result['LoadBalancerEdition'] = self.load_balancer_edition
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        result['LoadBalancerOperationLocks'] = []
        if self.load_balancer_operation_locks is not None:
            for k in self.load_balancer_operation_locks:
                result['LoadBalancerOperationLocks'].append(k.to_map() if k else None)
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogConfig') is not None:
            temp_model = ListLoadBalancersResponseBodyLoadBalancersAccessLogConfig()
            self.access_log_config = temp_model.from_map(m['AccessLogConfig'])
        if m.get('AddressAllocatedMode') is not None:
            self.address_allocated_mode = m.get('AddressAllocatedMode')
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DNSName') is not None:
            self.dnsname = m.get('DNSName')
        if m.get('DeletionProtectionConfig') is not None:
            temp_model = ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig()
            self.deletion_protection_config = temp_model.from_map(m['DeletionProtectionConfig'])
        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')
        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig()
            self.load_balancer_billing_config = temp_model.from_map(m['LoadBalancerBillingConfig'])
        if m.get('LoadBalancerBussinessStatus') is not None:
            self.load_balancer_bussiness_status = m.get('LoadBalancerBussinessStatus')
        if m.get('LoadBalancerEdition') is not None:
            self.load_balancer_edition = m.get('LoadBalancerEdition')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        self.load_balancer_operation_locks = []
        if m.get('LoadBalancerOperationLocks') is not None:
            for k in m.get('LoadBalancerOperationLocks'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancersLoadBalancerOperationLocks()
                self.load_balancer_operation_locks.append(temp_model.from_map(k))
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('ModificationProtectionConfig') is not None:
            temp_model = ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m['ModificationProtectionConfig'])
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancersTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListLoadBalancersResponseBody(TeaModel):
    def __init__(
        self,
        load_balancers: List[ListLoadBalancersResponseBodyLoadBalancers] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 实例列表
        self.load_balancers = load_balancers
        # 本次请求所返回的最大记录条数。
        self.max_results = max_results
        # 用来表示当前调用返回读取到的位置，空代表数据已经读取完毕。
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 本次请求条件下的数据总量。
        self.total_count = total_count

    def validate(self):
        if self.load_balancers:
            for k in self.load_balancers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LoadBalancers'] = []
        if self.load_balancers is not None:
            for k in self.load_balancers:
                result['LoadBalancers'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancers = []
        if m.get('LoadBalancers') is not None:
            for k in m.get('LoadBalancers'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLoadBalancersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLoadBalancersResponseBody = None,
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
            temp_model = ListLoadBalancersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(
        self,
        listener_ids: List[str] = None,
        load_balancer_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        rule_ids: List[str] = None,
    ):
        # 监听ID列表
        self.listener_ids = listener_ids
        # 实例ID列表
        self.load_balancer_ids = load_balancer_ids
        # 本次读取的最大数据记录数量，此参数为可选参数，取值1-100，用户传入为空时，默认为20。
        self.max_results = max_results
        # 用来标记当前开始读取的位置，置空表示从头开始。
        self.next_token = next_token
        # 转发规则ID列表，N最大支持20
        self.rule_ids = rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_ids is not None:
            result['ListenerIds'] = self.listener_ids
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerIds') is not None:
            self.listener_ids = m.get('ListenerIds')
        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        return self


class ListRulesResponseBodyRulesRuleActionsFixedResponseConfig(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        http_code: str = None,
    ):
        # 内容
        self.content = content
        # 内容类型
        self.content_type = content_type
        # HTTP响应码
        self.http_code = http_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        return self


class ListRulesResponseBodyRulesRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        # 服务器组标识
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class ListRulesResponseBodyRulesRuleActionsForwardGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[ListRulesResponseBodyRulesRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # 转发到的目的服务器组列表
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = ListRulesResponseBodyRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class ListRulesResponseBodyRulesRuleActionsInsertHeaderConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        value_type: str = None,
    ):
        # HTTP标头
        self.key = key
        # HTTP标头内容
        self.value = value
        # 取值类型
        self.value_type = value_type

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
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class ListRulesResponseBodyRulesRuleActionsRedirectConfig(TeaModel):
    def __init__(
        self,
        host: str = None,
        http_code: str = None,
        path: str = None,
        port: str = None,
        protocol: str = None,
        query: str = None,
    ):
        # 要跳转的主机地址
        self.host = host
        # 跳转方式
        self.http_code = http_code
        # 要跳转的路径
        self.path = path
        # 要跳转的端口
        self.port = port
        # 要跳转的协议
        self.protocol = protocol
        # 要跳转的查询字符串
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class ListRulesResponseBodyRulesRuleActionsRewriteConfig(TeaModel):
    def __init__(
        self,
        host: str = None,
        path: str = None,
        query: str = None,
    ):
        # 主机名
        self.host = host
        # 路径
        self.path = path
        # 查询
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.path is not None:
            result['Path'] = self.path
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class ListRulesResponseBodyRulesRuleActionsTrafficLimitConfig(TeaModel):
    def __init__(
        self,
        qps: int = None,
    ):
        self.qps = qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['QPS'] = self.qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        return self


class ListRulesResponseBodyRulesRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class ListRulesResponseBodyRulesRuleActionsTrafficMirrorConfigMirrorGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[ListRulesResponseBodyRulesRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples] = None,
    ):
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = ListRulesResponseBodyRulesRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class ListRulesResponseBodyRulesRuleActionsTrafficMirrorConfig(TeaModel):
    def __init__(
        self,
        mirror_group_config: ListRulesResponseBodyRulesRuleActionsTrafficMirrorConfigMirrorGroupConfig = None,
        target_type: str = None,
    ):
        # TargetType为服务器组时必选，目标服务器组
        self.mirror_group_config = mirror_group_config
        # 流量镜像的目的，可以是服务器组
        self.target_type = target_type

    def validate(self):
        if self.mirror_group_config:
            self.mirror_group_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mirror_group_config is not None:
            result['MirrorGroupConfig'] = self.mirror_group_config.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MirrorGroupConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleActionsTrafficMirrorConfigMirrorGroupConfig()
            self.mirror_group_config = temp_model.from_map(m['MirrorGroupConfig'])
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListRulesResponseBodyRulesRuleActions(TeaModel):
    def __init__(
        self,
        fixed_response_config: ListRulesResponseBodyRulesRuleActionsFixedResponseConfig = None,
        forward_group_config: ListRulesResponseBodyRulesRuleActionsForwardGroupConfig = None,
        insert_header_config: ListRulesResponseBodyRulesRuleActionsInsertHeaderConfig = None,
        order: int = None,
        redirect_config: ListRulesResponseBodyRulesRuleActionsRedirectConfig = None,
        rewrite_config: ListRulesResponseBodyRulesRuleActionsRewriteConfig = None,
        traffic_limit_config: ListRulesResponseBodyRulesRuleActionsTrafficLimitConfig = None,
        traffic_mirror_config: ListRulesResponseBodyRulesRuleActionsTrafficMirrorConfig = None,
        type: str = None,
    ):
        # 返回固定内容动作配置
        self.fixed_response_config = fixed_response_config
        # 转发组动作配置
        self.forward_group_config = forward_group_config
        # 插入头部动作配置
        self.insert_header_config = insert_header_config
        # 优先级
        self.order = order
        # 重定向动作配置
        self.redirect_config = redirect_config
        # 内部重定向动作配置
        self.rewrite_config = rewrite_config
        self.traffic_limit_config = traffic_limit_config
        # 流量镜像Action对应的配置，type为TrafficMirror时必填且有效
        self.traffic_mirror_config = traffic_mirror_config
        # 转发规则动作类型
        self.type = type

    def validate(self):
        if self.fixed_response_config:
            self.fixed_response_config.validate()
        if self.forward_group_config:
            self.forward_group_config.validate()
        if self.insert_header_config:
            self.insert_header_config.validate()
        if self.redirect_config:
            self.redirect_config.validate()
        if self.rewrite_config:
            self.rewrite_config.validate()
        if self.traffic_limit_config:
            self.traffic_limit_config.validate()
        if self.traffic_mirror_config:
            self.traffic_mirror_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fixed_response_config is not None:
            result['FixedResponseConfig'] = self.fixed_response_config.to_map()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.insert_header_config is not None:
            result['InsertHeaderConfig'] = self.insert_header_config.to_map()
        if self.order is not None:
            result['Order'] = self.order
        if self.redirect_config is not None:
            result['RedirectConfig'] = self.redirect_config.to_map()
        if self.rewrite_config is not None:
            result['RewriteConfig'] = self.rewrite_config.to_map()
        if self.traffic_limit_config is not None:
            result['TrafficLimitConfig'] = self.traffic_limit_config.to_map()
        if self.traffic_mirror_config is not None:
            result['TrafficMirrorConfig'] = self.traffic_mirror_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedResponseConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleActionsFixedResponseConfig()
            self.fixed_response_config = temp_model.from_map(m['FixedResponseConfig'])
        if m.get('ForwardGroupConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('InsertHeaderConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleActionsInsertHeaderConfig()
            self.insert_header_config = temp_model.from_map(m['InsertHeaderConfig'])
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RedirectConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleActionsRedirectConfig()
            self.redirect_config = temp_model.from_map(m['RedirectConfig'])
        if m.get('RewriteConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleActionsRewriteConfig()
            self.rewrite_config = temp_model.from_map(m['RewriteConfig'])
        if m.get('TrafficLimitConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleActionsTrafficLimitConfig()
            self.traffic_limit_config = temp_model.from_map(m['TrafficLimitConfig'])
        if m.get('TrafficMirrorConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleActionsTrafficMirrorConfig()
            self.traffic_mirror_config = temp_model.from_map(m['TrafficMirrorConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRulesResponseBodyRulesRuleConditionsCookieConfigValues(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Cookie条件键
        self.key = key
        # Cookie条件值
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


class ListRulesResponseBodyRulesRuleConditionsCookieConfig(TeaModel):
    def __init__(
        self,
        values: List[ListRulesResponseBodyRulesRuleConditionsCookieConfigValues] = None,
    ):
        # Cookie键值对列表
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = ListRulesResponseBodyRulesRuleConditionsCookieConfigValues()
                self.values.append(temp_model.from_map(k))
        return self


class ListRulesResponseBodyRulesRuleConditionsHeaderConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # HTTP标头键
        self.key = key
        # HTTP标头值列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListRulesResponseBodyRulesRuleConditionsHostConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 主机名列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListRulesResponseBodyRulesRuleConditionsMethodConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # HTTP请求方法列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListRulesResponseBodyRulesRuleConditionsPathConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 路径条件列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListRulesResponseBodyRulesRuleConditionsQueryStringConfigValues(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 查询字符串条件键
        self.key = key
        # 查询字符串条件值
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


class ListRulesResponseBodyRulesRuleConditionsQueryStringConfig(TeaModel):
    def __init__(
        self,
        values: List[ListRulesResponseBodyRulesRuleConditionsQueryStringConfigValues] = None,
    ):
        # 查询字符串条件键值对列表
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = ListRulesResponseBodyRulesRuleConditionsQueryStringConfigValues()
                self.values.append(temp_model.from_map(k))
        return self


class ListRulesResponseBodyRulesRuleConditions(TeaModel):
    def __init__(
        self,
        cookie_config: ListRulesResponseBodyRulesRuleConditionsCookieConfig = None,
        header_config: ListRulesResponseBodyRulesRuleConditionsHeaderConfig = None,
        host_config: ListRulesResponseBodyRulesRuleConditionsHostConfig = None,
        method_config: ListRulesResponseBodyRulesRuleConditionsMethodConfig = None,
        path_config: ListRulesResponseBodyRulesRuleConditionsPathConfig = None,
        query_string_config: ListRulesResponseBodyRulesRuleConditionsQueryStringConfig = None,
        type: str = None,
    ):
        # Cookie条件配置
        self.cookie_config = cookie_config
        # HTTP标头条件配置
        self.header_config = header_config
        # 主机名条件配置
        self.host_config = host_config
        # HTTP请求方法条件配置
        self.method_config = method_config
        # 路径条件配置
        self.path_config = path_config
        # 查询字符串条件配置
        self.query_string_config = query_string_config
        # 条件类型
        self.type = type

    def validate(self):
        if self.cookie_config:
            self.cookie_config.validate()
        if self.header_config:
            self.header_config.validate()
        if self.host_config:
            self.host_config.validate()
        if self.method_config:
            self.method_config.validate()
        if self.path_config:
            self.path_config.validate()
        if self.query_string_config:
            self.query_string_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie_config is not None:
            result['CookieConfig'] = self.cookie_config.to_map()
        if self.header_config is not None:
            result['HeaderConfig'] = self.header_config.to_map()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        if self.method_config is not None:
            result['MethodConfig'] = self.method_config.to_map()
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.query_string_config is not None:
            result['QueryStringConfig'] = self.query_string_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleConditionsCookieConfig()
            self.cookie_config = temp_model.from_map(m['CookieConfig'])
        if m.get('HeaderConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleConditionsHeaderConfig()
            self.header_config = temp_model.from_map(m['HeaderConfig'])
        if m.get('HostConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        if m.get('MethodConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleConditionsMethodConfig()
            self.method_config = temp_model.from_map(m['MethodConfig'])
        if m.get('PathConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('QueryStringConfig') is not None:
            temp_model = ListRulesResponseBodyRulesRuleConditionsQueryStringConfig()
            self.query_string_config = temp_model.from_map(m['QueryStringConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        listener_id: str = None,
        load_balancer_id: str = None,
        priority: int = None,
        rule_actions: List[ListRulesResponseBodyRulesRuleActions] = None,
        rule_conditions: List[ListRulesResponseBodyRulesRuleConditions] = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_status: str = None,
    ):
        # 监听ID
        self.listener_id = listener_id
        # 实例ID
        self.load_balancer_id = load_balancer_id
        # 转发规则优先级
        self.priority = priority
        # 转发规则动作
        self.rule_actions = rule_actions
        # 转发规则条件
        self.rule_conditions = rule_conditions
        # 转发规则标识
        self.rule_id = rule_id
        # 转发规则名称
        self.rule_name = rule_name
        # 转发规则状态
        self.rule_status = rule_status

    def validate(self):
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = ListRulesResponseBodyRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = ListRulesResponseBodyRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        rules: List[ListRulesResponseBodyRules] = None,
        total_count: int = None,
    ):
        # 本次请求所返回的最大记录条数。
        self.max_results = max_results
        # 用来表示当前调用返回读取到的位置，空代表数据已经读取完毕。
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 转发规则列表
        self.rules = rules
        # 本次请求条件下的数据总量。
        self.total_count = total_count

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRulesResponseBody = None,
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
            temp_model = ListRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecurityPoliciesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        security_policy_ids: List[str] = None,
        security_policy_names: List[str] = None,
    ):
        # 查询数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # 资源组ID
        self.resource_group_id = resource_group_id
        # 安全策略id
        self.security_policy_ids = security_policy_ids
        # 安全策略名称
        self.security_policy_names = security_policy_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_policy_ids is not None:
            result['SecurityPolicyIds'] = self.security_policy_ids
        if self.security_policy_names is not None:
            result['SecurityPolicyNames'] = self.security_policy_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityPolicyIds') is not None:
            self.security_policy_ids = m.get('SecurityPolicyIds')
        if m.get('SecurityPolicyNames') is not None:
            self.security_policy_names = m.get('SecurityPolicyNames')
        return self


class ListSecurityPoliciesResponseBodySecurityPolicies(TeaModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        resource_group_id: str = None,
        security_policy_id: str = None,
        security_policy_name: str = None,
        security_policy_status: str = None,
        tlsversions: List[str] = None,
    ):
        # 加密套件
        self.ciphers = ciphers
        # 资源组id
        self.resource_group_id = resource_group_id
        # 安全策略id
        self.security_policy_id = security_policy_id
        # 安全策略名称
        self.security_policy_name = security_policy_name
        # 状态
        self.security_policy_status = security_policy_status
        # TLS策略
        self.tlsversions = tlsversions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name
        if self.security_policy_status is not None:
            result['SecurityPolicyStatus'] = self.security_policy_status
        if self.tlsversions is not None:
            result['TLSVersions'] = self.tlsversions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')
        if m.get('SecurityPolicyStatus') is not None:
            self.security_policy_status = m.get('SecurityPolicyStatus')
        if m.get('TLSVersions') is not None:
            self.tlsversions = m.get('TLSVersions')
        return self


class ListSecurityPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        security_policies: List[ListSecurityPoliciesResponseBodySecurityPolicies] = None,
        total_count: int = None,
    ):
        # 本次查询返回记录数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 安全策略
        self.security_policies = security_policies
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.security_policies:
            for k in self.security_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityPolicies'] = []
        if self.security_policies is not None:
            for k in self.security_policies:
                result['SecurityPolicies'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_policies = []
        if m.get('SecurityPolicies') is not None:
            for k in m.get('SecurityPolicies'):
                temp_model = ListSecurityPoliciesResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSecurityPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSecurityPoliciesResponseBody = None,
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
            temp_model = ListSecurityPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecurityPolicyRelationsRequest(TeaModel):
    def __init__(
        self,
        security_policy_ids: List[str] = None,
    ):
        # 安全策略id
        self.security_policy_ids = security_policy_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_policy_ids is not None:
            result['SecurityPolicyIds'] = self.security_policy_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityPolicyIds') is not None:
            self.security_policy_ids = m.get('SecurityPolicyIds')
        return self


class ListSecurityPolicyRelationsResponseBodySecrityPolicyRelationsRelatedListeners(TeaModel):
    def __init__(
        self,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balancer_id: str = None,
    ):
        # 监听id
        self.listener_id = listener_id
        # 监听端口
        self.listener_port = listener_port
        # 监听协议
        self.listener_protocol = listener_protocol
        # 实例id
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class ListSecurityPolicyRelationsResponseBodySecrityPolicyRelations(TeaModel):
    def __init__(
        self,
        related_listeners: List[ListSecurityPolicyRelationsResponseBodySecrityPolicyRelationsRelatedListeners] = None,
        security_policy_id: str = None,
    ):
        # 关联的监听列表
        self.related_listeners = related_listeners
        # 安全策略id
        self.security_policy_id = security_policy_id

    def validate(self):
        if self.related_listeners:
            for k in self.related_listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RelatedListeners'] = []
        if self.related_listeners is not None:
            for k in self.related_listeners:
                result['RelatedListeners'].append(k.to_map() if k else None)
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.related_listeners = []
        if m.get('RelatedListeners') is not None:
            for k in m.get('RelatedListeners'):
                temp_model = ListSecurityPolicyRelationsResponseBodySecrityPolicyRelationsRelatedListeners()
                self.related_listeners.append(temp_model.from_map(k))
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        return self


class ListSecurityPolicyRelationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secrity_policy_relations: List[ListSecurityPolicyRelationsResponseBodySecrityPolicyRelations] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 安全策略关联关系
        self.secrity_policy_relations = secrity_policy_relations

    def validate(self):
        if self.secrity_policy_relations:
            for k in self.secrity_policy_relations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecrityPolicyRelations'] = []
        if self.secrity_policy_relations is not None:
            for k in self.secrity_policy_relations:
                result['SecrityPolicyRelations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.secrity_policy_relations = []
        if m.get('SecrityPolicyRelations') is not None:
            for k in m.get('SecrityPolicyRelations'):
                temp_model = ListSecurityPolicyRelationsResponseBodySecrityPolicyRelations()
                self.secrity_policy_relations.append(temp_model.from_map(k))
        return self


class ListSecurityPolicyRelationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSecurityPolicyRelationsResponseBody = None,
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
            temp_model = ListSecurityPolicyRelationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServerGroupServersRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 标签键
        self.key = key
        # 标签值
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


class ListServerGroupServersRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        server_group_id: str = None,
        server_ids: List[str] = None,
        tag: List[ListServerGroupServersRequestTag] = None,
    ):
        # 查询数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # 服务器组id
        self.server_group_id = server_group_id
        self.server_ids = server_ids
        self.tag = tag

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.server_ids is not None:
            result['ServerIds'] = self.server_ids
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('ServerIds') is not None:
            self.server_ids = m.get('ServerIds')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListServerGroupServersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListServerGroupServersResponseBodyServers(TeaModel):
    def __init__(
        self,
        description: str = None,
        port: int = None,
        server_group_id: str = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        status: str = None,
        weight: int = None,
    ):
        # 描述信息
        self.description = description
        # 端口
        self.port = port
        # 服务器组id
        self.server_group_id = server_group_id
        # 服务器id
        self.server_id = server_id
        # 服务器ip
        self.server_ip = server_ip
        # 后端服务器类型
        self.server_type = server_type
        # 状态
        self.status = status
        # 权重
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.status is not None:
            result['Status'] = self.status
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ListServerGroupServersResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        servers: List[ListServerGroupServersResponseBodyServers] = None,
        total_count: int = None,
    ):
        # 本次查询返回记录数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 后端服务器
        self.servers = servers
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = ListServerGroupServersResponseBodyServers()
                self.servers.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServerGroupServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServerGroupServersResponseBody = None,
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
            temp_model = ListServerGroupServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServerGroupsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 标签键
        self.key = key
        # 标签值
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


class ListServerGroupsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        server_group_ids: List[str] = None,
        server_group_names: List[str] = None,
        tag: List[ListServerGroupsRequestTag] = None,
        vpc_id: str = None,
    ):
        # 查询数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # 资源组ID
        self.resource_group_id = resource_group_id
        # 服务器组Id列表
        self.server_group_ids = server_group_ids
        # 服务器组名称
        self.server_group_names = server_group_names
        # Tag列表
        self.tag = tag
        # VpcId
        self.vpc_id = vpc_id

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.server_group_ids is not None:
            result['ServerGroupIds'] = self.server_group_ids
        if self.server_group_names is not None:
            result['ServerGroupNames'] = self.server_group_names
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServerGroupIds') is not None:
            self.server_group_ids = m.get('ServerGroupIds')
        if m.get('ServerGroupNames') is not None:
            self.server_group_names = m.get('ServerGroupNames')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListServerGroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListServerGroupsResponseBodyServerGroupsHealthCheckConfig(TeaModel):
    def __init__(
        self,
        health_check_codes: List[str] = None,
        health_check_connect_port: int = None,
        health_check_enabled: bool = None,
        health_check_host: str = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_path: str = None,
        health_check_protocol: str = None,
        health_check_timeout: int = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
    ):
        # 状态码
        self.health_check_codes = health_check_codes
        # 端口
        self.health_check_connect_port = health_check_connect_port
        # 是否启用健康检查
        self.health_check_enabled = health_check_enabled
        # 域名
        self.health_check_host = health_check_host
        # 版本
        self.health_check_http_version = health_check_http_version
        # 间隔时间
        self.health_check_interval = health_check_interval
        # 方法
        self.health_check_method = health_check_method
        # uri
        self.health_check_path = health_check_path
        # 协议
        self.health_check_protocol = health_check_protocol
        # 超时时间
        self.health_check_timeout = health_check_timeout
        # 健康阈值
        self.healthy_threshold = healthy_threshold
        # 不健康阈值
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_codes is not None:
            result['HealthCheckCodes'] = self.health_check_codes
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_host is not None:
            result['HealthCheckHost'] = self.health_check_host
        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckCodes') is not None:
            self.health_check_codes = m.get('HealthCheckCodes')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckHost') is not None:
            self.health_check_host = m.get('HealthCheckHost')
        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class ListServerGroupsResponseBodyServerGroupsStickySessionConfig(TeaModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        sticky_session_enabled: bool = None,
        sticky_session_type: str = None,
    ):
        # Cookie
        self.cookie = cookie
        # Cookie超时时间
        self.cookie_timeout = cookie_timeout
        # 是否开启会话保持
        self.sticky_session_enabled = sticky_session_enabled
        # 会话保持类型
        self.sticky_session_type = sticky_session_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.sticky_session_enabled is not None:
            result['StickySessionEnabled'] = self.sticky_session_enabled
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('StickySessionEnabled') is not None:
            self.sticky_session_enabled = m.get('StickySessionEnabled')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        return self


class ListServerGroupsResponseBodyServerGroupsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 标签键
        self.key = key
        # 标签值
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


class ListServerGroupsResponseBodyServerGroups(TeaModel):
    def __init__(
        self,
        config_managed_enabled: bool = None,
        health_check_config: ListServerGroupsResponseBodyServerGroupsHealthCheckConfig = None,
        ipv_6enabled: bool = None,
        protocol: str = None,
        resource_group_id: str = None,
        scheduler: str = None,
        server_count: int = None,
        server_group_id: str = None,
        server_group_name: str = None,
        server_group_status: str = None,
        server_group_type: str = None,
        service_name: str = None,
        sticky_session_config: ListServerGroupsResponseBodyServerGroupsStickySessionConfig = None,
        tags: List[ListServerGroupsResponseBodyServerGroupsTags] = None,
        upstream_keepalive_enabled: bool = None,
        vpc_id: str = None,
    ):
        # 是否开启配置管理
        self.config_managed_enabled = config_managed_enabled
        # 健康检查配置
        self.health_check_config = health_check_config
        # 是否支持Ipv6
        self.ipv_6enabled = ipv_6enabled
        # 服务器组协议
        self.protocol = protocol
        # 资源组id
        self.resource_group_id = resource_group_id
        # 调度策略
        self.scheduler = scheduler
        # 服务器组内服务器数量
        self.server_count = server_count
        # 服务器组Id
        self.server_group_id = server_group_id
        # 服务器组名称
        self.server_group_name = server_group_name
        # 服务器组状态
        self.server_group_status = server_group_status
        # 服务器组类型
        self.server_group_type = server_group_type
        # 服务器名称
        self.service_name = service_name
        # 会话保持配置
        self.sticky_session_config = sticky_session_config
        # 标签列表
        self.tags = tags
        # 是否开启后端长链接
        self.upstream_keepalive_enabled = upstream_keepalive_enabled
        # 服务器组所在VpcId
        self.vpc_id = vpc_id

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()
        if self.sticky_session_config:
            self.sticky_session_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_managed_enabled is not None:
            result['ConfigManagedEnabled'] = self.config_managed_enabled
        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()
        if self.ipv_6enabled is not None:
            result['Ipv6Enabled'] = self.ipv_6enabled
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_count is not None:
            result['ServerCount'] = self.server_count
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name
        if self.server_group_status is not None:
            result['ServerGroupStatus'] = self.server_group_status
        if self.server_group_type is not None:
            result['ServerGroupType'] = self.server_group_type
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.sticky_session_config is not None:
            result['StickySessionConfig'] = self.sticky_session_config.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.upstream_keepalive_enabled is not None:
            result['UpstreamKeepaliveEnabled'] = self.upstream_keepalive_enabled
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigManagedEnabled') is not None:
            self.config_managed_enabled = m.get('ConfigManagedEnabled')
        if m.get('HealthCheckConfig') is not None:
            temp_model = ListServerGroupsResponseBodyServerGroupsHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m['HealthCheckConfig'])
        if m.get('Ipv6Enabled') is not None:
            self.ipv_6enabled = m.get('Ipv6Enabled')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerCount') is not None:
            self.server_count = m.get('ServerCount')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')
        if m.get('ServerGroupStatus') is not None:
            self.server_group_status = m.get('ServerGroupStatus')
        if m.get('ServerGroupType') is not None:
            self.server_group_type = m.get('ServerGroupType')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StickySessionConfig') is not None:
            temp_model = ListServerGroupsResponseBodyServerGroupsStickySessionConfig()
            self.sticky_session_config = temp_model.from_map(m['StickySessionConfig'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListServerGroupsResponseBodyServerGroupsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpstreamKeepaliveEnabled') is not None:
            self.upstream_keepalive_enabled = m.get('UpstreamKeepaliveEnabled')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListServerGroupsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        server_groups: List[ListServerGroupsResponseBodyServerGroups] = None,
        total_count: int = None,
    ):
        # 本次查询返回记录数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 服务器组
        self.server_groups = server_groups
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.server_groups:
            for k in self.server_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServerGroups'] = []
        if self.server_groups is not None:
            for k in self.server_groups:
                result['ServerGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.server_groups = []
        if m.get('ServerGroups') is not None:
            for k in m.get('ServerGroups'):
                temp_model = ListServerGroupsResponseBodyServerGroups()
                self.server_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServerGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServerGroupsResponseBody = None,
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
            temp_model = ListServerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSystemSecurityPoliciesResponseBodySecurityPolicies(TeaModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        security_policy_id: str = None,
        tlsversions: List[str] = None,
    ):
        # 加密套件
        self.ciphers = ciphers
        # 安全策略Id
        self.security_policy_id = security_policy_id
        # 协议版本
        self.tlsversions = tlsversions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.tlsversions is not None:
            result['TLSVersions'] = self.tlsversions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('TLSVersions') is not None:
            self.tlsversions = m.get('TLSVersions')
        return self


class ListSystemSecurityPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_policies: List[ListSystemSecurityPoliciesResponseBodySecurityPolicies] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 安全策略
        self.security_policies = security_policies

    def validate(self):
        if self.security_policies:
            for k in self.security_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityPolicies'] = []
        if self.security_policies is not None:
            for k in self.security_policies:
                result['SecurityPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_policies = []
        if m.get('SecurityPolicies') is not None:
            for k in m.get('SecurityPolicies'):
                temp_model = ListSystemSecurityPoliciesResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k))
        return self


class ListSystemSecurityPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSystemSecurityPoliciesResponseBody = None,
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
            temp_model = ListSystemSecurityPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_type: str = None,
    ):
        # 标签类型
        self.category = category
        # 具体的标签Key
        self.keyword = keyword
        # 查询数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # 资源类型
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(
        self,
        category: str = None,
        tag_key: str = None,
    ):
        # 标签类型
        self.category = category
        # 标签Key
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        tag_keys: List[ListTagKeysResponseBodyTagKeys] = None,
        total_count: int = None,
    ):
        # 本次查询返回记录数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 标签Key列表
        self.tag_keys = tag_keys
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagKeysResponseBody = None,
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 标签键
        self.key = key
        # 标签值
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # 查询数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # 资源实例Id
        self.resource_id = resource_id
        # 资源类型
        self.resource_type = resource_type
        # 标签列表
        self.tag = tag

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # 资源ID
        self.resource_id = resource_id
        # 资源类型
        self.resource_type = resource_type
        # 标签Key
        self.tag_key = tag_key
        # 标签Value
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
        total_count: int = None,
    ):
        # 本次查询返回记录数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 标签值列表
        self.tag_resources = tag_resources
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
    ):
        # 查询数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # 资源实例Id
        self.resource_id = resource_id
        # 资源类型
        self.resource_type = resource_type
        # 具体的标签Key
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        tag_values: List[str] = None,
        total_count: int = None,
    ):
        # 本次查询返回记录数量
        self.max_results = max_results
        # 分页查询标识
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 标签值列表
        self.tag_values = tag_values
        # 总记录数
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagValuesResponseBody = None,
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
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # 资源组id
        self.new_resource_group_id = new_resource_group_id
        # 指定资源Id
        self.resource_id = resource_id
        # 资源类型
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class MoveResourceGroupResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveResourceGroupResponseBody = None,
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveEntriesFromAclRequest(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        entries: List[str] = None,
    ):
        # 访问控制策略Id
        self.acl_id = acl_id
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 条目列表
        self.entries = entries

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.entries is not None:
            result['Entries'] = self.entries
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Entries') is not None:
            self.entries = m.get('Entries')
        return self


class RemoveEntriesFromAclResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveEntriesFromAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveEntriesFromAclResponseBody = None,
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
            temp_model = RemoveEntriesFromAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveServersFromServerGroupRequestServers(TeaModel):
    def __init__(
        self,
        port: int = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
    ):
        # 后端端口号
        self.port = port
        # 后端服务器id
        self.server_id = server_id
        # 后端服务器ip
        self.server_ip = server_ip
        # 后端服务器类型
        self.server_type = server_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        return self


class RemoveServersFromServerGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        server_group_id: str = None,
        servers: List[RemoveServersFromServerGroupRequestServers] = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 后端服务器Id
        self.server_group_id = server_group_id
        # 后端服务器
        self.servers = servers

    def validate(self):
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = RemoveServersFromServerGroupRequestServers()
                self.servers.append(temp_model.from_map(k))
        return self


class RemoveServersFromServerGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveServersFromServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveServersFromServerGroupResponseBody = None,
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
            temp_model = RemoveServersFromServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceServersInServerGroupRequestAddedServers(TeaModel):
    def __init__(
        self,
        description: str = None,
        port: int = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        weight: int = None,
    ):
        # 描述信息
        self.description = description
        # 后端端口号
        self.port = port
        # 后端服务器id
        self.server_id = server_id
        # 后端服务器ip
        self.server_ip = server_ip
        # 后端服务器类型
        self.server_type = server_type
        # 后端服务器权重
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ReplaceServersInServerGroupRequestRemovedServers(TeaModel):
    def __init__(
        self,
        port: int = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
    ):
        # 端口
        self.port = port
        # 后端服务器id
        self.server_id = server_id
        # 后端服务器ip
        self.server_ip = server_ip
        # 后端服务器类型
        self.server_type = server_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        return self


class ReplaceServersInServerGroupRequest(TeaModel):
    def __init__(
        self,
        added_servers: List[ReplaceServersInServerGroupRequestAddedServers] = None,
        client_token: str = None,
        dry_run: bool = None,
        removed_servers: List[ReplaceServersInServerGroupRequestRemovedServers] = None,
        server_group_id: str = None,
    ):
        # 待添加后端服务器
        self.added_servers = added_servers
        # 幂等Token
        self.client_token = client_token
        # dryRun
        self.dry_run = dry_run
        # 待删除后端服务器
        self.removed_servers = removed_servers
        # 后端服务器Id
        self.server_group_id = server_group_id

    def validate(self):
        if self.added_servers:
            for k in self.added_servers:
                if k:
                    k.validate()
        if self.removed_servers:
            for k in self.removed_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AddedServers'] = []
        if self.added_servers is not None:
            for k in self.added_servers:
                result['AddedServers'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['RemovedServers'] = []
        if self.removed_servers is not None:
            for k in self.removed_servers:
                result['RemovedServers'].append(k.to_map() if k else None)
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.added_servers = []
        if m.get('AddedServers') is not None:
            for k in m.get('AddedServers'):
                temp_model = ReplaceServersInServerGroupRequestAddedServers()
                self.added_servers.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.removed_servers = []
        if m.get('RemovedServers') is not None:
            for k in m.get('RemovedServers'):
                temp_model = ReplaceServersInServerGroupRequestRemovedServers()
                self.removed_servers.append(temp_model.from_map(k))
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class ReplaceServersInServerGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReplaceServersInServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReplaceServersInServerGroupResponseBody = None,
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
            temp_model = ReplaceServersInServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartListenerRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 监听id
        self.listener_id = listener_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class StartListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartListenerResponseBody = None,
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
            temp_model = StartListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopListenerRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 监听id
        self.listener_id = listener_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class StopListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopListenerResponseBody = None,
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
            temp_model = StopListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 标签键
        self.key = key
        # 标签值
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # 资源实例Id
        self.resource_id = resource_id
        # 资源类型
        self.resource_type = resource_type
        # 标签列表
        self.tag = tag

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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 标签键
        self.key = key
        # 标签值
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


class UnTagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[UnTagResourcesRequestTag] = None,
        tag_key: List[str] = None,
    ):
        # 资源实例Id
        self.resource_id = resource_id
        # 资源类型
        self.resource_type = resource_type
        # 标签列表
        self.tag = tag
        # 标签键列表
        self.tag_key = tag_key

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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = UnTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UnTagResourcesResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnTagResourcesResponseBody = None,
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
            temp_model = UnTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAclAttributeRequest(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_name: str = None,
        client_token: str = None,
        dry_run: bool = None,
    ):
        # AclId
        self.acl_id = acl_id
        # 访问控制策略名称
        self.acl_name = acl_name
        # 幂等参数
        self.client_token = client_token
        # 是否预校验请求
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class UpdateAclAttributeResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAclAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAclAttributeResponseBody = None,
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
            temp_model = UpdateAclAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHealthCheckTemplateAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        health_check_codes: List[str] = None,
        health_check_connect_port: int = None,
        health_check_host: str = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_path: str = None,
        health_check_protocol: str = None,
        health_check_template_id: str = None,
        health_check_template_name: str = None,
        health_check_timeout: int = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
    ):
        # 幂等参数
        self.client_token = client_token
        # dryRun
        self.dry_run = dry_run
        # 状态码
        self.health_check_codes = health_check_codes
        # 端口号
        self.health_check_connect_port = health_check_connect_port
        # 域名
        self.health_check_host = health_check_host
        # 版本
        self.health_check_http_version = health_check_http_version
        # 时间间隔
        self.health_check_interval = health_check_interval
        # 方法
        self.health_check_method = health_check_method
        # uri
        self.health_check_path = health_check_path
        # 协议
        self.health_check_protocol = health_check_protocol
        # 健康检查模板ID
        self.health_check_template_id = health_check_template_id
        # 名称
        self.health_check_template_name = health_check_template_name
        # 超时时间
        self.health_check_timeout = health_check_timeout
        # 健康阈值
        self.healthy_threshold = healthy_threshold
        # 不健康阈值
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.health_check_codes is not None:
            result['HealthCheckCodes'] = self.health_check_codes
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_host is not None:
            result['HealthCheckHost'] = self.health_check_host
        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.health_check_template_id is not None:
            result['HealthCheckTemplateId'] = self.health_check_template_id
        if self.health_check_template_name is not None:
            result['HealthCheckTemplateName'] = self.health_check_template_name
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('HealthCheckCodes') is not None:
            self.health_check_codes = m.get('HealthCheckCodes')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckHost') is not None:
            self.health_check_host = m.get('HealthCheckHost')
        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('HealthCheckTemplateId') is not None:
            self.health_check_template_id = m.get('HealthCheckTemplateId')
        if m.get('HealthCheckTemplateName') is not None:
            self.health_check_template_name = m.get('HealthCheckTemplateName')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class UpdateHealthCheckTemplateAttributeResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateHealthCheckTemplateAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateHealthCheckTemplateAttributeResponseBody = None,
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
            temp_model = UpdateHealthCheckTemplateAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateListenerAttributeRequestCaCertificates(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateListenerAttributeRequestCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # 正式标识
        self.certificate_id = certificate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class UpdateListenerAttributeRequestDefaultActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        # 服务器组ID
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class UpdateListenerAttributeRequestDefaultActionsForwardGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[UpdateListenerAttributeRequestDefaultActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # 服务器组列表
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = UpdateListenerAttributeRequestDefaultActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class UpdateListenerAttributeRequestDefaultActions(TeaModel):
    def __init__(
        self,
        forward_group_config: UpdateListenerAttributeRequestDefaultActionsForwardGroupConfig = None,
        type: str = None,
    ):
        # 转发组
        self.forward_group_config = forward_group_config
        # 动作类型
        self.type = type

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = UpdateListenerAttributeRequestDefaultActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateListenerAttributeRequestQuicConfig(TeaModel):
    def __init__(
        self,
        quic_listener_id: str = None,
        quic_upgrade_enabled: bool = None,
    ):
        # 需要关联的QUIC监听ID，HTTPS监听时有效，QuicUpgradeEnabled为true时必选
        self.quic_listener_id = quic_listener_id
        # 是否开启quic升级，HTTPS监听时有效
        self.quic_upgrade_enabled = quic_upgrade_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quic_listener_id is not None:
            result['QuicListenerId'] = self.quic_listener_id
        if self.quic_upgrade_enabled is not None:
            result['QuicUpgradeEnabled'] = self.quic_upgrade_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuicListenerId') is not None:
            self.quic_listener_id = m.get('QuicListenerId')
        if m.get('QuicUpgradeEnabled') is not None:
            self.quic_upgrade_enabled = m.get('QuicUpgradeEnabled')
        return self


class UpdateListenerAttributeRequestXForwardedForConfig(TeaModel):
    def __init__(
        self,
        xforwarded_for_client_cert_client_verify_alias: str = None,
        xforwarded_for_client_cert_client_verify_enabled: bool = None,
        xforwarded_for_client_cert_fingerprint_alias: str = None,
        xforwarded_for_client_cert_fingerprint_enabled: bool = None,
        xforwarded_for_client_cert_issuer_dnalias: str = None,
        xforwarded_for_client_cert_issuer_dnenabled: bool = None,
        xforwarded_for_client_cert_subject_dnalias: str = None,
        xforwarded_for_client_cert_subject_dnenabled: bool = None,
        xforwarded_for_client_src_port_enabled: bool = None,
        xforwarded_for_enabled: bool = None,
        xforwarded_for_proto_enabled: bool = None,
        xforwarded_for_slbid_enabled: bool = None,
        xforwarded_for_slbport_enabled: bool = None,
    ):
        # 自定义HEADER头名称，只有当XForwardedForClientCertClientVerifyEnabled的值为true的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_client_verify_alias = xforwarded_for_client_cert_client_verify_alias
        # 是否通过X-Forwarded-Clientcert-clientverify  头字段获取对访问负载均衡实例客户端证书的校验结果。HTTPS监听有效。
        self.xforwarded_for_client_cert_client_verify_enabled = xforwarded_for_client_cert_client_verify_enabled
        # 自定义HEADER头名称，只有当XForwardedForClientCertFingerprintEnabled的值为true的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_fingerprint_alias = xforwarded_for_client_cert_fingerprint_alias
        # 是否通过X-Forwarded-Clientcert-fingerprint 头字段获取访问负载均衡实例客户端证书的指纹取值，HTTPS监听有效。
        self.xforwarded_for_client_cert_fingerprint_enabled = xforwarded_for_client_cert_fingerprint_enabled
        # 自定义HEADER头名称，只有当XForwardedForClientCertIssuerDNEnabled的值为‘On’的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_issuer_dnalias = xforwarded_for_client_cert_issuer_dnalias
        # 是否通过 X-Forwarded-Clientcert-issuerdn 头字段获取访问负载均衡实例客户端证书的发行者信息。HTTPS监听有效。
        self.xforwarded_for_client_cert_issuer_dnenabled = xforwarded_for_client_cert_issuer_dnenabled
        # 自定义HEADER头名称，只有当XForwardedForClientCertSubjectDNEnabled的值为true的时候，此值才会生效；否则该值不会生效。HTTPS监听有效
        self.xforwarded_for_client_cert_subject_dnalias = xforwarded_for_client_cert_subject_dnalias
        # 是否通过X-Forwarded-Clientcert-subjectdn  头字段获取访问负载均衡实例客户端证书的所有者信息。HTTPS监听有效。
        self.xforwarded_for_client_cert_subject_dnenabled = xforwarded_for_client_cert_subject_dnenabled
        # 是否通过X-Forwarded-Client-Port 头字段获取访问负载均衡实例客户端的端口。HTTPS监听有效。
        self.xforwarded_for_client_src_port_enabled = xforwarded_for_client_src_port_enabled
        # 是否开启通过X-Forwarded-For头字段获取来访者真实 IP
        self.xforwarded_for_enabled = xforwarded_for_enabled
        # 是否通过X-Forwarded-Proto头字段获取负载均衡实例的监听协议。
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        # 是否通过SLB-ID头字段获取负载均衡实例ID。
        self.xforwarded_for_slbid_enabled = xforwarded_for_slbid_enabled
        # 是否通过X-Forwarded-Port 头字段获取负载均衡实例的监听端口。HTTPS监听有效。
        self.xforwarded_for_slbport_enabled = xforwarded_for_slbport_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.xforwarded_for_client_cert_client_verify_alias is not None:
            result['XForwardedForClientCertClientVerifyAlias'] = self.xforwarded_for_client_cert_client_verify_alias
        if self.xforwarded_for_client_cert_client_verify_enabled is not None:
            result['XForwardedForClientCertClientVerifyEnabled'] = self.xforwarded_for_client_cert_client_verify_enabled
        if self.xforwarded_for_client_cert_fingerprint_alias is not None:
            result['XForwardedForClientCertFingerprintAlias'] = self.xforwarded_for_client_cert_fingerprint_alias
        if self.xforwarded_for_client_cert_fingerprint_enabled is not None:
            result['XForwardedForClientCertFingerprintEnabled'] = self.xforwarded_for_client_cert_fingerprint_enabled
        if self.xforwarded_for_client_cert_issuer_dnalias is not None:
            result['XForwardedForClientCertIssuerDNAlias'] = self.xforwarded_for_client_cert_issuer_dnalias
        if self.xforwarded_for_client_cert_issuer_dnenabled is not None:
            result['XForwardedForClientCertIssuerDNEnabled'] = self.xforwarded_for_client_cert_issuer_dnenabled
        if self.xforwarded_for_client_cert_subject_dnalias is not None:
            result['XForwardedForClientCertSubjectDNAlias'] = self.xforwarded_for_client_cert_subject_dnalias
        if self.xforwarded_for_client_cert_subject_dnenabled is not None:
            result['XForwardedForClientCertSubjectDNEnabled'] = self.xforwarded_for_client_cert_subject_dnenabled
        if self.xforwarded_for_client_src_port_enabled is not None:
            result['XForwardedForClientSrcPortEnabled'] = self.xforwarded_for_client_src_port_enabled
        if self.xforwarded_for_enabled is not None:
            result['XForwardedForEnabled'] = self.xforwarded_for_enabled
        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled
        if self.xforwarded_for_slbid_enabled is not None:
            result['XForwardedForSLBIdEnabled'] = self.xforwarded_for_slbid_enabled
        if self.xforwarded_for_slbport_enabled is not None:
            result['XForwardedForSLBPortEnabled'] = self.xforwarded_for_slbport_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('XForwardedForClientCertClientVerifyAlias') is not None:
            self.xforwarded_for_client_cert_client_verify_alias = m.get('XForwardedForClientCertClientVerifyAlias')
        if m.get('XForwardedForClientCertClientVerifyEnabled') is not None:
            self.xforwarded_for_client_cert_client_verify_enabled = m.get('XForwardedForClientCertClientVerifyEnabled')
        if m.get('XForwardedForClientCertFingerprintAlias') is not None:
            self.xforwarded_for_client_cert_fingerprint_alias = m.get('XForwardedForClientCertFingerprintAlias')
        if m.get('XForwardedForClientCertFingerprintEnabled') is not None:
            self.xforwarded_for_client_cert_fingerprint_enabled = m.get('XForwardedForClientCertFingerprintEnabled')
        if m.get('XForwardedForClientCertIssuerDNAlias') is not None:
            self.xforwarded_for_client_cert_issuer_dnalias = m.get('XForwardedForClientCertIssuerDNAlias')
        if m.get('XForwardedForClientCertIssuerDNEnabled') is not None:
            self.xforwarded_for_client_cert_issuer_dnenabled = m.get('XForwardedForClientCertIssuerDNEnabled')
        if m.get('XForwardedForClientCertSubjectDNAlias') is not None:
            self.xforwarded_for_client_cert_subject_dnalias = m.get('XForwardedForClientCertSubjectDNAlias')
        if m.get('XForwardedForClientCertSubjectDNEnabled') is not None:
            self.xforwarded_for_client_cert_subject_dnenabled = m.get('XForwardedForClientCertSubjectDNEnabled')
        if m.get('XForwardedForClientSrcPortEnabled') is not None:
            self.xforwarded_for_client_src_port_enabled = m.get('XForwardedForClientSrcPortEnabled')
        if m.get('XForwardedForEnabled') is not None:
            self.xforwarded_for_enabled = m.get('XForwardedForEnabled')
        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')
        if m.get('XForwardedForSLBIdEnabled') is not None:
            self.xforwarded_for_slbid_enabled = m.get('XForwardedForSLBIdEnabled')
        if m.get('XForwardedForSLBPortEnabled') is not None:
            self.xforwarded_for_slbport_enabled = m.get('XForwardedForSLBPortEnabled')
        return self


class UpdateListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        ca_certificates: List[UpdateListenerAttributeRequestCaCertificates] = None,
        ca_enabled: bool = None,
        certificates: List[UpdateListenerAttributeRequestCertificates] = None,
        client_token: str = None,
        default_actions: List[UpdateListenerAttributeRequestDefaultActions] = None,
        dry_run: bool = None,
        gzip_enabled: bool = None,
        http_2enabled: bool = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_id: str = None,
        quic_config: UpdateListenerAttributeRequestQuicConfig = None,
        request_timeout: int = None,
        security_policy_id: str = None,
        xforwarded_for_config: UpdateListenerAttributeRequestXForwardedForConfig = None,
    ):
        # 监听默认CA证书列表，N当前取值范围为1
        self.ca_certificates = ca_certificates
        # 是否开启双向认证
        self.ca_enabled = ca_enabled
        # 监听默认服务器证书列表，N当前取值范围为1
        self.certificates = certificates
        # 幂等标识
        self.client_token = client_token
        # 监听默认动作
        self.default_actions = default_actions
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 是否开启Gzip压缩
        self.gzip_enabled = gzip_enabled
        # 是否开启HTTP/2特性
        self.http_2enabled = http_2enabled
        # 连接空闲超时时间
        self.idle_timeout = idle_timeout
        # 监听描述
        self.listener_description = listener_description
        # 监听标识
        self.listener_id = listener_id
        # HTTPS启用QUIC时相关属性
        self.quic_config = quic_config
        # 请求超时时间
        self.request_timeout = request_timeout
        # 安全策略
        self.security_policy_id = security_policy_id
        # XForward字段相关的配置
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
        if self.ca_certificates:
            for k in self.ca_certificates:
                if k:
                    k.validate()
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.default_actions:
            for k in self.default_actions:
                if k:
                    k.validate()
        if self.quic_config:
            self.quic_config.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CaCertificates'] = []
        if self.ca_certificates is not None:
            for k in self.ca_certificates:
                result['CaCertificates'].append(k.to_map() if k else None)
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['DefaultActions'] = []
        if self.default_actions is not None:
            for k in self.default_actions:
                result['DefaultActions'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.gzip_enabled is not None:
            result['GzipEnabled'] = self.gzip_enabled
        if self.http_2enabled is not None:
            result['Http2Enabled'] = self.http_2enabled
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.quic_config is not None:
            result['QuicConfig'] = self.quic_config.to_map()
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ca_certificates = []
        if m.get('CaCertificates') is not None:
            for k in m.get('CaCertificates'):
                temp_model = UpdateListenerAttributeRequestCaCertificates()
                self.ca_certificates.append(temp_model.from_map(k))
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = UpdateListenerAttributeRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.default_actions = []
        if m.get('DefaultActions') is not None:
            for k in m.get('DefaultActions'):
                temp_model = UpdateListenerAttributeRequestDefaultActions()
                self.default_actions.append(temp_model.from_map(k))
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('GzipEnabled') is not None:
            self.gzip_enabled = m.get('GzipEnabled')
        if m.get('Http2Enabled') is not None:
            self.http_2enabled = m.get('Http2Enabled')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('QuicConfig') is not None:
            temp_model = UpdateListenerAttributeRequestQuicConfig()
            self.quic_config = temp_model.from_map(m['QuicConfig'])
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('XForwardedForConfig') is not None:
            temp_model = UpdateListenerAttributeRequestXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m['XForwardedForConfig'])
        return self


class UpdateListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateListenerAttributeResponseBody = None,
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
            temp_model = UpdateListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateListenerLogConfigRequestAccessLogTracingConfig(TeaModel):
    def __init__(
        self,
        tracing_enabled: bool = None,
        tracing_sample: int = None,
        tracing_type: str = None,
    ):
        # Xtrace功能状态
        self.tracing_enabled = tracing_enabled
        # xtrace的采样率
        self.tracing_sample = tracing_sample
        # xtrace的类型
        self.tracing_type = tracing_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tracing_enabled is not None:
            result['TracingEnabled'] = self.tracing_enabled
        if self.tracing_sample is not None:
            result['TracingSample'] = self.tracing_sample
        if self.tracing_type is not None:
            result['TracingType'] = self.tracing_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TracingEnabled') is not None:
            self.tracing_enabled = m.get('TracingEnabled')
        if m.get('TracingSample') is not None:
            self.tracing_sample = m.get('TracingSample')
        if m.get('TracingType') is not None:
            self.tracing_type = m.get('TracingType')
        return self


class UpdateListenerLogConfigRequest(TeaModel):
    def __init__(
        self,
        access_log_record_customized_headers_enabled: bool = None,
        access_log_tracing_config: UpdateListenerLogConfigRequestAccessLogTracingConfig = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
    ):
        # 是否开启携带自定义Header
        self.access_log_record_customized_headers_enabled = access_log_record_customized_headers_enabled
        # 访问日志xtrace字段相关的配置
        self.access_log_tracing_config = access_log_tracing_config
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 监听标识
        self.listener_id = listener_id

    def validate(self):
        if self.access_log_tracing_config:
            self.access_log_tracing_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_record_customized_headers_enabled is not None:
            result['AccessLogRecordCustomizedHeadersEnabled'] = self.access_log_record_customized_headers_enabled
        if self.access_log_tracing_config is not None:
            result['AccessLogTracingConfig'] = self.access_log_tracing_config.to_map()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogRecordCustomizedHeadersEnabled') is not None:
            self.access_log_record_customized_headers_enabled = m.get('AccessLogRecordCustomizedHeadersEnabled')
        if m.get('AccessLogTracingConfig') is not None:
            temp_model = UpdateListenerLogConfigRequestAccessLogTracingConfig()
            self.access_log_tracing_config = temp_model.from_map(m['AccessLogTracingConfig'])
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class UpdateListenerLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateListenerLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateListenerLogConfigResponseBody = None,
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
            temp_model = UpdateListenerLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoadBalancerAddressTypeConfigRequestZoneMappings(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # 弹性公网IP
        self.allocation_id = allocation_id
        # 交换机标识
        self.v_switch_id = v_switch_id
        # 可用区
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateLoadBalancerAddressTypeConfigRequest(TeaModel):
    def __init__(
        self,
        address_type: str = None,
        client_token: str = None,
        dry_run: str = None,
        load_balancer_id: str = None,
        zone_mappings: List[UpdateLoadBalancerAddressTypeConfigRequestZoneMappings] = None,
    ):
        # 目标网络类型
        self.address_type = address_type
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 实例id
        self.load_balancer_id = load_balancer_id
        # 可用区及交换机映射列表
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = UpdateLoadBalancerAddressTypeConfigRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class UpdateLoadBalancerAddressTypeConfigResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoadBalancerAddressTypeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLoadBalancerAddressTypeConfigResponseBody = None,
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
            temp_model = UpdateLoadBalancerAddressTypeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoadBalancerAttributeRequestModificationProtectionConfig(TeaModel):
    def __init__(
        self,
        reason: str = None,
        status: str = None,
    ):
        # 设置修改保护状态的原因
        self.reason = reason
        # 负载均衡修改保护状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateLoadBalancerAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        modification_protection_config: UpdateLoadBalancerAttributeRequestModificationProtectionConfig = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 实例id
        self.load_balancer_id = load_balancer_id
        # 名称
        self.load_balancer_name = load_balancer_name
        # 负载均衡修改保护相关信息
        self.modification_protection_config = modification_protection_config

    def validate(self):
        if self.modification_protection_config:
            self.modification_protection_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('ModificationProtectionConfig') is not None:
            temp_model = UpdateLoadBalancerAttributeRequestModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m['ModificationProtectionConfig'])
        return self


class UpdateLoadBalancerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoadBalancerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLoadBalancerAttributeResponseBody = None,
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
            temp_model = UpdateLoadBalancerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoadBalancerEditionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_edition: str = None,
        load_balancer_id: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 实例版本
        self.load_balancer_edition = load_balancer_edition
        # 实例Id
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_edition is not None:
            result['LoadBalancerEdition'] = self.load_balancer_edition
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerEdition') is not None:
            self.load_balancer_edition = m.get('LoadBalancerEdition')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class UpdateLoadBalancerEditionResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoadBalancerEditionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLoadBalancerEditionResponseBody = None,
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
            temp_model = UpdateLoadBalancerEditionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoadBalancerZonesRequestZoneMappings(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # 交换机标识
        self.v_switch_id = v_switch_id
        # 可用区
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateLoadBalancerZonesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        zone_mappings: List[UpdateLoadBalancerZonesRequestZoneMappings] = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 实例id
        self.load_balancer_id = load_balancer_id
        # 可用区及交换机映射列表
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = UpdateLoadBalancerZonesRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class UpdateLoadBalancerZonesResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoadBalancerZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLoadBalancerZonesResponseBody = None,
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
            temp_model = UpdateLoadBalancerZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRuleAttributeRequestRuleActionsFixedResponseConfig(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        http_code: str = None,
    ):
        # 内容
        self.content = content
        # 内容类型
        self.content_type = content_type
        # HTTP响应码
        self.http_code = http_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        return self


class UpdateRuleAttributeRequestRuleActionsForwardGroupConfigServerGroupStickySession(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        timeout: int = None,
    ):
        # 是否开启会话保持
        self.enabled = enabled
        # 超时时间
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class UpdateRuleAttributeRequestRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        # 服务器组标识
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class UpdateRuleAttributeRequestRuleActionsForwardGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_sticky_session: UpdateRuleAttributeRequestRuleActionsForwardGroupConfigServerGroupStickySession = None,
        server_group_tuples: List[UpdateRuleAttributeRequestRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # 服务器组之间会话保持
        self.server_group_sticky_session = server_group_sticky_session
        # 转发到的目的服务器组列表
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_sticky_session:
            self.server_group_sticky_session.validate()
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_sticky_session is not None:
            result['ServerGroupStickySession'] = self.server_group_sticky_session.to_map()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupStickySession') is not None:
            temp_model = UpdateRuleAttributeRequestRuleActionsForwardGroupConfigServerGroupStickySession()
            self.server_group_sticky_session = temp_model.from_map(m['ServerGroupStickySession'])
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = UpdateRuleAttributeRequestRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class UpdateRuleAttributeRequestRuleActionsInsertHeaderConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        value_type: str = None,
    ):
        # HTTP标头
        self.key = key
        # HTTP标头内容
        self.value = value
        # 取值类型
        self.value_type = value_type

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
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class UpdateRuleAttributeRequestRuleActionsRedirectConfig(TeaModel):
    def __init__(
        self,
        host: str = None,
        http_code: str = None,
        path: str = None,
        port: str = None,
        protocol: str = None,
        query: str = None,
    ):
        # 要跳转的主机地址
        self.host = host
        # 跳转方式
        self.http_code = http_code
        # 要跳转的路径
        self.path = path
        # 要跳转的端口
        self.port = port
        # 要跳转的协议
        self.protocol = protocol
        # 要跳转的查询字符串
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class UpdateRuleAttributeRequestRuleActionsRewriteConfig(TeaModel):
    def __init__(
        self,
        host: str = None,
        path: str = None,
        query: str = None,
    ):
        # 主机名
        self.host = host
        # 路径
        self.path = path
        # 查询
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.path is not None:
            result['Path'] = self.path
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class UpdateRuleAttributeRequestRuleActionsTrafficLimitConfig(TeaModel):
    def __init__(
        self,
        qps: int = None,
    ):
        self.qps = qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['QPS'] = self.qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        return self


class UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfigMirrorGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples] = None,
    ):
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfig(TeaModel):
    def __init__(
        self,
        mirror_group_config: UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfigMirrorGroupConfig = None,
        target_type: str = None,
    ):
        # 镜像至服务器组
        self.mirror_group_config = mirror_group_config
        # 镜像目标类型
        self.target_type = target_type

    def validate(self):
        if self.mirror_group_config:
            self.mirror_group_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mirror_group_config is not None:
            result['MirrorGroupConfig'] = self.mirror_group_config.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MirrorGroupConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfigMirrorGroupConfig()
            self.mirror_group_config = temp_model.from_map(m['MirrorGroupConfig'])
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class UpdateRuleAttributeRequestRuleActions(TeaModel):
    def __init__(
        self,
        fixed_response_config: UpdateRuleAttributeRequestRuleActionsFixedResponseConfig = None,
        forward_group_config: UpdateRuleAttributeRequestRuleActionsForwardGroupConfig = None,
        insert_header_config: UpdateRuleAttributeRequestRuleActionsInsertHeaderConfig = None,
        order: int = None,
        redirect_config: UpdateRuleAttributeRequestRuleActionsRedirectConfig = None,
        rewrite_config: UpdateRuleAttributeRequestRuleActionsRewriteConfig = None,
        traffic_limit_config: UpdateRuleAttributeRequestRuleActionsTrafficLimitConfig = None,
        traffic_mirror_config: UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfig = None,
        type: str = None,
    ):
        # 返回固定内容动作配置
        self.fixed_response_config = fixed_response_config
        # 转发组动作配置
        self.forward_group_config = forward_group_config
        # 插入头部动作配置
        self.insert_header_config = insert_header_config
        # 优先级
        self.order = order
        # 重定向动作配置
        self.redirect_config = redirect_config
        # 内部重定向动作配置
        self.rewrite_config = rewrite_config
        # 流量限速
        self.traffic_limit_config = traffic_limit_config
        # 流量镜像
        self.traffic_mirror_config = traffic_mirror_config
        # 转发规则动作类型
        self.type = type

    def validate(self):
        if self.fixed_response_config:
            self.fixed_response_config.validate()
        if self.forward_group_config:
            self.forward_group_config.validate()
        if self.insert_header_config:
            self.insert_header_config.validate()
        if self.redirect_config:
            self.redirect_config.validate()
        if self.rewrite_config:
            self.rewrite_config.validate()
        if self.traffic_limit_config:
            self.traffic_limit_config.validate()
        if self.traffic_mirror_config:
            self.traffic_mirror_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fixed_response_config is not None:
            result['FixedResponseConfig'] = self.fixed_response_config.to_map()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.insert_header_config is not None:
            result['InsertHeaderConfig'] = self.insert_header_config.to_map()
        if self.order is not None:
            result['Order'] = self.order
        if self.redirect_config is not None:
            result['RedirectConfig'] = self.redirect_config.to_map()
        if self.rewrite_config is not None:
            result['RewriteConfig'] = self.rewrite_config.to_map()
        if self.traffic_limit_config is not None:
            result['TrafficLimitConfig'] = self.traffic_limit_config.to_map()
        if self.traffic_mirror_config is not None:
            result['TrafficMirrorConfig'] = self.traffic_mirror_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedResponseConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleActionsFixedResponseConfig()
            self.fixed_response_config = temp_model.from_map(m['FixedResponseConfig'])
        if m.get('ForwardGroupConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('InsertHeaderConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleActionsInsertHeaderConfig()
            self.insert_header_config = temp_model.from_map(m['InsertHeaderConfig'])
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RedirectConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleActionsRedirectConfig()
            self.redirect_config = temp_model.from_map(m['RedirectConfig'])
        if m.get('RewriteConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleActionsRewriteConfig()
            self.rewrite_config = temp_model.from_map(m['RewriteConfig'])
        if m.get('TrafficLimitConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleActionsTrafficLimitConfig()
            self.traffic_limit_config = temp_model.from_map(m['TrafficLimitConfig'])
        if m.get('TrafficMirrorConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfig()
            self.traffic_mirror_config = temp_model.from_map(m['TrafficMirrorConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateRuleAttributeRequestRuleConditionsCookieConfigValues(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Cookie条件键
        self.key = key
        # Cookie条件值
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


class UpdateRuleAttributeRequestRuleConditionsCookieConfig(TeaModel):
    def __init__(
        self,
        values: List[UpdateRuleAttributeRequestRuleConditionsCookieConfigValues] = None,
    ):
        # Cookie键值对列表
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = UpdateRuleAttributeRequestRuleConditionsCookieConfigValues()
                self.values.append(temp_model.from_map(k))
        return self


class UpdateRuleAttributeRequestRuleConditionsHeaderConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # HTTP标头键
        self.key = key
        # HTTP标头值列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateRuleAttributeRequestRuleConditionsHostConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 主机名列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateRuleAttributeRequestRuleConditionsMethodConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # HTTP请求方法列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateRuleAttributeRequestRuleConditionsPathConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 路径条件列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateRuleAttributeRequestRuleConditionsQueryStringConfigValues(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 查询字符串条件键
        self.key = key
        # 查询字符串条件值
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


class UpdateRuleAttributeRequestRuleConditionsQueryStringConfig(TeaModel):
    def __init__(
        self,
        values: List[UpdateRuleAttributeRequestRuleConditionsQueryStringConfigValues] = None,
    ):
        # 查询字符串条件键值对列表
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = UpdateRuleAttributeRequestRuleConditionsQueryStringConfigValues()
                self.values.append(temp_model.from_map(k))
        return self


class UpdateRuleAttributeRequestRuleConditionsSourceIpConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 基于源IP业务流量匹配
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateRuleAttributeRequestRuleConditions(TeaModel):
    def __init__(
        self,
        cookie_config: UpdateRuleAttributeRequestRuleConditionsCookieConfig = None,
        header_config: UpdateRuleAttributeRequestRuleConditionsHeaderConfig = None,
        host_config: UpdateRuleAttributeRequestRuleConditionsHostConfig = None,
        method_config: UpdateRuleAttributeRequestRuleConditionsMethodConfig = None,
        path_config: UpdateRuleAttributeRequestRuleConditionsPathConfig = None,
        query_string_config: UpdateRuleAttributeRequestRuleConditionsQueryStringConfig = None,
        source_ip_config: UpdateRuleAttributeRequestRuleConditionsSourceIpConfig = None,
        type: str = None,
    ):
        # Cookie条件配置
        self.cookie_config = cookie_config
        # HTTP标头条件配置
        self.header_config = header_config
        # 主机名条件配置
        self.host_config = host_config
        # HTTP请求方法条件配置
        self.method_config = method_config
        # 路径条件配置
        self.path_config = path_config
        # 查询字符串条件配置
        self.query_string_config = query_string_config
        # 基于源IP业务流量匹配
        self.source_ip_config = source_ip_config
        # 条件类型
        self.type = type

    def validate(self):
        if self.cookie_config:
            self.cookie_config.validate()
        if self.header_config:
            self.header_config.validate()
        if self.host_config:
            self.host_config.validate()
        if self.method_config:
            self.method_config.validate()
        if self.path_config:
            self.path_config.validate()
        if self.query_string_config:
            self.query_string_config.validate()
        if self.source_ip_config:
            self.source_ip_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie_config is not None:
            result['CookieConfig'] = self.cookie_config.to_map()
        if self.header_config is not None:
            result['HeaderConfig'] = self.header_config.to_map()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        if self.method_config is not None:
            result['MethodConfig'] = self.method_config.to_map()
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.query_string_config is not None:
            result['QueryStringConfig'] = self.query_string_config.to_map()
        if self.source_ip_config is not None:
            result['SourceIpConfig'] = self.source_ip_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleConditionsCookieConfig()
            self.cookie_config = temp_model.from_map(m['CookieConfig'])
        if m.get('HeaderConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleConditionsHeaderConfig()
            self.header_config = temp_model.from_map(m['HeaderConfig'])
        if m.get('HostConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        if m.get('MethodConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleConditionsMethodConfig()
            self.method_config = temp_model.from_map(m['MethodConfig'])
        if m.get('PathConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('QueryStringConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleConditionsQueryStringConfig()
            self.query_string_config = temp_model.from_map(m['QueryStringConfig'])
        if m.get('SourceIpConfig') is not None:
            temp_model = UpdateRuleAttributeRequestRuleConditionsSourceIpConfig()
            self.source_ip_config = temp_model.from_map(m['SourceIpConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateRuleAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        priority: int = None,
        rule_actions: List[UpdateRuleAttributeRequestRuleActions] = None,
        rule_conditions: List[UpdateRuleAttributeRequestRuleConditions] = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 转发规则优先级
        self.priority = priority
        # 转发规则动作
        self.rule_actions = rule_actions
        # 转发规则条件
        self.rule_conditions = rule_conditions
        # 转发规则标识
        self.rule_id = rule_id
        # 转发规则名称
        self.rule_name = rule_name

    def validate(self):
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = UpdateRuleAttributeRequestRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = UpdateRuleAttributeRequestRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class UpdateRuleAttributeResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRuleAttributeResponseBody = None,
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
            temp_model = UpdateRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRulesAttributeRequestRulesRuleActionsFixedResponseConfig(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        http_code: str = None,
    ):
        # 内容
        self.content = content
        # 内容类型
        self.content_type = content_type
        # HTTP响应码
        self.http_code = http_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        return self


class UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfigServerGroupStickySession(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        timeout: int = None,
    ):
        # 是否开启会话保持
        self.enabled = enabled
        # 超时时间
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
        weight: int = None,
    ):
        # 服务器组标识
        self.server_group_id = server_group_id
        # 权重
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_sticky_session: UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfigServerGroupStickySession = None,
        server_group_tuples: List[UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # 服务器组之间会话保持
        self.server_group_sticky_session = server_group_sticky_session
        # 转发到的目的服务器组列表
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_sticky_session:
            self.server_group_sticky_session.validate()
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_sticky_session is not None:
            result['ServerGroupStickySession'] = self.server_group_sticky_session.to_map()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupStickySession') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfigServerGroupStickySession()
            self.server_group_sticky_session = temp_model.from_map(m['ServerGroupStickySession'])
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class UpdateRulesAttributeRequestRulesRuleActionsInsertHeaderConfig(TeaModel):
    def __init__(
        self,
        cover_enabled: bool = None,
        key: str = None,
        value: str = None,
        value_type: str = None,
    ):
        # 是否覆盖请求中的值
        self.cover_enabled = cover_enabled
        # HTTP标头
        self.key = key
        # HTTP标头内容
        self.value = value
        # 取值类型
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_enabled is not None:
            result['CoverEnabled'] = self.cover_enabled
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverEnabled') is not None:
            self.cover_enabled = m.get('CoverEnabled')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class UpdateRulesAttributeRequestRulesRuleActionsRedirectConfig(TeaModel):
    def __init__(
        self,
        host: str = None,
        http_code: str = None,
        path: str = None,
        port: str = None,
        protocol: str = None,
        query: str = None,
    ):
        # 要跳转的主机地址
        self.host = host
        # 跳转方式
        self.http_code = http_code
        # 要跳转的路径
        self.path = path
        # 要跳转的端口
        self.port = port
        # 要跳转的协议
        self.protocol = protocol
        # 要跳转的查询字符串
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class UpdateRulesAttributeRequestRulesRuleActionsRemoveHeaderConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
    ):
        # HTTP标头键
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class UpdateRulesAttributeRequestRulesRuleActionsRewriteConfig(TeaModel):
    def __init__(
        self,
        host: str = None,
        path: str = None,
        query: str = None,
    ):
        # 主机名
        self.host = host
        # 路径
        self.path = path
        # 查询
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.path is not None:
            result['Path'] = self.path
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class UpdateRulesAttributeRequestRulesRuleActionsTrafficLimitConfig(TeaModel):
    def __init__(
        self,
        qps: int = None,
    ):
        self.qps = qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['QPS'] = self.qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        return self


class UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples] = None,
    ):
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfig(TeaModel):
    def __init__(
        self,
        mirror_group_config: UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfig = None,
        target_type: str = None,
    ):
        # 镜像至服务器组
        self.mirror_group_config = mirror_group_config
        # 镜像目标类型
        self.target_type = target_type

    def validate(self):
        if self.mirror_group_config:
            self.mirror_group_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mirror_group_config is not None:
            result['MirrorGroupConfig'] = self.mirror_group_config.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MirrorGroupConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfig()
            self.mirror_group_config = temp_model.from_map(m['MirrorGroupConfig'])
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class UpdateRulesAttributeRequestRulesRuleActions(TeaModel):
    def __init__(
        self,
        fixed_response_config: UpdateRulesAttributeRequestRulesRuleActionsFixedResponseConfig = None,
        forward_group_config: UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfig = None,
        insert_header_config: UpdateRulesAttributeRequestRulesRuleActionsInsertHeaderConfig = None,
        order: int = None,
        redirect_config: UpdateRulesAttributeRequestRulesRuleActionsRedirectConfig = None,
        remove_header_config: UpdateRulesAttributeRequestRulesRuleActionsRemoveHeaderConfig = None,
        rewrite_config: UpdateRulesAttributeRequestRulesRuleActionsRewriteConfig = None,
        traffic_limit_config: UpdateRulesAttributeRequestRulesRuleActionsTrafficLimitConfig = None,
        traffic_mirror_config: UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfig = None,
        type: str = None,
    ):
        # 返回固定内容动作配置
        self.fixed_response_config = fixed_response_config
        # 转发组动作配置
        self.forward_group_config = forward_group_config
        # 插入头部动作配置
        self.insert_header_config = insert_header_config
        # 优先级
        self.order = order
        # 重定向动作配置
        self.redirect_config = redirect_config
        # 去除HTTP标头
        self.remove_header_config = remove_header_config
        # 内部重定向动作配置
        self.rewrite_config = rewrite_config
        # 流量限速
        self.traffic_limit_config = traffic_limit_config
        # 流量镜像
        self.traffic_mirror_config = traffic_mirror_config
        # 转发规则动作类型
        self.type = type

    def validate(self):
        if self.fixed_response_config:
            self.fixed_response_config.validate()
        if self.forward_group_config:
            self.forward_group_config.validate()
        if self.insert_header_config:
            self.insert_header_config.validate()
        if self.redirect_config:
            self.redirect_config.validate()
        if self.remove_header_config:
            self.remove_header_config.validate()
        if self.rewrite_config:
            self.rewrite_config.validate()
        if self.traffic_limit_config:
            self.traffic_limit_config.validate()
        if self.traffic_mirror_config:
            self.traffic_mirror_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fixed_response_config is not None:
            result['FixedResponseConfig'] = self.fixed_response_config.to_map()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.insert_header_config is not None:
            result['InsertHeaderConfig'] = self.insert_header_config.to_map()
        if self.order is not None:
            result['Order'] = self.order
        if self.redirect_config is not None:
            result['RedirectConfig'] = self.redirect_config.to_map()
        if self.remove_header_config is not None:
            result['RemoveHeaderConfig'] = self.remove_header_config.to_map()
        if self.rewrite_config is not None:
            result['RewriteConfig'] = self.rewrite_config.to_map()
        if self.traffic_limit_config is not None:
            result['TrafficLimitConfig'] = self.traffic_limit_config.to_map()
        if self.traffic_mirror_config is not None:
            result['TrafficMirrorConfig'] = self.traffic_mirror_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedResponseConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleActionsFixedResponseConfig()
            self.fixed_response_config = temp_model.from_map(m['FixedResponseConfig'])
        if m.get('ForwardGroupConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('InsertHeaderConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleActionsInsertHeaderConfig()
            self.insert_header_config = temp_model.from_map(m['InsertHeaderConfig'])
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RedirectConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleActionsRedirectConfig()
            self.redirect_config = temp_model.from_map(m['RedirectConfig'])
        if m.get('RemoveHeaderConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleActionsRemoveHeaderConfig()
            self.remove_header_config = temp_model.from_map(m['RemoveHeaderConfig'])
        if m.get('RewriteConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleActionsRewriteConfig()
            self.rewrite_config = temp_model.from_map(m['RewriteConfig'])
        if m.get('TrafficLimitConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleActionsTrafficLimitConfig()
            self.traffic_limit_config = temp_model.from_map(m['TrafficLimitConfig'])
        if m.get('TrafficMirrorConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfig()
            self.traffic_mirror_config = temp_model.from_map(m['TrafficMirrorConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateRulesAttributeRequestRulesRuleConditionsCookieConfigValues(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Cookie条件键
        self.key = key
        # Cookie条件值
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


class UpdateRulesAttributeRequestRulesRuleConditionsCookieConfig(TeaModel):
    def __init__(
        self,
        values: List[UpdateRulesAttributeRequestRulesRuleConditionsCookieConfigValues] = None,
    ):
        # Cookie键值对列表
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = UpdateRulesAttributeRequestRulesRuleConditionsCookieConfigValues()
                self.values.append(temp_model.from_map(k))
        return self


class UpdateRulesAttributeRequestRulesRuleConditionsHeaderConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # HTTP标头键
        self.key = key
        # HTTP标头值列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateRulesAttributeRequestRulesRuleConditionsHostConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 主机名列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateRulesAttributeRequestRulesRuleConditionsMethodConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # HTTP请求方法列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateRulesAttributeRequestRulesRuleConditionsPathConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 路径条件列表
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateRulesAttributeRequestRulesRuleConditionsQueryStringConfigValues(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 查询字符串条件键
        self.key = key
        # 查询字符串条件值
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


class UpdateRulesAttributeRequestRulesRuleConditionsQueryStringConfig(TeaModel):
    def __init__(
        self,
        values: List[UpdateRulesAttributeRequestRulesRuleConditionsQueryStringConfigValues] = None,
    ):
        # 查询字符串条件键值对列表
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = UpdateRulesAttributeRequestRulesRuleConditionsQueryStringConfigValues()
                self.values.append(temp_model.from_map(k))
        return self


class UpdateRulesAttributeRequestRulesRuleConditionsResponseHeaderConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # 返回HTTP标头键
        self.key = key
        # 返回HTTP标头值
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateRulesAttributeRequestRulesRuleConditionsResponseStatusCodeConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # 返回状态码条件
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateRulesAttributeRequestRulesRuleConditionsSourceIpConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateRulesAttributeRequestRulesRuleConditions(TeaModel):
    def __init__(
        self,
        cookie_config: UpdateRulesAttributeRequestRulesRuleConditionsCookieConfig = None,
        header_config: UpdateRulesAttributeRequestRulesRuleConditionsHeaderConfig = None,
        host_config: UpdateRulesAttributeRequestRulesRuleConditionsHostConfig = None,
        method_config: UpdateRulesAttributeRequestRulesRuleConditionsMethodConfig = None,
        path_config: UpdateRulesAttributeRequestRulesRuleConditionsPathConfig = None,
        query_string_config: UpdateRulesAttributeRequestRulesRuleConditionsQueryStringConfig = None,
        response_header_config: UpdateRulesAttributeRequestRulesRuleConditionsResponseHeaderConfig = None,
        response_status_code_config: UpdateRulesAttributeRequestRulesRuleConditionsResponseStatusCodeConfig = None,
        source_ip_config: UpdateRulesAttributeRequestRulesRuleConditionsSourceIpConfig = None,
        type: str = None,
    ):
        # Cookie条件配置
        self.cookie_config = cookie_config
        # HTTP标头条件配置
        self.header_config = header_config
        # 主机名条件配置
        self.host_config = host_config
        # HTTP请求方法条件配置
        self.method_config = method_config
        # 查询字符串条件配置
        self.path_config = path_config
        # 查询字符串条件配置
        self.query_string_config = query_string_config
        # 返回HTTP标头
        self.response_header_config = response_header_config
        # 返回状态码条件
        self.response_status_code_config = response_status_code_config
        # 基于源IP业务流量匹配
        self.source_ip_config = source_ip_config
        # 条件类型
        self.type = type

    def validate(self):
        if self.cookie_config:
            self.cookie_config.validate()
        if self.header_config:
            self.header_config.validate()
        if self.host_config:
            self.host_config.validate()
        if self.method_config:
            self.method_config.validate()
        if self.path_config:
            self.path_config.validate()
        if self.query_string_config:
            self.query_string_config.validate()
        if self.response_header_config:
            self.response_header_config.validate()
        if self.response_status_code_config:
            self.response_status_code_config.validate()
        if self.source_ip_config:
            self.source_ip_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie_config is not None:
            result['CookieConfig'] = self.cookie_config.to_map()
        if self.header_config is not None:
            result['HeaderConfig'] = self.header_config.to_map()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        if self.method_config is not None:
            result['MethodConfig'] = self.method_config.to_map()
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.query_string_config is not None:
            result['QueryStringConfig'] = self.query_string_config.to_map()
        if self.response_header_config is not None:
            result['ResponseHeaderConfig'] = self.response_header_config.to_map()
        if self.response_status_code_config is not None:
            result['ResponseStatusCodeConfig'] = self.response_status_code_config.to_map()
        if self.source_ip_config is not None:
            result['SourceIpConfig'] = self.source_ip_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleConditionsCookieConfig()
            self.cookie_config = temp_model.from_map(m['CookieConfig'])
        if m.get('HeaderConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleConditionsHeaderConfig()
            self.header_config = temp_model.from_map(m['HeaderConfig'])
        if m.get('HostConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        if m.get('MethodConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleConditionsMethodConfig()
            self.method_config = temp_model.from_map(m['MethodConfig'])
        if m.get('PathConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('QueryStringConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleConditionsQueryStringConfig()
            self.query_string_config = temp_model.from_map(m['QueryStringConfig'])
        if m.get('ResponseHeaderConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleConditionsResponseHeaderConfig()
            self.response_header_config = temp_model.from_map(m['ResponseHeaderConfig'])
        if m.get('ResponseStatusCodeConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleConditionsResponseStatusCodeConfig()
            self.response_status_code_config = temp_model.from_map(m['ResponseStatusCodeConfig'])
        if m.get('SourceIpConfig') is not None:
            temp_model = UpdateRulesAttributeRequestRulesRuleConditionsSourceIpConfig()
            self.source_ip_config = temp_model.from_map(m['SourceIpConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateRulesAttributeRequestRules(TeaModel):
    def __init__(
        self,
        priority: int = None,
        rule_actions: List[UpdateRulesAttributeRequestRulesRuleActions] = None,
        rule_conditions: List[UpdateRulesAttributeRequestRulesRuleConditions] = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        # 转发规则优先级
        self.priority = priority
        # 转发规则动作
        self.rule_actions = rule_actions
        # 转发规则条件
        self.rule_conditions = rule_conditions
        # 转发规则ID
        self.rule_id = rule_id
        # 转发规则名称
        self.rule_name = rule_name

    def validate(self):
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = UpdateRulesAttributeRequestRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = UpdateRulesAttributeRequestRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class UpdateRulesAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        rules: List[UpdateRulesAttributeRequestRules] = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 转发规则列表
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = UpdateRulesAttributeRequestRules()
                self.rules.append(temp_model.from_map(k))
        return self


class UpdateRulesAttributeResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRulesAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRulesAttributeResponseBody = None,
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
            temp_model = UpdateRulesAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecurityPolicyAttributeRequest(TeaModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        security_policy_id: str = None,
        security_policy_name: str = None,
        tlsversions: List[str] = None,
    ):
        # 加密套件
        self.ciphers = ciphers
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 安全策略id
        self.security_policy_id = security_policy_id
        # 安全策略名称
        self.security_policy_name = security_policy_name
        # TLS版本
        self.tlsversions = tlsversions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name
        if self.tlsversions is not None:
            result['TLSVersions'] = self.tlsversions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')
        if m.get('TLSVersions') is not None:
            self.tlsversions = m.get('TLSVersions')
        return self


class UpdateSecurityPolicyAttributeResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSecurityPolicyAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSecurityPolicyAttributeResponseBody = None,
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
            temp_model = UpdateSecurityPolicyAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServerGroupAttributeRequestHealthCheckConfig(TeaModel):
    def __init__(
        self,
        health_check_codes: List[str] = None,
        health_check_connect_port: int = None,
        health_check_enabled: bool = None,
        health_check_host: str = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_path: str = None,
        health_check_protocol: str = None,
        health_check_timeout: int = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
    ):
        # 健康检查正常的状态码
        self.health_check_codes = health_check_codes
        # 健康检查端口
        self.health_check_connect_port = health_check_connect_port
        # 是否启用健康检查
        self.health_check_enabled = health_check_enabled
        # 健康检查域名
        self.health_check_host = health_check_host
        # 健康检查HTTP协议版本
        self.health_check_http_version = health_check_http_version
        # 健康检查间隔
        self.health_check_interval = health_check_interval
        # 健康检查方法
        self.health_check_method = health_check_method
        # 健康检查Path
        self.health_check_path = health_check_path
        # 健康检查协议类型
        self.health_check_protocol = health_check_protocol
        # 健康检查超时时间
        self.health_check_timeout = health_check_timeout
        # 健康检查成功判定阈值
        self.healthy_threshold = healthy_threshold
        # 健康检查不成功判定阈值
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_codes is not None:
            result['HealthCheckCodes'] = self.health_check_codes
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_host is not None:
            result['HealthCheckHost'] = self.health_check_host
        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckCodes') is not None:
            self.health_check_codes = m.get('HealthCheckCodes')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckHost') is not None:
            self.health_check_host = m.get('HealthCheckHost')
        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class UpdateServerGroupAttributeRequestStickySessionConfig(TeaModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        sticky_session_enabled: bool = None,
        sticky_session_type: str = None,
    ):
        # 服务器上配置的Cookie
        self.cookie = cookie
        # 服务器上配置的Cookie
        self.cookie_timeout = cookie_timeout
        # 是否启用会话保持
        self.sticky_session_enabled = sticky_session_enabled
        # 会话保持类型
        self.sticky_session_type = sticky_session_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.sticky_session_enabled is not None:
            result['StickySessionEnabled'] = self.sticky_session_enabled
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('StickySessionEnabled') is not None:
            self.sticky_session_enabled = m.get('StickySessionEnabled')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        return self


class UpdateServerGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        health_check_config: UpdateServerGroupAttributeRequestHealthCheckConfig = None,
        scheduler: str = None,
        server_group_id: str = None,
        server_group_name: str = None,
        service_name: str = None,
        sticky_session_config: UpdateServerGroupAttributeRequestStickySessionConfig = None,
    ):
        # 幂等标识
        self.client_token = client_token
        # 是否只预检此次请求
        self.dry_run = dry_run
        # 健康检查配置
        self.health_check_config = health_check_config
        # 调度策略
        self.scheduler = scheduler
        # 服务器组Id
        self.server_group_id = server_group_id
        # Acl名称
        self.server_group_name = server_group_name
        # 服务器名称
        self.service_name = service_name
        # 会话保持配置
        self.sticky_session_config = sticky_session_config

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()
        if self.sticky_session_config:
            self.sticky_session_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.sticky_session_config is not None:
            result['StickySessionConfig'] = self.sticky_session_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('HealthCheckConfig') is not None:
            temp_model = UpdateServerGroupAttributeRequestHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m['HealthCheckConfig'])
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StickySessionConfig') is not None:
            temp_model = UpdateServerGroupAttributeRequestStickySessionConfig()
            self.sticky_session_config = temp_model.from_map(m['StickySessionConfig'])
        return self


class UpdateServerGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServerGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateServerGroupAttributeResponseBody = None,
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
            temp_model = UpdateServerGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServerGroupServersAttributeRequestServers(TeaModel):
    def __init__(
        self,
        description: str = None,
        port: int = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        weight: int = None,
    ):
        # 后端服务器描述
        self.description = description
        # 后端端口号
        self.port = port
        # 后端服务器id
        self.server_id = server_id
        # 后端服务器ip
        self.server_ip = server_ip
        # 后端服务器类型
        self.server_type = server_type
        # 后端服务器权重
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateServerGroupServersAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        server_group_id: str = None,
        servers: List[UpdateServerGroupServersAttributeRequestServers] = None,
    ):
        # 幂等Token
        self.client_token = client_token
        # dryRun
        self.dry_run = dry_run
        # 后端服务器Id
        self.server_group_id = server_group_id
        # 后端服务器
        self.servers = servers

    def validate(self):
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = UpdateServerGroupServersAttributeRequestServers()
                self.servers.append(temp_model.from_map(k))
        return self


class UpdateServerGroupServersAttributeResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # 异步任务Id
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServerGroupServersAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateServerGroupServersAttributeResponseBody = None,
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
            temp_model = UpdateServerGroupServersAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


