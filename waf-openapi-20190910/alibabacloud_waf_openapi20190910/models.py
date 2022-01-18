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
    ):
        self.certificate = certificate
        self.certificate_name = certificate_name
        self.domain = domain
        self.instance_id = instance_id
        self.private_key = private_key

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
        body: CreateCertificateResponseBody = None,
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
            temp_model = CreateCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateByCertificateIdRequest(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        domain: str = None,
        instance_id: str = None,
    ):
        self.certificate_id = certificate_id
        self.domain = domain
        self.instance_id = instance_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        body: CreateCertificateByCertificateIdResponseBody = None,
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
        load_balancing: int = None,
        log_headers: str = None,
        read_time: int = None,
        resource_group_id: str = None,
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
        self.domain = domain
        self.http_2port = http_2port
        self.http_port = http_port
        self.http_to_user_ip = http_to_user_ip
        self.https_port = https_port
        self.https_redirect = https_redirect
        self.instance_id = instance_id
        self.ip_follow_status = ip_follow_status
        self.is_access_product = is_access_product
        self.load_balancing = load_balancing
        self.log_headers = log_headers
        self.read_time = read_time
        self.resource_group_id = resource_group_id
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
        if self.load_balancing is not None:
            result['LoadBalancing'] = self.load_balancing
        if self.log_headers is not None:
            result['LogHeaders'] = self.log_headers
        if self.read_time is not None:
            result['ReadTime'] = self.read_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('LoadBalancing') is not None:
            self.load_balancing = m.get('LoadBalancing')
        if m.get('LogHeaders') is not None:
            self.log_headers = m.get('LogHeaders')
        if m.get('ReadTime') is not None:
            self.read_time = m.get('ReadTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        body: CreateDomainResponseBody = None,
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
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProtectionModuleRuleRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        rule: str = None,
    ):
        self.defense_type = defense_type
        self.domain = domain
        self.instance_id = instance_id
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
        body: CreateProtectionModuleRuleResponseBody = None,
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
            temp_model = CreateProtectionModuleRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
    ):
        self.domain = domain
        self.instance_id = instance_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        body: DeleteDomainResponseBody = None,
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
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_group_id: str = None,
    ):
        self.instance_id = instance_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class DeleteProtectionModuleRuleRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        rule_id: int = None,
    ):
        self.defense_type = defense_type
        self.domain = domain
        self.instance_id = instance_id
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
        body: DeleteProtectionModuleRuleResponseBody = None,
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
    ):
        self.certificate = certificate
        self.domain = domain
        self.instance_id = instance_id
        self.private_key = private_key

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
        body: DescribeCertMatchStatusResponseBody = None,
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
            temp_model = DescribeCertMatchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificatesRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
    ):
        self.domain = domain
        self.instance_id = instance_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeCertificatesResponseBodyCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        certificate_name: str = None,
        common_name: str = None,
        is_using: bool = None,
        sans: List[str] = None,
    ):
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name
        self.common_name = common_name
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
        body: DescribeCertificatesResponseBody = None,
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
            temp_model = DescribeCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
    ):
        self.domain = domain
        self.instance_id = instance_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeDomainResponseBodyDomainCloudNativeInstancesProtocolPortConfigs(TeaModel):
    def __init__(
        self,
        ports: str = None,
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
        ipaddress_list: str = None,
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
        http_2port: List[str] = None,
        http_port: List[str] = None,
        http_to_user_ip: int = None,
        https_port: List[str] = None,
        https_redirect: int = None,
        ip_follow_status: int = None,
        is_access_product: int = None,
        load_balancing: int = None,
        log_headers: List[DescribeDomainResponseBodyDomainLogHeaders] = None,
        read_time: int = None,
        resource_group_id: str = None,
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
        self.load_balancing = load_balancing
        self.log_headers = log_headers
        self.read_time = read_time
        self.resource_group_id = resource_group_id
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
        body: DescribeDomainResponseBody = None,
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
            temp_model = DescribeDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAdvanceConfigsRequest(TeaModel):
    def __init__(
        self,
        domain_list: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
    ):
        self.domain_list = domain_list
        self.instance_id = instance_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        body: DescribeDomainAdvanceConfigsResponseBody = None,
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
        resource_group_id: str = None,
    ):
        self.access_type = access_type
        self.cloud_native_product_id = cloud_native_product_id
        self.domain_key = domain_key
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
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
        body: DescribeDomainBasicConfigsResponseBody = None,
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
        resource_group_id: str = None,
    ):
        self.domain_name = domain_name
        self.domain_names = domain_names
        self.instance_id = instance_id
        self.is_sub = is_sub
        self.page_number = page_number
        self.page_size = page_size
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
        body: DescribeDomainListResponseBody = None,
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
            temp_model = DescribeDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainNamesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_group_id: str = None,
    ):
        self.instance_id = instance_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        body: DescribeDomainNamesResponseBody = None,
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
            temp_model = DescribeDomainNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRuleGroupRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
    ):
        self.domain = domain
        self.instance_id = instance_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        body: DescribeDomainRuleGroupResponseBody = None,
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
            temp_model = DescribeDomainRuleGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_group_id: str = None,
    ):
        self.instance_id = instance_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        self.end_date = end_date
        self.in_debt = in_debt
        self.instance_id = instance_id
        self.pay_type = pay_type
        self.region = region
        self.remain_day = remain_day
        self.status = status
        self.subscription_type = subscription_type
        self.trial = trial
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
        self.instance_info = instance_info
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
        body: DescribeInstanceInfoResponseBody = None,
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
            temp_model = DescribeInstanceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_group_id: str = None,
    ):
        self.instance_id = instance_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        body: DescribeInstanceSpecInfoResponseBody = None,
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
        resource_group_id: str = None,
    ):
        self.domain_names = domain_names
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region = region
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
        body: DescribeLogServiceStatusResponseBody = None,
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
            temp_model = DescribeLogServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtectionModuleCodeConfigRequest(TeaModel):
    def __init__(
        self,
        code_type: int = None,
        code_value: int = None,
        instance_id: str = None,
        resource_group_id: str = None,
    ):
        self.code_type = code_type
        self.code_value = code_value
        self.instance_id = instance_id
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
        body: DescribeProtectionModuleCodeConfigResponseBody = None,
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
            temp_model = DescribeProtectionModuleCodeConfigResponseBody()
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
        resource_group_id: str = None,
    ):
        self.defense_type = defense_type
        self.domain = domain
        self.instance_id = instance_id
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.query = query
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
        body: DescribeProtectionModuleRulesResponseBody = None,
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
            temp_model = DescribeProtectionModuleRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtectionModuleStatusRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
    ):
        self.defense_type = defense_type
        self.domain = domain
        self.instance_id = instance_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        body: DescribeProtectionModuleStatusResponseBody = None,
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
            temp_model = DescribeProtectionModuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWafSourceIpSegmentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_group_id: str = None,
    ):
        self.instance_id = instance_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        body: DescribeWafSourceIpSegmentResponseBody = None,
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
        load_balancing: int = None,
        log_headers: str = None,
        read_time: int = None,
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
        self.domain = domain
        self.http_2port = http_2port
        self.http_port = http_port
        self.http_to_user_ip = http_to_user_ip
        self.https_port = https_port
        self.https_redirect = https_redirect
        self.instance_id = instance_id
        self.ip_follow_status = ip_follow_status
        self.is_access_product = is_access_product
        self.load_balancing = load_balancing
        self.log_headers = log_headers
        self.read_time = read_time
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
        if self.load_balancing is not None:
            result['LoadBalancing'] = self.load_balancing
        if self.log_headers is not None:
            result['LogHeaders'] = self.log_headers
        if self.read_time is not None:
            result['ReadTime'] = self.read_time
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
        if m.get('LoadBalancing') is not None:
            self.load_balancing = m.get('LoadBalancing')
        if m.get('LogHeaders') is not None:
            self.log_headers = m.get('LogHeaders')
        if m.get('ReadTime') is not None:
            self.read_time = m.get('ReadTime')
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
        body: ModifyDomainResponseBody = None,
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
            temp_model = ModifyDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainIpv6StatusRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: str = None,
        instance_id: str = None,
    ):
        self.domain = domain
        self.enabled = enabled
        self.instance_id = instance_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        body: ModifyDomainIpv6StatusResponseBody = None,
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
            temp_model = ModifyDomainIpv6StatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogRetrievalStatusRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: int = None,
        instance_id: str = None,
    ):
        self.domain = domain
        self.enabled = enabled
        self.instance_id = instance_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        body: ModifyLogRetrievalStatusResponseBody = None,
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
            temp_model = ModifyLogRetrievalStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogServiceStatusRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: int = None,
        instance_id: str = None,
    ):
        self.domain = domain
        self.enabled = enabled
        self.instance_id = instance_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        body: ModifyLogServiceStatusResponseBody = None,
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
    ):
        self.defense_type = defense_type
        self.domain = domain
        self.instance_id = instance_id
        self.mode = mode

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
        body: ModifyProtectionModuleModeResponseBody = None,
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
        rule: str = None,
        rule_id: int = None,
    ):
        self.defense_type = defense_type
        self.domain = domain
        self.instance_id = instance_id
        self.lock_version = lock_version
        self.rule = rule
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
        body: ModifyProtectionModuleRuleResponseBody = None,
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
    ):
        self.defense_type = defense_type
        self.domain = domain
        self.instance_id = instance_id
        self.module_status = module_status

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
        body: ModifyProtectionModuleStatusResponseBody = None,
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
            temp_model = ModifyProtectionModuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtectionRuleCacheStatusRequest(TeaModel):
    def __init__(
        self,
        defense_type: str = None,
        domain: str = None,
        instance_id: str = None,
        rule_id: int = None,
    ):
        self.defense_type = defense_type
        self.domain = domain
        self.instance_id = instance_id
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
        body: ModifyProtectionRuleCacheStatusResponseBody = None,
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
        rule_id: int = None,
        rule_status: int = None,
    ):
        self.defense_type = defense_type
        self.domain = domain
        self.instance_id = instance_id
        self.lock_version = lock_version
        self.rule_id = rule_id
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
        body: ModifyProtectionRuleStatusResponseBody = None,
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
            temp_model = ModifyProtectionRuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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


class SetDomainRuleGroupRequest(TeaModel):
    def __init__(
        self,
        domains: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
        rule_group_id: int = None,
        waf_ai_status: int = None,
        waf_version: int = None,
    ):
        self.domains = domains
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id
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
        body: SetDomainRuleGroupResponseBody = None,
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
            temp_model = SetDomainRuleGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


