# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        client_token: str = None,
        duration: int = None,
        pricing_cycle: str = None,
        version_code: int = None,
        vm_number: int = None,
        is_auto_renew: bool = None,
        auto_renew_duration: int = None,
    ):
        self.owner_id = owner_id
        self.client_token = client_token
        self.duration = duration
        self.pricing_cycle = pricing_cycle
        self.version_code = version_code
        self.vm_number = vm_number
        self.is_auto_renew = is_auto_renew
        self.auto_renew_duration = auto_renew_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.vm_number is not None:
            result['VmNumber'] = self.vm_number
        if self.is_auto_renew is not None:
            result['IsAutoRenew'] = self.is_auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VmNumber') is not None:
            self.vm_number = m.get('VmNumber')
        if m.get('IsAutoRenew') is not None:
            self.is_auto_renew = m.get('IsAutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
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
        result = dict()
        if self.headers is not None:
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


class DeleteRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteRuleResponseBody(TeaModel):
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
        result = dict()
        if self.headers is not None:
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


class DescribeAutoDelConfigRequest(TeaModel):
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


class DescribeAutoDelConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        days: int = None,
    ):
        self.request_id = request_id
        self.days = days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.days is not None:
            result['Days'] = self.days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        return self


class DescribeAutoDelConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAutoDelConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAutoDelConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCheckWarningDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        check_warning_id: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.check_warning_id = check_warning_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.check_warning_id is not None:
            result['CheckWarningId'] = self.check_warning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('CheckWarningId') is not None:
            self.check_warning_id = m.get('CheckWarningId')
        return self


class DescribeCheckWarningDetailResponseBody(TeaModel):
    def __init__(
        self,
        item: str = None,
        type: str = None,
        description: str = None,
        request_id: str = None,
        check_id: int = None,
        level: str = None,
        prompt: str = None,
        advice: str = None,
    ):
        self.item = item
        self.type = type
        self.description = description
        self.request_id = request_id
        self.check_id = check_id
        self.level = level
        self.prompt = prompt
        self.advice = advice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.item is not None:
            result['Item'] = self.item
        if self.type is not None:
            result['Type'] = self.type
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.level is not None:
            result['Level'] = self.level
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.advice is not None:
            result['Advice'] = self.advice
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        return self


class DescribeCheckWarningDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCheckWarningDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCheckWarningDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConcernNecessityRequest(TeaModel):
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


class DescribeConcernNecessityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        concern_necessity: List[str] = None,
    ):
        self.request_id = request_id
        self.concern_necessity = concern_necessity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.concern_necessity is not None:
            result['ConcernNecessity'] = self.concern_necessity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConcernNecessity') is not None:
            self.concern_necessity = m.get('ConcernNecessity')
        return self


class DescribeConcernNecessityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConcernNecessityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeConcernNecessityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStatisticsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        uuid: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeInstanceStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        account: int = None,
        uuid: str = None,
        vul: int = None,
        health: int = None,
        trojan: int = None,
        suspicious: int = None,
    ):
        self.account = account
        self.uuid = uuid
        self.vul = vul
        self.health = health
        self.trojan = trojan
        self.suspicious = suspicious

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.vul is not None:
            result['Vul'] = self.vul
        if self.health is not None:
            result['Health'] = self.health
        if self.trojan is not None:
            result['Trojan'] = self.trojan
        if self.suspicious is not None:
            result['Suspicious'] = self.suspicious
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Vul') is not None:
            self.vul = m.get('Vul')
        if m.get('Health') is not None:
            self.health = m.get('Health')
        if m.get('Trojan') is not None:
            self.trojan = m.get('Trojan')
        if m.get('Suspicious') is not None:
            self.suspicious = m.get('Suspicious')
        return self


class DescribeInstanceStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[DescribeInstanceStatisticsResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeInstanceStatisticsResponseBodyData()
                self.data.append(temp_model.from_map(k))
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


class DescribeStrategyExecDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        strategy_id: int = None,
    ):
        self.source_ip = source_ip
        self.strategy_id = strategy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        return self


class DescribeStrategyExecDetailResponseBodyFailedEcsList(TeaModel):
    def __init__(
        self,
        internet_ip: str = None,
        instance_name: str = None,
        ip: str = None,
        intranet_ip: str = None,
        reason: str = None,
    ):
        self.internet_ip = internet_ip
        self.instance_name = instance_name
        self.ip = ip
        self.intranet_ip = intranet_ip
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class DescribeStrategyExecDetailResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        percent: str = None,
        fail_count: int = None,
        start_time: str = None,
        success_count: int = None,
        source: str = None,
        failed_ecs_list: List[DescribeStrategyExecDetailResponseBodyFailedEcsList] = None,
        in_process_count: int = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.percent = percent
        self.fail_count = fail_count
        self.start_time = start_time
        self.success_count = success_count
        self.source = source
        self.failed_ecs_list = failed_ecs_list
        self.in_process_count = in_process_count

    def validate(self):
        if self.failed_ecs_list:
            for k in self.failed_ecs_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.source is not None:
            result['Source'] = self.source
        result['FailedEcsList'] = []
        if self.failed_ecs_list is not None:
            for k in self.failed_ecs_list:
                result['FailedEcsList'].append(k.to_map() if k else None)
        if self.in_process_count is not None:
            result['InProcessCount'] = self.in_process_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        self.failed_ecs_list = []
        if m.get('FailedEcsList') is not None:
            for k in m.get('FailedEcsList'):
                temp_model = DescribeStrategyExecDetailResponseBodyFailedEcsList()
                self.failed_ecs_list.append(temp_model.from_map(k))
        if m.get('InProcessCount') is not None:
            self.in_process_count = m.get('InProcessCount')
        return self


class DescribeStrategyExecDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStrategyExecDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeStrategyExecDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStratetyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        strategy_ids: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.strategy_ids = strategy_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.strategy_ids is not None:
            result['StrategyIds'] = self.strategy_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StrategyIds') is not None:
            self.strategy_ids = m.get('StrategyIds')
        return self


class DescribeStratetyResponseBodyStrategiesConfigTargets(TeaModel):
    def __init__(
        self,
        flag: str = None,
        target: str = None,
        target_type: str = None,
    ):
        self.flag = flag
        self.target = target
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class DescribeStratetyResponseBodyStrategies(TeaModel):
    def __init__(
        self,
        exec_status: int = None,
        type: int = None,
        config_targets: List[DescribeStratetyResponseBodyStrategiesConfigTargets] = None,
        cycle_start_time: int = None,
        ecs_count: int = None,
        process_rate: int = None,
        cycle_days: int = None,
        risk_count: int = None,
        name: str = None,
        pass_rate: int = None,
        id: int = None,
    ):
        self.exec_status = exec_status
        self.type = type
        self.config_targets = config_targets
        self.cycle_start_time = cycle_start_time
        self.ecs_count = ecs_count
        self.process_rate = process_rate
        self.cycle_days = cycle_days
        self.risk_count = risk_count
        self.name = name
        self.pass_rate = pass_rate
        self.id = id

    def validate(self):
        if self.config_targets:
            for k in self.config_targets:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.exec_status is not None:
            result['ExecStatus'] = self.exec_status
        if self.type is not None:
            result['Type'] = self.type
        result['ConfigTargets'] = []
        if self.config_targets is not None:
            for k in self.config_targets:
                result['ConfigTargets'].append(k.to_map() if k else None)
        if self.cycle_start_time is not None:
            result['CycleStartTime'] = self.cycle_start_time
        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count
        if self.process_rate is not None:
            result['ProcessRate'] = self.process_rate
        if self.cycle_days is not None:
            result['CycleDays'] = self.cycle_days
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.name is not None:
            result['Name'] = self.name
        if self.pass_rate is not None:
            result['PassRate'] = self.pass_rate
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecStatus') is not None:
            self.exec_status = m.get('ExecStatus')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.config_targets = []
        if m.get('ConfigTargets') is not None:
            for k in m.get('ConfigTargets'):
                temp_model = DescribeStratetyResponseBodyStrategiesConfigTargets()
                self.config_targets.append(temp_model.from_map(k))
        if m.get('CycleStartTime') is not None:
            self.cycle_start_time = m.get('CycleStartTime')
        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')
        if m.get('ProcessRate') is not None:
            self.process_rate = m.get('ProcessRate')
        if m.get('CycleDays') is not None:
            self.cycle_days = m.get('CycleDays')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassRate') is not None:
            self.pass_rate = m.get('PassRate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeStratetyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        strategies: List[DescribeStratetyResponseBodyStrategies] = None,
    ):
        self.request_id = request_id
        self.strategies = strategies

    def validate(self):
        if self.strategies:
            for k in self.strategies:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Strategies'] = []
        if self.strategies is not None:
            for k in self.strategies:
                result['Strategies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.strategies = []
        if m.get('Strategies') is not None:
            for k in m.get('Strategies'):
                temp_model = DescribeStratetyResponseBodyStrategies()
                self.strategies.append(temp_model.from_map(k))
        return self


class DescribeStratetyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStratetyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeStratetyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulWhitelistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeVulWhitelistResponseBodyVulWhitelists(TeaModel):
    def __init__(
        self,
        type: str = None,
        alias_name: str = None,
        name: str = None,
        reason: str = None,
    ):
        self.type = type
        self.alias_name = alias_name
        self.name = name
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class DescribeVulWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        vul_whitelists: List[DescribeVulWhitelistResponseBodyVulWhitelists] = None,
        current_page: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.vul_whitelists = vul_whitelists
        self.current_page = current_page

    def validate(self):
        if self.vul_whitelists:
            for k in self.vul_whitelists:
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
        result['VulWhitelists'] = []
        if self.vul_whitelists is not None:
            for k in self.vul_whitelists:
                result['VulWhitelists'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.vul_whitelists = []
        if m.get('VulWhitelists') is not None:
            for k in m.get('VulWhitelists'):
                temp_model = DescribeVulWhitelistResponseBodyVulWhitelists()
                self.vul_whitelists.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeVulWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVulWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVulWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        client_token: str = None,
        instance_id: str = None,
        vm_number: str = None,
        duration: int = None,
        pricing_cycle: str = None,
    ):
        self.owner_id = owner_id
        self.client_token = client_token
        self.instance_id = instance_id
        self.vm_number = vm_number
        self.duration = duration
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vm_number is not None:
            result['VmNumber'] = self.vm_number
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VmNumber') is not None:
            self.vm_number = m.get('VmNumber')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        client_token: str = None,
        instance_id: str = None,
        version_code: int = None,
        vm_number: int = None,
    ):
        self.owner_id = owner_id
        self.client_token = client_token
        self.instance_id = instance_id
        self.version_code = version_code
        self.vm_number = vm_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.vm_number is not None:
            result['VmNumber'] = self.vm_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VmNumber') is not None:
            self.vm_number = m.get('VmNumber')
        return self


class UpgradeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class UpgradeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


