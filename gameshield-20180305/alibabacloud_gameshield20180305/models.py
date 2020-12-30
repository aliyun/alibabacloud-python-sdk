# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CleanFlexAccFwdRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        esn_biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class CleanFlexAccFwdRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class CleanFlexAccFwdRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CleanFlexAccFwdRulesResponseBody = None,
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
            temp_model = CleanFlexAccFwdRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CleanFlexFwdRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class CleanFlexFwdRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class CleanFlexFwdRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CleanFlexFwdRulesResponseBody = None,
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
            temp_model = CleanFlexFwdRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearCcRouteRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class ClearCcRouteRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class ClearCcRouteRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ClearCcRouteRulesResponseBody = None,
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
            temp_model = ClearCcRouteRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_name: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_id: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.app_id = app_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppResponseBody = None,
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppKeyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class CreateAppKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class CreateAppKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppKeyResponseBody = None,
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
            temp_model = CreateAppKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBizRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
        app_name: str = None,
        biz_name: str = None,
        biz_type: int = None,
        use_cc: int = None,
        cc_qps: int = None,
        l_4rules: str = None,
        groups: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id
        self.app_name = app_name
        self.biz_name = biz_name
        self.biz_type = biz_type
        self.use_cc = use_cc
        self.cc_qps = cc_qps
        self.l_4rules = l_4rules
        self.groups = groups

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.use_cc is not None:
            result['UseCc'] = self.use_cc
        if self.cc_qps is not None:
            result['CcQps'] = self.cc_qps
        if self.l_4rules is not None:
            result['L4Rules'] = self.l_4rules
        if self.groups is not None:
            result['Groups'] = self.groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('UseCc') is not None:
            self.use_cc = m.get('UseCc')
        if m.get('CcQps') is not None:
            self.cc_qps = m.get('CcQps')
        if m.get('L4Rules') is not None:
            self.l_4rules = m.get('L4Rules')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        return self


class CreateBizResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class CreateBizResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBizResponseBody = None,
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
            temp_model = CreateBizResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCcRouteRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        route_list: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.route_list = route_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.route_list is not None:
            result['RouteList'] = self.route_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('RouteList') is not None:
            self.route_list = m.get('RouteList')
        return self


class CreateCcRouteRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class CreateCcRouteRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCcRouteRulesResponseBody = None,
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
            temp_model = CreateCcRouteRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlexAccFwdRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        biz_id: int = None,
        identity: str = None,
        ip_list: str = None,
        protocol_ex: str = None,
        domain_list: str = None,
        remark: str = None,
        master_ip_list: str = None,
        slave_ip_list: str = None,
        acc_type: int = None,
    ):
        self.source_ip = source_ip
        self.biz_id = biz_id
        self.identity = identity
        self.ip_list = ip_list
        self.protocol_ex = protocol_ex
        self.domain_list = domain_list
        self.remark = remark
        self.master_ip_list = master_ip_list
        self.slave_ip_list = slave_ip_list
        self.acc_type = acc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.protocol_ex is not None:
            result['ProtocolEx'] = self.protocol_ex
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.master_ip_list is not None:
            result['MasterIpList'] = self.master_ip_list
        if self.slave_ip_list is not None:
            result['SlaveIpList'] = self.slave_ip_list
        if self.acc_type is not None:
            result['AccType'] = self.acc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('ProtocolEx') is not None:
            self.protocol_ex = m.get('ProtocolEx')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('MasterIpList') is not None:
            self.master_ip_list = m.get('MasterIpList')
        if m.get('SlaveIpList') is not None:
            self.slave_ip_list = m.get('SlaveIpList')
        if m.get('AccType') is not None:
            self.acc_type = m.get('AccType')
        return self


class CreateFlexAccFwdRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class CreateFlexAccFwdRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFlexAccFwdRuleResponseBody = None,
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
            temp_model = CreateFlexAccFwdRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlexAccFwdRuleListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        biz_id: int = None,
        fwd_rule_list: str = None,
    ):
        self.source_ip = source_ip
        self.biz_id = biz_id
        self.fwd_rule_list = fwd_rule_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.fwd_rule_list is not None:
            result['FwdRuleList'] = self.fwd_rule_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('FwdRuleList') is not None:
            self.fwd_rule_list = m.get('FwdRuleList')
        return self


class CreateFlexAccFwdRuleListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class CreateFlexAccFwdRuleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFlexAccFwdRuleListResponseBody = None,
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
            temp_model = CreateFlexAccFwdRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlexFwdRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        identity: str = None,
        master_ip_list: str = None,
        slave_ip_list: str = None,
        remark: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.identity = identity
        self.master_ip_list = master_ip_list
        self.slave_ip_list = slave_ip_list
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.master_ip_list is not None:
            result['MasterIpList'] = self.master_ip_list
        if self.slave_ip_list is not None:
            result['SlaveIpList'] = self.slave_ip_list
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('MasterIpList') is not None:
            self.master_ip_list = m.get('MasterIpList')
        if m.get('SlaveIpList') is not None:
            self.slave_ip_list = m.get('SlaveIpList')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class CreateFlexFwdRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class CreateFlexFwdRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFlexFwdRuleResponseBody = None,
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
            temp_model = CreateFlexFwdRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        group_id: str = None,
        group_desc: str = None,
        ip_list: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.group_id = group_id
        self.group_desc = group_desc
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_desc is not None:
            result['GroupDesc'] = self.group_desc
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupDesc') is not None:
            self.group_desc = m.get('GroupDesc')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGroupResponseBody = None,
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
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayer4RuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
        biz_id: int = None,
        front_port: int = None,
        back_port: int = None,
        rservers: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id
        self.biz_id = biz_id
        self.front_port = front_port
        self.back_port = back_port
        self.rservers = rservers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.front_port is not None:
            result['FrontPort'] = self.front_port
        if self.back_port is not None:
            result['BackPort'] = self.back_port
        if self.rservers is not None:
            result['Rservers'] = self.rservers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')
        if m.get('BackPort') is not None:
            self.back_port = m.get('BackPort')
        if m.get('Rservers') is not None:
            self.rservers = m.get('Rservers')
        return self


class CreateLayer4RuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class CreateLayer4RuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLayer4RuleResponseBody = None,
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
            temp_model = CreateLayer4RuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayer4RulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        rules: str = None,
        flush: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.rules = rules
        self.flush = flush

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.flush is not None:
            result['Flush'] = self.flush
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('Flush') is not None:
            self.flush = m.get('Flush')
        return self


class CreateLayer4RulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class CreateLayer4RulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLayer4RulesResponseBody = None,
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
            temp_model = CreateLayer4RulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAppResponseBody = None,
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppKeyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteAppKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DeleteAppKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAppKeyResponseBody = None,
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
            temp_model = DeleteAppKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBizRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DeleteBizResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DeleteBizResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteBizResponseBody = None,
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
            temp_model = DeleteBizResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCcRouteRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        route_id_list: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.route_id_list = route_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.route_id_list is not None:
            result['RouteIdList'] = self.route_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('RouteIdList') is not None:
            self.route_id_list = m.get('RouteIdList')
        return self


class DeleteCcRouteRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DeleteCcRouteRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCcRouteRulesResponseBody = None,
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
            temp_model = DeleteCcRouteRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlexAccFwdRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        esn_biz_id: int = None,
        identity: str = None,
    ):
        self.source_ip = source_ip
        self.esn_biz_id = esn_biz_id
        self.identity = identity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.identity is not None:
            result['Identity'] = self.identity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        return self


class DeleteFlexAccFwdRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DeleteFlexAccFwdRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFlexAccFwdRuleResponseBody = None,
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
            temp_model = DeleteFlexAccFwdRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlexFwdRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_biz_id: int = None,
        identity: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_biz_id = esn_biz_id
        self.identity = identity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.identity is not None:
            result['Identity'] = self.identity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        return self


class DeleteFlexFwdRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DeleteFlexFwdRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFlexFwdRuleResponseBody = None,
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
            temp_model = DeleteFlexFwdRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DeleteGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGroupResponseBody = None,
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
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLayer4RuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        front_port: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.front_port = front_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.front_port is not None:
            result['FrontPort'] = self.front_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')
        return self


