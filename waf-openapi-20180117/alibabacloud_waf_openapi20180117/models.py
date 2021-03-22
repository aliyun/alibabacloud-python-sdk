# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateAclRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        rules: str = None,
        domain: str = None,
        instance_id: str = None,
        region: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.rules = rules
        self.domain = domain
        self.instance_id = instance_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class CreateAclRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: int = None,
        waf_task_id: str = None,
    ):
        self.status = status
        self.waf_task_id = waf_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
        return self


class CreateAclRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateAclRuleResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAclRuleResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAclRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAclRuleResponseBody = None,
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
            temp_model = CreateAclRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertAndKeyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        region: str = None,
        instance_id: str = None,
        cert: str = None,
        key: str = None,
        https_cert_name: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.region = region
        self.instance_id = instance_id
        self.cert = cert
        self.key = key
        self.https_cert_name = https_cert_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.key is not None:
            result['Key'] = self.key
        if self.https_cert_name is not None:
            result['HttpsCertName'] = self.https_cert_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('HttpsCertName') is not None:
            self.https_cert_name = m.get('HttpsCertName')
        return self


class CreateCertAndKeyResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: int = None,
        waf_task_id: str = None,
    ):
        self.status = status
        self.waf_task_id = waf_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
        return self


class CreateCertAndKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateCertAndKeyResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateCertAndKeyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateCertAndKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCertAndKeyResponseBody = None,
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
            temp_model = CreateCertAndKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        source_ips: str = None,
        http_port: str = None,
        https_port: str = None,
        instance_id: str = None,
        region: str = None,
        is_access_product: int = None,
        protocols: str = None,
        load_balancing: int = None,
        http_to_user_ip: int = None,
        https_redirect: int = None,
        rs_type: int = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.source_ips = source_ips
        self.http_port = http_port
        self.https_port = https_port
        self.instance_id = instance_id
        self.region = region
        self.is_access_product = is_access_product
        self.protocols = protocols
        self.load_balancing = load_balancing
        self.http_to_user_ip = http_to_user_ip
        self.https_redirect = https_redirect
        self.rs_type = rs_type
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.source_ips is not None:
            result['SourceIps'] = self.source_ips
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.is_access_product is not None:
            result['IsAccessProduct'] = self.is_access_product
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.load_balancing is not None:
            result['LoadBalancing'] = self.load_balancing
        if self.http_to_user_ip is not None:
            result['HttpToUserIp'] = self.http_to_user_ip
        if self.https_redirect is not None:
            result['HttpsRedirect'] = self.https_redirect
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SourceIps') is not None:
            self.source_ips = m.get('SourceIps')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IsAccessProduct') is not None:
            self.is_access_product = m.get('IsAccessProduct')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('LoadBalancing') is not None:
            self.load_balancing = m.get('LoadBalancing')
        if m.get('HttpToUserIp') is not None:
            self.http_to_user_ip = m.get('HttpToUserIp')
        if m.get('HttpsRedirect') is not None:
            self.https_redirect = m.get('HttpsRedirect')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateDomainConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: int = None,
        waf_task_id: str = None,
    ):
        self.status = status
        self.waf_task_id = waf_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
        return self


class CreateDomainConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateDomainConfigResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateDomainConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDomainConfigResponseBody = None,
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
            temp_model = CreateDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProtectionModuleRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        defense: str = None,
        rule: str = None,
        instance_id: str = None,
        region: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.defense = defense
        self.rule = rule
        self.instance_id = instance_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.defense is not None:
            result['Defense'] = self.defense
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Defense') is not None:
            self.defense = m.get('Defense')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
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


class DeleteAclRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        rule_id: int = None,
        domain: str = None,
        instance_id: str = None,
        region: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.rule_id = rule_id
        self.domain = domain
        self.instance_id = instance_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DeleteAclRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: int = None,
        waf_task_id: str = None,
    ):
        self.status = status
        self.waf_task_id = waf_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
        return self


class DeleteAclRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DeleteAclRuleResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteAclRuleResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteAclRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAclRuleResponseBody = None,
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
            temp_model = DeleteAclRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        instance_id: str = None,
        region: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.instance_id = instance_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DeleteDomainConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: int = None,
        waf_task_id: str = None,
    ):
        self.status = status
        self.waf_task_id = waf_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
        return self


class DeleteDomainConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DeleteDomainConfigResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteDomainConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDomainConfigResponseBody = None,
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
            temp_model = DeleteDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAclRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        region: str = None,
        instance_id: str = None,
        domain: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.region = region
        self.instance_id = instance_id
        self.domain = domain
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAclRulesResponseBodyResultAclRulesAclRuleConditionsCondition(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        contain: str = None,
    ):
        self.key = key
        self.value = value
        self.contain = contain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.contain is not None:
            result['Contain'] = self.contain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Contain') is not None:
            self.contain = m.get('Contain')
        return self


class DescribeAclRulesResponseBodyResultAclRulesAclRuleConditions(TeaModel):
    def __init__(
        self,
        condition: List[DescribeAclRulesResponseBodyResultAclRulesAclRuleConditionsCondition] = None,
    ):
        self.condition = condition

    def validate(self):
        if self.condition:
            for k in self.condition:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['condition'] = []
        if self.condition is not None:
            for k in self.condition:
                result['condition'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition = []
        if m.get('condition') is not None:
            for k in m.get('condition'):
                temp_model = DescribeAclRulesResponseBodyResultAclRulesAclRuleConditionsCondition()
                self.condition.append(temp_model.from_map(k))
        return self


class DescribeAclRulesResponseBodyResultAclRulesAclRule(TeaModel):
    def __init__(
        self,
        action: int = None,
        is_default: int = None,
        continue_waf: int = None,
        order: int = None,
        conditions: DescribeAclRulesResponseBodyResultAclRulesAclRuleConditions = None,
        continue_data_risk_control: int = None,
        continue_sdk: int = None,
        continue_cc: int = None,
        continue_sa: int = None,
        continue_block_geo: int = None,
        name: str = None,
        id: int = None,
    ):
        self.action = action
        self.is_default = is_default
        self.continue_waf = continue_waf
        self.order = order
        self.conditions = conditions
        self.continue_data_risk_control = continue_data_risk_control
        self.continue_sdk = continue_sdk
        self.continue_cc = continue_cc
        self.continue_sa = continue_sa
        self.continue_block_geo = continue_block_geo
        self.name = name
        self.id = id

    def validate(self):
        if self.conditions:
            self.conditions.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.continue_waf is not None:
            result['ContinueWaf'] = self.continue_waf
        if self.order is not None:
            result['Order'] = self.order
        if self.conditions is not None:
            result['Conditions'] = self.conditions.to_map()
        if self.continue_data_risk_control is not None:
            result['ContinueDataRiskControl'] = self.continue_data_risk_control
        if self.continue_sdk is not None:
            result['ContinueSdk'] = self.continue_sdk
        if self.continue_cc is not None:
            result['ContinueCc'] = self.continue_cc
        if self.continue_sa is not None:
            result['ContinueSA'] = self.continue_sa
        if self.continue_block_geo is not None:
            result['ContinueBlockGeo'] = self.continue_block_geo
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('ContinueWaf') is not None:
            self.continue_waf = m.get('ContinueWaf')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Conditions') is not None:
            temp_model = DescribeAclRulesResponseBodyResultAclRulesAclRuleConditions()
            self.conditions = temp_model.from_map(m['Conditions'])
        if m.get('ContinueDataRiskControl') is not None:
            self.continue_data_risk_control = m.get('ContinueDataRiskControl')
        if m.get('ContinueSdk') is not None:
            self.continue_sdk = m.get('ContinueSdk')
        if m.get('ContinueCc') is not None:
            self.continue_cc = m.get('ContinueCc')
        if m.get('ContinueSA') is not None:
            self.continue_sa = m.get('ContinueSA')
        if m.get('ContinueBlockGeo') is not None:
            self.continue_block_geo = m.get('ContinueBlockGeo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeAclRulesResponseBodyResultAclRules(TeaModel):
    def __init__(
        self,
        acl_rule: List[DescribeAclRulesResponseBodyResultAclRulesAclRule] = None,
    ):
        self.acl_rule = acl_rule

    def validate(self):
        if self.acl_rule:
            for k in self.acl_rule:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AclRule'] = []
        if self.acl_rule is not None:
            for k in self.acl_rule:
                result['AclRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_rule = []
        if m.get('AclRule') is not None:
            for k in m.get('AclRule'):
                temp_model = DescribeAclRulesResponseBodyResultAclRulesAclRule()
                self.acl_rule.append(temp_model.from_map(k))
        return self


class DescribeAclRulesResponseBodyResult(TeaModel):
    def __init__(
        self,
        acl_rules: DescribeAclRulesResponseBodyResultAclRules = None,
        total: int = None,
    ):
        self.acl_rules = acl_rules
        self.total = total

    def validate(self):
        if self.acl_rules:
            self.acl_rules.validate()

    def to_map(self):
        result = dict()
        if self.acl_rules is not None:
            result['AclRules'] = self.acl_rules.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclRules') is not None:
            temp_model = DescribeAclRulesResponseBodyResultAclRules()
            self.acl_rules = temp_model.from_map(m['AclRules'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAclRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAclRulesResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAclRulesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAclRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAclRulesResponseBody = None,
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
            temp_model = DescribeAclRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAsyncTaskStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        region: str = None,
        instance_id: str = None,
        waf_request_id: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.region = region
        self.instance_id = instance_id
        self.waf_request_id = waf_request_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.waf_request_id is not None:
            result['WafRequestId'] = self.waf_request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('WafRequestId') is not None:
            self.waf_request_id = m.get('WafRequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeAsyncTaskStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        progress: int = None,
        err_code: str = None,
        err_msg: str = None,
        async_task_status: str = None,
    ):
        self.data = data
        self.progress = progress
        self.err_code = err_code
        self.err_msg = err_msg
        self.async_task_status = async_task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.async_task_status is not None:
            result['AsyncTaskStatus'] = self.async_task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('AsyncTaskStatus') is not None:
            self.async_task_status = m.get('AsyncTaskStatus')
        return self


class DescribeAsyncTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAsyncTaskStatusResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAsyncTaskStatusResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAsyncTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAsyncTaskStatusResponseBody = None,
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
            temp_model = DescribeAsyncTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        region: str = None,
        instance_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.region = region
        self.instance_id = instance_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainConfigResponseBodyResultDomainConfig(TeaModel):
    def __init__(
        self,
        cname: str = None,
        protocol_type: int = None,
        source_ips: str = None,
    ):
        self.cname = cname
        self.protocol_type = protocol_type
        self.source_ips = source_ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.source_ips is not None:
            result['SourceIps'] = self.source_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('SourceIps') is not None:
            self.source_ips = m.get('SourceIps')
        return self


class DescribeDomainConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: int = None,
        waf_task_id: str = None,
        domain_config: DescribeDomainConfigResponseBodyResultDomainConfig = None,
    ):
        self.status = status
        self.waf_task_id = waf_task_id
        self.domain_config = domain_config

    def validate(self):
        if self.domain_config:
            self.domain_config.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        if self.domain_config is not None:
            result['DomainConfig'] = self.domain_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
        if m.get('DomainConfig') is not None:
            temp_model = DescribeDomainConfigResponseBodyResultDomainConfig()
            self.domain_config = temp_model.from_map(m['DomainConfig'])
        return self


class DescribeDomainConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeDomainConfigResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeDomainConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainConfigResponseBody = None,
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
            temp_model = DescribeDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainConfigStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        region: str = None,
        instance_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.region = region
        self.instance_id = instance_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainConfigStatusResponseBodyResultDomainConfig(TeaModel):
    def __init__(
        self,
        config_status: str = None,
    ):
        self.config_status = config_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')
        return self


class DescribeDomainConfigStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: int = None,
        waf_task_id: str = None,
        domain_config: DescribeDomainConfigStatusResponseBodyResultDomainConfig = None,
    ):
        self.status = status
        self.waf_task_id = waf_task_id
        self.domain_config = domain_config

    def validate(self):
        if self.domain_config:
            self.domain_config.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        if self.domain_config is not None:
            result['DomainConfig'] = self.domain_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
        if m.get('DomainConfig') is not None:
            temp_model = DescribeDomainConfigStatusResponseBodyResultDomainConfig()
            self.domain_config = temp_model.from_map(m['DomainConfig'])
        return self


class DescribeDomainConfigStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeDomainConfigStatusResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeDomainConfigStatusResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeDomainConfigStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainConfigStatusResponseBody = None,
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
            temp_model = DescribeDomainConfigStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainNamesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        region: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.region = region
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDomainNamesResponseBodyResult(TeaModel):
    def __init__(
        self,
        domain_names: List[str] = None,
    ):
        self.domain_names = domain_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        return self


class DescribeDomainNamesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeDomainNamesResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeDomainNamesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
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


class DescribePayInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        region: str = None,
        instance_source: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.region = region
        self.instance_source = instance_source
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribePayInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: int = None,
        end_date: int = None,
        remain_day: int = None,
        region: str = None,
        pay_type: int = None,
        in_debt: int = None,
        instance_id: str = None,
        trial: int = None,
    ):
        self.status = status
        self.end_date = end_date
        self.remain_day = remain_day
        self.region = region
        self.pay_type = pay_type
        self.in_debt = in_debt
        self.instance_id = instance_id
        self.trial = trial

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.remain_day is not None:
            result['RemainDay'] = self.remain_day
        if self.region is not None:
            result['Region'] = self.region
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.trial is not None:
            result['Trial'] = self.trial
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('RemainDay') is not None:
            self.remain_day = m.get('RemainDay')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Trial') is not None:
            self.trial = m.get('Trial')
        return self


class DescribePayInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribePayInfoResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribePayInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribePayInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePayInfoResponseBody = None,
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
            temp_model = DescribePayInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtectionModuleRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        page_size: int = None,
        current_page: int = None,
        domain: str = None,
        defense: str = None,
        instance_id: str = None,
        region: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.page_size = page_size
        self.current_page = current_page
        self.domain = domain
        self.defense = defense
        self.instance_id = instance_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.defense is not None:
            result['Defense'] = self.defense
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Defense') is not None:
            self.defense = m.get('Defense')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeProtectionModuleRulesResponseBodyModuleRules(TeaModel):
    def __init__(
        self,
        time: int = None,
        version: int = None,
        content: str = None,
        id: int = None,
    ):
        self.time = time
        self.version = version
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.version is not None:
            result['Version'] = self.version
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeProtectionModuleRulesResponseBody(TeaModel):
    def __init__(
        self,
        module_rules: List[DescribeProtectionModuleRulesResponseBodyModuleRules] = None,
        request_id: str = None,
        total: int = None,
        task_status: int = None,
    ):
        self.module_rules = module_rules
        self.request_id = request_id
        self.total = total
        self.task_status = task_status

    def validate(self):
        if self.module_rules:
            for k in self.module_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ModuleRules'] = []
        if self.module_rules is not None:
            for k in self.module_rules:
                result['ModuleRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_rules = []
        if m.get('ModuleRules') is not None:
            for k in m.get('ModuleRules'):
                temp_model = DescribeProtectionModuleRulesResponseBodyModuleRules()
                self.module_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
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


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        region: str = None,
        display: str = None,
    ):
        self.region = region
        self.display = display

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.display is not None:
            result['Display'] = self.display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
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


class DescribeWafSourceIpSegmentRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id: str = None,
        region: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id = instance_id
        self.region = region
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWafSourceIpSegmentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ips: str = None,
    ):
        self.request_id = request_id
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ips is not None:
            result['Ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
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


class ModifyAclRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        rules: str = None,
        instance_id: str = None,
        region: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.rules = rules
        self.instance_id = instance_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ModifyAclRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: int = None,
        waf_task_id: str = None,
    ):
        self.status = status
        self.waf_task_id = waf_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
        return self


class ModifyAclRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifyAclRuleResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ModifyAclRuleResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ModifyAclRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAclRuleResponseBody = None,
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
            temp_model = ModifyAclRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        source_ips: str = None,
        http_port: str = None,
        https_port: str = None,
        instance_id: str = None,
        region: str = None,
        is_access_product: int = None,
        protocols: str = None,
        load_balancing: int = None,
        http_to_user_ip: int = None,
        https_redirect: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.source_ips = source_ips
        self.http_port = http_port
        self.https_port = https_port
        self.instance_id = instance_id
        self.region = region
        self.is_access_product = is_access_product
        self.protocols = protocols
        self.load_balancing = load_balancing
        self.http_to_user_ip = http_to_user_ip
        self.https_redirect = https_redirect

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.source_ips is not None:
            result['SourceIps'] = self.source_ips
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.is_access_product is not None:
            result['IsAccessProduct'] = self.is_access_product
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.load_balancing is not None:
            result['LoadBalancing'] = self.load_balancing
        if self.http_to_user_ip is not None:
            result['HttpToUserIp'] = self.http_to_user_ip
        if self.https_redirect is not None:
            result['HttpsRedirect'] = self.https_redirect
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SourceIps') is not None:
            self.source_ips = m.get('SourceIps')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IsAccessProduct') is not None:
            self.is_access_product = m.get('IsAccessProduct')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('LoadBalancing') is not None:
            self.load_balancing = m.get('LoadBalancing')
        if m.get('HttpToUserIp') is not None:
            self.http_to_user_ip = m.get('HttpToUserIp')
        if m.get('HttpsRedirect') is not None:
            self.https_redirect = m.get('HttpsRedirect')
        return self


class ModifyDomainConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: int = None,
        waf_task_id: str = None,
    ):
        self.status = status
        self.waf_task_id = waf_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
        return self


class ModifyDomainConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifyDomainConfigResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ModifyDomainConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ModifyDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDomainConfigResponseBody = None,
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
            temp_model = ModifyDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtectionRuleCacheStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        id: int = None,
        defense: str = None,
        instance_id: str = None,
        region: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.id = id
        self.defense = defense
        self.instance_id = instance_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.id is not None:
            result['Id'] = self.id
        if self.defense is not None:
            result['Defense'] = self.defense
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Defense') is not None:
            self.defense = m.get('Defense')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ModifyProtectionRuleCacheStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_status: int = None,
        waf_task_id: int = None,
    ):
        self.request_id = request_id
        self.task_status = task_status
        self.waf_task_id = waf_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
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
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        defense: str = None,
        id: int = None,
        rule_status: int = None,
        lock_version: int = None,
        instance_id: str = None,
        region: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.defense = defense
        self.id = id
        self.rule_status = rule_status
        self.lock_version = lock_version
        self.instance_id = instance_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.defense is not None:
            result['Defense'] = self.defense
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status
        if self.lock_version is not None:
            result['LockVersion'] = self.lock_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Defense') is not None:
            self.defense = m.get('Defense')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')
        if m.get('LockVersion') is not None:
            self.lock_version = m.get('LockVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ModifyProtectionRuleStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_status: int = None,
        waf_task_id: int = None,
    ):
        self.request_id = request_id
        self.task_status = task_status
        self.waf_task_id = waf_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
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


class ModifyWafSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        region: str = None,
        domain: str = None,
        instance_id: str = None,
        service_on: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.region = region
        self.domain = domain
        self.instance_id = instance_id
        self.service_on = service_on

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region is not None:
            result['Region'] = self.region
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.service_on is not None:
            result['ServiceOn'] = self.service_on
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ServiceOn') is not None:
            self.service_on = m.get('ServiceOn')
        return self


class ModifyWafSwitchResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: int = None,
        waf_task_id: str = None,
    ):
        self.status = status
        self.waf_task_id = waf_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_task_id is not None:
            result['WafTaskId'] = self.waf_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafTaskId') is not None:
            self.waf_task_id = m.get('WafTaskId')
        return self


class ModifyWafSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifyWafSwitchResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ModifyWafSwitchResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ModifyWafSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWafSwitchResponseBody = None,
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
            temp_model = ModifyWafSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


