# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddAutoCcBlacklistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        blacklist: str = None,
        expire_time: int = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.blacklist = blacklist
        self.expire_time = expire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.blacklist is not None:
            result['Blacklist'] = self.blacklist
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Blacklist') is not None:
            self.blacklist = m.get('Blacklist')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class AddAutoCcBlacklistResponseBody(TeaModel):
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


class AddAutoCcBlacklistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAutoCcBlacklistResponseBody = None,
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
            temp_model = AddAutoCcBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddAutoCcWhitelistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        whitelist: str = None,
        expire_time: int = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.whitelist = whitelist
        self.expire_time = expire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class AddAutoCcWhitelistResponseBody(TeaModel):
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


class AddAutoCcWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAutoCcWhitelistResponseBody = None,
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
            temp_model = AddAutoCcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateWebCertRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        cert_id: int = None,
        cert_name: str = None,
        cert: str = None,
        key: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.cert_id = cert_id
        self.cert_name = cert_name
        self.cert = cert
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class AssociateWebCertResponseBody(TeaModel):
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


class AssociateWebCertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateWebCertResponseBody = None,
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
            temp_model = AssociateWebCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachSceneDefenseObjectRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        policy_id: str = None,
        object_type: str = None,
        objects: str = None,
    ):
        self.source_ip = source_ip
        self.policy_id = policy_id
        self.object_type = object_type
        self.objects = objects

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.objects is not None:
            result['Objects'] = self.objects
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Objects') is not None:
            self.objects = m.get('Objects')
        return self


class AttachSceneDefenseObjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AttachSceneDefenseObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachSceneDefenseObjectResponseBody = None,
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
            temp_model = AttachSceneDefenseObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigL7RsPolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        policy: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class ConfigL7RsPolicyResponseBody(TeaModel):
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


class ConfigL7RsPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigL7RsPolicyResponseBody = None,
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
            temp_model = ConfigL7RsPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigNetworkRegionBlockRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        config: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ConfigNetworkRegionBlockResponseBody(TeaModel):
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


class ConfigNetworkRegionBlockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigNetworkRegionBlockResponseBody = None,
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
            temp_model = ConfigNetworkRegionBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigNetworkRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        network_rules: str = None,
    ):
        self.source_ip = source_ip
        self.network_rules = network_rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class ConfigNetworkRulesResponseBody(TeaModel):
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


class ConfigNetworkRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigNetworkRulesResponseBody = None,
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
            temp_model = ConfigNetworkRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigWebCCTemplateRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        template: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class ConfigWebCCTemplateResponseBody(TeaModel):
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


class ConfigWebCCTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigWebCCTemplateResponseBody = None,
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
            temp_model = ConfigWebCCTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigWebIpSetRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        black_list: List[str] = None,
        white_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.black_list = black_list
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class ConfigWebIpSetResponseBody(TeaModel):
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


class ConfigWebIpSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigWebIpSetResponseBody = None,
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
            temp_model = ConfigWebIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        task_type: int = None,
        task_params: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.task_type = task_type
        self.task_params = task_params

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
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        return self


class CreateAsyncTaskResponseBody(TeaModel):
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


class CreateAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAsyncTaskResponseBody = None,
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
            temp_model = CreateAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetworkRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        network_rules: str = None,
    ):
        self.source_ip = source_ip
        self.network_rules = network_rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class CreateNetworkRulesResponseBody(TeaModel):
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


class CreateNetworkRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNetworkRulesResponseBody = None,
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
            temp_model = CreateNetworkRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSceneDefensePolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        name: str = None,
        template: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.name = name
        self.template = template
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.template is not None:
            result['Template'] = self.template
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class CreateSceneDefensePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSceneDefensePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSceneDefensePolicyResponseBody = None,
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
            temp_model = CreateSceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSchedulerRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        rules: str = None,
        rule_name: str = None,
        rule_type: int = None,
        param: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.rules = rules
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.param = param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.param is not None:
            result['Param'] = self.param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        return self


class CreateSchedulerRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cname: str = None,
        rule_name: str = None,
    ):
        self.request_id = request_id
        self.cname = cname
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class CreateSchedulerRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSchedulerRuleResponseBody = None,
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
            temp_model = CreateSchedulerRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagResourcesRequestTags(TeaModel):
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


class CreateTagResourcesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        resource_ids: List[str] = None,
        tags: List[CreateTagResourcesRequestTags] = None,
    ):
        self.source_ip = source_ip
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.resource_ids = resource_ids
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateTagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateTagResourcesResponseBody(TeaModel):
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


class CreateTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTagResourcesResponseBody = None,
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
            temp_model = CreateTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebCCRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        name: str = None,
        act: str = None,
        count: int = None,
        interval: int = None,
        mode: str = None,
        ttl: int = None,
        uri: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.name = name
        self.act = act
        self.count = count
        self.interval = interval
        self.mode = mode
        self.ttl = ttl
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateWebCCRuleResponseBody(TeaModel):
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


class CreateWebCCRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateWebCCRuleResponseBody = None,
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
            temp_model = CreateWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        rs_type: int = None,
        rules: str = None,
        https_ext: str = None,
        defense_id: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.rs_type = rs_type
        self.rules = rules
        self.https_ext = https_ext
        self.defense_id = defense_id
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext
        if self.defense_id is not None:
            result['DefenseId'] = self.defense_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')
        if m.get('DefenseId') is not None:
            self.defense_id = m.get('DefenseId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class CreateWebRuleResponseBody(TeaModel):
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


class CreateWebRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateWebRuleResponseBody = None,
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
            temp_model = CreateWebRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        task_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteAsyncTaskResponseBody(TeaModel):
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


class DeleteAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAsyncTaskResponseBody = None,
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
            temp_model = DeleteAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoCcBlacklistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        blacklist: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.blacklist = blacklist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.blacklist is not None:
            result['Blacklist'] = self.blacklist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Blacklist') is not None:
            self.blacklist = m.get('Blacklist')
        return self


class DeleteAutoCcBlacklistResponseBody(TeaModel):
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


class DeleteAutoCcBlacklistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAutoCcBlacklistResponseBody = None,
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
            temp_model = DeleteAutoCcBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoCcWhitelistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        whitelist: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class DeleteAutoCcWhitelistResponseBody(TeaModel):
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


class DeleteAutoCcWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAutoCcWhitelistResponseBody = None,
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
            temp_model = DeleteAutoCcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetworkRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        network_rule: str = None,
    ):
        self.source_ip = source_ip
        self.network_rule = network_rule

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.network_rule is not None:
            result['NetworkRule'] = self.network_rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('NetworkRule') is not None:
            self.network_rule = m.get('NetworkRule')
        return self


class DeleteNetworkRuleResponseBody(TeaModel):
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


class DeleteNetworkRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNetworkRuleResponseBody = None,
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
            temp_model = DeleteNetworkRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSceneDefensePolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        policy_id: str = None,
    ):
        self.source_ip = source_ip
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DeleteSceneDefensePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSceneDefensePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSceneDefensePolicyResponseBody = None,
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
            temp_model = DeleteSceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSchedulerRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        rule_name: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DeleteSchedulerRuleResponseBody(TeaModel):
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


class DeleteSchedulerRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSchedulerRuleResponseBody = None,
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
            temp_model = DeleteSchedulerRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagResourcesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_ids: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.source_ip = source_ip
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.all = all
        self.resource_ids = resource_ids
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DeleteTagResourcesResponseBody(TeaModel):
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


class DeleteTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTagResourcesResponseBody = None,
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
            temp_model = DeleteTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebCacheCustomRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        rule_names: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.rule_names = rule_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rule_names is not None:
            result['RuleNames'] = self.rule_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RuleNames') is not None:
            self.rule_names = m.get('RuleNames')
        return self


class DeleteWebCacheCustomRuleResponseBody(TeaModel):
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


class DeleteWebCacheCustomRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteWebCacheCustomRuleResponseBody = None,
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
            temp_model = DeleteWebCacheCustomRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebCCRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        name: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteWebCCRuleResponseBody(TeaModel):
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


class DeleteWebCCRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteWebCCRuleResponseBody = None,
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
            temp_model = DeleteWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebPreciseAccessRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        rule_names: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.rule_names = rule_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rule_names is not None:
            result['RuleNames'] = self.rule_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RuleNames') is not None:
            self.rule_names = m.get('RuleNames')
        return self


class DeleteWebPreciseAccessRuleResponseBody(TeaModel):
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


class DeleteWebPreciseAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteWebPreciseAccessRuleResponseBody = None,
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
            temp_model = DeleteWebPreciseAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DeleteWebRuleResponseBody(TeaModel):
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


class DeleteWebRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteWebRuleResponseBody = None,
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
            temp_model = DeleteWebRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAsyncTasksRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.page_number = page_number
        self.page_size = page_size

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAsyncTasksResponseBodyAsyncTasks(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        task_type: int = None,
        start_time: int = None,
        task_params: str = None,
        task_status: int = None,
        task_result: str = None,
        task_id: int = None,
    ):
        self.end_time = end_time
        self.task_type = task_type
        self.start_time = start_time
        self.task_params = task_params
        self.task_status = task_status
        self.task_result = task_result
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeAsyncTasksResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        async_tasks: List[DescribeAsyncTasksResponseBodyAsyncTasks] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.async_tasks = async_tasks

    def validate(self):
        if self.async_tasks:
            for k in self.async_tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AsyncTasks'] = []
        if self.async_tasks is not None:
            for k in self.async_tasks:
                result['AsyncTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.async_tasks = []
        if m.get('AsyncTasks') is not None:
            for k in m.get('AsyncTasks'):
                temp_model = DescribeAsyncTasksResponseBodyAsyncTasks()
                self.async_tasks.append(temp_model.from_map(k))
        return self


class DescribeAsyncTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAsyncTasksResponseBody = None,
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
            temp_model = DescribeAsyncTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoCcBlacklistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        key_word: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.key_word = key_word
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAutoCcBlacklistResponseBodyAutoCcBlacklist(TeaModel):
    def __init__(
        self,
        type: str = None,
        end_time: int = None,
        source_ip: str = None,
        dest_ip: str = None,
    ):
        self.type = type
        self.end_time = end_time
        self.source_ip = source_ip
        self.dest_ip = dest_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.dest_ip is not None:
            result['DestIp'] = self.dest_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('DestIp') is not None:
            self.dest_ip = m.get('DestIp')
        return self


class DescribeAutoCcBlacklistResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        auto_cc_blacklist: List[DescribeAutoCcBlacklistResponseBodyAutoCcBlacklist] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.auto_cc_blacklist = auto_cc_blacklist

    def validate(self):
        if self.auto_cc_blacklist:
            for k in self.auto_cc_blacklist:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AutoCcBlacklist'] = []
        if self.auto_cc_blacklist is not None:
            for k in self.auto_cc_blacklist:
                result['AutoCcBlacklist'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.auto_cc_blacklist = []
        if m.get('AutoCcBlacklist') is not None:
            for k in m.get('AutoCcBlacklist'):
                temp_model = DescribeAutoCcBlacklistResponseBodyAutoCcBlacklist()
                self.auto_cc_blacklist.append(temp_model.from_map(k))
        return self


class DescribeAutoCcBlacklistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAutoCcBlacklistResponseBody = None,
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
            temp_model = DescribeAutoCcBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoCcListCountRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        query_type: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.query_type = query_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        return self


class DescribeAutoCcListCountResponseBody(TeaModel):
    def __init__(
        self,
        black_count: int = None,
        request_id: str = None,
        white_count: int = None,
    ):
        self.black_count = black_count
        self.request_id = request_id
        self.white_count = white_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.black_count is not None:
            result['BlackCount'] = self.black_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.white_count is not None:
            result['WhiteCount'] = self.white_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackCount') is not None:
            self.black_count = m.get('BlackCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WhiteCount') is not None:
            self.white_count = m.get('WhiteCount')
        return self


class DescribeAutoCcListCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAutoCcListCountResponseBody = None,
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
            temp_model = DescribeAutoCcListCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoCcWhitelistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        key_word: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.key_word = key_word
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAutoCcWhitelistResponseBodyAutoCcWhitelist(TeaModel):
    def __init__(
        self,
        type: str = None,
        end_time: int = None,
        source_ip: str = None,
        dest_ip: str = None,
    ):
        self.type = type
        self.end_time = end_time
        self.source_ip = source_ip
        self.dest_ip = dest_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.dest_ip is not None:
            result['DestIp'] = self.dest_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('DestIp') is not None:
            self.dest_ip = m.get('DestIp')
        return self


class DescribeAutoCcWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        auto_cc_whitelist: List[DescribeAutoCcWhitelistResponseBodyAutoCcWhitelist] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.auto_cc_whitelist = auto_cc_whitelist
        self.total_count = total_count
        self.request_id = request_id

    def validate(self):
        if self.auto_cc_whitelist:
            for k in self.auto_cc_whitelist:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AutoCcWhitelist'] = []
        if self.auto_cc_whitelist is not None:
            for k in self.auto_cc_whitelist:
                result['AutoCcWhitelist'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_cc_whitelist = []
        if m.get('AutoCcWhitelist') is not None:
            for k in m.get('AutoCcWhitelist'):
                temp_model = DescribeAutoCcWhitelistResponseBodyAutoCcWhitelist()
                self.auto_cc_whitelist.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAutoCcWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAutoCcWhitelistResponseBody = None,
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
            temp_model = DescribeAutoCcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackSourceCidrRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        line: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.line = line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class DescribeBackSourceCidrResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cidrs: List[str] = None,
    ):
        self.request_id = request_id
        self.cidrs = cidrs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        return self


class DescribeBackSourceCidrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackSourceCidrResponseBody = None,
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
            temp_model = DescribeBackSourceCidrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlackholeStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeBlackholeStatusResponseBodyBlackholeStatus(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        ip: str = None,
        black_status: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.ip = ip
        self.black_status = black_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.black_status is not None:
            result['BlackStatus'] = self.black_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('BlackStatus') is not None:
            self.black_status = m.get('BlackStatus')
        return self


class DescribeBlackholeStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        blackhole_status: List[DescribeBlackholeStatusResponseBodyBlackholeStatus] = None,
    ):
        self.request_id = request_id
        self.blackhole_status = blackhole_status

    def validate(self):
        if self.blackhole_status:
            for k in self.blackhole_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['BlackholeStatus'] = []
        if self.blackhole_status is not None:
            for k in self.blackhole_status:
                result['BlackholeStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.blackhole_status = []
        if m.get('BlackholeStatus') is not None:
            for k in m.get('BlackholeStatus'):
                temp_model = DescribeBlackholeStatusResponseBodyBlackholeStatus()
                self.blackhole_status.append(temp_model.from_map(k))
        return self


class DescribeBlackholeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBlackholeStatusResponseBody = None,
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
            temp_model = DescribeBlackholeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlockStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.instance_ids = instance_ids

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
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeBlockStatusResponseBodyStatusListBlockStatusList(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        line: str = None,
        block_status: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.line = line
        self.block_status = block_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.line is not None:
            result['Line'] = self.line
        if self.block_status is not None:
            result['BlockStatus'] = self.block_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('BlockStatus') is not None:
            self.block_status = m.get('BlockStatus')
        return self


class DescribeBlockStatusResponseBodyStatusList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        block_status_list: List[DescribeBlockStatusResponseBodyStatusListBlockStatusList] = None,
    ):
        self.ip = ip
        self.block_status_list = block_status_list

    def validate(self):
        if self.block_status_list:
            for k in self.block_status_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        result['BlockStatusList'] = []
        if self.block_status_list is not None:
            for k in self.block_status_list:
                result['BlockStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        self.block_status_list = []
        if m.get('BlockStatusList') is not None:
            for k in m.get('BlockStatusList'):
                temp_model = DescribeBlockStatusResponseBodyStatusListBlockStatusList()
                self.block_status_list.append(temp_model.from_map(k))
        return self


class DescribeBlockStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status_list: List[DescribeBlockStatusResponseBodyStatusList] = None,
    ):
        self.request_id = request_id
        self.status_list = status_list

    def validate(self):
        if self.status_list:
            for k in self.status_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatusList'] = []
        if self.status_list is not None:
            for k in self.status_list:
                result['StatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.status_list = []
        if m.get('StatusList') is not None:
            for k in m.get('StatusList'):
                temp_model = DescribeBlockStatusResponseBodyStatusList()
                self.status_list.append(temp_model.from_map(k))
        return self


class DescribeBlockStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBlockStatusResponseBody = None,
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
            temp_model = DescribeBlockStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeCertsResponseBodyCerts(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        domain_related: bool = None,
        start_date: str = None,
        issuer: str = None,
        name: str = None,
        common: str = None,
        id: int = None,
    ):
        self.end_date = end_date
        self.domain_related = domain_related
        self.start_date = start_date
        self.issuer = issuer
        self.name = name
        self.common = common
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.domain_related is not None:
            result['DomainRelated'] = self.domain_related
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.name is not None:
            result['Name'] = self.name
        if self.common is not None:
            result['Common'] = self.common
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('DomainRelated') is not None:
            self.domain_related = m.get('DomainRelated')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeCertsResponseBody(TeaModel):
    def __init__(
        self,
        certs: List[DescribeCertsResponseBodyCerts] = None,
        request_id: str = None,
    ):
        self.certs = certs
        self.request_id = request_id

    def validate(self):
        if self.certs:
            for k in self.certs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Certs'] = []
        if self.certs is not None:
            for k in self.certs:
                result['Certs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certs = []
        if m.get('Certs') is not None:
            for k in m.get('Certs'):
                temp_model = DescribeCertsResponseBodyCerts()
                self.certs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCertsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCertsResponseBody = None,
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
            temp_model = DescribeCertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCnameReusesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domains: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domains = domains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeCnameReusesResponseBodyCnameReuses(TeaModel):
    def __init__(
        self,
        domain: str = None,
        cname: str = None,
        enable: int = None,
    ):
        self.domain = domain
        self.cname = cname
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeCnameReusesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cname_reuses: List[DescribeCnameReusesResponseBodyCnameReuses] = None,
    ):
        self.request_id = request_id
        self.cname_reuses = cname_reuses

    def validate(self):
        if self.cname_reuses:
            for k in self.cname_reuses:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CnameReuses'] = []
        if self.cname_reuses is not None:
            for k in self.cname_reuses:
                result['CnameReuses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.cname_reuses = []
        if m.get('CnameReuses') is not None:
            for k in m.get('CnameReuses'):
                temp_model = DescribeCnameReusesResponseBodyCnameReuses()
                self.cname_reuses.append(temp_model.from_map(k))
        return self


class DescribeCnameReusesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCnameReusesResponseBody = None,
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
            temp_model = DescribeCnameReusesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosAllEventListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        event_type: str = None,
        start_time: int = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.event_type = event_type
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDDosAllEventListResponseBodyAttackEvents(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        event_type: str = None,
        mbps: int = None,
        ip: str = None,
        port: str = None,
        pps: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.event_type = event_type
        self.mbps = mbps
        self.ip = ip
        self.port = port
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeDDosAllEventListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        attack_events: List[DescribeDDosAllEventListResponseBodyAttackEvents] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.attack_events = attack_events

    def validate(self):
        if self.attack_events:
            for k in self.attack_events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['AttackEvents'] = []
        if self.attack_events is not None:
            for k in self.attack_events:
                result['AttackEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.attack_events = []
        if m.get('AttackEvents') is not None:
            for k in m.get('AttackEvents'):
                temp_model = DescribeDDosAllEventListResponseBodyAttackEvents()
                self.attack_events.append(temp_model.from_map(k))
        return self


class DescribeDDosAllEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDDosAllEventListResponseBody = None,
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
            temp_model = DescribeDDosAllEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventAreaRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        event_type: str = None,
        start_time: int = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.event_type = event_type
        self.start_time = start_time
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDDosEventAreaResponseBodyAreas(TeaModel):
    def __init__(
        self,
        in_pkts: int = None,
        area: str = None,
    ):
        self.in_pkts = in_pkts
        self.area = area

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.in_pkts is not None:
            result['InPkts'] = self.in_pkts
        if self.area is not None:
            result['Area'] = self.area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InPkts') is not None:
            self.in_pkts = m.get('InPkts')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        return self


class DescribeDDosEventAreaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        areas: List[DescribeDDosEventAreaResponseBodyAreas] = None,
    ):
        self.request_id = request_id
        self.areas = areas

    def validate(self):
        if self.areas:
            for k in self.areas:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Areas'] = []
        if self.areas is not None:
            for k in self.areas:
                result['Areas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.areas = []
        if m.get('Areas') is not None:
            for k in m.get('Areas'):
                temp_model = DescribeDDosEventAreaResponseBodyAreas()
                self.areas.append(temp_model.from_map(k))
        return self


class DescribeDDosEventAreaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDDosEventAreaResponseBody = None,
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
            temp_model = DescribeDDosEventAreaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventAttackTypeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        event_type: str = None,
        start_time: int = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.event_type = event_type
        self.start_time = start_time
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDDosEventAttackTypeResponseBodyAttackTypes(TeaModel):
    def __init__(
        self,
        attack_type: str = None,
        in_pkts: int = None,
    ):
        self.attack_type = attack_type
        self.in_pkts = in_pkts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.in_pkts is not None:
            result['InPkts'] = self.in_pkts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('InPkts') is not None:
            self.in_pkts = m.get('InPkts')
        return self


class DescribeDDosEventAttackTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        attack_types: List[DescribeDDosEventAttackTypeResponseBodyAttackTypes] = None,
    ):
        self.request_id = request_id
        self.attack_types = attack_types

    def validate(self):
        if self.attack_types:
            for k in self.attack_types:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AttackTypes'] = []
        if self.attack_types is not None:
            for k in self.attack_types:
                result['AttackTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.attack_types = []
        if m.get('AttackTypes') is not None:
            for k in m.get('AttackTypes'):
                temp_model = DescribeDDosEventAttackTypeResponseBodyAttackTypes()
                self.attack_types.append(temp_model.from_map(k))
        return self


class DescribeDDosEventAttackTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDDosEventAttackTypeResponseBody = None,
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
            temp_model = DescribeDDosEventAttackTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventIspRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        event_type: str = None,
        start_time: int = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.event_type = event_type
        self.start_time = start_time
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDDosEventIspResponseBodyIsps(TeaModel):
    def __init__(
        self,
        in_pkts: int = None,
        isp: str = None,
    ):
        self.in_pkts = in_pkts
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.in_pkts is not None:
            result['InPkts'] = self.in_pkts
        if self.isp is not None:
            result['Isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InPkts') is not None:
            self.in_pkts = m.get('InPkts')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        return self


class DescribeDDosEventIspResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        isps: List[DescribeDDosEventIspResponseBodyIsps] = None,
    ):
        self.request_id = request_id
        self.isps = isps

    def validate(self):
        if self.isps:
            for k in self.isps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Isps'] = []
        if self.isps is not None:
            for k in self.isps:
                result['Isps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.isps = []
        if m.get('Isps') is not None:
            for k in m.get('Isps'):
                temp_model = DescribeDDosEventIspResponseBodyIsps()
                self.isps.append(temp_model.from_map(k))
        return self


class DescribeDDosEventIspResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDDosEventIspResponseBody = None,
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
            temp_model = DescribeDDosEventIspResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventMaxRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDDosEventMaxResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        qps: int = None,
        cps: int = None,
        mbps: int = None,
    ):
        self.request_id = request_id
        self.qps = qps
        self.cps = cps
        self.mbps = mbps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        return self


class DescribeDDosEventMaxResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDDosEventMaxResponseBody = None,
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
            temp_model = DescribeDDosEventMaxResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDoSEventsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        end_time: int = None,
        start_time: int = None,
        page_size: int = None,
        page_number: int = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.end_time = end_time
        self.start_time = start_time
        self.page_size = page_size
        self.page_number = page_number
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeDDoSEventsResponseBodyDDoSEvents(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        event_type: str = None,
        region: str = None,
        ip: str = None,
        port: str = None,
        bps: int = None,
        pps: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.event_type = event_type
        self.region = region
        self.ip = ip
        self.port = port
        self.bps = bps
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.region is not None:
            result['Region'] = self.region
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeDDoSEventsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        ddo_sevents: List[DescribeDDoSEventsResponseBodyDDoSEvents] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.ddo_sevents = ddo_sevents

    def validate(self):
        if self.ddo_sevents:
            for k in self.ddo_sevents:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['DDoSEvents'] = []
        if self.ddo_sevents is not None:
            for k in self.ddo_sevents:
                result['DDoSEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.ddo_sevents = []
        if m.get('DDoSEvents') is not None:
            for k in m.get('DDoSEvents'):
                temp_model = DescribeDDoSEventsResponseBodyDDoSEvents()
                self.ddo_sevents.append(temp_model.from_map(k))
        return self


class DescribeDDoSEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDDoSEventsResponseBody = None,
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
            temp_model = DescribeDDoSEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventSrcIpRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        event_type: str = None,
        start_time: int = None,
        ip: str = None,
        range: int = None,
    ):
        self.source_ip = source_ip
        self.event_type = event_type
        self.start_time = start_time
        self.ip = ip
        self.range = range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.range is not None:
            result['Range'] = self.range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Range') is not None:
            self.range = m.get('Range')
        return self


class DescribeDDosEventSrcIpResponseBodyIps(TeaModel):
    def __init__(
        self,
        src_ip: str = None,
        area_id: str = None,
        isp: str = None,
    ):
        self.src_ip = src_ip
        self.area_id = area_id
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.isp is not None:
            result['Isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        return self


class DescribeDDosEventSrcIpResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ips: List[DescribeDDosEventSrcIpResponseBodyIps] = None,
    ):
        self.request_id = request_id
        self.ips = ips

    def validate(self):
        if self.ips:
            for k in self.ips:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Ips'] = []
        if self.ips is not None:
            for k in self.ips:
                result['Ips'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.ips = []
        if m.get('Ips') is not None:
            for k in m.get('Ips'):
                temp_model = DescribeDDosEventSrcIpResponseBodyIps()
                self.ips.append(temp_model.from_map(k))
        return self


class DescribeDDosEventSrcIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDDosEventSrcIpResponseBody = None,
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
            temp_model = DescribeDDosEventSrcIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefenseCountStatisticsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics(TeaModel):
    def __init__(
        self,
        max_usable_defense_count_current_month: int = None,
        flow_pack_count_remain: int = None,
        defense_count_total_usage_of_current_month: int = None,
    ):
        self.max_usable_defense_count_current_month = max_usable_defense_count_current_month
        self.flow_pack_count_remain = flow_pack_count_remain
        self.defense_count_total_usage_of_current_month = defense_count_total_usage_of_current_month

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_usable_defense_count_current_month is not None:
            result['MaxUsableDefenseCountCurrentMonth'] = self.max_usable_defense_count_current_month
        if self.flow_pack_count_remain is not None:
            result['FlowPackCountRemain'] = self.flow_pack_count_remain
        if self.defense_count_total_usage_of_current_month is not None:
            result['DefenseCountTotalUsageOfCurrentMonth'] = self.defense_count_total_usage_of_current_month
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxUsableDefenseCountCurrentMonth') is not None:
            self.max_usable_defense_count_current_month = m.get('MaxUsableDefenseCountCurrentMonth')
        if m.get('FlowPackCountRemain') is not None:
            self.flow_pack_count_remain = m.get('FlowPackCountRemain')
        if m.get('DefenseCountTotalUsageOfCurrentMonth') is not None:
            self.defense_count_total_usage_of_current_month = m.get('DefenseCountTotalUsageOfCurrentMonth')
        return self


class DescribeDefenseCountStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        defense_count_statistics: DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics = None,
    ):
        self.request_id = request_id
        self.defense_count_statistics = defense_count_statistics

    def validate(self):
        if self.defense_count_statistics:
            self.defense_count_statistics.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.defense_count_statistics is not None:
            result['DefenseCountStatistics'] = self.defense_count_statistics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DefenseCountStatistics') is not None:
            temp_model = DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics()
            self.defense_count_statistics = temp_model.from_map(m['DefenseCountStatistics'])
        return self


class DescribeDefenseCountStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDefenseCountStatisticsResponseBody = None,
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
            temp_model = DescribeDefenseCountStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefenseRecordsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        instance_id: str = None,
        start_time: int = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDefenseRecordsResponseBodyDefenseRecords(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        status: int = None,
        start_time: int = None,
        event_count: int = None,
        instance_id: str = None,
        attack_peak: int = None,
    ):
        self.end_time = end_time
        self.status = status
        self.start_time = start_time
        self.event_count = event_count
        self.instance_id = instance_id
        self.attack_peak = attack_peak

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.event_count is not None:
            result['EventCount'] = self.event_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.attack_peak is not None:
            result['AttackPeak'] = self.attack_peak
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AttackPeak') is not None:
            self.attack_peak = m.get('AttackPeak')
        return self


class DescribeDefenseRecordsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        defense_records: List[DescribeDefenseRecordsResponseBodyDefenseRecords] = None,
        request_id: str = None,
    ):
        self.total_count = total_count
        self.defense_records = defense_records
        self.request_id = request_id

    def validate(self):
        if self.defense_records:
            for k in self.defense_records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['DefenseRecords'] = []
        if self.defense_records is not None:
            for k in self.defense_records:
                result['DefenseRecords'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.defense_records = []
        if m.get('DefenseRecords') is not None:
            for k in m.get('DefenseRecords'):
                temp_model = DescribeDefenseRecordsResponseBodyDefenseRecords()
                self.defense_records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDefenseRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDefenseRecordsResponseBody = None,
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
            temp_model = DescribeDefenseRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAttackEventsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
        domain: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.domain = domain
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDomainAttackEventsResponseBodyDomainAttackEvents(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        domain: str = None,
        max_qps: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.domain = domain
        self.max_qps = max_qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        return self


class DescribeDomainAttackEventsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        domain_attack_events: List[DescribeDomainAttackEventsResponseBodyDomainAttackEvents] = None,
        request_id: str = None,
    ):
        self.total_count = total_count
        self.domain_attack_events = domain_attack_events
        self.request_id = request_id

    def validate(self):
        if self.domain_attack_events:
            for k in self.domain_attack_events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['DomainAttackEvents'] = []
        if self.domain_attack_events is not None:
            for k in self.domain_attack_events:
                result['DomainAttackEvents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.domain_attack_events = []
        if m.get('DomainAttackEvents') is not None:
            for k in m.get('DomainAttackEvents'):
                temp_model = DescribeDomainAttackEventsResponseBodyDomainAttackEvents()
                self.domain_attack_events.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainAttackEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainAttackEventsResponseBody = None,
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
            temp_model = DescribeDomainAttackEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainOverviewRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainOverviewResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        max_https: int = None,
        max_http: int = None,
    ):
        self.request_id = request_id
        self.max_https = max_https
        self.max_http = max_http

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_https is not None:
            result['MaxHttps'] = self.max_https
        if self.max_http is not None:
            result['MaxHttp'] = self.max_http
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxHttps') is not None:
            self.max_https = m.get('MaxHttps')
        if m.get('MaxHttp') is not None:
            self.max_http = m.get('MaxHttp')
        return self


class DescribeDomainOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainOverviewResponseBody = None,
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
            temp_model = DescribeDomainOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQPSListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
        interval: int = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainQPSListResponseBodyDomainQPSList(TeaModel):
    def __init__(
        self,
        index: int = None,
        time: int = None,
        max_attack_qps: int = None,
        attack_qps: int = None,
        max_qps: int = None,
        max_normal_qps: int = None,
        total_qps: int = None,
        total_count: int = None,
        cache_hits: int = None,
    ):
        self.index = index
        self.time = time
        self.max_attack_qps = max_attack_qps
        self.attack_qps = attack_qps
        self.max_qps = max_qps
        self.max_normal_qps = max_normal_qps
        self.total_qps = total_qps
        self.total_count = total_count
        self.cache_hits = cache_hits

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.time is not None:
            result['Time'] = self.time
        if self.max_attack_qps is not None:
            result['MaxAttackQps'] = self.max_attack_qps
        if self.attack_qps is not None:
            result['AttackQps'] = self.attack_qps
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        if self.max_normal_qps is not None:
            result['MaxNormalQps'] = self.max_normal_qps
        if self.total_qps is not None:
            result['TotalQps'] = self.total_qps
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.cache_hits is not None:
            result['CacheHits'] = self.cache_hits
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('MaxAttackQps') is not None:
            self.max_attack_qps = m.get('MaxAttackQps')
        if m.get('AttackQps') is not None:
            self.attack_qps = m.get('AttackQps')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        if m.get('MaxNormalQps') is not None:
            self.max_normal_qps = m.get('MaxNormalQps')
        if m.get('TotalQps') is not None:
            self.total_qps = m.get('TotalQps')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('CacheHits') is not None:
            self.cache_hits = m.get('CacheHits')
        return self


class DescribeDomainQPSListResponseBody(TeaModel):
    def __init__(
        self,
        domain_qpslist: List[DescribeDomainQPSListResponseBodyDomainQPSList] = None,
        request_id: str = None,
    ):
        self.domain_qpslist = domain_qpslist
        self.request_id = request_id

    def validate(self):
        if self.domain_qpslist:
            for k in self.domain_qpslist:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainQPSList'] = []
        if self.domain_qpslist is not None:
            for k in self.domain_qpslist:
                result['DomainQPSList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_qpslist = []
        if m.get('DomainQPSList') is not None:
            for k in m.get('DomainQPSList'):
                temp_model = DescribeDomainQPSListResponseBodyDomainQPSList()
                self.domain_qpslist.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainQPSListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainQPSListResponseBody = None,
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
            temp_model = DescribeDomainQPSListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQpsWithCacheRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDomainQpsWithCacheResponseBody(TeaModel):
    def __init__(
        self,
        ip_block_qps: List[str] = None,
        cc_js_qps: List[str] = None,
        blocks: List[str] = None,
        precise_blocks: List[str] = None,
        request_id: str = None,
        precise_js_qps: List[str] = None,
        totals: List[str] = None,
        start_time: int = None,
        cc_block_qps: List[str] = None,
        interval: int = None,
        region_blocks: List[str] = None,
        cache_hits: List[str] = None,
    ):
        self.ip_block_qps = ip_block_qps
        self.cc_js_qps = cc_js_qps
        self.blocks = blocks
        self.precise_blocks = precise_blocks
        self.request_id = request_id
        self.precise_js_qps = precise_js_qps
        self.totals = totals
        self.start_time = start_time
        self.cc_block_qps = cc_block_qps
        self.interval = interval
        self.region_blocks = region_blocks
        self.cache_hits = cache_hits

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ip_block_qps is not None:
            result['IpBlockQps'] = self.ip_block_qps
        if self.cc_js_qps is not None:
            result['CcJsQps'] = self.cc_js_qps
        if self.blocks is not None:
            result['Blocks'] = self.blocks
        if self.precise_blocks is not None:
            result['PreciseBlocks'] = self.precise_blocks
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.precise_js_qps is not None:
            result['PreciseJsQps'] = self.precise_js_qps
        if self.totals is not None:
            result['Totals'] = self.totals
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.cc_block_qps is not None:
            result['CcBlockQps'] = self.cc_block_qps
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.region_blocks is not None:
            result['RegionBlocks'] = self.region_blocks
        if self.cache_hits is not None:
            result['CacheHits'] = self.cache_hits
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpBlockQps') is not None:
            self.ip_block_qps = m.get('IpBlockQps')
        if m.get('CcJsQps') is not None:
            self.cc_js_qps = m.get('CcJsQps')
        if m.get('Blocks') is not None:
            self.blocks = m.get('Blocks')
        if m.get('PreciseBlocks') is not None:
            self.precise_blocks = m.get('PreciseBlocks')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PreciseJsQps') is not None:
            self.precise_js_qps = m.get('PreciseJsQps')
        if m.get('Totals') is not None:
            self.totals = m.get('Totals')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CcBlockQps') is not None:
            self.cc_block_qps = m.get('CcBlockQps')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('RegionBlocks') is not None:
            self.region_blocks = m.get('RegionBlocks')
        if m.get('CacheHits') is not None:
            self.cache_hits = m.get('CacheHits')
        return self


class DescribeDomainQpsWithCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainQpsWithCacheResponseBody = None,
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
            temp_model = DescribeDomainQpsWithCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.instance_ids = instance_ids

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
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeDomainsResponseBody(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        request_id: str = None,
    ):
        self.domains = domains
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainsResponseBody = None,
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
            temp_model = DescribeDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainStatusCodeCountRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainStatusCodeCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status_501: int = None,
        status_502: int = None,
        status_403: int = None,
        status_503: int = None,
        status_404: int = None,
        status_405: int = None,
        status_504: int = None,
        status_2xx: int = None,
        status_200: int = None,
        status_3xx: int = None,
        status_4xx: int = None,
        status_5xx: int = None,
    ):
        self.request_id = request_id
        self.status_501 = status_501
        self.status_502 = status_502
        self.status_403 = status_403
        self.status_503 = status_503
        self.status_404 = status_404
        self.status_405 = status_405
        self.status_504 = status_504
        self.status_2xx = status_2xx
        self.status_200 = status_200
        self.status_3xx = status_3xx
        self.status_4xx = status_4xx
        self.status_5xx = status_5xx

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status_501 is not None:
            result['Status501'] = self.status_501
        if self.status_502 is not None:
            result['Status502'] = self.status_502
        if self.status_403 is not None:
            result['Status403'] = self.status_403
        if self.status_503 is not None:
            result['Status503'] = self.status_503
        if self.status_404 is not None:
            result['Status404'] = self.status_404
        if self.status_405 is not None:
            result['Status405'] = self.status_405
        if self.status_504 is not None:
            result['Status504'] = self.status_504
        if self.status_2xx is not None:
            result['Status2XX'] = self.status_2xx
        if self.status_200 is not None:
            result['Status200'] = self.status_200
        if self.status_3xx is not None:
            result['Status3XX'] = self.status_3xx
        if self.status_4xx is not None:
            result['Status4XX'] = self.status_4xx
        if self.status_5xx is not None:
            result['Status5XX'] = self.status_5xx
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status501') is not None:
            self.status_501 = m.get('Status501')
        if m.get('Status502') is not None:
            self.status_502 = m.get('Status502')
        if m.get('Status403') is not None:
            self.status_403 = m.get('Status403')
        if m.get('Status503') is not None:
            self.status_503 = m.get('Status503')
        if m.get('Status404') is not None:
            self.status_404 = m.get('Status404')
        if m.get('Status405') is not None:
            self.status_405 = m.get('Status405')
        if m.get('Status504') is not None:
            self.status_504 = m.get('Status504')
        if m.get('Status2XX') is not None:
            self.status_2xx = m.get('Status2XX')
        if m.get('Status200') is not None:
            self.status_200 = m.get('Status200')
        if m.get('Status3XX') is not None:
            self.status_3xx = m.get('Status3XX')
        if m.get('Status4XX') is not None:
            self.status_4xx = m.get('Status4XX')
        if m.get('Status5XX') is not None:
            self.status_5xx = m.get('Status5XX')
        return self


class DescribeDomainStatusCodeCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainStatusCodeCountResponseBody = None,
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
            temp_model = DescribeDomainStatusCodeCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainStatusCodeListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
        interval: int = None,
        domain: str = None,
        query_type: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.domain = domain
        self.query_type = query_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        return self


class DescribeDomainStatusCodeListResponseBodyStatusCodeList(TeaModel):
    def __init__(
        self,
        status_502: int = None,
        index: int = None,
        time: int = None,
        status_405: int = None,
        status_3xx: int = None,
        status_503: int = None,
        status_4xx: int = None,
        status_2xx: int = None,
        status_5xx: int = None,
        status_504: int = None,
        status_403: int = None,
        status_200: int = None,
        status_404: int = None,
        status_501: int = None,
    ):
        self.status_502 = status_502
        self.index = index
        self.time = time
        self.status_405 = status_405
        self.status_3xx = status_3xx
        self.status_503 = status_503
        self.status_4xx = status_4xx
        self.status_2xx = status_2xx
        self.status_5xx = status_5xx
        self.status_504 = status_504
        self.status_403 = status_403
        self.status_200 = status_200
        self.status_404 = status_404
        self.status_501 = status_501

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status_502 is not None:
            result['Status502'] = self.status_502
        if self.index is not None:
            result['Index'] = self.index
        if self.time is not None:
            result['Time'] = self.time
        if self.status_405 is not None:
            result['Status405'] = self.status_405
        if self.status_3xx is not None:
            result['Status3XX'] = self.status_3xx
        if self.status_503 is not None:
            result['Status503'] = self.status_503
        if self.status_4xx is not None:
            result['Status4XX'] = self.status_4xx
        if self.status_2xx is not None:
            result['Status2XX'] = self.status_2xx
        if self.status_5xx is not None:
            result['Status5XX'] = self.status_5xx
        if self.status_504 is not None:
            result['Status504'] = self.status_504
        if self.status_403 is not None:
            result['Status403'] = self.status_403
        if self.status_200 is not None:
            result['Status200'] = self.status_200
        if self.status_404 is not None:
            result['Status404'] = self.status_404
        if self.status_501 is not None:
            result['Status501'] = self.status_501
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status502') is not None:
            self.status_502 = m.get('Status502')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Status405') is not None:
            self.status_405 = m.get('Status405')
        if m.get('Status3XX') is not None:
            self.status_3xx = m.get('Status3XX')
        if m.get('Status503') is not None:
            self.status_503 = m.get('Status503')
        if m.get('Status4XX') is not None:
            self.status_4xx = m.get('Status4XX')
        if m.get('Status2XX') is not None:
            self.status_2xx = m.get('Status2XX')
        if m.get('Status5XX') is not None:
            self.status_5xx = m.get('Status5XX')
        if m.get('Status504') is not None:
            self.status_504 = m.get('Status504')
        if m.get('Status403') is not None:
            self.status_403 = m.get('Status403')
        if m.get('Status200') is not None:
            self.status_200 = m.get('Status200')
        if m.get('Status404') is not None:
            self.status_404 = m.get('Status404')
        if m.get('Status501') is not None:
            self.status_501 = m.get('Status501')
        return self


class DescribeDomainStatusCodeListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status_code_list: List[DescribeDomainStatusCodeListResponseBodyStatusCodeList] = None,
    ):
        self.request_id = request_id
        self.status_code_list = status_code_list

    def validate(self):
        if self.status_code_list:
            for k in self.status_code_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatusCodeList'] = []
        if self.status_code_list is not None:
            for k in self.status_code_list:
                result['StatusCodeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.status_code_list = []
        if m.get('StatusCodeList') is not None:
            for k in m.get('StatusCodeList'):
                temp_model = DescribeDomainStatusCodeListResponseBodyStatusCodeList()
                self.status_code_list.append(temp_model.from_map(k))
        return self


class DescribeDomainStatusCodeListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainStatusCodeListResponseBody = None,
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
            temp_model = DescribeDomainStatusCodeListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTopAttackListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDomainTopAttackListResponseBodyAttackList(TeaModel):
    def __init__(
        self,
        attack: int = None,
        domain: str = None,
        count: int = None,
    ):
        self.attack = attack
        self.domain = domain
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.attack is not None:
            result['Attack'] = self.attack
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attack') is not None:
            self.attack = m.get('Attack')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDomainTopAttackListResponseBody(TeaModel):
    def __init__(
        self,
        attack_list: List[DescribeDomainTopAttackListResponseBodyAttackList] = None,
        request_id: str = None,
    ):
        self.attack_list = attack_list
        self.request_id = request_id

    def validate(self):
        if self.attack_list:
            for k in self.attack_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AttackList'] = []
        if self.attack_list is not None:
            for k in self.attack_list:
                result['AttackList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attack_list = []
        if m.get('AttackList') is not None:
            for k in m.get('AttackList'):
                temp_model = DescribeDomainTopAttackListResponseBodyAttackList()
                self.attack_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainTopAttackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainTopAttackListResponseBody = None,
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
            temp_model = DescribeDomainTopAttackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainViewSourceCountriesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainViewSourceCountriesResponseBodySourceCountrys(TeaModel):
    def __init__(
        self,
        country_id: str = None,
        count: int = None,
    ):
        self.country_id = country_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDomainViewSourceCountriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        source_countrys: List[DescribeDomainViewSourceCountriesResponseBodySourceCountrys] = None,
    ):
        self.request_id = request_id
        self.source_countrys = source_countrys

    def validate(self):
        if self.source_countrys:
            for k in self.source_countrys:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SourceCountrys'] = []
        if self.source_countrys is not None:
            for k in self.source_countrys:
                result['SourceCountrys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.source_countrys = []
        if m.get('SourceCountrys') is not None:
            for k in m.get('SourceCountrys'):
                temp_model = DescribeDomainViewSourceCountriesResponseBodySourceCountrys()
                self.source_countrys.append(temp_model.from_map(k))
        return self


class DescribeDomainViewSourceCountriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainViewSourceCountriesResponseBody = None,
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
            temp_model = DescribeDomainViewSourceCountriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainViewSourceProvincesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainViewSourceProvincesResponseBodySourceProvinces(TeaModel):
    def __init__(
        self,
        province_id: str = None,
        count: int = None,
    ):
        self.province_id = province_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDomainViewSourceProvincesResponseBody(TeaModel):
    def __init__(
        self,
        source_provinces: List[DescribeDomainViewSourceProvincesResponseBodySourceProvinces] = None,
        request_id: str = None,
    ):
        self.source_provinces = source_provinces
        self.request_id = request_id

    def validate(self):
        if self.source_provinces:
            for k in self.source_provinces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SourceProvinces'] = []
        if self.source_provinces is not None:
            for k in self.source_provinces:
                result['SourceProvinces'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_provinces = []
        if m.get('SourceProvinces') is not None:
            for k in m.get('SourceProvinces'):
                temp_model = DescribeDomainViewSourceProvincesResponseBodySourceProvinces()
                self.source_provinces.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainViewSourceProvincesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainViewSourceProvincesResponseBody = None,
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
            temp_model = DescribeDomainViewSourceProvincesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainViewTopCostTimeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
        domain: str = None,
        top: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.domain = domain
        self.top = top

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.top is not None:
            result['Top'] = self.top
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        return self


class DescribeDomainViewTopCostTimeResponseBodyUrlList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        cost_time: float = None,
        url: str = None,
    ):
        self.domain = domain
        self.cost_time = cost_time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeDomainViewTopCostTimeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url_list: List[DescribeDomainViewTopCostTimeResponseBodyUrlList] = None,
    ):
        self.request_id = request_id
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainViewTopCostTimeResponseBodyUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainViewTopCostTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainViewTopCostTimeResponseBody = None,
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
            temp_model = DescribeDomainViewTopCostTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainViewTopUrlRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
        domain: str = None,
        top: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.domain = domain
        self.top = top

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.top is not None:
            result['Top'] = self.top
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        return self


class DescribeDomainViewTopUrlResponseBodyUrlList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        url: str = None,
        count: int = None,
    ):
        self.domain = domain
        self.url = url
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.url is not None:
            result['Url'] = self.url
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDomainViewTopUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url_list: List[DescribeDomainViewTopUrlResponseBodyUrlList] = None,
    ):
        self.request_id = request_id
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainViewTopUrlResponseBodyUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainViewTopUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainViewTopUrlResponseBody = None,
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
            temp_model = DescribeDomainViewTopUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeElasticBandwidthSpecRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeElasticBandwidthSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        elastic_bandwidth_spec: List[str] = None,
    ):
        self.request_id = request_id
        self.elastic_bandwidth_spec = elastic_bandwidth_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.elastic_bandwidth_spec is not None:
            result['ElasticBandwidthSpec'] = self.elastic_bandwidth_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ElasticBandwidthSpec') is not None:
            self.elastic_bandwidth_spec = m.get('ElasticBandwidthSpec')
        return self


class DescribeElasticBandwidthSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeElasticBandwidthSpecResponseBody = None,
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
            temp_model = DescribeElasticBandwidthSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthCheckListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        network_rules: str = None,
    ):
        self.source_ip = source_ip
        self.network_rules = network_rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck(TeaModel):
    def __init__(
        self,
        timeout: int = None,
        type: str = None,
        domain: str = None,
        interval: int = None,
        up: int = None,
        down: int = None,
        port: int = None,
        uri: str = None,
    ):
        self.timeout = timeout
        self.type = type
        self.domain = domain
        self.interval = interval
        self.up = up
        self.down = down
        self.port = port
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.type is not None:
            result['Type'] = self.type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.up is not None:
            result['Up'] = self.up
        if self.down is not None:
            result['Down'] = self.down
        if self.port is not None:
            result['Port'] = self.port
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Up') is not None:
            self.up = m.get('Up')
        if m.get('Down') is not None:
            self.down = m.get('Down')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeHealthCheckListResponseBodyHealthCheckList(TeaModel):
    def __init__(
        self,
        frontend_port: int = None,
        protocol: str = None,
        instance_id: str = None,
        health_check: DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck = None,
    ):
        self.frontend_port = frontend_port
        self.protocol = protocol
        self.instance_id = instance_id
        self.health_check = health_check

    def validate(self):
        if self.health_check:
            self.health_check.validate()

    def to_map(self):
        result = dict()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('HealthCheck') is not None:
            temp_model = DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck()
            self.health_check = temp_model.from_map(m['HealthCheck'])
        return self


class DescribeHealthCheckListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        health_check_list: List[DescribeHealthCheckListResponseBodyHealthCheckList] = None,
    ):
        self.request_id = request_id
        self.health_check_list = health_check_list

    def validate(self):
        if self.health_check_list:
            for k in self.health_check_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HealthCheckList'] = []
        if self.health_check_list is not None:
            for k in self.health_check_list:
                result['HealthCheckList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.health_check_list = []
        if m.get('HealthCheckList') is not None:
            for k in m.get('HealthCheckList'):
                temp_model = DescribeHealthCheckListResponseBodyHealthCheckList()
                self.health_check_list.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHealthCheckListResponseBody = None,
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
            temp_model = DescribeHealthCheckListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthCheckStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        network_rules: str = None,
    ):
        self.source_ip = source_ip
        self.network_rules = network_rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class DescribeHealthCheckStatusResponseBodyHealthCheckStatusRealServerStatusList(TeaModel):
    def __init__(
        self,
        status: str = None,
        address: str = None,
    ):
        self.status = status
        self.address = address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.address is not None:
            result['Address'] = self.address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        return self


class DescribeHealthCheckStatusResponseBodyHealthCheckStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        frontend_port: int = None,
        protocol: str = None,
        instance_id: str = None,
        real_server_status_list: List[DescribeHealthCheckStatusResponseBodyHealthCheckStatusRealServerStatusList] = None,
    ):
        self.status = status
        self.frontend_port = frontend_port
        self.protocol = protocol
        self.instance_id = instance_id
        self.real_server_status_list = real_server_status_list

    def validate(self):
        if self.real_server_status_list:
            for k in self.real_server_status_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['RealServerStatusList'] = []
        if self.real_server_status_list is not None:
            for k in self.real_server_status_list:
                result['RealServerStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.real_server_status_list = []
        if m.get('RealServerStatusList') is not None:
            for k in m.get('RealServerStatusList'):
                temp_model = DescribeHealthCheckStatusResponseBodyHealthCheckStatusRealServerStatusList()
                self.real_server_status_list.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        health_check_status: List[DescribeHealthCheckStatusResponseBodyHealthCheckStatus] = None,
    ):
        self.request_id = request_id
        self.health_check_status = health_check_status

    def validate(self):
        if self.health_check_status:
            for k in self.health_check_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HealthCheckStatus'] = []
        if self.health_check_status is not None:
            for k in self.health_check_status:
                result['HealthCheckStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.health_check_status = []
        if m.get('HealthCheckStatus') is not None:
            for k in m.get('HealthCheckStatus'):
                temp_model = DescribeHealthCheckStatusResponseBodyHealthCheckStatus()
                self.health_check_status.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHealthCheckStatusResponseBody = None,
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
            temp_model = DescribeHealthCheckStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceDetailsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos(TeaModel):
    def __init__(
        self,
        status: str = None,
        eip: str = None,
    ):
        self.status = status
        self.eip = eip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.eip is not None:
            result['Eip'] = self.eip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        return self


class DescribeInstanceDetailsResponseBodyInstanceDetails(TeaModel):
    def __init__(
        self,
        line: str = None,
        instance_id: str = None,
        eip_infos: List[DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos] = None,
    ):
        self.line = line
        self.instance_id = instance_id
        self.eip_infos = eip_infos

    def validate(self):
        if self.eip_infos:
            for k in self.eip_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.line is not None:
            result['Line'] = self.line
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['EipInfos'] = []
        if self.eip_infos is not None:
            for k in self.eip_infos:
                result['EipInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.eip_infos = []
        if m.get('EipInfos') is not None:
            for k in m.get('EipInfos'):
                temp_model = DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos()
                self.eip_infos.append(temp_model.from_map(k))
        return self


class DescribeInstanceDetailsResponseBody(TeaModel):
    def __init__(
        self,
        instance_details: List[DescribeInstanceDetailsResponseBodyInstanceDetails] = None,
        request_id: str = None,
    ):
        self.instance_details = instance_details
        self.request_id = request_id

    def validate(self):
        if self.instance_details:
            for k in self.instance_details:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k in self.instance_details:
                result['InstanceDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_details = []
        if m.get('InstanceDetails') is not None:
            for k in m.get('InstanceDetails'):
                temp_model = DescribeInstanceDetailsResponseBodyInstanceDetails()
                self.instance_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceDetailsResponseBody = None,
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
            temp_model = DescribeInstanceDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceIdsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        edition: int = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.edition = edition
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceIdsResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        edition: int = None,
        remark: str = None,
        instance_id: str = None,
    ):
        self.edition = edition
        self.remark = remark
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceIdsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_ids: List[DescribeInstanceIdsResponseBodyInstanceIds] = None,
    ):
        self.request_id = request_id
        self.instance_ids = instance_ids

    def validate(self):
        if self.instance_ids:
            for k in self.instance_ids:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceIds'] = []
        if self.instance_ids is not None:
            for k in self.instance_ids:
                result['InstanceIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_ids = []
        if m.get('InstanceIds') is not None:
            for k in m.get('InstanceIds'):
                temp_model = DescribeInstanceIdsResponseBodyInstanceIds()
                self.instance_ids.append(temp_model.from_map(k))
        return self


class DescribeInstanceIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceIdsResponseBody = None,
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
            temp_model = DescribeInstanceIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
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


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        page_number: str = None,
        page_size: str = None,
        ip: str = None,
        remark: str = None,
        edition: int = None,
        enabled: int = None,
        expire_start_time: int = None,
        expire_end_time: int = None,
        instance_ids: List[str] = None,
        status: List[int] = None,
        tag: List[DescribeInstancesRequestTag] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.page_number = page_number
        self.page_size = page_size
        self.ip = ip
        self.remark = remark
        self.edition = edition
        self.enabled = enabled
        self.expire_start_time = expire_start_time
        self.expire_end_time = expire_end_time
        self.instance_ids = instance_ids
        self.status = status
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.expire_start_time is not None:
            result['ExpireStartTime'] = self.expire_start_time
        if self.expire_end_time is not None:
            result['ExpireEndTime'] = self.expire_end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExpireStartTime') is not None:
            self.expire_start_time = m.get('ExpireStartTime')
        if m.get('ExpireEndTime') is not None:
            self.expire_end_time = m.get('ExpireEndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        status: int = None,
        debt_status: int = None,
        edition: int = None,
        expire_time: int = None,
        remark: str = None,
        create_time: int = None,
        enabled: int = None,
        instance_id: str = None,
        conn_instance_id: str = None,
    ):
        self.status = status
        self.debt_status = debt_status
        self.edition = edition
        self.expire_time = expire_time
        self.remark = remark
        self.create_time = create_time
        self.enabled = enabled
        self.instance_id = instance_id
        self.conn_instance_id = conn_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.debt_status is not None:
            result['DebtStatus'] = self.debt_status
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.conn_instance_id is not None:
            result['ConnInstanceId'] = self.conn_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DebtStatus') is not None:
            self.debt_status = m.get('DebtStatus')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConnInstanceId') is not None:
            self.conn_instance_id = m.get('ConnInstanceId')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeInstancesResponseBodyInstances] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.instances = instances
        self.total_count = total_count
        self.request_id = request_id

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstancesResponseBody = None,
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceSpecsResponseBodyInstanceSpecs(TeaModel):
    def __init__(
        self,
        base_bandwidth: int = None,
        qps_limit: int = None,
        bandwidth_mbps: int = None,
        defense_count: int = None,
        site_limit: int = None,
        port_limit: int = None,
        elastic_bandwidth: int = None,
        function_version: str = None,
        instance_id: str = None,
        domain_limit: int = None,
    ):
        self.base_bandwidth = base_bandwidth
        self.qps_limit = qps_limit
        self.bandwidth_mbps = bandwidth_mbps
        self.defense_count = defense_count
        self.site_limit = site_limit
        self.port_limit = port_limit
        self.elastic_bandwidth = elastic_bandwidth
        self.function_version = function_version
        self.instance_id = instance_id
        self.domain_limit = domain_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.base_bandwidth is not None:
            result['BaseBandwidth'] = self.base_bandwidth
        if self.qps_limit is not None:
            result['QpsLimit'] = self.qps_limit
        if self.bandwidth_mbps is not None:
            result['BandwidthMbps'] = self.bandwidth_mbps
        if self.defense_count is not None:
            result['DefenseCount'] = self.defense_count
        if self.site_limit is not None:
            result['SiteLimit'] = self.site_limit
        if self.port_limit is not None:
            result['PortLimit'] = self.port_limit
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain_limit is not None:
            result['DomainLimit'] = self.domain_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseBandwidth') is not None:
            self.base_bandwidth = m.get('BaseBandwidth')
        if m.get('QpsLimit') is not None:
            self.qps_limit = m.get('QpsLimit')
        if m.get('BandwidthMbps') is not None:
            self.bandwidth_mbps = m.get('BandwidthMbps')
        if m.get('DefenseCount') is not None:
            self.defense_count = m.get('DefenseCount')
        if m.get('SiteLimit') is not None:
            self.site_limit = m.get('SiteLimit')
        if m.get('PortLimit') is not None:
            self.port_limit = m.get('PortLimit')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DomainLimit') is not None:
            self.domain_limit = m.get('DomainLimit')
        return self


class DescribeInstanceSpecsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_specs: List[DescribeInstanceSpecsResponseBodyInstanceSpecs] = None,
    ):
        self.request_id = request_id
        self.instance_specs = instance_specs

    def validate(self):
        if self.instance_specs:
            for k in self.instance_specs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceSpecs'] = []
        if self.instance_specs is not None:
            for k in self.instance_specs:
                result['InstanceSpecs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_specs = []
        if m.get('InstanceSpecs') is not None:
            for k in m.get('InstanceSpecs'):
                temp_model = DescribeInstanceSpecsResponseBodyInstanceSpecs()
                self.instance_specs.append(temp_model.from_map(k))
        return self


class DescribeInstanceSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceSpecsResponseBody = None,
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
            temp_model = DescribeInstanceSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStatisticsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceStatisticsResponseBodyInstanceStatistics(TeaModel):
    def __init__(
        self,
        domain_usage: int = None,
        defense_count_usage: int = None,
        instance_id: str = None,
        site_usage: int = None,
        port_usage: int = None,
    ):
        self.domain_usage = domain_usage
        self.defense_count_usage = defense_count_usage
        self.instance_id = instance_id
        self.site_usage = site_usage
        self.port_usage = port_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain_usage is not None:
            result['DomainUsage'] = self.domain_usage
        if self.defense_count_usage is not None:
            result['DefenseCountUsage'] = self.defense_count_usage
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.site_usage is not None:
            result['SiteUsage'] = self.site_usage
        if self.port_usage is not None:
            result['PortUsage'] = self.port_usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainUsage') is not None:
            self.domain_usage = m.get('DomainUsage')
        if m.get('DefenseCountUsage') is not None:
            self.defense_count_usage = m.get('DefenseCountUsage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SiteUsage') is not None:
            self.site_usage = m.get('SiteUsage')
        if m.get('PortUsage') is not None:
            self.port_usage = m.get('PortUsage')
        return self


class DescribeInstanceStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        instance_statistics: List[DescribeInstanceStatisticsResponseBodyInstanceStatistics] = None,
        request_id: str = None,
    ):
        self.instance_statistics = instance_statistics
        self.request_id = request_id

    def validate(self):
        if self.instance_statistics:
            for k in self.instance_statistics:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceStatistics'] = []
        if self.instance_statistics is not None:
            for k in self.instance_statistics:
                result['InstanceStatistics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_statistics = []
        if m.get('InstanceStatistics') is not None:
            for k in m.get('InstanceStatistics'):
                temp_model = DescribeInstanceStatisticsResponseBodyInstanceStatistics()
                self.instance_statistics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceStatisticsResponseBody = None,
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
            temp_model = DescribeInstanceStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        product_type: int = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DescribeInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
        instance_status: int = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id
        self.instance_status = instance_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        return self


class DescribeInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceStatusResponseBody = None,
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
            temp_model = DescribeInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeL7RsPolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        real_servers: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.real_servers = real_servers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        return self


class DescribeL7RsPolicyResponseBodyAttributesAttribute(TeaModel):
    def __init__(
        self,
        weight: int = None,
    ):
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeL7RsPolicyResponseBodyAttributes(TeaModel):
    def __init__(
        self,
        rs_type: int = None,
        attribute: DescribeL7RsPolicyResponseBodyAttributesAttribute = None,
        real_server: str = None,
    ):
        self.rs_type = rs_type
        self.attribute = attribute
        self.real_server = real_server

    def validate(self):
        if self.attribute:
            self.attribute.validate()

    def to_map(self):
        result = dict()
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.attribute is not None:
            result['Attribute'] = self.attribute.to_map()
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('Attribute') is not None:
            temp_model = DescribeL7RsPolicyResponseBodyAttributesAttribute()
            self.attribute = temp_model.from_map(m['Attribute'])
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')
        return self


class DescribeL7RsPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        attributes: List[DescribeL7RsPolicyResponseBodyAttributes] = None,
        proxy_mode: str = None,
    ):
        self.request_id = request_id
        self.attributes = attributes
        self.proxy_mode = proxy_mode

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.proxy_mode is not None:
            result['ProxyMode'] = self.proxy_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = DescribeL7RsPolicyResponseBodyAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('ProxyMode') is not None:
            self.proxy_mode = m.get('ProxyMode')
        return self


class DescribeL7RsPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeL7RsPolicyResponseBody = None,
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
            temp_model = DescribeL7RsPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogStoreExistStatusRequest(TeaModel):
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


class DescribeLogStoreExistStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        exist_status: bool = None,
    ):
        self.request_id = request_id
        self.exist_status = exist_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.exist_status is not None:
            result['ExistStatus'] = self.exist_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExistStatus') is not None:
            self.exist_status = m.get('ExistStatus')
        return self


class DescribeLogStoreExistStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLogStoreExistStatusResponseBody = None,
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
            temp_model = DescribeLogStoreExistStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkRegionBlockRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeNetworkRegionBlockResponseBodyConfig(TeaModel):
    def __init__(
        self,
        region_block_switch: str = None,
        provinces: List[str] = None,
        countries: List[str] = None,
    ):
        self.region_block_switch = region_block_switch
        self.provinces = provinces
        self.countries = countries

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_block_switch is not None:
            result['RegionBlockSwitch'] = self.region_block_switch
        if self.provinces is not None:
            result['Provinces'] = self.provinces
        if self.countries is not None:
            result['Countries'] = self.countries
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionBlockSwitch') is not None:
            self.region_block_switch = m.get('RegionBlockSwitch')
        if m.get('Provinces') is not None:
            self.provinces = m.get('Provinces')
        if m.get('Countries') is not None:
            self.countries = m.get('Countries')
        return self


class DescribeNetworkRegionBlockResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config: DescribeNetworkRegionBlockResponseBodyConfig = None,
    ):
        self.request_id = request_id
        self.config = config

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config is not None:
            result['Config'] = self.config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Config') is not None:
            temp_model = DescribeNetworkRegionBlockResponseBodyConfig()
            self.config = temp_model.from_map(m['Config'])
        return self


class DescribeNetworkRegionBlockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNetworkRegionBlockResponseBody = None,
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
            temp_model = DescribeNetworkRegionBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkRuleAttributesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        network_rules: str = None,
    ):
        self.source_ip = source_ip
        self.network_rules = network_rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCcSblack(TeaModel):
    def __init__(
        self,
        type: int = None,
        expires: int = None,
        during: int = None,
        cnt: int = None,
    ):
        self.type = type
        self.expires = expires
        self.during = during
        self.cnt = cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.during is not None:
            result['During'] = self.during
        if self.cnt is not None:
            result['Cnt'] = self.cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        if m.get('During') is not None:
            self.during = m.get('During')
        if m.get('Cnt') is not None:
            self.cnt = m.get('Cnt')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc(TeaModel):
    def __init__(
        self,
        sblack: List[DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCcSblack] = None,
    ):
        self.sblack = sblack

    def validate(self):
        if self.sblack:
            for k in self.sblack:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Sblack'] = []
        if self.sblack is not None:
            for k in self.sblack:
                result['Sblack'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sblack = []
        if m.get('Sblack') is not None:
            for k in m.get('Sblack'):
                temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCcSblack()
                self.sblack.append(temp_model.from_map(k))
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigPayloadLen(TeaModel):
    def __init__(
        self,
        max: int = None,
        min: int = None,
    ):
        self.max = max
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSla(TeaModel):
    def __init__(
        self,
        maxconn_enable: int = None,
        cps_enable: int = None,
        cps: int = None,
        maxconn: int = None,
    ):
        self.maxconn_enable = maxconn_enable
        self.cps_enable = cps_enable
        self.cps = cps
        self.maxconn = maxconn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxconnEnable') is not None:
            self.maxconn_enable = m.get('MaxconnEnable')
        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Maxconn') is not None:
            self.maxconn = m.get('Maxconn')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSlimit(TeaModel):
    def __init__(
        self,
        maxconn_enable: int = None,
        cps_enable: int = None,
        cps: int = None,
        pps: int = None,
        bps: int = None,
        maxconn: int = None,
        cps_mode: int = None,
    ):
        self.maxconn_enable = maxconn_enable
        self.cps_enable = cps_enable
        self.cps = cps
        self.pps = pps
        self.bps = bps
        self.maxconn = maxconn
        self.cps_mode = cps_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn
        if self.cps_mode is not None:
            result['CpsMode'] = self.cps_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxconnEnable') is not None:
            self.maxconn_enable = m.get('MaxconnEnable')
        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Maxconn') is not None:
            self.maxconn = m.get('Maxconn')
        if m.get('CpsMode') is not None:
            self.cps_mode = m.get('CpsMode')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig(TeaModel):
    def __init__(
        self,
        cc: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc = None,
        payload_len: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigPayloadLen = None,
        persistence_timeout: int = None,
        sla: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSla = None,
        slimit: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSlimit = None,
        nodata_conn: str = None,
        synproxy: str = None,
    ):
        self.cc = cc
        self.payload_len = payload_len
        self.persistence_timeout = persistence_timeout
        self.sla = sla
        self.slimit = slimit
        self.nodata_conn = nodata_conn
        self.synproxy = synproxy

    def validate(self):
        if self.cc:
            self.cc.validate()
        if self.payload_len:
            self.payload_len.validate()
        if self.sla:
            self.sla.validate()
        if self.slimit:
            self.slimit.validate()

    def to_map(self):
        result = dict()
        if self.cc is not None:
            result['Cc'] = self.cc.to_map()
        if self.payload_len is not None:
            result['PayloadLen'] = self.payload_len.to_map()
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.sla is not None:
            result['Sla'] = self.sla.to_map()
        if self.slimit is not None:
            result['Slimit'] = self.slimit.to_map()
        if self.nodata_conn is not None:
            result['NodataConn'] = self.nodata_conn
        if self.synproxy is not None:
            result['Synproxy'] = self.synproxy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cc') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc()
            self.cc = temp_model.from_map(m['Cc'])
        if m.get('PayloadLen') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigPayloadLen()
            self.payload_len = temp_model.from_map(m['PayloadLen'])
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('Sla') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSla()
            self.sla = temp_model.from_map(m['Sla'])
        if m.get('Slimit') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSlimit()
            self.slimit = temp_model.from_map(m['Slimit'])
        if m.get('NodataConn') is not None:
            self.nodata_conn = m.get('NodataConn')
        if m.get('Synproxy') is not None:
            self.synproxy = m.get('Synproxy')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributes(TeaModel):
    def __init__(
        self,
        frontend_port: int = None,
        protocol: str = None,
        instance_id: str = None,
        config: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig = None,
    ):
        self.frontend_port = frontend_port
        self.protocol = protocol
        self.instance_id = instance_id
        self.config = config

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.config is not None:
            result['Config'] = self.config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Config') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig()
            self.config = temp_model.from_map(m['Config'])
        return self


class DescribeNetworkRuleAttributesResponseBody(TeaModel):
    def __init__(
        self,
        network_rule_attributes: List[DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributes] = None,
        request_id: str = None,
    ):
        self.network_rule_attributes = network_rule_attributes
        self.request_id = request_id

    def validate(self):
        if self.network_rule_attributes:
            for k in self.network_rule_attributes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['NetworkRuleAttributes'] = []
        if self.network_rule_attributes is not None:
            for k in self.network_rule_attributes:
                result['NetworkRuleAttributes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_rule_attributes = []
        if m.get('NetworkRuleAttributes') is not None:
            for k in m.get('NetworkRuleAttributes'):
                temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributes()
                self.network_rule_attributes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNetworkRuleAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNetworkRuleAttributesResponseBody = None,
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
            temp_model = DescribeNetworkRuleAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        forward_protocol: str = None,
        frontend_port: int = None,
        page_number: int = None,
        page_size: int = None,
        is_offset: bool = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.forward_protocol = forward_protocol
        self.frontend_port = frontend_port
        self.page_number = page_number
        self.page_size = page_size
        self.is_offset = is_offset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.is_offset is not None:
            result['IsOffset'] = self.is_offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IsOffset') is not None:
            self.is_offset = m.get('IsOffset')
        return self


class DescribeNetworkRulesResponseBodyNetworkRules(TeaModel):
    def __init__(
        self,
        frontend_port: int = None,
        is_auto_create: bool = None,
        protocol: str = None,
        real_servers: List[str] = None,
        instance_id: str = None,
        backend_port: int = None,
    ):
        self.frontend_port = frontend_port
        self.is_auto_create = is_auto_create
        self.protocol = protocol
        self.real_servers = real_servers
        self.instance_id = instance_id
        self.backend_port = backend_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.is_auto_create is not None:
            result['IsAutoCreate'] = self.is_auto_create
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('IsAutoCreate') is not None:
            self.is_auto_create = m.get('IsAutoCreate')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')
        return self


class DescribeNetworkRulesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        network_rules: List[DescribeNetworkRulesResponseBodyNetworkRules] = None,
        request_id: str = None,
    ):
        self.total_count = total_count
        self.network_rules = network_rules
        self.request_id = request_id

    def validate(self):
        if self.network_rules:
            for k in self.network_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['NetworkRules'] = []
        if self.network_rules is not None:
            for k in self.network_rules:
                result['NetworkRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.network_rules = []
        if m.get('NetworkRules') is not None:
            for k in m.get('NetworkRules'):
                temp_model = DescribeNetworkRulesResponseBodyNetworkRules()
                self.network_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNetworkRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNetworkRulesResponseBody = None,
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
            temp_model = DescribeNetworkRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpEntitiesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        entity_type: int = None,
        entity_object: str = None,
        start_time: int = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.entity_type = entity_type
        self.entity_object = entity_object
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeOpEntitiesResponseBodyOpEntities(TeaModel):
    def __init__(
        self,
        entity_type: int = None,
        entity_object: str = None,
        gmt_create: int = None,
        op_action: int = None,
        op_account: str = None,
        op_desc: str = None,
    ):
        self.entity_type = entity_type
        self.entity_object = entity_object
        self.gmt_create = gmt_create
        self.op_action = op_action
        self.op_account = op_account
        self.op_desc = op_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.op_action is not None:
            result['OpAction'] = self.op_action
        if self.op_account is not None:
            result['OpAccount'] = self.op_account
        if self.op_desc is not None:
            result['OpDesc'] = self.op_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')
        if m.get('OpAccount') is not None:
            self.op_account = m.get('OpAccount')
        if m.get('OpDesc') is not None:
            self.op_desc = m.get('OpDesc')
        return self


class DescribeOpEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        op_entities: List[DescribeOpEntitiesResponseBodyOpEntities] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.op_entities = op_entities

    def validate(self):
        if self.op_entities:
            for k in self.op_entities:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OpEntities'] = []
        if self.op_entities is not None:
            for k in self.op_entities:
                result['OpEntities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.op_entities = []
        if m.get('OpEntities') is not None:
            for k in m.get('OpEntities'):
                temp_model = DescribeOpEntitiesResponseBodyOpEntities()
                self.op_entities.append(temp_model.from_map(k))
        return self


class DescribeOpEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOpEntitiesResponseBody = None,
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
            temp_model = DescribeOpEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortAttackMaxFlowRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        end_time: int = None,
        start_time: int = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.end_time = end_time
        self.start_time = start_time
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortAttackMaxFlowResponseBody(TeaModel):
    def __init__(
        self,
        pps: int = None,
        request_id: str = None,
        bps: int = None,
    ):
        self.pps = pps
        self.request_id = request_id
        self.bps = bps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bps is not None:
            result['Bps'] = self.bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        return self


class DescribePortAttackMaxFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePortAttackMaxFlowResponseBody = None,
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
            temp_model = DescribePortAttackMaxFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortAutoCcStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortAutoCcStatusResponseBodyPortAutoCcStatus(TeaModel):
    def __init__(
        self,
        switch: str = None,
        mode: str = None,
        web_switch: str = None,
        web_mode: str = None,
    ):
        self.switch = switch
        self.mode = mode
        self.web_switch = web_switch
        self.web_mode = web_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.switch is not None:
            result['Switch'] = self.switch
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.web_switch is not None:
            result['WebSwitch'] = self.web_switch
        if self.web_mode is not None:
            result['WebMode'] = self.web_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Switch') is not None:
            self.switch = m.get('Switch')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('WebSwitch') is not None:
            self.web_switch = m.get('WebSwitch')
        if m.get('WebMode') is not None:
            self.web_mode = m.get('WebMode')
        return self


class DescribePortAutoCcStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        port_auto_cc_status: List[DescribePortAutoCcStatusResponseBodyPortAutoCcStatus] = None,
    ):
        self.request_id = request_id
        self.port_auto_cc_status = port_auto_cc_status

    def validate(self):
        if self.port_auto_cc_status:
            for k in self.port_auto_cc_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PortAutoCcStatus'] = []
        if self.port_auto_cc_status is not None:
            for k in self.port_auto_cc_status:
                result['PortAutoCcStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.port_auto_cc_status = []
        if m.get('PortAutoCcStatus') is not None:
            for k in m.get('PortAutoCcStatus'):
                temp_model = DescribePortAutoCcStatusResponseBodyPortAutoCcStatus()
                self.port_auto_cc_status.append(temp_model.from_map(k))
        return self


class DescribePortAutoCcStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePortAutoCcStatusResponseBody = None,
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
            temp_model = DescribePortAutoCcStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortConnsCountRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        end_time: int = None,
        start_time: int = None,
        port: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.end_time = end_time
        self.start_time = start_time
        self.port = port
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortConnsCountResponseBody(TeaModel):
    def __init__(
        self,
        conns: int = None,
        request_id: str = None,
        cps: int = None,
        in_act_conns: int = None,
        act_conns: int = None,
    ):
        self.conns = conns
        self.request_id = request_id
        self.cps = cps
        self.in_act_conns = in_act_conns
        self.act_conns = act_conns

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conns is not None:
            result['Conns'] = self.conns
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.in_act_conns is not None:
            result['InActConns'] = self.in_act_conns
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conns') is not None:
            self.conns = m.get('Conns')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('InActConns') is not None:
            self.in_act_conns = m.get('InActConns')
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')
        return self


class DescribePortConnsCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePortConnsCountResponseBody = None,
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
            temp_model = DescribePortConnsCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortConnsListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        end_time: int = None,
        start_time: int = None,
        interval: int = None,
        port: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.end_time = end_time
        self.start_time = start_time
        self.interval = interval
        self.port = port
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortConnsListResponseBodyConnsList(TeaModel):
    def __init__(
        self,
        act_conns: int = None,
        in_act_conns: int = None,
        index: int = None,
        time: int = None,
        cps: int = None,
        conns: int = None,
    ):
        self.act_conns = act_conns
        self.in_act_conns = in_act_conns
        self.index = index
        self.time = time
        self.cps = cps
        self.conns = conns

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns
        if self.in_act_conns is not None:
            result['InActConns'] = self.in_act_conns
        if self.index is not None:
            result['Index'] = self.index
        if self.time is not None:
            result['Time'] = self.time
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.conns is not None:
            result['Conns'] = self.conns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')
        if m.get('InActConns') is not None:
            self.in_act_conns = m.get('InActConns')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Conns') is not None:
            self.conns = m.get('Conns')
        return self


class DescribePortConnsListResponseBody(TeaModel):
    def __init__(
        self,
        conns_list: List[DescribePortConnsListResponseBodyConnsList] = None,
        request_id: str = None,
    ):
        self.conns_list = conns_list
        self.request_id = request_id

    def validate(self):
        if self.conns_list:
            for k in self.conns_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConnsList'] = []
        if self.conns_list is not None:
            for k in self.conns_list:
                result['ConnsList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conns_list = []
        if m.get('ConnsList') is not None:
            for k in m.get('ConnsList'):
                temp_model = DescribePortConnsListResponseBodyConnsList()
                self.conns_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePortConnsListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePortConnsListResponseBody = None,
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
            temp_model = DescribePortConnsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortFlowListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        end_time: int = None,
        start_time: int = None,
        interval: int = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.end_time = end_time
        self.start_time = start_time
        self.interval = interval
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortFlowListResponseBodyPortFlowList(TeaModel):
    def __init__(
        self,
        index: int = None,
        time: int = None,
        in_pps: int = None,
        in_bps: int = None,
        region: str = None,
        out_pps: int = None,
        attack_pps: int = None,
        out_bps: int = None,
        attack_bps: int = None,
    ):
        self.index = index
        self.time = time
        self.in_pps = in_pps
        self.in_bps = in_bps
        self.region = region
        self.out_pps = out_pps
        self.attack_pps = attack_pps
        self.out_bps = out_bps
        self.attack_bps = attack_bps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.time is not None:
            result['Time'] = self.time
        if self.in_pps is not None:
            result['InPps'] = self.in_pps
        if self.in_bps is not None:
            result['InBps'] = self.in_bps
        if self.region is not None:
            result['Region'] = self.region
        if self.out_pps is not None:
            result['OutPps'] = self.out_pps
        if self.attack_pps is not None:
            result['AttackPps'] = self.attack_pps
        if self.out_bps is not None:
            result['OutBps'] = self.out_bps
        if self.attack_bps is not None:
            result['AttackBps'] = self.attack_bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')
        if m.get('AttackPps') is not None:
            self.attack_pps = m.get('AttackPps')
        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')
        if m.get('AttackBps') is not None:
            self.attack_bps = m.get('AttackBps')
        return self


class DescribePortFlowListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        port_flow_list: List[DescribePortFlowListResponseBodyPortFlowList] = None,
    ):
        self.request_id = request_id
        self.port_flow_list = port_flow_list

    def validate(self):
        if self.port_flow_list:
            for k in self.port_flow_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PortFlowList'] = []
        if self.port_flow_list is not None:
            for k in self.port_flow_list:
                result['PortFlowList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.port_flow_list = []
        if m.get('PortFlowList') is not None:
            for k in m.get('PortFlowList'):
                temp_model = DescribePortFlowListResponseBodyPortFlowList()
                self.port_flow_list.append(temp_model.from_map(k))
        return self


class DescribePortFlowListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePortFlowListResponseBody = None,
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
            temp_model = DescribePortFlowListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortMaxConnsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        end_time: int = None,
        start_time: int = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.end_time = end_time
        self.start_time = start_time
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortMaxConnsResponseBodyPortMaxConns(TeaModel):
    def __init__(
        self,
        cps: int = None,
        ip: str = None,
        port: str = None,
    ):
        self.cps = cps
        self.ip = ip
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribePortMaxConnsResponseBody(TeaModel):
    def __init__(
        self,
        port_max_conns: List[DescribePortMaxConnsResponseBodyPortMaxConns] = None,
        request_id: str = None,
    ):
        self.port_max_conns = port_max_conns
        self.request_id = request_id

    def validate(self):
        if self.port_max_conns:
            for k in self.port_max_conns:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PortMaxConns'] = []
        if self.port_max_conns is not None:
            for k in self.port_max_conns:
                result['PortMaxConns'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.port_max_conns = []
        if m.get('PortMaxConns') is not None:
            for k in m.get('PortMaxConns'):
                temp_model = DescribePortMaxConnsResponseBodyPortMaxConns()
                self.port_max_conns.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePortMaxConnsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePortMaxConnsResponseBody = None,
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
            temp_model = DescribePortMaxConnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortViewSourceCountriesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        end_time: int = None,
        start_time: int = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.end_time = end_time
        self.start_time = start_time
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortViewSourceCountriesResponseBodySourceCountrys(TeaModel):
    def __init__(
        self,
        country_id: str = None,
        count: int = None,
    ):
        self.country_id = country_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePortViewSourceCountriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        source_countrys: List[DescribePortViewSourceCountriesResponseBodySourceCountrys] = None,
    ):
        self.request_id = request_id
        self.source_countrys = source_countrys

    def validate(self):
        if self.source_countrys:
            for k in self.source_countrys:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SourceCountrys'] = []
        if self.source_countrys is not None:
            for k in self.source_countrys:
                result['SourceCountrys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.source_countrys = []
        if m.get('SourceCountrys') is not None:
            for k in m.get('SourceCountrys'):
                temp_model = DescribePortViewSourceCountriesResponseBodySourceCountrys()
                self.source_countrys.append(temp_model.from_map(k))
        return self


class DescribePortViewSourceCountriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePortViewSourceCountriesResponseBody = None,
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
            temp_model = DescribePortViewSourceCountriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortViewSourceIspsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        end_time: int = None,
        start_time: int = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.end_time = end_time
        self.start_time = start_time
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortViewSourceIspsResponseBodyIsps(TeaModel):
    def __init__(
        self,
        isp_id: str = None,
        count: int = None,
    ):
        self.isp_id = isp_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.isp_id is not None:
            result['IspId'] = self.isp_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IspId') is not None:
            self.isp_id = m.get('IspId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePortViewSourceIspsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        isps: List[DescribePortViewSourceIspsResponseBodyIsps] = None,
    ):
        self.request_id = request_id
        self.isps = isps

    def validate(self):
        if self.isps:
            for k in self.isps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Isps'] = []
        if self.isps is not None:
            for k in self.isps:
                result['Isps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.isps = []
        if m.get('Isps') is not None:
            for k in m.get('Isps'):
                temp_model = DescribePortViewSourceIspsResponseBodyIsps()
                self.isps.append(temp_model.from_map(k))
        return self


class DescribePortViewSourceIspsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePortViewSourceIspsResponseBody = None,
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
            temp_model = DescribePortViewSourceIspsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortViewSourceProvincesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        end_time: int = None,
        start_time: int = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.end_time = end_time
        self.start_time = start_time
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortViewSourceProvincesResponseBodySourceProvinces(TeaModel):
    def __init__(
        self,
        province_id: str = None,
        count: int = None,
    ):
        self.province_id = province_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePortViewSourceProvincesResponseBody(TeaModel):
    def __init__(
        self,
        source_provinces: List[DescribePortViewSourceProvincesResponseBodySourceProvinces] = None,
        request_id: str = None,
    ):
        self.source_provinces = source_provinces
        self.request_id = request_id

    def validate(self):
        if self.source_provinces:
            for k in self.source_provinces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SourceProvinces'] = []
        if self.source_provinces is not None:
            for k in self.source_provinces:
                result['SourceProvinces'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_provinces = []
        if m.get('SourceProvinces') is not None:
            for k in m.get('SourceProvinces'):
                temp_model = DescribePortViewSourceProvincesResponseBodySourceProvinces()
                self.source_provinces.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePortViewSourceProvincesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePortViewSourceProvincesResponseBody = None,
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
            temp_model = DescribePortViewSourceProvincesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneDefenseObjectsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        policy_id: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.policy_id = policy_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSceneDefenseObjectsResponseBodyObjects(TeaModel):
    def __init__(
        self,
        domain: str = None,
        policy_id: str = None,
        vip: str = None,
    ):
        self.domain = domain
        self.policy_id = policy_id
        self.vip = vip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.vip is not None:
            result['Vip'] = self.vip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Vip') is not None:
            self.vip = m.get('Vip')
        return self


class DescribeSceneDefenseObjectsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        objects: List[DescribeSceneDefenseObjectsResponseBodyObjects] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.objects = objects
        self.success = success

    def validate(self):
        if self.objects:
            for k in self.objects:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Objects'] = []
        if self.objects is not None:
            for k in self.objects:
                result['Objects'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.objects = []
        if m.get('Objects') is not None:
            for k in m.get('Objects'):
                temp_model = DescribeSceneDefenseObjectsResponseBodyObjects()
                self.objects.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSceneDefenseObjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSceneDefenseObjectsResponseBody = None,
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
            temp_model = DescribeSceneDefenseObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneDefensePoliciesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        template: str = None,
        status: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.template = template
        self.status = status
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.template is not None:
            result['Template'] = self.template
        if self.status is not None:
            result['Status'] = self.status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies(TeaModel):
    def __init__(
        self,
        status: int = None,
        old_value: str = None,
        new_value: str = None,
        policy_type: int = None,
    ):
        self.status = status
        self.old_value = old_value
        self.new_value = new_value
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.old_value is not None:
            result['oldValue'] = self.old_value
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('oldValue') is not None:
            self.old_value = m.get('oldValue')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class DescribeSceneDefensePoliciesResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        done: int = None,
        end_time: int = None,
        status: int = None,
        start_time: int = None,
        object_count: int = None,
        template: str = None,
        policy_id: str = None,
        name: str = None,
        runtime_policies: List[DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies] = None,
    ):
        self.done = done
        self.end_time = end_time
        self.status = status
        self.start_time = start_time
        self.object_count = object_count
        self.template = template
        self.policy_id = policy_id
        self.name = name
        self.runtime_policies = runtime_policies

    def validate(self):
        if self.runtime_policies:
            for k in self.runtime_policies:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.done is not None:
            result['Done'] = self.done
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.object_count is not None:
            result['ObjectCount'] = self.object_count
        if self.template is not None:
            result['Template'] = self.template
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.name is not None:
            result['Name'] = self.name
        result['RuntimePolicies'] = []
        if self.runtime_policies is not None:
            for k in self.runtime_policies:
                result['RuntimePolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Done') is not None:
            self.done = m.get('Done')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ObjectCount') is not None:
            self.object_count = m.get('ObjectCount')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.runtime_policies = []
        if m.get('RuntimePolicies') is not None:
            for k in m.get('RuntimePolicies'):
                temp_model = DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies()
                self.runtime_policies.append(temp_model.from_map(k))
        return self


class DescribeSceneDefensePoliciesResponseBody(TeaModel):
    def __init__(
        self,
        policies: List[DescribeSceneDefensePoliciesResponseBodyPolicies] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.policies = policies
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = DescribeSceneDefensePoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSceneDefensePoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSceneDefensePoliciesResponseBody = None,
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
            temp_model = DescribeSceneDefensePoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSchedulerRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        rule_name: str = None,
        offset: int = None,
        page_number: int = None,
        page_size: int = None,
        is_offset: bool = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.rule_name = rule_name
        self.offset = offset
        self.page_number = page_number
        self.page_size = page_size
        self.is_offset = is_offset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.is_offset is not None:
            result['IsOffset'] = self.is_offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IsOffset') is not None:
            self.is_offset = m.get('IsOffset')
        return self


class DescribeSchedulerRulesResponseBodySchedulerRulesParamParamData(TeaModel):
    def __init__(
        self,
        cloud_instance_id: str = None,
    ):
        self.cloud_instance_id = cloud_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cloud_instance_id is not None:
            result['CloudInstanceId'] = self.cloud_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudInstanceId') is not None:
            self.cloud_instance_id = m.get('CloudInstanceId')
        return self


class DescribeSchedulerRulesResponseBodySchedulerRulesParam(TeaModel):
    def __init__(
        self,
        param_data: DescribeSchedulerRulesResponseBodySchedulerRulesParamParamData = None,
        param_type: str = None,
    ):
        self.param_data = param_data
        self.param_type = param_type

    def validate(self):
        if self.param_data:
            self.param_data.validate()

    def to_map(self):
        result = dict()
        if self.param_data is not None:
            result['ParamData'] = self.param_data.to_map()
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamData') is not None:
            temp_model = DescribeSchedulerRulesResponseBodySchedulerRulesParamParamData()
            self.param_data = temp_model.from_map(m['ParamData'])
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        return self


class DescribeSchedulerRulesResponseBodySchedulerRulesRules(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: int = None,
        value: str = None,
        value_type: int = None,
        priority: int = None,
        restore_delay: int = None,
        region_id: str = None,
    ):
        self.type = type
        self.status = status
        self.value = value
        self.value_type = value_type
        self.priority = priority
        self.restore_delay = restore_delay
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.restore_delay is not None:
            result['RestoreDelay'] = self.restore_delay
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RestoreDelay') is not None:
            self.restore_delay = m.get('RestoreDelay')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSchedulerRulesResponseBodySchedulerRules(TeaModel):
    def __init__(
        self,
        rule_type: str = None,
        param: DescribeSchedulerRulesResponseBodySchedulerRulesParam = None,
        cname: str = None,
        rules: List[DescribeSchedulerRulesResponseBodySchedulerRulesRules] = None,
        rule_name: str = None,
    ):
        self.rule_type = rule_type
        self.param = param
        self.cname = cname
        self.rules = rules
        self.rule_name = rule_name

    def validate(self):
        if self.param:
            self.param.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.cname is not None:
            result['Cname'] = self.cname
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Param') is not None:
            temp_model = DescribeSchedulerRulesResponseBodySchedulerRulesParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeSchedulerRulesResponseBodySchedulerRulesRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeSchedulerRulesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: str = None,
        request_id: str = None,
        scheduler_rules: List[DescribeSchedulerRulesResponseBodySchedulerRules] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.scheduler_rules = scheduler_rules

    def validate(self):
        if self.scheduler_rules:
            for k in self.scheduler_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SchedulerRules'] = []
        if self.scheduler_rules is not None:
            for k in self.scheduler_rules:
                result['SchedulerRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scheduler_rules = []
        if m.get('SchedulerRules') is not None:
            for k in m.get('SchedulerRules'):
                temp_model = DescribeSchedulerRulesResponseBodySchedulerRules()
                self.scheduler_rules.append(temp_model.from_map(k))
        return self


class DescribeSchedulerRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSchedulerRulesResponseBody = None,
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
            temp_model = DescribeSchedulerRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsAuthStatusRequest(TeaModel):
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


class DescribeSlsAuthStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sls_auth_status: bool = None,
    ):
        self.request_id = request_id
        self.sls_auth_status = sls_auth_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_auth_status is not None:
            result['SlsAuthStatus'] = self.sls_auth_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsAuthStatus') is not None:
            self.sls_auth_status = m.get('SlsAuthStatus')
        return self


class DescribeSlsAuthStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSlsAuthStatusResponseBody = None,
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
            temp_model = DescribeSlsAuthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsLogstoreInfoRequest(TeaModel):
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


class DescribeSlsLogstoreInfoResponseBody(TeaModel):
    def __init__(
        self,
        project: str = None,
        request_id: str = None,
        quota: int = None,
        log_store: str = None,
        used: int = None,
        ttl: int = None,
    ):
        self.project = project
        self.request_id = request_id
        self.quota = quota
        self.log_store = log_store
        self.used = used
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.used is not None:
            result['Used'] = self.used
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class DescribeSlsLogstoreInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSlsLogstoreInfoResponseBody = None,
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
            temp_model = DescribeSlsLogstoreInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsOpenStatusRequest(TeaModel):
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


class DescribeSlsOpenStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sls_open_status: bool = None,
    ):
        self.request_id = request_id
        self.sls_open_status = sls_open_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_open_status is not None:
            result['SlsOpenStatus'] = self.sls_open_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsOpenStatus') is not None:
            self.sls_open_status = m.get('SlsOpenStatus')
        return self


class DescribeSlsOpenStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSlsOpenStatusResponseBody = None,
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
            temp_model = DescribeSlsOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStsGrantStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        role: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class DescribeStsGrantStatusResponseBodyStsGrant(TeaModel):
    def __init__(
        self,
        status: int = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeStsGrantStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sts_grant: DescribeStsGrantStatusResponseBodyStsGrant = None,
    ):
        self.request_id = request_id
        self.sts_grant = sts_grant

    def validate(self):
        if self.sts_grant:
            self.sts_grant.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sts_grant is not None:
            result['StsGrant'] = self.sts_grant.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StsGrant') is not None:
            temp_model = DescribeStsGrantStatusResponseBodyStsGrant()
            self.sts_grant = temp_model.from_map(m['StsGrant'])
        return self


class DescribeStsGrantStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStsGrantStatusResponseBody = None,
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
            temp_model = DescribeStsGrantStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagKeysRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.source_ip = source_ip
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(
        self,
        tag_count: int = None,
        tag_key: str = None,
    ):
        self.tag_count = tag_count
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DescribeTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        tag_keys: List[DescribeTagKeysResponseBodyTagKeys] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.tag_keys = tag_keys

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = DescribeTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        return self


class DescribeTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTagKeysResponseBody = None,
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
            temp_model = DescribeTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagResourcesRequestTags(TeaModel):
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


class DescribeTagResourcesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        next_token: str = None,
        resource_ids: List[str] = None,
        tags: List[DescribeTagResourcesRequestTags] = None,
    ):
        self.source_ip = source_ip
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.next_token = next_token
        self.resource_ids = resource_ids
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeTagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_value: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.resource_type = resource_type
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DescribeTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[DescribeTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = DescribeTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: DescribeTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = DescribeTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class DescribeTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTagResourcesResponseBody = None,
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
            temp_model = DescribeTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUnBlackholeCountRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeUnBlackholeCountResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        remain_count: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.remain_count = remain_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.remain_count is not None:
            result['RemainCount'] = self.remain_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RemainCount') is not None:
            self.remain_count = m.get('RemainCount')
        return self


class DescribeUnBlackholeCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUnBlackholeCountResponseBody = None,
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
            temp_model = DescribeUnBlackholeCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUnBlockCountRequest(TeaModel):
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


class DescribeUnBlockCountResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        remain_count: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.remain_count = remain_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.remain_count is not None:
            result['RemainCount'] = self.remain_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RemainCount') is not None:
            self.remain_count = m.get('RemainCount')
        return self


class DescribeUnBlockCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUnBlockCountResponseBody = None,
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
            temp_model = DescribeUnBlockCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAccessLogDispatchStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.page_number = page_number
        self.page_size = page_size

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enable: bool = None,
    ):
        self.domain = domain
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeWebAccessLogDispatchStatusResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        sls_config_status: List[DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.sls_config_status = sls_config_status

    def validate(self):
        if self.sls_config_status:
            for k in self.sls_config_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SlsConfigStatus'] = []
        if self.sls_config_status is not None:
            for k in self.sls_config_status:
                result['SlsConfigStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sls_config_status = []
        if m.get('SlsConfigStatus') is not None:
            for k in m.get('SlsConfigStatus'):
                temp_model = DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus()
                self.sls_config_status.append(temp_model.from_map(k))
        return self


class DescribeWebAccessLogDispatchStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebAccessLogDispatchStatusResponseBody = None,
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
            temp_model = DescribeWebAccessLogDispatchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAccessLogEmptyCountRequest(TeaModel):
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


class DescribeWebAccessLogEmptyCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        available_count: int = None,
    ):
        self.request_id = request_id
        self.available_count = available_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.available_count is not None:
            result['AvailableCount'] = self.available_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AvailableCount') is not None:
            self.available_count = m.get('AvailableCount')
        return self


class DescribeWebAccessLogEmptyCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebAccessLogEmptyCountResponseBody = None,
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
            temp_model = DescribeWebAccessLogEmptyCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAccessLogStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.domain = domain

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
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeWebAccessLogStatusResponseBody(TeaModel):
    def __init__(
        self,
        sls_project: str = None,
        sls_status: bool = None,
        request_id: str = None,
        sls_logstore: str = None,
    ):
        self.sls_project = sls_project
        self.sls_status = sls_status
        self.request_id = request_id
        self.sls_logstore = sls_logstore

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        if self.sls_status is not None:
            result['SlsStatus'] = self.sls_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        if m.get('SlsStatus') is not None:
            self.sls_status = m.get('SlsStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsLogstore') is not None:
            self.sls_logstore = m.get('SlsLogstore')
        return self


class DescribeWebAccessLogStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebAccessLogStatusResponseBody = None,
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
            temp_model = DescribeWebAccessLogStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAccessModeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        domains: List[str] = None,
    ):
        self.source_ip = source_ip
        self.domains = domains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebAccessModeResponseBodyDomainModes(TeaModel):
    def __init__(
        self,
        access_mode: int = None,
        domain: str = None,
    ):
        self.access_mode = access_mode
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeWebAccessModeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_modes: List[DescribeWebAccessModeResponseBodyDomainModes] = None,
    ):
        self.request_id = request_id
        self.domain_modes = domain_modes

    def validate(self):
        if self.domain_modes:
            for k in self.domain_modes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DomainModes'] = []
        if self.domain_modes is not None:
            for k in self.domain_modes:
                result['DomainModes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.domain_modes = []
        if m.get('DomainModes') is not None:
            for k in m.get('DomainModes'):
                temp_model = DescribeWebAccessModeResponseBodyDomainModes()
                self.domain_modes.append(temp_model.from_map(k))
        return self


class DescribeWebAccessModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebAccessModeResponseBody = None,
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
            temp_model = DescribeWebAccessModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAreaBlockConfigsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domains: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domains = domains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigsRegionList(TeaModel):
    def __init__(
        self,
        block: int = None,
        region: str = None,
    ):
        self.block = block
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigs(TeaModel):
    def __init__(
        self,
        domain: str = None,
        region_list: List[DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigsRegionList] = None,
    ):
        self.domain = domain
        self.region_list = region_list

    def validate(self):
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        result['RegionList'] = []
        if self.region_list is not None:
            for k in self.region_list:
                result['RegionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        self.region_list = []
        if m.get('RegionList') is not None:
            for k in m.get('RegionList'):
                temp_model = DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigsRegionList()
                self.region_list.append(temp_model.from_map(k))
        return self


class DescribeWebAreaBlockConfigsResponseBody(TeaModel):
    def __init__(
        self,
        area_block_configs: List[DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigs] = None,
        request_id: str = None,
    ):
        self.area_block_configs = area_block_configs
        self.request_id = request_id

    def validate(self):
        if self.area_block_configs:
            for k in self.area_block_configs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AreaBlockConfigs'] = []
        if self.area_block_configs is not None:
            for k in self.area_block_configs:
                result['AreaBlockConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.area_block_configs = []
        if m.get('AreaBlockConfigs') is not None:
            for k in m.get('AreaBlockConfigs'):
                temp_model = DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigs()
                self.area_block_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebAreaBlockConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebAreaBlockConfigsResponseBody = None,
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
            temp_model = DescribeWebAreaBlockConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebCacheConfigsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domains: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domains = domains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules(TeaModel):
    def __init__(
        self,
        cache_ttl: int = None,
        mode: str = None,
        name: str = None,
        uri: str = None,
    ):
        self.cache_ttl = cache_ttl
        self.mode = mode
        self.name = name
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cache_ttl is not None:
            result['CacheTtl'] = self.cache_ttl
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheTtl') is not None:
            self.cache_ttl = m.get('CacheTtl')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeWebCacheConfigsResponseBodyDomainCacheConfigs(TeaModel):
    def __init__(
        self,
        domain: str = None,
        custom_rules: List[DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules] = None,
        mode: str = None,
        enable: int = None,
    ):
        self.domain = domain
        self.custom_rules = custom_rules
        self.mode = mode
        self.enable = enable

    def validate(self):
        if self.custom_rules:
            for k in self.custom_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        result['CustomRules'] = []
        if self.custom_rules is not None:
            for k in self.custom_rules:
                result['CustomRules'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        self.custom_rules = []
        if m.get('CustomRules') is not None:
            for k in m.get('CustomRules'):
                temp_model = DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules()
                self.custom_rules.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeWebCacheConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_cache_configs: List[DescribeWebCacheConfigsResponseBodyDomainCacheConfigs] = None,
    ):
        self.request_id = request_id
        self.domain_cache_configs = domain_cache_configs

    def validate(self):
        if self.domain_cache_configs:
            for k in self.domain_cache_configs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DomainCacheConfigs'] = []
        if self.domain_cache_configs is not None:
            for k in self.domain_cache_configs:
                result['DomainCacheConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.domain_cache_configs = []
        if m.get('DomainCacheConfigs') is not None:
            for k in m.get('DomainCacheConfigs'):
                temp_model = DescribeWebCacheConfigsResponseBodyDomainCacheConfigs()
                self.domain_cache_configs.append(temp_model.from_map(k))
        return self


class DescribeWebCacheConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebCacheConfigsResponseBody = None,
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
            temp_model = DescribeWebCacheConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebCcProtectSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domains: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domains = domains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebCcProtectSwitchResponseBodyProtectSwitchList(TeaModel):
    def __init__(
        self,
        black_white_list_enable: int = None,
        ai_template: str = None,
        precise_rule_enable: int = None,
        domain: str = None,
        ai_mode: str = None,
        ai_rule_enable: int = None,
        region_block_enable: int = None,
        cc_template: str = None,
        cc_custom_rule_enable: int = None,
        cc_enable: int = None,
    ):
        self.black_white_list_enable = black_white_list_enable
        self.ai_template = ai_template
        self.precise_rule_enable = precise_rule_enable
        self.domain = domain
        self.ai_mode = ai_mode
        self.ai_rule_enable = ai_rule_enable
        self.region_block_enable = region_block_enable
        self.cc_template = cc_template
        self.cc_custom_rule_enable = cc_custom_rule_enable
        self.cc_enable = cc_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.black_white_list_enable is not None:
            result['BlackWhiteListEnable'] = self.black_white_list_enable
        if self.ai_template is not None:
            result['AiTemplate'] = self.ai_template
        if self.precise_rule_enable is not None:
            result['PreciseRuleEnable'] = self.precise_rule_enable
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ai_mode is not None:
            result['AiMode'] = self.ai_mode
        if self.ai_rule_enable is not None:
            result['AiRuleEnable'] = self.ai_rule_enable
        if self.region_block_enable is not None:
            result['RegionBlockEnable'] = self.region_block_enable
        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template
        if self.cc_custom_rule_enable is not None:
            result['CcCustomRuleEnable'] = self.cc_custom_rule_enable
        if self.cc_enable is not None:
            result['CcEnable'] = self.cc_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackWhiteListEnable') is not None:
            self.black_white_list_enable = m.get('BlackWhiteListEnable')
        if m.get('AiTemplate') is not None:
            self.ai_template = m.get('AiTemplate')
        if m.get('PreciseRuleEnable') is not None:
            self.precise_rule_enable = m.get('PreciseRuleEnable')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('AiMode') is not None:
            self.ai_mode = m.get('AiMode')
        if m.get('AiRuleEnable') is not None:
            self.ai_rule_enable = m.get('AiRuleEnable')
        if m.get('RegionBlockEnable') is not None:
            self.region_block_enable = m.get('RegionBlockEnable')
        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')
        if m.get('CcCustomRuleEnable') is not None:
            self.cc_custom_rule_enable = m.get('CcCustomRuleEnable')
        if m.get('CcEnable') is not None:
            self.cc_enable = m.get('CcEnable')
        return self


class DescribeWebCcProtectSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        protect_switch_list: List[DescribeWebCcProtectSwitchResponseBodyProtectSwitchList] = None,
    ):
        self.request_id = request_id
        self.protect_switch_list = protect_switch_list

    def validate(self):
        if self.protect_switch_list:
            for k in self.protect_switch_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ProtectSwitchList'] = []
        if self.protect_switch_list is not None:
            for k in self.protect_switch_list:
                result['ProtectSwitchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.protect_switch_list = []
        if m.get('ProtectSwitchList') is not None:
            for k in m.get('ProtectSwitchList'):
                temp_model = DescribeWebCcProtectSwitchResponseBodyProtectSwitchList()
                self.protect_switch_list.append(temp_model.from_map(k))
        return self


class DescribeWebCcProtectSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebCcProtectSwitchResponseBody = None,
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
            temp_model = DescribeWebCcProtectSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebCCRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        offset: int = None,
        page_number: int = None,
        page_size: str = None,
        is_offset: bool = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.offset = offset
        self.page_number = page_number
        self.page_size = page_size
        self.is_offset = is_offset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.is_offset is not None:
            result['IsOffset'] = self.is_offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IsOffset') is not None:
            self.is_offset = m.get('IsOffset')
        return self


class DescribeWebCCRulesResponseBodyWebCCRules(TeaModel):
    def __init__(
        self,
        ttl: int = None,
        act: str = None,
        interval: int = None,
        mode: str = None,
        name: str = None,
        uri: str = None,
        count: int = None,
    ):
        self.ttl = ttl
        self.act = act
        self.interval = interval
        self.mode = mode
        self.name = name
        self.uri = uri
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.act is not None:
            result['Act'] = self.act
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeWebCCRulesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        web_ccrules: List[DescribeWebCCRulesResponseBodyWebCCRules] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.web_ccrules = web_ccrules

    def validate(self):
        if self.web_ccrules:
            for k in self.web_ccrules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['WebCCRules'] = []
        if self.web_ccrules is not None:
            for k in self.web_ccrules:
                result['WebCCRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.web_ccrules = []
        if m.get('WebCCRules') is not None:
            for k in m.get('WebCCRules'):
                temp_model = DescribeWebCCRulesResponseBodyWebCCRules()
                self.web_ccrules.append(temp_model.from_map(k))
        return self


class DescribeWebCCRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebCCRulesResponseBody = None,
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
            temp_model = DescribeWebCCRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebCustomPortsRequest(TeaModel):
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


class DescribeWebCustomPortsResponseBodyWebCustomPorts(TeaModel):
    def __init__(
        self,
        proxy_ports: List[str] = None,
        proxy_type: str = None,
    ):
        self.proxy_ports = proxy_ports
        self.proxy_type = proxy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyPorts') is not None:
            self.proxy_ports = m.get('ProxyPorts')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        return self


class DescribeWebCustomPortsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        web_custom_ports: List[DescribeWebCustomPortsResponseBodyWebCustomPorts] = None,
    ):
        self.request_id = request_id
        self.web_custom_ports = web_custom_ports

    def validate(self):
        if self.web_custom_ports:
            for k in self.web_custom_ports:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['WebCustomPorts'] = []
        if self.web_custom_ports is not None:
            for k in self.web_custom_ports:
                result['WebCustomPorts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.web_custom_ports = []
        if m.get('WebCustomPorts') is not None:
            for k in m.get('WebCustomPorts'):
                temp_model = DescribeWebCustomPortsResponseBodyWebCustomPorts()
                self.web_custom_ports.append(temp_model.from_map(k))
        return self


class DescribeWebCustomPortsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebCustomPortsResponseBody = None,
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
            temp_model = DescribeWebCustomPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebInstanceRelationsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domains: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domains = domains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebInstanceRelationsResponseBodyWebInstanceRelationsInstanceDetails(TeaModel):
    def __init__(
        self,
        eip_list: List[str] = None,
        function_version: str = None,
        instance_id: str = None,
    ):
        self.eip_list = eip_list
        self.function_version = function_version
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.eip_list is not None:
            result['EipList'] = self.eip_list
        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipList') is not None:
            self.eip_list = m.get('EipList')
        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeWebInstanceRelationsResponseBodyWebInstanceRelations(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_details: List[DescribeWebInstanceRelationsResponseBodyWebInstanceRelationsInstanceDetails] = None,
    ):
        self.domain = domain
        self.instance_details = instance_details

    def validate(self):
        if self.instance_details:
            for k in self.instance_details:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k in self.instance_details:
                result['InstanceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        self.instance_details = []
        if m.get('InstanceDetails') is not None:
            for k in m.get('InstanceDetails'):
                temp_model = DescribeWebInstanceRelationsResponseBodyWebInstanceRelationsInstanceDetails()
                self.instance_details.append(temp_model.from_map(k))
        return self


class DescribeWebInstanceRelationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        web_instance_relations: List[DescribeWebInstanceRelationsResponseBodyWebInstanceRelations] = None,
    ):
        self.request_id = request_id
        self.web_instance_relations = web_instance_relations

    def validate(self):
        if self.web_instance_relations:
            for k in self.web_instance_relations:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['WebInstanceRelations'] = []
        if self.web_instance_relations is not None:
            for k in self.web_instance_relations:
                result['WebInstanceRelations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.web_instance_relations = []
        if m.get('WebInstanceRelations') is not None:
            for k in m.get('WebInstanceRelations'):
                temp_model = DescribeWebInstanceRelationsResponseBodyWebInstanceRelations()
                self.web_instance_relations.append(temp_model.from_map(k))
        return self


class DescribeWebInstanceRelationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebInstanceRelationsResponseBody = None,
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
            temp_model = DescribeWebInstanceRelationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebPreciseAccessRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domains: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domains = domains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList(TeaModel):
    def __init__(
        self,
        match_method: str = None,
        field: str = None,
        content: str = None,
        header_name: str = None,
    ):
        self.match_method = match_method
        self.field = field
        self.content = content
        self.header_name = header_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.match_method is not None:
            result['MatchMethod'] = self.match_method
        if self.field is not None:
            result['Field'] = self.field
        if self.content is not None:
            result['Content'] = self.content
        if self.header_name is not None:
            result['HeaderName'] = self.header_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchMethod') is not None:
            self.match_method = m.get('MatchMethod')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('HeaderName') is not None:
            self.header_name = m.get('HeaderName')
        return self


class DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleList(TeaModel):
    def __init__(
        self,
        action: str = None,
        owner: str = None,
        expires: int = None,
        name: str = None,
        condition_list: List[DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList] = None,
    ):
        self.action = action
        self.owner = owner
        self.expires = expires
        self.name = name
        self.condition_list = condition_list

    def validate(self):
        if self.condition_list:
            for k in self.condition_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.name is not None:
            result['Name'] = self.name
        result['ConditionList'] = []
        if self.condition_list is not None:
            for k in self.condition_list:
                result['ConditionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.condition_list = []
        if m.get('ConditionList') is not None:
            for k in m.get('ConditionList'):
                temp_model = DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList()
                self.condition_list.append(temp_model.from_map(k))
        return self


class DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        rule_list: List[DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleList] = None,
    ):
        self.domain = domain
        self.rule_list = rule_list

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleList()
                self.rule_list.append(temp_model.from_map(k))
        return self


class DescribeWebPreciseAccessRuleResponseBody(TeaModel):
    def __init__(
        self,
        precise_access_config_list: List[DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigList] = None,
        request_id: str = None,
    ):
        self.precise_access_config_list = precise_access_config_list
        self.request_id = request_id

    def validate(self):
        if self.precise_access_config_list:
            for k in self.precise_access_config_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PreciseAccessConfigList'] = []
        if self.precise_access_config_list is not None:
            for k in self.precise_access_config_list:
                result['PreciseAccessConfigList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.precise_access_config_list = []
        if m.get('PreciseAccessConfigList') is not None:
            for k in m.get('PreciseAccessConfigList'):
                temp_model = DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigList()
                self.precise_access_config_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebPreciseAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebPreciseAccessRuleResponseBody = None,
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
            temp_model = DescribeWebPreciseAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        query_domain_pattern: str = None,
        page_number: int = None,
        page_size: int = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.query_domain_pattern = query_domain_pattern
        self.page_number = page_number
        self.page_size = page_size
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.query_domain_pattern is not None:
            result['QueryDomainPattern'] = self.query_domain_pattern
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('QueryDomainPattern') is not None:
            self.query_domain_pattern = m.get('QueryDomainPattern')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeWebRulesResponseBodyWebRulesRealServers(TeaModel):
    def __init__(
        self,
        rs_type: int = None,
        real_server: str = None,
    ):
        self.rs_type = rs_type
        self.real_server = real_server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')
        return self


class DescribeWebRulesResponseBodyWebRulesProxyTypes(TeaModel):
    def __init__(
        self,
        proxy_ports: List[str] = None,
        proxy_type: str = None,
    ):
        self.proxy_ports = proxy_ports
        self.proxy_type = proxy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyPorts') is not None:
            self.proxy_ports = m.get('ProxyPorts')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        return self


class DescribeWebRulesResponseBodyWebRules(TeaModel):
    def __init__(
        self,
        domain: str = None,
        http_2https_enable: bool = None,
        custom_ciphers: List[str] = None,
        black_list: List[str] = None,
        white_list: List[str] = None,
        real_servers: List[DescribeWebRulesResponseBodyWebRulesRealServers] = None,
        proxy_types: List[DescribeWebRulesResponseBodyWebRulesProxyTypes] = None,
        ssl_protocols: str = None,
        cc_template: str = None,
        cc_enabled: bool = None,
        ssl_ciphers: str = None,
        cc_rule_enabled: bool = None,
        ssl_13enabled: bool = None,
        proxy_enabled: bool = None,
        cert_name: str = None,
        policy_mode: str = None,
        cname: str = None,
        http_2enable: bool = None,
        https_2http_enable: bool = None,
    ):
        self.domain = domain
        self.http_2https_enable = http_2https_enable
        self.custom_ciphers = custom_ciphers
        self.black_list = black_list
        self.white_list = white_list
        self.real_servers = real_servers
        self.proxy_types = proxy_types
        self.ssl_protocols = ssl_protocols
        self.cc_template = cc_template
        self.cc_enabled = cc_enabled
        self.ssl_ciphers = ssl_ciphers
        self.cc_rule_enabled = cc_rule_enabled
        self.ssl_13enabled = ssl_13enabled
        self.proxy_enabled = proxy_enabled
        self.cert_name = cert_name
        self.policy_mode = policy_mode
        self.cname = cname
        self.http_2enable = http_2enable
        self.https_2http_enable = https_2http_enable

    def validate(self):
        if self.real_servers:
            for k in self.real_servers:
                if k:
                    k.validate()
        if self.proxy_types:
            for k in self.proxy_types:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.http_2https_enable is not None:
            result['Http2HttpsEnable'] = self.http_2https_enable
        if self.custom_ciphers is not None:
            result['CustomCiphers'] = self.custom_ciphers
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        result['RealServers'] = []
        if self.real_servers is not None:
            for k in self.real_servers:
                result['RealServers'].append(k.to_map() if k else None)
        result['ProxyTypes'] = []
        if self.proxy_types is not None:
            for k in self.proxy_types:
                result['ProxyTypes'].append(k.to_map() if k else None)
        if self.ssl_protocols is not None:
            result['SslProtocols'] = self.ssl_protocols
        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template
        if self.cc_enabled is not None:
            result['CcEnabled'] = self.cc_enabled
        if self.ssl_ciphers is not None:
            result['SslCiphers'] = self.ssl_ciphers
        if self.cc_rule_enabled is not None:
            result['CcRuleEnabled'] = self.cc_rule_enabled
        if self.ssl_13enabled is not None:
            result['Ssl13Enabled'] = self.ssl_13enabled
        if self.proxy_enabled is not None:
            result['ProxyEnabled'] = self.proxy_enabled
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.policy_mode is not None:
            result['PolicyMode'] = self.policy_mode
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.http_2enable is not None:
            result['Http2Enable'] = self.http_2enable
        if self.https_2http_enable is not None:
            result['Https2HttpEnable'] = self.https_2http_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Http2HttpsEnable') is not None:
            self.http_2https_enable = m.get('Http2HttpsEnable')
        if m.get('CustomCiphers') is not None:
            self.custom_ciphers = m.get('CustomCiphers')
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        self.real_servers = []
        if m.get('RealServers') is not None:
            for k in m.get('RealServers'):
                temp_model = DescribeWebRulesResponseBodyWebRulesRealServers()
                self.real_servers.append(temp_model.from_map(k))
        self.proxy_types = []
        if m.get('ProxyTypes') is not None:
            for k in m.get('ProxyTypes'):
                temp_model = DescribeWebRulesResponseBodyWebRulesProxyTypes()
                self.proxy_types.append(temp_model.from_map(k))
        if m.get('SslProtocols') is not None:
            self.ssl_protocols = m.get('SslProtocols')
        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')
        if m.get('CcEnabled') is not None:
            self.cc_enabled = m.get('CcEnabled')
        if m.get('SslCiphers') is not None:
            self.ssl_ciphers = m.get('SslCiphers')
        if m.get('CcRuleEnabled') is not None:
            self.cc_rule_enabled = m.get('CcRuleEnabled')
        if m.get('Ssl13Enabled') is not None:
            self.ssl_13enabled = m.get('Ssl13Enabled')
        if m.get('ProxyEnabled') is not None:
            self.proxy_enabled = m.get('ProxyEnabled')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('PolicyMode') is not None:
            self.policy_mode = m.get('PolicyMode')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Http2Enable') is not None:
            self.http_2enable = m.get('Http2Enable')
        if m.get('Https2HttpEnable') is not None:
            self.https_2http_enable = m.get('Https2HttpEnable')
        return self


class DescribeWebRulesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        web_rules: List[DescribeWebRulesResponseBodyWebRules] = None,
        request_id: str = None,
    ):
        self.total_count = total_count
        self.web_rules = web_rules
        self.request_id = request_id

    def validate(self):
        if self.web_rules:
            for k in self.web_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WebRules'] = []
        if self.web_rules is not None:
            for k in self.web_rules:
                result['WebRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.web_rules = []
        if m.get('WebRules') is not None:
            for k in m.get('WebRules'):
                temp_model = DescribeWebRulesResponseBodyWebRules()
                self.web_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebRulesResponseBody = None,
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
            temp_model = DescribeWebRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachSceneDefenseObjectRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        policy_id: str = None,
        object_type: str = None,
        objects: str = None,
    ):
        self.source_ip = source_ip
        self.policy_id = policy_id
        self.object_type = object_type
        self.objects = objects

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.objects is not None:
            result['Objects'] = self.objects
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Objects') is not None:
            self.objects = m.get('Objects')
        return self


class DetachSceneDefenseObjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetachSceneDefenseObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachSceneDefenseObjectResponseBody = None,
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
            temp_model = DetachSceneDefenseObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSceneDefensePolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        policy_id: str = None,
    ):
        self.source_ip = source_ip
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DisableSceneDefensePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableSceneDefensePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableSceneDefensePolicyResponseBody = None,
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
            temp_model = DisableSceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableWebAccessLogConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.domain = domain

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
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DisableWebAccessLogConfigResponseBody(TeaModel):
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


class DisableWebAccessLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableWebAccessLogConfigResponseBody = None,
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
            temp_model = DisableWebAccessLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableWebCCRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DisableWebCCResponseBody(TeaModel):
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


class DisableWebCCResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableWebCCResponseBody = None,
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
            temp_model = DisableWebCCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableWebCCRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DisableWebCCRuleResponseBody(TeaModel):
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


class DisableWebCCRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableWebCCRuleResponseBody = None,
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
            temp_model = DisableWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmptyAutoCcBlacklistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EmptyAutoCcBlacklistResponseBody(TeaModel):
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


class EmptyAutoCcBlacklistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EmptyAutoCcBlacklistResponseBody = None,
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
            temp_model = EmptyAutoCcBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmptyAutoCcWhitelistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EmptyAutoCcWhitelistResponseBody(TeaModel):
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


class EmptyAutoCcWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EmptyAutoCcWhitelistResponseBody = None,
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
            temp_model = EmptyAutoCcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmptySlsLogstoreRequest(TeaModel):
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


class EmptySlsLogstoreResponseBody(TeaModel):
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


class EmptySlsLogstoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EmptySlsLogstoreResponseBody = None,
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
            temp_model = EmptySlsLogstoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSceneDefensePolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        policy_id: str = None,
    ):
        self.source_ip = source_ip
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class EnableSceneDefensePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableSceneDefensePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableSceneDefensePolicyResponseBody = None,
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
            temp_model = EnableSceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWebAccessLogConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.domain = domain

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
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class EnableWebAccessLogConfigResponseBody(TeaModel):
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


class EnableWebAccessLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableWebAccessLogConfigResponseBody = None,
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
            temp_model = EnableWebAccessLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWebCCRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class EnableWebCCResponseBody(TeaModel):
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


class EnableWebCCResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableWebCCResponseBody = None,
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
            temp_model = EnableWebCCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWebCCRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class EnableWebCCRuleResponseBody(TeaModel):
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


class EnableWebCCRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableWebCCRuleResponseBody = None,
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
            temp_model = EnableWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBlackholeStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        blackhole_status: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.blackhole_status = blackhole_status
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.blackhole_status is not None:
            result['BlackholeStatus'] = self.blackhole_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('BlackholeStatus') is not None:
            self.blackhole_status = m.get('BlackholeStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyBlackholeStatusResponseBody(TeaModel):
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


class ModifyBlackholeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBlackholeStatusResponseBody = None,
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
            temp_model = ModifyBlackholeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBlockStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        status: str = None,
        duration: int = None,
        instance_id: str = None,
        lines: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.status = status
        self.duration = duration
        self.instance_id = instance_id
        self.lines = lines

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lines is not None:
            result['Lines'] = self.lines
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        return self


class ModifyBlockStatusResponseBody(TeaModel):
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


class ModifyBlockStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBlockStatusResponseBody = None,
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
            temp_model = ModifyBlockStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCnameReuseRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        cname: str = None,
        enable: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.cname = cname
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyCnameReuseResponseBody(TeaModel):
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


class ModifyCnameReuseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCnameReuseResponseBody = None,
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
            temp_model = ModifyCnameReuseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyElasticBandWidthRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        elastic_bandwidth: int = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.elastic_bandwidth = elastic_bandwidth
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyElasticBandWidthResponseBody(TeaModel):
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


class ModifyElasticBandWidthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyElasticBandWidthResponseBody = None,
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
            temp_model = ModifyElasticBandWidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFullLogTtlRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ttl: int = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ttl = ttl
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyFullLogTtlResponseBody(TeaModel):
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


class ModifyFullLogTtlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyFullLogTtlResponseBody = None,
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
            temp_model = ModifyFullLogTtlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHealthCheckConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        forward_protocol: str = None,
        frontend_port: int = None,
        health_check: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.forward_protocol = forward_protocol
        self.frontend_port = frontend_port
        self.health_check = health_check

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        return self


class ModifyHealthCheckConfigResponseBody(TeaModel):
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


class ModifyHealthCheckConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHealthCheckConfigResponseBody = None,
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
            temp_model = ModifyHealthCheckConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHttp2EnableRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        enable: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyHttp2EnableResponseBody(TeaModel):
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


class ModifyHttp2EnableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHttp2EnableResponseBody = None,
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
            temp_model = ModifyHttp2EnableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceRemarkRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        remark: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ModifyInstanceRemarkResponseBody(TeaModel):
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


class ModifyInstanceRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceRemarkResponseBody = None,
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
            temp_model = ModifyInstanceRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNetworkRuleAttributeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        forward_protocol: str = None,
        frontend_port: int = None,
        config: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.forward_protocol = forward_protocol
        self.frontend_port = frontend_port
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyNetworkRuleAttributeResponseBody(TeaModel):
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


class ModifyNetworkRuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyNetworkRuleAttributeResponseBody = None,
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
            temp_model = ModifyNetworkRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPortAutoCcStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id: str = None,
        switch: str = None,
        mode: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id = instance_id
        self.switch = switch
        self.mode = mode

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
        if self.switch is not None:
            result['Switch'] = self.switch
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Switch') is not None:
            self.switch = m.get('Switch')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class ModifyPortAutoCcStatusResponseBody(TeaModel):
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


class ModifyPortAutoCcStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPortAutoCcStatusResponseBody = None,
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
            temp_model = ModifyPortAutoCcStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySceneDefensePolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        policy_id: str = None,
        name: str = None,
        template: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.policy_id = policy_id
        self.name = name
        self.template = template
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.name is not None:
            result['Name'] = self.name
        if self.template is not None:
            result['Template'] = self.template
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ModifySceneDefensePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifySceneDefensePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySceneDefensePolicyResponseBody = None,
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
            temp_model = ModifySceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySchedulerRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        rules: str = None,
        rule_name: str = None,
        rule_type: int = None,
        param: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.rules = rules
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.param = param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.param is not None:
            result['Param'] = self.param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        return self


class ModifySchedulerRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cname: str = None,
        rule_name: str = None,
    ):
        self.request_id = request_id
        self.cname = cname
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ModifySchedulerRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySchedulerRuleResponseBody = None,
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
            temp_model = ModifySchedulerRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTlsConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        config: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyTlsConfigResponseBody(TeaModel):
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


class ModifyTlsConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyTlsConfigResponseBody = None,
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
            temp_model = ModifyTlsConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAccessModeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        domain: str = None,
        access_mode: int = None,
    ):
        self.source_ip = source_ip
        self.domain = domain
        self.access_mode = access_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        return self


class ModifyWebAccessModeResponseBody(TeaModel):
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


class ModifyWebAccessModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebAccessModeResponseBody = None,
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
            temp_model = ModifyWebAccessModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAIProtectModeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        config: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyWebAIProtectModeResponseBody(TeaModel):
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


class ModifyWebAIProtectModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebAIProtectModeResponseBody = None,
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
            temp_model = ModifyWebAIProtectModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAIProtectSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        config: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyWebAIProtectSwitchResponseBody(TeaModel):
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


class ModifyWebAIProtectSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebAIProtectSwitchResponseBody = None,
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
            temp_model = ModifyWebAIProtectSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAreaBlockRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        regions: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.regions = regions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.regions is not None:
            result['Regions'] = self.regions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        return self


class ModifyWebAreaBlockResponseBody(TeaModel):
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


class ModifyWebAreaBlockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebAreaBlockResponseBody = None,
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
            temp_model = ModifyWebAreaBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAreaBlockSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        config: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyWebAreaBlockSwitchResponseBody(TeaModel):
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


class ModifyWebAreaBlockSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebAreaBlockSwitchResponseBody = None,
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
            temp_model = ModifyWebAreaBlockSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebCacheCustomRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        rules: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class ModifyWebCacheCustomRuleResponseBody(TeaModel):
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


class ModifyWebCacheCustomRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebCacheCustomRuleResponseBody = None,
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
            temp_model = ModifyWebCacheCustomRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebCacheModeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        mode: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class ModifyWebCacheModeResponseBody(TeaModel):
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


class ModifyWebCacheModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebCacheModeResponseBody = None,
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
            temp_model = ModifyWebCacheModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebCacheSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        enable: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyWebCacheSwitchResponseBody(TeaModel):
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


class ModifyWebCacheSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebCacheSwitchResponseBody = None,
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
            temp_model = ModifyWebCacheSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebCCRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        name: str = None,
        act: str = None,
        count: int = None,
        interval: int = None,
        mode: str = None,
        ttl: int = None,
        uri: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.name = name
        self.act = act
        self.count = count
        self.interval = interval
        self.mode = mode
        self.ttl = ttl
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class ModifyWebCCRuleResponseBody(TeaModel):
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


class ModifyWebCCRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebCCRuleResponseBody = None,
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
            temp_model = ModifyWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebIpSetSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        config: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyWebIpSetSwitchResponseBody(TeaModel):
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


class ModifyWebIpSetSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebIpSetSwitchResponseBody = None,
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
            temp_model = ModifyWebIpSetSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebPreciseAccessRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        rules: str = None,
        expires: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.rules = rules
        self.expires = expires

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.expires is not None:
            result['Expires'] = self.expires
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        return self


class ModifyWebPreciseAccessRuleResponseBody(TeaModel):
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


class ModifyWebPreciseAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebPreciseAccessRuleResponseBody = None,
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
            temp_model = ModifyWebPreciseAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebPreciseAccessSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        config: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyWebPreciseAccessSwitchResponseBody(TeaModel):
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


class ModifyWebPreciseAccessSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebPreciseAccessSwitchResponseBody = None,
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
            temp_model = ModifyWebPreciseAccessSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        proxy_types: str = None,
        rs_type: int = None,
        https_ext: str = None,
        real_servers: List[str] = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.proxy_types = proxy_types
        self.rs_type = rs_type
        self.https_ext = https_ext
        self.real_servers = real_servers
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.proxy_types is not None:
            result['ProxyTypes'] = self.proxy_types
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ProxyTypes') is not None:
            self.proxy_types = m.get('ProxyTypes')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class ModifyWebRuleResponseBody(TeaModel):
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


class ModifyWebRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebRuleResponseBody = None,
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
            temp_model = ModifyWebRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstanceRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ReleaseInstanceResponseBody(TeaModel):
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


class ReleaseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseInstanceResponseBody = None,
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
            temp_model = ReleaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchSchedulerRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        rule_name: str = None,
        rule_type: int = None,
        switch_data: str = None,
    ):
        self.source_ip = source_ip
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.switch_data = switch_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.switch_data is not None:
            result['SwitchData'] = self.switch_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SwitchData') is not None:
            self.switch_data = m.get('SwitchData')
        return self


class SwitchSchedulerRuleResponseBody(TeaModel):
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


class SwitchSchedulerRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SwitchSchedulerRuleResponseBody = None,
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
            temp_model = SwitchSchedulerRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