class DeleteLayer4RuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DeleteLayer4RuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLayer4RuleResponseBody = None,
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
            temp_model = DeleteLayer4RuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccResSummaryRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
    ):
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeAccResSummaryResponseBodyFullNodesSummaryNodes(TeaModel):
    def __init__(
        self,
        type: int = None,
        biz_id: str = None,
        ip: str = None,
        region_id: str = None,
        app_name: str = None,
        region_name: str = None,
        group_id: str = None,
        app_id: str = None,
        in_use: int = None,
        biz_name: str = None,
        ddos_status: int = None,
        is_disabled: bool = None,
        threshold: int = None,
        esn_biz_id: str = None,
    ):
        self.type = type
        self.biz_id = biz_id
        self.ip = ip
        self.region_id = region_id
        self.app_name = app_name
        self.region_name = region_name
        self.group_id = group_id
        self.app_id = app_id
        self.in_use = in_use
        self.biz_name = biz_name
        self.ddos_status = ddos_status
        self.is_disabled = is_disabled
        self.threshold = threshold
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.is_disabled is not None:
            result['IsDisabled'] = self.is_disabled
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('IsDisabled') is not None:
            self.is_disabled = m.get('IsDisabled')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class DescribeAccResSummaryResponseBodyFullNodesSummary(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeAccResSummaryResponseBodyFullNodesSummaryNodes] = None,
        clean_count: int = None,
        hole_count: int = None,
        used_count: int = None,
        un_used_count: int = None,
        total_count: int = None,
    ):
        self.nodes = nodes
        self.clean_count = clean_count
        self.hole_count = hole_count
        self.used_count = used_count
        self.un_used_count = un_used_count
        self.total_count = total_count

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.clean_count is not None:
            result['CleanCount'] = self.clean_count
        if self.hole_count is not None:
            result['HoleCount'] = self.hole_count
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        if self.un_used_count is not None:
            result['UnUsedCount'] = self.un_used_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeAccResSummaryResponseBodyFullNodesSummaryNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('CleanCount') is not None:
            self.clean_count = m.get('CleanCount')
        if m.get('HoleCount') is not None:
            self.hole_count = m.get('HoleCount')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        if m.get('UnUsedCount') is not None:
            self.un_used_count = m.get('UnUsedCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAccResSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        full_nodes_summary: DescribeAccResSummaryResponseBodyFullNodesSummary = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.full_nodes_summary = full_nodes_summary
        self.prompt_info = prompt_info

    def validate(self):
        if self.full_nodes_summary:
            self.full_nodes_summary.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.full_nodes_summary is not None:
            result['FullNodesSummary'] = self.full_nodes_summary.to_map()
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FullNodesSummary') is not None:
            temp_model = DescribeAccResSummaryResponseBodyFullNodesSummary()
            self.full_nodes_summary = temp_model.from_map(m['FullNodesSummary'])
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeAccResSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccResSummaryResponseBody = None,
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
            temp_model = DescribeAccResSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllLocalIpsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeAllLocalIpsResponseBodyLocalIps(TeaModel):
    def __init__(
        self,
        bgp: List[str] = None,
        gf: List[str] = None,
    ):
        self.bgp = bgp
        self.gf = gf

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bgp is not None:
            result['Bgp'] = self.bgp
        if self.gf is not None:
            result['Gf'] = self.gf
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bgp') is not None:
            self.bgp = m.get('Bgp')
        if m.get('Gf') is not None:
            self.gf = m.get('Gf')
        return self


class DescribeAllLocalIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        local_ips: DescribeAllLocalIpsResponseBodyLocalIps = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.local_ips = local_ips
        self.prompt_info = prompt_info

    def validate(self):
        if self.local_ips:
            self.local_ips.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.local_ips is not None:
            result['LocalIps'] = self.local_ips.to_map()
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LocalIps') is not None:
            temp_model = DescribeAllLocalIpsResponseBodyLocalIps()
            self.local_ips = temp_model.from_map(m['LocalIps'])
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeAllLocalIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAllLocalIpsResponseBody = None,
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
            temp_model = DescribeAllLocalIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppDailyDetailsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_app_id: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_app_id = esn_app_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_app_id is not None:
            result['EsnAppId'] = self.esn_app_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnAppId') is not None:
            self.esn_app_id = m.get('EsnAppId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeAppDailyDetailsResponseBodyAppDailyDetails(TeaModel):
    def __init__(
        self,
        ios_active_count: int = None,
        index: int = None,
        android_count: int = None,
        ios_count: int = None,
        new_count: int = None,
        ip_active_count: int = None,
        active_count: int = None,
        count: int = None,
        android_active_count: int = None,
    ):
        self.ios_active_count = ios_active_count
        self.index = index
        self.android_count = android_count
        self.ios_count = ios_count
        self.new_count = new_count
        self.ip_active_count = ip_active_count
        self.active_count = active_count
        self.count = count
        self.android_active_count = android_active_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ios_active_count is not None:
            result['IosActiveCount'] = self.ios_active_count
        if self.index is not None:
            result['Index'] = self.index
        if self.android_count is not None:
            result['AndroidCount'] = self.android_count
        if self.ios_count is not None:
            result['IosCount'] = self.ios_count
        if self.new_count is not None:
            result['NewCount'] = self.new_count
        if self.ip_active_count is not None:
            result['IpActiveCount'] = self.ip_active_count
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count
        if self.count is not None:
            result['Count'] = self.count
        if self.android_active_count is not None:
            result['AndroidActiveCount'] = self.android_active_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IosActiveCount') is not None:
            self.ios_active_count = m.get('IosActiveCount')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('AndroidCount') is not None:
            self.android_count = m.get('AndroidCount')
        if m.get('IosCount') is not None:
            self.ios_count = m.get('IosCount')
        if m.get('NewCount') is not None:
            self.new_count = m.get('NewCount')
        if m.get('IpActiveCount') is not None:
            self.ip_active_count = m.get('IpActiveCount')
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('AndroidActiveCount') is not None:
            self.android_active_count = m.get('AndroidActiveCount')
        return self


class DescribeAppDailyDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_daily_details: List[DescribeAppDailyDetailsResponseBodyAppDailyDetails] = None,
    ):
        self.request_id = request_id
        self.app_daily_details = app_daily_details

    def validate(self):
        if self.app_daily_details:
            for k in self.app_daily_details:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AppDailyDetails'] = []
        if self.app_daily_details is not None:
            for k in self.app_daily_details:
                result['AppDailyDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.app_daily_details = []
        if m.get('AppDailyDetails') is not None:
            for k in m.get('AppDailyDetails'):
                temp_model = DescribeAppDailyDetailsResponseBodyAppDailyDetails()
                self.app_daily_details.append(temp_model.from_map(k))
        return self


class DescribeAppDailyDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppDailyDetailsResponseBody = None,
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
            temp_model = DescribeAppDailyDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppDailySdkVersionsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_app_id: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_app_id = esn_app_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_app_id is not None:
            result['EsnAppId'] = self.esn_app_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnAppId') is not None:
            self.esn_app_id = m.get('EsnAppId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeAppDailySdkVersionsResponseBodyAppDailySdkVersions(TeaModel):
    def __init__(
        self,
        index: int = None,
        version: str = None,
        count: int = None,
    ):
        self.index = index
        self.version = version
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.version is not None:
            result['Version'] = self.version
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeAppDailySdkVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_daily_sdk_versions: List[DescribeAppDailySdkVersionsResponseBodyAppDailySdkVersions] = None,
    ):
        self.request_id = request_id
        self.app_daily_sdk_versions = app_daily_sdk_versions

    def validate(self):
        if self.app_daily_sdk_versions:
            for k in self.app_daily_sdk_versions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AppDailySdkVersions'] = []
        if self.app_daily_sdk_versions is not None:
            for k in self.app_daily_sdk_versions:
                result['AppDailySdkVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.app_daily_sdk_versions = []
        if m.get('AppDailySdkVersions') is not None:
            for k in m.get('AppDailySdkVersions'):
                temp_model = DescribeAppDailySdkVersionsResponseBodyAppDailySdkVersions()
                self.app_daily_sdk_versions.append(temp_model.from_map(k))
        return self


class DescribeAppDailySdkVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppDailySdkVersionsResponseBody = None,
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
            temp_model = DescribeAppDailySdkVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
        app_name: str = None,
        app_id_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id
        self.app_name = app_name
        self.app_id_list = app_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')
        return self


class DescribeAppListResponseBodyAppList(TeaModel):
    def __init__(
        self,
        old_app_key: str = None,
        app_name: str = None,
        app_key: str = None,
        app_id: int = None,
        has_old_app_key: bool = None,
        sdk_version: str = None,
        biz_num: int = None,
        group_num: int = None,
        node_num: int = None,
    ):
        self.old_app_key = old_app_key
        self.app_name = app_name
        self.app_key = app_key
        self.app_id = app_id
        self.has_old_app_key = has_old_app_key
        self.sdk_version = sdk_version
        self.biz_num = biz_num
        self.group_num = group_num
        self.node_num = node_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.old_app_key is not None:
            result['OldAppKey'] = self.old_app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.has_old_app_key is not None:
            result['HasOldAppKey'] = self.has_old_app_key
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.biz_num is not None:
            result['BizNum'] = self.biz_num
        if self.group_num is not None:
            result['GroupNum'] = self.group_num
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OldAppKey') is not None:
            self.old_app_key = m.get('OldAppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('HasOldAppKey') is not None:
            self.has_old_app_key = m.get('HasOldAppKey')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('BizNum') is not None:
            self.biz_num = m.get('BizNum')
        if m.get('GroupNum') is not None:
            self.group_num = m.get('GroupNum')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        return self


class DescribeAppListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
        app_list: List[DescribeAppListResponseBodyAppList] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info
        self.app_list = app_list

    def validate(self):
        if self.app_list:
            for k in self.app_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        result['AppList'] = []
        if self.app_list is not None:
            for k in self.app_list:
                result['AppList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        self.app_list = []
        if m.get('AppList') is not None:
            for k in m.get('AppList'):
                temp_model = DescribeAppListResponseBodyAppList()
                self.app_list.append(temp_model.from_map(k))
        return self


class DescribeAppListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppListResponseBody = None,
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
            temp_model = DescribeAppListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppSimpleListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id_list = app_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')
        return self


class DescribeAppSimpleListResponseBodyAppSimpleList(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        ng_app_id: str = None,
        app_id: int = None,
        esn_app_id: str = None,
    ):
        self.app_name = app_name
        self.ng_app_id = ng_app_id
        self.app_id = app_id
        self.esn_app_id = esn_app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.ng_app_id is not None:
            result['NgAppId'] = self.ng_app_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.esn_app_id is not None:
            result['EsnAppId'] = self.esn_app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('NgAppId') is not None:
            self.ng_app_id = m.get('NgAppId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EsnAppId') is not None:
            self.esn_app_id = m.get('EsnAppId')
        return self


class DescribeAppSimpleListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_simple_list: List[DescribeAppSimpleListResponseBodyAppSimpleList] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.app_simple_list = app_simple_list
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.app_simple_list:
            for k in self.app_simple_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AppSimpleList'] = []
        if self.app_simple_list is not None:
            for k in self.app_simple_list:
                result['AppSimpleList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.app_simple_list = []
        if m.get('AppSimpleList') is not None:
            for k in m.get('AppSimpleList'):
                temp_model = DescribeAppSimpleListResponseBodyAppSimpleList()
                self.app_simple_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeAppSimpleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppSimpleListResponseBody = None,
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
            temp_model = DescribeAppSimpleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAsyncOperationRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeAsyncOperationResponseBodyAsyncOperation(TeaModel):
    def __init__(
        self,
        status: str = None,
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


class DescribeAsyncOperationResponseBody(TeaModel):
    def __init__(
        self,
        async_operation: DescribeAsyncOperationResponseBodyAsyncOperation = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.async_operation = async_operation
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.async_operation:
            self.async_operation.validate()

    def to_map(self):
        result = dict()
        if self.async_operation is not None:
            result['AsyncOperation'] = self.async_operation.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncOperation') is not None:
            temp_model = DescribeAsyncOperationResponseBodyAsyncOperation()
            self.async_operation = temp_model.from_map(m['AsyncOperation'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeAsyncOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAsyncOperationResponseBody = None,
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
            temp_model = DescribeAsyncOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutomaticTraceabilitySlsLogRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: int = None,
        end_time: int = None,
        page: int = None,
        page_size: int = None,
        esn_app_id: str = None,
        source: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.esn_app_id = esn_app_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.esn_app_id is not None:
            result['EsnAppId'] = self.esn_app_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EsnAppId') is not None:
            self.esn_app_id = m.get('EsnAppId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeAutomaticTraceabilitySlsLogResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        time: str = None,
        token: str = None,
        point: str = None,
        ip: str = None,
        source_ip_location: str = None,
    ):
        self.source_ip = source_ip
        self.time = time
        self.token = token
        self.point = point
        self.ip = ip
        self.source_ip_location = source_ip_location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.time is not None:
            result['Time'] = self.time
        if self.token is not None:
            result['Token'] = self.token
        if self.point is not None:
            result['Point'] = self.point
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.source_ip_location is not None:
            result['SourceIpLocation'] = self.source_ip_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Point') is not None:
            self.point = m.get('Point')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('SourceIpLocation') is not None:
            self.source_ip_location = m.get('SourceIpLocation')
        return self


class DescribeAutomaticTraceabilitySlsLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[DescribeAutomaticTraceabilitySlsLogResponseBodyStatistic] = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.total = total

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeAutomaticTraceabilitySlsLogResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAutomaticTraceabilitySlsLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAutomaticTraceabilitySlsLogResponseBody = None,
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
            temp_model = DescribeAutomaticTraceabilitySlsLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBgpResSummaryRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeBgpResSummaryResponseBodyFullNodesSummaryNodes(TeaModel):
    def __init__(
        self,
        type: int = None,
        biz_id: str = None,
        ip: str = None,
        region_id: str = None,
        app_name: str = None,
        region_name: str = None,
        group_id: str = None,
        app_id: str = None,
        in_use: int = None,
        biz_name: str = None,
        ddos_status: int = None,
        is_disabled: bool = None,
        threshold: int = None,
        esn_biz_id: str = None,
    ):
        self.type = type
        self.biz_id = biz_id
        self.ip = ip
        self.region_id = region_id
        self.app_name = app_name
        self.region_name = region_name
        self.group_id = group_id
        self.app_id = app_id
        self.in_use = in_use
        self.biz_name = biz_name
        self.ddos_status = ddos_status
        self.is_disabled = is_disabled
        self.threshold = threshold
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.is_disabled is not None:
            result['IsDisabled'] = self.is_disabled
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('IsDisabled') is not None:
            self.is_disabled = m.get('IsDisabled')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class DescribeBgpResSummaryResponseBodyFullNodesSummary(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeBgpResSummaryResponseBodyFullNodesSummaryNodes] = None,
        clean_count: int = None,
        hole_count: int = None,
        used_count: int = None,
        un_used_count: int = None,
        total_count: int = None,
    ):
        self.nodes = nodes
        self.clean_count = clean_count
        self.hole_count = hole_count
        self.used_count = used_count
        self.un_used_count = un_used_count
        self.total_count = total_count

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.clean_count is not None:
            result['CleanCount'] = self.clean_count
        if self.hole_count is not None:
            result['HoleCount'] = self.hole_count
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        if self.un_used_count is not None:
            result['UnUsedCount'] = self.un_used_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeBgpResSummaryResponseBodyFullNodesSummaryNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('CleanCount') is not None:
            self.clean_count = m.get('CleanCount')
        if m.get('HoleCount') is not None:
            self.hole_count = m.get('HoleCount')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        if m.get('UnUsedCount') is not None:
            self.un_used_count = m.get('UnUsedCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBgpResSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        full_nodes_summary: DescribeBgpResSummaryResponseBodyFullNodesSummary = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.full_nodes_summary = full_nodes_summary
        self.prompt_info = prompt_info

    def validate(self):
        if self.full_nodes_summary:
            self.full_nodes_summary.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.full_nodes_summary is not None:
            result['FullNodesSummary'] = self.full_nodes_summary.to_map()
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FullNodesSummary') is not None:
            temp_model = DescribeBgpResSummaryResponseBodyFullNodesSummary()
            self.full_nodes_summary = temp_model.from_map(m['FullNodesSummary'])
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeBgpResSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBgpResSummaryResponseBody = None,
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
            temp_model = DescribeBgpResSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBizListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
        biz_id: int = None,
        biz_name: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id
        self.biz_id = biz_id
        self.biz_name = biz_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        return self


class DescribeBizListResponseBodyBizList(TeaModel):
    def __init__(
        self,
        type: int = None,
        node_in_use_num: int = None,
        ng_group_id: str = None,
        use_cc: int = None,
        biz_id: int = None,
        group_num: int = None,
        node_un_use_num: int = None,
        app_id: int = None,
        biz_name: str = None,
        node_num: int = None,
        esn_biz_id: str = None,
        cc_qps: int = None,
    ):
        self.type = type
        self.node_in_use_num = node_in_use_num
        self.ng_group_id = ng_group_id
        self.use_cc = use_cc
        self.biz_id = biz_id
        self.group_num = group_num
        self.node_un_use_num = node_un_use_num
        self.app_id = app_id
        self.biz_name = biz_name
        self.node_num = node_num
        self.esn_biz_id = esn_biz_id
        self.cc_qps = cc_qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.node_in_use_num is not None:
            result['NodeInUseNum'] = self.node_in_use_num
        if self.ng_group_id is not None:
            result['NgGroupId'] = self.ng_group_id
        if self.use_cc is not None:
            result['UseCc'] = self.use_cc
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.group_num is not None:
            result['GroupNum'] = self.group_num
        if self.node_un_use_num is not None:
            result['NodeUnUseNum'] = self.node_un_use_num
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.cc_qps is not None:
            result['CcQps'] = self.cc_qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NodeInUseNum') is not None:
            self.node_in_use_num = m.get('NodeInUseNum')
        if m.get('NgGroupId') is not None:
            self.ng_group_id = m.get('NgGroupId')
        if m.get('UseCc') is not None:
            self.use_cc = m.get('UseCc')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GroupNum') is not None:
            self.group_num = m.get('GroupNum')
        if m.get('NodeUnUseNum') is not None:
            self.node_un_use_num = m.get('NodeUnUseNum')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('CcQps') is not None:
            self.cc_qps = m.get('CcQps')
        return self


class DescribeBizListResponseBody(TeaModel):
    def __init__(
        self,
        biz_list: List[DescribeBizListResponseBodyBizList] = None,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.biz_list = biz_list
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.biz_list:
            for k in self.biz_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BizList'] = []
        if self.biz_list is not None:
            for k in self.biz_list:
                result['BizList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_list = []
        if m.get('BizList') is not None:
            for k in m.get('BizList'):
                temp_model = DescribeBizListResponseBodyBizList()
                self.biz_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeBizListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBizListResponseBody = None,
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
            temp_model = DescribeBizListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBizSimpleListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
        app_id_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id
        self.app_id_list = app_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')
        return self


class DescribeBizSimpleListResponseBodyBizSimpleList(TeaModel):
    def __init__(
        self,
        type: int = None,
        ng_group_id: str = None,
        app_id: int = None,
        use_cc: int = None,
        biz_id: int = None,
        biz_name: str = None,
        esn_biz_id: str = None,
        cc_qps: int = None,
    ):
        self.type = type
        self.ng_group_id = ng_group_id
        self.app_id = app_id
        self.use_cc = use_cc
        self.biz_id = biz_id
        self.biz_name = biz_name
        self.esn_biz_id = esn_biz_id
        self.cc_qps = cc_qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.ng_group_id is not None:
            result['NgGroupId'] = self.ng_group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.use_cc is not None:
            result['UseCc'] = self.use_cc
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.cc_qps is not None:
            result['CcQps'] = self.cc_qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NgGroupId') is not None:
            self.ng_group_id = m.get('NgGroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UseCc') is not None:
            self.use_cc = m.get('UseCc')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('CcQps') is not None:
            self.cc_qps = m.get('CcQps')
        return self


class DescribeBizSimpleListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
        biz_simple_list: List[DescribeBizSimpleListResponseBodyBizSimpleList] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info
        self.biz_simple_list = biz_simple_list

    def validate(self):
        if self.biz_simple_list:
            for k in self.biz_simple_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        result['BizSimpleList'] = []
        if self.biz_simple_list is not None:
            for k in self.biz_simple_list:
                result['BizSimpleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        self.biz_simple_list = []
        if m.get('BizSimpleList') is not None:
            for k in m.get('BizSimpleList'):
                temp_model = DescribeBizSimpleListResponseBodyBizSimpleList()
                self.biz_simple_list.append(temp_model.from_map(k))
        return self


class DescribeBizSimpleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBizSimpleListResponseBody = None,
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
            temp_model = DescribeBizSimpleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBpsFlowRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        group_id: str = None,
        begin_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.group_id = group_id
        self.begin_time = begin_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeBpsFlowResponseBodyFlowDataItems(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
        name: str = None,
    ):
        self.values = values
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBpsFlowResponseBodyFlowDataTimeScope(TeaModel):
    def __init__(
        self,
        start: int = None,
        interval: int = None,
    ):
        self.start = start
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeBpsFlowResponseBodyFlowData(TeaModel):
    def __init__(
        self,
        items: List[DescribeBpsFlowResponseBodyFlowDataItems] = None,
        categories: List[str] = None,
        time_scope: DescribeBpsFlowResponseBodyFlowDataTimeScope = None,
        categories_type: str = None,
    ):
        self.items = items
        self.categories = categories
        self.time_scope = time_scope
        self.categories_type = categories_type

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        if self.time_scope:
            self.time_scope.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.time_scope is not None:
            result['TimeScope'] = self.time_scope.to_map()
        if self.categories_type is not None:
            result['CategoriesType'] = self.categories_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeBpsFlowResponseBodyFlowDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('TimeScope') is not None:
            temp_model = DescribeBpsFlowResponseBodyFlowDataTimeScope()
            self.time_scope = temp_model.from_map(m['TimeScope'])
        if m.get('CategoriesType') is not None:
            self.categories_type = m.get('CategoriesType')
        return self


class DescribeBpsFlowResponseBody(TeaModel):
    def __init__(
        self,
        flow_data: DescribeBpsFlowResponseBodyFlowData = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.flow_data = flow_data
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.flow_data:
            self.flow_data.validate()

    def to_map(self):
        result = dict()
        if self.flow_data is not None:
            result['FlowData'] = self.flow_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowData') is not None:
            temp_model = DescribeBpsFlowResponseBodyFlowData()
            self.flow_data = temp_model.from_map(m['FlowData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeBpsFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBpsFlowResponseBody = None,
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
            temp_model = DescribeBpsFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcBlackListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeCcBlackListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
        black_list: List[str] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info
        self.black_list = black_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        return self


class DescribeCcBlackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcBlackListResponseBody = None,
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
            temp_model = DescribeCcBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcDevieIpListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeCcDevieIpListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ip_list: List[str] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.ip_list = ip_list
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeCcDevieIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcDevieIpListResponseBody = None,
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
            temp_model = DescribeCcDevieIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcFlowRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        begin_time: int = None,
        end_time: int = None,
        interval: int = None,
        api_version: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.begin_time = begin_time
        self.end_time = end_time
        self.interval = interval
        self.api_version = api_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        return self


class DescribeCcFlowResponseBodyFlowDataItems(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
        name: str = None,
    ):
        self.values = values
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeCcFlowResponseBodyFlowDataTimeScope(TeaModel):
    def __init__(
        self,
        start: int = None,
        interval: int = None,
    ):
        self.start = start
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeCcFlowResponseBodyFlowData(TeaModel):
    def __init__(
        self,
        items: List[DescribeCcFlowResponseBodyFlowDataItems] = None,
        categories: List[str] = None,
        time_scope: DescribeCcFlowResponseBodyFlowDataTimeScope = None,
        categories_type: str = None,
    ):
        self.items = items
        self.categories = categories
        self.time_scope = time_scope
        self.categories_type = categories_type

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        if self.time_scope:
            self.time_scope.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.time_scope is not None:
            result['TimeScope'] = self.time_scope.to_map()
        if self.categories_type is not None:
            result['CategoriesType'] = self.categories_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeCcFlowResponseBodyFlowDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('TimeScope') is not None:
            temp_model = DescribeCcFlowResponseBodyFlowDataTimeScope()
            self.time_scope = temp_model.from_map(m['TimeScope'])
        if m.get('CategoriesType') is not None:
            self.categories_type = m.get('CategoriesType')
        return self


class DescribeCcFlowResponseBody(TeaModel):
    def __init__(
        self,
        flow_data: DescribeCcFlowResponseBodyFlowData = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.flow_data = flow_data
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.flow_data:
            self.flow_data.validate()

    def to_map(self):
        result = dict()
        if self.flow_data is not None:
            result['FlowData'] = self.flow_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowData') is not None:
            temp_model = DescribeCcFlowResponseBodyFlowData()
            self.flow_data = temp_model.from_map(m['FlowData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeCcFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcFlowResponseBody = None,
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
            temp_model = DescribeCcFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcIDCBlockSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeCcIDCBlockSwitchResponseBodyCcSwitch(TeaModel):
    def __init__(
        self,
        enable: int = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeCcIDCBlockSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        cc_switch: DescribeCcIDCBlockSwitchResponseBodyCcSwitch = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.cc_switch = cc_switch

    def validate(self):
        if self.cc_switch:
            self.cc_switch.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.cc_switch is not None:
            result['CcSwitch'] = self.cc_switch.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('CcSwitch') is not None:
            temp_model = DescribeCcIDCBlockSwitchResponseBodyCcSwitch()
            self.cc_switch = temp_model.from_map(m['CcSwitch'])
        return self


class DescribeCcIDCBlockSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcIDCBlockSwitchResponseBody = None,
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
            temp_model = DescribeCcIDCBlockSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcMaxFwRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        begin_time: int = None,
        end_time: int = None,
        source: str = None,
        dest_port: int = None,
        page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.begin_time = begin_time
        self.end_time = end_time
        self.source = source
        self.dest_port = dest_port
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source is not None:
            result['Source'] = self.source
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCcMaxFwResponseBodyFwMaxInfoList(TeaModel):
    def __init__(
        self,
        in_white_list: bool = None,
        time: int = None,
        source_ip: str = None,
        dest_port: int = None,
        action: int = None,
        protocol: int = None,
        in_black_list: bool = None,
        count: int = None,
    ):
        self.in_white_list = in_white_list
        self.time = time
        self.source_ip = source_ip
        self.dest_port = dest_port
        self.action = action
        self.protocol = protocol
        self.in_black_list = in_black_list
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.in_white_list is not None:
            result['InWhiteList'] = self.in_white_list
        if self.time is not None:
            result['Time'] = self.time
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.action is not None:
            result['Action'] = self.action
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.in_black_list is not None:
            result['InBlackList'] = self.in_black_list
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InWhiteList') is not None:
            self.in_white_list = m.get('InWhiteList')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('InBlackList') is not None:
            self.in_black_list = m.get('InBlackList')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeCcMaxFwResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        fw_max_info_list: List[DescribeCcMaxFwResponseBodyFwMaxInfoList] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.fw_max_info_list = fw_max_info_list
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.fw_max_info_list:
            for k in self.fw_max_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FwMaxInfoList'] = []
        if self.fw_max_info_list is not None:
            for k in self.fw_max_info_list:
                result['FwMaxInfoList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.fw_max_info_list = []
        if m.get('FwMaxInfoList') is not None:
            for k in m.get('FwMaxInfoList'):
                temp_model = DescribeCcMaxFwResponseBodyFwMaxInfoList()
                self.fw_max_info_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeCcMaxFwResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcMaxFwResponseBody = None,
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
            temp_model = DescribeCcMaxFwResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcResSummaryRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeCcResSummaryResponseBodyFullNodesSummaryNGResInfoList(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_id: str = None,
        used_qps: int = None,
        biz_name: str = None,
        biz_id: str = None,
    ):
        self.app_name = app_name
        self.app_id = app_id
        self.used_qps = used_qps
        self.biz_name = biz_name
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.used_qps is not None:
            result['UsedQps'] = self.used_qps
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UsedQps') is not None:
            self.used_qps = m.get('UsedQps')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeCcResSummaryResponseBodyFullNodesSummary(TeaModel):
    def __init__(
        self,
        un_used_qps: int = None,
        used_qps: int = None,
        total_qps: int = None,
        ngres_info_list: List[DescribeCcResSummaryResponseBodyFullNodesSummaryNGResInfoList] = None,
    ):
        self.un_used_qps = un_used_qps
        self.used_qps = used_qps
        self.total_qps = total_qps
        self.ngres_info_list = ngres_info_list

    def validate(self):
        if self.ngres_info_list:
            for k in self.ngres_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.un_used_qps is not None:
            result['UnUsedQps'] = self.un_used_qps
        if self.used_qps is not None:
            result['UsedQps'] = self.used_qps
        if self.total_qps is not None:
            result['TotalQps'] = self.total_qps
        result['NGResInfoList'] = []
        if self.ngres_info_list is not None:
            for k in self.ngres_info_list:
                result['NGResInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UnUsedQps') is not None:
            self.un_used_qps = m.get('UnUsedQps')
        if m.get('UsedQps') is not None:
            self.used_qps = m.get('UsedQps')
        if m.get('TotalQps') is not None:
            self.total_qps = m.get('TotalQps')
        self.ngres_info_list = []
        if m.get('NGResInfoList') is not None:
            for k in m.get('NGResInfoList'):
                temp_model = DescribeCcResSummaryResponseBodyFullNodesSummaryNGResInfoList()
                self.ngres_info_list.append(temp_model.from_map(k))
        return self


class DescribeCcResSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        full_nodes_summary: DescribeCcResSummaryResponseBodyFullNodesSummary = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.full_nodes_summary = full_nodes_summary
        self.prompt_info = prompt_info

    def validate(self):
        if self.full_nodes_summary:
            self.full_nodes_summary.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.full_nodes_summary is not None:
            result['FullNodesSummary'] = self.full_nodes_summary.to_map()
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FullNodesSummary') is not None:
            temp_model = DescribeCcResSummaryResponseBodyFullNodesSummary()
            self.full_nodes_summary = temp_model.from_map(m['FullNodesSummary'])
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeCcResSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcResSummaryResponseBody = None,
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
            temp_model = DescribeCcResSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcRouteRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        route_comment: str = None,
        route_id: str = None,
        route_ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.route_comment = route_comment
        self.route_id = route_id
        self.route_ip = route_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.route_comment is not None:
            result['RouteComment'] = self.route_comment
        if self.route_id is not None:
            result['RouteId'] = self.route_id
        if self.route_ip is not None:
            result['RouteIp'] = self.route_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('RouteComment') is not None:
            self.route_comment = m.get('RouteComment')
        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')
        if m.get('RouteIp') is not None:
            self.route_ip = m.get('RouteIp')
        return self


class DescribeCcRouteRulesResponseBodyRuleQueryResultRouteRules(TeaModel):
    def __init__(
        self,
        comment: str = None,
        rservers: List[str] = None,
        id: str = None,
    ):
        self.comment = comment
        self.rservers = rservers
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.rservers is not None:
            result['Rservers'] = self.rservers
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Rservers') is not None:
            self.rservers = m.get('Rservers')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeCcRouteRulesResponseBodyRuleQueryResult(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        route_rules: List[DescribeCcRouteRulesResponseBodyRuleQueryResultRouteRules] = None,
        biz_id: str = None,
    ):
        self.app_id = app_id
        self.route_rules = route_rules
        self.biz_id = biz_id

    def validate(self):
        if self.route_rules:
            for k in self.route_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        result['RouteRules'] = []
        if self.route_rules is not None:
            for k in self.route_rules:
                result['RouteRules'].append(k.to_map() if k else None)
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        self.route_rules = []
        if m.get('RouteRules') is not None:
            for k in m.get('RouteRules'):
                temp_model = DescribeCcRouteRulesResponseBodyRuleQueryResultRouteRules()
                self.route_rules.append(temp_model.from_map(k))
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeCcRouteRulesResponseBody(TeaModel):
    def __init__(
        self,
        rule_query_result: DescribeCcRouteRulesResponseBodyRuleQueryResult = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.rule_query_result = rule_query_result
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.rule_query_result:
            self.rule_query_result.validate()

    def to_map(self):
        result = dict()
        if self.rule_query_result is not None:
            result['RuleQueryResult'] = self.rule_query_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleQueryResult') is not None:
            temp_model = DescribeCcRouteRulesResponseBodyRuleQueryResult()
            self.rule_query_result = temp_model.from_map(m['RuleQueryResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeCcRouteRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcRouteRulesResponseBody = None,
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
            temp_model = DescribeCcRouteRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcRouteSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeCcRouteSwitchResponseBodySwitch(TeaModel):
    def __init__(
        self,
        enable: int = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeCcRouteSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        switch: DescribeCcRouteSwitchResponseBodySwitch = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.switch = switch
        self.prompt_info = prompt_info

    def validate(self):
        if self.switch:
            self.switch.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.switch is not None:
            result['Switch'] = self.switch.to_map()
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Switch') is not None:
            temp_model = DescribeCcRouteSwitchResponseBodySwitch()
            self.switch = temp_model.from_map(m['Switch'])
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeCcRouteSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcRouteSwitchResponseBody = None,
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
            temp_model = DescribeCcRouteSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcSocketDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        begin_time: int = None,
        end_time: int = None,
        interval: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.begin_time = begin_time
        self.end_time = end_time
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeCcSocketDetailResponseBodyFlowDataItems(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
        name: str = None,
    ):
        self.values = values
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeCcSocketDetailResponseBodyFlowDataTimeScope(TeaModel):
    def __init__(
        self,
        start: int = None,
        interval: int = None,
    ):
        self.start = start
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeCcSocketDetailResponseBodyFlowData(TeaModel):
    def __init__(
        self,
        items: List[DescribeCcSocketDetailResponseBodyFlowDataItems] = None,
        categories: List[str] = None,
        time_scope: DescribeCcSocketDetailResponseBodyFlowDataTimeScope = None,
        categories_type: str = None,
    ):
        self.items = items
        self.categories = categories
        self.time_scope = time_scope
        self.categories_type = categories_type

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        if self.time_scope:
            self.time_scope.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.time_scope is not None:
            result['TimeScope'] = self.time_scope.to_map()
        if self.categories_type is not None:
            result['CategoriesType'] = self.categories_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeCcSocketDetailResponseBodyFlowDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('TimeScope') is not None:
            temp_model = DescribeCcSocketDetailResponseBodyFlowDataTimeScope()
            self.time_scope = temp_model.from_map(m['TimeScope'])
        if m.get('CategoriesType') is not None:
            self.categories_type = m.get('CategoriesType')
        return self


class DescribeCcSocketDetailResponseBody(TeaModel):
    def __init__(
        self,
        flow_data: DescribeCcSocketDetailResponseBodyFlowData = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.flow_data = flow_data
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.flow_data:
            self.flow_data.validate()

    def to_map(self):
        result = dict()
        if self.flow_data is not None:
            result['FlowData'] = self.flow_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowData') is not None:
            temp_model = DescribeCcSocketDetailResponseBodyFlowData()
            self.flow_data = temp_model.from_map(m['FlowData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeCcSocketDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcSocketDetailResponseBody = None,
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
            temp_model = DescribeCcSocketDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcTotalFwRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        begin_time: int = None,
        end_time: int = None,
        source: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.begin_time = begin_time
        self.end_time = end_time
        self.source = source
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source is not None:
            result['Source'] = self.source
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCcTotalFwResponseBodyFwTotalInfoList(TeaModel):
    def __init__(
        self,
        in_white_list: bool = None,
        time: int = None,
        source_ip: str = None,
        attack_type: str = None,
        in_black_list: bool = None,
        count: int = None,
        source_location: str = None,
    ):
        self.in_white_list = in_white_list
        self.time = time
        self.source_ip = source_ip
        self.attack_type = attack_type
        self.in_black_list = in_black_list
        self.count = count
        self.source_location = source_location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.in_white_list is not None:
            result['InWhiteList'] = self.in_white_list
        if self.time is not None:
            result['Time'] = self.time
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.in_black_list is not None:
            result['InBlackList'] = self.in_black_list
        if self.count is not None:
            result['Count'] = self.count
        if self.source_location is not None:
            result['SourceLocation'] = self.source_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InWhiteList') is not None:
            self.in_white_list = m.get('InWhiteList')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('InBlackList') is not None:
            self.in_black_list = m.get('InBlackList')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('SourceLocation') is not None:
            self.source_location = m.get('SourceLocation')
        return self


class DescribeCcTotalFwResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
        fw_total_info_list: List[DescribeCcTotalFwResponseBodyFwTotalInfoList] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info
        self.fw_total_info_list = fw_total_info_list

    def validate(self):
        if self.fw_total_info_list:
            for k in self.fw_total_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        result['FwTotalInfoList'] = []
        if self.fw_total_info_list is not None:
            for k in self.fw_total_info_list:
                result['FwTotalInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        self.fw_total_info_list = []
        if m.get('FwTotalInfoList') is not None:
            for k in m.get('FwTotalInfoList'):
                temp_model = DescribeCcTotalFwResponseBodyFwTotalInfoList()
                self.fw_total_info_list.append(temp_model.from_map(k))
        return self


class DescribeCcTotalFwResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcTotalFwResponseBody = None,
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
            temp_model = DescribeCcTotalFwResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcTunnelRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeCcTunnelResponseBodyCcTunnel(TeaModel):
    def __init__(
        self,
        status: str = None,
        only_allow: bool = None,
        gray: int = None,
    ):
        self.status = status
        self.only_allow = only_allow
        self.gray = gray

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.only_allow is not None:
            result['OnlyAllow'] = self.only_allow
        if self.gray is not None:
            result['Gray'] = self.gray
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OnlyAllow') is not None:
            self.only_allow = m.get('OnlyAllow')
        if m.get('Gray') is not None:
            self.gray = m.get('Gray')
        return self


class DescribeCcTunnelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        cc_tunnel: DescribeCcTunnelResponseBodyCcTunnel = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.cc_tunnel = cc_tunnel

    def validate(self):
        if self.cc_tunnel:
            self.cc_tunnel.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.cc_tunnel is not None:
            result['CcTunnel'] = self.cc_tunnel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('CcTunnel') is not None:
            temp_model = DescribeCcTunnelResponseBodyCcTunnel()
            self.cc_tunnel = temp_model.from_map(m['CcTunnel'])
        return self


class DescribeCcTunnelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcTunnelResponseBody = None,
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
            temp_model = DescribeCcTunnelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcWhiteListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeCcWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
        white_list: List[str] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class DescribeCcWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcWhiteListResponseBody = None,
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
            temp_model = DescribeCcWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcZoneBlockConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeCcZoneBlockConfigResponseBodyBlockConfigCcZones(TeaModel):
    def __init__(
        self,
        provinces: List[str] = None,
        country: str = None,
    ):
        self.provinces = provinces
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.provinces is not None:
            result['Provinces'] = self.provinces
        if self.country is not None:
            result['Country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Provinces') is not None:
            self.provinces = m.get('Provinces')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        return self


class DescribeCcZoneBlockConfigResponseBodyBlockConfig(TeaModel):
    def __init__(
        self,
        cc_zones: List[DescribeCcZoneBlockConfigResponseBodyBlockConfigCcZones] = None,
        enable: int = None,
    ):
        self.cc_zones = cc_zones
        self.enable = enable

    def validate(self):
        if self.cc_zones:
            for k in self.cc_zones:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CcZones'] = []
        if self.cc_zones is not None:
            for k in self.cc_zones:
                result['CcZones'].append(k.to_map() if k else None)
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cc_zones = []
        if m.get('CcZones') is not None:
            for k in m.get('CcZones'):
                temp_model = DescribeCcZoneBlockConfigResponseBodyBlockConfigCcZones()
                self.cc_zones.append(temp_model.from_map(k))
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeCcZoneBlockConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        block_config: DescribeCcZoneBlockConfigResponseBodyBlockConfig = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.block_config = block_config

    def validate(self):
        if self.block_config:
            self.block_config.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.block_config is not None:
            result['BlockConfig'] = self.block_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('BlockConfig') is not None:
            temp_model = DescribeCcZoneBlockConfigResponseBodyBlockConfig()
            self.block_config = temp_model.from_map(m['BlockConfig'])
        return self


class DescribeCcZoneBlockConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcZoneBlockConfigResponseBody = None,
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
            temp_model = DescribeCcZoneBlockConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcZonesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeCcZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        zone_list: List[str] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.zone_list = zone_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.zone_list is not None:
            result['ZoneList'] = self.zone_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('ZoneList') is not None:
            self.zone_list = m.get('ZoneList')
        return self


class DescribeCcZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcZonesResponseBody = None,
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
            temp_model = DescribeCcZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDailyDetailsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDailyDetailsResponseBodyDailyDetails(TeaModel):
    def __init__(
        self,
        ios_active_count: int = None,
        index: int = None,
        android_count: int = None,
        ios_count: int = None,
        new_count: int = None,
        ip_active_count: int = None,
        active_count: int = None,
        count: int = None,
        android_active_count: int = None,
    ):
        self.ios_active_count = ios_active_count
        self.index = index
        self.android_count = android_count
        self.ios_count = ios_count
        self.new_count = new_count
        self.ip_active_count = ip_active_count
        self.active_count = active_count
        self.count = count
        self.android_active_count = android_active_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ios_active_count is not None:
            result['IosActiveCount'] = self.ios_active_count
        if self.index is not None:
            result['Index'] = self.index
        if self.android_count is not None:
            result['AndroidCount'] = self.android_count
        if self.ios_count is not None:
            result['IosCount'] = self.ios_count
        if self.new_count is not None:
            result['NewCount'] = self.new_count
        if self.ip_active_count is not None:
            result['IpActiveCount'] = self.ip_active_count
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count
        if self.count is not None:
            result['Count'] = self.count
        if self.android_active_count is not None:
            result['AndroidActiveCount'] = self.android_active_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IosActiveCount') is not None:
            self.ios_active_count = m.get('IosActiveCount')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('AndroidCount') is not None:
            self.android_count = m.get('AndroidCount')
        if m.get('IosCount') is not None:
            self.ios_count = m.get('IosCount')
        if m.get('NewCount') is not None:
            self.new_count = m.get('NewCount')
        if m.get('IpActiveCount') is not None:
            self.ip_active_count = m.get('IpActiveCount')
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('AndroidActiveCount') is not None:
            self.android_active_count = m.get('AndroidActiveCount')
        return self


class DescribeDailyDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        daily_details: List[DescribeDailyDetailsResponseBodyDailyDetails] = None,
    ):
        self.request_id = request_id
        self.daily_details = daily_details

    def validate(self):
        if self.daily_details:
            for k in self.daily_details:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DailyDetails'] = []
        if self.daily_details is not None:
            for k in self.daily_details:
                result['DailyDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.daily_details = []
        if m.get('DailyDetails') is not None:
            for k in m.get('DailyDetails'):
                temp_model = DescribeDailyDetailsResponseBodyDailyDetails()
                self.daily_details.append(temp_model.from_map(k))
        return self


class DescribeDailyDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDailyDetailsResponseBody = None,
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
            temp_model = DescribeDailyDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadUrlsForAppKeyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
        app_key_version: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id
        self.app_key_version = app_key_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_key_version is not None:
            result['AppKeyVersion'] = self.app_key_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppKeyVersion') is not None:
            self.app_key_version = m.get('AppKeyVersion')
        return self


class DescribeDownloadUrlsForAppKeyResponseBodyUrlResultUrls(TeaModel):
    def __init__(
        self,
        android: str = None,
        wins: str = None,
        ios: str = None,
    ):
        self.android = android
        self.wins = wins
        self.ios = ios

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.android is not None:
            result['Android'] = self.android
        if self.wins is not None:
            result['Wins'] = self.wins
        if self.ios is not None:
            result['IOS'] = self.ios
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Android') is not None:
            self.android = m.get('Android')
        if m.get('Wins') is not None:
            self.wins = m.get('Wins')
        if m.get('IOS') is not None:
            self.ios = m.get('IOS')
        return self


class DescribeDownloadUrlsForAppKeyResponseBodyUrlResult(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        urls: DescribeDownloadUrlsForAppKeyResponseBodyUrlResultUrls = None,
    ):
        self.app_id = app_id
        self.urls = urls

    def validate(self):
        if self.urls:
            self.urls.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.urls is not None:
            result['Urls'] = self.urls.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Urls') is not None:
            temp_model = DescribeDownloadUrlsForAppKeyResponseBodyUrlResultUrls()
            self.urls = temp_model.from_map(m['Urls'])
        return self


class DescribeDownloadUrlsForAppKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        url_result: DescribeDownloadUrlsForAppKeyResponseBodyUrlResult = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.url_result = url_result

    def validate(self):
        if self.url_result:
            self.url_result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.url_result is not None:
            result['UrlResult'] = self.url_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('UrlResult') is not None:
            temp_model = DescribeDownloadUrlsForAppKeyResponseBodyUrlResult()
            self.url_result = temp_model.from_map(m['UrlResult'])
        return self


class DescribeDownloadUrlsForAppKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDownloadUrlsForAppKeyResponseBody = None,
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
            temp_model = DescribeDownloadUrlsForAppKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadUrlsForSDKRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
        sdk_version: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id
        self.sdk_version = sdk_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        return self


class DescribeDownloadUrlsForSDKResponseBodyUrlResultUrls(TeaModel):
    def __init__(
        self,
        android: str = None,
        wins: str = None,
        ios: str = None,
    ):
        self.android = android
        self.wins = wins
        self.ios = ios

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.android is not None:
            result['Android'] = self.android
        if self.wins is not None:
            result['Wins'] = self.wins
        if self.ios is not None:
            result['IOS'] = self.ios
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Android') is not None:
            self.android = m.get('Android')
        if m.get('Wins') is not None:
            self.wins = m.get('Wins')
        if m.get('IOS') is not None:
            self.ios = m.get('IOS')
        return self


class DescribeDownloadUrlsForSDKResponseBodyUrlResult(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        urls: DescribeDownloadUrlsForSDKResponseBodyUrlResultUrls = None,
    ):
        self.app_id = app_id
        self.urls = urls

    def validate(self):
        if self.urls:
            self.urls.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.urls is not None:
            result['Urls'] = self.urls.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Urls') is not None:
            temp_model = DescribeDownloadUrlsForSDKResponseBodyUrlResultUrls()
            self.urls = temp_model.from_map(m['Urls'])
        return self


class DescribeDownloadUrlsForSDKResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        url_result: DescribeDownloadUrlsForSDKResponseBodyUrlResult = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.url_result = url_result

    def validate(self):
        if self.url_result:
            self.url_result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.url_result is not None:
            result['UrlResult'] = self.url_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('UrlResult') is not None:
            temp_model = DescribeDownloadUrlsForSDKResponseBodyUrlResult()
            self.url_result = temp_model.from_map(m['UrlResult'])
        return self


class DescribeDownloadUrlsForSDKResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDownloadUrlsForSDKResponseBody = None,
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
            temp_model = DescribeDownloadUrlsForSDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlexAccConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        esn_biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class DescribeFlexAccConfigResponseBodyFlexAccConfig(TeaModel):
    def __init__(
        self,
        status: int = None,
        tcp_ports: str = None,
        udp_ports: str = None,
    ):
        self.status = status
        self.tcp_ports = tcp_ports
        self.udp_ports = udp_ports

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.tcp_ports is not None:
            result['TcpPorts'] = self.tcp_ports
        if self.udp_ports is not None:
            result['UdpPorts'] = self.udp_ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TcpPorts') is not None:
            self.tcp_ports = m.get('TcpPorts')
        if m.get('UdpPorts') is not None:
            self.udp_ports = m.get('UdpPorts')
        return self


class DescribeFlexAccConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        flex_acc_config: DescribeFlexAccConfigResponseBodyFlexAccConfig = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.flex_acc_config = flex_acc_config
        self.prompt_info = prompt_info

    def validate(self):
        if self.flex_acc_config:
            self.flex_acc_config.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.flex_acc_config is not None:
            result['FlexAccConfig'] = self.flex_acc_config.to_map()
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FlexAccConfig') is not None:
            temp_model = DescribeFlexAccConfigResponseBodyFlexAccConfig()
            self.flex_acc_config = temp_model.from_map(m['FlexAccConfig'])
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeFlexAccConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlexAccConfigResponseBody = None,
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
            temp_model = DescribeFlexAccConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlexAccFlowRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        biz_id: int = None,
        begin_time: int = None,
        end_time: int = None,
        interval: int = None,
        api_version: str = None,
    ):
        self.source_ip = source_ip
        self.biz_id = biz_id
        self.begin_time = begin_time
        self.end_time = end_time
        self.interval = interval
        self.api_version = api_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        return self


class DescribeFlexAccFlowResponseBodyFlowDataItems(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
        name: str = None,
    ):
        self.values = values
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeFlexAccFlowResponseBodyFlowDataTimeScope(TeaModel):
    def __init__(
        self,
        start: int = None,
        interval: int = None,
    ):
        self.start = start
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeFlexAccFlowResponseBodyFlowData(TeaModel):
    def __init__(
        self,
        items: List[DescribeFlexAccFlowResponseBodyFlowDataItems] = None,
        categories: List[str] = None,
        time_scope: DescribeFlexAccFlowResponseBodyFlowDataTimeScope = None,
        categories_type: str = None,
    ):
        self.items = items
        self.categories = categories
        self.time_scope = time_scope
        self.categories_type = categories_type

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        if self.time_scope:
            self.time_scope.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.time_scope is not None:
            result['TimeScope'] = self.time_scope.to_map()
        if self.categories_type is not None:
            result['CategoriesType'] = self.categories_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeFlexAccFlowResponseBodyFlowDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('TimeScope') is not None:
            temp_model = DescribeFlexAccFlowResponseBodyFlowDataTimeScope()
            self.time_scope = temp_model.from_map(m['TimeScope'])
        if m.get('CategoriesType') is not None:
            self.categories_type = m.get('CategoriesType')
        return self


class DescribeFlexAccFlowResponseBody(TeaModel):
    def __init__(
        self,
        flow_data: DescribeFlexAccFlowResponseBodyFlowData = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.flow_data = flow_data
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.flow_data:
            self.flow_data.validate()

    def to_map(self):
        result = dict()
        if self.flow_data is not None:
            result['FlowData'] = self.flow_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowData') is not None:
            temp_model = DescribeFlexAccFlowResponseBodyFlowData()
            self.flow_data = temp_model.from_map(m['FlowData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeFlexAccFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlexAccFlowResponseBody = None,
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
            temp_model = DescribeFlexAccFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlexAccFwdRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        esn_biz_id: int = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.esn_biz_id = esn_biz_id
        self.keyword = keyword
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeFlexAccFwdRulesResponseBodyFlexAccFwdRules(TeaModel):
    def __init__(
        self,
        master_ip_list: str = None,
        remark: str = None,
        slave_ip_list: str = None,
        identity: str = None,
        protocol: str = None,
        acc_type: int = None,
        ip_list: str = None,
        domain_list: str = None,
    ):
        self.master_ip_list = master_ip_list
        self.remark = remark
        self.slave_ip_list = slave_ip_list
        self.identity = identity
        self.protocol = protocol
        self.acc_type = acc_type
        self.ip_list = ip_list
        self.domain_list = domain_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.master_ip_list is not None:
            result['MasterIpList'] = self.master_ip_list
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.slave_ip_list is not None:
            result['SlaveIpList'] = self.slave_ip_list
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.acc_type is not None:
            result['AccType'] = self.acc_type
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterIpList') is not None:
            self.master_ip_list = m.get('MasterIpList')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SlaveIpList') is not None:
            self.slave_ip_list = m.get('SlaveIpList')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('AccType') is not None:
            self.acc_type = m.get('AccType')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        return self


class DescribeFlexAccFwdRulesResponseBody(TeaModel):
    def __init__(
        self,
        flex_acc_fwd_rules: List[DescribeFlexAccFwdRulesResponseBodyFlexAccFwdRules] = None,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.flex_acc_fwd_rules = flex_acc_fwd_rules
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.flex_acc_fwd_rules:
            for k in self.flex_acc_fwd_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FlexAccFwdRules'] = []
        if self.flex_acc_fwd_rules is not None:
            for k in self.flex_acc_fwd_rules:
                result['FlexAccFwdRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flex_acc_fwd_rules = []
        if m.get('FlexAccFwdRules') is not None:
            for k in m.get('FlexAccFwdRules'):
                temp_model = DescribeFlexAccFwdRulesResponseBodyFlexAccFwdRules()
                self.flex_acc_fwd_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeFlexAccFwdRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlexAccFwdRulesResponseBody = None,
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
            temp_model = DescribeFlexAccFwdRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlexBackupGroupsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribeFlexBackupGroupsResponseBodyAllBackupGroupsSharedGroups(TeaModel):
    def __init__(
        self,
        status: int = None,
        group_id: str = None,
        spec_desc: str = None,
    ):
        self.status = status
        self.group_id = group_id
        self.spec_desc = spec_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.spec_desc is not None:
            result['SpecDesc'] = self.spec_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SpecDesc') is not None:
            self.spec_desc = m.get('SpecDesc')
        return self


class DescribeFlexBackupGroupsResponseBodyAllBackupGroupsBackupGroups(TeaModel):
    def __init__(
        self,
        status: int = None,
        group_id: str = None,
    ):
        self.status = status
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribeFlexBackupGroupsResponseBodyAllBackupGroups(TeaModel):
    def __init__(
        self,
        shared_groups: List[DescribeFlexBackupGroupsResponseBodyAllBackupGroupsSharedGroups] = None,
        backup_groups: List[DescribeFlexBackupGroupsResponseBodyAllBackupGroupsBackupGroups] = None,
    ):
        self.shared_groups = shared_groups
        self.backup_groups = backup_groups

    def validate(self):
        if self.shared_groups:
            for k in self.shared_groups:
                if k:
                    k.validate()
        if self.backup_groups:
            for k in self.backup_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SharedGroups'] = []
        if self.shared_groups is not None:
            for k in self.shared_groups:
                result['SharedGroups'].append(k.to_map() if k else None)
        result['BackupGroups'] = []
        if self.backup_groups is not None:
            for k in self.backup_groups:
                result['BackupGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shared_groups = []
        if m.get('SharedGroups') is not None:
            for k in m.get('SharedGroups'):
                temp_model = DescribeFlexBackupGroupsResponseBodyAllBackupGroupsSharedGroups()
                self.shared_groups.append(temp_model.from_map(k))
        self.backup_groups = []
        if m.get('BackupGroups') is not None:
            for k in m.get('BackupGroups'):
                temp_model = DescribeFlexBackupGroupsResponseBodyAllBackupGroupsBackupGroups()
                self.backup_groups.append(temp_model.from_map(k))
        return self


class DescribeFlexBackupGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        all_backup_groups: DescribeFlexBackupGroupsResponseBodyAllBackupGroups = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.all_backup_groups = all_backup_groups

    def validate(self):
        if self.all_backup_groups:
            self.all_backup_groups.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.all_backup_groups is not None:
            result['AllBackupGroups'] = self.all_backup_groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('AllBackupGroups') is not None:
            temp_model = DescribeFlexBackupGroupsResponseBodyAllBackupGroups()
            self.all_backup_groups = temp_model.from_map(m['AllBackupGroups'])
        return self


class DescribeFlexBackupGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlexBackupGroupsResponseBody = None,
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
            temp_model = DescribeFlexBackupGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlexConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class DescribeFlexConfigResponseBodyFlexConfig(TeaModel):
    def __init__(
        self,
        status: int = None,
        link_type: int = None,
        ports: str = None,
        rate: int = None,
    ):
        self.status = status
        self.link_type = link_type
        self.ports = ports
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.link_type is not None:
            result['LinkType'] = self.link_type
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.rate is not None:
            result['Rate'] = self.rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('LinkType') is not None:
            self.link_type = m.get('LinkType')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        return self


class DescribeFlexConfigResponseBody(TeaModel):
    def __init__(
        self,
        flex_config: DescribeFlexConfigResponseBodyFlexConfig = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.flex_config = flex_config
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.flex_config:
            self.flex_config.validate()

    def to_map(self):
        result = dict()
        if self.flex_config is not None:
            result['FlexConfig'] = self.flex_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlexConfig') is not None:
            temp_model = DescribeFlexConfigResponseBodyFlexConfig()
            self.flex_config = temp_model.from_map(m['FlexConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeFlexConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlexConfigResponseBody = None,
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
            temp_model = DescribeFlexConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlexFwdRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_biz_id: int = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_biz_id = esn_biz_id
        self.keyword = keyword
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeFlexFwdRulesResponseBodyFlexFwdRules(TeaModel):
    def __init__(
        self,
        master_ip_list: str = None,
        remark: str = None,
        slave_ip_list: str = None,
        protocol: str = None,
        identity: str = None,
    ):
        self.master_ip_list = master_ip_list
        self.remark = remark
        self.slave_ip_list = slave_ip_list
        self.protocol = protocol
        self.identity = identity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.master_ip_list is not None:
            result['MasterIpList'] = self.master_ip_list
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.slave_ip_list is not None:
            result['SlaveIpList'] = self.slave_ip_list
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.identity is not None:
            result['Identity'] = self.identity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterIpList') is not None:
            self.master_ip_list = m.get('MasterIpList')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SlaveIpList') is not None:
            self.slave_ip_list = m.get('SlaveIpList')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        return self


class DescribeFlexFwdRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
        flex_fwd_rules: List[DescribeFlexFwdRulesResponseBodyFlexFwdRules] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info
        self.flex_fwd_rules = flex_fwd_rules

    def validate(self):
        if self.flex_fwd_rules:
            for k in self.flex_fwd_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        result['FlexFwdRules'] = []
        if self.flex_fwd_rules is not None:
            for k in self.flex_fwd_rules:
                result['FlexFwdRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        self.flex_fwd_rules = []
        if m.get('FlexFwdRules') is not None:
            for k in m.get('FlexFwdRules'):
                temp_model = DescribeFlexFwdRulesResponseBodyFlexFwdRules()
                self.flex_fwd_rules.append(temp_model.from_map(k))
        return self


class DescribeFlexFwdRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlexFwdRulesResponseBody = None,
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
            temp_model = DescribeFlexFwdRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlexSechedPolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_biz_id: int = None,
        group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_biz_id = esn_biz_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribeFlexSechedPolicyResponseBodyFlexSechedPolicy(TeaModel):
    def __init__(
        self,
        grey_group_policy: int = None,
        group_inner_policy: int = None,
        backup_group_policy: int = None,
    ):
        self.grey_group_policy = grey_group_policy
        self.group_inner_policy = group_inner_policy
        self.backup_group_policy = backup_group_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.grey_group_policy is not None:
            result['GreyGroupPolicy'] = self.grey_group_policy
        if self.group_inner_policy is not None:
            result['GroupInnerPolicy'] = self.group_inner_policy
        if self.backup_group_policy is not None:
            result['BackupGroupPolicy'] = self.backup_group_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyGroupPolicy') is not None:
            self.grey_group_policy = m.get('GreyGroupPolicy')
        if m.get('GroupInnerPolicy') is not None:
            self.group_inner_policy = m.get('GroupInnerPolicy')
        if m.get('BackupGroupPolicy') is not None:
            self.backup_group_policy = m.get('BackupGroupPolicy')
        return self


class DescribeFlexSechedPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        flex_seched_policy: DescribeFlexSechedPolicyResponseBodyFlexSechedPolicy = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.flex_seched_policy = flex_seched_policy

    def validate(self):
        if self.flex_seched_policy:
            self.flex_seched_policy.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.flex_seched_policy is not None:
            result['FlexSechedPolicy'] = self.flex_seched_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('FlexSechedPolicy') is not None:
            temp_model = DescribeFlexSechedPolicyResponseBodyFlexSechedPolicy()
            self.flex_seched_policy = temp_model.from_map(m['FlexSechedPolicy'])
        return self


class DescribeFlexSechedPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlexSechedPolicyResponseBody = None,
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
            temp_model = DescribeFlexSechedPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowReportRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        interval: int = None,
        start_time: int = None,
        end_time: int = None,
        esn_app_id: str = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.interval = interval
        self.start_time = start_time
        self.end_time = end_time
        self.esn_app_id = esn_app_id
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.esn_app_id is not None:
            result['EsnAppId'] = self.esn_app_id
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EsnAppId') is not None:
            self.esn_app_id = m.get('EsnAppId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeFlowReportResponseBodyFlowReport(TeaModel):
    def __init__(
        self,
        index: int = None,
        act_conns: int = None,
        inact_conns: int = None,
        in_bps: int = None,
        out_bps: int = None,
    ):
        self.index = index
        self.act_conns = act_conns
        self.inact_conns = inact_conns
        self.in_bps = in_bps
        self.out_bps = out_bps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns
        if self.inact_conns is not None:
            result['InactConns'] = self.inact_conns
        if self.in_bps is not None:
            result['InBps'] = self.in_bps
        if self.out_bps is not None:
            result['OutBps'] = self.out_bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')
        if m.get('InactConns') is not None:
            self.inact_conns = m.get('InactConns')
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')
        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')
        return self


class DescribeFlowReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        flow_report: List[DescribeFlowReportResponseBodyFlowReport] = None,
    ):
        self.request_id = request_id
        self.flow_report = flow_report

    def validate(self):
        if self.flow_report:
            for k in self.flow_report:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FlowReport'] = []
        if self.flow_report is not None:
            for k in self.flow_report:
                result['FlowReport'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.flow_report = []
        if m.get('FlowReport') is not None:
            for k in m.get('FlowReport'):
                temp_model = DescribeFlowReportResponseBodyFlowReport()
                self.flow_report.append(temp_model.from_map(k))
        return self


class DescribeFlowReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlowReportResponseBody = None,
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
            temp_model = DescribeFlowReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFullNodesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
        group_id: str = None,
        in_use: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id
        self.group_id = group_id
        self.in_use = in_use

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.in_use is not None:
            result['InUse'] = self.in_use
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        return self


class DescribeFullNodesResponseBodyNodeList(TeaModel):
    def __init__(
        self,
        type: int = None,
        biz_id: str = None,
        ip: str = None,
        region_id: str = None,
        app_name: str = None,
        region_name: str = None,
        group_id: str = None,
        app_id: str = None,
        in_use: int = None,
        biz_name: str = None,
        ddos_status: int = None,
        is_disabled: bool = None,
        threshold: int = None,
        esn_biz_id: str = None,
    ):
        self.type = type
        self.biz_id = biz_id
        self.ip = ip
        self.region_id = region_id
        self.app_name = app_name
        self.region_name = region_name
        self.group_id = group_id
        self.app_id = app_id
        self.in_use = in_use
        self.biz_name = biz_name
        self.ddos_status = ddos_status
        self.is_disabled = is_disabled
        self.threshold = threshold
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.is_disabled is not None:
            result['IsDisabled'] = self.is_disabled
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('IsDisabled') is not None:
            self.is_disabled = m.get('IsDisabled')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class DescribeFullNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        node_list: List[DescribeFullNodesResponseBodyNodeList] = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.node_list = node_list
        self.prompt_info = prompt_info

    def validate(self):
        if self.node_list:
            for k in self.node_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['NodeList'] = []
        if self.node_list is not None:
            for k in self.node_list:
                result['NodeList'].append(k.to_map() if k else None)
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.node_list = []
        if m.get('NodeList') is not None:
            for k in m.get('NodeList'):
                temp_model = DescribeFullNodesResponseBodyNodeList()
                self.node_list.append(temp_model.from_map(k))
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeFullNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFullNodesResponseBody = None,
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
            temp_model = DescribeFullNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFullNodesSummaryRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeFullNodesSummaryResponseBodyFullNodesSummaryHolingNodes(TeaModel):
    def __init__(
        self,
        type: int = None,
        biz_id: str = None,
        ip: str = None,
        region_id: str = None,
        app_name: str = None,
        region_name: str = None,
        group_id: str = None,
        app_id: str = None,
        in_use: int = None,
        biz_name: str = None,
        ddos_status: int = None,
        is_disabled: bool = None,
        threshold: int = None,
        esn_biz_id: str = None,
    ):
        self.type = type
        self.biz_id = biz_id
        self.ip = ip
        self.region_id = region_id
        self.app_name = app_name
        self.region_name = region_name
        self.group_id = group_id
        self.app_id = app_id
        self.in_use = in_use
        self.biz_name = biz_name
        self.ddos_status = ddos_status
        self.is_disabled = is_disabled
        self.threshold = threshold
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.is_disabled is not None:
            result['IsDisabled'] = self.is_disabled
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('IsDisabled') is not None:
            self.is_disabled = m.get('IsDisabled')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class DescribeFullNodesSummaryResponseBodyFullNodesSummaryCleaningNodes(TeaModel):
    def __init__(
        self,
        type: int = None,
        biz_id: str = None,
        ip: str = None,
        region_id: str = None,
        app_name: str = None,
        region_name: str = None,
        group_id: str = None,
        app_id: str = None,
        in_use: int = None,
        biz_name: str = None,
        ddos_status: int = None,
        is_disabled: bool = None,
        threshold: int = None,
        esn_biz_id: str = None,
    ):
        self.type = type
        self.biz_id = biz_id
        self.ip = ip
        self.region_id = region_id
        self.app_name = app_name
        self.region_name = region_name
        self.group_id = group_id
        self.app_id = app_id
        self.in_use = in_use
        self.biz_name = biz_name
        self.ddos_status = ddos_status
        self.is_disabled = is_disabled
        self.threshold = threshold
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.is_disabled is not None:
            result['IsDisabled'] = self.is_disabled
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('IsDisabled') is not None:
            self.is_disabled = m.get('IsDisabled')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class DescribeFullNodesSummaryResponseBodyFullNodesSummary(TeaModel):
    def __init__(
        self,
        clean_count: int = None,
        holing_nodes: List[DescribeFullNodesSummaryResponseBodyFullNodesSummaryHolingNodes] = None,
        hole_count: int = None,
        cleaning_nodes: List[DescribeFullNodesSummaryResponseBodyFullNodesSummaryCleaningNodes] = None,
        used_count: int = None,
        un_used_count: int = None,
        total_count: int = None,
    ):
        self.clean_count = clean_count
        self.holing_nodes = holing_nodes
        self.hole_count = hole_count
        self.cleaning_nodes = cleaning_nodes
        self.used_count = used_count
        self.un_used_count = un_used_count
        self.total_count = total_count

    def validate(self):
        if self.holing_nodes:
            for k in self.holing_nodes:
                if k:
                    k.validate()
        if self.cleaning_nodes:
            for k in self.cleaning_nodes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.clean_count is not None:
            result['CleanCount'] = self.clean_count
        result['HolingNodes'] = []
        if self.holing_nodes is not None:
            for k in self.holing_nodes:
                result['HolingNodes'].append(k.to_map() if k else None)
        if self.hole_count is not None:
            result['HoleCount'] = self.hole_count
        result['CleaningNodes'] = []
        if self.cleaning_nodes is not None:
            for k in self.cleaning_nodes:
                result['CleaningNodes'].append(k.to_map() if k else None)
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        if self.un_used_count is not None:
            result['UnUsedCount'] = self.un_used_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleanCount') is not None:
            self.clean_count = m.get('CleanCount')
        self.holing_nodes = []
        if m.get('HolingNodes') is not None:
            for k in m.get('HolingNodes'):
                temp_model = DescribeFullNodesSummaryResponseBodyFullNodesSummaryHolingNodes()
                self.holing_nodes.append(temp_model.from_map(k))
        if m.get('HoleCount') is not None:
            self.hole_count = m.get('HoleCount')
        self.cleaning_nodes = []
        if m.get('CleaningNodes') is not None:
            for k in m.get('CleaningNodes'):
                temp_model = DescribeFullNodesSummaryResponseBodyFullNodesSummaryCleaningNodes()
                self.cleaning_nodes.append(temp_model.from_map(k))
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        if m.get('UnUsedCount') is not None:
            self.un_used_count = m.get('UnUsedCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeFullNodesSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        full_nodes_summary: DescribeFullNodesSummaryResponseBodyFullNodesSummary = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.full_nodes_summary = full_nodes_summary
        self.prompt_info = prompt_info

    def validate(self):
        if self.full_nodes_summary:
            self.full_nodes_summary.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.full_nodes_summary is not None:
            result['FullNodesSummary'] = self.full_nodes_summary.to_map()
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FullNodesSummary') is not None:
            temp_model = DescribeFullNodesSummaryResponseBodyFullNodesSummary()
            self.full_nodes_summary = temp_model.from_map(m['FullNodesSummary'])
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeFullNodesSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFullNodesSummaryResponseBody = None,
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
            temp_model = DescribeFullNodesSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGfResSummaryRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeGfResSummaryResponseBodyFullNodesSummaryNodes(TeaModel):
    def __init__(
        self,
        type: int = None,
        biz_id: str = None,
        ip: str = None,
        region_id: str = None,
        app_name: str = None,
        region_name: str = None,
        group_id: str = None,
        app_id: str = None,
        in_use: int = None,
        biz_name: str = None,
        ddos_status: int = None,
        is_disabled: bool = None,
        threshold: int = None,
        esn_biz_id: str = None,
    ):
        self.type = type
        self.biz_id = biz_id
        self.ip = ip
        self.region_id = region_id
        self.app_name = app_name
        self.region_name = region_name
        self.group_id = group_id
        self.app_id = app_id
        self.in_use = in_use
        self.biz_name = biz_name
        self.ddos_status = ddos_status
        self.is_disabled = is_disabled
        self.threshold = threshold
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.is_disabled is not None:
            result['IsDisabled'] = self.is_disabled
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('IsDisabled') is not None:
            self.is_disabled = m.get('IsDisabled')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class DescribeGfResSummaryResponseBodyFullNodesSummary(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeGfResSummaryResponseBodyFullNodesSummaryNodes] = None,
        clean_count: int = None,
        hole_count: int = None,
        used_count: int = None,
        un_used_count: int = None,
        total_count: int = None,
    ):
        self.nodes = nodes
        self.clean_count = clean_count
        self.hole_count = hole_count
        self.used_count = used_count
        self.un_used_count = un_used_count
        self.total_count = total_count

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.clean_count is not None:
            result['CleanCount'] = self.clean_count
        if self.hole_count is not None:
            result['HoleCount'] = self.hole_count
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        if self.un_used_count is not None:
            result['UnUsedCount'] = self.un_used_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeGfResSummaryResponseBodyFullNodesSummaryNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('CleanCount') is not None:
            self.clean_count = m.get('CleanCount')
        if m.get('HoleCount') is not None:
            self.hole_count = m.get('HoleCount')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        if m.get('UnUsedCount') is not None:
            self.un_used_count = m.get('UnUsedCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeGfResSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        full_nodes_summary: DescribeGfResSummaryResponseBodyFullNodesSummary = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.full_nodes_summary = full_nodes_summary
        self.prompt_info = prompt_info

    def validate(self):
        if self.full_nodes_summary:
            self.full_nodes_summary.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.full_nodes_summary is not None:
            result['FullNodesSummary'] = self.full_nodes_summary.to_map()
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FullNodesSummary') is not None:
            temp_model = DescribeGfResSummaryResponseBodyFullNodesSummary()
            self.full_nodes_summary = temp_model.from_map(m['FullNodesSummary'])
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeGfResSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGfResSummaryResponseBody = None,
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
            temp_model = DescribeGfResSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeGroupListResponseBodyGroupList(TeaModel):
    def __init__(
        self,
        status: str = None,
        is_dns_enabled: bool = None,
        group_id: str = None,
        black_ip: int = None,
        normal_ip: int = None,
        clean_ip: int = None,
        total_ip: int = None,
        is_disabled: bool = None,
        dns_status: str = None,
        group_desc: str = None,
    ):
        self.status = status
        self.is_dns_enabled = is_dns_enabled
        self.group_id = group_id
        self.black_ip = black_ip
        self.normal_ip = normal_ip
        self.clean_ip = clean_ip
        self.total_ip = total_ip
        self.is_disabled = is_disabled
        self.dns_status = dns_status
        self.group_desc = group_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.is_dns_enabled is not None:
            result['IsDnsEnabled'] = self.is_dns_enabled
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.black_ip is not None:
            result['BlackIp'] = self.black_ip
        if self.normal_ip is not None:
            result['NormalIp'] = self.normal_ip
        if self.clean_ip is not None:
            result['CleanIp'] = self.clean_ip
        if self.total_ip is not None:
            result['TotalIp'] = self.total_ip
        if self.is_disabled is not None:
            result['IsDisabled'] = self.is_disabled
        if self.dns_status is not None:
            result['DnsStatus'] = self.dns_status
        if self.group_desc is not None:
            result['GroupDesc'] = self.group_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('IsDnsEnabled') is not None:
            self.is_dns_enabled = m.get('IsDnsEnabled')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('BlackIp') is not None:
            self.black_ip = m.get('BlackIp')
        if m.get('NormalIp') is not None:
            self.normal_ip = m.get('NormalIp')
        if m.get('CleanIp') is not None:
            self.clean_ip = m.get('CleanIp')
        if m.get('TotalIp') is not None:
            self.total_ip = m.get('TotalIp')
        if m.get('IsDisabled') is not None:
            self.is_disabled = m.get('IsDisabled')
        if m.get('DnsStatus') is not None:
            self.dns_status = m.get('DnsStatus')
        if m.get('GroupDesc') is not None:
            self.group_desc = m.get('GroupDesc')
        return self


class DescribeGroupListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group_list: List[DescribeGroupListResponseBodyGroupList] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.group_list = group_list
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.group_list:
            for k in self.group_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['GroupList'] = []
        if self.group_list is not None:
            for k in self.group_list:
                result['GroupList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.group_list = []
        if m.get('GroupList') is not None:
            for k in m.get('GroupList'):
                temp_model = DescribeGroupListResponseBodyGroupList()
                self.group_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeGroupListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGroupListResponseBody = None,
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
            temp_model = DescribeGroupListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupSimpleListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeGroupSimpleListResponseBodyGroupList(TeaModel):
    def __init__(
        self,
        is_dns_enabled: bool = None,
        group_id: str = None,
        group_name: str = None,
        app_id: str = None,
        biz_id: str = None,
        is_disabled: bool = None,
    ):
        self.is_dns_enabled = is_dns_enabled
        self.group_id = group_id
        self.group_name = group_name
        self.app_id = app_id
        self.biz_id = biz_id
        self.is_disabled = is_disabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_dns_enabled is not None:
            result['IsDnsEnabled'] = self.is_dns_enabled
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.is_disabled is not None:
            result['IsDisabled'] = self.is_disabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDnsEnabled') is not None:
            self.is_dns_enabled = m.get('IsDnsEnabled')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IsDisabled') is not None:
            self.is_disabled = m.get('IsDisabled')
        return self


class DescribeGroupSimpleListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group_list: List[DescribeGroupSimpleListResponseBodyGroupList] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.group_list = group_list
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.group_list:
            for k in self.group_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['GroupList'] = []
        if self.group_list is not None:
            for k in self.group_list:
                result['GroupList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.group_list = []
        if m.get('GroupList') is not None:
            for k in m.get('GroupList'):
                temp_model = DescribeGroupSimpleListResponseBodyGroupList()
                self.group_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeGroupSimpleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGroupSimpleListResponseBody = None,
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
            temp_model = DescribeGroupSimpleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeInstanceResponseBodyInstanceInfo(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        status: int = None,
        package_code: str = None,
        region: str = None,
        spec_map: Dict[str, Any] = None,
        instance_id: str = None,
    ):
        self.end_time = end_time
        self.status = status
        self.package_code = package_code
        self.region = region
        self.spec_map = spec_map
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.package_code is not None:
            result['PackageCode'] = self.package_code
        if self.region is not None:
            result['Region'] = self.region
        if self.spec_map is not None:
            result['SpecMap'] = self.spec_map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PackageCode') is not None:
            self.package_code = m.get('PackageCode')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SpecMap') is not None:
            self.spec_map = m.get('SpecMap')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        instance_info: DescribeInstanceResponseBodyInstanceInfo = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.instance_info = instance_info

    def validate(self):
        if self.instance_info:
            self.instance_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('InstanceInfo') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceInfo()
            self.instance_info = temp_model.from_map(m['InstanceInfo'])
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceResponseBody = None,
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
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpFlowReportRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        ip: str = None,
        end_time: int = None,
        fport: int = None,
        interval: int = None,
        protocol_ex: int = None,
        start_time: int = None,
    ):
        self.source_ip = source_ip
        self.ip = ip
        self.end_time = end_time
        self.fport = fport
        self.interval = interval
        self.protocol_ex = protocol_ex
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.fport is not None:
            result['FPort'] = self.fport
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.protocol_ex is not None:
            result['ProtocolEx'] = self.protocol_ex
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FPort') is not None:
            self.fport = m.get('FPort')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ProtocolEx') is not None:
            self.protocol_ex = m.get('ProtocolEx')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeIpFlowReportResponseBodyIpFlowReportList(TeaModel):
    def __init__(
        self,
        outpps: str = None,
        cps: str = None,
        inkbps: str = None,
        inpps: str = None,
        inbps: str = None,
        conns: bool = None,
        inpkts: str = None,
        inbytes: str = None,
        outbytes: str = None,
        cluster_name: str = None,
        actconns: str = None,
        outbps: str = None,
        outpkts: str = None,
        vip: str = None,
        qtime: str = None,
        outkbps: str = None,
        inactconns: str = None,
    ):
        self.outpps = outpps
        self.cps = cps
        self.inkbps = inkbps
        self.inpps = inpps
        self.inbps = inbps
        self.conns = conns
        self.inpkts = inpkts
        self.inbytes = inbytes
        self.outbytes = outbytes
        self.cluster_name = cluster_name
        self.actconns = actconns
        self.outbps = outbps
        self.outpkts = outpkts
        self.vip = vip
        self.qtime = qtime
        self.outkbps = outkbps
        self.inactconns = inactconns

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.outpps is not None:
            result['Outpps'] = self.outpps
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.inkbps is not None:
            result['Inkbps'] = self.inkbps
        if self.inpps is not None:
            result['Inpps'] = self.inpps
        if self.inbps is not None:
            result['Inbps'] = self.inbps
        if self.conns is not None:
            result['Conns'] = self.conns
        if self.inpkts is not None:
            result['Inpkts'] = self.inpkts
        if self.inbytes is not None:
            result['Inbytes'] = self.inbytes
        if self.outbytes is not None:
            result['Outbytes'] = self.outbytes
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.actconns is not None:
            result['Actconns'] = self.actconns
        if self.outbps is not None:
            result['Outbps'] = self.outbps
        if self.outpkts is not None:
            result['Outpkts'] = self.outpkts
        if self.vip is not None:
            result['Vip'] = self.vip
        if self.qtime is not None:
            result['Qtime'] = self.qtime
        if self.outkbps is not None:
            result['Outkbps'] = self.outkbps
        if self.inactconns is not None:
            result['Inactconns'] = self.inactconns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outpps') is not None:
            self.outpps = m.get('Outpps')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Inkbps') is not None:
            self.inkbps = m.get('Inkbps')
        if m.get('Inpps') is not None:
            self.inpps = m.get('Inpps')
        if m.get('Inbps') is not None:
            self.inbps = m.get('Inbps')
        if m.get('Conns') is not None:
            self.conns = m.get('Conns')
        if m.get('Inpkts') is not None:
            self.inpkts = m.get('Inpkts')
        if m.get('Inbytes') is not None:
            self.inbytes = m.get('Inbytes')
        if m.get('Outbytes') is not None:
            self.outbytes = m.get('Outbytes')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Actconns') is not None:
            self.actconns = m.get('Actconns')
        if m.get('Outbps') is not None:
            self.outbps = m.get('Outbps')
        if m.get('Outpkts') is not None:
            self.outpkts = m.get('Outpkts')
        if m.get('Vip') is not None:
            self.vip = m.get('Vip')
        if m.get('Qtime') is not None:
            self.qtime = m.get('Qtime')
        if m.get('Outkbps') is not None:
            self.outkbps = m.get('Outkbps')
        if m.get('Inactconns') is not None:
            self.inactconns = m.get('Inactconns')
        return self


class DescribeIpFlowReportResponseBody(TeaModel):
    def __init__(
        self,
        ip_flow_report_list: List[DescribeIpFlowReportResponseBodyIpFlowReportList] = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.ip_flow_report_list = ip_flow_report_list
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.ip_flow_report_list:
            for k in self.ip_flow_report_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['IpFlowReportList'] = []
        if self.ip_flow_report_list is not None:
            for k in self.ip_flow_report_list:
                result['IpFlowReportList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_flow_report_list = []
        if m.get('IpFlowReportList') is not None:
            for k in m.get('IpFlowReportList'):
                temp_model = DescribeIpFlowReportResponseBodyIpFlowReportList()
                self.ip_flow_report_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeIpFlowReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIpFlowReportResponseBody = None,
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
            temp_model = DescribeIpFlowReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJianYuTestGetRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeJianYuTestGetResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        id: int = None,
    ):
        self.create_time = create_time
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeJianYuTestGetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        data: DescribeJianYuTestGetResponseBodyData = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('Data') is not None:
            temp_model = DescribeJianYuTestGetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeJianYuTestGetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeJianYuTestGetResponseBody = None,
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
            temp_model = DescribeJianYuTestGetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJianYuTestListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeJianYuTestListResponseBodyList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        id: int = None,
    ):
        self.create_time = create_time
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeJianYuTestListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        list: List[DescribeJianYuTestListResponseBodyList] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeJianYuTestListResponseBodyList()
                self.list.append(temp_model.from_map(k))
        return self


class DescribeJianYuTestListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeJianYuTestListResponseBody = None,
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
            temp_model = DescribeJianYuTestListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJianYuTestPaginationRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: str = None,
        end_time: str = None,
        page: str = None,
        page_size: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeJianYuTestPaginationResponseBodyList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        id: int = None,
    ):
        self.create_time = create_time
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeJianYuTestPaginationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
        list: List[DescribeJianYuTestPaginationResponseBodyList] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeJianYuTestPaginationResponseBodyList()
                self.list.append(temp_model.from_map(k))
        return self


class DescribeJianYuTestPaginationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeJianYuTestPaginationResponseBody = None,
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
            temp_model = DescribeJianYuTestPaginationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeL4EventsSelectiveRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        begin_time: int = None,
        end_time: int = None,
        page: int = None,
        page_size: int = None,
        esn_app_id: str = None,
        esn_biz_id: str = None,
        group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.begin_time = begin_time
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.esn_app_id = esn_app_id
        self.esn_biz_id = esn_biz_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.esn_app_id is not None:
            result['EsnAppId'] = self.esn_app_id
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EsnAppId') is not None:
            self.esn_app_id = m.get('EsnAppId')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribeL4EventsSelectiveResponseBodyEsnL4EventList(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        target_region: str = None,
        attack_type: int = None,
        result: int = None,
        attack_src: str = None,
        duration: int = None,
        attack_time: int = None,
        max_attack: int = None,
        target: str = None,
        target_type: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.target_region = target_region
        self.attack_type = attack_type
        self.result = result
        self.attack_src = attack_src
        self.duration = duration
        self.attack_time = attack_time
        self.max_attack = max_attack
        self.target = target
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.target_region is not None:
            result['TargetRegion'] = self.target_region
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.result is not None:
            result['Result'] = self.result
        if self.attack_src is not None:
            result['AttackSrc'] = self.attack_src
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.attack_time is not None:
            result['AttackTime'] = self.attack_time
        if self.max_attack is not None:
            result['MaxAttack'] = self.max_attack
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TargetRegion') is not None:
            self.target_region = m.get('TargetRegion')
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('AttackSrc') is not None:
            self.attack_src = m.get('AttackSrc')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('AttackTime') is not None:
            self.attack_time = m.get('AttackTime')
        if m.get('MaxAttack') is not None:
            self.max_attack = m.get('MaxAttack')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class DescribeL4EventsSelectiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        esn_l4event_list: List[DescribeL4EventsSelectiveResponseBodyEsnL4EventList] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.esn_l4event_list = esn_l4event_list
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.esn_l4event_list:
            for k in self.esn_l4event_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['EsnL4EventList'] = []
        if self.esn_l4event_list is not None:
            for k in self.esn_l4event_list:
                result['EsnL4EventList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.esn_l4event_list = []
        if m.get('EsnL4EventList') is not None:
            for k in m.get('EsnL4EventList'):
                temp_model = DescribeL4EventsSelectiveResponseBodyEsnL4EventList()
                self.esn_l4event_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeL4EventsSelectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeL4EventsSelectiveResponseBody = None,
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
            temp_model = DescribeL4EventsSelectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLayer4RulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeLayer4RulesResponseBodyExtInfo(TeaModel):
    def __init__(
        self,
        use_cc: int = None,
        ng_route_enable: int = None,
    ):
        self.use_cc = use_cc
        self.ng_route_enable = ng_route_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.use_cc is not None:
            result['UseCc'] = self.use_cc
        if self.ng_route_enable is not None:
            result['NgRouteEnable'] = self.ng_route_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UseCc') is not None:
            self.use_cc = m.get('UseCc')
        if m.get('NgRouteEnable') is not None:
            self.ng_route_enable = m.get('NgRouteEnable')
        return self


class DescribeLayer4RulesResponseBodyL4RuleList(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        app_id: int = None,
        back_port: int = None,
        biz_id: int = None,
        rservers: List[str] = None,
        lvs_policy: str = None,
        front_port: int = None,
        rule_id: str = None,
    ):
        self.protocol = protocol
        self.app_id = app_id
        self.back_port = back_port
        self.biz_id = biz_id
        self.rservers = rservers
        self.lvs_policy = lvs_policy
        self.front_port = front_port
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.back_port is not None:
            result['BackPort'] = self.back_port
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.rservers is not None:
            result['Rservers'] = self.rservers
        if self.lvs_policy is not None:
            result['LvsPolicy'] = self.lvs_policy
        if self.front_port is not None:
            result['FrontPort'] = self.front_port
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BackPort') is not None:
            self.back_port = m.get('BackPort')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Rservers') is not None:
            self.rservers = m.get('Rservers')
        if m.get('LvsPolicy') is not None:
            self.lvs_policy = m.get('LvsPolicy')
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeLayer4RulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ext_info: DescribeLayer4RulesResponseBodyExtInfo = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
        l_4rule_list: List[DescribeLayer4RulesResponseBodyL4RuleList] = None,
    ):
        self.request_id = request_id
        self.ext_info = ext_info
        self.total = total
        self.prompt_info = prompt_info
        self.l_4rule_list = l_4rule_list

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()
        if self.l_4rule_list:
            for k in self.l_4rule_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info.to_map()
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        result['L4RuleList'] = []
        if self.l_4rule_list is not None:
            for k in self.l_4rule_list:
                result['L4RuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExtInfo') is not None:
            temp_model = DescribeLayer4RulesResponseBodyExtInfo()
            self.ext_info = temp_model.from_map(m['ExtInfo'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        self.l_4rule_list = []
        if m.get('L4RuleList') is not None:
            for k in m.get('L4RuleList'):
                temp_model = DescribeLayer4RulesResponseBodyL4RuleList()
                self.l_4rule_list.append(temp_model.from_map(k))
        return self


class DescribeLayer4RulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLayer4RulesResponseBody = None,
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
            temp_model = DescribeLayer4RulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMianLiuResSummaryRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeMianLiuResSummaryResponseBodyFullNodesSummaryNodes(TeaModel):
    def __init__(
        self,
        type: int = None,
        biz_id: str = None,
        ip: str = None,
        region_id: str = None,
        app_name: str = None,
        region_name: str = None,
        group_id: str = None,
        app_id: str = None,
        in_use: int = None,
        biz_name: str = None,
        ddos_status: int = None,
        is_disabled: bool = None,
        threshold: int = None,
        esn_biz_id: str = None,
    ):
        self.type = type
        self.biz_id = biz_id
        self.ip = ip
        self.region_id = region_id
        self.app_name = app_name
        self.region_name = region_name
        self.group_id = group_id
        self.app_id = app_id
        self.in_use = in_use
        self.biz_name = biz_name
        self.ddos_status = ddos_status
        self.is_disabled = is_disabled
        self.threshold = threshold
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.is_disabled is not None:
            result['IsDisabled'] = self.is_disabled
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('IsDisabled') is not None:
            self.is_disabled = m.get('IsDisabled')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class DescribeMianLiuResSummaryResponseBodyFullNodesSummary(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeMianLiuResSummaryResponseBodyFullNodesSummaryNodes] = None,
        clean_count: int = None,
        hole_count: int = None,
        used_count: int = None,
        un_used_count: int = None,
        total_count: int = None,
    ):
        self.nodes = nodes
        self.clean_count = clean_count
        self.hole_count = hole_count
        self.used_count = used_count
        self.un_used_count = un_used_count
        self.total_count = total_count

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.clean_count is not None:
            result['CleanCount'] = self.clean_count
        if self.hole_count is not None:
            result['HoleCount'] = self.hole_count
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        if self.un_used_count is not None:
            result['UnUsedCount'] = self.un_used_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeMianLiuResSummaryResponseBodyFullNodesSummaryNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('CleanCount') is not None:
            self.clean_count = m.get('CleanCount')
        if m.get('HoleCount') is not None:
            self.hole_count = m.get('HoleCount')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        if m.get('UnUsedCount') is not None:
            self.un_used_count = m.get('UnUsedCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeMianLiuResSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        full_nodes_summary: DescribeMianLiuResSummaryResponseBodyFullNodesSummary = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.full_nodes_summary = full_nodes_summary
        self.prompt_info = prompt_info

    def validate(self):
        if self.full_nodes_summary:
            self.full_nodes_summary.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.full_nodes_summary is not None:
            result['FullNodesSummary'] = self.full_nodes_summary.to_map()
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FullNodesSummary') is not None:
            temp_model = DescribeMianLiuResSummaryResponseBodyFullNodesSummary()
            self.full_nodes_summary = temp_model.from_map(m['FullNodesSummary'])
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeMianLiuResSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMianLiuResSummaryResponseBody = None,
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
            temp_model = DescribeMianLiuResSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNgSourceDiagnosisLogRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: int = None,
        end_time: int = None,
        page: int = None,
        page_size: int = None,
        app_id: str = None,
        biz_id: str = None,
        source: str = None,
        source_port: str = None,
        detect_port: str = None,
        detect_ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.app_id = app_id
        self.biz_id = biz_id
        self.source = source
        self.source_port = source_port
        self.detect_port = detect_port
        self.detect_ip = detect_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        if self.detect_port is not None:
            result['DetectPort'] = self.detect_port
        if self.detect_ip is not None:
            result['DetectIp'] = self.detect_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        if m.get('DetectPort') is not None:
            self.detect_port = m.get('DetectPort')
        if m.get('DetectIp') is not None:
            self.detect_ip = m.get('DetectIp')
        return self


class DescribeNgSourceDiagnosisLogResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        time: str = None,
        source_ip: str = None,
        app_name: str = None,
        source_port: str = None,
        detect_port: str = None,
        app_id: str = None,
        detect_ip: str = None,
        user_id: str = None,
        biz_name: str = None,
        biz_id: str = None,
        source_ip_location: str = None,
    ):
        self.time = time
        self.source_ip = source_ip
        self.app_name = app_name
        self.source_port = source_port
        self.detect_port = detect_port
        self.app_id = app_id
        self.detect_ip = detect_ip
        self.user_id = user_id
        self.biz_name = biz_name
        self.biz_id = biz_id
        self.source_ip_location = source_ip_location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        if self.detect_port is not None:
            result['DetectPort'] = self.detect_port
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.detect_ip is not None:
            result['DetectIp'] = self.detect_ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.source_ip_location is not None:
            result['SourceIpLocation'] = self.source_ip_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        if m.get('DetectPort') is not None:
            self.detect_port = m.get('DetectPort')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DetectIp') is not None:
            self.detect_ip = m.get('DetectIp')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SourceIpLocation') is not None:
            self.source_ip_location = m.get('SourceIpLocation')
        return self


class DescribeNgSourceDiagnosisLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[DescribeNgSourceDiagnosisLogResponseBodyStatistic] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeNgSourceDiagnosisLogResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeNgSourceDiagnosisLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNgSourceDiagnosisLogResponseBody = None,
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
            temp_model = DescribeNgSourceDiagnosisLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRemainQpsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeRemainQpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        qps: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.qps = qps
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeRemainQpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRemainQpsResponseBody = None,
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
            temp_model = DescribeRemainQpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRequestStatisticByEsnBizIntervalRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_app: str = None,
        esn_biz: str = None,
        start_time: int = None,
        end_time: int = None,
        interval: int = None,
        province: str = None,
        country: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_app = esn_app
        self.esn_biz = esn_biz
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.province = province
        self.country = country
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_app is not None:
            result['EsnApp'] = self.esn_app
        if self.esn_biz is not None:
            result['EsnBiz'] = self.esn_biz
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.province is not None:
            result['Province'] = self.province
        if self.country is not None:
            result['Country'] = self.country
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnApp') is not None:
            self.esn_app = m.get('EsnApp')
        if m.get('EsnBiz') is not None:
            self.esn_biz = m.get('EsnBiz')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRequestStatisticByEsnBizIntervalResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        index: int = None,
        time: int = None,
        failure_count: int = None,
        total_count: int = None,
        success_count: int = None,
    ):
        self.index = index
        self.time = time
        self.failure_count = failure_count
        self.total_count = total_count
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.time is not None:
            result['Time'] = self.time
        if self.failure_count is not None:
            result['FailureCount'] = self.failure_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('FailureCount') is not None:
            self.failure_count = m.get('FailureCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class DescribeRequestStatisticByEsnBizIntervalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[DescribeRequestStatisticByEsnBizIntervalResponseBodyStatistic] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeRequestStatisticByEsnBizIntervalResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeRequestStatisticByEsnBizIntervalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRequestStatisticByEsnBizIntervalResponseBody = None,
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
            temp_model = DescribeRequestStatisticByEsnBizIntervalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRequestStatisticCountByEsnBiz1DayRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_app: str = None,
        esn_biz: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_app = esn_app
        self.esn_biz = esn_biz
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_app is not None:
            result['EsnApp'] = self.esn_app
        if self.esn_biz is not None:
            result['EsnBiz'] = self.esn_biz
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnApp') is not None:
            self.esn_app = m.get('EsnApp')
        if m.get('EsnBiz') is not None:
            self.esn_biz = m.get('EsnBiz')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeRequestStatisticCountByEsnBiz1DayResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        failure_count: int = None,
        success_count: int = None,
        total_count: int = None,
    ):
        self.failure_count = failure_count
        self.success_count = success_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.failure_count is not None:
            result['FailureCount'] = self.failure_count
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureCount') is not None:
            self.failure_count = m.get('FailureCount')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRequestStatisticCountByEsnBiz1DayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: DescribeRequestStatisticCountByEsnBiz1DayResponseBodyStatistic = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            self.statistic.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistic is not None:
            result['Statistic'] = self.statistic.to_map()
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Statistic') is not None:
            temp_model = DescribeRequestStatisticCountByEsnBiz1DayResponseBodyStatistic()
            self.statistic = temp_model.from_map(m['Statistic'])
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeRequestStatisticCountByEsnBiz1DayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRequestStatisticCountByEsnBiz1DayResponseBody = None,
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
            temp_model = DescribeRequestStatisticCountByEsnBiz1DayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRequestStatisticCountByEsnBiz1DayProvinceRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_app: str = None,
        esn_biz: str = None,
        start_time: int = None,
        end_time: int = None,
        page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_app = esn_app
        self.esn_biz = esn_biz
        self.start_time = start_time
        self.end_time = end_time
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_app is not None:
            result['EsnApp'] = self.esn_app
        if self.esn_biz is not None:
            result['EsnBiz'] = self.esn_biz
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnApp') is not None:
            self.esn_app = m.get('EsnApp')
        if m.get('EsnBiz') is not None:
            self.esn_biz = m.get('EsnBiz')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRequestStatisticCountByEsnBiz1DayProvinceResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        failure_count: int = None,
        province_id: int = None,
        total_count: int = None,
        success_count: int = None,
    ):
        self.failure_count = failure_count
        self.province_id = province_id
        self.total_count = total_count
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.failure_count is not None:
            result['FailureCount'] = self.failure_count
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureCount') is not None:
            self.failure_count = m.get('FailureCount')
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class DescribeRequestStatisticCountByEsnBiz1DayProvinceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[DescribeRequestStatisticCountByEsnBiz1DayProvinceResponseBodyStatistic] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeRequestStatisticCountByEsnBiz1DayProvinceResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeRequestStatisticCountByEsnBiz1DayProvinceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRequestStatisticCountByEsnBiz1DayProvinceResponseBody = None,
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
            temp_model = DescribeRequestStatisticCountByEsnBiz1DayProvinceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRequestStatisticCountByEsnBiz1M30MRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_app: str = None,
        esn_biz: str = None,
        time: int = None,
        page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_app = esn_app
        self.esn_biz = esn_biz
        self.time = time
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_app is not None:
            result['EsnApp'] = self.esn_app
        if self.esn_biz is not None:
            result['EsnBiz'] = self.esn_biz
        if self.time is not None:
            result['Time'] = self.time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnApp') is not None:
            self.esn_app = m.get('EsnApp')
        if m.get('EsnBiz') is not None:
            self.esn_biz = m.get('EsnBiz')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRequestStatisticCountByEsnBiz1M30MResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        time: int = None,
        count: int = None,
    ):
        self.time = time
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeRequestStatisticCountByEsnBiz1M30MResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[DescribeRequestStatisticCountByEsnBiz1M30MResponseBodyStatistic] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeRequestStatisticCountByEsnBiz1M30MResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeRequestStatisticCountByEsnBiz1M30MResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRequestStatisticCountByEsnBiz1M30MResponseBody = None,
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
            temp_model = DescribeRequestStatisticCountByEsnBiz1M30MResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRequestStatisticCountByEsnBiz30MRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_app: str = None,
        esn_biz: str = None,
        time: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_app = esn_app
        self.esn_biz = esn_biz
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_app is not None:
            result['EsnApp'] = self.esn_app
        if self.esn_biz is not None:
            result['EsnBiz'] = self.esn_biz
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnApp') is not None:
            self.esn_app = m.get('EsnApp')
        if m.get('EsnBiz') is not None:
            self.esn_biz = m.get('EsnBiz')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeRequestStatisticCountByEsnBiz30MResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        failure_count: int = None,
        success_count: int = None,
        total_count: int = None,
    ):
        self.failure_count = failure_count
        self.success_count = success_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.failure_count is not None:
            result['FailureCount'] = self.failure_count
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureCount') is not None:
            self.failure_count = m.get('FailureCount')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRequestStatisticCountByEsnBiz30MResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: DescribeRequestStatisticCountByEsnBiz30MResponseBodyStatistic = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            self.statistic.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistic is not None:
            result['Statistic'] = self.statistic.to_map()
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Statistic') is not None:
            temp_model = DescribeRequestStatisticCountByEsnBiz30MResponseBodyStatistic()
            self.statistic = temp_model.from_map(m['Statistic'])
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeRequestStatisticCountByEsnBiz30MResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRequestStatisticCountByEsnBiz30MResponseBody = None,
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
            temp_model = DescribeRequestStatisticCountByEsnBiz30MResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRequestStatisticCountByEsnBizGroup30MRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_app: str = None,
        esn_biz: str = None,
        time: int = None,
        page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_app = esn_app
        self.esn_biz = esn_biz
        self.time = time
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_app is not None:
            result['EsnApp'] = self.esn_app
        if self.esn_biz is not None:
            result['EsnBiz'] = self.esn_biz
        if self.time is not None:
            result['Time'] = self.time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnApp') is not None:
            self.esn_app = m.get('EsnApp')
        if m.get('EsnBiz') is not None:
            self.esn_biz = m.get('EsnBiz')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRequestStatisticCountByEsnBizGroup30MResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        detect_ip: str = None,
        esn_group_id: str = None,
        count: int = None,
    ):
        self.detect_ip = detect_ip
        self.esn_group_id = esn_group_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.detect_ip is not None:
            result['DetectIp'] = self.detect_ip
        if self.esn_group_id is not None:
            result['EsnGroupId'] = self.esn_group_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectIp') is not None:
            self.detect_ip = m.get('DetectIp')
        if m.get('EsnGroupId') is not None:
            self.esn_group_id = m.get('EsnGroupId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeRequestStatisticCountByEsnBizGroup30MResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[DescribeRequestStatisticCountByEsnBizGroup30MResponseBodyStatistic] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeRequestStatisticCountByEsnBizGroup30MResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeRequestStatisticCountByEsnBizGroup30MResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRequestStatisticCountByEsnBizGroup30MResponseBody = None,
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
            temp_model = DescribeRequestStatisticCountByEsnBizGroup30MResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRequestStatisticLogRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: int = None,
        end_time: int = None,
        page: int = None,
        page_size: int = None,
        esn_app: str = None,
        esn_biz: str = None,
        esn_group: str = None,
        source: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        isp: str = None,
        token: str = None,
        sdk: str = None,
        call_result: str = None,
        os_type: str = None,
        escaped_less_than: int = None,
        escaped_greater_than: int = None,
        detect_ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.esn_app = esn_app
        self.esn_biz = esn_biz
        self.esn_group = esn_group
        self.source = source
        self.country = country
        self.province = province
        self.city = city
        self.isp = isp
        self.token = token
        self.sdk = sdk
        self.call_result = call_result
        self.os_type = os_type
        self.escaped_less_than = escaped_less_than
        self.escaped_greater_than = escaped_greater_than
        self.detect_ip = detect_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.esn_app is not None:
            result['EsnApp'] = self.esn_app
        if self.esn_biz is not None:
            result['EsnBiz'] = self.esn_biz
        if self.esn_group is not None:
            result['EsnGroup'] = self.esn_group
        if self.source is not None:
            result['Source'] = self.source
        if self.country is not None:
            result['Country'] = self.country
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.token is not None:
            result['Token'] = self.token
        if self.sdk is not None:
            result['SDK'] = self.sdk
        if self.call_result is not None:
            result['CallResult'] = self.call_result
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.escaped_less_than is not None:
            result['EscapedLessThan'] = self.escaped_less_than
        if self.escaped_greater_than is not None:
            result['EscapedGreaterThan'] = self.escaped_greater_than
        if self.detect_ip is not None:
            result['DetectIp'] = self.detect_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EsnApp') is not None:
            self.esn_app = m.get('EsnApp')
        if m.get('EsnBiz') is not None:
            self.esn_biz = m.get('EsnBiz')
        if m.get('EsnGroup') is not None:
            self.esn_group = m.get('EsnGroup')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('SDK') is not None:
            self.sdk = m.get('SDK')
        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('EscapedLessThan') is not None:
            self.escaped_less_than = m.get('EscapedLessThan')
        if m.get('EscapedGreaterThan') is not None:
            self.escaped_greater_than = m.get('EscapedGreaterThan')
        if m.get('DetectIp') is not None:
            self.detect_ip = m.get('DetectIp')
        return self


class DescribeRequestStatisticLogResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        server_time: str = None,
        call_result: str = None,
        token: str = None,
        user_id: str = None,
        country_id: str = None,
        detect_ip: str = None,
        esn_app_id: str = None,
        city: str = None,
        isp_id: str = None,
        isp: str = None,
        escaped_time: str = None,
        source_ip: str = None,
        city_id: str = None,
        province_id: str = None,
        os_type: str = None,
        sdk_version: str = None,
        country: str = None,
        esn_group_id: str = None,
        province: str = None,
        esn_biz_id: str = None,
    ):
        self.server_time = server_time
        self.call_result = call_result
        self.token = token
        self.user_id = user_id
        self.country_id = country_id
        self.detect_ip = detect_ip
        self.esn_app_id = esn_app_id
        self.city = city
        self.isp_id = isp_id
        self.isp = isp
        self.escaped_time = escaped_time
        self.source_ip = source_ip
        self.city_id = city_id
        self.province_id = province_id
        self.os_type = os_type
        self.sdk_version = sdk_version
        self.country = country
        self.esn_group_id = esn_group_id
        self.province = province
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.server_time is not None:
            result['ServerTime'] = self.server_time
        if self.call_result is not None:
            result['CallResult'] = self.call_result
        if self.token is not None:
            result['Token'] = self.token
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.detect_ip is not None:
            result['DetectIp'] = self.detect_ip
        if self.esn_app_id is not None:
            result['EsnAppId'] = self.esn_app_id
        if self.city is not None:
            result['City'] = self.city
        if self.isp_id is not None:
            result['IspId'] = self.isp_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.escaped_time is not None:
            result['EscapedTime'] = self.escaped_time
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.city_id is not None:
            result['CityId'] = self.city_id
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.country is not None:
            result['Country'] = self.country
        if self.esn_group_id is not None:
            result['EsnGroupId'] = self.esn_group_id
        if self.province is not None:
            result['Province'] = self.province
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerTime') is not None:
            self.server_time = m.get('ServerTime')
        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('DetectIp') is not None:
            self.detect_ip = m.get('DetectIp')
        if m.get('EsnAppId') is not None:
            self.esn_app_id = m.get('EsnAppId')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('IspId') is not None:
            self.isp_id = m.get('IspId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('EscapedTime') is not None:
            self.escaped_time = m.get('EscapedTime')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EsnGroupId') is not None:
            self.esn_group_id = m.get('EsnGroupId')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class DescribeRequestStatisticLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[DescribeRequestStatisticLogResponseBodyStatistic] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeRequestStatisticLogResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeRequestStatisticLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRequestStatisticLogResponseBody = None,
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
            temp_model = DescribeRequestStatisticLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSDKStatisticLogRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: int = None,
        end_time: int = None,
        page: int = None,
        page_size: int = None,
        esn_app: str = None,
        esn_biz: str = None,
        esn_group: str = None,
        source: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        isp: str = None,
        token: str = None,
        result: str = None,
        os_type: str = None,
        detect_ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.esn_app = esn_app
        self.esn_biz = esn_biz
        self.esn_group = esn_group
        self.source = source
        self.country = country
        self.province = province
        self.city = city
        self.isp = isp
        self.token = token
        self.result = result
        self.os_type = os_type
        self.detect_ip = detect_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.esn_app is not None:
            result['EsnApp'] = self.esn_app
        if self.esn_biz is not None:
            result['EsnBiz'] = self.esn_biz
        if self.esn_group is not None:
            result['EsnGroup'] = self.esn_group
        if self.source is not None:
            result['Source'] = self.source
        if self.country is not None:
            result['Country'] = self.country
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.token is not None:
            result['Token'] = self.token
        if self.result is not None:
            result['Result'] = self.result
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.detect_ip is not None:
            result['DetectIp'] = self.detect_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EsnApp') is not None:
            self.esn_app = m.get('EsnApp')
        if m.get('EsnBiz') is not None:
            self.esn_biz = m.get('EsnBiz')
        if m.get('EsnGroup') is not None:
            self.esn_group = m.get('EsnGroup')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('DetectIp') is not None:
            self.detect_ip = m.get('DetectIp')
        return self


class DescribeSDKStatisticLogResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        server_time: str = None,
        call_result: str = None,
        token: str = None,
        ping_result: str = None,
        user_id: str = None,
        country_id: str = None,
        city: str = None,
        connect_result: str = None,
        source_ip: str = None,
        province_id: str = None,
        detect_ip: str = None,
        trace_result: str = None,
        esn_app_id: str = None,
        mtype: str = None,
        isp_id: str = None,
        isp: str = None,
        city_id: str = None,
        os_type: str = None,
        verdict_code: str = None,
        sdk_version: str = None,
        country: str = None,
        esn_group_id: str = None,
        province: str = None,
        esn_biz_id: str = None,
    ):
        self.server_time = server_time
        self.call_result = call_result
        self.token = token
        self.ping_result = ping_result
        self.user_id = user_id
        self.country_id = country_id
        self.city = city
        self.connect_result = connect_result
        self.source_ip = source_ip
        self.province_id = province_id
        self.detect_ip = detect_ip
        self.trace_result = trace_result
        self.esn_app_id = esn_app_id
        self.mtype = mtype
        self.isp_id = isp_id
        self.isp = isp
        self.city_id = city_id
        self.os_type = os_type
        self.verdict_code = verdict_code
        self.sdk_version = sdk_version
        self.country = country
        self.esn_group_id = esn_group_id
        self.province = province
        self.esn_biz_id = esn_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.server_time is not None:
            result['ServerTime'] = self.server_time
        if self.call_result is not None:
            result['CallResult'] = self.call_result
        if self.token is not None:
            result['Token'] = self.token
        if self.ping_result is not None:
            result['PingResult'] = self.ping_result
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.city is not None:
            result['City'] = self.city
        if self.connect_result is not None:
            result['ConnectResult'] = self.connect_result
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        if self.detect_ip is not None:
            result['DetectIp'] = self.detect_ip
        if self.trace_result is not None:
            result['TraceResult'] = self.trace_result
        if self.esn_app_id is not None:
            result['EsnAppId'] = self.esn_app_id
        if self.mtype is not None:
            result['MType'] = self.mtype
        if self.isp_id is not None:
            result['IspId'] = self.isp_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.city_id is not None:
            result['CityId'] = self.city_id
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.verdict_code is not None:
            result['VerdictCode'] = self.verdict_code
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.country is not None:
            result['Country'] = self.country
        if self.esn_group_id is not None:
            result['EsnGroupId'] = self.esn_group_id
        if self.province is not None:
            result['Province'] = self.province
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerTime') is not None:
            self.server_time = m.get('ServerTime')
        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('PingResult') is not None:
            self.ping_result = m.get('PingResult')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ConnectResult') is not None:
            self.connect_result = m.get('ConnectResult')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        if m.get('DetectIp') is not None:
            self.detect_ip = m.get('DetectIp')
        if m.get('TraceResult') is not None:
            self.trace_result = m.get('TraceResult')
        if m.get('EsnAppId') is not None:
            self.esn_app_id = m.get('EsnAppId')
        if m.get('MType') is not None:
            self.mtype = m.get('MType')
        if m.get('IspId') is not None:
            self.isp_id = m.get('IspId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('VerdictCode') is not None:
            self.verdict_code = m.get('VerdictCode')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EsnGroupId') is not None:
            self.esn_group_id = m.get('EsnGroupId')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        return self


class DescribeSDKStatisticLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[DescribeSDKStatisticLogResponseBodyStatistic] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeSDKStatisticLogResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeSDKStatisticLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSDKStatisticLogResponseBody = None,
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
            temp_model = DescribeSDKStatisticLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSDKStatisticResultByEsnBizISP1M30MRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_app: str = None,
        esn_biz: str = None,
        time: int = None,
        page: int = None,
        page_size: int = None,
        type: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_app = esn_app
        self.esn_biz = esn_biz
        self.time = time
        self.page = page
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_app is not None:
            result['EsnApp'] = self.esn_app
        if self.esn_biz is not None:
            result['EsnBiz'] = self.esn_biz
        if self.time is not None:
            result['Time'] = self.time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnApp') is not None:
            self.esn_app = m.get('EsnApp')
        if m.get('EsnBiz') is not None:
            self.esn_biz = m.get('EsnBiz')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeSDKStatisticResultByEsnBizISP1M30MResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        time: int = None,
        result: str = None,
        isp_id: str = None,
        count: int = None,
    ):
        self.time = time
        self.result = result
        self.isp_id = isp_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.result is not None:
            result['Result'] = self.result
        if self.isp_id is not None:
            result['IspId'] = self.isp_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('IspId') is not None:
            self.isp_id = m.get('IspId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeSDKStatisticResultByEsnBizISP1M30MResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[DescribeSDKStatisticResultByEsnBizISP1M30MResponseBodyStatistic] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeSDKStatisticResultByEsnBizISP1M30MResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeSDKStatisticResultByEsnBizISP1M30MResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSDKStatisticResultByEsnBizISP1M30MResponseBody = None,
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
            temp_model = DescribeSDKStatisticResultByEsnBizISP1M30MResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSDKStatisticResultByEsnBizISPIntervalRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_app: str = None,
        esn_biz: str = None,
        start_time: int = None,
        end_time: int = None,
        page: int = None,
        page_size: int = None,
        type: str = None,
        interval: int = None,
        province: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_app = esn_app
        self.esn_biz = esn_biz
        self.start_time = start_time
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.type = type
        self.interval = interval
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_app is not None:
            result['EsnApp'] = self.esn_app
        if self.esn_biz is not None:
            result['EsnBiz'] = self.esn_biz
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnApp') is not None:
            self.esn_app = m.get('EsnApp')
        if m.get('EsnBiz') is not None:
            self.esn_biz = m.get('EsnBiz')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class DescribeSDKStatisticResultByEsnBizISPIntervalResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        index: int = None,
        time: int = None,
        result: str = None,
        isp_id: str = None,
        count: int = None,
    ):
        self.index = index
        self.time = time
        self.result = result
        self.isp_id = isp_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.time is not None:
            result['Time'] = self.time
        if self.result is not None:
            result['Result'] = self.result
        if self.isp_id is not None:
            result['IspId'] = self.isp_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('IspId') is not None:
            self.isp_id = m.get('IspId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeSDKStatisticResultByEsnBizISPIntervalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[DescribeSDKStatisticResultByEsnBizISPIntervalResponseBodyStatistic] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeSDKStatisticResultByEsnBizISPIntervalResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeSDKStatisticResultByEsnBizISPIntervalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSDKStatisticResultByEsnBizISPIntervalResponseBody = None,
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
            temp_model = DescribeSDKStatisticResultByEsnBizISPIntervalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSDKStatisticResultByEsnBizProvince1DayRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_app: str = None,
        esn_biz: str = None,
        start_time: int = None,
        end_time: int = None,
        page: int = None,
        page_size: int = None,
        type: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_app = esn_app
        self.esn_biz = esn_biz
        self.start_time = start_time
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_app is not None:
            result['EsnApp'] = self.esn_app
        if self.esn_biz is not None:
            result['EsnBiz'] = self.esn_biz
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnApp') is not None:
            self.esn_app = m.get('EsnApp')
        if m.get('EsnBiz') is not None:
            self.esn_biz = m.get('EsnBiz')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeSDKStatisticResultByEsnBizProvince1DayResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        result: str = None,
        province_id: str = None,
        count: int = None,
    ):
        self.result = result
        self.province_id = province_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeSDKStatisticResultByEsnBizProvince1DayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[DescribeSDKStatisticResultByEsnBizProvince1DayResponseBodyStatistic] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeSDKStatisticResultByEsnBizProvince1DayResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeSDKStatisticResultByEsnBizProvince1DayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSDKStatisticResultByEsnBizProvince1DayResponseBody = None,
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
            temp_model = DescribeSDKStatisticResultByEsnBizProvince1DayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSDKStatisticResultByEsnBizProvince30MRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_app: str = None,
        esn_biz: str = None,
        time: int = None,
        page: int = None,
        page_size: int = None,
        type: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_app = esn_app
        self.esn_biz = esn_biz
        self.time = time
        self.page = page
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_app is not None:
            result['EsnApp'] = self.esn_app
        if self.esn_biz is not None:
            result['EsnBiz'] = self.esn_biz
        if self.time is not None:
            result['Time'] = self.time
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnApp') is not None:
            self.esn_app = m.get('EsnApp')
        if m.get('EsnBiz') is not None:
            self.esn_biz = m.get('EsnBiz')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeSDKStatisticResultByEsnBizProvince30MResponseBodyStatistic(TeaModel):
    def __init__(
        self,
        result: str = None,
        province_id: str = None,
        count: int = None,
    ):
        self.result = result
        self.province_id = province_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeSDKStatisticResultByEsnBizProvince30MResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[DescribeSDKStatisticResultByEsnBizProvince30MResponseBodyStatistic] = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.statistic = statistic
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeSDKStatisticResultByEsnBizProvince30MResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeSDKStatisticResultByEsnBizProvince30MResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSDKStatisticResultByEsnBizProvince30MResponseBody = None,
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
            temp_model = DescribeSDKStatisticResultByEsnBizProvince30MResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSourceFailureTopIpRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_biz_id: str = None,
        start_time: int = None,
        end_time: int = None,
        limit: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_biz_id = esn_biz_id
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class DescribeSourceFailureTopIpResponseBodyTopIps(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
        total_count: int = None,
    ):
        self.ip = ip
        self.port = port
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSourceFailureTopIpResponseBody(TeaModel):
    def __init__(
        self,
        top_ips: List[DescribeSourceFailureTopIpResponseBodyTopIps] = None,
        request_id: str = None,
    ):
        self.top_ips = top_ips
        self.request_id = request_id

    def validate(self):
        if self.top_ips:
            for k in self.top_ips:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TopIps'] = []
        if self.top_ips is not None:
            for k in self.top_ips:
                result['TopIps'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.top_ips = []
        if m.get('TopIps') is not None:
            for k in m.get('TopIps'):
                temp_model = DescribeSourceFailureTopIpResponseBodyTopIps()
                self.top_ips.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSourceFailureTopIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSourceFailureTopIpResponseBody = None,
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
            temp_model = DescribeSourceFailureTopIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSourceFailureTrendGraphRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_biz_id: str = None,
        start_time: int = None,
        end_time: int = None,
        interval: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_biz_id = esn_biz_id
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeSourceFailureTrendGraphResponseBodyTrendGraph(TeaModel):
    def __init__(
        self,
        index: int = None,
        total_count: int = None,
    ):
        self.index = index
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSourceFailureTrendGraphResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trend_graph: List[DescribeSourceFailureTrendGraphResponseBodyTrendGraph] = None,
    ):
        self.request_id = request_id
        self.trend_graph = trend_graph

    def validate(self):
        if self.trend_graph:
            for k in self.trend_graph:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TrendGraph'] = []
        if self.trend_graph is not None:
            for k in self.trend_graph:
                result['TrendGraph'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.trend_graph = []
        if m.get('TrendGraph') is not None:
            for k in m.get('TrendGraph'):
                temp_model = DescribeSourceFailureTrendGraphResponseBodyTrendGraph()
                self.trend_graph.append(temp_model.from_map(k))
        return self


class DescribeSourceFailureTrendGraphResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSourceFailureTrendGraphResponseBody = None,
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
            temp_model = DescribeSourceFailureTrendGraphResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUploadPreSignRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeUploadPreSignResponseBody(TeaModel):
    def __init__(
        self,
        policy: str = None,
        request_id: str = None,
        access_id: str = None,
        signature: str = None,
        prompt_info: Dict[str, Any] = None,
        host: str = None,
        key: str = None,
    ):
        self.policy = policy
        self.request_id = request_id
        self.access_id = access_id
        self.signature = signature
        self.prompt_info = prompt_info
        self.host = host
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.host is not None:
            result['Host'] = self.host
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class DescribeUploadPreSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUploadPreSignResponseBody = None,
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
            temp_model = DescribeUploadPreSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserFlowInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeUserFlowInfoResponseBodyFlowInfo(TeaModel):
    def __init__(
        self,
        biz_band_width: int = None,
    ):
        self.biz_band_width = biz_band_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.biz_band_width is not None:
            result['BizBandWidth'] = self.biz_band_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizBandWidth') is not None:
            self.biz_band_width = m.get('BizBandWidth')
        return self


class DescribeUserFlowInfoResponseBody(TeaModel):
    def __init__(
        self,
        flow_info: DescribeUserFlowInfoResponseBodyFlowInfo = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.flow_info = flow_info
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.flow_info:
            self.flow_info.validate()

    def to_map(self):
        result = dict()
        if self.flow_info is not None:
            result['FlowInfo'] = self.flow_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowInfo') is not None:
            temp_model = DescribeUserFlowInfoResponseBodyFlowInfo()
            self.flow_info = temp_model.from_map(m['FlowInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DescribeUserFlowInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserFlowInfoResponseBody = None,
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
            temp_model = DescribeUserFlowInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserFlowReportRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        end_time: int = None,
        interval: int = None,
        start_time: int = None,
        esn_group_id: str = None,
        esn_biz_id: int = None,
        esn_app_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.end_time = end_time
        self.interval = interval
        self.start_time = start_time
        self.esn_group_id = esn_group_id
        self.esn_biz_id = esn_biz_id
        self.esn_app_id = esn_app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.esn_group_id is not None:
            result['EsnGroupId'] = self.esn_group_id
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.esn_app_id is not None:
            result['EsnAppId'] = self.esn_app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EsnGroupId') is not None:
            self.esn_group_id = m.get('EsnGroupId')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('EsnAppId') is not None:
            self.esn_app_id = m.get('EsnAppId')
        return self


class DescribeUserFlowReportResponseBodyFlowReport(TeaModel):
    def __init__(
        self,
        time: List[str] = None,
        max_inflow: List[str] = None,
        attack_flow: List[str] = None,
        max_out_flow: List[str] = None,
    ):
        self.time = time
        self.max_inflow = max_inflow
        self.attack_flow = attack_flow
        self.max_out_flow = max_out_flow

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.max_inflow is not None:
            result['MaxInflow'] = self.max_inflow
        if self.attack_flow is not None:
            result['AttackFlow'] = self.attack_flow
        if self.max_out_flow is not None:
            result['MaxOutFlow'] = self.max_out_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('MaxInflow') is not None:
            self.max_inflow = m.get('MaxInflow')
        if m.get('AttackFlow') is not None:
            self.attack_flow = m.get('AttackFlow')
        if m.get('MaxOutFlow') is not None:
            self.max_out_flow = m.get('MaxOutFlow')
        return self


class DescribeUserFlowReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        flow_report: DescribeUserFlowReportResponseBodyFlowReport = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.flow_report = flow_report

    def validate(self):
        if self.flow_report:
            self.flow_report.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.flow_report is not None:
            result['FlowReport'] = self.flow_report.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('FlowReport') is not None:
            temp_model = DescribeUserFlowReportResponseBodyFlowReport()
            self.flow_report = temp_model.from_map(m['FlowReport'])
        return self


class DescribeUserFlowReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserFlowReportResponseBody = None,
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
            temp_model = DescribeUserFlowReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserTotalFlowReportRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        end_time: int = None,
        interval: int = None,
        start_time: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.end_time = end_time
        self.interval = interval
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeUserTotalFlowReportResponseBodyFlowReport(TeaModel):
    def __init__(
        self,
        time: List[str] = None,
        max_inflow: List[str] = None,
        attack_flow: List[str] = None,
        max_out_flow: List[str] = None,
    ):
        self.time = time
        self.max_inflow = max_inflow
        self.attack_flow = attack_flow
        self.max_out_flow = max_out_flow

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.max_inflow is not None:
            result['MaxInflow'] = self.max_inflow
        if self.attack_flow is not None:
            result['AttackFlow'] = self.attack_flow
        if self.max_out_flow is not None:
            result['MaxOutFlow'] = self.max_out_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('MaxInflow') is not None:
            self.max_inflow = m.get('MaxInflow')
        if m.get('AttackFlow') is not None:
            self.attack_flow = m.get('AttackFlow')
        if m.get('MaxOutFlow') is not None:
            self.max_out_flow = m.get('MaxOutFlow')
        return self


class DescribeUserTotalFlowReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        flow_report: DescribeUserTotalFlowReportResponseBodyFlowReport = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.flow_report = flow_report

    def validate(self):
        if self.flow_report:
            self.flow_report.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.flow_report is not None:
            result['FlowReport'] = self.flow_report.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('FlowReport') is not None:
            temp_model = DescribeUserTotalFlowReportResponseBodyFlowReport()
            self.flow_report = temp_model.from_map(m['FlowReport'])
        return self


class DescribeUserTotalFlowReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserTotalFlowReportResponseBody = None,
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
            temp_model = DescribeUserTotalFlowReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadAppKeyFileRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
        platform: str = None,
        key_version: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id
        self.platform = platform
        self.key_version = key_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.key_version is not None:
            result['KeyVersion'] = self.key_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('KeyVersion') is not None:
            self.key_version = m.get('KeyVersion')
        return self


class DownloadAppKeyFileResponseBodyDownloadLinkResult(TeaModel):
    def __init__(
        self,
        download_link: str = None,
    ):
        self.download_link = download_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        return self


class DownloadAppKeyFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
        download_link_result: DownloadAppKeyFileResponseBodyDownloadLinkResult = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info
        self.download_link_result = download_link_result

    def validate(self):
        if self.download_link_result:
            self.download_link_result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        if self.download_link_result is not None:
            result['DownloadLinkResult'] = self.download_link_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        if m.get('DownloadLinkResult') is not None:
            temp_model = DownloadAppKeyFileResponseBodyDownloadLinkResult()
            self.download_link_result = temp_model.from_map(m['DownloadLinkResult'])
        return self


class DownloadAppKeyFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DownloadAppKeyFileResponseBody = None,
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
            temp_model = DownloadAppKeyFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadCcRouteRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DownloadCcRouteRulesResponseBodyDownloadFileResult(TeaModel):
    def __init__(
        self,
        download_link: str = None,
    ):
        self.download_link = download_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        return self


class DownloadCcRouteRulesResponseBody(TeaModel):
    def __init__(
        self,
        download_file_result: DownloadCcRouteRulesResponseBodyDownloadFileResult = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.download_file_result = download_file_result
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.download_file_result:
            self.download_file_result.validate()

    def to_map(self):
        result = dict()
        if self.download_file_result is not None:
            result['DownloadFileResult'] = self.download_file_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadFileResult') is not None:
            temp_model = DownloadCcRouteRulesResponseBodyDownloadFileResult()
            self.download_file_result = temp_model.from_map(m['DownloadFileResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DownloadCcRouteRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DownloadCcRouteRulesResponseBody = None,
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
            temp_model = DownloadCcRouteRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadFlexAccRulesFileRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DownloadFlexAccRulesFileResponseBodyDownloadFileResult(TeaModel):
    def __init__(
        self,
        download_link: str = None,
    ):
        self.download_link = download_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        return self


class DownloadFlexAccRulesFileResponseBody(TeaModel):
    def __init__(
        self,
        download_file_result: DownloadFlexAccRulesFileResponseBodyDownloadFileResult = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.download_file_result = download_file_result
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.download_file_result:
            self.download_file_result.validate()

    def to_map(self):
        result = dict()
        if self.download_file_result is not None:
            result['DownloadFileResult'] = self.download_file_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadFileResult') is not None:
            temp_model = DownloadFlexAccRulesFileResponseBodyDownloadFileResult()
            self.download_file_result = temp_model.from_map(m['DownloadFileResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DownloadFlexAccRulesFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DownloadFlexAccRulesFileResponseBody = None,
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
            temp_model = DownloadFlexAccRulesFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadLayer4RulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DownloadLayer4RulesResponseBodyDownloadFileResult(TeaModel):
    def __init__(
        self,
        download_link: str = None,
    ):
        self.download_link = download_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        return self


class DownloadLayer4RulesResponseBody(TeaModel):
    def __init__(
        self,
        download_file_result: DownloadLayer4RulesResponseBodyDownloadFileResult = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.download_file_result = download_file_result
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.download_file_result:
            self.download_file_result.validate()

    def to_map(self):
        result = dict()
        if self.download_file_result is not None:
            result['DownloadFileResult'] = self.download_file_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadFileResult') is not None:
            temp_model = DownloadLayer4RulesResponseBodyDownloadFileResult()
            self.download_file_result = temp_model.from_map(m['DownloadFileResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DownloadLayer4RulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DownloadLayer4RulesResponseBody = None,
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
            temp_model = DownloadLayer4RulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadSdkFileRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_id: int = None,
        sdk_version: str = None,
        platform: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_id = app_id
        self.sdk_version = sdk_version
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class DownloadSdkFileResponseBodyDownloadFileResult(TeaModel):
    def __init__(
        self,
        download_link: str = None,
    ):
        self.download_link = download_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        return self


class DownloadSdkFileResponseBody(TeaModel):
    def __init__(
        self,
        download_file_result: DownloadSdkFileResponseBodyDownloadFileResult = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.download_file_result = download_file_result
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.download_file_result:
            self.download_file_result.validate()

    def to_map(self):
        result = dict()
        if self.download_file_result is not None:
            result['DownloadFileResult'] = self.download_file_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadFileResult') is not None:
            temp_model = DownloadSdkFileResponseBodyDownloadFileResult()
            self.download_file_result = temp_model.from_map(m['DownloadFileResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DownloadSdkFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DownloadSdkFileResponseBody = None,
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
            temp_model = DownloadSdkFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadUserTotalFlowReportRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: int = None,
        end_time: int = None,
        interval: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DownloadUserTotalFlowReportResponseBodyDownloadFileResult(TeaModel):
    def __init__(
        self,
        download_link: str = None,
    ):
        self.download_link = download_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        return self


class DownloadUserTotalFlowReportResponseBody(TeaModel):
    def __init__(
        self,
        download_file_result: DownloadUserTotalFlowReportResponseBodyDownloadFileResult = None,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.download_file_result = download_file_result
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        if self.download_file_result:
            self.download_file_result.validate()

    def to_map(self):
        result = dict()
        if self.download_file_result is not None:
            result['DownloadFileResult'] = self.download_file_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadFileResult') is not None:
            temp_model = DownloadUserTotalFlowReportResponseBodyDownloadFileResult()
            self.download_file_result = temp_model.from_map(m['DownloadFileResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class DownloadUserTotalFlowReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DownloadUserTotalFlowReportResponseBody = None,
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
            temp_model = DownloadUserTotalFlowReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlushLayer4RulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class FlushLayer4RulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class FlushLayer4RulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FlushLayer4RulesResponseBody = None,
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
            temp_model = FlushLayer4RulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReallocNgResourceRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: str = None,
        cc_qps: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.cc_qps = cc_qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.cc_qps is not None:
            result['CcQps'] = self.cc_qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CcQps') is not None:
            self.cc_qps = m.get('CcQps')
        return self


class ReallocNgResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class ReallocNgResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReallocNgResourceResponseBody = None,
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
            temp_model = ReallocNgResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceCcRouteRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        route_list: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.route_list = route_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.route_list is not None:
            result['RouteList'] = self.route_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('RouteList') is not None:
            self.route_list = m.get('RouteList')
        return self


class ReplaceCcRouteRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class ReplaceCcRouteRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReplaceCcRouteRulesResponseBody = None,
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
            temp_model = ReplaceCcRouteRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchFlexFwdRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_biz_id: int = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_biz_id = esn_biz_id
        self.keyword = keyword
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class SearchFlexFwdRulesResponseBodyFlexFwdRules(TeaModel):
    def __init__(
        self,
        master_ip_list: str = None,
        remark: str = None,
        slave_ip_list: str = None,
        protocol: str = None,
        identity: str = None,
    ):
        self.master_ip_list = master_ip_list
        self.remark = remark
        self.slave_ip_list = slave_ip_list
        self.protocol = protocol
        self.identity = identity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.master_ip_list is not None:
            result['MasterIpList'] = self.master_ip_list
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.slave_ip_list is not None:
            result['SlaveIpList'] = self.slave_ip_list
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.identity is not None:
            result['Identity'] = self.identity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterIpList') is not None:
            self.master_ip_list = m.get('MasterIpList')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SlaveIpList') is not None:
            self.slave_ip_list = m.get('SlaveIpList')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        return self


class SearchFlexFwdRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
        flex_fwd_rules: List[SearchFlexFwdRulesResponseBodyFlexFwdRules] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info
        self.flex_fwd_rules = flex_fwd_rules

    def validate(self):
        if self.flex_fwd_rules:
            for k in self.flex_fwd_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        result['FlexFwdRules'] = []
        if self.flex_fwd_rules is not None:
            for k in self.flex_fwd_rules:
                result['FlexFwdRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        self.flex_fwd_rules = []
        if m.get('FlexFwdRules') is not None:
            for k in m.get('FlexFwdRules'):
                temp_model = SearchFlexFwdRulesResponseBodyFlexFwdRules()
                self.flex_fwd_rules.append(temp_model.from_map(k))
        return self


class SearchFlexFwdRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchFlexFwdRulesResponseBody = None,
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
            temp_model = SearchFlexFwdRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_name: str = None,
        app_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_name = app_name
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class UpdateAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppResponseBody = None,
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
            temp_model = UpdateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCcBlackListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        ips: str = None,
        action_type: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.ips = ips
        self.action_type = action_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        return self


class UpdateCcBlackListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateCcBlackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCcBlackListResponseBody = None,
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
            temp_model = UpdateCcBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCcIDCBlockSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        enable: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class UpdateCcIDCBlockSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateCcIDCBlockSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCcIDCBlockSwitchResponseBody = None,
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
            temp_model = UpdateCcIDCBlockSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCcRouteRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        routelist: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.routelist = routelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.routelist is not None:
            result['Routelist'] = self.routelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Routelist') is not None:
            self.routelist = m.get('Routelist')
        return self


class UpdateCcRouteRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateCcRouteRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCcRouteRulesResponseBody = None,
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
            temp_model = UpdateCcRouteRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCcRouteSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        enable: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class UpdateCcRouteSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateCcRouteSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCcRouteSwitchResponseBody = None,
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
            temp_model = UpdateCcRouteSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCcTunnelGrayAndOnlyAllowRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: str = None,
        only_allow: int = None,
        gray: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.only_allow = only_allow
        self.gray = gray

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.only_allow is not None:
            result['OnlyAllow'] = self.only_allow
        if self.gray is not None:
            result['Gray'] = self.gray
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('OnlyAllow') is not None:
            self.only_allow = m.get('OnlyAllow')
        if m.get('Gray') is not None:
            self.gray = m.get('Gray')
        return self


class UpdateCcTunnelGrayAndOnlyAllowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateCcTunnelGrayAndOnlyAllowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCcTunnelGrayAndOnlyAllowResponseBody = None,
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
            temp_model = UpdateCcTunnelGrayAndOnlyAllowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCcTunnelStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: str = None,
        status: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateCcTunnelStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateCcTunnelStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCcTunnelStatusResponseBody = None,
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
            temp_model = UpdateCcTunnelStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCcUseRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        action_type: str = None,
        cc_qps: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.action_type = action_type
        self.cc_qps = cc_qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.cc_qps is not None:
            result['CcQps'] = self.cc_qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('CcQps') is not None:
            self.cc_qps = m.get('CcQps')
        return self


class UpdateCcUseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateCcUseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCcUseResponseBody = None,
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
            temp_model = UpdateCcUseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCcWhiteListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        ips: str = None,
        action_type: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.ips = ips
        self.action_type = action_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        return self


class UpdateCcWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateCcWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCcWhiteListResponseBody = None,
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
            temp_model = UpdateCcWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCcZoneBlockConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        config: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class UpdateCcZoneBlockConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateCcZoneBlockConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCcZoneBlockConfigResponseBody = None,
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
            temp_model = UpdateCcZoneBlockConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCcZoneBlockStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        enable: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class UpdateCcZoneBlockStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateCcZoneBlockStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCcZoneBlockStatusResponseBody = None,
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
            temp_model = UpdateCcZoneBlockStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlexAccFwdRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        esn_biz_id: int = None,
        identity: str = None,
        protocol_ex: str = None,
        ip_list: str = None,
        domain_list: str = None,
        remark: str = None,
    ):
        self.source_ip = source_ip
        self.esn_biz_id = esn_biz_id
        self.identity = identity
        self.protocol_ex = protocol_ex
        self.ip_list = ip_list
        self.domain_list = domain_list
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.protocol_ex is not None:
            result['ProtocolEx'] = self.protocol_ex
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('ProtocolEx') is not None:
            self.protocol_ex = m.get('ProtocolEx')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateFlexAccFwdRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateFlexAccFwdRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFlexAccFwdRuleResponseBody = None,
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
            temp_model = UpdateFlexAccFwdRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlexAccFwdRuleV2Request(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        biz_id: int = None,
        identity: str = None,
        ip_list: str = None,
        protocol_ex: str = None,
        domain_list: str = None,
        remark: str = None,
        master_ip_list: str = None,
        slave_ip_list: str = None,
        acc_type: int = None,
    ):
        self.source_ip = source_ip
        self.biz_id = biz_id
        self.identity = identity
        self.ip_list = ip_list
        self.protocol_ex = protocol_ex
        self.domain_list = domain_list
        self.remark = remark
        self.master_ip_list = master_ip_list
        self.slave_ip_list = slave_ip_list
        self.acc_type = acc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.protocol_ex is not None:
            result['ProtocolEx'] = self.protocol_ex
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.master_ip_list is not None:
            result['MasterIpList'] = self.master_ip_list
        if self.slave_ip_list is not None:
            result['SlaveIpList'] = self.slave_ip_list
        if self.acc_type is not None:
            result['AccType'] = self.acc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('ProtocolEx') is not None:
            self.protocol_ex = m.get('ProtocolEx')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('MasterIpList') is not None:
            self.master_ip_list = m.get('MasterIpList')
        if m.get('SlaveIpList') is not None:
            self.slave_ip_list = m.get('SlaveIpList')
        if m.get('AccType') is not None:
            self.acc_type = m.get('AccType')
        return self


class UpdateFlexAccFwdRuleV2ResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateFlexAccFwdRuleV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFlexAccFwdRuleV2ResponseBody = None,
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
            temp_model = UpdateFlexAccFwdRuleV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlexAccStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        biz_id: int = None,
        status: str = None,
    ):
        self.source_ip = source_ip
        self.biz_id = biz_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateFlexAccStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateFlexAccStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFlexAccStatusResponseBody = None,
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
            temp_model = UpdateFlexAccStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlexAccTcpPortsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        esn_biz_id: int = None,
        ports: str = None,
    ):
        self.source_ip = source_ip
        self.esn_biz_id = esn_biz_id
        self.ports = ports

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.ports is not None:
            result['Ports'] = self.ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        return self


class UpdateFlexAccTcpPortsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateFlexAccTcpPortsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFlexAccTcpPortsResponseBody = None,
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
            temp_model = UpdateFlexAccTcpPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlexAccUdpPortsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        esn_biz_id: int = None,
        ports: str = None,
    ):
        self.source_ip = source_ip
        self.esn_biz_id = esn_biz_id
        self.ports = ports

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.ports is not None:
            result['Ports'] = self.ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        return self


class UpdateFlexAccUdpPortsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateFlexAccUdpPortsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFlexAccUdpPortsResponseBody = None,
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
            temp_model = UpdateFlexAccUdpPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlexBackupGroupsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_biz_id: int = None,
        group_id: str = None,
        backup_group_policy: int = None,
        backups: str = None,
        shared_backups: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_biz_id = esn_biz_id
        self.group_id = group_id
        self.backup_group_policy = backup_group_policy
        self.backups = backups
        self.shared_backups = shared_backups

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.backup_group_policy is not None:
            result['BackupGroupPolicy'] = self.backup_group_policy
        if self.backups is not None:
            result['Backups'] = self.backups
        if self.shared_backups is not None:
            result['SharedBackups'] = self.shared_backups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('BackupGroupPolicy') is not None:
            self.backup_group_policy = m.get('BackupGroupPolicy')
        if m.get('Backups') is not None:
            self.backups = m.get('Backups')
        if m.get('SharedBackups') is not None:
            self.shared_backups = m.get('SharedBackups')
        return self


class UpdateFlexBackupGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateFlexBackupGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFlexBackupGroupsResponseBody = None,
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
            temp_model = UpdateFlexBackupGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlexFwdRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        identity: str = None,
        master_ip_list: str = None,
        slave_ip_list: str = None,
        remark: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.identity = identity
        self.master_ip_list = master_ip_list
        self.slave_ip_list = slave_ip_list
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.master_ip_list is not None:
            result['MasterIpList'] = self.master_ip_list
        if self.slave_ip_list is not None:
            result['SlaveIpList'] = self.slave_ip_list
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('MasterIpList') is not None:
            self.master_ip_list = m.get('MasterIpList')
        if m.get('SlaveIpList') is not None:
            self.slave_ip_list = m.get('SlaveIpList')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateFlexFwdRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateFlexFwdRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFlexFwdRuleResponseBody = None,
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
            temp_model = UpdateFlexFwdRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlexInnerPolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_biz_id: int = None,
        group_id: str = None,
        group_inner_policy: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_biz_id = esn_biz_id
        self.group_id = group_id
        self.group_inner_policy = group_inner_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_inner_policy is not None:
            result['GroupInnerPolicy'] = self.group_inner_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupInnerPolicy') is not None:
            self.group_inner_policy = m.get('GroupInnerPolicy')
        return self


class UpdateFlexInnerPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateFlexInnerPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFlexInnerPolicyResponseBody = None,
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
            temp_model = UpdateFlexInnerPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlexLinkTypeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_biz_id: int = None,
        link_type: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_biz_id = esn_biz_id
        self.link_type = link_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.link_type is not None:
            result['LinkType'] = self.link_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('LinkType') is not None:
            self.link_type = m.get('LinkType')
        return self


class UpdateFlexLinkTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateFlexLinkTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFlexLinkTypeResponseBody = None,
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
            temp_model = UpdateFlexLinkTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlexPortsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        esn_biz_id: int = None,
        ports: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.esn_biz_id = esn_biz_id
        self.ports = ports

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.esn_biz_id is not None:
            result['EsnBizId'] = self.esn_biz_id
        if self.ports is not None:
            result['Ports'] = self.ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('EsnBizId') is not None:
            self.esn_biz_id = m.get('EsnBizId')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        return self


class UpdateFlexPortsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateFlexPortsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFlexPortsResponseBody = None,
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
            temp_model = UpdateFlexPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlexStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        status: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateFlexStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateFlexStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFlexStatusResponseBody = None,
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
            temp_model = UpdateFlexStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        group_id: str = None,
        group_desc: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.group_id = group_id
        self.group_desc = group_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_desc is not None:
            result['GroupDesc'] = self.group_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupDesc') is not None:
            self.group_desc = m.get('GroupDesc')
        return self


class UpdateGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupResponseBody = None,
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
            temp_model = UpdateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupDnsStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        group_id: str = None,
        status: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.group_id = group_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateGroupDnsStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateGroupDnsStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupDnsStatusResponseBody = None,
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
            temp_model = UpdateGroupDnsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupNodesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        group_id: str = None,
        ip_list: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.group_id = group_id
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class UpdateGroupNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateGroupNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupNodesResponseBody = None,
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
            temp_model = UpdateGroupNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        group_id: str = None,
        status: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.group_id = group_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateGroupStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateGroupStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupStatusResponseBody = None,
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
            temp_model = UpdateGroupStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLayer4RuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        front_port: int = None,
        rservers: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.front_port = front_port
        self.rservers = rservers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.front_port is not None:
            result['FrontPort'] = self.front_port
        if self.rservers is not None:
            result['Rservers'] = self.rservers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')
        if m.get('Rservers') is not None:
            self.rservers = m.get('Rservers')
        return self


class UpdateLayer4RuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UpdateLayer4RuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLayer4RuleResponseBody = None,
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
            temp_model = UpdateLayer4RuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadCcRouteFileForParseRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        file_key: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.file_key = file_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        return self


class UploadCcRouteFileForParseResponseBodyRouteRules(TeaModel):
    def __init__(
        self,
        comment: str = None,
        rservers: List[str] = None,
        id: str = None,
    ):
        self.comment = comment
        self.rservers = rservers
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.rservers is not None:
            result['Rservers'] = self.rservers
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Rservers') is not None:
            self.rservers = m.get('Rservers')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UploadCcRouteFileForParseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
        route_rules: List[UploadCcRouteFileForParseResponseBodyRouteRules] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info
        self.route_rules = route_rules

    def validate(self):
        if self.route_rules:
            for k in self.route_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        result['RouteRules'] = []
        if self.route_rules is not None:
            for k in self.route_rules:
                result['RouteRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        self.route_rules = []
        if m.get('RouteRules') is not None:
            for k in m.get('RouteRules'):
                temp_model = UploadCcRouteFileForParseResponseBodyRouteRules()
                self.route_rules.append(temp_model.from_map(k))
        return self


class UploadCcRouteFileForParseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadCcRouteFileForParseResponseBody = None,
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
            temp_model = UploadCcRouteFileForParseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadCcWhiteBlackListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_id: int = None,
        bwlist: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_id = biz_id
        self.bwlist = bwlist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.bwlist is not None:
            result['BWList'] = self.bwlist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BWList') is not None:
            self.bwlist = m.get('BWList')
        return self


class UploadCcWhiteBlackListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.prompt_info = prompt_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UploadCcWhiteBlackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadCcWhiteBlackListResponseBody = None,
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
            temp_model = UploadCcWhiteBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadFlexAccRulesFileForParseRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        file_key: str = None,
    ):
        self.source_ip = source_ip
        self.file_key = file_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        return self


class UploadFlexAccRulesFileForParseResponseBodyFlexAccFwdRules(TeaModel):
    def __init__(
        self,
        master_ip_list: str = None,
        remark: str = None,
        slave_ip_list: str = None,
        identity: str = None,
        protocol: str = None,
        acc_type: int = None,
        ip_list: str = None,
        domain_list: str = None,
    ):
        self.master_ip_list = master_ip_list
        self.remark = remark
        self.slave_ip_list = slave_ip_list
        self.identity = identity
        self.protocol = protocol
        self.acc_type = acc_type
        self.ip_list = ip_list
        self.domain_list = domain_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.master_ip_list is not None:
            result['MasterIpList'] = self.master_ip_list
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.slave_ip_list is not None:
            result['SlaveIpList'] = self.slave_ip_list
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.acc_type is not None:
            result['AccType'] = self.acc_type
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterIpList') is not None:
            self.master_ip_list = m.get('MasterIpList')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SlaveIpList') is not None:
            self.slave_ip_list = m.get('SlaveIpList')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('AccType') is not None:
            self.acc_type = m.get('AccType')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        return self


class UploadFlexAccRulesFileForParseResponseBody(TeaModel):
    def __init__(
        self,
        flex_acc_fwd_rules: List[UploadFlexAccRulesFileForParseResponseBodyFlexAccFwdRules] = None,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
    ):
        self.flex_acc_fwd_rules = flex_acc_fwd_rules
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info

    def validate(self):
        if self.flex_acc_fwd_rules:
            for k in self.flex_acc_fwd_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FlexAccFwdRules'] = []
        if self.flex_acc_fwd_rules is not None:
            for k in self.flex_acc_fwd_rules:
                result['FlexAccFwdRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flex_acc_fwd_rules = []
        if m.get('FlexAccFwdRules') is not None:
            for k in m.get('FlexAccFwdRules'):
                temp_model = UploadFlexAccRulesFileForParseResponseBodyFlexAccFwdRules()
                self.flex_acc_fwd_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        return self


class UploadFlexAccRulesFileForParseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadFlexAccRulesFileForParseResponseBody = None,
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
            temp_model = UploadFlexAccRulesFileForParseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadFlexRulesFileForParseRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        file_key: str = None,
    ):
        self.source_ip = source_ip
        self.file_key = file_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        return self


class UploadFlexRulesFileForParseResponseBodyFlexFwdRules(TeaModel):
    def __init__(
        self,
        master_ip_list: str = None,
        remark: str = None,
        slave_ip_list: str = None,
        protocol: str = None,
        identity: str = None,
    ):
        self.master_ip_list = master_ip_list
        self.remark = remark
        self.slave_ip_list = slave_ip_list
        self.protocol = protocol
        self.identity = identity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.master_ip_list is not None:
            result['MasterIpList'] = self.master_ip_list
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.slave_ip_list is not None:
            result['SlaveIpList'] = self.slave_ip_list
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.identity is not None:
            result['Identity'] = self.identity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterIpList') is not None:
            self.master_ip_list = m.get('MasterIpList')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SlaveIpList') is not None:
            self.slave_ip_list = m.get('SlaveIpList')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        return self


class UploadFlexRulesFileForParseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        flex_fwd_rules: List[UploadFlexRulesFileForParseResponseBodyFlexFwdRules] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.flex_fwd_rules = flex_fwd_rules

    def validate(self):
        if self.flex_fwd_rules:
            for k in self.flex_fwd_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['FlexFwdRules'] = []
        if self.flex_fwd_rules is not None:
            for k in self.flex_fwd_rules:
                result['FlexFwdRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.flex_fwd_rules = []
        if m.get('FlexFwdRules') is not None:
            for k in m.get('FlexFwdRules'):
                temp_model = UploadFlexRulesFileForParseResponseBodyFlexFwdRules()
                self.flex_fwd_rules.append(temp_model.from_map(k))
        return self


class UploadFlexRulesFileForParseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadFlexRulesFileForParseResponseBody = None,
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
            temp_model = UploadFlexRulesFileForParseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadL4RulesFileForParseRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        file_key: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.file_key = file_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        return self


class UploadL4RulesFileForParseResponseBodyL4RuleList(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        app_id: int = None,
        back_port: int = None,
        biz_id: int = None,
        rservers: List[str] = None,
        lvs_policy: str = None,
        front_port: int = None,
        rule_id: str = None,
    ):
        self.protocol = protocol
        self.app_id = app_id
        self.back_port = back_port
        self.biz_id = biz_id
        self.rservers = rservers
        self.lvs_policy = lvs_policy
        self.front_port = front_port
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.back_port is not None:
            result['BackPort'] = self.back_port
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.rservers is not None:
            result['Rservers'] = self.rservers
        if self.lvs_policy is not None:
            result['LvsPolicy'] = self.lvs_policy
        if self.front_port is not None:
            result['FrontPort'] = self.front_port
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BackPort') is not None:
            self.back_port = m.get('BackPort')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Rservers') is not None:
            self.rservers = m.get('Rservers')
        if m.get('LvsPolicy') is not None:
            self.lvs_policy = m.get('LvsPolicy')
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class UploadL4RulesFileForParseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        prompt_info: Dict[str, Any] = None,
        l_4rule_list: List[UploadL4RulesFileForParseResponseBodyL4RuleList] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.prompt_info = prompt_info
        self.l_4rule_list = l_4rule_list

    def validate(self):
        if self.l_4rule_list:
            for k in self.l_4rule_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.prompt_info is not None:
            result['PromptInfo'] = self.prompt_info
        result['L4RuleList'] = []
        if self.l_4rule_list is not None:
            for k in self.l_4rule_list:
                result['L4RuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PromptInfo') is not None:
            self.prompt_info = m.get('PromptInfo')
        self.l_4rule_list = []
        if m.get('L4RuleList') is not None:
            for k in m.get('L4RuleList'):
                temp_model = UploadL4RulesFileForParseResponseBodyL4RuleList()
                self.l_4rule_list.append(temp_model.from_map(k))
        return self


class UploadL4RulesFileForParseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadL4RulesFileForParseResponseBody = None,
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
            temp_model = UploadL4RulesFileForParseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


