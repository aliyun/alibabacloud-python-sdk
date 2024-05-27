# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreateCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate: str = None,
        certificate_name: str = None,
        domain: str = None,
        instance_id: str = None,
        private_key: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.certificate = certificate
        # This parameter is required.
        self.certificate_name = certificate_name
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.private_key = private_key
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateCertificateResponseBody(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        request_id: str = None,
    ):
        self.certificate_id = certificate_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCertificateResponseBody = None,
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
            temp_model = CreateCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateByCertificateIdRequest(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        domain: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.certificate_id = certificate_id
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateCertificateByCertificateIdResponseBody(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        request_id: str = None,
    ):
        self.certificate_id = certificate_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCertificateByCertificateIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCertificateByCertificateIdResponseBody = None,
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
            temp_model = CreateCertificateByCertificateIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequest(TeaModel):
    def __init__(
        self,
        access_header_mode: int = None,
        access_headers: str = None,
        access_type: str = None,
        cloud_native_instances: str = None,
        cluster_type: int = None,
        connection_time: int = None,
        domain: str = None,
        http_2port: str = None,
        http_port: str = None,
        http_to_user_ip: int = None,
        https_port: str = None,
        https_redirect: int = None,
        instance_id: str = None,
        ip_follow_status: int = None,
        is_access_product: int = None,
        keepalive: bool = None,
        keepalive_requests: int = None,
        keepalive_timeout: int = None,
        load_balancing: int = None,
        log_headers: str = None,
        read_time: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        retry: bool = None,
        sni_host: str = None,
        sni_status: int = None,
        source_ips: str = None,
        write_time: int = None,
    ):
        self.access_header_mode = access_header_mode
        self.access_headers = access_headers
        self.access_type = access_type
        self.cloud_native_instances = cloud_native_instances
        self.cluster_type = cluster_type
        self.connection_time = connection_time
        # This parameter is required.
        self.domain = domain
        self.http_2port = http_2port
        self.http_port = http_port
        self.http_to_user_ip = http_to_user_ip
        self.https_port = https_port
        self.https_redirect = https_redirect
        # This parameter is required.
        self.instance_id = instance_id
        self.ip_follow_status = ip_follow_status
        # This parameter is required.
        self.is_access_product = is_access_product
        self.keepalive = keepalive
        self.keepalive_requests = keepalive_requests
        self.keepalive_timeout = keepalive_timeout
        self.load_balancing = load_balancing
        self.log_headers = log_headers
        self.read_time = read_time
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.retry = retry
        self.sni_host = sni_host
        self.sni_status = sni_status
        self.source_ips = source_ips
        self.write_time = write_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_header_mode is not None:
            result['AccessHeaderMode'] = self.access_header_mode
        if self.access_headers is not None:
            result['AccessHeaders'] = self.access_headers
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.cloud_native_instances is not None:
            result['CloudNativeInstances'] = self.cloud_native_instances
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.connection_time is not None:
            result['ConnectionTime'] = self.connection_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.http_2port is not None:
            result['Http2Port'] = self.http_2port
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.http_to_user_ip is not None:
            result['HttpToUserIp'] = self.http_to_user_ip
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.https_redirect is not None:
            result['HttpsRedirect'] = self.https_redirect
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_follow_status is not None:
            result['IpFollowStatus'] = self.ip_follow_status
        if self.is_access_product is not None:
            result['IsAccessProduct'] = self.is_access_product
        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive
        if self.keepalive_requests is not None:
            result['KeepaliveRequests'] = self.keepalive_requests
        if self.keepalive_timeout is not None:
            result['KeepaliveTimeout'] = self.keepalive_timeout
        if self.load_balancing is not None:
            result['LoadBalancing'] = self.load_balancing
        if self.log_headers is not None:
            result['LogHeaders'] = self.log_headers
        if self.read_time is not None:
            result['ReadTime'] = self.read_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.retry is not None:
            result['Retry'] = self.retry
        if self.sni_host is not None:
            result['SniHost'] = self.sni_host
        if self.sni_status is not None:
            result['SniStatus'] = self.sni_status
        if self.source_ips is not None:
            result['SourceIps'] = self.source_ips
        if self.write_time is not None:
            result['WriteTime'] = self.write_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessHeaderMode') is not None:
            self.access_header_mode = m.get('AccessHeaderMode')
        if m.get('AccessHeaders') is not None:
            self.access_headers = m.get('AccessHeaders')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('CloudNativeInstances') is not None:
            self.cloud_native_instances = m.get('CloudNativeInstances')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ConnectionTime') is not None:
            self.connection_time = m.get('ConnectionTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Http2Port') is not None:
            self.http_2port = m.get('Http2Port')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('HttpToUserIp') is not None:
            self.http_to_user_ip = m.get('HttpToUserIp')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('HttpsRedirect') is not None:
            self.https_redirect = m.get('HttpsRedirect')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpFollowStatus') is not None:
            self.ip_follow_status = m.get('IpFollowStatus')
        if m.get('IsAccessProduct') is not None:
            self.is_access_product = m.get('IsAccessProduct')
        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')
        if m.get('KeepaliveRequests') is not None:
            self.keepalive_requests = m.get('KeepaliveRequests')
        if m.get('KeepaliveTimeout') is not None:
            self.keepalive_timeout = m.get('KeepaliveTimeout')
        if m.get('LoadBalancing') is not None:
            self.load_balancing = m.get('LoadBalancing')
        if m.get('LogHeaders') is not None:
            self.log_headers = m.get('LogHeaders')
        if m.get('ReadTime') is not None:
            self.read_time = m.get('ReadTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Retry') is not None:
            self.retry = m.get('Retry')
        if m.get('SniHost') is not None:
            self.sni_host = m.get('SniHost')
        if m.get('SniStatus') is not None:
            self.sni_status = m.get('SniStatus')
        if m.get('SourceIps') is not None:
            self.source_ips = m.get('SourceIps')
        if m.get('WriteTime') is not None:
            self.write_time = m.get('WriteTime')
        return self


class CreateDomainResponseBody(TeaModel):
    def __init__(
        self,
        cname: str = None,
        request_id: str = None,
    ):
        self.cname = cname
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDomainResponseBody = None,
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
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProtectionModuleRuleRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        rule: str = None,
    ):
        # This parameter is required.
        self.defense_type = defense_type
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.rule = rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule is not None:
            result['Rule'] = self.rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        return self


class CreateProtectionModuleRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class CreateProtectionModuleRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProtectionModuleRuleResponseBody = None,
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
            temp_model = CreateProtectionModuleRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDomainResponseBody = None,
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
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteProtectionModuleRuleRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        rule_id: int = None,
    ):
        # This parameter is required.
        self.defense_type = defense_type
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteProtectionModuleRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteProtectionModuleRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProtectionModuleRuleResponseBody = None,
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
            temp_model = DeleteProtectionModuleRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertMatchStatusRequest(TeaModel):
    def __init__(
        self,
        certificate: str = None,
        domain: str = None,
        instance_id: str = None,
        private_key: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.certificate = certificate
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.private_key = private_key
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeCertMatchStatusResponseBody(TeaModel):
    def __init__(
        self,
        match_status: bool = None,
        request_id: str = None,
    ):
        self.match_status = match_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_status is not None:
            result['MatchStatus'] = self.match_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchStatus') is not None:
            self.match_status = m.get('MatchStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCertMatchStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCertMatchStatusResponseBody = None,
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
            temp_model = DescribeCertMatchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificatesRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeCertificatesResponseBodyCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        certificate_name: str = None,
        common_name: str = None,
        end_time: int = None,
        is_using: bool = None,
        sans: List[str] = None,
    ):
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name
        self.common_name = common_name
        self.end_time = end_time
        self.is_using = is_using
        self.sans = sans

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_using is not None:
            result['IsUsing'] = self.is_using
        if self.sans is not None:
            result['Sans'] = self.sans
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsUsing') is not None:
            self.is_using = m.get('IsUsing')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        return self


class DescribeCertificatesResponseBody(TeaModel):
    def __init__(
        self,
        certificates: List[DescribeCertificatesResponseBodyCertificates] = None,
        request_id: str = None,
    ):
        self.certificates = certificates
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = DescribeCertificatesResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCertificatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCertificatesResponseBody = None,
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
            temp_model = DescribeCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDomainResponseBodyDomainCloudNativeInstancesProtocolPortConfigs(TeaModel):
    def __init__(
        self,
        ports: List[int] = None,
        protocol: str = None,
    ):
        self.ports = ports
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeDomainResponseBodyDomainCloudNativeInstances(TeaModel):
    def __init__(
        self,
        cloud_native_product_name: str = None,
        ipaddress_list: List[str] = None,
        instance_id: str = None,
        protocol_port_configs: List[DescribeDomainResponseBodyDomainCloudNativeInstancesProtocolPortConfigs] = None,
        redirection_type_name: str = None,
    ):
        self.cloud_native_product_name = cloud_native_product_name
        self.ipaddress_list = ipaddress_list
        self.instance_id = instance_id
        self.protocol_port_configs = protocol_port_configs
        self.redirection_type_name = redirection_type_name

    def validate(self):
        if self.protocol_port_configs:
            for k in self.protocol_port_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_native_product_name is not None:
            result['CloudNativeProductName'] = self.cloud_native_product_name
        if self.ipaddress_list is not None:
            result['IPAddressList'] = self.ipaddress_list
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['ProtocolPortConfigs'] = []
        if self.protocol_port_configs is not None:
            for k in self.protocol_port_configs:
                result['ProtocolPortConfigs'].append(k.to_map() if k else None)
        if self.redirection_type_name is not None:
            result['RedirectionTypeName'] = self.redirection_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudNativeProductName') is not None:
            self.cloud_native_product_name = m.get('CloudNativeProductName')
        if m.get('IPAddressList') is not None:
            self.ipaddress_list = m.get('IPAddressList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.protocol_port_configs = []
        if m.get('ProtocolPortConfigs') is not None:
            for k in m.get('ProtocolPortConfigs'):
                temp_model = DescribeDomainResponseBodyDomainCloudNativeInstancesProtocolPortConfigs()
                self.protocol_port_configs.append(temp_model.from_map(k))
        if m.get('RedirectionTypeName') is not None:
            self.redirection_type_name = m.get('RedirectionTypeName')
        return self


class DescribeDomainResponseBodyDomainLogHeaders(TeaModel):
    def __init__(
        self,
        k: str = None,
        v: str = None,
    ):
        self.k = k
        self.v = v

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k is not None:
            result['k'] = self.k
        if self.v is not None:
            result['v'] = self.v
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('k') is not None:
            self.k = m.get('k')
        if m.get('v') is not None:
            self.v = m.get('v')
        return self


class DescribeDomainResponseBodyDomain(TeaModel):
    def __init__(
        self,
        access_header_mode: int = None,
        access_headers: List[str] = None,
        access_type: str = None,
        cloud_native_instances: List[DescribeDomainResponseBodyDomainCloudNativeInstances] = None,
        cluster_type: int = None,
        cname: str = None,
        connection_time: int = None,
        http_2port: List[int] = None,
        http_port: List[int] = None,
        http_to_user_ip: int = None,
        https_port: List[int] = None,
        https_redirect: int = None,
        ip_follow_status: int = None,
        is_access_product: int = None,
        keepalive: bool = None,
        keepalive_requests: int = None,
        keepalive_timeout: int = None,
        load_balancing: int = None,
        log_headers: List[DescribeDomainResponseBodyDomainLogHeaders] = None,
        read_time: int = None,
        resource_group_id: str = None,
        retry: bool = None,
        sni_host: str = None,
        sni_status: int = None,
        source_ips: List[str] = None,
        version: int = None,
        write_time: int = None,
    ):
        self.access_header_mode = access_header_mode
        self.access_headers = access_headers
        self.access_type = access_type
        self.cloud_native_instances = cloud_native_instances
        self.cluster_type = cluster_type
        self.cname = cname
        self.connection_time = connection_time
        self.http_2port = http_2port
        self.http_port = http_port
        self.http_to_user_ip = http_to_user_ip
        self.https_port = https_port
        self.https_redirect = https_redirect
        self.ip_follow_status = ip_follow_status
        self.is_access_product = is_access_product
        self.keepalive = keepalive
        self.keepalive_requests = keepalive_requests
        self.keepalive_timeout = keepalive_timeout
        self.load_balancing = load_balancing
        self.log_headers = log_headers
        self.read_time = read_time
        self.resource_group_id = resource_group_id
        self.retry = retry
        self.sni_host = sni_host
        self.sni_status = sni_status
        self.source_ips = source_ips
        self.version = version
        self.write_time = write_time

    def validate(self):
        if self.cloud_native_instances:
            for k in self.cloud_native_instances:
                if k:
                    k.validate()
        if self.log_headers:
            for k in self.log_headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_header_mode is not None:
            result['AccessHeaderMode'] = self.access_header_mode
        if self.access_headers is not None:
            result['AccessHeaders'] = self.access_headers
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        result['CloudNativeInstances'] = []
        if self.cloud_native_instances is not None:
            for k in self.cloud_native_instances:
                result['CloudNativeInstances'].append(k.to_map() if k else None)
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.connection_time is not None:
            result['ConnectionTime'] = self.connection_time
        if self.http_2port is not None:
            result['Http2Port'] = self.http_2port
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.http_to_user_ip is not None:
            result['HttpToUserIp'] = self.http_to_user_ip
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.https_redirect is not None:
            result['HttpsRedirect'] = self.https_redirect
        if self.ip_follow_status is not None:
            result['IpFollowStatus'] = self.ip_follow_status
        if self.is_access_product is not None:
            result['IsAccessProduct'] = self.is_access_product
        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive
        if self.keepalive_requests is not None:
            result['KeepaliveRequests'] = self.keepalive_requests
        if self.keepalive_timeout is not None:
            result['KeepaliveTimeout'] = self.keepalive_timeout
        if self.load_balancing is not None:
            result['LoadBalancing'] = self.load_balancing
        result['LogHeaders'] = []
        if self.log_headers is not None:
            for k in self.log_headers:
                result['LogHeaders'].append(k.to_map() if k else None)
        if self.read_time is not None:
            result['ReadTime'] = self.read_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.retry is not None:
            result['Retry'] = self.retry
        if self.sni_host is not None:
            result['SniHost'] = self.sni_host
        if self.sni_status is not None:
            result['SniStatus'] = self.sni_status
        if self.source_ips is not None:
            result['SourceIps'] = self.source_ips
        if self.version is not None:
            result['Version'] = self.version
        if self.write_time is not None:
            result['WriteTime'] = self.write_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessHeaderMode') is not None:
            self.access_header_mode = m.get('AccessHeaderMode')
        if m.get('AccessHeaders') is not None:
            self.access_headers = m.get('AccessHeaders')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        self.cloud_native_instances = []
        if m.get('CloudNativeInstances') is not None:
            for k in m.get('CloudNativeInstances'):
                temp_model = DescribeDomainResponseBodyDomainCloudNativeInstances()
                self.cloud_native_instances.append(temp_model.from_map(k))
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('ConnectionTime') is not None:
            self.connection_time = m.get('ConnectionTime')
        if m.get('Http2Port') is not None:
            self.http_2port = m.get('Http2Port')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('HttpToUserIp') is not None:
            self.http_to_user_ip = m.get('HttpToUserIp')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('HttpsRedirect') is not None:
            self.https_redirect = m.get('HttpsRedirect')
        if m.get('IpFollowStatus') is not None:
            self.ip_follow_status = m.get('IpFollowStatus')
        if m.get('IsAccessProduct') is not None:
            self.is_access_product = m.get('IsAccessProduct')
        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')
        if m.get('KeepaliveRequests') is not None:
            self.keepalive_requests = m.get('KeepaliveRequests')
        if m.get('KeepaliveTimeout') is not None:
            self.keepalive_timeout = m.get('KeepaliveTimeout')
        if m.get('LoadBalancing') is not None:
            self.load_balancing = m.get('LoadBalancing')
        self.log_headers = []
        if m.get('LogHeaders') is not None:
            for k in m.get('LogHeaders'):
                temp_model = DescribeDomainResponseBodyDomainLogHeaders()
                self.log_headers.append(temp_model.from_map(k))
        if m.get('ReadTime') is not None:
            self.read_time = m.get('ReadTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Retry') is not None:
            self.retry = m.get('Retry')
        if m.get('SniHost') is not None:
            self.sni_host = m.get('SniHost')
        if m.get('SniStatus') is not None:
            self.sni_status = m.get('SniStatus')
        if m.get('SourceIps') is not None:
            self.source_ips = m.get('SourceIps')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WriteTime') is not None:
            self.write_time = m.get('WriteTime')
        return self


class DescribeDomainResponseBody(TeaModel):
    def __init__(
        self,
        domain: DescribeDomainResponseBodyDomain = None,
        request_id: str = None,
    ):
        self.domain = domain
        self.request_id = request_id

    def validate(self):
        if self.domain:
            self.domain.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            temp_model = DescribeDomainResponseBodyDomain()
            self.domain = temp_model.from_map(m['Domain'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainResponseBody = None,
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
            temp_model = DescribeDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAdvanceConfigsRequest(TeaModel):
    def __init__(
        self,
        domain_list: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.domain_list = domain_list
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDomainAdvanceConfigsResponseBodyDomainConfigsProfile(TeaModel):
    def __init__(
        self,
        cert_status: int = None,
        cluster_type: int = None,
        cname: str = None,
        exclusive_vip_status: int = None,
        gslbstatus: str = None,
        http_2port: List[int] = None,
        http_port: List[int] = None,
        https_port: List[int] = None,
        ipv_6status: int = None,
        resolved_type: int = None,
        rs: List[str] = None,
        vip_service_status: int = None,
    ):
        self.cert_status = cert_status
        self.cluster_type = cluster_type
        self.cname = cname
        self.exclusive_vip_status = exclusive_vip_status
        self.gslbstatus = gslbstatus
        self.http_2port = http_2port
        self.http_port = http_port
        self.https_port = https_port
        self.ipv_6status = ipv_6status
        self.resolved_type = resolved_type
        self.rs = rs
        self.vip_service_status = vip_service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_status is not None:
            result['CertStatus'] = self.cert_status
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.exclusive_vip_status is not None:
            result['ExclusiveVipStatus'] = self.exclusive_vip_status
        if self.gslbstatus is not None:
            result['GSLBStatus'] = self.gslbstatus
        if self.http_2port is not None:
            result['Http2Port'] = self.http_2port
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.ipv_6status is not None:
            result['Ipv6Status'] = self.ipv_6status
        if self.resolved_type is not None:
            result['ResolvedType'] = self.resolved_type
        if self.rs is not None:
            result['Rs'] = self.rs
        if self.vip_service_status is not None:
            result['VipServiceStatus'] = self.vip_service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertStatus') is not None:
            self.cert_status = m.get('CertStatus')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('ExclusiveVipStatus') is not None:
            self.exclusive_vip_status = m.get('ExclusiveVipStatus')
        if m.get('GSLBStatus') is not None:
            self.gslbstatus = m.get('GSLBStatus')
        if m.get('Http2Port') is not None:
            self.http_2port = m.get('Http2Port')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('Ipv6Status') is not None:
            self.ipv_6status = m.get('Ipv6Status')
        if m.get('ResolvedType') is not None:
            self.resolved_type = m.get('ResolvedType')
        if m.get('Rs') is not None:
            self.rs = m.get('Rs')
        if m.get('VipServiceStatus') is not None:
            self.vip_service_status = m.get('VipServiceStatus')
        return self


class DescribeDomainAdvanceConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(
        self,
        domain: str = None,
        profile: DescribeDomainAdvanceConfigsResponseBodyDomainConfigsProfile = None,
    ):
        self.domain = domain
        self.profile = profile

    def validate(self):
        if self.profile:
            self.profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.profile is not None:
            result['Profile'] = self.profile.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Profile') is not None:
            temp_model = DescribeDomainAdvanceConfigsResponseBodyDomainConfigsProfile()
            self.profile = temp_model.from_map(m['Profile'])
        return self


class DescribeDomainAdvanceConfigsResponseBody(TeaModel):
    def __init__(
        self,
        domain_configs: List[DescribeDomainAdvanceConfigsResponseBodyDomainConfigs] = None,
        request_id: str = None,
    ):
        self.domain_configs = domain_configs
        self.request_id = request_id

    def validate(self):
        if self.domain_configs:
            for k in self.domain_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfigs'] = []
        if self.domain_configs is not None:
            for k in self.domain_configs:
                result['DomainConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_configs = []
        if m.get('DomainConfigs') is not None:
            for k in m.get('DomainConfigs'):
                temp_model = DescribeDomainAdvanceConfigsResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainAdvanceConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainAdvanceConfigsResponseBody = None,
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
            temp_model = DescribeDomainAdvanceConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainBasicConfigsRequest(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        cloud_native_product_id: int = None,
        domain_key: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.access_type = access_type
        self.cloud_native_product_id = cloud_native_product_id
        self.domain_key = domain_key
        # This parameter is required.
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.cloud_native_product_id is not None:
            result['CloudNativeProductId'] = self.cloud_native_product_id
        if self.domain_key is not None:
            result['DomainKey'] = self.domain_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('CloudNativeProductId') is not None:
            self.cloud_native_product_id = m.get('CloudNativeProductId')
        if m.get('DomainKey') is not None:
            self.domain_key = m.get('DomainKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDomainBasicConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        acl_status: int = None,
        cc_mode: int = None,
        cc_status: int = None,
        domain: str = None,
        owner: str = None,
        status: int = None,
        version: int = None,
        waf_mode: int = None,
        waf_status: int = None,
    ):
        self.access_type = access_type
        self.acl_status = acl_status
        self.cc_mode = cc_mode
        self.cc_status = cc_status
        self.domain = domain
        self.owner = owner
        self.status = status
        self.version = version
        self.waf_mode = waf_mode
        self.waf_status = waf_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.cc_mode is not None:
            result['CcMode'] = self.cc_mode
        if self.cc_status is not None:
            result['CcStatus'] = self.cc_status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        if self.waf_mode is not None:
            result['WafMode'] = self.waf_mode
        if self.waf_status is not None:
            result['WafStatus'] = self.waf_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('CcMode') is not None:
            self.cc_mode = m.get('CcMode')
        if m.get('CcStatus') is not None:
            self.cc_status = m.get('CcStatus')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WafMode') is not None:
            self.waf_mode = m.get('WafMode')
        if m.get('WafStatus') is not None:
            self.waf_status = m.get('WafStatus')
        return self


class DescribeDomainBasicConfigsResponseBody(TeaModel):
    def __init__(
        self,
        domain_configs: List[DescribeDomainBasicConfigsResponseBodyDomainConfigs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.domain_configs = domain_configs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.domain_configs:
            for k in self.domain_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfigs'] = []
        if self.domain_configs is not None:
            for k in self.domain_configs:
                result['DomainConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_configs = []
        if m.get('DomainConfigs') is not None:
            for k in m.get('DomainConfigs'):
                temp_model = DescribeDomainBasicConfigsResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDomainBasicConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainBasicConfigsResponseBody = None,
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
            temp_model = DescribeDomainBasicConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainListRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_names: List[str] = None,
        instance_id: str = None,
        is_sub: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.domain_name = domain_name
        self.domain_names = domain_names
        # This parameter is required.
        self.instance_id = instance_id
        self.is_sub = is_sub
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_sub is not None:
            result['IsSub'] = self.is_sub
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSub') is not None:
            self.is_sub = m.get('IsSub')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDomainListResponseBody(TeaModel):
    def __init__(
        self,
        domain_names: List[str] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.domain_names = domain_names
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDomainListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainListResponseBody = None,
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
            temp_model = DescribeDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainNamesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDomainNamesResponseBody(TeaModel):
    def __init__(
        self,
        domain_names: List[str] = None,
        request_id: str = None,
    ):
        self.domain_names = domain_names
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainNamesResponseBody = None,
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
            temp_model = DescribeDomainNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRuleGroupRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDomainRuleGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rule_group_id: int = None,
        waf_ai_status: int = None,
    ):
        self.request_id = request_id
        self.rule_group_id = rule_group_id
        self.waf_ai_status = waf_ai_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_group_id is not None:
            result['RuleGroupId'] = self.rule_group_id
        if self.waf_ai_status is not None:
            result['WafAiStatus'] = self.waf_ai_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleGroupId') is not None:
            self.rule_group_id = m.get('RuleGroupId')
        if m.get('WafAiStatus') is not None:
            self.waf_ai_status = m.get('WafAiStatus')
        return self


class DescribeDomainRuleGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRuleGroupResponseBody = None,
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
            temp_model = DescribeDomainRuleGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the WAF instance.
        # 
        # If you do not configure this parameter, all WAF instances in the Chinese mainland or all WAF instances outside the Chinese mainland are queried.
        self.instance_id = instance_id
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the resource group to which the WAF instance belongs in Resource Management. If you do not configure this parameter, the WAF instance belongs to the default resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceInfoResponseBodyInstanceInfo(TeaModel):
    def __init__(
        self,
        end_date: int = None,
        in_debt: int = None,
        instance_id: str = None,
        pay_type: int = None,
        region: str = None,
        remain_day: int = None,
        status: int = None,
        subscription_type: str = None,
        trial: int = None,
        version: str = None,
    ):
        # The expiration time of the WAF instance. This value is a UNIX timestamp. Unit: seconds.
        # 
        # >  If the value of **PayType** is **0**, this parameter is not returned. The value 0 indicates that no WAF instances are purchased.
        self.end_date = end_date
        # Indicates whether the WAF instance has overdue payments. Valid values:
        # 
        # *   **0**: The instance has overdue payments.
        # *   **1**: The instance does not have overdue payments.
        # 
        # >  If the value of **PayType** is **0**, this parameter is not returned. The value 0 indicates that no WAF instances are purchased.
        self.in_debt = in_debt
        # The ID of the WAF instance.
        # 
        # >  If the value of **PayType** is **0**, this parameter is not returned. The value 0 indicates that no WAF instances are purchased.
        self.instance_id = instance_id
        # The activation status of WAF. Valid values:
        # 
        # *   **0**: No WAF instances are purchased within the Alibaba Cloud account.
        # *   **1**: A subscription WAF instance is purchased within the Alibaba Cloud account.
        self.pay_type = pay_type
        # The region in which the WAF instance resides. Valid values:
        # 
        # *   **cn**: a region in the Chinese mainland
        # *   **cn-hongkong**: a region outside the Chinese mainland
        # 
        # >  If the value of **PayType** is **0**, this parameter is not returned. The value 0 indicates that no WAF instances are purchased.
        self.region = region
        # The number of remaining days before the trial period of the WAF instance ends.
        # 
        # >  This parameter is returned only if the value of **Trial** is **1**. The value 1 indicates that the free trial of a WAF instance is activated.
        self.remain_day = remain_day
        # Indicates whether the WAF instance expires. Valid values:
        # 
        # *   **0**: The instance expires.
        # *   **1**: The instance does not expire.
        # 
        # >  If the value of **PayType** is **0**, this parameter is not returned. The value 0 indicates that no WAF instances are purchased.
        self.status = status
        # The billing method of the WAF instance: The value is fixed as **Subscription**.
        # 
        # >  If the value of **PayType** is **0**, this parameter is not returned. The value 0 indicates that no WAF instances are purchased.
        self.subscription_type = subscription_type
        # Indicates whether a WAF instance of the free trial edition is activated within the Alibaba Cloud account. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        # 
        # >  This parameter is returned only if a WAF instance of the free trial edition is activated within the Alibaba Cloud account.
        self.trial = trial
        # The edition of the WAF instance. Valid values:
        # 
        # *   **version_pro_china**: a WAF Pro instance in the Chinese mainland
        # *   **version_business_china**: a WAF Business instance in the Chinese mainland
        # *   **version_enterprise_china**: a WAF Enterprise instance in the Chinese mainland
        # *   **version_exclusive_china**: a WAF Exclusive instance in the Chinese mainland
        # *   **version_hybrid_cloud_standard_china**: a Hybrid Cloud WAF instance in the Chinese mainland
        # *   **version_pro_china**: a WAF Pro instance outside the Chinese mainland
        # *   **version_business**: a WAF Business instance outside the Chinese mainland
        # *   **version_enterprise**: a WAF Enterprise instance outside the Chinese mainland
        # *   **version_exclusive**: a WAF Exclusive instance outside the Chinese mainland
        # *   **version_hybrid_cloud_standard**: a Hybrid Cloud WAF instance outside the Chinese mainland
        # 
        # The preceding list contains all the editions of WAF instances within accounts that are created at the International site. If the returned version is not in the list, check whether your account is created at the International site.
        # 
        # >  If the value of **PayType** is **0**, this parameter is not returned. The value 0 indicates that no WAF instances are purchased.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region is not None:
            result['Region'] = self.region
        if self.remain_day is not None:
            result['RemainDay'] = self.remain_day
        if self.status is not None:
            result['Status'] = self.status
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.trial is not None:
            result['Trial'] = self.trial
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RemainDay') is not None:
            self.remain_day = m.get('RemainDay')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Trial') is not None:
            self.trial = m.get('Trial')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeInstanceInfoResponseBody(TeaModel):
    def __init__(
        self,
        instance_info: DescribeInstanceInfoResponseBodyInstanceInfo = None,
        request_id: str = None,
    ):
        # The information about the WAF instance.
        self.instance_info = instance_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_info:
            self.instance_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceInfo') is not None:
            temp_model = DescribeInstanceInfoResponseBodyInstanceInfo()
            self.instance_info = temp_model.from_map(m['InstanceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceInfoResponseBody = None,
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
            temp_model = DescribeInstanceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceSpecInfoResponseBodyInstanceSpecInfos(TeaModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        self.code = code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeInstanceSpecInfoResponseBody(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        instance_id: str = None,
        instance_spec_infos: List[DescribeInstanceSpecInfoResponseBodyInstanceSpecInfos] = None,
        request_id: str = None,
        version: str = None,
    ):
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_spec_infos = instance_spec_infos
        self.request_id = request_id
        self.version = version

    def validate(self):
        if self.instance_spec_infos:
            for k in self.instance_spec_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['InstanceSpecInfos'] = []
        if self.instance_spec_infos is not None:
            for k in self.instance_spec_infos:
                result['InstanceSpecInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.instance_spec_infos = []
        if m.get('InstanceSpecInfos') is not None:
            for k in m.get('InstanceSpecInfos'):
                temp_model = DescribeInstanceSpecInfoResponseBodyInstanceSpecInfos()
                self.instance_spec_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeInstanceSpecInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceSpecInfoResponseBody = None,
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
            temp_model = DescribeInstanceSpecInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogServiceStatusRequest(TeaModel):
    def __init__(
        self,
        domain_names: List[str] = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.domain_names = domain_names
        # This parameter is required.
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region = region
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeLogServiceStatusResponseBodyDomainStatus(TeaModel):
    def __init__(
        self,
        domain: str = None,
        sls_log_active: int = None,
    ):
        self.domain = domain
        self.sls_log_active = sls_log_active

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.sls_log_active is not None:
            result['SlsLogActive'] = self.sls_log_active
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SlsLogActive') is not None:
            self.sls_log_active = m.get('SlsLogActive')
        return self


class DescribeLogServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        domain_status: List[DescribeLogServiceStatusResponseBodyDomainStatus] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.domain_status = domain_status
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.domain_status:
            for k in self.domain_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainStatus'] = []
        if self.domain_status is not None:
            for k in self.domain_status:
                result['DomainStatus'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_status = []
        if m.get('DomainStatus') is not None:
            for k in m.get('DomainStatus'):
                temp_model = DescribeLogServiceStatusResponseBodyDomainStatus()
                self.domain_status.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeLogServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLogServiceStatusResponseBody = None,
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
            temp_model = DescribeLogServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtectionModuleCodeConfigRequest(TeaModel):
    def __init__(
        self,
        code_type: int = None,
        code_value: int = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.code_type = code_type
        self.code_value = code_value
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_type is not None:
            result['CodeType'] = self.code_type
        if self.code_value is not None:
            result['CodeValue'] = self.code_value
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeType') is not None:
            self.code_type = m.get('CodeType')
        if m.get('CodeValue') is not None:
            self.code_value = m.get('CodeValue')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeProtectionModuleCodeConfigResponseBody(TeaModel):
    def __init__(
        self,
        code_configs: str = None,
        request_id: str = None,
    ):
        self.code_configs = code_configs
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_configs is not None:
            result['CodeConfigs'] = self.code_configs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeConfigs') is not None:
            self.code_configs = m.get('CodeConfigs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProtectionModuleCodeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProtectionModuleCodeConfigResponseBody = None,
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
            temp_model = DescribeProtectionModuleCodeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtectionModuleModeRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.defense_type = defense_type
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeProtectionModuleModeResponseBody(TeaModel):
    def __init__(
        self,
        mode: int = None,
        request_id: str = None,
    ):
        self.mode = mode
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProtectionModuleModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProtectionModuleModeResponseBody = None,
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
            temp_model = DescribeProtectionModuleModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtectionModuleRulesRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.defense_type = defense_type
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.query = query
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeProtectionModuleRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        rule_id: int = None,
        status: int = None,
        time: int = None,
        version: int = None,
    ):
        self.content = content
        self.rule_id = rule_id
        self.status = status
        self.time = time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.status is not None:
            result['Status'] = self.status
        if self.time is not None:
            result['Time'] = self.time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeProtectionModuleRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rules: List[DescribeProtectionModuleRulesResponseBodyRules] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.rules = rules
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeProtectionModuleRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeProtectionModuleRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProtectionModuleRulesResponseBody = None,
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
            temp_model = DescribeProtectionModuleRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtectionModuleStatusRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.defense_type = defense_type
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeProtectionModuleStatusResponseBody(TeaModel):
    def __init__(
        self,
        module_status: int = None,
        request_id: str = None,
    ):
        self.module_status = module_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_status is not None:
            result['ModuleStatus'] = self.module_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleStatus') is not None:
            self.module_status = m.get('ModuleStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProtectionModuleStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProtectionModuleStatusResponseBody = None,
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
            temp_model = DescribeProtectionModuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRuleGroupsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: str = None,
        lang: str = None,
        page_size: int = None,
        policy_id: int = None,
        region: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
        type: int = None,
        waf_lang: str = None,
    ):
        self.current_page = current_page
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        self.page_size = page_size
        self.policy_id = policy_id
        self.region = region
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip
        self.type = type
        self.waf_lang = waf_lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        if self.waf_lang is not None:
            result['WafLang'] = self.waf_lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WafLang') is not None:
            self.waf_lang = m.get('WafLang')
        return self


class DescribeRuleGroupsResponseBodyRuleGroups(TeaModel):
    def __init__(
        self,
        desc: str = None,
        domain_list: List[str] = None,
        name: str = None,
        policy_id: int = None,
        rule_cnt: int = None,
        rule_group_template_name: str = None,
        rule_group_update_time: int = None,
        template_policy_id: int = None,
        type: int = None,
        waf_version: int = None,
    ):
        self.desc = desc
        self.domain_list = domain_list
        self.name = name
        self.policy_id = policy_id
        self.rule_cnt = rule_cnt
        self.rule_group_template_name = rule_group_template_name
        self.rule_group_update_time = rule_group_update_time
        self.template_policy_id = template_policy_id
        self.type = type
        self.waf_version = waf_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.rule_cnt is not None:
            result['RuleCnt'] = self.rule_cnt
        if self.rule_group_template_name is not None:
            result['RuleGroupTemplateName'] = self.rule_group_template_name
        if self.rule_group_update_time is not None:
            result['RuleGroupUpdateTime'] = self.rule_group_update_time
        if self.template_policy_id is not None:
            result['TemplatePolicyId'] = self.template_policy_id
        if self.type is not None:
            result['Type'] = self.type
        if self.waf_version is not None:
            result['WafVersion'] = self.waf_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RuleCnt') is not None:
            self.rule_cnt = m.get('RuleCnt')
        if m.get('RuleGroupTemplateName') is not None:
            self.rule_group_template_name = m.get('RuleGroupTemplateName')
        if m.get('RuleGroupUpdateTime') is not None:
            self.rule_group_update_time = m.get('RuleGroupUpdateTime')
        if m.get('TemplatePolicyId') is not None:
            self.template_policy_id = m.get('TemplatePolicyId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WafVersion') is not None:
            self.waf_version = m.get('WafVersion')
        return self


class DescribeRuleGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rule_groups: List[DescribeRuleGroupsResponseBodyRuleGroups] = None,
        task_status: int = None,
        total: int = None,
        waf_task_id: str = None,
    ):
        self.request_id = request_id
        self.rule_groups = rule_groups
        self.task_status = task_status
        self.total = total
        self.waf_task_id = waf_task_id

    def validate(self):
        if self.rule_groups:
            for k in self.rule_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleGroups'] = []
        if self.rule_groups is not None:
            for k in self.rule_groups:
                result['RuleGroups'].append(k.to_map() if k else None)
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.total is not None:
            result['Total'] = self.total
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_groups = []
        if m.get('RuleGroups') is not None:
            for k in m.get('RuleGroups'):
                temp_model = DescribeRuleGroupsResponseBodyRuleGroups()
                self.rule_groups.append(temp_model.from_map(k))
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
        return self


class DescribeRuleGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRuleGroupsResponseBody = None,
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
            temp_model = DescribeRuleGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRulesRequest(TeaModel):
    def __init__(
        self,
        application_type: int = None,
        cve_id_key: str = None,
        instance_id: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        protection_type: int = None,
        region: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        risk_level: int = None,
        rule_group_id: int = None,
        rule_id_key: str = None,
        source_ip: str = None,
    ):
        self.application_type = application_type
        # CVE ID
        self.cve_id_key = cve_id_key
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.protection_type = protection_type
        self.region = region
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.risk_level = risk_level
        # This parameter is required.
        self.rule_group_id = rule_group_id
        self.rule_id_key = rule_id_key
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.cve_id_key is not None:
            result['CveIdKey'] = self.cve_id_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.protection_type is not None:
            result['ProtectionType'] = self.protection_type
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.rule_group_id is not None:
            result['RuleGroupId'] = self.rule_group_id
        if self.rule_id_key is not None:
            result['RuleIdKey'] = self.rule_id_key
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CveIdKey') is not None:
            self.cve_id_key = m.get('CveIdKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProtectionType') is not None:
            self.protection_type = m.get('ProtectionType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RuleGroupId') is not None:
            self.rule_group_id = m.get('RuleGroupId')
        if m.get('RuleIdKey') is not None:
            self.rule_id_key = m.get('RuleIdKey')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        application_type: int = None,
        cve_id: str = None,
        cve_url: str = None,
        description: str = None,
        protection_type: int = None,
        risk_level: int = None,
        rule_id: int = None,
        rule_name: str = None,
        update_time: int = None,
    ):
        self.application_type = application_type
        # CVE ID。
        self.cve_id = cve_id
        self.cve_url = cve_url
        self.description = description
        self.protection_type = protection_type
        self.risk_level = risk_level
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.cve_id is not None:
            result['CveId'] = self.cve_id
        if self.cve_url is not None:
            result['CveUrl'] = self.cve_url
        if self.description is not None:
            result['Description'] = self.description
        if self.protection_type is not None:
            result['ProtectionType'] = self.protection_type
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')
        if m.get('CveUrl') is not None:
            self.cve_url = m.get('CveUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProtectionType') is not None:
            self.protection_type = m.get('ProtectionType')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeRulesResponseBody(TeaModel):
    def __init__(
        self,
        is_subscribe: int = None,
        request_id: str = None,
        rule_group_name: str = None,
        rule_group_template_id: str = None,
        rule_group_template_name: str = None,
        rules: List[DescribeRulesResponseBodyRules] = None,
        total_count: int = None,
    ):
        self.is_subscribe = is_subscribe
        self.request_id = request_id
        self.rule_group_name = rule_group_name
        self.rule_group_template_id = rule_group_template_id
        self.rule_group_template_name = rule_group_template_name
        self.rules = rules
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
        if self.is_subscribe is not None:
            result['IsSubscribe'] = self.is_subscribe
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_group_name is not None:
            result['RuleGroupName'] = self.rule_group_name
        if self.rule_group_template_id is not None:
            result['RuleGroupTemplateId'] = self.rule_group_template_id
        if self.rule_group_template_name is not None:
            result['RuleGroupTemplateName'] = self.rule_group_template_name
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSubscribe') is not None:
            self.is_subscribe = m.get('IsSubscribe')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleGroupName') is not None:
            self.rule_group_name = m.get('RuleGroupName')
        if m.get('RuleGroupTemplateId') is not None:
            self.rule_group_template_id = m.get('RuleGroupTemplateId')
        if m.get('RuleGroupTemplateName') is not None:
            self.rule_group_template_name = m.get('RuleGroupTemplateName')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRulesResponseBody = None,
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
            temp_model = DescribeRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWafSourceIpSegmentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWafSourceIpSegmentResponseBody(TeaModel):
    def __init__(
        self,
        ip_v6s: str = None,
        ips: str = None,
        request_id: str = None,
    ):
        self.ip_v6s = ip_v6s
        self.ips = ips
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_v6s is not None:
            result['IpV6s'] = self.ip_v6s
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpV6s') is not None:
            self.ip_v6s = m.get('IpV6s')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWafSourceIpSegmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWafSourceIpSegmentResponseBody = None,
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
            temp_model = DescribeWafSourceIpSegmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainRequest(TeaModel):
    def __init__(
        self,
        access_header_mode: int = None,
        access_headers: str = None,
        access_type: str = None,
        cloud_native_instances: str = None,
        cluster_type: int = None,
        connection_time: int = None,
        domain: str = None,
        http_2port: str = None,
        http_port: str = None,
        http_to_user_ip: int = None,
        https_port: str = None,
        https_redirect: int = None,
        instance_id: str = None,
        ip_follow_status: int = None,
        is_access_product: int = None,
        keepalive: bool = None,
        keepalive_requests: int = None,
        keepalive_timeout: int = None,
        load_balancing: int = None,
        log_headers: str = None,
        read_time: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        retry: bool = None,
        sni_host: str = None,
        sni_status: int = None,
        source_ips: str = None,
        write_time: int = None,
    ):
        # The method that WAF uses to obtain the actual IP address of a client. Valid values:
        # 
        # *   **0**: WAF reads the first value of the X-Forwarded-For (XFF) header field as the actual IP address of the client. This is the default value.
        # *   **1**: WAF reads the value of a custom header field as the actual IP address of the client.
        # 
        # >  You need to specify the parameter only when the **IsAccessProduct** parameter is set to **1**.
        self.access_header_mode = access_header_mode
        # The custom header fields that are used to obtain the actual IP address of a client. Specify the value in the `["header1","header2",...]` format.
        # 
        # >  You need to specify the parameter only when the **AccessHeaderMode** parameter is set to **1**.
        self.access_headers = access_headers
        # The mode that is used to add the domain name. Valid values:
        # 
        # *   **waf-cloud-dns**: CNAME record mode. This is the default value.
        # *   **waf-cloud-native**: transparent proxy mode.
        self.access_type = access_type
        # The list of server and port configurations for the transparent proxy mode. The value is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        # *   **ProtocolPortConfigs**: the list of protocol and port configurations. This field is required. Data type: array. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        #     *   **Ports**: the list of ports. This field is required. Data type: array. The value is in the `[port1,port2,……]` format.
        #     *   **Protocol**: the protocol. This field is required. Data type: string. Valid values: **http** and **https**.
        # 
        # *   **CloudNativeProductName**: the type of the cloud service instance. This field is required. Data type: string. Valid values: **ECS**, **SLB**, and **ALB**.
        # 
        # *   **RedirectionTypeName**: the type of traffic redirection port. This field is required. Data type: string. Valid values: **ECS**, **SLB-L4**, **SLB-L7**, and **ALB**.
        # 
        # *   **InstanceId**: the ID of the cloud service instance. This field is required. Data type: string.
        # 
        # *   **IPAddressList**: the list of public IP addresses of the cloud service instance. This field is required. Data type: array. The value is in the `["ip1","ip2",...]` format.
        # 
        # >  You need to specify the parameter only when the value of the **AccessType** parameter is set to **waf-cloud-native**.
        self.cloud_native_instances = cloud_native_instances
        # The type of WAF protection cluster. Valid values:
        # 
        # *   **0**: shared cluster. This is the default value.
        # *   **1**: exclusive cluster.
        # 
        # >  You need to specify the parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns**.
        self.cluster_type = cluster_type
        # The timeout period for connections of WAF exclusive clusters. Unit: seconds.
        # 
        # >  You need to specify the parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns** and the value of the **ClusterType** parameter is set to **1**.
        self.connection_time = connection_time
        # The domain name whose configurations you want to modify.
        # 
        # >  You can call the [DescribeDomainNames](https://help.aliyun.com/document_detail/86373.html) operation to query the domain names that are added to Web Application Firewall (WAF).
        # 
        # This parameter is required.
        self.domain = domain
        # The HTTP/2 ports. Specify the value in the `["port1","port2",...]` format.
        # 
        # >  You need to specify this parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns** and the **HttpsPort** parameter is not empty. If the HttpsPort parameter is not empty, your website uses HTTPS.
        self.http_2port = http_2port
        # The HTTP ports. Specify the value in the `["port1","port2",...]` format.
        # 
        # >  You need to specify the parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns**. If you specify this parameter, your website uses HTTP. You must specify at least one of the **HttpPort** and **HttpsPort** parameters.
        self.http_port = http_port
        # Specifies whether to enable the feature of redirecting HTTPS requests to HTTP requests. If you enable the feature, HTTPS requests are redirected to HTTP requests on port 80, which is used by default. Valid values:
        # 
        # *   **0**: disables the feature. This is the default value.
        # *   **1**: enables the feature.
        # 
        # >  You need to specify this parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns** and the **HttpsPort** parameter is not empty. If the HttpsPort parameter is not empty, your website uses HTTPS.
        self.http_to_user_ip = http_to_user_ip
        # The HTTPS ports. Specify the value in the `["port1","port2",...]` format.
        # 
        # >  You need to specify the parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns**. If you specify this parameter, your website uses HTTPS. You must specify at least one of the **HttpPort** and **HttpsPort** parameters.
        self.https_port = https_port
        # Specifies whether to enable the feature of redirecting HTTP requests to HTTPS requests. If you enable the feature, HTTP requests are redirected to HTTPS requests on port 443, which is used by default. Valid values:
        # 
        # *   **0**: disables the feature. This is the default value.
        # *   **1**: enables the feature.
        # 
        # >  You need to specify this parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns** and the **HttpsPort** parameter is not empty. If the HttpsPort parameter is not empty, your website uses HTTPS.
        self.https_redirect = https_redirect
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstanceInfo](https://help.aliyun.com/document_detail/140857.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to enable the feature of forwarding requests to the origin servers that use the IP address type specified in the requests. If you enable the feature, WAF forwards requests from IPv4 addresses to origin servers that use IPv4 addresses and requests from IPv6 addresses to origin servers that use IPv6 addresses. Valid values:
        # 
        # *   **0**: disables the feature. This is the default value.
        # *   **1**: enables the feature.
        # 
        # >  You need to specify the parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns**.
        self.ip_follow_status = ip_follow_status
        # Specifies whether to deploy a Layer 7 proxy, which is used to filter inbound traffic before the traffic reaches the WAF instance. The supported Layer 7 proxies include Anti-DDoS Pro, Anti-DDoS Premium, and Alibaba Cloud CDN. Valid values:
        # 
        # *   **0**: does not configure a Layer 7 proxy
        # *   **1**: configures a Layer 7 proxy
        # 
        # This parameter is required.
        self.is_access_product = is_access_product
        self.keepalive = keepalive
        self.keepalive_requests = keepalive_requests
        self.keepalive_timeout = keepalive_timeout
        # The load balancing algorithm that is used when WAF forwards requests to the origin server. Valid values:
        # 
        # *   **0**: IP hash
        # *   **1**: round-robin
        # *   **2**: least time
        # 
        # >  You need to specify the parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns**.
        self.load_balancing = load_balancing
        # The key-value pair that is used to mark the requests that pass through the WAF instance.
        # 
        # Specify the key-value pair in the `[{"k":"_key_","v":"_value_"}]` format. `_key_` specifies a header field in a custom request. `_value_` specifies the value of the field.
        # 
        # WAF automatically adds the key-value pair to the headers of requests. This way, the requests that pass through WAF are identified.
        # 
        # >  If requests contain the custom header field, WAF overwrites the original value of the field with the specified value.
        self.log_headers = log_headers
        # The timeout period for read connections of WAF exclusive clusters. Unit: seconds.
        # 
        # >  You need to specify the parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns** and the value of the **ClusterType** parameter is set to **1**.
        self.read_time = read_time
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.retry = retry
        # The value of the custom SNI field. If this parameter is not specified, the value of the **Host** field in the request header is automatically used as the value of the SNI field.
        # 
        # If you want WAF to use an SNI field whose value is different from the value of the Host field, you can specify a custom value for the SNI field.
        # 
        # >  This parameter needs to be set only when the value of the **SniStatus** parameter is set to **1**.
        self.sni_host = sni_host
        # Specifies whether to enable origin SNI. Origin Server Name Indication (SNI) specifies the domain name to which an HTTPS connection needs to be established at the start of the TLS handshaking process when WAF forwards requests to the origin server. If the origin server hosts multiple domain names, you must enable this feature. Valid values:
        # 
        # *   **0**: disables origin SNI.
        # *   **1**: enables origin SNI.
        # 
        # By default, origin SNI is disabled for WAF instances in the Chinese mainland and enabled for WAF instances outside the Chinese mainland.
        # 
        # >  You need to specify this parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns** and the **HttpsPort** parameter is not empty. If the HttpsPort parameter is not empty, your website uses HTTPS.
        self.sni_status = sni_status
        # The address type of the origin server. The address can be an IP address or a domain name. You can specify only one type of address.
        # 
        # *   If you use the IP address type, specify the value in the `["ip1","ip2",...]` format. You can add up to 20 IP addresses.
        # *   If you use the domain name type, specify the value in the `["domain"]` format. You can enter only one domain name.
        # 
        # >  You need to specify the parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns**.
        self.source_ips = source_ips
        # The timeout period for write connections of WAF exclusive clusters. Unit: seconds.
        # 
        # >  You need to specify the parameter only when the value of the **AccessType** parameter is set to **waf-cloud-dns** and the value of the **ClusterType** parameter is set to **1**.
        self.write_time = write_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_header_mode is not None:
            result['AccessHeaderMode'] = self.access_header_mode
        if self.access_headers is not None:
            result['AccessHeaders'] = self.access_headers
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.cloud_native_instances is not None:
            result['CloudNativeInstances'] = self.cloud_native_instances
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.connection_time is not None:
            result['ConnectionTime'] = self.connection_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.http_2port is not None:
            result['Http2Port'] = self.http_2port
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.http_to_user_ip is not None:
            result['HttpToUserIp'] = self.http_to_user_ip
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.https_redirect is not None:
            result['HttpsRedirect'] = self.https_redirect
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_follow_status is not None:
            result['IpFollowStatus'] = self.ip_follow_status
        if self.is_access_product is not None:
            result['IsAccessProduct'] = self.is_access_product
        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive
        if self.keepalive_requests is not None:
            result['KeepaliveRequests'] = self.keepalive_requests
        if self.keepalive_timeout is not None:
            result['KeepaliveTimeout'] = self.keepalive_timeout
        if self.load_balancing is not None:
            result['LoadBalancing'] = self.load_balancing
        if self.log_headers is not None:
            result['LogHeaders'] = self.log_headers
        if self.read_time is not None:
            result['ReadTime'] = self.read_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.retry is not None:
            result['Retry'] = self.retry
        if self.sni_host is not None:
            result['SniHost'] = self.sni_host
        if self.sni_status is not None:
            result['SniStatus'] = self.sni_status
        if self.source_ips is not None:
            result['SourceIps'] = self.source_ips
        if self.write_time is not None:
            result['WriteTime'] = self.write_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessHeaderMode') is not None:
            self.access_header_mode = m.get('AccessHeaderMode')
        if m.get('AccessHeaders') is not None:
            self.access_headers = m.get('AccessHeaders')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('CloudNativeInstances') is not None:
            self.cloud_native_instances = m.get('CloudNativeInstances')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ConnectionTime') is not None:
            self.connection_time = m.get('ConnectionTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Http2Port') is not None:
            self.http_2port = m.get('Http2Port')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('HttpToUserIp') is not None:
            self.http_to_user_ip = m.get('HttpToUserIp')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('HttpsRedirect') is not None:
            self.https_redirect = m.get('HttpsRedirect')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpFollowStatus') is not None:
            self.ip_follow_status = m.get('IpFollowStatus')
        if m.get('IsAccessProduct') is not None:
            self.is_access_product = m.get('IsAccessProduct')
        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')
        if m.get('KeepaliveRequests') is not None:
            self.keepalive_requests = m.get('KeepaliveRequests')
        if m.get('KeepaliveTimeout') is not None:
            self.keepalive_timeout = m.get('KeepaliveTimeout')
        if m.get('LoadBalancing') is not None:
            self.load_balancing = m.get('LoadBalancing')
        if m.get('LogHeaders') is not None:
            self.log_headers = m.get('LogHeaders')
        if m.get('ReadTime') is not None:
            self.read_time = m.get('ReadTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Retry') is not None:
            self.retry = m.get('Retry')
        if m.get('SniHost') is not None:
            self.sni_host = m.get('SniHost')
        if m.get('SniStatus') is not None:
            self.sni_status = m.get('SniStatus')
        if m.get('SourceIps') is not None:
            self.source_ips = m.get('SourceIps')
        if m.get('WriteTime') is not None:
            self.write_time = m.get('WriteTime')
        return self


class ModifyDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDomainResponseBody = None,
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
            temp_model = ModifyDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainIpv6StatusRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.enabled = enabled
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyDomainIpv6StatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class ModifyDomainIpv6StatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDomainIpv6StatusResponseBody = None,
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
            temp_model = ModifyDomainIpv6StatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogRetrievalStatusRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: int = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.enabled = enabled
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyLogRetrievalStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class ModifyLogRetrievalStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyLogRetrievalStatusResponseBody = None,
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
            temp_model = ModifyLogRetrievalStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogServiceStatusRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: int = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.enabled = enabled
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyLogServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class ModifyLogServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyLogServiceStatusResponseBody = None,
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
            temp_model = ModifyLogServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtectionModuleModeRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        mode: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.defense_type = defense_type
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.mode = mode
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyProtectionModuleModeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class ModifyProtectionModuleModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyProtectionModuleModeResponseBody = None,
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
            temp_model = ModifyProtectionModuleModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtectionModuleRuleRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        lock_version: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        rule: str = None,
        rule_id: int = None,
    ):
        # This parameter is required.
        self.defense_type = defense_type
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.lock_version = lock_version
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.rule = rule
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lock_version is not None:
            result['LockVersion'] = self.lock_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LockVersion') is not None:
            self.lock_version = m.get('LockVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ModifyProtectionModuleRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class ModifyProtectionModuleRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyProtectionModuleRuleResponseBody = None,
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
            temp_model = ModifyProtectionModuleRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtectionModuleStatusRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        module_status: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.defense_type = defense_type
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.module_status = module_status
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_status is not None:
            result['ModuleStatus'] = self.module_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleStatus') is not None:
            self.module_status = m.get('ModuleStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyProtectionModuleStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class ModifyProtectionModuleStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyProtectionModuleStatusResponseBody = None,
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
            temp_model = ModifyProtectionModuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtectionRuleCacheStatusRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        rule_id: int = None,
    ):
        # This parameter is required.
        self.defense_type = defense_type
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ModifyProtectionRuleCacheStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class ModifyProtectionRuleCacheStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyProtectionRuleCacheStatusResponseBody = None,
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
            temp_model = ModifyProtectionRuleCacheStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtectionRuleStatusRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        lock_version: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        rule_id: int = None,
        rule_status: int = None,
    ):
        # This parameter is required.
        self.defense_type = defense_type
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.lock_version = lock_version
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.rule_id = rule_id
        # This parameter is required.
        self.rule_status = rule_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lock_version is not None:
            result['LockVersion'] = self.lock_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LockVersion') is not None:
            self.lock_version = m.get('LockVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')
        return self


class ModifyProtectionRuleStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class ModifyProtectionRuleStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyProtectionRuleStatusResponseBody = None,
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
            temp_model = ModifyProtectionRuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.region_id = region_id
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        status_code: int = None,
        body: MoveResourceGroupResponseBody = None,
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainRuleGroupRequest(TeaModel):
    def __init__(
        self,
        domains: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        rule_group_id: int = None,
        waf_ai_status: int = None,
        waf_version: int = None,
    ):
        # This parameter is required.
        self.domains = domains
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.rule_group_id = rule_group_id
        self.waf_ai_status = waf_ai_status
        self.waf_version = waf_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_group_id is not None:
            result['RuleGroupId'] = self.rule_group_id
        if self.waf_ai_status is not None:
            result['WafAiStatus'] = self.waf_ai_status
        if self.waf_version is not None:
            result['WafVersion'] = self.waf_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleGroupId') is not None:
            self.rule_group_id = m.get('RuleGroupId')
        if m.get('WafAiStatus') is not None:
            self.waf_ai_status = m.get('WafAiStatus')
        if m.get('WafVersion') is not None:
            self.waf_version = m.get('WafVersion')
        return self


class SetDomainRuleGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class SetDomainRuleGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDomainRuleGroupResponseBody = None,
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
            temp_model = SetDomainRuleGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


